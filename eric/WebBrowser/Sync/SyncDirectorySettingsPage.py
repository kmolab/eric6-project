# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the synchronization shared directory settings wizard page.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QWizardPage

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_SyncDirectorySettingsPage import Ui_SyncDirectorySettingsPage

import Preferences


class SyncDirectorySettingsPage(QWizardPage, Ui_SyncDirectorySettingsPage):
    """
    Class implementing the shared directory host settings wizard page.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(SyncDirectorySettingsPage, self).__init__(parent)
        self.setupUi(self)
        
        self.directoryPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.directoryPicker.setText(
            Preferences.getWebBrowser("SyncDirectoryPath"))
        
        self.directoryPicker.textChanged.connect(self.completeChanged)
    
    def nextId(self):
        """
        Public method returning the ID of the next wizard page.
        
        @return next wizard page ID (integer)
        """
        # save the settings
        Preferences.setWebBrowser(
            "SyncDirectoryPath", self.directoryPicker.text())
        
        from . import SyncGlobals
        return SyncGlobals.PageCheck
    
    def isComplete(self):
        """
        Public method to check the completeness of the page.
        
        @return flag indicating completeness (boolean)
        """
        return self.directoryPicker.text() != ""
