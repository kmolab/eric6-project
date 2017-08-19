# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a synchronization handler using a shared directory.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, QByteArray, QFileInfo, QCoreApplication

from .SyncHandler import SyncHandler

from WebBrowser.WebBrowserWindow import WebBrowserWindow

import Preferences


class DirectorySyncHandler(SyncHandler):
    """
    Class implementing a synchronization handler using a shared directory.
    
    @signal syncStatus(type_, message) emitted to indicate the synchronization
        status (string one of "bookmarks", "history", "passwords",
        "useragents" or "speeddial", string)
    @signal syncError(message) emitted for a general error with the error
        message (string)
    @signal syncMessage(message) emitted to send a message about
        synchronization (string)
    @signal syncFinished(type_, done, download) emitted after a
        synchronization has finished (string one of "bookmarks", "history",
        "passwords", "useragents" or "speeddial", boolean, boolean)
    """
    syncStatus = pyqtSignal(str, str)
    syncError = pyqtSignal(str)
    syncMessage = pyqtSignal(str)
    syncFinished = pyqtSignal(str, bool, bool)
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(DirectorySyncHandler, self).__init__(parent)
        self.__forceUpload = False
        
        self.__remoteFilesFound = []
    
    def initialLoadAndCheck(self, forceUpload):
        """
        Public method to do the initial check.
        
        @keyparam forceUpload flag indicating a forced upload of the files
            (boolean)
        """
        if not Preferences.getWebBrowser("SyncEnabled"):
            return
        
        self.__forceUpload = forceUpload
        
        self.__remoteFilesFound = []
        
        # check the existence of the shared directory; create it, if it is
        # not there
        if not os.path.exists(Preferences.getWebBrowser("SyncDirectoryPath")):
            try:
                os.makedirs(Preferences.getWebBrowser("SyncDirectoryPath"))
            except OSError as err:
                self.syncError.emit(
                    self.tr("Error creating the shared directory.\n{0}")
                    .format(str(err)))
                return
        
        self.__initialSync()
    
    def __downloadFile(self, type_, fileName, timestamp):
        """
        Private method to downlaod the given file.
        
        @param type_ type of the synchronization event (string one
            of "bookmarks", "history", "passwords", "useragents" or
            "speeddial")
        @param fileName name of the file to be downloaded (string)
        @param timestamp time stamp in seconds of the file to be downloaded
            (integer)
        """
        self.syncStatus.emit(type_, self._messages[type_]["RemoteExists"])
        try:
            f = open(os.path.join(
                Preferences.getWebBrowser("SyncDirectoryPath"),
                self._remoteFiles[type_]), "rb")
            data = f.read()
            f.close()
        except IOError as err:
            self.syncStatus.emit(
                type_,
                self.tr("Cannot read remote file.\n{0}").format(str(err)))
            self.syncFinished.emit(type_, False, True)
            return
        
        QCoreApplication.processEvents()
        ok, error = self.writeFile(QByteArray(data), fileName, type_,
                                   timestamp)
        if not ok:
            self.syncStatus.emit(type_, error)
        self.syncFinished.emit(type_, ok, True)
    
    def __uploadFile(self, type_, fileName):
        """
        Private method to upload the given file.
        
        @param type_ type of the synchronization event (string one
            of "bookmarks", "history", "passwords", "useragents" or
            "speeddial")
        @param fileName name of the file to be uploaded (string)
        """
        QCoreApplication.processEvents()
        data = self.readFile(fileName, type_)
        if data.isEmpty():
            self.syncStatus.emit(type_, self._messages[type_]["LocalMissing"])
            self.syncFinished.emit(type_, False, False)
            return
        else:
            try:
                f = open(os.path.join(
                    Preferences.getWebBrowser("SyncDirectoryPath"),
                    self._remoteFiles[type_]), "wb")
                f.write(bytes(data))
                f.close()
            except IOError as err:
                self.syncStatus.emit(
                    type_,
                    self.tr("Cannot write remote file.\n{0}").format(
                        str(err)))
                self.syncFinished.emit(type_, False, False)
                return
            
        self.syncFinished.emit(type_, True, False)
    
    def __initialSyncFile(self, type_, fileName):
        """
        Private method to do the initial synchronization of the given file.
        
        @param type_ type of the synchronization event (string one
            of "bookmarks", "history", "passwords", "useragents" or
            "speeddial")
        @param fileName name of the file to be synchronized (string)
        """
        if not self.__forceUpload and \
                os.path.exists(os.path.join(
                    Preferences.getWebBrowser("SyncDirectoryPath"),
                    self._remoteFiles[type_])) and \
                QFileInfo(fileName).lastModified() <= QFileInfo(
                    os.path.join(
                        Preferences.getWebBrowser("SyncDirectoryPath"),
                        self._remoteFiles[type_])).lastModified():
            self.__downloadFile(
                type_, fileName,
                QFileInfo(os.path.join(
                    Preferences.getWebBrowser("SyncDirectoryPath"),
                    self._remoteFiles[type_])).lastModified().toTime_t())
        else:
            if not os.path.exists(os.path.join(
                    Preferences.getWebBrowser("SyncDirectoryPath"),
                    self._remoteFiles[type_])):
                self.syncStatus.emit(
                    type_, self._messages[type_]["RemoteMissing"])
            else:
                self.syncStatus.emit(
                    type_, self._messages[type_]["LocalNewer"])
            self.__uploadFile(type_, fileName)
    
    def __initialSync(self):
        """
        Private slot to do the initial synchronization.
        """
        QCoreApplication.processEvents()
        # Bookmarks
        if Preferences.getWebBrowser("SyncBookmarks"):
            self.__initialSyncFile(
                "bookmarks",
                WebBrowserWindow.bookmarksManager().getFileName())
        
        QCoreApplication.processEvents()
        # History
        if Preferences.getWebBrowser("SyncHistory"):
            self.__initialSyncFile(
                "history",
                WebBrowserWindow.historyManager().getFileName())
        
        QCoreApplication.processEvents()
        # Passwords
        if Preferences.getWebBrowser("SyncPasswords"):
            self.__initialSyncFile(
                "passwords",
                WebBrowserWindow.passwordManager().getFileName())
        
        QCoreApplication.processEvents()
        # User Agent Settings
        if Preferences.getWebBrowser("SyncUserAgents"):
            self.__initialSyncFile(
                "useragents",
                WebBrowserWindow.userAgentsManager().getFileName())
        
        QCoreApplication.processEvents()
        # Speed Dial Settings
        if Preferences.getWebBrowser("SyncSpeedDial"):
            self.__initialSyncFile(
                "speeddial",
                WebBrowserWindow.speedDial().getFileName())
        
        self.__forceUpload = False
        self.syncMessage.emit(self.tr("Synchronization finished"))
    
    def __syncFile(self, type_, fileName):
        """
        Private method to synchronize the given file.
        
        @param type_ type of the synchronization event (string one
            of "bookmarks", "history", "passwords", "useragents" or
            "speeddial")
        @param fileName name of the file to be synchronized (string)
        """
        self.syncStatus.emit(type_, self._messages[type_]["Uploading"])
        self.__uploadFile(type_, fileName)
    
    def syncBookmarks(self):
        """
        Public method to synchronize the bookmarks.
        """
        self.__syncFile(
            "bookmarks",
            WebBrowserWindow.bookmarksManager().getFileName())
    
    def syncHistory(self):
        """
        Public method to synchronize the history.
        """
        self.__syncFile(
            "history",
            WebBrowserWindow.historyManager().getFileName())
    
    def syncPasswords(self):
        """
        Public method to synchronize the passwords.
        """
        self.__syncFile(
            "passwords",
            WebBrowserWindow.passwordManager().getFileName())
    
    def syncUserAgents(self):
        """
        Public method to synchronize the user agents.
        """
        self.__syncFile(
            "useragents",
            WebBrowserWindow.userAgentsManager().getFileName())
    
    def syncSpeedDial(self):
        """
        Public method to synchronize the speed dial data.
        """
        self.__syncFile(
            "speeddial",
            WebBrowserWindow.speedDial().getFileName())
    
    def shutdown(self):
        """
        Public method to shut down the handler.
        """
        # nothing to do
        return
