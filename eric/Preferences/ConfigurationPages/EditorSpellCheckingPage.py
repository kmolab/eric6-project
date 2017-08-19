# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Editor Spellchecking configuration page.
"""

from __future__ import unicode_literals

from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_EditorSpellCheckingPage import Ui_EditorSpellCheckingPage

import Preferences


class EditorSpellCheckingPage(ConfigurationPageBase,
                              Ui_EditorSpellCheckingPage):
    """
    Class implementing the Editor Spellchecking configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(EditorSpellCheckingPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("EditorSpellCheckingPage")
        
        self.pwlPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.pwlPicker.setFilters(self.tr(
            "Dictionary File (*.dic);;All Files (*)"))
        
        self.pelPicker.setMode(E5PathPickerModes.OpenFileMode)
        self.pelPicker.setFilters(self.tr(
            "Dictionary File (*.dic);;All Files (*)"))
        
        from QScintilla.SpellChecker import SpellChecker
        languages = sorted(SpellChecker.getAvailableLanguages())
        self.defaultLanguageCombo.addItems(languages)
        if languages:
            self.errorLabel.hide()
        else:
            self.spellingFrame.setEnabled(False)
        
        # set initial values
        self.checkingEnabledCheckBox.setChecked(
            Preferences.getEditor("SpellCheckingEnabled"))
        
        self.defaultLanguageCombo.setCurrentIndex(
            self.defaultLanguageCombo.findText(
                Preferences.getEditor("SpellCheckingDefaultLanguage")))
        
        self.stringsOnlyCheckBox.setChecked(
            Preferences.getEditor("SpellCheckStringsOnly"))
        self.minimumWordSizeSlider.setValue(
            Preferences.getEditor("SpellCheckingMinWordSize"))
        
        self.initColour(
            "SpellingMarkers", self.spellingMarkerButton,
            Preferences.getEditorColour, hasAlpha=True)
        
        self.pwlPicker.setText(
            Preferences.getEditor("SpellCheckingPersonalWordList"))
        self.pelPicker.setText(
            Preferences.getEditor("SpellCheckingPersonalExcludeList"))
        
        if self.spellingFrame.isEnabled():
            self.enabledCheckBox.setChecked(
                Preferences.getEditor("AutoSpellCheckingEnabled"))
        else:
            self.enabledCheckBox.setChecked(False)  # not available
        self.chunkSizeSpinBox.setValue(
            Preferences.getEditor("AutoSpellCheckChunkSize"))
        
    def save(self):
        """
        Public slot to save the Editor Search configuration.
        """
        Preferences.setEditor(
            "SpellCheckingEnabled", self.checkingEnabledCheckBox.isChecked())
        
        Preferences.setEditor(
            "SpellCheckingDefaultLanguage",
            self.defaultLanguageCombo.currentText())
        
        Preferences.setEditor(
            "SpellCheckStringsOnly", self.stringsOnlyCheckBox.isChecked())
        Preferences.setEditor(
            "SpellCheckingMinWordSize", self.minimumWordSizeSlider.value())
        
        self.saveColours(Preferences.setEditorColour)
        
        Preferences.setEditor(
            "SpellCheckingPersonalWordList", self.pwlPicker.text())
        Preferences.setEditor(
            "SpellCheckingPersonalExcludeList", self.pelPicker.text())
        
        Preferences.setEditor(
            "AutoSpellCheckingEnabled", self.enabledCheckBox.isChecked())
        Preferences.setEditor(
            "AutoSpellCheckChunkSize", self.chunkSizeSpinBox.value())


def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = EditorSpellCheckingPage()
    return page
