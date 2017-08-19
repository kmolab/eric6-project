# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to browse the log history.
"""

from __future__ import unicode_literals
try:
    str = unicode
except NameError:
    pass

import os
import re
import collections

from PyQt5.QtCore import pyqtSlot, Qt, QDate, QProcess, QTimer, QRegExp, \
    QSize, QPoint, QFileInfo
from PyQt5.QtGui import QCursor, QColor, QPixmap, QPainter, QPen, QBrush, \
    QIcon, QTextCursor
from PyQt5.QtWidgets import QWidget, QDialogButtonBox, QHeaderView, \
    QTreeWidgetItem, QApplication, QLineEdit, QMenu, QInputDialog, QToolTip

from E5Gui.E5Application import e5App
from E5Gui import E5MessageBox, E5FileDialog

from .Ui_HgLogBrowserDialog import Ui_HgLogBrowserDialog

from .HgDiffHighlighter import HgDiffHighlighter
from .HgDiffGenerator import HgDiffGenerator

import UI.PixmapCache
import Preferences
import Utilities
from Globals import qVersionTuple

COLORNAMES = ["blue", "darkgreen", "red", "green", "darkblue", "purple",
              "cyan", "olive", "magenta", "darkred", "darkmagenta",
              "darkcyan", "gray", "yellow"]
COLORS = [str(QColor(x).name()) for x in COLORNAMES]


class HgLogBrowserDialog(QWidget, Ui_HgLogBrowserDialog):
    """
    Class implementing a dialog to browse the log history.
    """
    IconColumn = 0
    BranchColumn = 1
    RevisionColumn = 2
    PhaseColumn = 3
    AuthorColumn = 4
    DateColumn = 5
    MessageColumn = 6
    TagsColumn = 7
    BookmarksColumn = 8
    
    LargefilesCacheL = ".hglf/"
    LargefilesCacheW = ".hglf\\"
    PathSeparatorRe = re.compile(r"/|\\")
    
    ClosedIndicator = " \u2612"
    
    def __init__(self, vcs, mode="log", parent=None):
        """
        Constructor
        
        @param vcs reference to the vcs object
        @param mode mode of the dialog (string; one of log, incoming, outgoing)
        @param parent parent widget (QWidget)
        """
        super(HgLogBrowserDialog, self).__init__(parent)
        self.setupUi(self)
        
        windowFlags = self.windowFlags()
        windowFlags |= Qt.WindowContextHelpButtonHint
        self.setWindowFlags(windowFlags)
        
        self.mainSplitter.setSizes([300, 400])
        self.mainSplitter.setStretchFactor(0, 1)
        self.mainSplitter.setStretchFactor(1, 2)
        self.diffSplitter.setStretchFactor(0, 1)
        self.diffSplitter.setStretchFactor(1, 2)
        
        if mode == "log":
            self.setWindowTitle(self.tr("Mercurial Log"))
        elif mode == "incoming":
            self.setWindowTitle(self.tr("Mercurial Log (Incoming)"))
        elif mode == "outgoing":
            self.setWindowTitle(self.tr("Mercurial Log (Outgoing)"))
        
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)
        
        self.filesTree.headerItem().setText(self.filesTree.columnCount(), "")
        self.filesTree.header().setSortIndicator(0, Qt.AscendingOrder)
        
        self.upButton.setIcon(UI.PixmapCache.getIcon("1uparrow.png"))
        self.downButton.setIcon(UI.PixmapCache.getIcon("1downarrow.png"))
        
        self.refreshButton = self.buttonBox.addButton(
            self.tr("&Refresh"), QDialogButtonBox.ActionRole)
        self.refreshButton.setToolTip(
            self.tr("Press to refresh the list of changesets"))
        self.refreshButton.setEnabled(False)
        
        self.findPrevButton.setIcon(UI.PixmapCache.getIcon("1leftarrow.png"))
        self.findNextButton.setIcon(UI.PixmapCache.getIcon("1rightarrow.png"))
        self.__findBackwards = False
        
        self.modeComboBox.addItem(self.tr("Find"), "find")
        self.modeComboBox.addItem(self.tr("Filter"), "filter")
        
        self.fieldCombo.addItem(self.tr("Revision"), "revision")
        self.fieldCombo.addItem(self.tr("Author"), "author")
        self.fieldCombo.addItem(self.tr("Message"), "message")
        self.fieldCombo.addItem(self.tr("File"), "file")
        
        font = Preferences.getEditorOtherFonts("MonospacedFont")
        self.diffEdit.setFontFamily(font.family())
        self.diffEdit.setFontPointSize(font.pointSize())
        
        self.diffHighlighter = HgDiffHighlighter(self.diffEdit.document())
        self.__diffGenerator = HgDiffGenerator(vcs, self)
        self.__diffGenerator.finished.connect(self.__generatorFinished)
        
        self.vcs = vcs
        if mode in ("log", "incoming", "outgoing"):
            self.commandMode = mode
            self.initialCommandMode = mode
        else:
            self.commandMode = "log"
            self.initialCommandMode = "log"
        self.__hgClient = vcs.getClient()
        
        self.__detailsTemplate = self.tr(
            "<table>"
            "<tr><td><b>Revision</b></td><td>{0}</td></tr>"
            "<tr><td><b>Date</b></td><td>{1}</td></tr>"
            "<tr><td><b>Author</b></td><td>{2}</td></tr>"
            "<tr><td><b>Branch</b></td><td>{3}</td></tr>"
            "{4}"
            "<tr><td><b>Message</b></td><td>{5}</td></tr>"
            "</table>"
        )
        self.__parentsTemplate = self.tr(
            "<tr><td><b>Parents</b></td><td>{0}</td></tr>"
        )
        self.__childrenTemplate = self.tr(
            "<tr><td><b>Children</b></td><td>{0}</td></tr>"
        )
        self.__tagsTemplate = self.tr(
            "<tr><td><b>Tags</b></td><td>{0}</td></tr>"
        )
        self.__latestTagTemplate = self.tr(
            "<tr><td><b>Latest Tag</b></td><td>{0}</td></tr>"
        )
        self.__bookmarksTemplate = self.tr(
            "<tr><td><b>Bookmarks</b></td><td>{0}</td></tr>"
        )
        
        self.__bundle = ""
        self.__filename = ""
        self.__isFile = False
        self.__selectedRevisions = []
        self.intercept = False
        
        self.__initData()
        
        self.__allBranchesFilter = self.tr("All")
        
        self.fromDate.setDisplayFormat("yyyy-MM-dd")
        self.toDate.setDisplayFormat("yyyy-MM-dd")
        self.__resetUI()
        
        # roles used in the log tree
        self.__messageRole = Qt.UserRole
        self.__changesRole = Qt.UserRole + 1
        self.__edgesRole = Qt.UserRole + 2
        self.__parentsRole = Qt.UserRole + 3
        self.__latestTagRole = Qt.UserRole + 4
        
        # roles used in the file tree
        self.__diffFileLineRole = Qt.UserRole
        
        if self.__hgClient:
            self.process = None
        else:
            self.process = QProcess()
            self.process.finished.connect(self.__procFinished)
            self.process.readyReadStandardOutput.connect(self.__readStdout)
            self.process.readyReadStandardError.connect(self.__readStderr)
        
        self.flags = {
            'A': self.tr('Added'),
            'D': self.tr('Deleted'),
            'M': self.tr('Modified'),
        }
        
        self.phases = {
            'draft': self.tr("Draft"),
            'public': self.tr("Public"),
            'secret': self.tr("Secret"),
        }
        
        self.__dotRadius = 8
        self.__rowHeight = 20
        
        self.logTree.setIconSize(
            QSize(100 * self.__rowHeight, self.__rowHeight))
        self.BookmarksColumn = self.logTree.columnCount()
        self.logTree.headerItem().setText(
            self.BookmarksColumn, self.tr("Bookmarks"))
        
        self.__logTreeNormalFont = self.logTree.font()
        self.__logTreeNormalFont.setBold(False)
        self.__logTreeBoldFont = self.logTree.font()
        self.__logTreeBoldFont.setBold(True)
        
        self.detailsEdit.anchorClicked.connect(self.__revisionClicked)
        
        self.__initActionsMenu()
        
        self.__finishCallbacks = []
    
    def __addFinishCallback(self, callback):
        """
        Private method to add a method to be called once the process finished.
        
        The callback methods are invoke in a FIFO style and are consumed. If
        a callback method needs to be called again, it must be added again.
        
        @param callback callback method
        @type function
        """
        if callback not in self.__finishCallbacks:
            self.__finishCallbacks.append(callback)
    
    def __initActionsMenu(self):
        """
        Private method to initialize the actions menu.
        """
        self.__actionsMenu = QMenu()
        self.__actionsMenu.setTearOffEnabled(True)
        if qVersionTuple() >= (5, 1, 0):
            self.__actionsMenu.setToolTipsVisible(True)
        else:
            self.__actionsMenu.hovered.connect(self.__actionsMenuHovered)
        
        self.__graftAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsGraft.png"),
            self.tr("Copy Changesets"), self.__graftActTriggered)
        self.__graftAct.setToolTip(self.tr(
            "Copy the selected changesets to the current branch"))
        
        self.__mergeAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsMerge.png"),
            self.tr("Merge with Changeset"), self.__mergeActTriggered)
        self.__mergeAct.setToolTip(self.tr(
            "Merge the working directory with the selected changeset"))
        
        self.__phaseAct = self.__actionsMenu.addAction(
            self.tr("Change Phase"), self.__phaseActTriggered)
        self.__phaseAct.setToolTip(self.tr(
            "Change the phase of the selected revisions"))
        self.__phaseAct.setWhatsThis(self.tr(
            """<b>Change Phase</b>\n<p>This changes the phase of the"""
            """ selected revisions. The selected revisions have to have"""
            """ the same current phase.</p>"""))
        
        self.__tagAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsTag.png"), self.tr("Tag"),
            self.__tagActTriggered)
        self.__tagAct.setToolTip(self.tr("Tag the selected revision"))
        
        self.__switchAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsSwitch.png"), self.tr("Switch"),
            self.__switchActTriggered)
        self.__switchAct.setToolTip(self.tr(
            "Switch the working directory to the selected revision"))
        
        self.__actionsMenu.addSeparator()
        
        self.__bookmarkAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("addBookmark.png"),
            self.tr("Define Bookmark..."), self.__bookmarkActTriggered)
        self.__bookmarkAct.setToolTip(
            self.tr("Bookmark the selected revision"))
        self.__bookmarkMoveAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("moveBookmark.png"),
            self.tr("Move Bookmark..."), self.__bookmarkMoveActTriggered)
        self.__bookmarkMoveAct.setToolTip(
            self.tr("Move bookmark to the selected revision"))
        
        self.__actionsMenu.addSeparator()
        
        self.__pullAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsUpdate.png"), self.tr("Pull Changes"),
            self.__pullActTriggered)
        self.__pullAct.setToolTip(self.tr(
            "Pull changes from a remote repository"))
        self.__lfPullAct = self.__actionsMenu.addAction(
            self.tr("Pull Large Files"), self.__lfPullActTriggered)
        self.__lfPullAct.setToolTip(self.tr(
            "Pull large files for selected revisions"))
        self.__fetchAct = self.__actionsMenu.addAction(
            self.tr("Fetch Changes"), self.__fetchActTriggered)
        self.__fetchAct.setToolTip(self.tr(
            "Fetch changes from a remote repository"))
        
        self.__actionsMenu.addSeparator()
        
        self.__pushAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsCommit.png"),
            self.tr("Push Selected Changes"), self.__pushActTriggered)
        self.__pushAct.setToolTip(self.tr(
            "Push changes of the selected changeset and its ancestors"
            " to a remote repository"))
        self.__pushAllAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsCommit.png"),
            self.tr("Push All Changes"), self.__pushAllActTriggered)
        self.__pushAllAct.setToolTip(self.tr(
            "Push all changes to a remote repository"))
        
        self.__actionsMenu.addSeparator()
        
        self.__bundleAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsCreateChangegroup.png"),
            self.tr("Create Changegroup"), self.__bundleActTriggered)
        self.__bundleAct.setToolTip(self.tr(
            "Create a changegroup file containing the selected changesets"))
        self.__bundleAct.setWhatsThis(self.tr(
            """<b>Create Changegroup</b>\n<p>This creates a changegroup"""
            """ file containing the selected revisions. If no revisions"""
            """ are selected, all changesets will be bundled. If one"""
            """ revision is selected, it will be interpreted as the base"""
            """ revision. Otherwise the lowest revision will be used as"""
            """ the base revision and all other revision will be bundled."""
            """ If the dialog is showing outgoing changesets, all"""
            """ selected changesets will be bundled.</p>"""))
        self.__unbundleAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("vcsApplyChangegroup.png"),
            self.tr("Apply Changegroup"), self.__unbundleActTriggered)
        self.__unbundleAct.setToolTip(self.tr(
            "Apply the currently viewed changegroup file"))
        
        self.__actionsMenu.addSeparator()
        
        self.__gpgSignAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("changesetSign.png"),
            self.tr("Sign Revisions"), self.__gpgSignActTriggered)
        self.__gpgSignAct.setToolTip(self.tr(
            "Add a signature for the selected revisions"))
        self.__gpgVerifyAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("changesetSignVerify.png"),
            self.tr("Verify Signatures"), self.__gpgVerifyActTriggered)
        self.__gpgVerifyAct.setToolTip(self.tr(
            "Verify all signatures there may be for the selected revision"))
        
        self.__actionsMenu.addSeparator()
        
        self.__stripAct = self.__actionsMenu.addAction(
            UI.PixmapCache.getIcon("fileDelete.png"),
            self.tr("Strip Changesets"), self.__stripActTriggered)
        self.__stripAct.setToolTip(self.tr(
            "Strip changesets from a repository"))
        
        self.__actionsMenu.addSeparator()
        
        self.__selectAllAct = self.__actionsMenu.addAction(
            self.tr("Select All Entries"), self.__selectAllActTriggered)
        self.__unselectAllAct = self.__actionsMenu.addAction(
            self.tr("Deselect All Entries"),
            lambda: self.__selectAllActTriggered(False))
        
        self.actionsButton.setIcon(
            UI.PixmapCache.getIcon("actionsToolButton.png"))
        self.actionsButton.setMenu(self.__actionsMenu)
    
    def __actionsMenuHovered(self, action):
        """
        Private slot to show the tooltip for an action menu entry.
        
        @param action action to show tooltip for
        @type QAction
        """
        QToolTip.showText(
            QCursor.pos(), action.toolTip(),
            self.__actionsMenu, self.__actionsMenu.actionGeometry(action))
    
    def __initData(self):
        """
        Private method to (re-)initialize some data.
        """
        self.__maxDate = QDate()
        self.__minDate = QDate()
        self.__filterLogsEnabled = True
        
        self.buf = []        # buffer for stdout
        self.diff = None
        self.__started = False
        self.__lastRev = 0
        self.projectMode = False
        
        # attributes to store log graph data
        self.__revs = []
        self.__revColors = {}
        self.__revColor = 0
        
        self.__branchColors = {}
        
        self.__projectRevision = -1
        self.__projectBranch = ""
        
        self.__childrenInfo = collections.defaultdict(list)
    
    def closeEvent(self, e):
        """
        Protected slot implementing a close event handler.
        
        @param e close event (QCloseEvent)
        """
        if self.__hgClient:
            if self.__hgClient.isExecuting():
                self.__hgClient.cancel()
        else:
            if self.process is not None and \
               self.process.state() != QProcess.NotRunning:
                self.process.terminate()
                QTimer.singleShot(2000, self.process.kill)
                self.process.waitForFinished(3000)
        
        self.vcs.getPlugin().setPreferences(
            "LogBrowserGeometry", self.saveGeometry())
        self.vcs.getPlugin().setPreferences(
            "LogBrowserSplitterStates", [
                self.mainSplitter.saveState(),
                self.detailsSplitter.saveState(),
                self.diffSplitter.saveState(),
            ]
        )
        
        e.accept()
    
    def show(self):
        """
        Public slot to show the dialog.
        """
        self.__reloadGeometry()
        self.__restoreSplitterStates()
        self.__resetUI()
        
        super(HgLogBrowserDialog, self).show()

    def __reloadGeometry(self):
        """
        Private method to restore the geometry.
        """
        geom = self.vcs.getPlugin().getPreferences("LogBrowserGeometry")
        if geom.isEmpty():
            s = QSize(1000, 800)
            self.resize(s)
        else:
            self.restoreGeometry(geom)
    
    def __restoreSplitterStates(self):
        """
        Private method to restore the state of the various splitters.
        """
        states = self.vcs.getPlugin().getPreferences(
            "LogBrowserSplitterStates")
        if len(states) == 3:
            # we have three splitters
            self.mainSplitter.restoreState(states[0])
            self.detailsSplitter.restoreState(states[1])
            self.diffSplitter.restoreState(states[2])
    
    def __resetUI(self):
        """
        Private method to reset the user interface.
        """
        self.branchCombo.clear()
        self.fromDate.setDate(QDate.currentDate())
        self.toDate.setDate(QDate.currentDate())
        self.fieldCombo.setCurrentIndex(self.fieldCombo.findData("message"))
        self.limitSpinBox.setValue(self.vcs.getPlugin().getPreferences(
            "LogLimit"))
        self.stopCheckBox.setChecked(self.vcs.getPlugin().getPreferences(
            "StopLogOnCopy"))
        
        if self.initialCommandMode in ("incoming", "outgoing"):
            self.nextButton.setEnabled(False)
            self.limitSpinBox.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)
            self.limitSpinBox.setEnabled(True)
        
        self.logTree.clear()
        
        self.commandMode = self.initialCommandMode
    
    def __resizeColumnsLog(self):
        """
        Private method to resize the log tree columns.
        """
        self.logTree.header().resizeSections(QHeaderView.ResizeToContents)
        self.logTree.header().setStretchLastSection(True)
    
    def __resizeColumnsFiles(self):
        """
        Private method to resize the changed files tree columns.
        """
        self.filesTree.header().resizeSections(QHeaderView.ResizeToContents)
        self.filesTree.header().setStretchLastSection(True)
    
    def __resortFiles(self):
        """
        Private method to resort the changed files tree.
        """
        sortColumn = self.filesTree.sortColumn()
        self.filesTree.sortItems(
            1, self.filesTree.header().sortIndicatorOrder())
        self.filesTree.sortItems(
            sortColumn, self.filesTree.header().sortIndicatorOrder())
    
    def __getColor(self, n):
        """
        Private method to get the (rotating) name of the color given an index.
        
        @param n color index (integer)
        @return color name (string)
        """
        return COLORS[n % len(COLORS)]
    
    def __branchColor(self, branchName):
        """
        Private method to calculate a color for a given branch name.
        
        @param branchName name of the branch (string)
        @return name of the color to use (string)
        """
        if branchName not in self.__branchColors:
            self.__branchColors[branchName] = self.__getColor(
                len(self.__branchColors))
        return self.__branchColors[branchName]
    
    def __generateEdges(self, rev, parents):
        """
        Private method to generate edge info for the give data.
        
        @param rev revision to calculate edge info for (integer)
        @param parents list of parent revisions (list of integers)
        @return tuple containing the column and color index for
            the given node and a list of tuples indicating the edges
            between the given node and its parents
            (integer, integer, [(integer, integer, integer), ...])
        """
        if rev not in self.__revs:
            # new head
            self.__revs.append(rev)
            self.__revColors[rev] = self.__revColor
            self.__revColor += 1
        
        col = self.__revs.index(rev)
        color = self.__revColors.pop(rev)
        nextRevs = self.__revs[:]
        
        # add parents to next
        addparents = [p for p in parents if p not in nextRevs]
        nextRevs[col:col + 1] = addparents
        
        # set colors for the parents
        for i, p in enumerate(addparents):
            if not i:
                self.__revColors[p] = color
            else:
                self.__revColors[p] = self.__revColor
                self.__revColor += 1
        
        # add edges to the graph
        edges = []
        if parents[0] != -1:
            for ecol, erev in enumerate(self.__revs):
                if erev in nextRevs:
                    edges.append(
                        (ecol, nextRevs.index(erev), self.__revColors[erev]))
                elif erev == rev:
                    for p in parents:
                        edges.append(
                            (ecol, nextRevs.index(p), self.__revColors[p]))
        
        self.__revs = nextRevs
        return col, color, edges
    
    def __generateIcon(self, column, color, bottomedges, topedges, dotColor,
                       currentRev, closed):
        """
        Private method to generate an icon containing the revision tree for the
        given data.
        
        @param column column index of the revision (integer)
        @param color color of the node (integer)
        @param bottomedges list of edges for the bottom of the node
            (list of tuples of three integers)
        @param topedges list of edges for the top of the node
            (list of tuples of three integers)
        @param dotColor color to be used for the dot (QColor)
        @param currentRev flag indicating to draw the icon for the
            current revision (boolean)
        @param closed flag indicating to draw an icon for a closed
            branch (boolean)
        @return icon for the node (QIcon)
        """
        def col2x(col, radius):
            """
            Local function to calculate a x-position for a column.
            
            @param col column number (integer)
            @param radius radius of the indicator circle (integer)
            """
            return int(1.2 * radius) * col + radius // 2 + 3
        
        radius = self.__dotRadius
        w = len(bottomedges) * radius + 20
        h = self.__rowHeight
        
        dot_x = col2x(column, radius) - radius // 2
        dot_y = h // 2
        
        pix = QPixmap(w, h)
        pix.fill(QColor(0, 0, 0, 0))
        painter = QPainter(pix)
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen(Qt.blue)
        pen.setWidth(2)
        painter.setPen(pen)
        
        lpen = QPen(pen)
        lpen.setColor(Qt.black)
        painter.setPen(lpen)
        
        # draw the revision history lines
        for y1, y2, lines in ((0, h, bottomedges),
                              (-h, 0, topedges)):
            if lines:
                for start, end, ecolor in lines:
                    lpen = QPen(pen)
                    lpen.setColor(QColor(self.__getColor(ecolor)))
                    lpen.setWidth(2)
                    painter.setPen(lpen)
                    x1 = col2x(start, radius)
                    x2 = col2x(end, radius)
                    painter.drawLine(x1, dot_y + y1, x2, dot_y + y2)
        
        penradius = 1
        pencolor = Qt.black
        
        dot_y = (h // 2) - radius // 2
        
        # draw a dot for the revision
        if currentRev:
            # enlarge dot for the current revision
            delta = 1
            radius += 2 * delta
            dot_y -= delta
            dot_x -= delta
            penradius = 3
        painter.setBrush(dotColor)
        pen = QPen(pencolor)
        pen.setWidth(penradius)
        painter.setPen(pen)
        if closed:
            painter.drawRect(dot_x - 2, dot_y + 1,
                             radius + 4, radius - 2)
        elif self.commandMode in ("incoming", "outgoing"):
            offset = radius // 2
            painter.drawConvexPolygon(
                QPoint(dot_x + offset, dot_y),
                QPoint(dot_x, dot_y + offset),
                QPoint(dot_x + offset, dot_y + 2 * offset),
                QPoint(dot_x + 2 * offset, dot_y + offset)
            )
        else:
            painter.drawEllipse(dot_x, dot_y, radius, radius)
        painter.end()
        return QIcon(pix)
    
    def __getParents(self, rev):
        """
        Private method to get the parents of the currently viewed
        file/directory.
        
        @param rev revision number to get parents for (string)
        @return list of parent revisions (list of integers)
        """
        errMsg = ""
        parents = [-1]
        
        if int(rev) > 0:
            args = self.vcs.initCommand("parents")
            if self.commandMode == "incoming":
                if self.__bundle:
                    args.append("--repository")
                    args.append(self.__bundle)
                elif self.vcs.bundleFile and \
                        os.path.exists(self.vcs.bundleFile):
                    args.append("--repository")
                    args.append(self.vcs.bundleFile)
            args.append("--template")
            args.append("{rev}\n")
            args.append("-r")
            args.append(rev)
            if not self.projectMode:
                args.append(self.__filename)
            
            output = ""
            if self.__hgClient:
                output, errMsg = self.__hgClient.runcommand(args)
            else:
                process = QProcess()
                process.setWorkingDirectory(self.repodir)
                process.start('hg', args)
                procStarted = process.waitForStarted(5000)
                if procStarted:
                    finished = process.waitForFinished(30000)
                    if finished and process.exitCode() == 0:
                        output = str(process.readAllStandardOutput(),
                                     self.vcs.getEncoding(), 'replace')
                    else:
                        if not finished:
                            errMsg = self.tr(
                                "The hg process did not finish within 30s.")
                else:
                    errMsg = self.tr("Could not start the hg executable.")
                
                if errMsg:
                    E5MessageBox.critical(
                        self,
                        self.tr("Mercurial Error"),
                        errMsg)
            
            if output:
                parents = [int(p) for p in output.strip().splitlines()]
        
        return parents
    
    def __identifyProject(self):
        """
        Private method to determine the revision of the project directory.
        """
        errMsg = ""
        
        args = self.vcs.initCommand("identify")
        args.append("-nb")
        
        output = ""
        if self.__hgClient:
            output, errMsg = self.__hgClient.runcommand(args)
        else:
            process = QProcess()
            process.setWorkingDirectory(self.repodir)
            process.start('hg', args)
            procStarted = process.waitForStarted(5000)
            if procStarted:
                finished = process.waitForFinished(30000)
                if finished and process.exitCode() == 0:
                    output = str(process.readAllStandardOutput(),
                                 self.vcs.getEncoding(), 'replace')
                else:
                    if not finished:
                        errMsg = self.tr(
                            "The hg process did not finish within 30s.")
            else:
                errMsg = self.tr("Could not start the hg executable.")
        
        if errMsg:
            E5MessageBox.critical(
                self,
                self.tr("Mercurial Error"),
                errMsg)
        
        if output:
            outputList = output.strip().split(None, 1)
            if len(outputList) == 2:
                self.__projectRevision = outputList[0].strip()
                if self.__projectRevision.endswith("+"):
                    self.__projectRevision = self.__projectRevision[:-1]
                self.__projectBranch = outputList[1].strip()
    
    def __getClosedBranches(self):
        """
        Private method to get the list of closed branches.
        """
        self.__closedBranchesRevs = []
        errMsg = ""
        
        args = self.vcs.initCommand("branches")
        args.append("--closed")
        
        output = ""
        if self.__hgClient:
            output, errMsg = self.__hgClient.runcommand(args)
        else:
            process = QProcess()
            process.setWorkingDirectory(self.repodir)
            process.start('hg', args)
            procStarted = process.waitForStarted(5000)
            if procStarted:
                finished = process.waitForFinished(30000)
                if finished and process.exitCode() == 0:
                    output = str(process.readAllStandardOutput(),
                                 self.vcs.getEncoding(), 'replace')
                else:
                    if not finished:
                        errMsg = self.tr(
                            "The hg process did not finish within 30s.")
            else:
                errMsg = self.tr("Could not start the hg executable.")
        
        if errMsg:
            E5MessageBox.critical(
                self,
                self.tr("Mercurial Error"),
                errMsg)
        
        if output:
            for line in output.splitlines():
                if line.strip().endswith("(closed)"):
                    parts = line.split()
                    self.__closedBranchesRevs.append(
                        parts[-2].split(":", 1)[0])
    
    def __getRevisionOfTag(self, tag):
        """
        Private method to get the revision of a tag.
        
        @param tag tag name
        @type str
        @return tuple containing the revision and changeset ID
        @rtype tuple of (str, str)
        """
        errMsg = ""
        
        args = self.vcs.initCommand("tags")
        
        output = ""
        if self.__hgClient:
            output, errMsg = self.__hgClient.runcommand(args)
        else:
            process = QProcess()
            process.setWorkingDirectory(self.repodir)
            process.start('hg', args)
            procStarted = process.waitForStarted(5000)
            if procStarted:
                finished = process.waitForFinished(30000)
                if finished and process.exitCode() == 0:
                    output = str(process.readAllStandardOutput(),
                                 self.vcs.getEncoding(), 'replace')
                else:
                    if not finished:
                        errMsg = self.tr(
                            "The hg process did not finish within 30s.")
            else:
                errMsg = self.tr("Could not start the hg executable.")
        
        if errMsg:
            E5MessageBox.critical(
                self,
                self.tr("Mercurial Error"),
                errMsg)
        
        res = ("", "")
        if output:
            for line in output.splitlines():
                if line.strip():
                    try:
                        name, rev = line.strip().rsplit(None, 1)
                        if name == tag:
                            res = tuple(rev.split(":", 1))
                            break
                    except ValueError:
                        # ignore silently
                        pass
        
        return res
    
    def __generateLogItem(self, author, date, message, revision, changedPaths,
                          parents, branches, tags, phase, bookmarks,
                          latestTag):
        """
        Private method to generate a log tree entry.
        
        @param author author info (string)
        @param date date info (string)
        @param message text of the log message (list of strings)
        @param revision revision info (string)
        @param changedPaths list of dictionary objects containing
            info about the changed files/directories
        @param parents list of parent revisions (list of integers)
        @param branches list of branches (list of strings)
        @param tags list of tags (string)
        @param phase phase of the entry (string)
        @param bookmarks list of bookmarks (string)
        @param latestTag the latest tag(s) reachable from the changeset
            (list of strings)
        @return reference to the generated item (QTreeWidgetItem)
        """
        logMessageColumnWidth = self.vcs.getPlugin().getPreferences(
            "LogMessageColumnWidth")
        msgtxt = ""
        for line in message:
            if ". " in line:
                msgtxt += " " + line.strip().split(". ", 1)[0] + "."
                break
            else:
                msgtxt += " " + line.strip()
        if len(msgtxt) > logMessageColumnWidth:
            msgtxt = "{0}...".format(msgtxt[:logMessageColumnWidth])
        
        rev, node = revision.split(":")
        if rev in self.__closedBranchesRevs:
            closedStr = self.ClosedIndicator
        else:
            closedStr = ""
        if phase in self.phases:
            phaseStr = self.phases[phase]
        else:
            phaseStr = phase
        columnLabels = [
            "",
            branches[0] + closedStr,
            "{0:>7}:{1}".format(rev, node),
            phaseStr,
            author,
            date,
            msgtxt,
            ", ".join(tags),
        ]
        if bookmarks is not None:
            columnLabels.append(", ".join(bookmarks))
        itm = QTreeWidgetItem(self.logTree, columnLabels)
        
        itm.setForeground(self.BranchColumn,
                          QBrush(QColor(self.__branchColor(branches[0]))))
        
        if not self.projectMode:
            parents = self.__getParents(rev)
        if not parents:
            parents = [int(rev) - 1]
        column, color, edges = self.__generateEdges(int(rev), parents)
        
        itm.setData(0, self.__messageRole, message)
        itm.setData(0, self.__changesRole, changedPaths)
        itm.setData(0, self.__edgesRole, edges)
        itm.setData(0, self.__latestTagRole, latestTag)
        if parents == [-1]:
            itm.setData(0, self.__parentsRole, [])
        else:
            itm.setData(0, self.__parentsRole, parents)
            for parent in parents:
                self.__childrenInfo[parent].append(int(rev))
        
        if self.logTree.topLevelItemCount() > 1:
            topedges = \
                self.logTree.topLevelItem(
                    self.logTree.indexOfTopLevelItem(itm) - 1)\
                .data(0, self.__edgesRole)
        else:
            topedges = None
        
        icon = self.__generateIcon(column, color, edges, topedges,
                                   QColor(self.__branchColor(branches[0])),
                                   rev == self.__projectRevision,
                                   rev in self.__closedBranchesRevs)
        itm.setIcon(0, icon)
        
        try:
            self.__lastRev = int(revision.split(":")[0])
        except ValueError:
            self.__lastRev = 0
        
        return itm
    
    def __getLogEntries(self, startRev=None, noEntries=0):
        """
        Private method to retrieve log entries from the repository.
        
        @param startRev revision number to start from (integer, string)
        @keyparam noEntries number of entries to get (0 = default) (int)
        """
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Cancel).setEnabled(True)
        self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)
        QApplication.processEvents()
        
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QApplication.processEvents()
        
        self.buf = []
        self.cancelled = False
        self.errors.clear()
        self.intercept = False
        
        if noEntries == 0:
            noEntries = self.limitSpinBox.value()
        
        preargs = []
        args = self.vcs.initCommand(self.commandMode)
        args.append('--verbose')
        if self.commandMode not in ("incoming", "outgoing"):
            args.append('--limit')
            args.append(str(noEntries))
        if self.commandMode in ("incoming", "outgoing"):
            args.append("--newest-first")
            if self.vcs.hasSubrepositories():
                args.append("--subrepos")
        if startRev is not None:
            args.append('--rev')
            args.append('{0}:0'.format(startRev))
        if not self.projectMode and \
           not self.fname == "." and \
           not self.stopCheckBox.isChecked():
            args.append('--follow')
        if self.commandMode == "log":
            args.append('--copies')
        args.append('--template')
        args.append(os.path.join(os.path.dirname(__file__),
                                 "templates",
                                 "logBrowserBookmarkPhase.tmpl"))
        if self.commandMode == "incoming":
            if self.__bundle:
                args.append(self.__bundle)
            elif not self.vcs.hasSubrepositories():
                project = e5App().getObject("Project")
                self.vcs.bundleFile = os.path.join(
                    project.getProjectManagementDir(), "hg-bundle.hg")
                if os.path.exists(self.vcs.bundleFile):
                    os.remove(self.vcs.bundleFile)
                preargs = args[:]
                preargs.append("--quiet")
                preargs.append('--bundle')
                preargs.append(self.vcs.bundleFile)
                args.append(self.vcs.bundleFile)
        if not self.projectMode:
            args.append(self.__filename)
        
        if self.__hgClient:
            self.inputGroup.setEnabled(False)
            self.inputGroup.hide()
            
            if preargs:
                out, err = self.__hgClient.runcommand(preargs)
            else:
                err = ""
            if err:
                self.__showError(err)
            elif self.commandMode != "incoming" or \
                (self.vcs.bundleFile and
                 os.path.exists(self.vcs.bundleFile)) or \
                    self.__bundle:
                out, err = self.__hgClient.runcommand(args)
                self.buf = out.splitlines(True)
                if err:
                    self.__showError(err)
                self.__processBuffer()
            self.__finish()
        else:
            self.process.kill()
            
            self.process.setWorkingDirectory(self.repodir)
            
            if preargs:
                process = QProcess()
                process.setWorkingDirectory(self.repodir)
                process.start('hg', args)
                procStarted = process.waitForStarted(5000)
                if procStarted:
                    process.waitForFinished(30000)
            
            if self.commandMode != "incoming" or \
                (self.vcs.bundleFile and
                 os.path.exists(self.vcs.bundleFile)) or \
                    self.__bundle:
                self.process.start('hg', args)
                procStarted = self.process.waitForStarted(5000)
                if not procStarted:
                    self.inputGroup.setEnabled(False)
                    self.inputGroup.hide()
                    E5MessageBox.critical(
                        self,
                        self.tr('Process Generation Error'),
                        self.tr(
                            'The process {0} could not be started. '
                            'Ensure, that it is in the search path.'
                        ).format('hg'))
            else:
                self.__finish()
    
    def start(self, fn, bundle=None, isFile=False, noEntries=0):
        """
        Public slot to start the hg log command.
        
        @param fn filename to show the log for (string)
        @keyparam bundle name of a bundle file (string)
        @keyparam isFile flag indicating log for a file is to be shown
            (boolean)
        @keyparam noEntries number of entries to get (0 = default) (int)
        """
        self.__bundle = bundle
        self.__isFile = isFile
        
        self.sbsSelectLabel.clear()
        
        self.errorGroup.hide()
        QApplication.processEvents()
        
        self.__initData()
        
        self.__filename = fn
        self.dname, self.fname = self.vcs.splitPath(fn)
        
        # find the root of the repo
        self.repodir = self.dname
        while not os.path.isdir(os.path.join(self.repodir, self.vcs.adminDir)):
            self.repodir = os.path.dirname(self.repodir)
            if os.path.splitdrive(self.repodir)[1] == os.sep:
                return
        
        self.projectMode = (self.fname == "." and self.dname == self.repodir)
        self.stopCheckBox.setDisabled(self.projectMode or self.fname == ".")
        self.activateWindow()
        self.raise_()
        
        self.logTree.clear()
        self.__started = True
        self.__identifyProject()
        self.__getClosedBranches()
        self.__getLogEntries(noEntries=noEntries)
    
    def __procFinished(self, exitCode, exitStatus):
        """
        Private slot connected to the finished signal.
        
        @param exitCode exit code of the process (integer)
        @param exitStatus exit status of the process (QProcess.ExitStatus)
        """
        self.__processBuffer()
        self.__finish()
    
    def __finish(self):
        """
        Private slot called when the process finished or the user pressed
        the button.
        """
        if self.process is not None and \
           self.process.state() != QProcess.NotRunning:
            self.process.terminate()
            QTimer.singleShot(2000, self.process.kill)
            self.process.waitForFinished(3000)
        
        QApplication.restoreOverrideCursor()
        
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)
        self.buttonBox.button(QDialogButtonBox.Cancel).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Close).setDefault(True)
        
        self.inputGroup.setEnabled(False)
        self.inputGroup.hide()
        self.refreshButton.setEnabled(True)
        
        while self.__finishCallbacks:
            self.__finishCallbacks.pop(0)()
    
    def __modifyForLargeFiles(self, filename):
        """
        Private method to convert the displayed file name for a large file.
        
        @param filename file name to be processed (string)
        @return processed file name (string)
        """
        if filename.startswith((self.LargefilesCacheL, self.LargefilesCacheW)):
            return self.tr("{0} (large file)").format(
                self.PathSeparatorRe.split(filename, 1)[1])
        else:
            return filename
    
    def __processBuffer(self):
        """
        Private method to process the buffered output of the hg log command.
        """
        noEntries = 0
        log = {"message": [], "bookmarks": None, "phase": ""}
        changedPaths = []
        initialText = True
        fileCopies = {}
        for s in self.buf:
            if s != "@@@\n":
                try:
                    key, value = s.split("|", 1)
                except ValueError:
                    key = ""
                    value = s
                if key == "change":
                    initialText = False
                    log["revision"] = value.strip()
                elif key == "user":
                    log["author"] = value.strip()
                elif key == "parents":
                    log["parents"] = \
                        [int(x.split(":", 1)[0])
                         for x in value.strip().split()]
                elif key == "date":
                    log["date"] = " ".join(value.strip().split()[:2])
                elif key == "description":
                    log["message"].append(value.strip())
                elif key == "file_adds":
                    if value.strip():
                        for f in value.strip().split(", "):
                            if f in fileCopies:
                                changedPaths.append({
                                    "action": "A",
                                    "path": self.__modifyForLargeFiles(f),
                                    "copyfrom": self.__modifyForLargeFiles(
                                        fileCopies[f]),
                                })
                            else:
                                changedPaths.append({
                                    "action": "A",
                                    "path": self.__modifyForLargeFiles(f),
                                    "copyfrom": "",
                                })
                elif key == "files_mods":
                    if value.strip():
                        for f in value.strip().split(", "):
                            changedPaths.append({
                                "action": "M",
                                "path": self.__modifyForLargeFiles(f),
                                "copyfrom": "",
                            })
                elif key == "file_dels":
                    if value.strip():
                        for f in value.strip().split(", "):
                            changedPaths.append({
                                "action": "D",
                                "path": self.__modifyForLargeFiles(f),
                                "copyfrom": "",
                            })
                elif key == "file_copies":
                    if value.strip():
                        for entry in value.strip().split(", "):
                            newName, oldName = entry[:-1].split(" (")
                            fileCopies[newName] = oldName
                elif key == "branches":
                    if value.strip():
                        log["branches"] = value.strip().split(", ")
                    else:
                        log["branches"] = ["default"]
                elif key == "tags":
                    log["tags"] = value.strip().split(", ")
                elif key == "bookmarks":
                    log["bookmarks"] = value.strip().split(", ")
                elif key == "phase":
                    log["phase"] = value.strip()
                elif key == "latesttag":
                    tag = value.strip()
                    if tag == "null":
                        log["latesttag"] = []
                    elif ":" in tag:
                        log["latesttag"] = [
                            t.strip() for t in tag.split(":") if t.strip()]
                    else:
                        log["latesttag"] = [tag]
                else:
                    if initialText:
                        continue
                    if value.strip():
                        log["message"].append(value.strip())
            else:
                if len(log) > 1:
                    self.__generateLogItem(
                        log["author"], log["date"],
                        log["message"], log["revision"], changedPaths,
                        log["parents"], log["branches"], log["tags"],
                        log["phase"], log["bookmarks"], log["latesttag"])
                    dt = QDate.fromString(log["date"], Qt.ISODate)
                    if not self.__maxDate.isValid() and \
                       not self.__minDate.isValid():
                        self.__maxDate = dt
                        self.__minDate = dt
                    else:
                        if self.__maxDate < dt:
                            self.__maxDate = dt
                        if self.__minDate > dt:
                            self.__minDate = dt
                    noEntries += 1
                    log = {"message": [], "bookmarks": None, "phase": ""}
                    changedPaths = []
                    fileCopies = {}
        
        self.__resizeColumnsLog()
        
        if self.__started:
            if self.__selectedRevisions:
                foundItems = self.logTree.findItems(
                    self.__selectedRevisions[0], Qt.MatchExactly,
                    self.RevisionColumn)
                if foundItems:
                    self.logTree.setCurrentItem(foundItems[0])
                else:
                    self.logTree.setCurrentItem(self.logTree.topLevelItem(0))
            else:
                self.logTree.setCurrentItem(self.logTree.topLevelItem(0))
            self.__started = False
        
        if self.commandMode in ("incoming", "outgoing"):
            self.commandMode = "log"    # switch to log mode
            if self.__lastRev > 0:
                self.nextButton.setEnabled(True)
                self.limitSpinBox.setEnabled(True)
        else:
            if noEntries < self.limitSpinBox.value() and not self.cancelled:
                self.nextButton.setEnabled(False)
                self.limitSpinBox.setEnabled(False)
        
        # update the log filters
        self.__filterLogsEnabled = False
        self.fromDate.setMinimumDate(self.__minDate)
        self.fromDate.setMaximumDate(self.__maxDate)
        self.fromDate.setDate(self.__minDate)
        self.toDate.setMinimumDate(self.__minDate)
        self.toDate.setMaximumDate(self.__maxDate)
        self.toDate.setDate(self.__maxDate)
        
        branchFilter = self.branchCombo.currentText()
        if not branchFilter:
            branchFilter = self.__allBranchesFilter
        self.branchCombo.clear()
        self.branchCombo.addItems(
            [self.__allBranchesFilter] + sorted(self.__branchColors.keys()))
        self.branchCombo.setCurrentIndex(
            self.branchCombo.findText(branchFilter))
        
        self.__filterLogsEnabled = True
        if self.__actionMode() == "filter":
            self.__filterLogs()
        self.__updateToolMenuActions()
        
        # restore current item
        if self.__selectedRevisions:
            for revision in self.__selectedRevisions:
                items = self.logTree.findItems(
                    revision, Qt.MatchExactly, self.RevisionColumn)
                if items:
                    items[0].setSelected(True)
            self.__selectedRevisions = []
    
    def __readStdout(self):
        """
        Private slot to handle the readyReadStandardOutput signal.
        
        It reads the output of the process and inserts it into a buffer.
        """
        self.process.setReadChannel(QProcess.StandardOutput)
        
        while self.process.canReadLine():
            line = str(self.process.readLine(), self.vcs.getEncoding(),
                       'replace')
            self.buf.append(line)
    
    def __readStderr(self):
        """
        Private slot to handle the readyReadStandardError signal.
        
        It reads the error output of the process and inserts it into the
        error pane.
        """
        if self.process is not None:
            s = str(self.process.readAllStandardError(),
                    self.vcs.getEncoding(), 'replace')
            self.__showError(s)
    
    def __showError(self, out):
        """
        Private slot to show some error.
        
        @param out error to be shown (string)
        """
        self.errorGroup.show()
        self.errors.insertPlainText(out)
        self.errors.ensureCursorVisible()
        
        if not self.__hgClient:
            # show input in case the process asked for some input
            self.inputGroup.setEnabled(True)
            self.inputGroup.show()
    
    def on_buttonBox_clicked(self, button):
        """
        Private slot called by a button of the button box clicked.
        
        @param button button that was clicked (QAbstractButton)
        """
        if button == self.buttonBox.button(QDialogButtonBox.Close):
            self.close()
        elif button == self.buttonBox.button(QDialogButtonBox.Cancel):
            self.cancelled = True
            if self.__hgClient:
                self.__hgClient.cancel()
            else:
                self.__finish()
        elif button == self.refreshButton:
            self.on_refreshButton_clicked()
    
    def __updateSbsSelectLabel(self):
        """
        Private slot to update the enabled status of the diff buttons.
        """
        self.sbsSelectLabel.clear()
        if self.__isFile:
            selectedItems = self.logTree.selectedItems()
            if len(selectedItems) == 1:
                currentItem = selectedItems[0]
                rev2 = currentItem.text(self.RevisionColumn).split(":", 1)[0]\
                    .strip()
                parents = currentItem.data(0, self.__parentsRole)
                if parents:
                    parentLinks = []
                    for index in range(len(parents)):
                        parentLinks.append(
                            '<a href="sbsdiff:{0}_{1}">&nbsp;{2}&nbsp;</a>'
                            .format(parents[index], rev2, index + 1))
                    self.sbsSelectLabel.setText(
                        self.tr('Side-by-Side Diff to Parent {0}').format(
                            " ".join(parentLinks)))
            elif len(selectedItems) == 2:
                rev1 = int(selectedItems[0].text(self.RevisionColumn)
                           .split(":", 1)[0])
                rev2 = int(selectedItems[1].text(self.RevisionColumn)
                           .split(":", 1)[0])
                if rev1 > rev2:
                    # Swap the entries, so that rev1 < rev2
                    rev1, rev2 = rev2, rev1
                self.sbsSelectLabel.setText(self.tr(
                    '<a href="sbsdiff:{0}_{1}">Side-by-Side Compare</a>')
                    .format(rev1, rev2))
    
    def __updateToolMenuActions(self):
        """
        Private slot to update the status of the tool menu actions and
        the tool menu button.
        """
        if self.initialCommandMode == "log" and self.projectMode:
            # do the phase action
            # step 1: count entries with changeable phases
            secret = 0
            draft = 0
            public = 0
            for itm in self.logTree.selectedItems():
                phase = itm.text(self.PhaseColumn)
                if phase == self.phases["draft"]:
                    draft += 1
                elif phase == self.phases["secret"]:
                    secret += 1
                else:
                    public += 1
            
            # step 2: set the status of the phase action
            if public == 0 and \
               ((secret > 0 and draft == 0) or
                    (secret == 0 and draft > 0)):
                self.__phaseAct.setEnabled(True)
            else:
                self.__phaseAct.setEnabled(False)
            
            # do the graft action
            # step 1: count selected entries not belonging to the
            #         current branch
            otherBranches = 0
            for itm in self.logTree.selectedItems():
                branch = itm.text(self.BranchColumn)
                if branch != self.__projectBranch:
                    otherBranches += 1
            
            # step 2: set the status of the graft action
            self.__graftAct.setEnabled(otherBranches > 0)
            
            selectedItemsCount = len(self.logTree.selectedItems())
            self.__mergeAct.setEnabled(selectedItemsCount == 1)
            self.__tagAct.setEnabled(selectedItemsCount == 1)
            self.__switchAct.setEnabled(selectedItemsCount == 1)
            self.__bookmarkAct.setEnabled(selectedItemsCount == 1)
            self.__bookmarkMoveAct.setEnabled(selectedItemsCount == 1)
            
            self.__pullAct.setText(self.tr("Pull Changes"))
            self.__fetchAct.setText(self.tr("Fetch Changes"))
            if self.vcs.canPull():
                self.__pullAct.setEnabled(True)
                self.__lfPullAct.setEnabled(
                    self.vcs.isExtensionActive("largefiles") and
                    selectedItemsCount > 0)
                self.__fetchAct.setEnabled(
                    self.vcs.isExtensionActive("fetch"))
            else:
                self.__pullAct.setEnabled(False)
                self.__lfPullAct.setEnabled(False)
                self.__fetchAct.setEnabled(False)
            
            if self.vcs.canPush():
                self.__pushAct.setEnabled(
                    selectedItemsCount == 1 and
                    self.logTree.selectedItems()[0].text(self.PhaseColumn) ==
                    self.phases["draft"])
                self.__pushAllAct.setEnabled(True)
            else:
                self.__pushAct.setEnabled(False)
                self.__pushAllAct.setEnabled(False)
            
            self.__stripAct.setEnabled(
                self.vcs.isExtensionActive("strip") and
                selectedItemsCount == 1)
            
            self.__bundleAct.setEnabled(self.logTree.topLevelItemCount() > 0)
            self.__unbundleAct.setEnabled(False)
            
            self.__gpgSignAct.setEnabled(
                self.vcs.isExtensionActive("gpg") and
                selectedItemsCount > 0)
            self.__gpgVerifyAct.setEnabled(
                self.vcs.isExtensionActive("gpg") and
                selectedItemsCount == 1)
            
            self.actionsButton.setEnabled(True)
        
        elif self.initialCommandMode == "incoming" and self.projectMode:
            for act in [self.__phaseAct, self.__graftAct, self.__mergeAct,
                        self.__tagAct, self.__switchAct, self.__bookmarkAct,
                        self.__bookmarkMoveAct, self.__pushAct,
                        self.__pushAllAct, self.__stripAct, self.__bundleAct,
                        self.__gpgSignAct, self.__gpgVerifyAct]:
                act.setEnabled(False)
            
            self.__pullAct.setText(self.tr("Pull Selected Changes"))
            self.__fetchAct.setText(self.tr("Fetch Selected Changes"))
            if self.vcs.canPull():
                # step 1: determine number of selected draft changesets
                #         i.e. those that can be pulled
                selectedDraftItemsCount = 0
                for itm in self.logTree.selectedItems():
                    phase = itm.text(self.PhaseColumn)
                    if phase == self.phases["draft"]:
                        selectedDraftItemsCount += 1
                self.__pullAct.setEnabled(selectedDraftItemsCount > 0)
                self.__lfPullAct.setEnabled(
                    self.vcs.isExtensionActive("largefiles") and
                    selectedItemsCount > 0)
                self.__fetchAct.setEnabled(
                    self.vcs.isExtensionActive("fetch") and
                    selectedDraftItemsCount > 0)
            else:
                self.__pullAct.setEnabled(False)
                self.__lfPullAct.setEnabled(False)
                self.__fetchAct.setEnabled(False)
            
            self.__unbundleAct.setEnabled(bool(self.__bundle))
            
            self.actionsButton.setEnabled(True)
        
        elif self.initialCommandMode == "outgoing" and self.projectMode:
            for act in [self.__phaseAct, self.__graftAct, self.__mergeAct,
                        self.__tagAct, self.__switchAct, self.__bookmarkAct,
                        self.__bookmarkMoveAct, self.__pullAct,
                        self.__lfPullAct, self.__fetchAct, self.__stripAct,
                        self.__gpgSignAct, self.__gpgVerifyAct,
                        self.__unbundleAct]:
                act.setEnabled(False)
            
            selectedItemsCount = len(self.logTree.selectedItems())
            if self.vcs.canPush():
                self.__pushAct.setEnabled(
                    selectedItemsCount == 1 and
                    self.logTree.selectedItems()[0].text(self.PhaseColumn) ==
                    self.phases["draft"])
                self.__pushAllAct.setEnabled(True)
            else:
                self.__pushAct.setEnabled(False)
                self.__pushAllAct.setEnabled(False)
            
            self.__bundleAct.setEnabled(selectedItemsCount > 0)
        
        else:
            self.actionsButton.setEnabled(False)
    
    def __updateDetailsAndFiles(self):
        """
        Private slot to update the details and file changes panes.
        """
        self.detailsEdit.clear()
        self.filesTree.clear()
        self.__diffUpdatesFiles = False
        
        selectedItems = self.logTree.selectedItems()
        if len(selectedItems) == 1:
            self.detailsEdit.setHtml(
                self.__generateDetailsTableText(selectedItems[0]))
            self.__updateFilesTree(self.filesTree, selectedItems[0])
            self.__resizeColumnsFiles()
            self.__resortFiles()
        elif len(selectedItems) == 2:
            self.__diffUpdatesFiles = True
            index1 = self.logTree.indexOfTopLevelItem(selectedItems[0])
            index2 = self.logTree.indexOfTopLevelItem(selectedItems[1])
            if index1 > index2:
                # Swap the entries
                selectedItems[0], selectedItems[1] = \
                    selectedItems[1], selectedItems[0]
            html = "{0}<hr/>{1}".format(
                self.__generateDetailsTableText(selectedItems[0]),
                self.__generateDetailsTableText(selectedItems[1]),
            )
            self.detailsEdit.setHtml(html)
            # self.filesTree is updated by the diff
    
    def __generateDetailsTableText(self, itm):
        """
        Private method to generate an HTML table with the details of the given
        changeset.
        
        @param itm reference to the item the table should be based on
        @type QTreeWidgetItem
        @return HTML table containing details
        @rtype str
        """
        if itm is not None:
            if itm.text(self.TagsColumn):
                tagsStr = self.__tagsTemplate.format(itm.text(self.TagsColumn))
            else:
                tagsStr = ""
            
            if itm.text(self.BookmarksColumn):
                bookmarksStr = self.__bookmarksTemplate.format(
                    itm.text(self.BookmarksColumn))
            else:
                bookmarksStr = ""
            
            if self.projectMode and itm.data(0, self.__latestTagRole):
                latestTagLinks = []
                for tag in itm.data(0, self.__latestTagRole):
                    latestTagLinks.append('<a href="rev:{0}">{1}</a>'.format(
                        self.__getRevisionOfTag(tag)[0], tag))
                latestTagStr = self.__latestTagTemplate.format(
                    ", ".join(latestTagLinks))
            else:
                latestTagStr = ""
            
            rev = int(itm.text(self.RevisionColumn).split(":", 1)[0])
            
            if itm.data(0, self.__parentsRole):
                parentLinks = []
                for parent in [str(x) for x in
                               itm.data(0, self.__parentsRole)]:
                    parentLinks.append(
                        '<a href="rev:{0}">{0}</a>'.format(parent))
                parentsStr = self.__parentsTemplate.format(
                    ", ".join(parentLinks))
            else:
                parentsStr = ""
            
            if self.__childrenInfo[rev]:
                childLinks = []
                for child in [str(x) for x in self.__childrenInfo[rev]]:
                    childLinks.append(
                        '<a href="rev:{0}">{0}</a>'.format(child))
                childrenStr = self.__childrenTemplate.format(
                    ", ".join(childLinks))
            else:
                childrenStr = ""
            
            messageStr = "<br />\n".join([
                line.strip() for line in itm.data(0, self.__messageRole)
            ])
            
            html = self.__detailsTemplate.format(
                itm.text(self.RevisionColumn),
                itm.text(self.DateColumn),
                itm.text(self.AuthorColumn),
                itm.text(self.BranchColumn).replace(
                    self.ClosedIndicator, ""),
                parentsStr + childrenStr + tagsStr + latestTagStr +
                bookmarksStr,
                messageStr,
            )
        else:
            html = ""
        
        return html
    
    def __updateFilesTree(self, parent, itm):
        """
        Private method to update the files tree with changes of the given item.
        
        @param parent parent for the items to be added
        @type QTreeWidget or QTreeWidgetItem
        @param itm reference to the item the update should be based on
        @type QTreeWidgetItem
        """
        if itm is not None:
            changes = itm.data(0, self.__changesRole)
            if len(changes) > 0:
                for change in changes:
                    QTreeWidgetItem(parent, [
                        self.flags[change["action"]],
                        change["path"].strip(),
                        change["copyfrom"].strip(),
                    ])
    
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_logTree_currentItemChanged(self, current, previous):
        """
        Private slot called, when the current item of the log tree changes.
        
        @param current reference to the new current item (QTreeWidgetItem)
        @param previous reference to the old current item (QTreeWidgetItem)
        """
        self.__updateToolMenuActions()
        
        # Highlight the current entry using a bold font
        for col in range(self.logTree.columnCount()):
            current and current.setFont(col, self.__logTreeBoldFont)
            previous and previous.setFont(col, self.__logTreeNormalFont)
        
        # set the state of the up and down buttons
        self.upButton.setEnabled(
            current is not None and
            self.logTree.indexOfTopLevelItem(current) > 0)
        self.downButton.setEnabled(
            current is not None and
            int(current.text(self.RevisionColumn).split(":")[0]) > 0 and
            (self.logTree.indexOfTopLevelItem(current) <
                self.logTree.topLevelItemCount() - 1 or
             self.nextButton.isEnabled()))
    
    @pyqtSlot()
    def on_logTree_itemSelectionChanged(self):
        """
        Private slot called, when the selection has changed.
        """
        self.__updateDetailsAndFiles()
        self.__updateSbsSelectLabel()
        self.__updateToolMenuActions()
        self.__generateDiffs()
    
    @pyqtSlot()
    def on_upButton_clicked(self):
        """
        Private slot to move the current item up one entry.
        """
        itm = self.logTree.itemAbove(self.logTree.currentItem())
        if itm:
            self.logTree.setCurrentItem(itm)
    
    @pyqtSlot()
    def on_downButton_clicked(self):
        """
        Private slot to move the current item down one entry.
        """
        itm = self.logTree.itemBelow(self.logTree.currentItem())
        if itm:
            self.logTree.setCurrentItem(itm)
        else:
            # load the next bunch and try again
            if self.nextButton.isEnabled():
                self.__addFinishCallback(self.on_downButton_clicked)
                self.on_nextButton_clicked()
    
    @pyqtSlot()
    def on_nextButton_clicked(self):
        """
        Private slot to handle the Next button.
        """
        if self.__lastRev > 0 and self.nextButton.isEnabled():
            self.__getLogEntries(startRev=self.__lastRev - 1)
    
    @pyqtSlot(QDate)
    def on_fromDate_dateChanged(self, date):
        """
        Private slot called, when the from date changes.
        
        @param date new date (QDate)
        """
        if self.__actionMode() == "filter":
            self.__filterLogs()
    
    @pyqtSlot(QDate)
    def on_toDate_dateChanged(self, date):
        """
        Private slot called, when the from date changes.
        
        @param date new date (QDate)
        """
        if self.__actionMode() == "filter":
            self.__filterLogs()
    
    @pyqtSlot(str)
    def on_branchCombo_activated(self, txt):
        """
        Private slot called, when a new branch is selected.
        
        @param txt text of the selected branch (string)
        """
        if self.__actionMode() == "filter":
            self.__filterLogs()
    
    @pyqtSlot(str)
    def on_fieldCombo_activated(self, txt):
        """
        Private slot called, when a new filter field is selected.
        
        @param txt text of the selected field (string)
        """
        if self.__actionMode() == "filter":
            self.__filterLogs()
    
    @pyqtSlot(str)
    def on_rxEdit_textChanged(self, txt):
        """
        Private slot called, when a filter expression is entered.
        
        @param txt filter expression (string)
        """
        if self.__actionMode() == "filter":
            self.__filterLogs()
        elif self.__actionMode() == "find":
            self.__findItem(self.__findBackwards, interactive=True)
    
    @pyqtSlot()
    def on_rxEdit_returnPressed(self):
        """
        Private slot handling a press of the Return key in the rxEdit input.
        """
        if self.__actionMode() == "find":
            self.__findItem(self.__findBackwards, interactive=True)
    
    def __filterLogs(self):
        """
        Private method to filter the log entries.
        """
        if self.__filterLogsEnabled:
            from_ = self.fromDate.date().toString("yyyy-MM-dd")
            to_ = self.toDate.date().addDays(1).toString("yyyy-MM-dd")
            branch = self.branchCombo.currentText()
            closedBranch = branch + '--'
            fieldIndex, searchRx, indexIsRole = self.__prepareFieldSearch()
            
            visibleItemCount = self.logTree.topLevelItemCount()
            currentItem = self.logTree.currentItem()
            for topIndex in range(self.logTree.topLevelItemCount()):
                topItem = self.logTree.topLevelItem(topIndex)
                if indexIsRole:
                    if fieldIndex == self.__changesRole:
                        changes = topItem.data(0, self.__changesRole)
                        txt = "\n".join(
                            [c["path"] for c in changes] +
                            [c["copyfrom"] for c in changes]
                        )
                    else:
                        # Find based on complete message text
                        txt = "\n".join(topItem.data(0, self.__messageRole))
                else:
                    txt = topItem.text(fieldIndex)
                if topItem.text(self.DateColumn) <= to_ and \
                   topItem.text(self.DateColumn) >= from_ and \
                   (branch == self.__allBranchesFilter or
                    topItem.text(self.BranchColumn) in
                        [branch, closedBranch]) and \
                   searchRx.indexIn(txt) > -1:
                    topItem.setHidden(False)
                    if topItem is currentItem:
                        self.on_logTree_currentItemChanged(topItem, None)
                else:
                    topItem.setHidden(True)
                    if topItem is currentItem:
                        self.filesTree.clear()
                    visibleItemCount -= 1
            self.logTree.header().setSectionHidden(
                self.IconColumn,
                visibleItemCount != self.logTree.topLevelItemCount())
    
    def __prepareFieldSearch(self):
        """
        Private slot to prepare the filed search data.
        
        @return tuple of field index, search expression and flag indicating
            that the field index is a data role (integer, string, boolean)
        """
        indexIsRole = False
        txt = self.fieldCombo.itemData(self.fieldCombo.currentIndex())
        if txt == "author":
            fieldIndex = self.AuthorColumn
            searchRx = QRegExp(self.rxEdit.text(), Qt.CaseInsensitive)
        elif txt == "revision":
            fieldIndex = self.RevisionColumn
            txt = self.rxEdit.text()
            if txt.startswith("^"):
                searchRx = QRegExp("^\s*{0}".format(txt[1:]),
                                   Qt.CaseInsensitive)
            else:
                searchRx = QRegExp(txt, Qt.CaseInsensitive)
        elif txt == "file":
            fieldIndex = self.__changesRole
            searchRx = QRegExp(self.rxEdit.text(), Qt.CaseInsensitive)
            indexIsRole = True
        else:
            fieldIndex = self.__messageRole
            searchRx = QRegExp(self.rxEdit.text(), Qt.CaseInsensitive)
            indexIsRole = True
        
        return fieldIndex, searchRx, indexIsRole
    
    @pyqtSlot(bool)
    def on_stopCheckBox_clicked(self, checked):
        """
        Private slot called, when the stop on copy/move checkbox is clicked.
        
        @param checked flag indicating the state of the check box (boolean)
        """
        self.vcs.getPlugin().setPreferences("StopLogOnCopy",
                                            self.stopCheckBox.isChecked())
        self.nextButton.setEnabled(True)
        self.limitSpinBox.setEnabled(True)
    
    @pyqtSlot()
    def on_refreshButton_clicked(self):
        """
        Private slot to refresh the log.
        """
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Cancel).setEnabled(True)
        self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)
        
        self.refreshButton.setEnabled(False)
        
        # save the selected items commit IDs
        self.__selectedRevisions = []
        for item in self.logTree.selectedItems():
            self.__selectedRevisions.append(item.text(self.RevisionColumn))
        
        if self.initialCommandMode in ("incoming", "outgoing"):
            self.nextButton.setEnabled(False)
            self.limitSpinBox.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)
            self.limitSpinBox.setEnabled(True)
        
        self.commandMode = self.initialCommandMode
        self.start(self.__filename, isFile=self.__isFile,
                   noEntries=self.logTree.topLevelItemCount())
    
    def on_passwordCheckBox_toggled(self, isOn):
        """
        Private slot to handle the password checkbox toggled.
        
        @param isOn flag indicating the status of the check box (boolean)
        """
        if isOn:
            self.input.setEchoMode(QLineEdit.Password)
        else:
            self.input.setEchoMode(QLineEdit.Normal)
    
    @pyqtSlot()
    def on_sendButton_clicked(self):
        """
        Private slot to send the input to the mercurial process.
        """
        inputTxt = self.input.text()
        inputTxt += os.linesep
        
        if self.passwordCheckBox.isChecked():
            self.errors.insertPlainText(os.linesep)
            self.errors.ensureCursorVisible()
        else:
            self.errors.insertPlainText(inputTxt)
            self.errors.ensureCursorVisible()
        
        self.process.write(inputTxt)
        
        self.passwordCheckBox.setChecked(False)
        self.input.clear()
    
    def on_input_returnPressed(self):
        """
        Private slot to handle the press of the return key in the input field.
        """
        self.intercept = True
        self.on_sendButton_clicked()
    
    def keyPressEvent(self, evt):
        """
        Protected slot to handle a key press event.
        
        @param evt the key press event (QKeyEvent)
        """
        if self.intercept:
            self.intercept = False
            evt.accept()
            return
        super(HgLogBrowserDialog, self).keyPressEvent(evt)
    
    @pyqtSlot()
    def __phaseActTriggered(self):
        """
        Private slot to handle the Change Phase action.
        """
        currentPhase = self.logTree.selectedItems()[0].text(self.PhaseColumn)
        revs = []
        for itm in self.logTree.selectedItems():
            if itm.text(self.PhaseColumn) == currentPhase:
                revs.append(
                    itm.text(self.RevisionColumn).split(":")[0].strip())
        
        if not revs:
            self.__phaseAct.setEnabled(False)
            return
        
        if currentPhase == self.phases["draft"]:
            newPhase = self.phases["secret"]
            data = (revs, "s", True)
        else:
            newPhase = self.phases["draft"]
            data = (revs, "d", False)
        res = self.vcs.hgPhase(self.repodir, data)
        if res:
            for itm in self.logTree.selectedItems():
                itm.setText(self.PhaseColumn, newPhase)
    
    @pyqtSlot()
    def __graftActTriggered(self):
        """
        Private slot to handle the Copy Changesets action.
        """
        revs = []
        
        for itm in self.logTree.selectedItems():
            branch = itm.text(self.BranchColumn)
            if branch != self.__projectBranch:
                revs.append(
                    itm.text(self.RevisionColumn).strip().split(":", 1)[0])
        
        if revs:
            shouldReopen = self.vcs.hgGraft(self.repodir, revs)
            if shouldReopen:
                res = E5MessageBox.yesNo(
                    None,
                    self.tr("Copy Changesets"),
                    self.tr(
                        """The project should be reread. Do this now?"""),
                    yesDefault=True)
                if res:
                    e5App().getObject("Project").reopenProject()
                    return
            
            self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __tagActTriggered(self):
        """
        Private slot to tag the selected revision.
        """
        if len(self.logTree.selectedItems()) == 1:
            itm = self.logTree.selectedItems()[0]
            rev = itm.text(self.RevisionColumn).strip().split(":", 1)[0]
            tag = itm.text(self.TagsColumn).strip().split(", ", 1)[0]
            res = self.vcs.vcsTag(self.repodir, revision=rev, tagName=tag)
            if res:
                self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __switchActTriggered(self):
        """
        Private slot to switch the working directory to the
        selected revision.
        """
        if len(self.logTree.selectedItems()) == 1:
            itm = self.logTree.selectedItems()[0]
            rev = itm.text(self.RevisionColumn).strip().split(":", 1)[0]
            bookmarks = [bm.strip() for bm in
                         itm.text(self.BookmarksColumn).strip().split(",")
                         if bm.strip()]
            if bookmarks:
                bookmark, ok = QInputDialog.getItem(
                    self,
                    self.tr("Switch"),
                    self.tr("Select bookmark to switch to (leave empty to"
                            " use revision):"),
                    [""] + bookmarks,
                    0, False)
                if not ok:
                    return
                if bookmark:
                    rev = bookmark
            if rev:
                shouldReopen = self.vcs.vcsUpdate(self.repodir, revision=rev)
                if shouldReopen:
                    res = E5MessageBox.yesNo(
                        None,
                        self.tr("Switch"),
                        self.tr(
                            """The project should be reread. Do this now?"""),
                        yesDefault=True)
                    if res:
                        e5App().getObject("Project").reopenProject()
                        return
                
                self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __bookmarkActTriggered(self):
        """
        Private slot to bookmark the selected revision.
        """
        if len(self.logTree.selectedItems()) == 1:
            itm = self.logTree.selectedItems()[0]
            rev, changeset = \
                itm.text(self.RevisionColumn).strip().split(":", 1)
            bookmark, ok = QInputDialog.getText(
                self,
                self.tr("Define Bookmark"),
                self.tr('Enter bookmark name for changeset "{0}":').format(
                    changeset),
                QLineEdit.Normal)
            if ok and bool(bookmark):
                self.vcs.hgBookmarkDefine(
                    self.repodir, revision="rev({0})".format(rev),
                    bookmark=bookmark)
                self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __bookmarkMoveActTriggered(self):
        """
        Private slot to move a bookmark to the selected revision.
        """
        if len(self.logTree.selectedItems()) == 1:
            itm = self.logTree.selectedItems()[0]
            rev, changeset = \
                itm.text(self.RevisionColumn).strip().split(":", 1)
            bookmarksList = self.vcs.hgGetBookmarksList(self.repodir)
            bookmark, ok = QInputDialog.getItem(
                self,
                self.tr("Move Bookmark"),
                self.tr('Select the bookmark to be moved  to changeset'
                        ' "{0}":').format(changeset),
                [""] + bookmarksList,
                0, False)
            if ok and bool(bookmark):
                self.vcs.hgBookmarkMove(
                    self.repodir, revision="rev({0})".format(rev),
                    bookmark=bookmark)
                self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __lfPullActTriggered(self):
        """
        Private slot to pull large files of selected revisions.
        """
        revs = []
        for itm in self.logTree.selectedItems():
            rev = itm.text(self.RevisionColumn).strip().split(":", 1)[0]
            if rev:
                revs.append(rev)
        
        if revs:
            self.vcs.getExtensionObject("largefiles").hgLfPull(
                self.repodir, revisions=revs)
    
    @pyqtSlot()
    def __fetchActTriggered(self):
        """
        Private slot to fetch changes from a remote repository.
        """
        shouldReopen = False
        refresh = False
        
        if self.initialCommandMode == "log":
            shouldReopen = self.vcs.getExtensionObject("fetch").hgFetch(
                self.repodir)
            refresh = True
        elif self.initialCommandMode == "incoming":
            revs = []
            for itm in self.logTree.selectedItems():
                rev = itm.text(self.RevisionColumn).split(":")[1].strip()
                phase = itm.text(self.PhaseColumn).strip()
                if rev and phase == self.phases["draft"]:
                    revs.append(rev)
            if revs:
                shouldReopen = self.vcs.getExtensionObject("fetch").hgFetch(
                    self.repodir, )
                refresh = True
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Fetch Changes"),
                self.tr(
                    """The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                e5App().getObject("Project").reopenProject()
                return
        
        if refresh:
            self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __pullActTriggered(self):
        """
        Private slot to pull changes from a remote repository.
        """
        shouldReopen = False
        refresh = False
        
        if self.initialCommandMode == "log":
            shouldReopen = self.vcs.hgPull(self.repodir)
            refresh = True
        elif self.initialCommandMode == "incoming":
            revs = []
            for itm in self.logTree.selectedItems():
                rev = itm.text(self.RevisionColumn).split(":")[1].strip()
                phase = itm.text(self.PhaseColumn).strip()
                if rev and phase == self.phases["draft"]:
                    revs.append(rev)
            if revs:
                shouldReopen = self.vcs.hgPull(self.repodir, revisions=revs)
                refresh = True
        
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Pull Changes"),
                self.tr(
                    """The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                e5App().getObject("Project").reopenProject()
                return
        
        if refresh:
            self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __pushActTriggered(self):
        """
        Private slot to push changes to a remote repository up to a selected
        changeset.
        """
        itm = self.logTree.selectedItems()[0]
        rev = itm.text(self.RevisionColumn).strip().split(":", 1)[0]
        if rev:
            self.vcs.hgPush(self.repodir, rev=rev)
            self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __pushAllActTriggered(self):
        """
        Private slot to push all changes to a remote repository.
        """
        self.vcs.hgPush(self.repodir)
        self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __stripActTriggered(self):
        """
        Private slot to strip changesets from the repository.
        """
        itm = self.logTree.selectedItems()[0]
        rev = itm.text(self.RevisionColumn).strip().split(":", 1)[1]
        shouldReopen = self.vcs.getExtensionObject("strip").hgStrip(
            self.repodir, rev=rev)
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Strip Changesets"),
                self.tr(
                    """The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                e5App().getObject("Project").reopenProject()
                return
        
        self.on_refreshButton_clicked()
    
    @pyqtSlot()
    def __mergeActTriggered(self):
        """
        Private slot to merge the working directory with the selected
        changeset.
        """
        itm = self.logTree.selectedItems()[0]
        rev = "rev({0})".format(
            itm.text(self.RevisionColumn).strip().split(":", 1)[0])
        self.vcs.vcsMerge(self.repodir, rev=rev)
    
    @pyqtSlot()
    def __bundleActTriggered(self):
        """
        Private slot to create a changegroup file.
        """
        if self.initialCommandMode == "log":
            selectedItems = self.logTree.selectedItems()
            if len(selectedItems) == 0:
                # all revisions of the local repository will be bundled
                bundleData = {
                    "revs": [],
                    "base": "",
                    "all": True,
                }
            elif len(selectedItems) == 1:
                # the selected changeset is the base
                rev = selectedItems[0].text(self.RevisionColumn)\
                    .split(":", 1)[0].strip()
                bundleData = {
                    "revs": [],
                    "base": rev,
                    "all": False,
                }
            else:
                # lowest revision is the base, others will be bundled
                revs = []
                for itm in selectedItems:
                    rev = itm.text(self.RevisionColumn).split(":", 1)[0]
                    try:
                        revs.append(int(rev))
                    except ValueError:
                        # ignore silently
                        pass
                baseRev = min(revs)
                while baseRev in revs:
                    revs.remove(baseRev)
                
                bundleData = {
                    "revs": [str(rev) for rev in revs],
                    "base": str(baseRev),
                    "all": False,
                }
        elif self.initialCommandMode == "outgoing":
            selectedItems = self.logTree.selectedItems()
            if len(selectedItems) > 0:
                revs = []
                for itm in selectedItems:
                    rev = itm.text(self.RevisionColumn).split(":", 1)[0]
                    revs.append(rev.strip())
                
                bundleData = {
                    "revs": revs,
                    "base": "",
                    "all": False,
                }
        
        self.vcs.hgBundle(self.repodir, bundleData=bundleData)
    
    @pyqtSlot()
    def __unbundleActTriggered(self):
        """
        Private slot to apply the currently previewed bundle file.
        """
        if self.initialCommandMode == "incoming" and bool(self.__bundle):
            shouldReopen = self.vcs.hgUnbundle(self.repodir,
                                               files=[self.__bundle])
            if shouldReopen:
                res = E5MessageBox.yesNo(
                    None,
                    self.tr("Apply Changegroup"),
                    self.tr("""The project should be reread. Do this now?"""),
                    yesDefault=True)
                if res:
                    e5App().getObject("Project").reopenProject()
                    return
            
            self.vcs.vcsLogBrowser(self.repodir)
            self.close()
    
    @pyqtSlot()
    def __gpgSignActTriggered(self):
        """
        Private slot to sign the selected revisions.
        """
        revs = []
        for itm in self.logTree.selectedItems():
            rev = itm.text(self.RevisionColumn).split(":", 1)[0].strip()
            if rev:
                revs.append(rev)
        
        if revs:
            self.vcs.getExtensionObject("gpg").hgGpgSign(
                self.repodir, revisions=revs)
    
    @pyqtSlot()
    def __gpgVerifyActTriggered(self):
        """
        Private slot to verify the signatures of a selected revisions.
        """
        rev = self.logTree.selectedItems()[0].text(self.RevisionColumn)\
            .split(":", 1)[0].strip()
        if rev:
            self.vcs.getExtensionObject("gpg").hgGpgVerifySignatures(
                self.repodir, rev=rev)
    
    def __selectAllActTriggered(self, select=True):
        """
        Private method to select or unselect all log entries.
        
        @param select flag indicating to select all entries
        @type bool
        """
        blocked = self.logTree.blockSignals(True)
        for row in range(self.logTree.topLevelItemCount()):
            self.logTree.topLevelItem(row).setSelected(select)
        self.logTree.blockSignals(blocked)
        self.on_logTree_itemSelectionChanged()
    
    def __actionMode(self):
        """
        Private method to get the selected action mode.
        
        @return selected action mode (string, one of filter or find)
        """
        return self.modeComboBox.itemData(
            self.modeComboBox.currentIndex())
    
    @pyqtSlot(int)
    def on_modeComboBox_currentIndexChanged(self, index):
        """
        Private slot to react on mode changes.
        
        @param index index of the selected entry (integer)
        """
        mode = self.modeComboBox.itemData(index)
        findMode = mode == "find"
        filterMode = mode == "filter"
        
        self.fromDate.setEnabled(filterMode)
        self.toDate.setEnabled(filterMode)
        self.branchCombo.setEnabled(filterMode)
        self.findPrevButton.setVisible(findMode)
        self.findNextButton.setVisible(findMode)
        
        if findMode:
            for topIndex in range(self.logTree.topLevelItemCount()):
                self.logTree.topLevelItem(topIndex).setHidden(False)
            self.logTree.header().setSectionHidden(self.IconColumn, False)
        elif filterMode:
            self.__filterLogs()
    
    @pyqtSlot()
    def on_findPrevButton_clicked(self):
        """
        Private slot to find the previous item matching the entered criteria.
        """
        self.__findItem(True)
    
    @pyqtSlot()
    def on_findNextButton_clicked(self):
        """
        Private slot to find the next item matching the entered criteria.
        """
        self.__findItem(False)
    
    def __findItem(self, backwards=False, interactive=False):
        """
        Private slot to find an item matching the entered criteria.
        
        @param backwards flag indicating to search backwards (boolean)
        @param interactive flag indicating an interactive search (boolean)
        """
        self.__findBackwards = backwards
        
        fieldIndex, searchRx, indexIsRole = self.__prepareFieldSearch()
        currentIndex = self.logTree.indexOfTopLevelItem(
            self.logTree.currentItem())
        if backwards:
            if interactive:
                indexes = range(currentIndex, -1, -1)
            else:
                indexes = range(currentIndex - 1, -1, -1)
        else:
            if interactive:
                indexes = range(currentIndex, self.logTree.topLevelItemCount())
            else:
                indexes = range(currentIndex + 1,
                                self.logTree.topLevelItemCount())
        
        for index in indexes:
            topItem = self.logTree.topLevelItem(index)
            if indexIsRole:
                if fieldIndex == self.__changesRole:
                    changes = topItem.data(0, self.__changesRole)
                    txt = "\n".join(
                        [c["path"] for c in changes] +
                        [c["copyfrom"] for c in changes]
                    )
                else:
                    # Find based on complete message text
                    txt = "\n".join(topItem.data(0, self.__messageRole))
            else:
                txt = topItem.text(fieldIndex)
            if searchRx.indexIn(txt) > -1:
                self.logTree.setCurrentItem(self.logTree.topLevelItem(index))
                break
        else:
            E5MessageBox.information(
                self,
                self.tr("Find Commit"),
                self.tr("""'{0}' was not found.""").format(self.rxEdit.text()))
    
    def __revisionClicked(self, url):
        """
        Private slot to handle the anchorClicked signal of the changeset
        details pane.
        
        @param url URL that was clicked
        @type QUrl
        """
        if url.scheme() == "rev":
            # a parent or child revision was clicked, show the respective item
            rev = url.path()
            searchStr = "{0:>7}:".format(rev)
            # format must be in sync with item generation format
            items = self.logTree.findItems(searchStr, Qt.MatchStartsWith,
                                           self.RevisionColumn)
            if items:
                itm = items[0]
                if itm.isHidden():
                    itm.setHidden(False)
                self.logTree.setCurrentItem(itm)
            else:
                # load the next batch and try again
                if self.nextButton.isEnabled():
                    self.__addFinishCallback(
                        lambda: self.__revisionClicked(url))
                    self.on_nextButton_clicked()
    
    ###########################################################################
    ## Diff handling methods below
    ###########################################################################
    
    def __generateDiffs(self, parent=1):
        """
        Private slot to generate diff outputs for the selected item.
        
        @param parent number of parent to diff against
        @type int
        """
        self.diffEdit.setPlainText(self.tr("Generating differences ..."))
        self.diffLabel.setText(self.tr("Differences"))
        self.diffSelectLabel.clear()
        self.diffHighlighter.regenerateRules()
        
        selectedItems = self.logTree.selectedItems()
        if len(selectedItems) == 1:
            currentItem = selectedItems[0]
            rev2 = currentItem.text(self.RevisionColumn).split(":", 1)[0]
            parents = currentItem.data(0, self.__parentsRole)
            if len(parents) >= parent:
                self.diffLabel.setText(
                    self.tr("Differences to Parent {0}").format(parent))
                rev1 = parents[parent - 1]
                
                self.__diffGenerator.start(self.__filename, [rev1, rev2],
                                           self.__bundle)
            
            if len(parents) > 1:
                if parent == 1:
                    par1 = "&nbsp;1&nbsp;"
                else:
                    par1 = '<a href="diff:1">&nbsp;1&nbsp;</a>'
                if parent == 2:
                    par2 = "&nbsp;2&nbsp;"
                else:
                    par2 = '<a href="diff:2">&nbsp;2&nbsp;</a>'
                self.diffSelectLabel.setText(
                    self.tr('Diff to Parent {0}{1}').format(par1, par2))
        elif len(selectedItems) == 2:
            rev2 = int(selectedItems[0].text(
                self.RevisionColumn).split(":")[0])
            rev1 = int(selectedItems[1].text(
                self.RevisionColumn).split(":")[0])
            
            self.__diffGenerator.start(self.__filename,
                                       [min(rev1, rev2), max(rev1, rev2)],
                                       self.__bundle)
        else:
            self.diffEdit.clear()
    
    def __generatorFinished(self):
        """
        Private slot connected to the finished signal of the diff generator.
        """
        diff, errors, fileSeparators = self.__diffGenerator.getResult()
        
        if diff:
            self.diffEdit.setPlainText("".join(diff))
        elif errors:
            self.diffEdit.setPlainText("".join(errors))
        else:
            self.diffEdit.setPlainText(self.tr('There is no difference.'))
        
        self.saveLabel.setVisible(bool(diff))
        
        if self.__diffUpdatesFiles:
            for oldFileName, newFileName, lineNumber in fileSeparators:
                if oldFileName == newFileName:
                    fileName = oldFileName
                elif oldFileName == "__NULL__":
                    fileName = newFileName
                else:
                    fileName = oldFileName
                item = QTreeWidgetItem(self.filesTree, ["", fileName, ""])
                item.setData(0, self.__diffFileLineRole, lineNumber)
            self.__resizeColumnsFiles()
            self.__resortFiles()
        else:
            for oldFileName, newFileName, lineNumber in fileSeparators:
                for fileName in (oldFileName, newFileName):
                    if fileName != "__NULL__":
                        items = self.filesTree.findItems(
                            fileName, Qt.MatchExactly, 1)
                        for item in items:
                            item.setData(0, self.__diffFileLineRole,
                                         lineNumber)
        
        tc = self.diffEdit.textCursor()
        tc.movePosition(QTextCursor.Start)
        self.diffEdit.setTextCursor(tc)
        self.diffEdit.ensureCursorVisible()
    
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_filesTree_currentItemChanged(self, current, previous):
        """
        Private slot called, when the current item of the files tree changes.
        
        @param current reference to the new current item (QTreeWidgetItem)
        @param previous reference to the old current item (QTreeWidgetItem)
        """
        if current:
            para = current.data(0, self.__diffFileLineRole)
            if para is not None:
                if para == 0:
                    tc = self.diffEdit.textCursor()
                    tc.movePosition(QTextCursor.Start)
                    self.diffEdit.setTextCursor(tc)
                    self.diffEdit.ensureCursorVisible()
                elif para == -1:
                    tc = self.diffEdit.textCursor()
                    tc.movePosition(QTextCursor.End)
                    self.diffEdit.setTextCursor(tc)
                    self.diffEdit.ensureCursorVisible()
                else:
                    # step 1: move cursor to end
                    tc = self.diffEdit.textCursor()
                    tc.movePosition(QTextCursor.End)
                    self.diffEdit.setTextCursor(tc)
                    self.diffEdit.ensureCursorVisible()
                    
                    # step 2: move cursor to desired line
                    tc = self.diffEdit.textCursor()
                    delta = tc.blockNumber() - para
                    tc.movePosition(QTextCursor.PreviousBlock,
                                    QTextCursor.MoveAnchor, delta)
                    self.diffEdit.setTextCursor(tc)
                    self.diffEdit.ensureCursorVisible()
    
    @pyqtSlot(str)
    def on_diffSelectLabel_linkActivated(self, link):
        """
        Private slot to handle the selection of a diff target.
        
        @param link activated link
        @type str
        """
        if ":" in link:
            scheme, parent = link.split(":", 1)
            if scheme == "diff":
                try:
                    parent = int(parent)
                    self.__generateDiffs(parent)
                except ValueError:
                    # ignore silently
                    pass
    
    @pyqtSlot(str)
    def on_saveLabel_linkActivated(self, link):
        """
        Private slot to handle the selection of the save link.
        
        @param link activated link
        @type str
        """
        if ":" not in link:
            return
        
        scheme, rest = link.split(":", 1)
        if scheme != "save" or rest != "me":
            return
        
        if self.projectMode:
            fname = self.vcs.splitPath(self.__filename)[0]
            fname += "/{0}.diff".format(os.path.split(fname)[-1])
        else:
            dname, fname = self.vcs.splitPath(self.__filename)
            if fname != '.':
                fname = "{0}.diff".format(self.__filename)
            else:
                fname = dname
        
        fname, selectedFilter = E5FileDialog.getSaveFileNameAndFilter(
            self,
            self.tr("Save Diff"),
            fname,
            self.tr("Patch Files (*.diff)"),
            None,
            E5FileDialog.Options(E5FileDialog.DontConfirmOverwrite))
        
        if not fname:
            return  # user aborted
        
        ext = QFileInfo(fname).suffix()
        if not ext:
            ex = selectedFilter.split("(*")[1].split(")")[0]
            if ex:
                fname += ex
        if QFileInfo(fname).exists():
            res = E5MessageBox.yesNo(
                self,
                self.tr("Save Diff"),
                self.tr("<p>The patch file <b>{0}</b> already exists."
                        " Overwrite it?</p>").format(fname),
                icon=E5MessageBox.Warning)
            if not res:
                return
        fname = Utilities.toNativeSeparators(fname)
        
        eol = e5App().getObject("Project").getEolString()
        try:
            f = open(fname, "w", encoding="utf-8", newline="")
            f.write(eol.join(self.diffEdit.toPlainText().splitlines()))
            f.close()
        except IOError as why:
            E5MessageBox.critical(
                self, self.tr('Save Diff'),
                self.tr(
                    '<p>The patch file <b>{0}</b> could not be saved.'
                    '<br>Reason: {1}</p>')
                .format(fname, str(why)))
    
    @pyqtSlot(str)
    def on_sbsSelectLabel_linkActivated(self, link):
        """
        Private slot to handle selection of a side-by-side link.
        
        @param link text of the selected link
        @type str
        """
        if ":" in link:
            scheme, path = link.split(":", 1)
            if scheme == "sbsdiff" and "_" in path:
                rev1, rev2 = path.split("_", 1)
                self.vcs.hgSbsDiff(self.__filename, revisions=(rev1, rev2))
