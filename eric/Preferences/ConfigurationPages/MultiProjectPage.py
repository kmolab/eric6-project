# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Multi Project configuration page.
"""

from __future__ import unicode_literals

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_MultiProjectPage import Ui_MultiProjectPage

from E5Gui.E5PathPicker import E5PathPickerModes

import Preferences
import Utilities


class MultiProjectPage(ConfigurationPageBase, Ui_MultiProjectPage):
    """
    Class implementing the Multi Project configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(MultiProjectPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("MultiProjectPage")
        
        self.workspacePicker.setMode(E5PathPickerModes.DirectoryMode)
        
        # set initial values
        self.openMasterAutomaticallyCheckBox.setChecked(
            Preferences.getMultiProject("OpenMasterAutomatically"))
        self.multiProjectTimestampCheckBox.setChecked(
            Preferences.getMultiProject("XMLTimestamp"))
        self.multiProjectRecentSpinBox.setValue(
            Preferences.getMultiProject("RecentNumber"))
        self.workspacePicker.setText(
            Utilities.toNativeSeparators(
                Preferences.getMultiProject("Workspace") or
                Utilities.getHomeDir()))
        
    def save(self):
        """
        Public slot to save the Project configuration.
        """
        Preferences.setMultiProject(
            "OpenMasterAutomatically",
            self.openMasterAutomaticallyCheckBox.isChecked())
        Preferences.setMultiProject(
            "XMLTimestamp",
            self.multiProjectTimestampCheckBox.isChecked())
        Preferences.setMultiProject(
            "RecentNumber",
            self.multiProjectRecentSpinBox.value())
        Preferences.setMultiProject(
            "Workspace",
            self.workspacePicker.text())
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = MultiProjectPage()
    return page
