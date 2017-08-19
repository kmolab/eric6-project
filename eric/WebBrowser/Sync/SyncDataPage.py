# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the synchronization data wizard page.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QWizardPage

from .Ui_SyncDataPage import Ui_SyncDataPage

import Preferences


class SyncDataPage(QWizardPage, Ui_SyncDataPage):
    """
    Class implementing the synchronization data wizard page.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(SyncDataPage, self).__init__(parent)
        self.setupUi(self)
        
        self.bookmarksCheckBox.setChecked(
            Preferences.getWebBrowser("SyncBookmarks"))
        self.historyCheckBox.setChecked(
            Preferences.getWebBrowser("SyncHistory"))
        self.passwordsCheckBox.setChecked(
            Preferences.getWebBrowser("SyncPasswords"))
        self.userAgentsCheckBox.setChecked(
            Preferences.getWebBrowser("SyncUserAgents"))
        self.speedDialCheckBox.setChecked(
            Preferences.getWebBrowser("SyncSpeedDial"))
        
        self.activeCheckBox.setChecked(
            Preferences.getWebBrowser("SyncEnabled"))
    
    def nextId(self):
        """
        Public method returning the ID of the next wizard page.
        
        @return next wizard page ID (integer)
        """
        # save the settings
        Preferences.setWebBrowser(
            "SyncEnabled", self.activeCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "SyncBookmarks", self.bookmarksCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SyncHistory", self.historyCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SyncPasswords", self.passwordsCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SyncUserAgents", self.userAgentsCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SyncSpeedDial", self.speedDialCheckBox.isChecked())
        
        from . import SyncGlobals
        if self.activeCheckBox.isChecked():
            return SyncGlobals.PageEncryption
        else:
            return SyncGlobals.PageCheck
