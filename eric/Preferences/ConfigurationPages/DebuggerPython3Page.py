# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Debugger Python3 configuration page.
"""

from __future__ import unicode_literals

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_DebuggerPython3Page import Ui_DebuggerPython3Page

import Preferences


class DebuggerPython3Page(ConfigurationPageBase, Ui_DebuggerPython3Page):
    """
    Class implementing the Debugger Python3 configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(DebuggerPython3Page, self).__init__()
        self.setupUi(self)
        self.setObjectName("DebuggerPython3Page")
        
        self.interpreterPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.interpreterPicker.setToolTip(self.tr(
            "Press to select the Python3 interpreter via a file selection"
            " dialog"))
        
        self.debugClientPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.debugClientPicker.setToolTip(self.tr(
            "Press to select the Debug Client via a file selection dialog"))
        self.debugClientPicker.setFilters(self.tr("Python Files (*.py *.py3)"))
        
        # set initial values
        self.interpreterPicker.setText(
            Preferences.getDebugger("Python3Interpreter"), toNative=False)
        dct = Preferences.getDebugger("DebugClientType3")
        if dct == "standard":
            self.standardButton.setChecked(True)
        else:
            self.customButton.setChecked(True)
        self.debugClientPicker.setText(
            Preferences.getDebugger("DebugClient3"), toNative=False)
        self.pyRedirectCheckBox.setChecked(
            Preferences.getDebugger("Python3Redirect"))
        self.pyNoEncodingCheckBox.setChecked(
            Preferences.getDebugger("Python3NoEncoding"))
        self.sourceExtensionsEdit.setText(
            Preferences.getDebugger("Python3Extensions"))
        
    def save(self):
        """
        Public slot to save the Debugger Python configuration.
        """
        Preferences.setDebugger(
            "Python3Interpreter",
            self.interpreterPicker.text(toNative=False))
        if self.standardButton.isChecked():
            dct = "standard"
        else:
            dct = "custom"
        Preferences.setDebugger("DebugClientType3", dct)
        Preferences.setDebugger(
            "DebugClient3",
            self.debugClientPicker.text(toNative=False))
        Preferences.setDebugger(
            "Python3Redirect",
            self.pyRedirectCheckBox.isChecked())
        Preferences.setDebugger(
            "Python3NoEncoding",
            self.pyNoEncodingCheckBox.isChecked())
        Preferences.setDebugger(
            "Python3Extensions",
            self.sourceExtensionsEdit.text())
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = DebuggerPython3Page()
    return page
