# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a Markdown lexer with some additional methods.
"""

from __future__ import unicode_literals

from PyQt5.Qsci import QsciLexerMarkdown

from .Lexer import Lexer


class LexerMarkdown(Lexer, QsciLexerMarkdown):
    """
    Subclass to implement some additional lexer dependent methods.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent parent widget of this lexer
        """
        QsciLexerMarkdown.__init__(self, parent)
        Lexer.__init__(self)
    
    def defaultKeywords(self, kwSet):
        """
        Public method to get the default keywords.
        
        @param kwSet number of the keyword set (integer)
        @return string giving the keywords (string) or None
        """
        return QsciLexerMarkdown.keywords(self, kwSet)
