# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the data to strip changesets.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from .Ui_HgStripDialog import Ui_HgStripDialog


class HgStripDialog(QDialog, Ui_HgStripDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, tagsList, branchesList, bookmarksList=None, rev="",
                 parent=None):
        """
        Constructor
        
        @param tagsList list of tags
        @type list of str
        @param branchesList list of branches
        @type list of str
        @param bookmarksList list of bookmarks
        @type list of str
        @keyparam rev revision to strip from
        @type str
        @param parent reference to the parent widget
        @type QWidget
        """
        super(HgStripDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.tagCombo.addItems(sorted(tagsList))
        self.branchCombo.addItems(["default"] + sorted(branchesList))
        if bookmarksList is not None:
            self.bookmarkCombo.addItems([""] + sorted(bookmarksList))
        self.idEdit.setText(rev)
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
        
        self.__updateOK()
        
        self.idEdit.setFocus()
    
    def __updateOK(self):
        """
        Private slot to update the OK button.
        """
        enabled = True
        if self.numberButton.isChecked():
            enabled = enabled and self.numberSpinBox.value() >= 0
        elif self.idButton.isChecked():
            enabled = enabled and self.idEdit.text() != ""
        elif self.tagButton.isChecked():
            enabled = enabled and self.tagCombo.currentText() != ""
        elif self.branchButton.isChecked():
            enabled = enabled and self.branchCombo.currentText() != ""
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enabled)
    
    @pyqtSlot(bool)
    def on_numberButton_toggled(self, checked):
        """
        Private slot to handle changes of the Number select button.
        
        @param checked state of the button
        @type bool
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_idButton_toggled(self, checked):
        """
        Private slot to handle changes of the ID select button.
        
        @param checked state of the button
        @type bool
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_tagButton_toggled(self, checked):
        """
        Private slot to handle changes of the Tag select button.
        
        @param checked state of the button
        @type bool
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_branchButton_toggled(self, checked):
        """
        Private slot to handle changes of the Branch select button.
        
        @param checked state of the button
        @type bool
        """
        self.__updateOK()
    
    @pyqtSlot(int)
    def on_numberSpinBox_valueChanged(self, val):
        """
        Private slot to handle changes of the Number spin box.
        
        @param val value of the spin box
        @type int
        """
        self.__updateOK()
    
    @pyqtSlot(str)
    def on_idEdit_textChanged(self, txt):
        """
        Private slot to handle changes of the ID edit.
        
        @param txt text of the edit
        @type str
        """
        self.__updateOK()
    
    @pyqtSlot(str)
    def on_tagCombo_editTextChanged(self, txt):
        """
        Private slot to handle changes of the Tag combo.
        
        @param txt text of the combo
        @type str
        """
        self.__updateOK()
    
    @pyqtSlot(str)
    def on_branchCombo_editTextChanged(self, txt):
        """
        Private slot to handle changes of the Branch combo.
        
        @param txt text of the combo
        @type str
        """
        self.__updateOK()
    
    def __getRevision(self):
        """
        Private method to generate the revision.
        
        @return revision
        @rtype str
        """
        if self.numberButton.isChecked():
            return "rev({0})".format(self.numberSpinBox.value())
        elif self.idButton.isChecked():
            return "id({0})".format(self.idEdit.text())
        elif self.tagButton.isChecked():
            return self.tagCombo.currentText()
        elif self.branchButton.isChecked():
            return self.branchCombo.currentText()
        else:
            # should not happen
            return ""
    
    def getData(self):
        """
        Public method to retrieve the data for the strip action.
        
        @return tuple with the revision, a bookmark name, a flag indicating
            to enforce the strip action, a flag indicating to omit the creation
            of backup bundles and a flag indicating to not modify the working
            directory
        @rtype tuple (str, str, bool, bool, bool)
        """
        return (
            self.__getRevision(),
            self.bookmarkCombo.currentText(),
            self.forceCheckBox.isChecked(),
            self.noBackupCheckBox.isChecked(),
            self.keepCheckBox.isChecked(),
        )
