# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing an object to load web site icons.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtNetwork import QNetworkRequest

import WebBrowser.WebBrowserWindow


class WebIconLoader(QObject):
    """
    Class implementing a loader for web site icons.
    
    @signal iconLoaded(icon) emitted when the con has been loaded
    """
    iconLoaded = pyqtSignal(QIcon)
    
    def __init__(self, url, parent=None):
        """
        Constructor
        
        @param url URL to fetch the icon from
        @type QUrl
        @param parent reference to the parent object
        @type QObject
        """
        super(WebIconLoader, self).__init__(parent)
        
        networkManager = \
            WebBrowser.WebBrowserWindow.WebBrowserWindow.networkManager()
        self.__reply = networkManager.get(QNetworkRequest(url))
        self.__reply.finished.connect(self.__finished)
    
    @pyqtSlot()
    def __finished(self):
        """
        Private slot handling the downloaded icon.
        """
        # ignore any errors and emit an empty icon in this case
        data = self.__reply.readAll()
        icon = QIcon(QPixmap.fromImage(QImage.fromData(data)))
        self.iconLoaded.emit(icon)
        
        self.__reply.deleteLater()
        self.__reply = None
