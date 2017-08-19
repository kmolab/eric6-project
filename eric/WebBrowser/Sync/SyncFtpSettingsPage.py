# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the synchronization FTP host settings wizard page.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QWizardPage

from .Ui_SyncFtpSettingsPage import Ui_SyncFtpSettingsPage

import Preferences


class SyncFtpSettingsPage(QWizardPage, Ui_SyncFtpSettingsPage):
    """
    Class implementing the synchronization FTP host settings wizard page.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(SyncFtpSettingsPage, self).__init__(parent)
        self.setupUi(self)
        
        self.serverEdit.setText(Preferences.getWebBrowser("SyncFtpServer"))
        self.userNameEdit.setText(Preferences.getWebBrowser("SyncFtpUser"))
        self.passwordEdit.setText(Preferences.getWebBrowser("SyncFtpPassword"))
        self.pathEdit.setText(Preferences.getWebBrowser("SyncFtpPath"))
        self.portSpinBox.setValue(Preferences.getWebBrowser("SyncFtpPort"))
        self.idleSpinBox.setValue(
            Preferences.getWebBrowser("SyncFtpIdleTimeout"))
        
        self.serverEdit.textChanged.connect(self.completeChanged)
        self.userNameEdit.textChanged.connect(self.completeChanged)
        self.passwordEdit.textChanged.connect(self.completeChanged)
        self.pathEdit.textChanged.connect(self.completeChanged)
    
    def nextId(self):
        """
        Public method returning the ID of the next wizard page.
        
        @return next wizard page ID (integer)
        """
        # save the settings
        Preferences.setWebBrowser("SyncFtpServer", self.serverEdit.text())
        Preferences.setWebBrowser("SyncFtpUser", self.userNameEdit.text())
        Preferences.setWebBrowser("SyncFtpPassword", self.passwordEdit.text())
        Preferences.setWebBrowser("SyncFtpPath", self.pathEdit.text())
        Preferences.setWebBrowser("SyncFtpPort", self.portSpinBox.value())
        Preferences.setWebBrowser("SyncFtpIdleTimeout",
                                  self.idleSpinBox.value())
        
        from . import SyncGlobals
        return SyncGlobals.PageCheck
    
    def isComplete(self):
        """
        Public method to check the completeness of the page.
        
        @return flag indicating completeness (boolean)
        """
        return self.serverEdit.text() != "" and \
            self.userNameEdit.text() != "" and \
            self.passwordEdit.text() != "" and \
            self.pathEdit.text() != ""
