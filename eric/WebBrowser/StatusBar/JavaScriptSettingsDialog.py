# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the JavaScript settings dialog.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_JavaScriptSettingsDialog import Ui_JavaScriptSettingsDialog

import Preferences


class JavaScriptSettingsDialog(QDialog, Ui_JavaScriptSettingsDialog):
    """
    Class implementing the JavaScript settings dialog.
    
    Note: it contains the JavaScript part of the web browser configuration
    dialog.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(JavaScriptSettingsDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.jsOpenWindowsCheckBox.setChecked(
            Preferences.getWebBrowser("JavaScriptCanOpenWindows"))
        self.jsClipboardCheckBox.setChecked(
            Preferences.getWebBrowser("JavaScriptCanAccessClipboard"))
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    @pyqtSlot()
    def accept(self):
        """
        Public slot to accept the dialog.
        """
        Preferences.setWebBrowser(
            "JavaScriptCanOpenWindows",
            self.jsOpenWindowsCheckBox.isChecked())
        Preferences.setWebBrowser(
            "JavaScriptCanAccessClipboard",
            self.jsClipboardCheckBox.isChecked())
        
        Preferences.syncPreferences()
        
        super(JavaScriptSettingsDialog, self).accept()
