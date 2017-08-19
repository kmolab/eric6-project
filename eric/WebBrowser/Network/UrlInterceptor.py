# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing an URL interceptor base class.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QObject


class UrlInterceptor(QObject):
    """
    Class implementing an URL interceptor base class.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent referemce to the parent object
        @type QObject
        """
        super(UrlInterceptor, self).__init__(parent)
    
    def interceptRequest(self, info):
        """
        Public method to intercept a request.
        
        @param info request info object
        @type QWebEngineUrlRequestInfo
        """
        pass
