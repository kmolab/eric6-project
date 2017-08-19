# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Interface configuration page (variant for web browser).
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QStyleFactory

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_HelpInterfacePage import Ui_HelpInterfacePage

import Preferences


class HelpInterfacePage(ConfigurationPageBase, Ui_HelpInterfacePage):
    """
    Class implementing the Interface configuration page (variant for web
    browser).
    """
    def __init__(self):
        """
        Constructor
        """
        super(HelpInterfacePage, self).__init__()
        self.setupUi(self)
        self.setObjectName("InterfacePage")
        
        self.styleSheetPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.styleSheetPicker.setFilters(self.tr(
            "Qt Style Sheets (*.qss);;Cascading Style Sheets (*.css);;"
            "All files (*)"))
        
        # set initial values
        self.__populateStyleCombo()
        self.styleSheetPicker.setText(Preferences.getUI("StyleSheet"))
    
    def save(self):
        """
        Public slot to save the Interface configuration.
        """
        # save the style settings
        styleIndex = self.styleComboBox.currentIndex()
        style = self.styleComboBox.itemData(styleIndex)
        Preferences.setUI("Style", style)
        Preferences.setUI(
            "StyleSheet",
            self.styleSheetPicker.text())
    
    def __populateStyleCombo(self):
        """
        Private method to populate the style combo box.
        """
        curStyle = Preferences.getUI("Style")
        styles = sorted(list(QStyleFactory.keys()))
        self.styleComboBox.addItem(self.tr('System'), "System")
        for style in styles:
            self.styleComboBox.addItem(style, style)
        currentIndex = self.styleComboBox.findData(curStyle)
        if currentIndex == -1:
            currentIndex = 0
        self.styleComboBox.setCurrentIndex(currentIndex)
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = HelpInterfacePage()
    return page
