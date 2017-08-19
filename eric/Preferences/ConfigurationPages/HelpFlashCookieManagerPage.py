# -*- coding: utf-8 -*-

# Copyright (c) 2015 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Flash Cookies Manager configuration page.
"""

from __future__ import unicode_literals

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_HelpFlashCookieManagerPage import Ui_HelpFlashCookieManagerPage

import Preferences


class HelpFlashCookieManagerPage(ConfigurationPageBase,
                                 Ui_HelpFlashCookieManagerPage):
    """
    Class implementing the Flash Cookies Manager configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(HelpFlashCookieManagerPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("HelpFlashCookieManagerPage")
        
        self.flashDataPathPicker.setMode(E5PathPickerModes.DirectoryMode)
        
        # set initial values
        self.flashDataPathPicker.setText(
            Preferences.getHelp("FlashCookiesDataPath"))
        self.autoModeGroup.setChecked(
            Preferences.getHelp("FlashCookieAutoRefresh"))
        self.notificationGroup.setChecked(
            Preferences.getHelp("FlashCookieNotify"))
        self.deleteGroup.setChecked(
            Preferences.getHelp("FlashCookiesDeleteOnStartExit"))
    
    def save(self):
        """
        Public slot to save the Flash Cookies Manager configuration.
        """
        Preferences.setHelp("FlashCookiesDataPath",
                            self.flashDataPathPicker.text())
        Preferences.setHelp("FlashCookieAutoRefresh",
                            self.autoModeGroup.isChecked())
        Preferences.setHelp("FlashCookieNotify",
                            self.notificationGroup.isChecked())
        Preferences.setHelp("FlashCookiesDeleteOnStartExit",
                            self.deleteGroup.isChecked())
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = HelpFlashCookieManagerPage()
    return page
