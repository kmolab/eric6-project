# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Mercurial Options Dialog for a new project from the
repository.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QComboBox

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_HgNewProjectOptionsDialog import Ui_HgNewProjectOptionsDialog
from .Config import ConfigHgSchemes

import Utilities
import Preferences
import UI.PixmapCache


class HgNewProjectOptionsDialog(QDialog, Ui_HgNewProjectOptionsDialog):
    """
    Class implementing the Options Dialog for a new project from the
    repository.
    """
    def __init__(self, vcs, parent=None):
        """
        Constructor
        
        @param vcs reference to the version control object
        @param parent parent widget (QWidget)
        """
        super(HgNewProjectOptionsDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.vcsProjectDirPicker.setMode(E5PathPickerModes.DirectoryMode)
        
        self.__vcs = vcs
        
        vcsUrlHistory = self.__vcs.getPlugin().getPreferences(
            "RepositoryUrlHistory")
        self.vcsUrlPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.vcsUrlPicker.setInsertPolicy(QComboBox.InsertAtTop)
        self.vcsUrlPicker.setSizeAdjustPolicy(
            QComboBox.AdjustToMinimumContentsLength)
        self.vcsUrlPicker.setPathsList(vcsUrlHistory)
        self.vcsUrlClearHistoryButton.setIcon(
            UI.PixmapCache.getIcon("editDelete.png"))
        self.vcsUrlPicker.setText("")
        
        ipath = Preferences.getMultiProject("Workspace") or \
            Utilities.getHomeDir()
        self.__initPaths = [
            Utilities.fromNativeSeparators(ipath),
            Utilities.fromNativeSeparators(ipath) + "/",
        ]
        self.vcsProjectDirPicker.setText(self.__initPaths[0])
        
        self.lfNoteLabel.setVisible(
            self.__vcs.isExtensionActive("largefiles"))
        self.largeCheckBox.setVisible(
            self.__vcs.isExtensionActive("largefiles"))
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    @pyqtSlot(str)
    def on_vcsProjectDirPicker_textChanged(self, txt):
        """
        Private slot to handle a change of the project directory.
        
        @param txt name of the project directory (string)
        """
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            bool(txt) and
            Utilities.fromNativeSeparators(txt) not in self.__initPaths)
    
    @pyqtSlot(str)
    def on_vcsUrlPicker_textChanged(self, txt):
        """
        Private slot to handle changes of the URL.
        
        @param txt current text of the line edit (string)
        """
        url = QUrl.fromUserInput(txt)
        enable = url.isValid() and url.scheme() in ConfigHgSchemes
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)
        
        self.vcsUrlPicker.setPickerEnabled(url.scheme() == "file" or
                                           len(txt) == 0)
    
    @pyqtSlot()
    def on_vcsUrlClearHistoryButton_clicked(self):
        """
        Private slot to clear the history of entered repository URLs.
        """
        currentVcsUrl = self.vcsUrlPicker.text()
        self.vcsUrlPicker.clear()
        self.vcsUrlPicker.setText(currentVcsUrl)
        
        self.__saveHistory()
    
    def getData(self):
        """
        Public slot to retrieve the data entered into the dialog and to
        save the history of entered repository URLs.
        
        @return a tuple of a string (project directory) and a dictionary
            containing the data entered.
        """
        self.__saveHistory()
        
        url = QUrl.fromUserInput(self.vcsUrlPicker.text().replace("\\", "/"))
        vcsdatadict = {
            "url": url.toString(QUrl.None_),
            "revision": self.vcsRevisionEdit.text(),
            "largefiles": self.largeCheckBox.isChecked(),
        }
        return (self.vcsProjectDirPicker.text(), vcsdatadict)
    
    def __saveHistory(self):
        """
        Private method to save the repository URL history.
        """
        url = self.vcsUrlPicker.text()
        vcsUrlHistory = self.vcsUrlPicker.getPathItems()
        if url not in vcsUrlHistory:
            vcsUrlHistory.insert(0, url)
        
        # max. list sizes is hard coded to 20 entries
        newVcsUrlHistory = [url for url in vcsUrlHistory if url]
        if len(newVcsUrlHistory) > 20:
            newVcsUrlHistory = newVcsUrlHistory[:20]
        
        self.__vcs.getPlugin().setPreferences(
            "RepositoryUrlHistory", newVcsUrlHistory)
