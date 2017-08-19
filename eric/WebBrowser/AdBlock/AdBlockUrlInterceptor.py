# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing an URL interceptor base class.
"""

from __future__ import unicode_literals

from ..Network.UrlInterceptor import UrlInterceptor


class AdBlockUrlInterceptor(UrlInterceptor):
    """
    Class implementing an URL interceptor for AdBlock.
    """
    def __init__(self, manager, parent=None):
        """
        Constructor
        
        @param manager reference to the AdBlock manager
        @type AdBlockManager
        @param parent referemce to the parent object
        @type QObject
        """
        super(AdBlockUrlInterceptor, self).__init__(parent)
        
        self.__manager = manager
    
    def interceptRequest(self, info):
        """
        Public method to intercept a request.
        
        @param info request info object
        @type QWebEngineUrlRequestInfo
        """
        if self.__manager.block(info):
            info.block(True)
