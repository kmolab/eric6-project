# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#


"""
Module implementing the Hex Editor configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFontDialog

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_HexEditorPage import Ui_HexEditorPage

import Preferences

try:
    MonospacedFontsOption = QFontDialog.MonospacedFonts
except AttributeError:
    MonospacedFontsOption = QFontDialog.FontDialogOptions(0x10)


class HexEditorPage(ConfigurationPageBase, Ui_HexEditorPage):
    """
    Class implementing the Hex Editor configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(HexEditorPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("HexEditorPage")
        
        # set initial values
        self.readOnlyCheckBox.setChecked(Preferences.getHexEditor(
            "OpenReadOnly"))
        self.overwriteCheckBox.setChecked(Preferences.getHexEditor(
            "OpenInOverwriteMode"))
        self.addressAreaCheckBox.setChecked(Preferences.getHexEditor(
            "ShowAddressArea"))
        self.addressAreaWidthSpinBox.setValue(Preferences.getHexEditor(
            "AddressAreaWidth"))
        self.asciiAreaCheckBox.setChecked(Preferences.getHexEditor(
            "ShowAsciiArea"))
        self.highlightingCheckBox.setChecked(Preferences.getHexEditor(
            "HighlightChanges"))
        self.recentFilesSpinBox.setValue(Preferences.getHexEditor(
            "RecentNumber"))
        
        # font
        self.monospacedFont = Preferences.getHexEditor("Font")
        self.monospacedFontSample.setFont(self.monospacedFont)

        # colours
        self.initColour("HighlightingBackGround",
                        self.highlightingBackGroundButton,
                        Preferences.getHexEditor)
        self.initColour("HighlightingForeGround",
                        self.highlightingForeGroundButton,
                        Preferences.getHexEditor)
        self.initColour("SelectionBackGround",
                        self.selectionBackGroundButton,
                        Preferences.getHexEditor)
        self.initColour("SelectionForeGround",
                        self.selectionForeGroundButton,
                        Preferences.getHexEditor)
        self.initColour("AddressAreaBackGround",
                        self.addressAreaBackGroundButton,
                        Preferences.getHexEditor)
        self.initColour("AddressAreaForeGround",
                        self.addressAreaForeGroundButton,
                        Preferences.getHexEditor)
    
    def save(self):
        """
        Public slot to save the IRC configuration.
        """
        Preferences.setHexEditor(
            "OpenReadOnly", self.readOnlyCheckBox.isChecked())
        Preferences.setHexEditor(
            "OpenInOverwriteMode", self.overwriteCheckBox.isChecked())
        Preferences.setHexEditor(
            "ShowAddressArea", self.addressAreaCheckBox.isChecked())
        Preferences.setHexEditor(
            "AddressAreaWidth", self.addressAreaWidthSpinBox.value())
        Preferences.setHexEditor(
            "ShowAsciiArea", self.asciiAreaCheckBox.isChecked())
        Preferences.setHexEditor(
            "HighlightChanges", self.highlightingCheckBox.isChecked())
        Preferences.setHexEditor(
            "Font", self.monospacedFont)
        Preferences.setHexEditor(
            "RecentNumber", self.recentFilesSpinBox.value())
        
        # colours
        self.saveColours(Preferences.setHexEditor)
    
    @pyqtSlot()
    def on_monospacedFontButton_clicked(self):
        """
        Private method used to select the font to be used.
        """
        self.monospacedFont = self.selectFont(
            self.monospacedFontSample, self.monospacedFont,
            options=MonospacedFontsOption)
    
    def polishPage(self):
        """
        Public slot to perform some polishing actions.
        """
        self.monospacedFontSample.setFont(self.monospacedFont)


def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = HexEditorPage()
    return page
