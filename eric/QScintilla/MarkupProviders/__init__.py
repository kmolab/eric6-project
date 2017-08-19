# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Package providing various markup providers.
"""

from __future__ import unicode_literals

import os

import Preferences


def getMarkupProvider(editor):
    """
    Public method to get a markup provider for the given editor.
    
    @param editor reference to the editor to get the markup provider for
    @type Editor
    @return markup provider
    @rtype MarkupBase
    """
    if editor is not None:
        fn = editor.getFileName()
        
        if fn:
            extension = os.path.normcase(os.path.splitext(fn)[1][1:])
        else:
            extension = ""
        if extension in \
            Preferences.getEditor("PreviewHtmlFileNameExtensions") or \
                editor.getLanguage() == "HTML":
            from .HtmlProvider import HtmlProvider
            return HtmlProvider()
        elif extension in \
            Preferences.getEditor("PreviewMarkdownFileNameExtensions") or \
                editor.getLanguage().lower() == "markdown":
            from .MarkdownProvider import MarkdownProvider
            return MarkdownProvider()
        elif extension in \
            Preferences.getEditor("PreviewRestFileNameExtensions") or \
                editor.getLanguage().lower() == "restructuredtext":
            from .RestructuredTextProvider import RestructuredTextProvider
            return RestructuredTextProvider()
    
    # no supported markup provider identified
    from .MarkupBase import MarkupBase
    return MarkupBase()
