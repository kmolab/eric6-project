# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the downloader for GreaseMonkey scripts.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QSettings, QFileInfo
from PyQt5.QtNetwork import QNetworkReply, QNetworkRequest

from WebBrowser.WebBrowserWindow import WebBrowserWindow


class GreaseMonkeyDownloader(QObject):
    """
    Class implementing the downloader for GreaseMonkey scripts.
    
    @signal finished(fileName) emitted to indicate the end of a script download
        (str)
    @signal error() emitted to indicate a script download error
    """
    finished = pyqtSignal(str)
    error = pyqtSignal()
    
    DownloadMainScript = 1
    DownloadRequireScript = 2
    
    def __init__(self, url, manager, mode):
        """
        Constructor
        
        @param url URL to download script from
        @type QUrl
        @param manager reference to the GreaseMonkey manager
        @type GreaseMonkeyManager
        @param mode download mode
        @type int (one of DownloadMainScript, DownloadRequireScript)
        """
        super(GreaseMonkeyDownloader, self).__init__()
        
        self.__manager = manager
        
        self.__reply = WebBrowserWindow.networkManager().get(
            QNetworkRequest(url))
        if mode == GreaseMonkeyDownloader.DownloadMainScript:
            self.__reply.finished.connect(self.__scriptDownloaded)
        else:
            self.__reply.finished.connect(self.__requireDownloaded)
        
        self.__fileName = ""
    
    def updateScript(self, fileName):
        """
        Public method to set the file name for the script to be downloaded.
        
        @param fileName file name for the script
        @type str
        """
        self.__fileName = fileName
    
    @pyqtSlot()
    def __scriptDownloaded(self):
        """
        Private slot to handle the finished download of a script.
        """
        self.deleteLater()
        self.__reply.deleteLater()
        
        if self.sender() != self.__reply:
            self.error.emit()
            return
        
        if self.__reply.error() != QNetworkReply.NoError:
            self.error.emit()
            return
        
        response = bytes(self.__reply.readAll()).decode()
        
        if "// ==UserScript==" not in response:
            self.error.emit()
            return
        
        if not self.__fileName:
            from WebBrowser.Tools import WebBrowserTools
            filePath = os.path.join(
                self.__manager.scriptsDirectory(),
                WebBrowserTools.getFileNameFromUrl(self.__reply.url()))
            self.__fileName = WebBrowserTools.ensureUniqueFilename(filePath)
        
        try:
            f = open(self.__fileName, "w", encoding="utf-8")
        except (IOError, OSError) as err:
            self.error.emit()
            return
        f.write(response)
        f.close()
        
        self.finished.emit(self.__fileName)
    
    @pyqtSlot()
    def __requireDownloaded(self):
        """
        Private slot to handle the finished download of a required script.
        """
        self.deleteLater()
        self.__reply.deleteLater()
        
        if self.sender() != self.__reply:
            self.error.emit()
            return
        
        if self.__reply.error() != QNetworkReply.NoError:
            self.error.emit()
            return
        
        response = bytes(self.__reply.readAll()).decode()
        
        if not response:
            self.error.emit()
            return
        
        settings = QSettings(
            os.path.join(self.__manager.requireScriptsDirectory(),
                         "requires.ini"),
            QSettings.IniFormat)
        settings.beginGroup("Files")
        
        if not self.__fileName:
            self.__fileName = settings.value(
                self.__reply.request().url().toString())
            if not self.__fileName:
                name = QFileInfo(self.__reply.request().url().path())\
                    .fileName()
                if not name:
                    name = "require.js"
                elif not name.endswith(".js"):
                    name += ".js"
                filePath = os.path.join(
                    self.__manager.requireScriptsDirectory(), name)
                from WebBrowser.Tools import WebBrowserTools
                self.__fileName = WebBrowserTools.ensureUniqueFilename(
                    filePath, "{0}")
            if not QFileInfo(self.__fileName).isAbsolute():
                self.__fileName = os.path.join(
                    self.__manager.requireScriptsDirectory(),
                    self.__fileName)
        
        try:
            f = open(self.__fileName, "w", encoding="utf-8")
        except (IOError, OSError) as err:
            self.error.emit()
            return
        f.write(response)
        f.close()
        
        settings.setValue(self.__reply.request().url().toString(),
                          QFileInfo(self.__fileName).fileName())
        
        self.finished.emit(self.__fileName)
