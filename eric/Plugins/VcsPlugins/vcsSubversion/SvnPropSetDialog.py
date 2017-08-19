# -*- coding: utf-8 -*-

# Copyright (c) 2003 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the data for a new property.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QDialog

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_SvnPropSetDialog import Ui_SvnPropSetDialog


class SvnPropSetDialog(QDialog, Ui_SvnPropSetDialog):
    """
    Class implementing a dialog to enter the data for a new property.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent parent widget (QWidget)
        """
        super(SvnPropSetDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.propFilePicker.setMode(E5PathPickerModes.OpenFileMode)
        
    def getData(self):
        """
        Public slot used to retrieve the data entered into the dialog.
        
        @return tuple of three values giving the property name, a flag
            indicating a file was selected and the text of the property
            or the selected filename. (string, boolean, string)
        """
        if self.fileRadioButton.isChecked():
            return (self.propNameEdit.text(), True, self.propFilePicker.text())
        else:
            return (self.propNameEdit.text(), False,
                    self.propTextEdit.toPlainText())
