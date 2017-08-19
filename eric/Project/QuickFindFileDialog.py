# -*- coding: utf-8 -*-

# Copyright (c) 2004 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a quick search for files.

This is basically the FindFileNameDialog modified to support faster
interactions.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QEvent
from PyQt5.QtWidgets import QWidget, QHeaderView, QApplication, \
    QDialogButtonBox, QTreeWidgetItem

from .Ui_QuickFindFile import Ui_QuickFindFile


class QuickFindFileDialog(QWidget, Ui_QuickFindFile):
    """
    Class implementing the Quick Find File by Name Dialog.
    
    This dialog provides a slightly more streamlined behaviour
    than the standard FindFileNameDialog in that it tries to
    match any name in the project against (fragmentary) bits of
    file names.
    
    @signal sourceFile(str) emitted to open a file in the editor
    @signal designerFile(str) emitted to open a Qt-Designer file
    @signal linguistFile(str) emitted to open a Qt translation file
    """
    sourceFile = pyqtSignal(str)
    designerFile = pyqtSignal(str)
    linguistFile = pyqtSignal(str)
    
    def __init__(self, project, parent=None):
        """
        Constructor
        
        @param project reference to the project object
        @type Project
        @param parent parent widget of this dialog
        @type QWidget
        """
        super(QuickFindFileDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.fileList.headerItem().setText(self.fileList.columnCount(), "")
        self.fileNameEdit.returnPressed.connect(
            self.on_fileNameEdit_returnPressed)
        self.installEventFilter(self)

        self.stopButton = self.buttonBox.addButton(
            self.tr("Stop"), QDialogButtonBox.ActionRole)
        self.project = project
    
    def eventFilter(self, source, event):
        """
        Public method to handle event for another object.
        
        @param source object to handle events for
        @type QObject
        @param event event to handle
        @type QEvent
        @return flag indicating that the event was handled
        @rtype bool
        """
        if event.type() == QEvent.KeyPress:
            
            # Anywhere in the dialog, make hitting escape cancel it
            if event.key() == Qt.Key_Escape:
                self.close()
            
            # Anywhere in the dialog, make hitting up/down choose next item
            # Note: This doesn't really do anything, as other than the text
            #       input there's nothing that doesn't handle up/down already.
            elif event.key() == Qt.Key_Up or event.key() == Qt.Key_Down:
                current = self.fileList.currentItem()
                index = self.fileList.indexOfTopLevelItem(current)
                if event.key() == Qt.Key_Up:
                    if index != 0:
                        self.fileList.setCurrentItem(
                            self.fileList.topLevelItem(index - 1))
                else:
                    if index < (self.fileList.topLevelItemCount() - 1):
                        self.fileList.setCurrentItem(
                            self.fileList.topLevelItem(index + 1))
        return QWidget.eventFilter(self, source, event)

    def on_buttonBox_clicked(self, button):
        """
        Private slot called by a button of the button box clicked.
        
        @param button button that was clicked (QAbstractButton)
        """
        if button == self.stopButton:
            self.shouldStop = True
        elif button == self.buttonBox.button(QDialogButtonBox.Open):
            self.__openFile()
    
    def __openFile(self, itm=None):
        """
        Private slot to open a file.
        
        It emits the signal sourceFile or designerFile depending on the
        file extension.
        
        @param itm item to be opened
        @type QTreeWidgetItem
        @return flag indicating a file was opened
        @rtype bool
        """
        if itm is None:
            itm = self.fileList.currentItem()
        if itm is not None:
            filePath = itm.text(1)
            fileName = itm.text(0)
            fullPath = os.path.join(self.project.ppath, filePath, fileName)
            
            if fullPath.endswith('.ui'):
                self.designerFile.emit(fullPath)
            elif fullPath.endswith(('.ts', '.qm')):
                self.linguistFile.emit(fullPath)
            else:
                self.sourceFile.emit(fullPath)
            return True
        
        return False
    
    def __generateLocations(self):
        """
        Private method to generate a set of locations that can be searched.
        
        @return yields set of files in our project...
        @rtype str
        """
        for typ in ["SOURCES", "FORMS", "INTERFACES", "RESOURCES",
                    "TRANSLATIONS", "OTHERS"]:
            entries = self.project.pdata.get(typ)
            for entry in entries[:]:
                yield entry
    
    def __sortedMatches(self, items, searchTerm):
        """
        Private method to find the subset of items which match a search term.
        
        @param items list of items to be scanned for the search term
        @type list of str
        @param searchTerm search term to be searched for
        @type str
        @return sorted subset of items which match searchTerm in
            relevance order (i.e. the most likely match first)
        @rtype list of tuple of bool, int and str
        """
        fragments = searchTerm.split()
        
        possible = [
            # matches, in_order, file name
        ]
        
        for entry in items:
            count = 0
            match_order = []
            for fragment in fragments:
                index = entry.find(fragment)
                if index == -1:
                    # try case-insensitive match
                    index = entry.lower().find(fragment.lower())
                if index != -1:
                    count += 1
                    match_order.append(index)
            if count:
                record = (count, match_order == sorted(match_order), entry)
                if possible and count < possible[0][0]:
                    # ignore...
                    continue
                elif possible and count > possible[0][0]:
                    # better than all previous matches, discard them and
                    # keep this
                    del possible[:]
                possible.append(record)
        
        ordered = []
        for (_, in_order, name) in possible:
            try:
                age = os.stat(os.path.join(self.project.ppath, name)).st_mtime
            except (IOError, OSError):
                # skipping, because it doesn't appear to exist...
                continue
            ordered.append((
                in_order,    # we want closer match first
                - age,       # then approximately "most recently edited"
                name
            ))
        ordered.sort()
        return ordered

    def __searchFile(self):
        """
        Private slot to handle the search.
        """
        fileName = self.fileNameEdit.text().strip()
        if not fileName:
            self.fileList.clear()
            return
        
        ordered = self.__sortedMatches(self.__generateLocations(), fileName)
        
        found = False
        self.fileList.clear()
        locations = {}

        for in_order, age, name in ordered:
            found = True
            QTreeWidgetItem(self.fileList, [os.path.basename(name),
                                            os.path.dirname(name)])
        QApplication.processEvents()
            
        del locations
        self.stopButton.setEnabled(False)
        self.fileList.header().resizeSections(QHeaderView.ResizeToContents)
        self.fileList.header().setStretchLastSection(True)
        
        if found:
            self.fileList.setCurrentItem(self.fileList.topLevelItem(0))

    def on_fileNameEdit_textChanged(self, text):
        """
        Private slot to handle the textChanged signal of the file name edit.
        
        @param text (ignored)
        """
        self.__searchFile()

    def on_fileNameEdit_returnPressed(self):
        """
        Private slot to handle enter being pressed on the file name edit box.
        """
        if self.__openFile():
            self.close()
    
    def on_fileList_itemActivated(self, itm, column):
        """
        Private slot to handle the double click on a file item.
        
        It emits the signal sourceFile or designerFile depending on the
        file extension.
        
        @param itm the double clicked listview item (QTreeWidgetItem)
        @param column column that was double clicked (integer) (ignored)
        """
        self.__openFile(itm)
    
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_fileList_currentItemChanged(self, current, previous):
        """
        Private slot handling a change of the current item.
        
        @param current current item (QTreeWidgetItem)
        @param previous prevoius current item (QTreeWidgetItem)
        """
        self.buttonBox.button(QDialogButtonBox.Open).setEnabled(
            current is not None)

    def show(self):
        """
        Public method to enable/disable the project checkbox.
        """
        self.fileNameEdit.selectAll()
        self.fileNameEdit.setFocus()
        
        super(QuickFindFileDialog, self).show()
