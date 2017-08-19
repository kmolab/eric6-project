# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to add files of a directory to the project.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_AddDirectoryDialog import Ui_AddDirectoryDialog


class AddDirectoryDialog(QDialog, Ui_AddDirectoryDialog):
    """
    Class implementing a dialog to add files of a directory to the project.
    """
    def __init__(self, pro, fileTypeFilter='source', parent=None, name=None,
                 startdir=None):
        """
        Constructor
        
        @param pro reference to the project object
        @param fileTypeFilter file type filter (string)
        @param parent parent widget of this dialog (QWidget)
        @param name name of this dialog (string)
        @param startdir start directory for the selection dialog
        """
        super(AddDirectoryDialog, self).__init__(parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        
        self.sourceDirPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.sourceDirPicker.setDefaultDirectory(startdir)
        self.targetDirPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.targetDirPicker.setDefaultDirectory(startdir)
        
        self.ppath = pro.ppath
        self.targetDirPicker.setText(self.ppath)
        self.on_filterComboBox_highlighted('(*.py)')
        # enable all dialog elements
        if fileTypeFilter == 'source':  # it is a source file
            self.filterComboBox.addItem(
                self.tr("Source Files"), "SOURCES")
        elif fileTypeFilter == 'form':
            self.filterComboBox.addItem(
                self.tr("Forms Files"), "FORMS")
        elif fileTypeFilter == 'resource':
            self.filterComboBox.addItem(
                self.tr("Resource Files"), "RESOURCES")
        elif fileTypeFilter == 'interface':
            self.filterComboBox.addItem(
                self.tr("Interface Files"), "INTERFACES")
        elif fileTypeFilter == 'others':
            self.filterComboBox.addItem(
                self.tr("Other Files (*)"), "OTHERS")
            self.on_filterComboBox_highlighted('(*)')
        else:
            self.filterComboBox.addItem(
                self.tr("Source Files"), "SOURCES")
            self.filterComboBox.addItem(
                self.tr("Forms Files"), "FORMS")
            self.filterComboBox.addItem(
                self.tr("Resource Files"), "RESOURCES")
            self.filterComboBox.addItem(
                self.tr("Interface Files"), "INTERFACES")
            self.filterComboBox.addItem(
                self.tr("Other Files (*)"), "OTHERS")
        self.filterComboBox.setCurrentIndex(0)
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
        
    @pyqtSlot(str)
    def on_filterComboBox_highlighted(self, fileType):
        """
        Private slot to handle the selection of a file type.
        
        @param fileType the selected file type (string)
        """
        if fileType.endswith('(*)'):
            self.targetDirLabel.setEnabled(False)
            self.targetDirPicker.setEnabled(False)
            self.recursiveCheckBox.setEnabled(False)
        else:
            self.targetDirLabel.setEnabled(True)
            self.targetDirPicker.setEnabled(True)
            self.recursiveCheckBox.setEnabled(True)
        
    @pyqtSlot(str)
    def on_sourceDirPicker_textChanged(self, directory):
        """
        Private slot to handle the source directory text changed.
        
        If the entered source directory is a subdirectory of the current
        projects main directory, the target directory path is synchronized.
        It is assumed, that the user wants to add a bunch of files to
        the project in place.
        
        @param directory the text of the source directory line edit (string)
        """
        if directory.startswith(self.ppath):
            self.targetDirPicker.setText(directory)
        
    def getData(self):
        """
        Public slot to retrieve the dialogs data.
        
        @return tuple of four values (string, string, string, boolean) giving
            the selected file type, the source and target directory and
            a flag indicating a recursive add
        """
        filetype = \
            self.filterComboBox.itemData(self.filterComboBox.currentIndex())
        return (
            filetype,
            self.sourceDirPicker.text(),
            self.targetDirPicker.text(),
            self.recursiveCheckBox.isChecked())
