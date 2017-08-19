# -*- coding: utf-8 -*-

# Copyright (c) 2007 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the data for a new dialog class file.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_NewDialogClassDialog import Ui_NewDialogClassDialog


class NewDialogClassDialog(QDialog, Ui_NewDialogClassDialog):
    """
    Class implementing a dialog to ente the data for a new dialog class file.
    """
    def __init__(self, defaultClassName, defaultFile, defaultPath,
                 parent=None):
        """
        Constructor
        
        @param defaultClassName proposed name for the new class (string)
        @param defaultFile proposed name for the source file (string)
        @param defaultPath default path for the new file (string)
        @param parent parent widget if the dialog (QWidget)
        """
        super(NewDialogClassDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.pathnamePicker.setMode(E5PathPickerModes.DirectoryMode)
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.setEnabled(False)
        
        self.classnameEdit.setText(defaultClassName)
        self.filenameEdit.setText(defaultFile)
        self.pathnamePicker.setText(defaultPath)
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
        
    def __enableOkButton(self):
        """
        Private slot to set the enable state of theok button.
        """
        self.okButton.setEnabled(
            self.classnameEdit.text() != "" and
            self.filenameEdit.text() != "" and
            self.pathnamePicker.text() != "")
        
    def on_classnameEdit_textChanged(self, text):
        """
        Private slot called, when thext of the classname edit has changed.
        
        @param text changed text (string)
        """
        self.__enableOkButton()
        
    def on_filenameEdit_textChanged(self, text):
        """
        Private slot called, when thext of the filename edit has changed.
        
        @param text changed text (string)
        """
        self.__enableOkButton()
        
    def on_pathnamePicker_textChanged(self, text):
        """
        Private slot called, when the text of the path name has changed.
        
        @param text changed text (string)
        """
        self.__enableOkButton()
        
    def getData(self):
        """
        Public method to retrieve the data entered into the dialog.
        
        @return tuple giving the classname (string) and the file name (string)
        """
        return self.classnameEdit.text(), \
            os.path.join(self.pathnamePicker.text(),
                         self.filenameEdit.text())
