# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Icons configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QListWidgetItem

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_IconsPage import Ui_IconsPage

import Preferences


class IconsPage(ConfigurationPageBase, Ui_IconsPage):
    """
    Class implementing the Icons configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(IconsPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("IconsPage")
        
        self.iconDirectoryPicker.setMode(E5PathPickerModes.DirectoryMode)
        
        # set initial values
        dirList = Preferences.getIcons("Path")[:]
        for directory in dirList:
            if directory:
                QListWidgetItem(directory, self.iconDirectoryList)
        
    def save(self):
        """
        Public slot to save the Icons configuration.
        """
        dirList = []
        for i in range(self.iconDirectoryList.count()):
            dirList.append(self.iconDirectoryList.item(i).text())
        Preferences.setIcons("Path", dirList)
        
    def on_iconDirectoryList_currentRowChanged(self, row):
        """
        Private slot to handle the currentRowChanged signal of the icons
        directory list.
        
        @param row the current row (integer)
        """
        if row == -1:
            self.deleteIconDirectoryButton.setEnabled(False)
            self.upButton.setEnabled(False)
            self.downButton.setEnabled(False)
            self.showIconsButton.setEnabled(
                self.iconDirectoryPicker.text() != "")
        else:
            maxIndex = self.iconDirectoryList.count() - 1
            self.upButton.setEnabled(row != 0)
            self.downButton.setEnabled(row != maxIndex)
            self.deleteIconDirectoryButton.setEnabled(True)
            self.showIconsButton.setEnabled(True)
        
    def on_iconDirectoryPicker_textChanged(self, txt):
        """
        Private slot to handle the textChanged signal of the directory picker.
        
        @param txt the text of the directory picker (string)
        """
        self.addIconDirectoryButton.setEnabled(txt != "")
        self.showIconsButton.setEnabled(
            txt != "" or
            self.iconDirectoryList.currentRow() != -1)
        
    @pyqtSlot()
    def on_upButton_clicked(self):
        """
        Private slot called to move the selected item up in the list.
        """
        row = self.iconDirectoryList.currentRow()
        if row == 0:
            # we're already at the top
            return
        
        itm = self.iconDirectoryList.takeItem(row)
        self.iconDirectoryList.insertItem(row - 1, itm)
        self.iconDirectoryList.setCurrentItem(itm)
        if row == 1:
            self.upButton.setEnabled(False)
        else:
            self.upButton.setEnabled(True)
        self.downButton.setEnabled(True)
        
    @pyqtSlot()
    def on_downButton_clicked(self):
        """
        Private slot called to move the selected item down in the list.
        """
        rows = self.iconDirectoryList.count()
        row = self.iconDirectoryList.currentRow()
        if row == rows - 1:
            # we're already at the end
            return
        
        itm = self.iconDirectoryList.takeItem(row)
        self.iconDirectoryList.insertItem(row + 1, itm)
        self.iconDirectoryList.setCurrentItem(itm)
        self.upButton.setEnabled(True)
        if row == rows - 2:
            self.downButton.setEnabled(False)
        else:
            self.downButton.setEnabled(True)
        
    @pyqtSlot()
    def on_addIconDirectoryButton_clicked(self):
        """
        Private slot to add the icon directory displayed to the listbox.
        """
        directory = self.iconDirectoryPicker.text()
        if directory:
            QListWidgetItem(directory, self.iconDirectoryList)
            self.iconDirectoryPicker.clear()
        row = self.iconDirectoryList.currentRow()
        self.on_iconDirectoryList_currentRowChanged(row)
        
    @pyqtSlot()
    def on_deleteIconDirectoryButton_clicked(self):
        """
        Private slot to delete the currently selected directory of the listbox.
        """
        row = self.iconDirectoryList.currentRow()
        itm = self.iconDirectoryList.takeItem(row)
        del itm
        row = self.iconDirectoryList.currentRow()
        self.on_iconDirectoryList_currentRowChanged(row)
        
    @pyqtSlot()
    def on_showIconsButton_clicked(self):
        """
        Private slot to display a preview of an icons directory.
        """
        directory = self.iconDirectoryPicker.text()
        if not directory:
            itm = self.iconDirectoryList.currentItem()
            if itm is not None:
                directory = itm.text()
        if directory:
            from .IconsPreviewDialog import IconsPreviewDialog
            dlg = IconsPreviewDialog(self, directory)
            dlg.exec_()
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = IconsPage()
    return page
