# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing an object to create a thumbnail image of a web site.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, QObject, QSize, Qt, QUrl, QTimer
from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWebEngineWidgets import QWebEngineView


class PageThumbnailer(QObject):
    """
    Class implementing a thumbnail creator for web sites.
    
    @signal thumbnailCreated(QPixmap) emitted after the thumbnail has been
        created
    """
    thumbnailCreated = pyqtSignal(QPixmap)
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(PageThumbnailer, self).__init__(parent)
        
        self.__size = QSize(231, 130)
        self.__loadTitle = False
        self.__title = ""
        self.__url = QUrl()
        
        self.__view = QWebEngineView()
        self.__view.setAttribute(Qt.WA_DontShowOnScreen)
        self.__view.resize(1920, 1080)
        self.__view.show()
    
    def setSize(self, size):
        """
        Public method to set the size of the image.
        
        @param size size of the image (QSize)
        """
        if size.isValid():
            self.__size = QSize(size)
    
    def setUrl(self, url):
        """
        Public method to set the URL of the site to be thumbnailed.
        
        @param url URL of the web site (QUrl)
        """
        if url.isValid():
            self.__url = QUrl(url)
    
    def url(self):
        """
        Public method to get the URL of the thumbnail.
        
        @return URL of the thumbnail (QUrl)
        """
        return QUrl(self.__url)
    
    def loadTitle(self):
        """
        Public method to check, if the title is loaded from the web site.
        
        @return flag indicating, that the title is loaded (boolean)
        """
        return self.__loadTitle
    
    def setLoadTitle(self, load):
        """
        Public method to set a flag indicating to load the title from
        the web site.
        
        @param load flag indicating to load the title (boolean)
        """
        self.__loadTitle = load
    
    def title(self):
        """
        Public method to get the title of the thumbnail.
        
        @return title of the thumbnail (string)
        """
        if self.__title:
            title = self.__title
        else:
            title = self.__url.host()
        if not title:
            title = self.__url.toString()
        return title
    
    def start(self):
        """
        Public method to start the thumbnailing action.
        """
        self.__view.loadFinished.connect(self.__createThumbnail)
        self.__view.load(self.__url)
    
    def __createThumbnail(self, status):
        """
        Private slot creating the thumbnail of the web site.
        
        @param status flag indicating a successful load of the web site
            (boolean)
        """
        if not status:
            self.thumbnailCreated.emit(QPixmap())
            return
        
        QTimer.singleShot(1000, self.__grabThumbnail)
    
    def __grabThumbnail(self):
        """
        Private slot to grab the thumbnail image from the view.
        """
        self.__title = self.__view.title()
        
        image = QImage(self.__view.size(), QImage.Format_ARGB32)
        painter = QPainter(image)
        self.__view.render(painter)
        painter.end()
        
        scaledImage = image.scaled(self.__size,
                                   Qt.KeepAspectRatioByExpanding,
                                   Qt.SmoothTransformation)
        
        self.thumbnailCreated.emit(QPixmap.fromImage(scaledImage))
