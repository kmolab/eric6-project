# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Qt configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_QtPage import Ui_QtPage

import Preferences
from Globals import qVersionTuple


class QtPage(ConfigurationPageBase, Ui_QtPage):
    """
    Class implementing the Qt configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(QtPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("QtPage")
        
        self.qt4TransPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.qtToolsDirPicker.setMode(E5PathPickerModes.DirectoryShowFilesMode)
        self.pyqtToolsDirPicker.setMode(
            E5PathPickerModes.DirectoryShowFilesMode)
        
        # set initial values
        if qVersionTuple() < (5, 0, 0):
            self.qt4TransPicker.setText(
                Preferences.getQt("Qt4TranslationsDir"))
        else:
            self.qt4TransPicker.setText(
                Preferences.getQt("Qt5TranslationsDir"))
        self.qtToolsDirPicker.setText(Preferences.getQt("QtToolsDir"))
        self.qt4PrefixEdit.setText(Preferences.getQt("QtToolsPrefix4"))
        self.qt4PostfixEdit.setText(Preferences.getQt("QtToolsPostfix4"))
        self.__updateQt4Sample()
        self.pyqtToolsDirPicker.setText(Preferences.getQt("PyQtToolsDir"))
        self.pyuicIndentSpinBox.setValue(Preferences.getQt("PyuicIndent"))
        self.pyuicImportsCheckBox.setChecked(
            Preferences.getQt("PyuicFromImports"))
        
    def save(self):
        """
        Public slot to save the Qt configuration.
        """
        if qVersionTuple() < (5, 0, 0):
            Preferences.setQt("Qt4TranslationsDir", self.qt4TransPicker.text())
        else:
            Preferences.setQt("Qt5TranslationsDir", self.qt4TransPicker.text())
        Preferences.setQt("QtToolsDir", self.qtToolsDirPicker.text())
        Preferences.setQt("QtToolsPrefix4", self.qt4PrefixEdit.text())
        Preferences.setQt("QtToolsPostfix4", self.qt4PostfixEdit.text())
        Preferences.setQt("PyQtToolsDir", self.pyqtToolsDirPicker.text())
        Preferences.setQt("PyuicIndent", self.pyuicIndentSpinBox.value())
        Preferences.setQt("PyuicFromImports",
                          self.pyuicImportsCheckBox.isChecked())
        
    def __updateQt4Sample(self):
        """
        Private slot to update the Qt4 tools sample label.
        """
        self.qt4SampleLabel.setText(
            self.tr("Sample: {0}designer{1}").format(
                self.qt4PrefixEdit.text(), self.qt4PostfixEdit.text()))
    
    @pyqtSlot(str)
    def on_qt4PrefixEdit_textChanged(self, txt):
        """
        Private slot to handle a change in the entered Qt directory.
        
        @param txt the entered string (string)
        """
        self.__updateQt4Sample()
    
    @pyqtSlot(str)
    def on_qt4PostfixEdit_textChanged(self, txt):
        """
        Private slot to handle a change in the entered Qt directory.
        
        @param txt the entered string (string)
        """
        self.__updateQt4Sample()
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = QtPage()
    return page
