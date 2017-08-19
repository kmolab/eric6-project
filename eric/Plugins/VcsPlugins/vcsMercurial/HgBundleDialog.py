# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the data for a bundle operation.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from .Ui_HgBundleDialog import Ui_HgBundleDialog


class HgBundleDialog(QDialog, Ui_HgBundleDialog):
    """
    Class implementing a dialog to enter the data for a bundle operation.
    """
    def __init__(self, tagsList, branchesList, bookmarksList=None,
                 version=(0, 0, 0), parent=None):
        """
        Constructor
        
        @param tagsList list of tags
        @type list of str
        @param branchesList list of branches
        @type list of str
        @param bookmarksList list of bookmarks
        @type list of str
        @param version Mercurial version info
        @type tuple of three integers
        @param parent parent widget
        @type QWidget
        """
        super(HgBundleDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        self.__version = version
        
        bundleTypes = ["", "bzip2", "gzip", "none"]
        if version >= (4, 1, 0):
            bundleTypes.insert(-1, "zstd")
        self.compressionCombo.addItems(bundleTypes)
        self.tagCombo.addItems(sorted(tagsList))
        self.branchCombo.addItems(["default"] + sorted(branchesList))
        if bookmarksList is not None:
            self.bookmarkCombo.addItems(sorted(bookmarksList))
        else:
            self.bookmarkButton.setHidden(True)
            self.bookmarkCombo.setHidden(True)
    
    def __updateOK(self):
        """
        Private slot to update the OK button.
        """
        enabled = True
        if self.multipleButton.isChecked():
            enabled = self.multipleEdit.toPlainText() != ""
        elif self.tagButton.isChecked():
            enabled = self.tagCombo.currentText() != ""
        elif self.branchButton.isChecked():
            enabled = self.branchCombo.currentText() != ""
        elif self.bookmarkButton.isChecked():
            enabled = self.bookmarkCombo.currentText() != ""
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enabled)
    
    @pyqtSlot(bool)
    def on_multipleButton_toggled(self, checked):
        """
        Private slot to handle changes of the Multiple select button.
        
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
    def on_branchButton_toggled(self, checked):
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
    
    @pyqtSlot()
    def on_multipleEdit_textChanged(self):
        """
        Private slot to handle changes of the Multiple edit.
        """
        self.__updateOK()
    
    @pyqtSlot(str)
    def on_tagCombo_editTextChanged(self, txt):
        """
        Private slot to handle changes of the Tag combo.
        
        @param txt text of the combo (string)
        """
        self.__updateOK()
    
    @pyqtSlot(str)
    def on_branchCombo_editTextChanged(self, txt):
        """
        Private slot to handle changes of the Branch combo.
        
        @param txt text of the combo (string)
        """
        self.__updateOK()
    
    @pyqtSlot(str)
    def on_bookmarkCombo_editTextChanged(self, txt):
        """
        Private slot to handle changes of the Bookmark combo.
        
        @param txt text of the combo (string)
        """
        self.__updateOK()
    
    def getParameters(self):
        """
        Public method to retrieve the bundle data.
        
        @return tuple naming the revisions, base revisions, the compression
            type and a flag indicating to bundle all changesets (string,
            string, boolean)
        """
        if self.multipleButton.isChecked():
            revs = [rev.strip() for rev in
                    self.multipleEdit.toPlainText().strip().splitlines()
                    if rev.strip()]
        elif self.tagButton.isChecked():
            revs = [self.tagCombo.currentText()]
        elif self.branchButton.isChecked():
            revs = [self.branchCombo.currentText()]
        elif self.bookmarkButton.isChecked():
            revs = [self.bookmarkCombo.currentText()]
        else:
            revs = []
        
        baseRevs = [rev.strip() for rev in
                    self.baseRevisionsEdit.toPlainText().strip().splitlines()
                    if rev.strip()]
        
        bundleType = self.compressionCombo.currentText()
        if bundleType == "zstd":
            bundleType += "-v2"
        
        return (revs, baseRevs, bundleType, self.allCheckBox.isChecked())
