# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the image search engine.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QObject, QUrl

import Preferences


class ImageSearchEngine(QObject):
    """
    Class implementing the image search engine.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object
        @type QObject
        """
        super(ImageSearchEngine, self).__init__(parent)
        
        self.__searchEngineNames = ["Google", "TinEye", "Yandex"]
    
    def searchEngine(self):
        """
        Public method to get the name of the current search engine.
        
        @return name of the current search engine
        @rtype str
        """
        return Preferences.getWebBrowser("ImageSearchEngine")
    
    def setSearchEngine(self, searchEngine):
        """
        Public method to set the current search engine.
        
        @param searchEngine name of the search engine
        @type str
        """
        Preferences.setWebBrowser("ImageSearchEngine", searchEngine)
    
    def searchEngineNames(self):
        """
        Public method to get the list of supported search engines.
        
        @return list of supported search engines
        @rtype list of str
        """
        return self.__searchEngineNames[:]
    
    def getSearchQuery(self, imageUrl, searchEngine=None):
        """
        Public method to get the image search query URL.
        
        @param imageUrl URL of the image to search for
        @type QUrl
        @param searchEngine name of the image search engine to be used
        @type str
        @return search query URL
        @rtype QUrl
        """
        if not searchEngine:
            searchEngine = self.searchEngine()
        
        searchEngine_l = searchEngine.lower()
        if searchEngine_l == "google":
            return QUrl("https://www.google.com/searchbyimage?"
                        "site=search&image_url={0}".format(
                            imageUrl.toString()))
        elif searchEngine_l == "yandex":
            return QUrl("https://yandex.com/images/search?"
                        "&img_url={0}&rpt=imageview".format(
                            imageUrl.toString()))
        elif searchEngine_l == "tineye":
            return QUrl("http://www.tineye.com/search?url={0}".format(
                imageUrl.toString()))
        else:
            return QUrl()
