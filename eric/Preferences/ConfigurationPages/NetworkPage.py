# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Network configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot

from E5Gui.E5PathPicker import E5PathPickerModes

from E5Network.E5Ftp import E5FtpProxyType

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_NetworkPage import Ui_NetworkPage

import Preferences


class NetworkPage(ConfigurationPageBase, Ui_NetworkPage):
    """
    Class implementing the Network configuration page.
    """
    def __init__(self, configDialog):
        """
        Constructor
        
        @param configDialog reference to the configuration dialog
            (ConfigurationDialog)
        """
        super(NetworkPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("NetworkPage")
        
        self.__configDlg = configDialog
        self.__displayMode = None
        self.__webEngine = False
        self.__webKit = False
        
        self.downloadDirPicker.setMode(E5PathPickerModes.DirectoryMode)
        
        self.ftpProxyTypeCombo.addItem(
            self.tr("No FTP Proxy"), E5FtpProxyType.NoProxy)
        self.ftpProxyTypeCombo.addItem(
            self.tr("No Proxy Authentication required"),
            E5FtpProxyType.NonAuthorizing)
        self.ftpProxyTypeCombo.addItem(
            self.tr("User@Server"), E5FtpProxyType.UserAtServer)
        self.ftpProxyTypeCombo.addItem(
            self.tr("SITE"), E5FtpProxyType.Site)
        self.ftpProxyTypeCombo.addItem(
            self.tr("OPEN"), E5FtpProxyType.Open)
        self.ftpProxyTypeCombo.addItem(
            self.tr("User@Proxyuser@Server"),
            E5FtpProxyType.UserAtProxyuserAtServer)
        self.ftpProxyTypeCombo.addItem(
            self.tr("Proxyuser@Server"), E5FtpProxyType.ProxyuserAtServer)
        self.ftpProxyTypeCombo.addItem(
            self.tr("AUTH and RESP"), E5FtpProxyType.AuthResp)
        self.ftpProxyTypeCombo.addItem(
            self.tr("Bluecoat Proxy"), E5FtpProxyType.Bluecoat)
        
        # set initial values
        self.dynamicOnlineCheckBox.setChecked(
            Preferences.getUI("DynamicOnlineCheck"))
        self.downloadDirPicker.setText(Preferences.getUI("DownloadPath"))
        self.requestFilenameCheckBox.setChecked(
            Preferences.getUI("RequestDownloadFilename"))
        
        # HTTP proxy
        self.httpProxyHostEdit.setText(
            Preferences.getUI("ProxyHost/Http"))
        self.httpProxyPortSpin.setValue(
            Preferences.getUI("ProxyPort/Http"))
        
        # HTTPS proxy
        self.httpsProxyHostEdit.setText(
            Preferences.getUI("ProxyHost/Https"))
        self.httpsProxyPortSpin.setValue(
            Preferences.getUI("ProxyPort/Https"))
        
        # FTP proxy
        self.ftpProxyHostEdit.setText(
            Preferences.getUI("ProxyHost/Ftp"))
        self.ftpProxyPortSpin.setValue(
            Preferences.getUI("ProxyPort/Ftp"))
        self.ftpProxyTypeCombo.setCurrentIndex(
            self.ftpProxyTypeCombo.findData(
                Preferences.getUI("ProxyType/Ftp")))
        self.ftpProxyUserEdit.setText(
            Preferences.getUI("ProxyUser/Ftp"))
        self.ftpProxyPasswordEdit.setText(
            Preferences.getUI("ProxyPassword/Ftp"))
        self.ftpProxyAccountEdit.setText(
            Preferences.getUI("ProxyAccount/Ftp"))
        
        self.httpProxyForAllCheckBox.setChecked(
            Preferences.getUI("UseHttpProxyForAll"))
        if not Preferences.getUI("UseProxy"):
            self.noProxyButton.setChecked(True)
        elif Preferences.getUI("UseSystemProxy"):
            self.systemProxyButton.setChecked(True)
        else:
            self.manualProxyButton.setChecked(True)
        
        self.exceptionsEdit.setText(
            ", ".join(Preferences.getUI("ProxyExceptions").split(",")))
    
    def setMode(self, displayMode):
        """
        Public method to perform mode dependent setups.
        
        @param displayMode mode of the configuration dialog
            (ConfigurationWidget.DefaultMode,
             ConfigurationWidget.HelpBrowserMode,
             ConfigurationWidget.WebBrowserMode)
        """
        from ..ConfigurationDialog import ConfigurationWidget
        assert displayMode in (
            ConfigurationWidget.DefaultMode,
            ConfigurationWidget.HelpBrowserMode,
            ConfigurationWidget.WebBrowserMode
        )
        
        self.__displayMode = displayMode
        if self.__displayMode == ConfigurationWidget.HelpBrowserMode or \
                not self.__configDlg.isUsingWebEngine():
            try:
                policy = Preferences.getHelp("DownloadManagerRemovePolicy")
                from Helpviewer.Download.DownloadManager import DownloadManager
                if policy == DownloadManager.RemoveNever:
                    self.cleanupNeverButton.setChecked(True)
                elif policy == DownloadManager.RemoveExit:
                    self.cleanupExitButton.setChecked(True)
                else:
                    self.cleanupSuccessfulButton.setChecked(True)
                self.__webKit = True
            except ImportError:
                self.cleanupGroup.hide()
        else:
            policy = Preferences.getWebBrowser("DownloadManagerRemovePolicy")
            from WebBrowser.Download.DownloadManager import DownloadManager
            if policy == DownloadManager.RemoveNever:
                self.cleanupNeverButton.setChecked(True)
            elif policy == DownloadManager.RemoveExit:
                self.cleanupExitButton.setChecked(True)
            else:
                self.cleanupSuccessfulButton.setChecked(True)
            self.__webEngine = True
    
    def save(self):
        """
        Public slot to save the Networj configuration.
        """
        Preferences.setUI(
            "DynamicOnlineCheck",
            self.dynamicOnlineCheckBox.isChecked())
        Preferences.setUI(
            "DownloadPath",
            self.downloadDirPicker.text())
        Preferences.setUI(
            "RequestDownloadFilename",
            self.requestFilenameCheckBox.isChecked())
        if self.__webKit:
            from Helpviewer.Download.DownloadManager import DownloadManager
            if self.cleanupNeverButton.isChecked():
                policy = DownloadManager.RemoveNever
            elif self.cleanupExitButton.isChecked():
                policy = DownloadManager.RemoveExit
            else:
                policy = DownloadManager.RemoveSuccessFullDownload
            Preferences.setHelp("DownloadManagerRemovePolicy", policy)
        elif self.__webEngine:
            from WebBrowser.Download.DownloadManager import DownloadManager
            if self.cleanupNeverButton.isChecked():
                policy = DownloadManager.RemoveNever
            elif self.cleanupExitButton.isChecked():
                policy = DownloadManager.RemoveExit
            else:
                policy = DownloadManager.RemoveSuccessFullDownload
            Preferences.setWebBrowser("DownloadManagerRemovePolicy", policy)
        
        Preferences.setUI(
            "UseProxy",
            not self.noProxyButton.isChecked())
        Preferences.setUI(
            "UseSystemProxy",
            self.systemProxyButton.isChecked())
        Preferences.setUI(
            "UseHttpProxyForAll",
            self.httpProxyForAllCheckBox.isChecked())
        
        Preferences.setUI(
            "ProxyExceptions",
            ",".join(
                [h.strip() for h in self.exceptionsEdit.text().split(",")]))
        
        # HTTP proxy
        Preferences.setUI(
            "ProxyHost/Http",
            self.httpProxyHostEdit.text())
        Preferences.setUI(
            "ProxyPort/Http",
            self.httpProxyPortSpin.value())
        
        # HTTPS proxy
        Preferences.setUI(
            "ProxyHost/Https",
            self.httpsProxyHostEdit.text())
        Preferences.setUI(
            "ProxyPort/Https",
            self.httpsProxyPortSpin.value())
        
        # FTP proxy
        Preferences.setUI(
            "ProxyHost/Ftp",
            self.ftpProxyHostEdit.text())
        Preferences.setUI(
            "ProxyPort/Ftp",
            self.ftpProxyPortSpin.value())
        Preferences.setUI(
            "ProxyType/Ftp",
            self.ftpProxyTypeCombo.itemData(
                self.ftpProxyTypeCombo.currentIndex()))
        Preferences.setUI(
            "ProxyUser/Ftp",
            self.ftpProxyUserEdit.text())
        Preferences.setUI(
            "ProxyPassword/Ftp",
            self.ftpProxyPasswordEdit.text())
        Preferences.setUI(
            "ProxyAccount/Ftp",
            self.ftpProxyAccountEdit.text())
    
    @pyqtSlot()
    def on_clearProxyPasswordsButton_clicked(self):
        """
        Private slot to clear the saved HTTP(S) proxy passwords.
        """
        Preferences.setUI("ProxyPassword/Http", "")
        Preferences.setUI("ProxyPassword/Https", "")
    
    @pyqtSlot(int)
    def on_ftpProxyTypeCombo_currentIndexChanged(self, index):
        """
        Private slot handling the selection of a proxy type.
        
        @param index index of the selected item (integer)
        """
        proxyType = self.ftpProxyTypeCombo.itemData(index)
        self.ftpProxyHostEdit.setEnabled(proxyType != E5FtpProxyType.NoProxy)
        self.ftpProxyPortSpin.setEnabled(proxyType != E5FtpProxyType.NoProxy)
        self.ftpProxyUserEdit.setEnabled(
            proxyType not in [E5FtpProxyType.NoProxy,
                              E5FtpProxyType.NonAuthorizing])
        self.ftpProxyPasswordEdit.setEnabled(
            proxyType not in [E5FtpProxyType.NoProxy,
                              E5FtpProxyType.NonAuthorizing])
        self.ftpProxyAccountEdit.setEnabled(
            proxyType not in [E5FtpProxyType.NoProxy,
                              E5FtpProxyType.NonAuthorizing])
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = NetworkPage(dlg)
    return page
