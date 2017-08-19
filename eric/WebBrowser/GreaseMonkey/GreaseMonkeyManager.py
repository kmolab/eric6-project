# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the manager for GreaseMonkey scripts.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QObject, QTimer, QFile, \
    QFileInfo, QDir, QSettings, QMetaObject, QUrl, Q_ARG, QCoreApplication
from PyQt5.QtWidgets import QDialog

from E5Gui import E5MessageBox

import Utilities
import Preferences

from WebBrowser.WebBrowserWindow import WebBrowserWindow


class GreaseMonkeyManager(QObject):
    """
    Class implementing the manager for GreaseMonkey scripts.
    
    @signal scriptsChanged() emitted to indicate a change of scripts
    """
    scriptsChanged = pyqtSignal()
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(GreaseMonkeyManager, self).__init__(parent)
        
        self.__disabledScripts = []
        self.__scripts = []
        self.__downloaders = []
        
        QTimer.singleShot(0, self.__load)
    
    def showConfigurationDialog(self, parent=None):
        """
        Public method to show the configuration dialog.
        
        @param parent reference to the parent widget (QWidget)
        """
        from .GreaseMonkeyConfiguration.GreaseMonkeyConfigurationDialog \
            import GreaseMonkeyConfigurationDialog
        self.__configDiaolg = GreaseMonkeyConfigurationDialog(self, parent)
        self.__configDiaolg.show()
    
    def downloadScript(self, url):
        """
        Public method to download a GreaseMonkey script.
        
        @param url URL to download script from
        @type QUrl
        """
        QMetaObject.invokeMethod(
            self, "doDownloadScript", Qt.QueuedConnection,
            Q_ARG(QUrl, url))
    
    @pyqtSlot(QUrl)
    def doDownloadScript(self, url):
        """
        Public slot to download a GreaseMonkey script.
        
        Note: The download needed to be separated in the invoking part
        (s.a.) and the one doing the real download because the invoking
        part runs in a different thread (i.e. the web engine thread).
        
        @param url URL to download script from
        @type QUrl
        """
        from .GreaseMonkeyDownloader import GreaseMonkeyDownloader
        downloader = GreaseMonkeyDownloader(
            url, self, GreaseMonkeyDownloader.DownloadMainScript)
        downloader.finished.connect(self.__downloaderFinished)
        self.__downloaders.append(downloader)
    
    def __downloaderFinished(self, fileName):
        """
        Private slot to handle the completion of a script download.
        
        @param fileName name of the downloaded script
        @type str
        """
        downloader = self.sender()
        if downloader is None or downloader not in self.__downloaders:
            return
        
        self.__downloaders.remove(downloader)
        
        deleteScript = True
        from .GreaseMonkeyScript import GreaseMonkeyScript
        script = GreaseMonkeyScript(self, fileName)
        if script.isValid():
            if not self.containsScript(script.fullName()):
                from .GreaseMonkeyAddScriptDialog import \
                    GreaseMonkeyAddScriptDialog
                dlg = GreaseMonkeyAddScriptDialog(self, script)
                deleteScript = dlg.exec_() != QDialog.Accepted
            else:
                E5MessageBox.information(
                    None,
                    QCoreApplication.translate(
                        "GreaseMonkeyManager",
                        "Install GreaseMonkey Script"),
                    QCoreApplication.translate(
                        "GreaseMonkeyManager",
                        """'{0}' is already installed.""").format(
                        script.fullName())
                )
        
        if deleteScript:
            try:
                os.remove(fileName)
            except (IOError, OSError):
                # ignore
                pass
    
    def scriptsDirectory(self):
        """
        Public method to get the path of the scripts directory.
        
        @return path of the scripts directory (string)
        """
        return os.path.join(
            Utilities.getConfigDir(), "web_browser", "greasemonkey")
    
    def requireScriptsDirectory(self):
        """
        Public method to get the path of the scripts directory.
        
        @return path of the scripts directory (string)
        """
        return os.path.join(self.scriptsDirectory(), "requires")
    
    def requireScripts(self, urlList):
        """
        Public method to get the sources of all required scripts.
        
        @param urlList list of URLs (list of string)
        @return sources of all required scripts (string)
        """
        requiresDir = QDir(self.requireScriptsDirectory())
        if not requiresDir.exists() or len(urlList) == 0:
            return ""
        
        script = ""
        
        settings = QSettings(
            os.path.join(self.requireScriptsDirectory(), "requires.ini"),
            QSettings.IniFormat)
        settings.beginGroup("Files")
        for url in urlList:
            if settings.contains(url):
                fileName = settings.value(url)
                if not QFileInfo(fileName).isAbsolute():
                    fileName = os.path.join(self.requireScriptsDirectory(),
                                            fileName)
                try:
                    f = open(fileName, "r", encoding="utf-8")
                    source = f.read().strip()
                    f.close()
                except (IOError, OSError):
                    source = ""
                if source:
                    script += source + "\n"
        
        return script
    
    def saveConfiguration(self):
        """
        Public method to save the configuration.
        """
        Preferences.setWebBrowser("GreaseMonkeyDisabledScripts",
                                  self.__disabledScripts)
    
    def allScripts(self):
        """
        Public method to get a list of all scripts.
        
        @return list of all scripts (list of GreaseMonkeyScript)
        """
        return self.__scripts[:]
    
    def containsScript(self, fullName):
        """
        Public method to check, if the given script exists.
        
        @param fullName full name of the script (string)
        @return flag indicating the existence (boolean)
        """
        for script in self.__scripts:
            if script.fullName() == fullName:
                return True
        
        return False
    
    def enableScript(self, script):
        """
        Public method to enable the given script.
        
        @param script script to be enabled (GreaseMonkeyScript)
        """
        script.setEnabled(True)
        fullName = script.fullName()
        if fullName in self.__disabledScripts:
            self.__disabledScripts.remove(fullName)
        
        collection = WebBrowserWindow.webProfile().scripts()
        collection.insert(script.webScript())
    
    def disableScript(self, script):
        """
        Public method to disable the given script.
        
        @param script script to be disabled (GreaseMonkeyScript)
        """
        script.setEnabled(False)
        fullName = script.fullName()
        if fullName not in self.__disabledScripts:
            self.__disabledScripts.append(fullName)
        
        collection = WebBrowserWindow.webProfile().scripts()
        collection.remove(collection.findScript(fullName))
    
    def addScript(self, script):
        """
        Public method to add a script.
        
        @param script script to be added (GreaseMonkeyScript)
        @return flag indicating success (boolean)
        """
        if not script or not script.isValid():
            return False
        
        self.__scripts.append(script)
        script.scriptChanged.connect(self.__scriptChanged)
        
        collection = WebBrowserWindow.webProfile().scripts()
        collection.insert(script.webScript())
        
        self.scriptsChanged.emit()
        return True
    
    def removeScript(self, script, removeFile=True):
        """
        Public method to remove a script.
        
        @param script script to be removed (GreaseMonkeyScript)
        @param removeFile flag indicating to remove the script file as well
            (bool)
        @return flag indicating success (boolean)
        """
        if not script:
            return False
        
        try:
            self.__scripts.remove(script)
        except ValueError:
            pass
        
        fullName = script.fullName()
        collection = WebBrowserWindow.webProfile().scripts()
        collection.remove(collection.findScript(fullName))
        
        if fullName in self.__disabledScripts:
            self.__disabledScripts.remove(fullName)
        
        if removeFile:
            QFile.remove(script.fileName())
            del script
        
        self.scriptsChanged.emit()
        return True
    
    def canRunOnScheme(self, scheme):
        """
        Public method to check, if scripts can be run on a scheme.
        
        @param scheme scheme to check (string)
        @return flag indicating, that scripts can be run (boolean)
        """
        return scheme in ["http", "https", "data", "ftp"]
    
    def __load(self):
        """
        Private slot to load the available scripts into the manager.
        """
        scriptsDir = QDir(self.scriptsDirectory())
        if not scriptsDir.exists():
            scriptsDir.mkpath(self.scriptsDirectory())
        
        if not scriptsDir.exists("requires"):
            scriptsDir.mkdir("requires")
        
        self.__disabledScripts = \
            Preferences.getWebBrowser("GreaseMonkeyDisabledScripts")
        
        from .GreaseMonkeyScript import GreaseMonkeyScript
        for fileName in scriptsDir.entryList(["*.js"], QDir.Files):
            absolutePath = scriptsDir.absoluteFilePath(fileName)
            script = GreaseMonkeyScript(self, absolutePath)
            
            if not script.isValid():
                del script
                continue
            
            self.__scripts.append(script)
            
            if script.fullName() in self.__disabledScripts:
                script.setEnabled(False)
            else:
                collection = WebBrowserWindow.webProfile().scripts()
                collection.insert(script.webScript())
    
    def __scriptChanged(self):
        """
        Private slot handling a changed script.
        """
        script = self.sender()
        if not script:
            return
        
        fullName = script.fullName()
        collection = WebBrowserWindow.webProfile().scripts()
        collection.remove(collection.findScript(fullName))
        collection.insert(script.webScript())
