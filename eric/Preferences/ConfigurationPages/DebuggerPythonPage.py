# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Debugger Python configuration page.
"""

from __future__ import unicode_literals

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_DebuggerPythonPage import Ui_DebuggerPythonPage

import Preferences


class DebuggerPythonPage(ConfigurationPageBase, Ui_DebuggerPythonPage):
    """
    Class implementing the Debugger Python configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(DebuggerPythonPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("DebuggerPythonPage")
        
        self.interpreterPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.interpreterPicker.setToolTip(self.tr(
            "Press to select the Python interpreter via a file selection"
            " dialog"))
        
        self.debugClientPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.debugClientPicker.setToolTip(self.tr(
            "Press to select the Debug Client via a file selection dialog"))
        self.debugClientPicker.setFilters(self.tr("Python Files (*.py *.py2)"))
        
        # set initial values
        self.interpreterPicker.setText(
            Preferences.getDebugger("PythonInterpreter"), toNative=False)
        dct = Preferences.getDebugger("DebugClientType")
        if dct == "standard":
            self.standardButton.setChecked(True)
        else:
            self.customButton.setChecked(True)
        self.debugClientPicker.setText(
            Preferences.getDebugger("DebugClient"), toNative=False)
        self.pyRedirectCheckBox.setChecked(
            Preferences.getDebugger("PythonRedirect"))
        self.pyNoEncodingCheckBox.setChecked(
            Preferences.getDebugger("PythonNoEncoding"))
        self.sourceExtensionsEdit.setText(
            Preferences.getDebugger("PythonExtensions"))
        
    def save(self):
        """
        Public slot to save the Debugger Python configuration.
        """
        Preferences.setDebugger(
            "PythonInterpreter",
            self.interpreterPicker.text(toNative=False))
        if self.standardButton.isChecked():
            dct = "standard"
        else:
            dct = "custom"
        Preferences.setDebugger("DebugClientType", dct)
        Preferences.setDebugger(
            "DebugClient",
            self.debugClientPicker.text(toNative=False))
        Preferences.setDebugger(
            "PythonRedirect",
            self.pyRedirectCheckBox.isChecked())
        Preferences.setDebugger(
            "PythonNoEncoding",
            self.pyNoEncodingCheckBox.isChecked())
        Preferences.setDebugger(
            "PythonExtensions",
            self.sourceExtensionsEdit.text())
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = DebuggerPythonPage()
    return page
