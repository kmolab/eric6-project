# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module containing a web site icon storage object.
"""

from __future__ import unicode_literals

import json
import os

from PyQt5.QtCore import pyqtSignal, QObject, QByteArray, QBuffer, QIODevice, \
    QUrl
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QDialog

from Utilities.AutoSaver import AutoSaver

import UI.PixmapCache


class WebIconProvider(QObject):
    """
    Class implementing a web site icon storage.
    
    @signal changed() emitted to indicate a change of the icons database
    """
    changed = pyqtSignal()
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(WebIconProvider, self).__init__(parent)
        
        self.__encoding = "iso-8859-1"
        self.__iconsFileName = "web_site_icons.json"
        self.__iconDatabasePath = ""    # saving of icons disabled
        
        self.__iconsDB = {}
        self.__loaded = False
        
        self.__saveTimer = AutoSaver(self, self.save)
        
        self.changed.connect(self.__saveTimer.changeOccurred)
    
    def setIconDatabasePath(self, path):
        """
        Public method to set the path for the web site icons store.
        
        @param path path to store the icons file to
        @type str
        """
        if path != self.__iconDatabasePath:
            self.close()
        
        self.__iconDatabasePath = path
    
    def iconDatabasePath(self):
        """
        Public method o get the path for the web site icons store.
        
        @return path to store the icons file to
        @rtype str
        """
        return self.__iconDatabasePath
    
    def close(self):
        """
        Public method to close the web icon provider.
        """
        self.__saveTimer.saveIfNeccessary()
        self.__loaded = False
        self.__iconsDB = {}
    
    def load(self):
        """
        Public method to load the bookmarks.
        """
        if self.__loaded:
            return
        
        if self.__iconDatabasePath:
            filename = os.path.join(self.__iconDatabasePath,
                                    self.__iconsFileName)
            try:
                f = open(filename, "r")
                db = json.load(f)
                f.close()
            except (IOError, OSError):
                # ignore silentyl
                db = {}
            
            self.__iconsDB = {}
            for url, data in db.items():
                self.__iconsDB[url] = QIcon(QPixmap.fromImage(QImage.fromData(
                    QByteArray(data.encode(self.__encoding)))))
        
        self.__loaded = True
    
    def save(self):
        """
        Public method to save the zoom values.
        """
        if not self.__loaded:
            return
        
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        if not WebBrowserWindow.isPrivate() and bool(self.__iconDatabasePath):
            db = {}
            for url, icon in self.__iconsDB.items():
                ba = QByteArray()
                buffer = QBuffer(ba)
                buffer.open(QIODevice.WriteOnly)
                icon.pixmap(32).toImage().save(buffer, "PNG")
                db[url] = bytes(buffer.data()).decode(self.__encoding)
            
            filename = os.path.join(self.__iconDatabasePath,
                                    self.__iconsFileName)
            try:
                f = open(filename, "w")
                json.dump(db, f)
                f.close()
            except (IOError, OSError):
                # ignore silentyl
                pass
    
    def saveIcon(self, view):
        """
        Public method to save a web site icon.
        
        @param view reference to the view object
        @type WebBrowserView
        """
        scheme = view.url().scheme()
        if scheme in ["eric", "about", "qthelp", "file", "abp", "ftp"]:
            return
        
        self.load()
        
        if view.mainWindow().isPrivate():
            return
        
        urlStr = self.__urlToString(view.url())
        self.__iconsDB[urlStr] = view.icon()
        
        self.changed.emit()
    
    def __urlToString(self, url):
        """
        Private method to convert an URL to a string.
        
        @param url URL to be converted
        @type QUrl
        @return string representation of the URL
        @rtype str
        """
        return url.toString(QUrl.PrettyDecoded | QUrl.RemoveUserInfo |
                            QUrl.RemoveFragment)
    
    def iconForUrl(self, url):
        """
        Public method to get an icon for an URL.
        
        @param url URL to get icon for
        @type QUrl
        @return icon for the URL
        @rtype QIcon
        """
        scheme = url.scheme()
        if scheme in ["eric", "about"]:
            return UI.PixmapCache.getIcon("ericWeb.png")
        elif scheme == "qthelp":
            return UI.PixmapCache.getIcon("qthelp.png")
        elif scheme == "file":
            return UI.PixmapCache.getIcon("fileMisc.png")
        elif scheme == "abp":
            return UI.PixmapCache.getIcon("adBlockPlus.png")
        elif scheme == "ftp":
            return UI.PixmapCache.getIcon("network-server.png")
        
        self.load()
        
        urlStr = self.__urlToString(url)
        for iconUrlStr in self.__iconsDB:
            if iconUrlStr.startswith(urlStr):
                return self.__iconsDB[iconUrlStr]
        
        # try replacing http scheme with https scheme
        url = QUrl(url)
        if url.scheme() == "http":
            url.setScheme("https")
        urlStr = self.__urlToString(url)
        for iconUrlStr in self.__iconsDB:
            if iconUrlStr.startswith(urlStr):
                return self.__iconsDB[iconUrlStr]
        
        if scheme == "https":
            return UI.PixmapCache.getIcon("securityHigh32.png")
        else:
            return UI.PixmapCache.getIcon("defaultIcon.png")
    
    def clear(self):
        """
        Public method to clear the icons cache.
        """
        self.load()
        self.__iconsDB = {}
        self.changed.emit()
        self.__saveTimer.saveIfNeccessary()
    
    def showWebIconDialog(self):
        """
        Public method to show a dialog to manage the Favicons.
        """
        self.load()
        
        from .WebIconDialog import WebIconDialog
        dlg = WebIconDialog(self.__iconsDB)
        if dlg.exec_() == QDialog.Accepted:
            changed = False
            urls = dlg.getUrls()
            for url in list(self.__iconsDB.keys())[:]:
                if url not in urls:
                    del self.__iconsDB[url]
                    changed = True
            if changed:
                self.changed.emit()


_WebIconProvider = None


def instance():
    """
    Global function to get a reference to the web icon provider and create it,
    if it hasn't been yet.
    
    @return reference to the web icon provider object
    @rtype WebIconProvider
    """
    global _WebIconProvider
    
    if _WebIconProvider is None:
        _WebIconProvider = WebIconProvider()
    
    return _WebIconProvider
