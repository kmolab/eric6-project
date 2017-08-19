# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Python side of the eric home page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, QObject


class StartPageJsObject(QObject):
    """
    Class implementing the Python side of the eric home page.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object
        @type ExternalJsObject
        """
        super(StartPageJsObject, self).__init__(parent)
        
        self.__external = parent
    
    @pyqtSlot(result=str)
    def providerString(self):
        """
        Public method to get a string for the search provider.
        
        @return string for the search provider (string)
        """
        return (self.tr("Search results provided by {0}")
                .format(self.__external.page().view().mainWindow()
                .openSearchManager().currentEngineName()))
    
    @pyqtSlot(str, result=str)
    def searchUrl(self, searchStr):
        """
        Public method to get the search URL for the given search term.
        
        @param searchStr search term (string)
        @return search URL (string)
        """
        return bytes(
            self.__external.page().view().mainWindow().openSearchManager()
            .currentEngine().searchUrl(searchStr).toEncoded()).decode()
