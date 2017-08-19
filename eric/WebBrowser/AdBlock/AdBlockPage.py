# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a class to apply AdBlock rules to a web page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QObject

from ..Tools import Scripts
from ..WebBrowserPage import WebBrowserPage


class AdBlockPage(QObject):
    """
    Class to apply AdBlock rules to a web page.
    """
    def hideBlockedPageEntries(self, page):
        """
        Public method to apply AdBlock rules to a web page.
        
        @param page reference to the web page (HelpWebPage)
        """
        if page is None:
            return
        
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        manager = WebBrowserWindow.adBlockManager()
        if not manager.isEnabled():
            return
        
        # apply global element hiding rules
        elementHiding = manager.elementHidingRules(page.url())
        if elementHiding:
            script = Scripts.setCss(elementHiding)
            page.runJavaScript(script, WebBrowserPage.SafeJsWorld)
        
        # apply domain specific element hiding rules
        elementHiding = manager.elementHidingRulesForDomain(page.url())
        if elementHiding:
            script = Scripts.setCss(elementHiding)
            page.runJavaScript(script, WebBrowserPage.SafeJsWorld)
