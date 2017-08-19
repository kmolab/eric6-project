# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the project properties dialog.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import QDir, pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from E5Gui.E5Application import e5App
from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_PropertiesDialog import Ui_PropertiesDialog

import Utilities
import Preferences


class PropertiesDialog(QDialog, Ui_PropertiesDialog):
    """
    Class implementing the project properties dialog.
    """
    def __init__(self, project, new=True, parent=None, name=None):
        """
        Constructor
        
        @param project reference to the project object
        @param new flag indicating the generation of a new project
        @param parent parent widget of this dialog (QWidget)
        @param name name of this dialog (string)
        """
        super(PropertiesDialog, self).__init__(parent)
        if name:
            self.setObjectName(name)
        self.setupUi(self)
        
        self.dirPicker.setMode(E5PathPickerModes.DirectoryMode)
        self.mainscriptPicker.setMode(E5PathPickerModes.OpenFileMode)
        
        self.project = project
        self.newProject = new
        self.transPropertiesDlg = None
        self.spellPropertiesDlg = None
        
        patterns = []
        for pattern, filetype in self.project.pdata["FILETYPES"].items():
            if filetype == "SOURCES":
                patterns.append(pattern)
        filters = self.tr("Source Files ({0});;All Files (*)")\
            .format(" ".join(sorted(patterns)))
        self.mainscriptPicker.setFilters(filters)
        
        self.languageComboBox.addItems(project.getProgrammingLanguages())
        
        projectTypes = project.getProjectTypes()
        self.projectTypeComboBox.clear()
        for projectType in sorted(projectTypes.keys()):
            self.projectTypeComboBox.addItem(
                projectTypes[projectType], projectType)
        
        ipath = Preferences.getMultiProject("Workspace") or \
            Utilities.getHomeDir()
        self.__initPaths = [
            Utilities.fromNativeSeparators(ipath),
            Utilities.fromNativeSeparators(ipath) + "/",
        ]
        
        if not new:
            name = os.path.splitext(self.project.pfile)[0]
            self.nameEdit.setText(os.path.basename(name))
            self.languageComboBox.setCurrentIndex(
                self.languageComboBox.findText(
                    self.project.pdata["PROGLANGUAGE"]))
            self.mixedLanguageCheckBox.setChecked(
                self.project.pdata["MIXEDLANGUAGE"])
            curIndex = self.projectTypeComboBox.findData(
                self.project.pdata["PROJECTTYPE"])
            if curIndex == -1:
                curIndex = self.projectTypeComboBox.findData("Qt4")
            self.projectTypeComboBox.setCurrentIndex(curIndex)
            self.dirPicker.setText(self.project.ppath)
            self.versionEdit.setText(self.project.pdata["VERSION"])
            self.mainscriptPicker.setText(self.project.pdata["MAINSCRIPT"])
            self.authorEdit.setText(self.project.pdata["AUTHOR"])
            self.emailEdit.setText(self.project.pdata["EMAIL"])
            self.descriptionEdit.setPlainText(
                self.project.pdata["DESCRIPTION"])
            self.eolComboBox.setCurrentIndex(self.project.pdata["EOL"])
            self.vcsLabel.show()
            if self.project.vcs is not None:
                vcsSystemsDict = e5App().getObject("PluginManager")\
                    .getPluginDisplayStrings("version_control")
                try:
                    vcsSystemDisplay = \
                        vcsSystemsDict[self.project.pdata["VCS"]]
                except KeyError:
                    vcsSystemDisplay = "None"
                self.vcsLabel.setText(
                    self.tr(
                        "The project is version controlled by <b>{0}</b>.")
                    .format(vcsSystemDisplay))
                self.vcsInfoButton.show()
            else:
                self.vcsLabel.setText(
                    self.tr("The project is not version controlled."))
                self.vcsInfoButton.hide()
            self.vcsCheckBox.hide()
        else:
            self.languageComboBox.setCurrentIndex(
                self.languageComboBox.findText("Python3"))
            self.projectTypeComboBox.setCurrentIndex(
                self.projectTypeComboBox.findData("PyQt5"))
            self.dirPicker.setText(self.__initPaths[0])
            self.versionEdit.setText('0.1')
            self.vcsLabel.hide()
            self.vcsInfoButton.hide()
            if not self.project.vcsSoftwareAvailable():
                self.vcsCheckBox.hide()
        
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            bool(self.dirPicker.text()) and
            self.dirPicker.text() not in
            self.__initPaths)
    
    @pyqtSlot(str)
    def on_languageComboBox_currentIndexChanged(self, language):
        """
        Private slot handling the selection of a programming language.
        
        @param language selected programming language (string)
        """
        curProjectType = self.getProjectType()
        
        self.projectTypeComboBox.clear()
        projectTypes = self.project.getProjectTypes(language)
        for projectType in sorted(projectTypes.keys()):
            self.projectTypeComboBox.addItem(
                projectTypes[projectType], projectType)
        
        index = self.projectTypeComboBox.findData(curProjectType)
        if index == -1:
            index = 0
        self.projectTypeComboBox.setCurrentIndex(index)
    
    @pyqtSlot(str)
    def on_dirPicker_textChanged(self, txt):
        """
        Private slot to handle a change of the project directory.
        
        @param txt name of the project directory (string)
        """
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            bool(txt) and
            Utilities.fromNativeSeparators(txt) not in self.__initPaths)
    
    @pyqtSlot()
    def on_spellPropertiesButton_clicked(self):
        """
        Private slot to display the spelling properties dialog.
        """
        if self.spellPropertiesDlg is None:
            from .SpellingPropertiesDialog import SpellingPropertiesDialog
            self.spellPropertiesDlg = \
                SpellingPropertiesDialog(self.project, self.newProject, self)
        res = self.spellPropertiesDlg.exec_()
        if res == QDialog.Rejected:
            self.spellPropertiesDlg.initDialog()  # reset the dialogs contents
    
    @pyqtSlot()
    def on_transPropertiesButton_clicked(self):
        """
        Private slot to display the translations properties dialog.
        """
        if self.transPropertiesDlg is None:
            from .TranslationPropertiesDialog import \
                TranslationPropertiesDialog
            self.transPropertiesDlg = \
                TranslationPropertiesDialog(self.project, self.newProject,
                                            self)
        else:
            self.transPropertiesDlg.initFilters()
        res = self.transPropertiesDlg.exec_()
        if res == QDialog.Rejected:
            self.transPropertiesDlg.initDialog()  # reset the dialogs contents
    
    @pyqtSlot(str)
    def on_mainscriptPicker_pathSelected(self, script):
        """
        Private slot to check the selected main script name.
        
        @param script name of the main script
        @type str
        """
        if script:
            ppath = self.dirPicker.text()
            if ppath:
                ppath = QDir(ppath).absolutePath() + QDir.separator()
                script = script.replace(ppath, "")
            self.mainscriptPicker.setText(script)
    
    @pyqtSlot()
    def on_mainscriptPicker_aboutToShowPathPickerDialog(self):
        """
        Private slot to perform actions before the main script selection dialog
        is shown.
        """
        path = self.dirPicker.text()
        if not path:
            path = QDir.currentPath()
        self.mainscriptPicker.setDefaultDirectory(path)
    
    @pyqtSlot()
    def on_vcsInfoButton_clicked(self):
        """
        Private slot to display a vcs information dialog.
        """
        if self.project.vcs is None:
            return
            
        from VCS.RepositoryInfoDialog import VcsRepositoryInfoDialog
        info = self.project.vcs.vcsRepositoryInfos(self.project.ppath)
        dlg = VcsRepositoryInfoDialog(self, info)
        dlg.exec_()
    
    def getProjectType(self):
        """
        Public method to get the selected project type.
        
        @return selected UI type (string)
        """
        return self.projectTypeComboBox.itemData(
            self.projectTypeComboBox.currentIndex())
    
    def getPPath(self):
        """
        Public method to get the project path.
        
        @return data of the project directory edit (string)
        """
        return os.path.abspath(self.dirPicker.text())
    
    def storeData(self):
        """
        Public method to store the entered/modified data.
        """
        self.project.ppath = os.path.abspath(self.dirPicker.text())
        fn = self.nameEdit.text()
        if fn:
            self.project.name = fn
            fn = "{0}.e4p".format(fn)
            self.project.pfile = os.path.join(self.project.ppath, fn)
        else:
            self.project.pfile = ""
        self.project.pdata["VERSION"] = self.versionEdit.text()
        fn = self.mainscriptPicker.text()
        if fn:
            fn = self.project.getRelativePath(fn)
            self.project.pdata["MAINSCRIPT"] = fn
            self.project.translationsRoot = os.path.splitext(fn)[0]
        else:
            self.project.pdata["MAINSCRIPT"] = ""
            self.project.translationsRoot = ""
        self.project.pdata["AUTHOR"] = self.authorEdit.text()
        self.project.pdata["EMAIL"] = self.emailEdit.text()
        self.project.pdata["DESCRIPTION"] = self.descriptionEdit.toPlainText()
        self.project.pdata["PROGLANGUAGE"] = \
            self.languageComboBox.currentText()
        self.project.pdata["MIXEDLANGUAGE"] = \
            self.mixedLanguageCheckBox.isChecked()
        projectType = self.getProjectType()
        if projectType is not None:
            self.project.pdata["PROJECTTYPE"] = projectType
        self.project.pdata["EOL"] = self.eolComboBox.currentIndex()
        
        self.project.vcsRequested = self.vcsCheckBox.isChecked()
        
        if self.spellPropertiesDlg is not None:
            self.spellPropertiesDlg.storeData()
        
        if self.transPropertiesDlg is not None:
            self.transPropertiesDlg.storeData()
