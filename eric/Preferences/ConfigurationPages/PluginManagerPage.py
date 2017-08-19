# -*- coding: utf-8 -*-

# Copyright (c) 2007 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Plugin Manager configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_PluginManagerPage import Ui_PluginManagerPage

import Preferences


class PluginManagerPage(ConfigurationPageBase, Ui_PluginManagerPage):
    """
    Class implementing the Plugin Manager configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(PluginManagerPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("PluginManagerPage")
        
        self.downloadDirPicker.setMode(E5PathPickerModes.DirectoryMode)
        
        # set initial values
        self.activateExternalPluginsCheckBox.setChecked(
            Preferences.getPluginManager("ActivateExternal"))
        self.downloadDirPicker.setText(
            Preferences.getPluginManager("DownloadPath"))
        self.generationsSpinBox.setValue(
            Preferences.getPluginManager("KeepGenerations"))
        self.keepHiddenCheckBox.setChecked(
            Preferences.getPluginManager("KeepHidden"))
        self.startupCleanupCheckBox.setChecked(
            Preferences.getPluginManager("StartupCleanup"))
        
        period = Preferences.getPluginManager("UpdatesCheckInterval")
        if period == 0:
            self.noCheckRadioButton.setChecked(True)
        elif period == 1:
            self.dailyCheckRadioButton.setChecked(True)
        elif period == 2:
            self.weeklyCheckRadioButton.setChecked(True)
        elif period == 3:
            self.monthlyCheckRadioButton.setChecked(True)
        elif period == 4:
            self.alwaysCheckRadioButton.setChecked(True)
        else:
            # invalid value, default to daily
            self.dailyCheckRadioButton.setChecked(True)
        
        self.downloadedOnlyCheckBox.setChecked(
            Preferences.getPluginManager("CheckInstalledOnly"))
        
        self.__repositoryUrl = Preferences.getUI("PluginRepositoryUrl6")
        self.repositoryUrlEdit.setText(self.__repositoryUrl)
    
    def save(self):
        """
        Public slot to save the Viewmanager configuration.
        """
        Preferences.setPluginManager(
            "ActivateExternal",
            self.activateExternalPluginsCheckBox.isChecked())
        Preferences.setPluginManager(
            "DownloadPath",
            self.downloadDirPicker.text())
        Preferences.setPluginManager(
            "KeepGenerations",
            self.generationsSpinBox.value())
        Preferences.setPluginManager(
            "KeepHidden",
            self.keepHiddenCheckBox.isChecked())
        Preferences.setPluginManager(
            "StartupCleanup",
            self.startupCleanupCheckBox.isChecked())
        
        if self.noCheckRadioButton.isChecked():
            period = 0
        elif self.dailyCheckRadioButton.isChecked():
            period = 1
        elif self.weeklyCheckRadioButton.isChecked():
            period = 2
        elif self.monthlyCheckRadioButton.isChecked():
            period = 3
        elif self.alwaysCheckRadioButton.isChecked():
            period = 4
        Preferences.setPluginManager("UpdatesCheckInterval", period)
        
        Preferences.setPluginManager(
            "CheckInstalledOnly",
            self.downloadedOnlyCheckBox.isChecked())
        
        if self.repositoryUrlEdit.text() != self.__repositoryUrl:
            Preferences.setUI(
                "PluginRepositoryUrl6", self.repositoryUrlEdit.text())
    
    @pyqtSlot(bool)
    def on_repositoryUrlEditButton_toggled(self, checked):
        """
        Private slot to set the read only status of the repository URL line
        edit.
        
        @param checked state of the push button (boolean)
        """
        self.repositoryUrlEdit.setReadOnly(not checked)
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = PluginManagerPage()
    return page
