# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Mercurial configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot

from Preferences.ConfigurationPages.ConfigurationPageBase import \
    ConfigurationPageBase
from .Ui_MercurialPage import Ui_MercurialPage

from Utilities import supportedCodecs


class MercurialPage(ConfigurationPageBase, Ui_MercurialPage):
    """
    Class implementing the Mercurial configuration page.
    """
    def __init__(self, plugin):
        """
        Constructor
        
        @param plugin reference to the plugin object
        """
        super(MercurialPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("MercurialPage")
        
        self.__plugin = plugin
        
        self.encodingComboBox.addItems(sorted(supportedCodecs))
        self.encodingModeComboBox.addItems(["strict", "ignore", "replace"])
        
        # set initial values
        # global options
        index = self.encodingComboBox.findText(
            self.__plugin.getPreferences("Encoding"))
        self.encodingComboBox.setCurrentIndex(index)
        index = self.encodingModeComboBox.findText(
            self.__plugin.getPreferences("EncodingMode"))
        self.encodingModeComboBox.setCurrentIndex(index)
        self.hiddenChangesetsCheckBox.setChecked(
            self.__plugin.getPreferences("ConsiderHidden"))
        # log
        self.logSpinBox.setValue(
            self.__plugin.getPreferences("LogLimit"))
        self.logWidthSpinBox.setValue(
            self.__plugin.getPreferences("LogMessageColumnWidth"))
        # commit
        self.commitSpinBox.setValue(
            self.__plugin.getPreferences("CommitMessages"))
        self.commitAuthorsSpinBox.setValue(
            self.__plugin.getPreferences("CommitAuthorsLimit"))
        # pull
        self.pullUpdateCheckBox.setChecked(
            self.__plugin.getPreferences("PullUpdate"))
        self.preferUnbundleCheckBox.setChecked(
            self.__plugin.getPreferences("PreferUnbundle"))
        # cleanup
        self.cleanupPatternEdit.setText(
            self.__plugin.getPreferences("CleanupPatterns"))
        # revert
        self.backupCheckBox.setChecked(
            self.__plugin.getPreferences("CreateBackup"))
        # merge
        self.internalMergeCheckBox.setChecked(
            self.__plugin.getPreferences("InternalMerge"))
    
    def save(self):
        """
        Public slot to save the Mercurial configuration.
        """
        # global options
        self.__plugin.setPreferences(
            "Encoding", self.encodingComboBox.currentText())
        self.__plugin.setPreferences(
            "EncodingMode", self.encodingModeComboBox.currentText())
        self.__plugin.setPreferences(
            "ConsiderHidden", self.hiddenChangesetsCheckBox.isChecked())
        # log
        self.__plugin.setPreferences(
            "LogLimit", self.logSpinBox.value())
        self.__plugin.setPreferences(
            "LogMessageColumnWidth", self.logWidthSpinBox.value())
        # commit
        self.__plugin.setPreferences(
            "CommitMessages", self.commitSpinBox.value())
        self.__plugin.setPreferences(
            "CommitAuthorsLimit", self.commitAuthorsSpinBox.value())
        # pull
        self.__plugin.setPreferences(
            "PullUpdate", self.pullUpdateCheckBox.isChecked())
        self.__plugin.setPreferences(
            "PreferUnbundle", self.preferUnbundleCheckBox.isChecked())
        # cleanup
        self.__plugin.setPreferences(
            "CleanupPatterns", self.cleanupPatternEdit.text())
        # revert
        self.__plugin.setPreferences(
            "CreateBackup", self.backupCheckBox.isChecked())
        # merge
        self.__plugin.setPreferences(
            "InternalMerge", self.internalMergeCheckBox.isChecked())
    
    @pyqtSlot()
    def on_configButton_clicked(self):
        """
        Private slot to edit the (per user) Mercurial configuration file.
        """
        from ..HgUserConfigDialog import HgUserConfigDialog
        from ..HgUtilities import hgVersion
        
        dlg = HgUserConfigDialog(version=hgVersion(self.__plugin)[1])
        dlg.exec_()
