# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Web Browser Spell Checking configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, Qt, QCoreApplication, QDir, QLibraryInfo, \
    QLocale
from PyQt5.QtWidgets import QListWidgetItem

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_WebBrowserSpellCheckingPage import Ui_WebBrowserSpellCheckingPage

import Preferences
import Globals


class WebBrowserSpellCheckingPage(ConfigurationPageBase,
                                  Ui_WebBrowserSpellCheckingPage):
    """
    Class implementing the Web Browser Spell Checking page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(WebBrowserSpellCheckingPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("WebBrowserSpellCheckingPage")
        
        # set initial values
        self.spellCheckEnabledCheckBox.setChecked(
            Preferences.getWebBrowser("SpellCheckEnabled"))
        self.on_spellCheckEnabledCheckBox_clicked()
        
        if Globals.isMacPlatform():
            dictionaryDirectories = {
                QDir.cleanPath(
                    QCoreApplication.applicationDirPath() +
                    "/../Resources/qtwebengine_dictionaries"),
                QDir.cleanPath(
                    QCoreApplication.applicationDirPath() +
                    "/../Frameworks/QtWebEngineCore.framework"
                    "/Resources/qtwebengine_dictionaries"),
            }
        else:
            dictionaryDirectories = {
                QDir.cleanPath(
                    QCoreApplication.applicationDirPath() +
                    "/qtwebengine_dictionaries"),
                QDir.cleanPath(
                    QLibraryInfo.location(QLibraryInfo.DataPath) +
                    "/qtwebengine_dictionaries"),
            }
        self.spellCheckDictionaryDirectoriesEdit.setPlainText(
            "\n".join(dictionaryDirectories))
        
        for path in dictionaryDirectories:
            directory = QDir(path)
            fileNames = directory.entryList(["*.bdic"])
            for fileName in fileNames:
                lang = fileName[:-5]
                langStr = self.__createLanguageString(lang)
                if self.spellCheckLanguagesList.findItems(langStr,
                                                          Qt.MatchExactly):
                    continue
                
                itm = QListWidgetItem(langStr, self.spellCheckLanguagesList)
                itm.setData(Qt.UserRole, lang)
                itm.setFlags(itm.flags() | Qt.ItemIsUserCheckable)
                itm.setCheckState(Qt.Unchecked)
        self.spellCheckLanguagesList.sortItems(Qt.AscendingOrder)
        
        spellCheckLanguages = Preferences.getWebBrowser("SpellCheckLanguages")
        topIndex = 0
        for lang in spellCheckLanguages:
            items = self.spellCheckLanguagesList.findItems(
                self.__createLanguageString(lang), Qt.MatchExactly)
            if items:
                itm = items[0]
                self.spellCheckLanguagesList.takeItem(
                    self.spellCheckLanguagesList.row(itm))
                self.spellCheckLanguagesList.insertItem(topIndex, itm)
                itm.setCheckState(Qt.Checked)
                topIndex += 1
        
        if self.spellCheckLanguagesList.count():
            self.noLanguagesLabel.hide()
        else:
            self.spellCheckLanguagesList.hide()
    
    def save(self):
        """
        Public slot to save the Help Viewers configuration.
        """
        languages = []
        for row in range(self.spellCheckLanguagesList.count()):
            itm = self.spellCheckLanguagesList.item(row)
            if itm.checkState() == Qt.Checked:
                languages.append(itm.data(Qt.UserRole))
        
        Preferences.setWebBrowser(
            "SpellCheckEnabled",
            self.spellCheckEnabledCheckBox.isChecked())
        Preferences.setWebBrowser(
            "SpellCheckLanguages",
            languages)
    
    @pyqtSlot()
    def on_spellCheckEnabledCheckBox_clicked(self):
        """
        Private slot handling a change of the spell checking enabled state.
        """
        enable = self.spellCheckEnabledCheckBox.isChecked()
        self.noLanguagesLabel.setEnabled(enable)
        self.spellCheckLanguagesList.setEnabled(enable)
    
    def __createLanguageString(self, language):
        """
        Private method to create a language string given a language identifier.
        
        @param language language identifier
        @type str
        @return language string
        @rtype str
        """
        loc = QLocale(language)
        
        if loc.language() == QLocale.C:
            return language
        
        country = QLocale.countryToString(loc.country())
        lang = QLocale.languageToString(loc.language())
        languageString = "{0}/{1} [{2}]".format(lang, country, language)
        return languageString


def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @type Configuration
    @return reference to the instantiated page
    @rtype ConfigurationPageBase
    """
    page = WebBrowserSpellCheckingPage()
    return page
