# -*- coding: utf-8 -*-

# Copyright (c) 2013 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the archive data.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_HgArchiveDialog import Ui_HgArchiveDialog

import Utilities


class HgArchiveDialog(QDialog, Ui_HgArchiveDialog):
    """
    Class implementing a dialog to enter the archive data.
    """
    def __init__(self, vcs, parent=None):
        """
        Constructor
        
        @param vcs reference to the Mercurial object (Hg)
        @param parent reference to the parent widget (QWidget)
        """
        super(HgArchiveDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.archivePicker.setMode(
            E5PathPickerModes.SaveFileEnsureExtensionMode)
        
        self.typeComboBox.addItem(
            self.tr("Detect Automatically"), "")
        self.typeComboBox.addItem(
            self.tr("Directory of Files"), "files")
        self.typeComboBox.addItem(
            self.tr("Uncompressed TAR-Archive"), "tar")
        self.typeComboBox.addItem(
            self.tr("Bzip2 compressed TAR-Archive"), "tbz2")
        self.typeComboBox.addItem(
            self.tr("Gzip compressed TAR-Archive"), "tgz")
        self.typeComboBox.addItem(
            self.tr("Uncompressed ZIP-Archive"), "uzip")
        self.typeComboBox.addItem(
            self.tr("Compressed ZIP-Archive"), "zip")
        
        self.__unixFileFilters = [
            self.tr("Bzip2 compressed TAR-Archive (*.tar.bz2)"),
            self.tr("Gzip compressed TAR-Archive (*.tar.gz)"),
            self.tr("Uncompressed TAR-Archive (*.tar)"),
        ]
        self.__windowsFileFilters = [
            self.tr("Compressed ZIP-Archive (*.zip)"),
            self.tr("Uncompressed ZIP-Archive (*.uzip)")
        ]
        if Utilities.isWindowsPlatform():
            fileFilters = ";;".join(
                self.__windowsFileFilters + self.__unixFileFilters)
        else:
            fileFilters = ";;".join(
                self.__unixFileFilters + self.__windowsFileFilters)
        fileFilters += ";;" + self.tr("All Files (*)")
        
        self.archivePicker.setFilters(fileFilters)
        
        self.__typeFilters = {
            "tar": ["*.tar"],
            "tbz2": ["*.tar.bz2", "*.tbz2"],
            "tgz": ["*.tar.gz", "*.tgz"],
            "uzip": ["*.uzip", "*.zip"],
            "zip": ["*.zip"],
        }
        
        self.subReposCheckBox.setEnabled(vcs.hasSubrepositories())
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        self.__projectPath = \
            vcs.getPlugin().getProjectHelper().getProject().getProjectPath()
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    @pyqtSlot(str)
    def on_archivePicker_textChanged(self, archive):
        """
        Private slot to handle changes of the archive name.
        
        @param archive name of the archive (string)
        """
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(archive != "")
    
    @pyqtSlot(int)
    def on_typeComboBox_activated(self, index):
        """
        Private slot to react on changes of the selected archive type.
        
        @param index index of the selected type (integer)
        """
        type_ = self.typeComboBox.itemData(index)
        if type_ == "files":
            self.archivePicker.setMode(E5PathPickerModes.DirectoryMode)
        else:
            self.archivePicker.setMode(
                E5PathPickerModes.SaveFileEnsureExtensionMode)
            if type_ in self.__typeFilters:
                self.archivePicker.setNameFilters(
                    self.__typeFilters[type_])
            else:
                self.archivePicker.setNameFilters([])
    
    def getData(self):
        """
        Public method to retrieve the data.
        
        @return tuple giving the archive name (string), the archive type
            (string), the directory prefix 8string) and a flag indicating
            to recurse into subrepositories (boolean)
        """
        return (
            self.archivePicker.text(),
            self.typeComboBox.itemData(self.typeComboBox.currentIndex()),
            self.prefixEdit.text(),
            self.subReposCheckBox.isChecked(),
        )
