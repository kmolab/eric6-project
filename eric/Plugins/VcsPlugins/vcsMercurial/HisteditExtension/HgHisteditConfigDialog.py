# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the histedit parameters.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QButtonGroup

from .Ui_HgHisteditConfigDialog import Ui_HgHisteditConfigDialog


class HgHisteditConfigDialog(QDialog, Ui_HgHisteditConfigDialog):
    """
    Class implementing a dialog to enter the histedit parameters.
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
        super(HgHisteditConfigDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.__sourceRevisionButtonGroup = QButtonGroup(self)
        self.__sourceRevisionButtonGroup.addButton(self.defaultButton)
        self.__sourceRevisionButtonGroup.addButton(self.outgoingButton)
        self.__sourceRevisionButtonGroup.addButton(self.revisionButton)
        
        self.tagCombo.addItems(sorted(tagsList))
        self.branchCombo.addItems(["default"] + sorted(branchesList))
        if bookmarksList is not None:
            self.bookmarkCombo.addItems(sorted(bookmarksList))
        
        self.idEdit.setText(rev)
        if rev:
            self.revisionButton.setChecked(True)
        else:
            self.defaultButton.setChecked(True)
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
        
        self.__updateOK()
    
    def __updateOK(self):
        """
        Private slot to update the OK button.
        """
        enabled = True
        
        if self.revisionButton.isChecked():
            if self.idButton.isChecked():
                enabled = enabled and bool(self.idEdit.text())
            elif self.tagButton.isChecked():
                enabled = enabled and bool(self.tagCombo.currentText())
            elif self.branchButton.isChecked():
                enabled = enabled and bool(self.branchCombo.currentText())
            elif self.bookmarkButton.isChecked():
                enabled = enabled and bool(self.bookmarkCombo.currentText())
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enabled)
    
    @pyqtSlot(bool)
    def on_defaultButton_toggled(self, checked):
        """
        Private slot to handle changes of the Default select button.
        
        @param checked state of the button
        @type bool
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_outgoingButton_toggled(self, checked):
        """
        Private slot to handle changes of the Outgoing select button.
        
        @param checked state of the button
        @type bool
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_revisionButton_toggled(self, checked):
        """
        Private slot to handle changes of the Revision select button.
        
        @param checked state of the button
        @type bool
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_idButton_toggled(self, checked):
        """
        Private slot to handle changes of the ID select button.
        
        @param checked state of the button (boolean)
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_tagButton_toggled(self, checked):
        """
        Private slot to handle changes of the Tag select button.
        
        @param checked state of the button (boolean)
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_branch1Button_toggled(self, checked):
        """
        Private slot to handle changes of the Branch select button.
        
        @param checked state of the button (boolean)
        """
        self.__updateOK()
    
    @pyqtSlot(bool)
    def on_bookmarkButton_toggled(self, checked):
        """
        Private slot to handle changes of the Bookmark select button.
        
        @param checked state of the button (boolean)
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
    
    @pyqtSlot(str)
    def on_bookmarkCombo_editTextChanged(self, txt):
        """
        Private slot to handle changes of the Bookmark combo.
        
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
        if self.defaultButton.isChecked():
            return ""
        elif self.outgoingButton.isChecked():
            return "--outgoing"
        else:
            # self.revisionButton.isChecked()
            if self.numberButton.isChecked():
                return "rev({0})".format(self.numberSpinBox.value())
            elif self.idButton.isChecked():
                return "id({0})".format(self.idEdit.text())
            elif self.tagButton.isChecked():
                return self.tagCombo.currentText()
            elif self.branchButton.isChecked():
                return self.branchCombo.currentText()
            elif self.bookmarkButton.isChecked():
                return self.bookmarkCombo.currentText()
    
    def getData(self):
        """
        Public method to retrieve the data for the strip action.
        
        @return tuple with the revision, a flag indicating to to outgoing and a
            flag indicating to keep old nodes
        @rtype tuple (str, bool, bool)
        """
        return (
            self.__getRevision(),
            self.forceCheckBox.isChecked(),
            self.keepCheckBox.isChecked(),
        )
