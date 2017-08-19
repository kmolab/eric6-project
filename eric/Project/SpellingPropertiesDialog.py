# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Spelling Properties dialog.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QDialog

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_SpellingPropertiesDialog import Ui_SpellingPropertiesDialog

import Preferences


class SpellingPropertiesDialog(QDialog, Ui_SpellingPropertiesDialog):
    """
    Class implementing the Spelling Properties dialog.
    """
    def __init__(self, project, new, parent):
        """
        Constructor
        
        @param project reference to the project object
        @param new flag indicating the generation of a new project
        @param parent parent widget of this dialog (QWidget)
        """
        super(SpellingPropertiesDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.pwlPicker.setMode(E5PathPickerModes.SaveFileMode)
        self.pwlPicker.setDefaultDirectory(project.ppath)
        self.pwlPicker.setFilters(self.tr(
            "Dictionary File (*.dic);;All Files (*)"))
        
        self.pelPicker.setMode(E5PathPickerModes.SaveFileMode)
        self.pelPicker.setDefaultDirectory(project.ppath)
        self.pelPicker.setFilters(self.tr(
            "Dictionary File (*.dic);;All Files (*)"))
        
        self.project = project
        self.parent = parent
        
        from QScintilla.SpellChecker import SpellChecker
        self.spellingComboBox.addItem(self.tr("<default>"))
        self.spellingComboBox.addItems(
            sorted(SpellChecker.getAvailableLanguages()))
        
        if not new:
            self.initDialog()
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    def initDialog(self):
        """
        Public method to initialize the dialogs data.
        """
        index = self.spellingComboBox.findText(
            self.project.pdata["SPELLLANGUAGE"])
        if index == -1:
            index = 0
        self.spellingComboBox.setCurrentIndex(index)
        if self.project.pdata["SPELLWORDS"]:
            self.pwlPicker.setText(self.project.pdata["SPELLWORDS"])
        if self.project.pdata["SPELLEXCLUDES"]:
            self.pelPicker.setText(self.project.pdata["SPELLEXCLUDES"])
    
    def storeData(self):
        """
        Public method to store the entered/modified data.
        """
        if self.spellingComboBox.currentIndex() == 0:
            self.project.pdata["SPELLLANGUAGE"] = \
                Preferences.getEditor("SpellCheckingDefaultLanguage")
        else:
            self.project.pdata["SPELLLANGUAGE"] = \
                self.spellingComboBox.currentText()
        self.project.pdata["SPELLWORDS"] = \
            self.project.getRelativePath(self.pwlPicker.text())
        self.project.pdata["SPELLEXCLUDES"] = \
            self.project.getRelativePath(self.pelPicker.text())
