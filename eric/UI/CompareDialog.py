# -*- coding: utf-8 -*-

# Copyright (c) 2004 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to compare two files and show the result side by
side.
"""

from __future__ import unicode_literals
try:
    basestring    # __IGNORE_WARNING__
except NameError:
    basestring = str

import re
from difflib import _mdiff, IS_CHARACTER_JUNK

from PyQt5.QtCore import QTimer, QEvent, pyqtSlot
from PyQt5.QtGui import QFontMetrics, QBrush, QTextCursor
from PyQt5.QtWidgets import QWidget, QApplication, QDialogButtonBox

from E5Gui import E5MessageBox
from E5Gui.E5MainWindow import E5MainWindow
from E5Gui.E5PathPicker import E5PathPickerModes

import UI.PixmapCache

from .Ui_CompareDialog import Ui_CompareDialog

import Preferences


def sbsdiff(a, b, linenumberwidth=4):
    """
    Compare two sequences of lines; generate the delta for display side by
    side.
    
    @param a first sequence of lines (list of strings)
    @param b second sequence of lines (list of strings)
    @param linenumberwidth width (in characters) of the linenumbers (integer)
    @return a generator yielding tuples of differences. The tuple is composed
        of strings as follows.
        <ul>
            <li>opcode -- one of e, d, i, r for equal, delete, insert,
                replace</li>
            <li>lineno a -- linenumber of sequence a</li>
            <li>line a -- line of sequence a</li>
            <li>lineno b -- linenumber of sequence b</li>
            <li>line b -- line of sequence b</li>
        </ul>
    """
    def removeMarkers(line):
        """
        Internal function to remove all diff markers.
        
        @param line line to work on (string)
        @return line without diff markers (string)
        """
        return line\
            .replace('\0+', "")\
            .replace('\0-', "")\
            .replace('\0^', "")\
            .replace('\1', "")

    linenumberformat = "{{0:{0:d}d}}".format(linenumberwidth)
    emptylineno = ' ' * linenumberwidth
    
    for (ln1, l1), (ln2, l2), flag in _mdiff(a, b, None, None,
                                             IS_CHARACTER_JUNK):
        if not flag:
            yield ('e', linenumberformat.format(ln1), l1,
                   linenumberformat.format(ln2), l2)
            continue
        if ln2 == "" and l2 in ("\r\n", "\n", "\r"):
            yield ('d', linenumberformat.format(ln1), removeMarkers(l1),
                   emptylineno, l2)
            continue
        if ln1 == "" and l1 in ("\r\n", "\n", "\r"):
            yield ('i', emptylineno, l1,
                   linenumberformat.format(ln2), removeMarkers(l2))
            continue
        yield ('r', linenumberformat.format(ln1), l1,
               linenumberformat.format(ln2), l2)


class CompareDialog(QWidget, Ui_CompareDialog):
    """
    Class implementing a dialog to compare two files and show the result side
    by side.
    """
    def __init__(self, files=None, parent=None):
        """
        Constructor
        
        @param files list of files to compare and their label
            (list of two tuples of two strings)
        @param parent parent widget (QWidget)
        """
        super(CompareDialog, self).__init__(parent)
        self.setupUi(self)
        
        if files is None:
            files = []
        
        self.file1Picker.setMode(E5PathPickerModes.OpenFileMode)
        self.file2Picker.setMode(E5PathPickerModes.OpenFileMode)
        
        self.diffButton = self.buttonBox.addButton(
            self.tr("Compare"), QDialogButtonBox.ActionRole)
        self.diffButton.setToolTip(
            self.tr("Press to perform the comparison of the two files"))
        self.diffButton.setEnabled(False)
        self.diffButton.setDefault(True)
        
        self.firstButton.setIcon(UI.PixmapCache.getIcon("2uparrow.png"))
        self.upButton.setIcon(UI.PixmapCache.getIcon("1uparrow.png"))
        self.downButton.setIcon(UI.PixmapCache.getIcon("1downarrow.png"))
        self.lastButton.setIcon(UI.PixmapCache.getIcon("2downarrow.png"))
        
        self.totalLabel.setText(self.tr('Total: {0}').format(0))
        self.changedLabel.setText(self.tr('Changed: {0}').format(0))
        self.addedLabel.setText(self.tr('Added: {0}').format(0))
        self.deletedLabel.setText(self.tr('Deleted: {0}').format(0))
        
        self.updateInterval = 20    # update every 20 lines
        
        self.vsb1 = self.contents_1.verticalScrollBar()
        self.hsb1 = self.contents_1.horizontalScrollBar()
        self.vsb2 = self.contents_2.verticalScrollBar()
        self.hsb2 = self.contents_2.horizontalScrollBar()
        
        self.on_synchronizeCheckBox_toggled(True)
        
        self.__generateFormats()
        
        # connect some of our widgets explicitly
        self.file1Picker.textChanged.connect(self.__fileChanged)
        self.file2Picker.textChanged.connect(self.__fileChanged)
        self.vsb1.valueChanged.connect(self.__scrollBarMoved)
        self.vsb1.valueChanged.connect(self.vsb2.setValue)
        self.vsb2.valueChanged.connect(self.vsb1.setValue)
        
        self.diffParas = []
        self.currentDiffPos = -1
        
        self.markerPattern = "\0\+|\0\^|\0\-"
        
        if len(files) == 2:
            self.filesGroup.hide()
            self.file1Picker.setText(files[0][1])
            self.file2Picker.setText(files[1][1])
            self.file1Label.setText(files[0][0])
            self.file2Label.setText(files[1][0])
            self.diffButton.hide()
            QTimer.singleShot(0, self.on_diffButton_clicked)
        else:
            self.file1Label.hide()
            self.file2Label.hide()
    
    def __generateFormats(self):
        """
        Private method to generate the various text formats.
        """
        font = Preferences.getEditorOtherFonts("MonospacedFont")
        self.contents_1.setFontFamily(font.family())
        self.contents_1.setFontPointSize(font.pointSize())
        self.contents_2.setFontFamily(font.family())
        self.contents_2.setFontPointSize(font.pointSize())
        self.fontHeight = QFontMetrics(self.contents_1.currentFont()).height()
        
        self.cNormalFormat = self.contents_1.currentCharFormat()
        self.cInsertedFormat = self.contents_1.currentCharFormat()
        self.cInsertedFormat.setBackground(
            QBrush(Preferences.getDiffColour("AddedColor")))
        self.cDeletedFormat = self.contents_1.currentCharFormat()
        self.cDeletedFormat.setBackground(
            QBrush(Preferences.getDiffColour("RemovedColor")))
        self.cReplacedFormat = self.contents_1.currentCharFormat()
        self.cReplacedFormat.setBackground(
            QBrush(Preferences.getDiffColour("ReplacedColor")))
    
    def show(self, filename=None):
        """
        Public slot to show the dialog.
        
        @param filename name of a file to use as the first file (string)
        """
        if filename:
            self.file1Picker.setText(filename)
        super(CompareDialog, self).show()
        
    def __appendText(self, pane, linenumber, line, charFormat,
                     interLine=False):
        """
        Private method to append text to the end of the contents pane.
        
        @param pane text edit widget to append text to (QTextedit)
        @param linenumber number of line to insert (string)
        @param line text to insert (string)
        @param charFormat text format to be used (QTextCharFormat)
        @param interLine flag indicating interline changes (boolean)
        """
        tc = pane.textCursor()
        tc.movePosition(QTextCursor.End)
        pane.setTextCursor(tc)
        pane.setCurrentCharFormat(charFormat)
        if interLine:
            pane.insertPlainText("{0} ".format(linenumber))
            for txt in re.split(self.markerPattern, line):
                if txt:
                    if txt.count('\1'):
                        txt1, txt = txt.split('\1', 1)
                        tc = pane.textCursor()
                        tc.movePosition(QTextCursor.End)
                        pane.setTextCursor(tc)
                        pane.setCurrentCharFormat(charFormat)
                        pane.insertPlainText(txt1)
                    tc = pane.textCursor()
                    tc.movePosition(QTextCursor.End)
                    pane.setTextCursor(tc)
                    pane.setCurrentCharFormat(self.cNormalFormat)
                    pane.insertPlainText(txt)
        else:
            pane.insertPlainText("{0} {1}".format(linenumber, line))

    def on_buttonBox_clicked(self, button):
        """
        Private slot called by a button of the button box clicked.
        
        @param button button that was clicked (QAbstractButton)
        """
        if button == self.diffButton:
            self.on_diffButton_clicked()
        
    @pyqtSlot()
    def on_diffButton_clicked(self):
        """
        Private slot to handle the Compare button press.
        """
        filename1 = self.file1Picker.text()
        try:
            f1 = open(filename1, "r", encoding="utf-8")
            lines1 = f1.readlines()
            f1.close()
        except IOError:
            E5MessageBox.critical(
                self,
                self.tr("Compare Files"),
                self.tr(
                    """<p>The file <b>{0}</b> could not be read.</p>""")
                .format(filename1))
            return

        filename2 = self.file2Picker.text()
        try:
            f2 = open(filename2, "r", encoding="utf-8")
            lines2 = f2.readlines()
            f2.close()
        except IOError:
            E5MessageBox.critical(
                self,
                self.tr("Compare Files"),
                self.tr(
                    """<p>The file <b>{0}</b> could not be read.</p>""")
                .format(filename2))
            return
        
        self.__compare(lines1, lines2)
        
    def compare(self, lines1, lines2, name1="", name2=""):
        """
        Public method to compare two lists of text.
        
        @param lines1 text to compare against (string or list of strings)
        @param lines2 text to compare (string or list of strings)
        @keyparam name1 name to be shown for the first text (string)
        @keyparam name2 name to be shown for the second text (string)
        """
        if name1 == "" or name2 == "":
            self.filesGroup.hide()
        else:
            self.file1Picker.setText(name1)
            self.file1Picker.setReadOnly(True)
            self.file2Picker.setText(name2)
            self.file2Picker.setReadOnly(True)
        self.diffButton.setEnabled(False)
        self.diffButton.hide()
        
        if isinstance(lines1, basestring):
            lines1 = lines1.splitlines(True)
        if isinstance(lines2, basestring):
            lines2 = lines2.splitlines(True)
        
        self.__compare(lines1, lines2)
        
    def __compare(self, lines1, lines2):
        """
        Private method to compare two lists of text.
        
        @param lines1 text to compare against (list of strings)
        @param lines2 text to compare (list of strings)
        """
        self.contents_1.clear()
        self.contents_2.clear()
        
        self.__generateFormats()
        
        # counters for changes
        added = 0
        deleted = 0
        changed = 0
        
        paras = 1
        self.diffParas = []
        self.currentDiffPos = -1
        oldOpcode = ''
        for opcode, ln1, l1, ln2, l2 in sbsdiff(lines1, lines2):
            if opcode in 'idr':
                if oldOpcode != opcode:
                    oldOpcode = opcode
                    self.diffParas.append(paras)
                    # update counters
                    if opcode == 'i':
                        added += 1
                    elif opcode == 'd':
                        deleted += 1
                    elif opcode == 'r':
                        changed += 1
                if opcode == 'i':
                    format1 = self.cNormalFormat
                    format2 = self.cInsertedFormat
                elif opcode == 'd':
                    format1 = self.cDeletedFormat
                    format2 = self.cNormalFormat
                elif opcode == 'r':
                    if ln1.strip():
                        format1 = self.cReplacedFormat
                    else:
                        format1 = self.cNormalFormat
                    if ln2.strip():
                        format2 = self.cReplacedFormat
                    else:
                        format2 = self.cNormalFormat
            else:
                oldOpcode = ''
                format1 = self.cNormalFormat
                format2 = self.cNormalFormat
            self.__appendText(self.contents_1, ln1, l1, format1, opcode == 'r')
            self.__appendText(self.contents_2, ln2, l2, format2, opcode == 'r')
            paras += 1
            if not (paras % self.updateInterval):
                QApplication.processEvents()
        
        self.vsb1.setValue(0)
        self.vsb2.setValue(0)
        self.firstButton.setEnabled(False)
        self.upButton.setEnabled(False)
        self.downButton.setEnabled(
            len(self.diffParas) > 0 and
            (self.vsb1.isVisible() or self.vsb2.isVisible()))
        self.lastButton.setEnabled(
            len(self.diffParas) > 0 and
            (self.vsb1.isVisible() or self.vsb2.isVisible()))
        
        self.totalLabel.setText(self.tr('Total: {0}')
                                    .format(added + deleted + changed))
        self.changedLabel.setText(self.tr('Changed: {0}').format(changed))
        self.addedLabel.setText(self.tr('Added: {0}').format(added))
        self.deletedLabel.setText(self.tr('Deleted: {0}').format(deleted))

    def __moveTextToCurrentDiffPos(self):
        """
        Private slot to move the text display to the current diff position.
        """
        if 0 <= self.currentDiffPos < len(self.diffParas):
            value = (self.diffParas[self.currentDiffPos] - 1) * self.fontHeight
            self.vsb1.setValue(value)
            self.vsb2.setValue(value)
    
    def __scrollBarMoved(self, value):
        """
        Private slot to enable the buttons and set the current diff position
        depending on scrollbar position.
        
        @param value scrollbar position (integer)
        """
        tPos = value / self.fontHeight + 1
        bPos = (value + self.vsb1.pageStep()) / self.fontHeight + 1
        
        self.currentDiffPos = -1
        
        if self.diffParas:
            self.firstButton.setEnabled(tPos > self.diffParas[0])
            self.upButton.setEnabled(tPos > self.diffParas[0])
            self.downButton.setEnabled(bPos < self.diffParas[-1])
            self.lastButton.setEnabled(bPos < self.diffParas[-1])
            
            if tPos >= self.diffParas[0]:
                for diffPos in self.diffParas:
                    self.currentDiffPos += 1
                    if tPos <= diffPos:
                        break
    
    @pyqtSlot()
    def on_upButton_clicked(self):
        """
        Private slot to go to the previous difference.
        """
        self.currentDiffPos -= 1
        self.__moveTextToCurrentDiffPos()
    
    @pyqtSlot()
    def on_downButton_clicked(self):
        """
        Private slot to go to the next difference.
        """
        self.currentDiffPos += 1
        self.__moveTextToCurrentDiffPos()
    
    @pyqtSlot()
    def on_firstButton_clicked(self):
        """
        Private slot to go to the first difference.
        """
        self.currentDiffPos = 0
        self.__moveTextToCurrentDiffPos()
    
    @pyqtSlot()
    def on_lastButton_clicked(self):
        """
        Private slot to go to the last difference.
        """
        self.currentDiffPos = len(self.diffParas) - 1
        self.__moveTextToCurrentDiffPos()
    
    def __fileChanged(self):
        """
        Private slot to enable/disable the Compare button.
        """
        if not self.file1Picker.text() or \
           not self.file2Picker.text():
            self.diffButton.setEnabled(False)
        else:
            self.diffButton.setEnabled(True)

    @pyqtSlot(bool)
    def on_synchronizeCheckBox_toggled(self, sync):
        """
        Private slot to connect or disconnect the scrollbars of the displays.
        
        @param sync flag indicating synchronisation status (boolean)
        """
        if sync:
            self.hsb2.setValue(self.hsb1.value())
            self.hsb1.valueChanged.connect(self.hsb2.setValue)
            self.hsb2.valueChanged.connect(self.hsb1.setValue)
        else:
            self.hsb1.valueChanged.disconnect(self.hsb2.setValue)
            self.hsb2.valueChanged.disconnect(self.hsb1.setValue)


class CompareWindow(E5MainWindow):
    """
    Main window class for the standalone dialog.
    """
    def __init__(self, files=None, parent=None):
        """
        Constructor
        
        @param files list of files to compare and their label
            (list of two tuples of two strings)
        @param parent reference to the parent widget (QWidget)
        """
        super(CompareWindow, self).__init__(parent)
        
        self.setStyle(Preferences.getUI("Style"),
                      Preferences.getUI("StyleSheet"))
        
        self.cw = CompareDialog(files, self)
        self.cw.installEventFilter(self)
        size = self.cw.size()
        self.setCentralWidget(self.cw)
        self.resize(size)
    
    def eventFilter(self, obj, event):
        """
        Public method to filter events.
        
        @param obj reference to the object the event is meant for (QObject)
        @param event reference to the event object (QEvent)
        @return flag indicating, whether the event was handled (boolean)
        """
        if event.type() == QEvent.Close:
            QApplication.exit()
            return True
        
        return False
