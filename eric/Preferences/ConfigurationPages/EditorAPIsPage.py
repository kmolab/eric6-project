# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Editor APIs configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QDir, pyqtSlot, QFileInfo
from PyQt5.QtWidgets import QInputDialog

from E5Gui.E5Application import e5App
from E5Gui import E5MessageBox
from E5Gui.E5PathPicker import E5PathPickerModes

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_EditorAPIsPage import Ui_EditorAPIsPage

import Preferences
import Utilities


class EditorAPIsPage(ConfigurationPageBase, Ui_EditorAPIsPage):
    """
    Class implementing the Editor APIs configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(EditorAPIsPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("EditorAPIsPage")
        
        self.apiFilePicker.setMode(E5PathPickerModes.OpenFileMode)
        self.apiFilePicker.setToolTip(self.tr(
            "Press to select an API file via a selection dialog"))
        self.apiFilePicker.setFilters(self.tr(
            "API File (*.api);;All Files (*)"))
        
        self.prepareApiButton.setText(self.tr("Compile APIs"))
        self.__currentAPI = None
        self.__inPreparation = False
        
        # set initial values
        self.pluginManager = e5App().getObject("PluginManager")
        self.apiAutoPrepareCheckBox.setChecked(
            Preferences.getEditor("AutoPrepareAPIs"))
        
        import QScintilla.Lexers
        self.apis = {}
        apiLanguages = sorted(
            [''] + list(QScintilla.Lexers.getSupportedApiLanguages()))
        for lang in apiLanguages:
            self.apiLanguageComboBox.addItem(
                QScintilla.Lexers.getLanguageIcon(lang, False),
                lang)
        apiProjectTypes = sorted(
            [("", "")] +
            [(trans, ptype) for ptype, trans in
                e5App().getObject("Project").getProjectTypes().items()
             ]
        )
        for projectTypeStr, projectType in apiProjectTypes:
            self.projectTypeComboBox.addItem(projectTypeStr, projectType)
        self.__currentApiLanguage = ""
        self.__currentApiProjectTypeIndex = 0
        self.__currentApiProjectType = ""
        self.on_apiLanguageComboBox_activated(self.__currentApiLanguage)
        self.on_projectTypeComboBox_activated(
            self.__currentApiProjectTypeIndex)
    
    def __apiKey(self, language, projectType):
        """
        Private method to generate a key for the apis dictionary.
        
        @param language programming language of the API
        @type str
        @param projectType project type of the API
        @type str
        @return key to be used
        @rtype str
        """
        if projectType:
            key = (language, projectType)
        else:
            key = (language, "")
        return key
    
    def save(self):
        """
        Public slot to save the Editor APIs configuration.
        """
        Preferences.setEditor(
            "AutoPrepareAPIs",
            self.apiAutoPrepareCheckBox.isChecked())
        
        language = self.apiLanguageComboBox.currentText()
        projectType = self.projectTypeComboBox.itemData(
            self.projectTypeComboBox.currentIndex())
        key = self.__apiKey(language, projectType)
        self.apis[key] = self.__editorGetApisFromApiList()
        
        for (language, projectType), apis in self.apis.items():
            Preferences.setEditorAPI(language, projectType, apis)
    
    @pyqtSlot(int)
    def on_projectTypeComboBox_activated(self, index):
        """
        Private slot to handle the selection of a project type.
        
        @param index index of the selected entry
        @type str
        """
        if self.__currentApiProjectTypeIndex == index:
            return
        
        self.__currentApiProjectTypeIndex = index
        self.__fillApisList()
        
    @pyqtSlot(str)
    def on_apiLanguageComboBox_activated(self, language):
        """
        Private slot to fill the api listbox of the api page.
        
        @param language selected API language (string)
        """
        if self.__currentApiLanguage == language:
            return
        
        self.__fillApisList()
    
    def __fillApisList(self):
        """
        Private slot to fill the list of API files.
        """
        self.apis[self.__apiKey(self.__currentApiLanguage,
                                self.__currentApiProjectType)] = \
            self.__editorGetApisFromApiList()
        
        self.__currentApiLanguage = self.apiLanguageComboBox.currentText()
        self.__currentApiProjectType = self.projectTypeComboBox.itemData(
            self.projectTypeComboBox.currentIndex())
        self.apiList.clear()
        
        if not self.__currentApiLanguage:
            self.apiGroup.setEnabled(False)
            return
            
        self.apiGroup.setEnabled(True)
        self.deleteApiFileButton.setEnabled(False)
        self.addApiFileButton.setEnabled(False)
        self.apiFilePicker.clear()
        
        key = self.__apiKey(self.__currentApiLanguage,
                            self.__currentApiProjectType)
        if key not in self.apis:
            # populate on demand
            self.apis[key] = Preferences.getEditorAPI(
                self.__currentApiLanguage,
                projectType=self.__currentApiProjectType)[:]
        for api in self.apis[key]:
            if api:
                self.apiList.addItem(api)
        self.prepareApiButton.setEnabled(self.apiList.count() > 0)
        
        from QScintilla.APIsManager import APIsManager
        self.__currentAPI = APIsManager().getAPIs(
            self.__currentApiLanguage,
            projectType=self.__currentApiProjectType)
        if self.__currentAPI is not None:
            self.__currentAPI.apiPreparationFinished.connect(
                self.__apiPreparationFinished)
            self.__currentAPI.apiPreparationCancelled.connect(
                self.__apiPreparationCancelled)
            self.__currentAPI.apiPreparationStarted.connect(
                self.__apiPreparationStarted)
            self.addInstalledApiFileButton.setEnabled(
                len(self.__currentAPI.installedAPIFiles()) > 0)
        else:
            self.addInstalledApiFileButton.setEnabled(False)
        
        self.addPluginApiFileButton.setEnabled(
            len(self.pluginManager.getPluginApiFiles(
                self.__currentApiLanguage)) > 0)
        
    def __editorGetApisFromApiList(self):
        """
        Private slot to retrieve the api filenames from the list.
        
        @return list of api filenames (list of strings)
        """
        apis = []
        for row in range(self.apiList.count()):
            apis.append(self.apiList.item(row).text())
        return apis
        
    @pyqtSlot()
    def on_addApiFileButton_clicked(self):
        """
        Private slot to add the api file displayed to the listbox.
        """
        file = self.apiFilePicker.text()
        if file:
            self.apiList.addItem(Utilities.toNativeSeparators(file))
            self.apiFilePicker.clear()
        self.prepareApiButton.setEnabled(self.apiList.count() > 0)
        
    @pyqtSlot()
    def on_deleteApiFileButton_clicked(self):
        """
        Private slot to delete the currently selected file of the listbox.
        """
        crow = self.apiList.currentRow()
        if crow >= 0:
            itm = self.apiList.takeItem(crow)       # __IGNORE_WARNING__
            del itm
        self.prepareApiButton.setEnabled(self.apiList.count() > 0)
        
    @pyqtSlot()
    def on_addInstalledApiFileButton_clicked(self):
        """
        Private slot to add an API file from the list of installed API files
        for the selected lexer language.
        """
        installedAPIFiles = self.__currentAPI.installedAPIFiles()
        if installedAPIFiles:
            installedAPIFilesPath = QFileInfo(installedAPIFiles[0]).path()
            installedAPIFilesShort = []
            for installedAPIFile in installedAPIFiles:
                installedAPIFilesShort.append(
                    QFileInfo(installedAPIFile).fileName())
            file, ok = QInputDialog.getItem(
                self,
                self.tr("Add from installed APIs"),
                self.tr("Select from the list of installed API files"),
                installedAPIFilesShort,
                0, False)
            if ok:
                self.apiList.addItem(Utilities.toNativeSeparators(
                    QFileInfo(QDir(installedAPIFilesPath), file)
                    .absoluteFilePath()))
        else:
            E5MessageBox.warning(
                self,
                self.tr("Add from installed APIs"),
                self.tr("""There are no APIs installed yet."""
                        """ Selection is not available."""))
            self.addInstalledApiFileButton.setEnabled(False)
        self.prepareApiButton.setEnabled(self.apiList.count() > 0)
        
    @pyqtSlot()
    def on_addPluginApiFileButton_clicked(self):
        """
        Private slot to add an API file from the list of API files installed
        by plugins for the selected lexer language.
        """
        pluginAPIFiles = self.pluginManager.getPluginApiFiles(
            self.__currentApiLanguage)
        pluginAPIFilesDict = {}
        for apiFile in pluginAPIFiles:
            pluginAPIFilesDict[QFileInfo(apiFile).fileName()] = apiFile
        file, ok = QInputDialog.getItem(
            self,
            self.tr("Add from Plugin APIs"),
            self.tr(
                "Select from the list of API files installed by plugins"),
            sorted(pluginAPIFilesDict.keys()),
            0, False)
        if ok:
            self.apiList.addItem(Utilities.toNativeSeparators(
                pluginAPIFilesDict[file]))
        self.prepareApiButton.setEnabled(self.apiList.count() > 0)
        
    @pyqtSlot()
    def on_prepareApiButton_clicked(self):
        """
        Private slot to prepare the API file for the currently selected
            language.
        """
        if self.__inPreparation:
            self.__currentAPI and self.__currentAPI.cancelPreparation()
        else:
            if self.__currentAPI is not None:
                self.__currentAPI.prepareAPIs(
                    ondemand=True,
                    rawList=self.__editorGetApisFromApiList())
        
    def __apiPreparationFinished(self):
        """
        Private method called after the API preparation has finished.
        """
        self.prepareApiProgressBar.reset()
        self.prepareApiProgressBar.setRange(0, 100)
        self.prepareApiProgressBar.setValue(0)
        self.prepareApiButton.setText(self.tr("Compile APIs"))
        self.__inPreparation = False
    
    def __apiPreparationCancelled(self):
        """
        Private slot called after the API preparation has been cancelled.
        """
        self.__apiPreparationFinished()
    
    def __apiPreparationStarted(self):
        """
        Private method called after the API preparation has started.
        """
        self.prepareApiProgressBar.setRange(0, 0)
        self.prepareApiProgressBar.setValue(0)
        self.prepareApiButton.setText(self.tr("Cancel compilation"))
        self.__inPreparation = True
        
    def saveState(self):
        """
        Public method to save the current state of the widget.
        
        @return tuple containing the index of the selected lexer language
            and the index of the selected project type
        @rtype tuple of int and int
        """
        return (
            self.apiLanguageComboBox.currentIndex(),
            self.projectTypeComboBox.currentIndex()
        )
        
    def setState(self, state):
        """
        Public method to set the state of the widget.
        
        @param state state data generated by saveState
        """
        self.apiLanguageComboBox.setCurrentIndex(state[0])
        self.projectTypeComboBox.setCurrentIndex(state[1])
        self.on_apiLanguageComboBox_activated(
            self.apiLanguageComboBox.currentText())
        self.on_projectTypeComboBox_activated(state[1])
    
    @pyqtSlot()
    def on_apiList_itemSelectionChanged(self):
        """
        Private slot to react on changes of API selections.
        """
        self.deleteApiFileButton.setEnabled(
            len(self.apiList.selectedItems()) > 0)
    
    @pyqtSlot(str)
    def on_apiFilePicker_textChanged(self, txt):
        """
        Private slot to handle the entering of an API file name.
        
        @param txt text of the line edit (string)
        """
        enable = txt != ""
        
        if enable:
            # check for already added file
            for row in range(self.apiList.count()):
                if txt == self.apiList.item(row).text():
                    enable = False
                    break
        
        self.addApiFileButton.setEnabled(enable)
    

def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = EditorAPIsPage()
    return page
