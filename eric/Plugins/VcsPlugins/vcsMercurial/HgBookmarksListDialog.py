# -*- coding: utf-8 -*-

# Copyright (c) 2011 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to show a list of bookmarks.
"""

from __future__ import unicode_literals
try:
    str = unicode
except NameError:
    pass

import os

from PyQt5.QtCore import pyqtSlot, QProcess, Qt, QTimer, QCoreApplication, \
    QPoint
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QHeaderView, \
    QTreeWidgetItem, QLineEdit, QMenu, QInputDialog

from E5Gui.E5Application import e5App
from E5Gui import E5MessageBox

from .Ui_HgBookmarksListDialog import Ui_HgBookmarksListDialog

import UI.PixmapCache


class HgBookmarksListDialog(QDialog, Ui_HgBookmarksListDialog):
    """
    Class implementing a dialog to show a list of bookmarks.
    """
    def __init__(self, vcs, parent=None):
        """
        Constructor
        
        @param vcs reference to the vcs object
        @param parent parent widget (QWidget)
        """
        super(HgBookmarksListDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        
        self.refreshButton = self.buttonBox.addButton(
            self.tr("Refresh"), QDialogButtonBox.ActionRole)
        self.refreshButton.setToolTip(
            self.tr("Press to refresh the bookmarks display"))
        self.refreshButton.setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)
        
        self.process = QProcess()
        self.vcs = vcs
        self.__bookmarksList = None
        self.__repoDir = None
        self.__hgClient = vcs.getClient()
        self.__bookmarksDefined = False
        self.__currentRevision = ""
        
        self.bookmarksList.headerItem().setText(
            self.bookmarksList.columnCount(), "")
        self.bookmarksList.header().setSortIndicator(3, Qt.AscendingOrder)
        
        self.process.finished.connect(self.__procFinished)
        self.process.readyReadStandardOutput.connect(self.__readStdout)
        self.process.readyReadStandardError.connect(self.__readStderr)
        
        self.show()
        QCoreApplication.processEvents()
    
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
        
        e.accept()
    
    def start(self, path, bookmarksList):
        """
        Public slot to start the bookmarks command.
        
        @param path name of directory to be listed (string)
        @param bookmarksList reference to string list receiving the bookmarks
            (list of strings)
        """
        self.bookmarksList.clear()
        self.__bookmarksDefined = False
        
        self.errorGroup.hide()
        
        self.intercept = False
        self.activateWindow()
        
        self.__bookmarksList = bookmarksList
        del self.__bookmarksList[:]     # clear the list
        
        dname, fname = self.vcs.splitPath(path)
        
        # find the root of the repo
        repodir = dname
        while not os.path.isdir(os.path.join(repodir, self.vcs.adminDir)):
            repodir = os.path.dirname(repodir)
            if os.path.splitdrive(repodir)[1] == os.sep:
                return
        self.__repoDir = repodir
        
        args = self.vcs.initCommand("bookmarks")
        
        if self.__hgClient:
            self.inputGroup.setEnabled(False)
            self.inputGroup.hide()
            self.refreshButton.setEnabled(False)
            
            out, err = self.__hgClient.runcommand(args)
            if err:
                self.__showError(err)
            if out:
                for line in out.splitlines():
                    self.__processOutputLine(line)
                    if self.__hgClient.wasCanceled():
                        break
            self.__finish()
        else:
            self.process.kill()
            self.process.setWorkingDirectory(repodir)
            
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
                self.buttonBox.button(QDialogButtonBox.Close).setEnabled(False)
                self.buttonBox.button(QDialogButtonBox.Cancel).setEnabled(True)
                self.buttonBox.button(QDialogButtonBox.Cancel).setDefault(True)
                
                self.inputGroup.setEnabled(True)
                self.inputGroup.show()
                self.refreshButton.setEnabled(False)
    
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
        
        self.inputGroup.setEnabled(False)
        self.inputGroup.hide()
        self.refreshButton.setEnabled(True)
        
        self.buttonBox.button(QDialogButtonBox.Close).setEnabled(True)
        self.buttonBox.button(QDialogButtonBox.Cancel).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Close).setDefault(True)
        self.buttonBox.button(QDialogButtonBox.Close).setFocus(
            Qt.OtherFocusReason)
        
        if self.bookmarksList.topLevelItemCount() == 0:
            # no bookmarks defined
            self.__generateItem(
                self.tr("no bookmarks defined"), "", "", "")
            self.__bookmarksDefined = False
        else:
            self.__bookmarksDefined = True
        
        self.__resizeColumns()
        self.__resort()
        
        # restore current item
        if self.__currentRevision:
            items = self.bookmarksList.findItems(
                self.__currentRevision, Qt.MatchExactly, 0)
            if items:
                self.bookmarksList.setCurrentItem(items[0])
                self.__currentRevision = ""
                self.bookmarksList.setFocus(Qt.OtherFocusReason)
    
    def on_buttonBox_clicked(self, button):
        """
        Private slot called by a button of the button box clicked.
        
        @param button button that was clicked (QAbstractButton)
        """
        if button == self.buttonBox.button(QDialogButtonBox.Close):
            self.close()
        elif button == self.buttonBox.button(QDialogButtonBox.Cancel):
            if self.__hgClient:
                self.__hgClient.cancel()
            else:
                self.__finish()
        elif button == self.refreshButton:
            self.on_refreshButton_clicked()
    
    def __procFinished(self, exitCode, exitStatus):
        """
        Private slot connected to the finished signal.
        
        @param exitCode exit code of the process (integer)
        @param exitStatus exit status of the process (QProcess.ExitStatus)
        """
        self.__finish()
    
    def __resort(self):
        """
        Private method to resort the tree.
        """
        self.bookmarksList.sortItems(
            self.bookmarksList.sortColumn(),
            self.bookmarksList.header().sortIndicatorOrder())
    
    def __resizeColumns(self):
        """
        Private method to resize the list columns.
        """
        self.bookmarksList.header().resizeSections(
            QHeaderView.ResizeToContents)
        self.bookmarksList.header().setStretchLastSection(True)
    
    def __generateItem(self, revision, changeset, status, name):
        """
        Private method to generate a bookmark item in the bookmarks list.
        
        @param revision revision of the bookmark (string)
        @param changeset changeset of the bookmark (string)
        @param status of the bookmark (string)
        @param name name of the bookmark (string)
        """
        itm = QTreeWidgetItem(self.bookmarksList)
        if revision[0].isdecimal():
            # valid bookmark entry
            itm.setData(0, Qt.DisplayRole, int(revision))
            itm.setData(1, Qt.DisplayRole, changeset)
            itm.setData(2, Qt.DisplayRole, status)
            itm.setData(3, Qt.DisplayRole, name)
            itm.setTextAlignment(0, Qt.AlignRight)
            itm.setTextAlignment(1, Qt.AlignRight)
            itm.setTextAlignment(2, Qt.AlignHCenter)
        else:
            # error message
            itm.setData(0, Qt.DisplayRole, revision)
    
    def __readStdout(self):
        """
        Private slot to handle the readyReadStdout signal.
        
        It reads the output of the process, formats it and inserts it into
        the contents pane.
        """
        self.process.setReadChannel(QProcess.StandardOutput)
        
        while self.process.canReadLine():
            s = str(self.process.readLine(), self.vcs.getEncoding(),
                    'replace').strip()
            self.__processOutputLine(s)
    
    def __processOutputLine(self, line):
        """
        Private method to process the lines of output.
        
        @param line output line to be processed (string)
        """
        li = line.split()
        if li[-1][0] in "1234567890":
            # last element is a rev:changeset
            rev, changeset = li[-1].split(":", 1)
            del li[-1]
            if li[0] == "*":
                status = "current"
                del li[0]
            else:
                status = ""
            name = " ".join(li)
            self.__generateItem(rev, changeset, status, name)
            if self.__bookmarksList is not None:
                self.__bookmarksList.append(name)
    
    def __readStderr(self):
        """
        Private slot to handle the readyReadStderr signal.
        
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
        Private slot to send the input to the subversion process.
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
        super(HgBookmarksListDialog, self).keyPressEvent(evt)
    
    @pyqtSlot()
    def on_refreshButton_clicked(self):
        """
        Private slot to refresh the status display.
        """
        # save the current items commit ID
        itm = self.bookmarksList.currentItem()
        if itm is not None:
            self.__currentRevision = itm.text(0)
        else:
            self.__currentRevision = ""
        
        self.start(self.__repoDir, self.__bookmarksList)
    
    @pyqtSlot(QPoint)
    def on_bookmarksList_customContextMenuRequested(self, pos):
        """
        Private slot to handle the context menu request.
        
        @param pos position the context menu was requetsed at
        @type QPoint
        """
        itm = self.bookmarksList.itemAt(pos)
        if itm is not None:
            menu = QMenu(self.bookmarksList)
            menu.addAction(
                UI.PixmapCache.getIcon("vcsSwitch.png"),
                self.tr("Switch to"), self.__switchTo)
            menu.addSeparator()
            menu.addAction(
                UI.PixmapCache.getIcon("deleteBookmark.png"),
                self.tr("Delete"), self.__deleteBookmark)
            menu.addAction(
                UI.PixmapCache.getIcon("renameBookmark.png"),
                self.tr("Rename"), self.__renameBookmark)
            menu.addSeparator()
            act = menu.addAction(
                UI.PixmapCache.getIcon("pullBookmark.png"),
                self.tr("Pull"), self.__pullBookmark)
            act.setEnabled(self.vcs.canPull())
            act = menu.addAction(
                UI.PixmapCache.getIcon("pushBookmark.png"),
                self.tr("Push"), self.__pushBookmark)
            act.setEnabled(self.vcs.canPush())
            menu.popup(self.bookmarksList.mapToGlobal(pos))
    
    def __switchTo(self):
        """
        Private slot to switch the working directory to the selected revision.
        """
        itm = self.bookmarksList.currentItem()
        bookmark = itm.text(3).strip()
        if bookmark:
            shouldReopen = self.vcs.vcsUpdate(
                self.__repoDir, revision=bookmark)
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
    
    def __deleteBookmark(self):
        """
        Private slot to delete the selected bookmark.
        """
        itm = self.bookmarksList.currentItem()
        bookmark = itm.text(3).strip()
        if bookmark:
            yes = E5MessageBox.yesNo(
                self,
                self.tr("Delete Bookmark"),
                self.tr("""<p>Shall the bookmark <b>{0}</b> really be"""
                        """ deleted?</p>""").format(bookmark))
            if yes:
                self.vcs.hgBookmarkDelete(self.__repoDir, bookmark=bookmark)
                self.on_refreshButton_clicked()
    
    def __renameBookmark(self):
        """
        Private slot to rename the selected bookmark.
        """
        itm = self.bookmarksList.currentItem()
        bookmark = itm.text(3).strip()
        if bookmark:
            newName, ok = QInputDialog.getText(
                self,
                self.tr("Rename Bookmark"),
                self.tr("<p>Enter the new name for bookmark <b>{0}</b>:</p>")
                .format(bookmark),
                QLineEdit.Normal)
            if ok and bool(newName):
                self.vcs.hgBookmarkRename(self.__repoDir, (bookmark, newName))
                self.on_refreshButton_clicked()
    
    def __pullBookmark(self):
        """
        Private slot to pull the selected bookmark.
        """
        itm = self.bookmarksList.currentItem()
        bookmark = itm.text(3).strip()
        if bookmark:
            self.vcs.hgBookmarkPull(self.__repoDir, bookmark=bookmark)
            self.on_refreshButton_clicked()
    
    def __pushBookmark(self):
        """
        Private slot to push the selected bookmark.
        """
        itm = self.bookmarksList.currentItem()
        bookmark = itm.text(3).strip()
        if bookmark:
            self.vcs.hgBookmarkPush(self.__repoDir, bookmark=bookmark)
            self.on_refreshButton_clicked()
