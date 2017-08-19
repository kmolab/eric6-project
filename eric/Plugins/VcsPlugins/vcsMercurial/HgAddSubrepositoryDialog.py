# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to add a sub-repository.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from E5Gui import E5MessageBox
from E5Gui.E5PathPicker import E5PathPickerModes

import Utilities

from .Ui_HgAddSubrepositoryDialog import Ui_HgAddSubrepositoryDialog


class HgAddSubrepositoryDialog(QDialog, Ui_HgAddSubrepositoryDialog):
    """
    Class implementing a dialog to add a sub-repository.
    """
    def __init__(self, projectPath, parent=None):
        """
        Constructor
        
        @param projectPath project directory name (string)
        @param parent reference to the parent widget (QWidget)
        """
        super(HgAddSubrepositoryDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.pathPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.pathPicker.setDefaultDirectory(projectPath)
        
        self.__ok = self.buttonBox.button(QDialogButtonBox.Ok)
        self.__ok.setEnabled(False)
        
        self.__projectPath = Utilities.toNativeSeparators(projectPath)
        
        self.typeCombo.addItem("Mercurial", "hg")
        self.typeCombo.addItem("GIT", "git")
        self.typeCombo.addItem("Subversion", "svn")
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    def __updateOk(self):
        """
        Private slot to update the state of the OK button.
        """
        path = self.pathPicker.text()
        url = self.urlEdit.text()
        
        self.__ok.setEnabled(
            path != "" and
            not os.path.isabs(path) and
            url != ""
        )
    
    @pyqtSlot(str)
    def on_pathPicker_textChanged(self, p0):
        """
        Private slot to handle the update of the path.
        
        @param p0 text of the path edit (string)
        """
        self.__updateOk()
    
    @pyqtSlot(str)
    def on_urlEdit_textChanged(self, p0):
        """
        Private slot to handle the update of the URL.
        
        @param p0 text of the URL edit (string)
        """
        self.__updateOk()
    
    @pyqtSlot(str)
    def on_pathPicker_pathSelected(self, path):
        """
        Private slot handling the selection of a subrepository path.
        
        @param path path of the subrepository
        @type str
        """
        if path.startswith(self.__projectPath + os.sep):
            path = path.replace(self.__projectPath + os.sep, "")
            self.pathPicker.setText(path)
        else:
            E5MessageBox.critical(
                self,
                self.tr("Add Sub-repository"),
                self.tr("""The sub-repository path must be inside"""
                        """ the project."""))
            self.pathPicker.setText("")
    
    def getData(self):
        """
        Public method to get the data.
        
        @return tuple containing the relative path within the project, the
            sub-repository type and the sub-repository URL (string, string,
            string)
        """
        return (
            self.pathPicker.text(),
            self.typeCombo.itemData(self.typeCombo.currentIndex()),
            self.urlEdit.text()
        )
