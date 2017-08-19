# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the JavaScript external object being the endpoint of
a web channel.
"""

#
# This code was ported from QupZilla and modified.
# Copyright (C) David Rosca <nowrep@gmail.com>
#

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtProperty, QObject

from WebBrowser.WebBrowserWindow import WebBrowserWindow

from .StartPageJsObject import StartPageJsObject
from .PasswordManagerJsObject import PasswordManagerJsObject


class ExternalJsObject(QObject):
    """
    Class implementing the endpoint of our web channel.
    """
    def __init__(self, page):
        """
        Constructor
        
        @param page reference to the web page object
        @type WebBrowserPage
        """
        super(ExternalJsObject, self).__init__(page)
        
        self.__page = page
        
        self.__startPage = None
        self.__passwordManager = None
    
    def page(self):
        """
        Public method returning a reference to the web page object.
        
        @return reference to the web page object
        @rtype WebBrowserPage
        """
        return self.__page
    
    @pyqtProperty(QObject, constant=True)
    def passwordManager(self):
        """
        Public method to get a reference to the password manager JavaScript
        object.
        
        @return reference to the password manager JavaScript object
        @rtype StartPageJsObject
        """
        if self.__passwordManager is None:
            self.__passwordManager = PasswordManagerJsObject(self)
        
        return self.__passwordManager
    
    @pyqtProperty(QObject, constant=True)
    def speedDial(self):
        """
        Public method returning a reference to a speed dial object.
        
        @return reference to a speed dial object
        @rtype SpeedDial
        """
        if self.__page.url().toString() != "eric:speeddial":
            return None
        
        return WebBrowserWindow.speedDial()
    
    @pyqtProperty(QObject, constant=True)
    def startPage(self):
        """
        Public method to get a reference to the start page JavaScript object.
        
        @return reference to the start page JavaScript object
        @rtype StartPageJsObject
        """
        if self.__startPage is None:
            self.__startPage = StartPageJsObject(self)
        
        return self.__startPage
