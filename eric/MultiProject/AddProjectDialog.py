# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the add project dialog.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_AddProjectDialog import Ui_AddProjectDialog

import Utilities


class AddProjectDialog(QDialog, Ui_AddProjectDialog):
    """
    Class implementing the add project dialog.
    """
    def __init__(self, parent=None, startdir=None, project=None,
                 categories=None):
        """
        Constructor
        
        @param parent parent widget of this dialog (QWidget)
        @param startdir start directory for the selection dialog (string)
        @param project dictionary containing project data
        @param categories list of already used categories (list of string)
        """
        super(AddProjectDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.filenamePicker.setMode(E5PathPickerModes.OpenFileMode)
        self.filenamePicker.setFilters(self.tr("Project Files (*.e4p)"))
        
        if categories:
            self.categoryComboBox.addItem("")
            self.categoryComboBox.addItems(sorted(categories))
        
        self.startdir = startdir
        self.uid = ""
        
        self.__okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.__okButton.setEnabled(False)
        
        if project is not None:
            self.setWindowTitle(self.tr("Project Properties"))
            
            self.nameEdit.setText(project['name'])
            self.filenamePicker.setText(project['file'])
            self.descriptionEdit.setPlainText(project['description'])
            self.masterCheckBox.setChecked(project['master'])
            index = self.categoryComboBox.findText(project['category'])
            if index == -1:
                index = 0
            self.categoryComboBox.setCurrentIndex(index)
            self.uid = project["uid"]
    
    def getData(self):
        """
        Public slot to retrieve the dialogs data.
        
        @return tuple of five values (string, string, boolean, string, string)
            giving the project name, the name of the project file, a flag
            telling whether the project shall be the main project, a short
            description for the project and the project category
        """
        if not self.uid:
            # new project entry
            from PyQt5.QtCore import QUuid
            self.uid = QUuid.createUuid().toString()
        
        filename = self.filenamePicker.text()
        if not os.path.isabs(filename):
            filename = Utilities.toNativeSeparators(
                os.path.join(self.startdir, filename))
        return (self.nameEdit.text(),
                filename,
                self.masterCheckBox.isChecked(),
                self.descriptionEdit.toPlainText(),
                self.categoryComboBox.currentText(),
                self.uid)
    
    @pyqtSlot(str)
    def on_nameEdit_textChanged(self, txt):
        """
        Private slot called when the project name has changed.
        
        @param txt text of the edit (string)
        """
        self.__updateUi()
    
    @pyqtSlot(str)
    def on_filenamePicker_textChanged(self, txt):
        """
        Private slot called when the project filename has changed.
        
        @param txt text of the edit (string)
        """
        self.__updateUi()
    
    def __updateUi(self):
        """
        Private method to update the dialog.
        """
        self.__okButton.setEnabled(self.nameEdit.text() != "" and
                                   self.filenamePicker.text() != "")
