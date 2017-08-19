# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Help Documentation configuration page.
"""

from __future__ import unicode_literals

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_HelpDocumentationPage import Ui_HelpDocumentationPage

import Preferences
import Utilities


class HelpDocumentationPage(ConfigurationPageBase, Ui_HelpDocumentationPage):
    """
    Class implementing the Help Documentation configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(HelpDocumentationPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("HelpDocumentationPage")
        
        self.ericDocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.ericDocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;All Files (*)"))
        self.python2DocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.python2DocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;"
            "Compressed Help Files (*.chm);;"
            "All Files (*)"))
        self.pythonDocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.pythonDocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;"
            "Compressed Help Files (*.chm);;"
            "All Files (*)"))
        self.qt4DocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.qt4DocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;All Files (*)"))
        self.qt5DocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.qt5DocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;All Files (*)"))
        self.pyqt4DocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.pyqt4DocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;All Files (*)"))
        self.pyqt5DocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.pyqt5DocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;All Files (*)"))
        self.pysideDocDirPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.pysideDocDirPicker.setFilters(self.tr(
            "HTML Files (*.html *.htm);;All Files (*)"))
        
        try:
            import PyQt5        # __IGNORE_WARNING__
        except ImportError:
            self.pyqt5Group.setEnabled(False)
        
        pyside2, pyside3 = Utilities.checkPyside()
        if pyside2 or pyside3:
            self.pysideGroup.setEnabled(True)
        else:
            self.pysideGroup.setEnabled(False)
        
        # set initial values
        self.ericDocDirPicker.setText(
            Preferences.getHelp("EricDocDir"), toNative=False)
        self.python2DocDirPicker.setText(
            Preferences.getHelp("Python2DocDir"), toNative=False)
        self.pythonDocDirPicker.setText(
            Preferences.getHelp("PythonDocDir"), toNative=False)
        self.qt4DocDirPicker.setText(
            Preferences.getHelp("Qt4DocDir"), toNative=False)
        self.qt5DocDirPicker.setText(
            Preferences.getHelp("Qt5DocDir"), toNative=False)
        self.pyqt4DocDirPicker.setText(
            Preferences.getHelp("PyQt4DocDir"), toNative=False)
        self.pyqt5DocDirPicker.setText(
            Preferences.getHelp("PyQt5DocDir"), toNative=False)
        self.pysideDocDirPicker.setText(
            Preferences.getHelp("PySideDocDir"), toNative=False)
        
    def save(self):
        """
        Public slot to save the Help Documentation configuration.
        """
        Preferences.setHelp(
            "EricDocDir",
            self.ericDocDirPicker.text(toNative=False))
        Preferences.setHelp(
            "Python2DocDir",
            self.python2DocDirPicker.text(toNative=False))
        Preferences.setHelp(
            "PythonDocDir",
            self.pythonDocDirPicker.text(toNative=False))
        Preferences.setHelp(
            "Qt4DocDir",
            self.qt4DocDirPicker.text(toNative=False))
        Preferences.setHelp(
            "Qt5DocDir",
            self.qt5DocDirPicker.text(toNative=False))
        Preferences.setHelp(
            "PyQt4DocDir",
            self.pyqt4DocDirPicker.text(toNative=False))
        Preferences.setHelp(
            "PyQt5DocDir",
            self.pyqt5DocDirPicker.text(toNative=False))
        Preferences.setHelp(
            "PySideDocDir",
            self.pysideDocDirPicker.text(toNative=False))
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = HelpDocumentationPage()
    return page
