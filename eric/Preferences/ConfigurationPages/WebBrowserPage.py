# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the  Web Browser configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, QLocale

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_WebBrowserPage import Ui_WebBrowserPage

import UI.PixmapCache
import Preferences


class WebBrowserPage(ConfigurationPageBase, Ui_WebBrowserPage):
    """
    Class documentation goes here.
    """
    def __init__(self, configDialog):
        """
        Constructor
        
        @param configDialog reference to the configuration dialog
            (ConfigurationDialog)
        """
        super(WebBrowserPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("WebBrowserPage")
        
        self.__configDlg = configDialog
        mw = configDialog.parent().parent()
        if hasattr(mw, "helpWindow") and mw.helpWindow is not None:
            # IDE
            self.__browserWindow = mw.helpWindow
        elif hasattr(mw, "currentBrowser"):
            # Web Browser
            self.__browserWindow = mw
        else:
            self.__browserWindow = None
        self.setCurrentPageButton.setEnabled(self.__browserWindow is not None)
        self.imageSearchGroup.setEnabled(self.__browserWindow is not None)
        
        defaultSchemes = ["file://", "http://", "https://"]
        self.defaultSchemeCombo.addItems(defaultSchemes)
        
        # set initial values
        self.singleHelpWindowCheckBox.setChecked(
            Preferences.getWebBrowser("SingleWebBrowserWindow"))
        self.saveGeometryCheckBox.setChecked(
            Preferences.getWebBrowser("SaveGeometry"))
        self.webSuggestionsCheckBox.setChecked(
            Preferences.getWebBrowser("WebSearchSuggestions"))
        self.showTabPreviews.setChecked(
            Preferences.getWebBrowser("ShowPreview"))
        self.errorPageCheckBox.setChecked(
            Preferences.getWebBrowser("ErrorPageEnabled"))
        self.scrollingCheckBox.setChecked(
            Preferences.getWebBrowser("ScrollAnimatorEnabled"))
        self.fullscreenCheckBox.setChecked(
            Preferences.getWebBrowser("FullScreenSupportEnabled"))
        try:
            # Qt 5.7+
            self.screenCaptureCheckBox.setChecked(
                Preferences.getWebBrowser("ScreenCaptureEnabled"))
            self.webGLCheckBox.setChecked(
                Preferences.getWebBrowser("WebGLEnabled"))
        except KeyError:
            self.screenCaptureCheckBox.setEnabled(False)
            self.webGLCheckBox.setEnabled(False)
        
        self.jsOpenWindowsCheckBox.setChecked(
            Preferences.getWebBrowser("JavaScriptCanOpenWindows"))
        self.jsClipboardCheckBox.setChecked(
            Preferences.getWebBrowser("JavaScriptCanAccessClipboard"))
        self.pluginsCheckBox.setChecked(
            Preferences.getWebBrowser("PluginsEnabled"))
        self.doNotTrackCheckBox.setChecked(
            Preferences.getWebBrowser("DoNotTrack"))
        self.sendRefererCheckBox.setChecked(
            Preferences.getWebBrowser("SendReferer"))
        
        self.diskCacheCheckBox.setChecked(
            Preferences.getWebBrowser("DiskCacheEnabled"))
        self.cacheSizeSpinBox.setValue(
            Preferences.getWebBrowser("DiskCacheSize"))
        
        self.startupCombo.setCurrentIndex(
            Preferences.getWebBrowser("StartupBehavior"))
        self.newTabCombo.setCurrentIndex(
            Preferences.getWebBrowser("NewTabBehavior"))
        self.homePageEdit.setText(
            Preferences.getWebBrowser("HomePage"))
        self.loadTabOnActivationCheckBox.setChecked(
            Preferences.getWebBrowser("LoadTabOnActivation"))
        
        self.saveSessionCheckBox.setChecked(
            Preferences.getWebBrowser("SessionAutoSave"))
        self.sessionTimerSpinBox.setValue(
            Preferences.getWebBrowser("SessionAutoSaveInterval"))
        
        self.defaultSchemeCombo.setCurrentIndex(
            self.defaultSchemeCombo.findText(
                Preferences.getWebBrowser("DefaultScheme")))
        
        historyLimit = Preferences.getWebBrowser("HistoryLimit")
        idx = 0
        if historyLimit == 1:
            idx = 0
        elif historyLimit == 7:
            idx = 1
        elif historyLimit == 14:
            idx = 2
        elif historyLimit == 30:
            idx = 3
        elif historyLimit == 365:
            idx = 4
        elif historyLimit == -1:
            idx = 5
        elif historyLimit == -2:
            idx = 6
        else:
            idx = 5
        self.expireHistory.setCurrentIndex(idx)
        
        for language in range(2, QLocale.LastLanguage + 1):
            countries = [l.country() for l in QLocale.matchingLocales(
                language, QLocale.AnyScript, QLocale.AnyCountry)]
            if len(countries) > 0:
                self.languageCombo.addItem(
                    QLocale.languageToString(language), language)
        self.languageCombo.model().sort(0)
        self.languageCombo.insertSeparator(0)
        self.languageCombo.insertItem(0, QLocale.languageToString(0), 0)
        index = self.languageCombo.findData(
            Preferences.getWebBrowser("SearchLanguage"))
        if index > -1:
            self.languageCombo.setCurrentIndex(index)
        
        if self.__browserWindow:
            for engineName in self.__browserWindow.imageSearchEngine()\
                    .searchEngineNames():
                self.imageSearchComboBox.addItem(
                    UI.PixmapCache.getIcon(
                        "{0}.png".format(engineName.lower())),
                    engineName)
            index = self.imageSearchComboBox.findText(
                Preferences.getWebBrowser("ImageSearchEngine"))
            if index > -1:
                self.imageSearchComboBox.setCurrentIndex(index)
        
        self.spatialCheckBox.setChecked(
            Preferences.getWebBrowser("SpatialNavigationEnabled"))
        self.linksInFocusChainCheckBox.setChecked(
            Preferences.getWebBrowser("LinksIncludedInFocusChain"))
        try:
            # Qt 5.8
            self.focusOnNavigationCheckBox.setChecked(
                Preferences.getWebBrowser("FocusOnNavigationEnabled"))
        except KeyError:
            self.focusOnNavigationCheckBox.setEnabled(False)
        
        self.xssAuditingCheckBox.setChecked(
            Preferences.getWebBrowser("XSSAuditingEnabled"))
        try:
            # Qt 5.8
            self.insecureContentsCheckBox.setChecked(
                Preferences.getWebBrowser("AllowRunningInsecureContent"))
        except KeyError:
            self.insecureContentsCheckBox.setEnabled(False)
        
        try:
            # Qt 5.8
            self.printBackgroundCheckBox.setChecked(
                Preferences.getWebBrowser("PrintElementBackgrounds"))
        except KeyError:
            self.printBackgroundCheckBox.setEnabled(False)
        
        self.autoScrollGroupBox.setChecked(
            Preferences.getWebBrowser("AutoScrollEnabled"))
        self.autoScrollDividerSpinBox.setValue(
            Preferences.getWebBrowser("AutoScrollDivider"))
        
        self.webInspectorGroup.setChecked(
            Preferences.getWebBrowser("WebInspectorEnabled"))
        self.webInspectorPortSpinBox.setValue(
            Preferences.getWebBrowser("WebInspectorPort"))
    
    def save(self):
        """
        Public slot to save the Help Viewers configuration.
        """
        Preferences.setWebBrowser(
            "SingleWebBrowserWindow",
            self.singleHelpWindowCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SaveGeometry",
            self.saveGeometryCheckBox.isChecked())
        Preferences.setWebBrowser(
            "WebSearchSuggestions",
            self.webSuggestionsCheckBox.isChecked())
        Preferences.setWebBrowser(
            "ShowPreview",
            self.showTabPreviews.isChecked())
        Preferences.setWebBrowser(
            "ErrorPageEnabled",
            self.errorPageCheckBox.isChecked())
        Preferences.setWebBrowser(
            "ScrollAnimatorEnabled",
            self.scrollingCheckBox.isChecked())
        Preferences.setWebBrowser(
            "FullScreenSupportEnabled",
            self.fullscreenCheckBox.isChecked())
        
        if self.screenCaptureCheckBox.isEnabled():
            Preferences.setWebBrowser(
                "ScreenCaptureEnabled",
                self.screenCaptureCheckBox.isChecked())
            Preferences.setWebBrowser(
                "WebGLEnabled",
                self.webGLCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "JavaScriptCanOpenWindows",
            self.jsOpenWindowsCheckBox.isChecked())
        Preferences.setWebBrowser(
            "JavaScriptCanAccessClipboard",
            self.jsClipboardCheckBox.isChecked())
        Preferences.setWebBrowser(
            "PluginsEnabled",
            self.pluginsCheckBox.isChecked())
        Preferences.setWebBrowser(
            "DoNotTrack",
            self.doNotTrackCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SendReferer",
            self.sendRefererCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "DiskCacheEnabled",
            self.diskCacheCheckBox.isChecked())
        Preferences.setWebBrowser(
            "DiskCacheSize",
            self.cacheSizeSpinBox.value())
        
        Preferences.setWebBrowser(
            "StartupBehavior",
            self.startupCombo.currentIndex())
        Preferences.setWebBrowser(
            "NewTabBehavior",
            self.newTabCombo.currentIndex())
        Preferences.setWebBrowser(
            "HomePage",
            self.homePageEdit.text())
        Preferences.setWebBrowser(
            "LoadTabOnActivation",
            self.loadTabOnActivationCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "SessionAutoSave",
            self.saveSessionCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SessionAutoSaveInterval",
            self.sessionTimerSpinBox.value())
        
        Preferences.setWebBrowser(
            "DefaultScheme",
            self.defaultSchemeCombo.currentText())
        
        idx = self.expireHistory.currentIndex()
        if idx == 0:
            historyLimit = 1
        elif idx == 1:
            historyLimit = 7
        elif idx == 2:
            historyLimit = 14
        elif idx == 3:
            historyLimit = 30
        elif idx == 4:
            historyLimit = 365
        elif idx == 5:
            historyLimit = -1
        elif idx == 6:
            historyLimit = -2
        Preferences.setWebBrowser("HistoryLimit", historyLimit)
        
        languageIndex = self.languageCombo.currentIndex()
        if languageIndex > -1:
            language = self.languageCombo.itemData(languageIndex)
        else:
            # fall back to system default
            language = QLocale.system().language()
        Preferences.setWebBrowser("SearchLanguage", language)
        
        Preferences.setWebBrowser(
            "ImageSearchEngine",
            self.imageSearchComboBox.currentText())
        
        Preferences.setWebBrowser(
            "SpatialNavigationEnabled",
            self.spatialCheckBox.isChecked())
        Preferences.setWebBrowser(
            "LinksIncludedInFocusChain",
            self.linksInFocusChainCheckBox.isChecked())
        if self.focusOnNavigationCheckBox.isEnabled():
            Preferences.setWebBrowser(
                "FocusOnNavigationEnabled",
                self.focusOnNavigationCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "XSSAuditingEnabled",
            self.xssAuditingCheckBox.isChecked())
        if self.insecureContentsCheckBox.isEnabled():
            Preferences.setWebBrowser(
                "AllowRunningInsecureContent",
                self.insecureContentsCheckBox.isChecked())
        
        if self.printBackgroundCheckBox.isEnabled():
            Preferences.setWebBrowser(
                "PrintElementBackgrounds",
                self.printBackgroundCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "AutoScrollEnabled",
            self.autoScrollGroupBox.isChecked())
        Preferences.setWebBrowser(
            "AutoScrollDivider",
            self.autoScrollDividerSpinBox.value())
        
        Preferences.setWebBrowser(
            "WebInspectorEnabled",
            self.webInspectorGroup.isChecked())
        Preferences.setWebBrowser(
            "WebInspectorPort",
            self.webInspectorPortSpinBox.value())
    
    @pyqtSlot()
    def on_setCurrentPageButton_clicked(self):
        """
        Private slot to set the current page as the home page.
        """
        url = self.__browserWindow.currentBrowser().url()
        self.homePageEdit.setText(bytes(url.toEncoded()).decode())
    
    @pyqtSlot()
    def on_defaultHomeButton_clicked(self):
        """
        Private slot to set the default home page.
        """
        self.homePageEdit.setText(Preferences.Prefs.helpDefaults["HomePage"])
    
    @pyqtSlot(int)
    def on_startupCombo_currentIndexChanged(self, index):
        """
        Private slot to enable elements depending on the selected startup
        entry.
        
        @param index index of the selected entry (integer)
        """
        # set state of the home page related items
        enable = index == 1
        self.homePageLabel.setEnabled(enable)
        self.homePageEdit.setEnabled(enable)
        self.defaultHomeButton.setEnabled(enable)
        self.setCurrentPageButton.setEnabled(enable)
        
        # set state of the session related items
        self.loadTabOnActivationCheckBox.setEnabled(
            index in [3, 4])
    
    @pyqtSlot()
    def on_refererWhitelistButton_clicked(self):
        """
        Private slot to edit the referer whitelist.
        """
        from WebBrowser.Network.SendRefererWhitelistDialog import \
            SendRefererWhitelistDialog
        SendRefererWhitelistDialog(self).exec_()


def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = WebBrowserPage(dlg)
    return page
