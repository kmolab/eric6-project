# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to add a file to the project.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_AddFileDialog import Ui_AddFileDialog


class AddFileDialog(QDialog, Ui_AddFileDialog):
    """
    Class implementing a dialog to add a file to the project.
    """
    def __init__(self, pro, parent=None, fileTypeFilter=None, name=None,
                 startdir=None):
        """
        Constructor
        
        @param pro reference to the project object
        @param parent parent widget of this dialog (QWidget)
        @param fileTypeFilter filter specification for the file to add (string)
        @param name name of this dialog (string)
        @param startdir start directory for the selection dialog
        """
        super(AddFileDialog, self).__init__(parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        
        self.sourceFilesPicker.setMode(E5PathPickerModes.OpenFilesMode)
        self.targetDirPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.targetDirPicker.setDefaultDirectory(startdir)
        
        self.targetDirPicker.setText(pro.ppath)
        self.fileTypeFilter = fileTypeFilter
        self.ppath = pro.ppath
        self.startdir = startdir
        self.filetypes = pro.pdata["FILETYPES"]
        # save a reference to the filetypes dict
        
        if self.fileTypeFilter is not None:
            self.sourcecodeCheckBox.hide()
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
        
    @pyqtSlot()
    def on_sourceFilesPicker_aboutToShowPathPickerDialog(self):
        """
        Private slot to perform actions before the source files selection
        dialog is shown.
        """
        path = self.targetDirPicker.text()
        if not path:
            path = self.startdir
        self.sourceFilesPicker.setDefaultDirectory(path)
        
        if self.fileTypeFilter is None:
            patterns = {
                "SOURCES": [],
                "FORMS": [],
                "RESOURCES": [],
                "INTERFACES": [],
                "TRANSLATIONS": [],
            }
            for pattern, filetype in list(self.filetypes.items()):
                if filetype in patterns:
                    patterns[filetype].append(pattern)
            dfilter = self.tr(
                "Source Files ({0});;"
                "Forms Files ({1});;"
                "Resource Files ({2});;"
                "Interface Files ({3});;"
                "Translation Files ({4});;"
                "All Files (*)")\
                .format(
                    " ".join(patterns["SOURCES"]),
                    " ".join(patterns["FORMS"]),
                    " ".join(patterns["RESOURCES"]),
                    " ".join(patterns["INTERFACES"]),
                    " ".join(patterns["TRANSLATIONS"]))
            caption = self.tr("Select Files")
        elif self.fileTypeFilter == 'form':
            patterns = []
            for pattern, filetype in list(self.filetypes.items()):
                if filetype == "FORMS":
                    patterns.append(pattern)
            dfilter = self.tr("Forms Files ({0})")\
                .format(" ".join(patterns))
            caption = self.tr("Select user-interface files")
        elif self.fileTypeFilter == "resource":
            patterns = []
            for pattern, filetype in list(self.filetypes.items()):
                if filetype == "RESOURCES":
                    patterns.append(pattern)
            dfilter = self.tr("Resource Files ({0})")\
                .format(" ".join(patterns))
            caption = self.tr("Select resource files")
        elif self.fileTypeFilter == 'source':
            patterns = []
            for pattern, filetype in list(self.filetypes.items()):
                if filetype == "SOURCES":
                    patterns.append(pattern)
            dfilter = self.tr("Source Files ({0});;All Files (*)")\
                .format(" ".join(patterns))
            caption = self.tr("Select source files")
        elif self.fileTypeFilter == 'interface':
            patterns = []
            for pattern, filetype in list(self.filetypes.items()):
                if filetype == "INTERFACES":
                    patterns.append(pattern)
            dfilter = self.tr("Interface Files ({0})")\
                .format(" ".join(patterns))
            caption = self.tr("Select interface files")
        elif self.fileTypeFilter == 'translation':
            patterns = []
            for pattern, filetype in list(self.filetypes.items()):
                if filetype == "TRANSLATIONS":
                    patterns.append(pattern)
            dfilter = self.tr("Translation Files ({0})")\
                .format(" ".join(patterns))
            caption = self.tr("Select translation files")
        elif self.fileTypeFilter == 'others':
            dfilter = self.tr("All Files (*)")
            caption = self.tr("Select files")
        else:
            dfilter = ""
            caption = ""
        
        self.sourceFilesPicker.setWindowTitle(caption)
        self.sourceFilesPicker.setFilters(dfilter)
        
    @pyqtSlot(str)
    def on_sourceFilesPicker_textChanged(self, sfile):
        """
        Private slot to handle the source file text changed.
        
        If the entered source directory is a subdirectory of the current
        projects main directory, the target directory path is synchronized.
        It is assumed, that the user wants to add a bunch of files to
        the project in place.
        
        @param sfile the text of the source file picker (string)
        """
        sfile = self.sourceFilesPicker.firstPath()
        if sfile.startswith(self.ppath):
            if os.path.isdir(sfile):
                directory = sfile
            else:
                directory = os.path.dirname(sfile)
            self.targetDirPicker.setText(directory)
        
    def getData(self):
        """
        Public slot to retrieve the dialogs data.
        
        @return tuple of three values (list of string, string, boolean)
            giving the source files, the target directory and a flag
            telling, whether the files shall be added as source code
        """
        return (
            self.sourceFilesPicker.paths(),
            self.targetDirPicker.text(),
            self.sourcecodeCheckBox.isChecked())
