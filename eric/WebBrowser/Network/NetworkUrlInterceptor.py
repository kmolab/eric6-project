# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a class to handle URL requests before they get processed
by QtWebEngine.
"""

from __future__ import unicode_literals

from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor

from ..WebBrowserPage import WebBrowserPage

import Preferences


class NetworkUrlInterceptor(QWebEngineUrlRequestInterceptor):
    """
    Class implementing an URL request handler.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object
        @type QObject
        """
        super(NetworkUrlInterceptor, self).__init__(parent)
        
        self.__interceptors = []
        
        self.__loadSettings()
    
    def interceptRequest(self, info):
        """
        Public method handling an URL request.
        
        @param info URL request information
        @type QWebEngineUrlRequestInfo
        """
        # Do Not Track feature
        if self.__doNotTrack:
            info.setHttpHeader(b"DNT", b"1")
            info.setHttpHeader(b"X-Do-Not-Track", b"1")
        
        # Send referer header?
        if not self.__sendReferer and info.requestUrl().host() not in \
                Preferences.getWebBrowser("SendRefererWhitelist"):
            info.setHttpHeader(b"Referer", b"")
        
        # User Agents header
        userAgent = WebBrowserPage.userAgentForUrl(info.requestUrl())
        info.setHttpHeader(b"User-Agent", userAgent.encode())
        
        for interceptor in self.__interceptors:
            interceptor.interceptRequest(info)
    
    def installUrlInterceptor(self, interceptor):
        """
        Public method to install an URL interceptor.
        
        @param interceptor URL interceptor to be installed
        @type UrlInterceptor
        """
        if interceptor not in self.__interceptors:
            self.__interceptors.append(interceptor)
    
    def removeUrlInterceptor(self, interceptor):
        """
        Public method to remove an URL interceptor.
        
        @param interceptor URL interceptor to be removed
        @type UrlInterceptor
        """
        if interceptor in self.__interceptors:
            self.__interceptors.remove(interceptor)
    
    def __loadSettings(self):
        """
        Private method to load the Network Manager settings.
        """
        self.__doNotTrack = Preferences.getWebBrowser("DoNotTrack")
        self.__sendReferer = Preferences.getWebBrowser("SendReferer")
    
    def preferencesChanged(self):
        """
        Public slot to handle a change of preferences.
        """
        self.__loadSettings()
