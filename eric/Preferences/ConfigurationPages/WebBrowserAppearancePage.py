# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Web Browser Appearance configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFontDialog

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_WebBrowserAppearancePage import Ui_WebBrowserAppearancePage

import Preferences

try:
    MonospacedFontsOption = QFontDialog.MonospacedFonts
except AttributeError:
    MonospacedFontsOption = QFontDialog.FontDialogOptions(0x10)


class WebBrowserAppearancePage(ConfigurationPageBase,
                               Ui_WebBrowserAppearancePage):
    """
    Class implementing the Web Browser Appearance page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(WebBrowserAppearancePage, self).__init__()
        self.setupUi(self)
        self.setObjectName("WebBrowserAppearancePage")
        
        self.styleSheetPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.styleSheetPicker.setFilters(self.tr(
            "Cascading Style Sheets (*.css);;All files (*)"))
        
        self.__displayMode = None
        
        # set initial values
        defaultFontSize = Preferences.getWebBrowser("DefaultFontSize")
        fixedFontSize = Preferences.getWebBrowser("DefaultFixedFontSize")
        self.defaultSizeSpinBox.setValue(defaultFontSize)
        self.fixedSizeSpinBox.setValue(fixedFontSize)
        self.minSizeSpinBox.setValue(
            Preferences.getWebBrowser("MinimumFontSize"))
        self.minLogicalSizeSpinBox.setValue(
            Preferences.getWebBrowser("MinimumLogicalFontSize"))
        
        self.standardFontCombo.setCurrentFont(
            QFont(Preferences.getWebBrowser("StandardFontFamily"),
                  defaultFontSize, QFont.Normal, False))
        self.fixedFontCombo.setCurrentFont(
            QFont(Preferences.getWebBrowser("FixedFontFamily"),
                  fixedFontSize, QFont.Normal, False))
        self.serifFontCombo.setCurrentFont(
            QFont(Preferences.getWebBrowser("SerifFontFamily"),
                  defaultFontSize, QFont.Normal, False))
        self.sansSerifFontCombo.setCurrentFont(
            QFont(Preferences.getWebBrowser("SansSerifFontFamily"),
                  defaultFontSize, QFont.Normal, False))
        self.cursiveFontCombo.setCurrentFont(
            QFont(Preferences.getWebBrowser("CursiveFontFamily"),
                  defaultFontSize, QFont.Normal, True))
        self.fantasyFontCombo.setCurrentFont(
            QFont(Preferences.getWebBrowser("FantasyFontFamily"),
                  defaultFontSize, QFont.Normal, False))
        try:
            # Qt 5.7+
            self.pictographFontCombo.setCurrentFont(
                QFont(Preferences.getWebBrowser("PictographFontFamily"),
                      defaultFontSize, QFont.Normal, False))
        except KeyError:
            self.pictographFontLabel.setEnabled(False)
            self.pictographFontCombo.setEnabled(False)
        
        self.initColour("SaveUrlColor", self.secureURLsColourButton,
                        Preferences.getWebBrowser)
        
        self.autoLoadImagesCheckBox.setChecked(
            Preferences.getWebBrowser("AutoLoadImages"))
        
        self.styleSheetPicker.setText(
            Preferences.getWebBrowser("UserStyleSheet"))
        
        self.tabsCloseButtonCheckBox.setChecked(
            Preferences.getUI("SingleCloseButton"))
        self.warnOnMultipleCloseCheckBox.setChecked(
            Preferences.getWebBrowser("WarnOnMultipleClose"))
        
        self.toolbarsCheckBox.setChecked(
            Preferences.getWebBrowser("ShowToolbars"))
    
    def setMode(self, displayMode):
        """
        Public method to perform mode dependent setups.
        
        @param displayMode mode of the configuration dialog
            (ConfigurationWidget.DefaultMode,
             ConfigurationWidget.HelpBrowserMode,
             ConfigurationWidget.TrayStarterMode)
        """
        from ..ConfigurationDialog import ConfigurationWidget
        assert displayMode in (
            ConfigurationWidget.DefaultMode,
            ConfigurationWidget.WebBrowserMode,
        )
        
        self.__displayMode = displayMode
        if self.__displayMode != ConfigurationWidget.WebBrowserMode:
            self.tabsGroupBox.hide()
    
    def save(self):
        """
        Public slot to save the Help Viewers configuration.
        """
        Preferences.setWebBrowser(
            "StandardFontFamily",
            self.standardFontCombo.currentFont().family())
        Preferences.setWebBrowser(
            "FixedFontFamily",
            self.fixedFontCombo.currentFont().family())
        Preferences.setWebBrowser(
            "SerifFontFamily",
            self.serifFontCombo.currentFont().family())
        Preferences.setWebBrowser(
            "SansSerifFontFamily",
            self.sansSerifFontCombo.currentFont().family())
        Preferences.setWebBrowser(
            "CursiveFontFamily",
            self.cursiveFontCombo.currentFont().family())
        Preferences.setWebBrowser(
            "FantasyFontFamily",
            self.fantasyFontCombo.currentFont().family())
        if self.pictographFontCombo.isEnabled():
            Preferences.setWebBrowser(
                "PictographFontFamily",
                self.pictographFontCombo.currentFont().family())
        
        Preferences.setWebBrowser(
            "DefaultFontSize",
            self.defaultSizeSpinBox.value())
        Preferences.setWebBrowser(
            "DefaultFixedFontSize",
            self.fixedSizeSpinBox.value())
        Preferences.setWebBrowser(
            "MinimumFontSize",
            self.minSizeSpinBox.value())
        Preferences.setWebBrowser(
            "MinimumLogicalFontSize",
            self.minLogicalSizeSpinBox.value())
        
        Preferences.setWebBrowser(
            "AutoLoadImages",
            self.autoLoadImagesCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "UserStyleSheet",
            self.styleSheetPicker.text())
        
        self.saveColours(Preferences.setWebBrowser)
        
        from ..ConfigurationDialog import ConfigurationWidget
        if self.__displayMode == ConfigurationWidget.WebBrowserMode:
            Preferences.setUI(
                "SingleCloseButton",
                self.tabsCloseButtonCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "WarnOnMultipleClose",
            self.warnOnMultipleCloseCheckBox.isChecked())
        
        Preferences.setWebBrowser(
            "ShowToolbars",
            self.toolbarsCheckBox.isChecked())
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = WebBrowserAppearancePage()
    return page
