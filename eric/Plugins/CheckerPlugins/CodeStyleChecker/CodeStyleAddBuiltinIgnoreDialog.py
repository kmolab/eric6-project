# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the data for a built-in assignment to
be ignored.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from .Ui_CodeStyleAddBuiltinIgnoreDialog import \
    Ui_CodeStyleAddBuiltinIgnoreDialog


class CodeStyleAddBuiltinIgnoreDialog(QDialog,
                                      Ui_CodeStyleAddBuiltinIgnoreDialog):
    """
    Class implementing a dialog to enter the data for a built-in assignment to
    be ignored.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CodeStyleAddBuiltinIgnoreDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.__updateOkButton
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    def __updateOkButton(self):
        """
        Private slot to set the state of the OK button.
        """
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            bool(self.leftEdit.text()) and
            bool(self.rightEdit.text()))
    
    @pyqtSlot(str)
    def on_leftEdit_textChanged(self, txt):
        """
        Private slot to handle a change of the text of the left side edit.
        
        @param txt text of the line edit
        @type str
        """
        self.__updateOkButton()
    
    @pyqtSlot(str)
    def on_rightEdit_textChanged(self, txt):
        """
        Private slot to handle a change of the text of the right side edit.
        
        @param txt text of the line edit
        @type str
        """
        self.__updateOkButton()
    
    def getData(self):
        """
        Public method to get the entered data.
        
        @return tuple containing the left and right hand side of the assignment
        @rtype tuple of two str
        """
        return self.leftEdit.text(), self.rightEdit.text()
