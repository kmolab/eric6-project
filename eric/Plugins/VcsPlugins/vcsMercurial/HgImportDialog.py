# -*- coding: utf-8 -*-

# Copyright (c) 2011 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter data for the Mercurial import command.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, QDateTime
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_HgImportDialog import Ui_HgImportDialog


class HgImportDialog(QDialog, Ui_HgImportDialog):
    """
    Class implementing a dialog to enter data for the Mercurial import command.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(HgImportDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.patchFilePicker.setMode(E5PathPickerModes.OpenFileMode)
        self.patchFilePicker.setFilters(self.tr(
            "Patch Files (*.diff *.patch);;All Files (*)"))
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        self.__initDateTime = QDateTime.currentDateTime()
        self.dateEdit.setDateTime(self.__initDateTime)
    
    def __updateOK(self):
        """
        Private slot to update the OK button.
        """
        enabled = True
        if self.patchFilePicker.text() == "":
            enabled = False
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enabled)
    
    @pyqtSlot(str)
    def on_patchFilePicker_textChanged(self, txt):
        """
        Private slot to react on changes of the patch file edit.
        
        @param txt contents of the line edit (string)
        """
        self.__updateOK()
    
    def getParameters(self):
        """
        Public method to retrieve the import data.
        
        @return tuple naming the patch file, a flag indicating to not commit,
            a commit message, a commit date, a commit user, a strip count and
            a flag indicating to enforce the import
            (string, boolean, string, string, string, integer, boolean)
        """
        if self.dateEdit.dateTime() != self.__initDateTime:
            date = self.dateEdit.dateTime().toString("yyyy-MM-dd hh:mm")
        else:
            date = ""
        
        return (self.patchFilePicker.text(), self.noCommitCheckBox.isChecked(),
                self.messageEdit.toPlainText(), date, self.userEdit.text(),
                self.stripSpinBox.value(), self.forceCheckBox.isChecked())
