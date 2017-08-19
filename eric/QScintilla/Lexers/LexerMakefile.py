# -*- coding: utf-8 -*-

# Copyright (c) 2005 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a Makefile lexer with some additional methods.
"""

from __future__ import unicode_literals

from PyQt5.Qsci import QsciLexerMakefile

from .Lexer import Lexer


class LexerMakefile(Lexer, QsciLexerMakefile):
    """
    Subclass to implement some additional lexer dependant methods.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent parent widget of this lexer
        """
        QsciLexerMakefile.__init__(self, parent)
        Lexer.__init__(self)
        
        self.commentString = "#"
        self._alwaysKeepTabs = True
    
    def isCommentStyle(self, style):
        """
        Public method to check, if a style is a comment style.
        
        @param style style to check (integer)
        @return flag indicating a comment style (boolean)
        """
        return style in [QsciLexerMakefile.Comment]
    
    def isStringStyle(self, style):
        """
        Public method to check, if a style is a string style.
        
        @param style style to check (integer)
        @return flag indicating a string style (boolean)
        """
        return False
    
    def defaultKeywords(self, kwSet):
        """
        Public method to get the default keywords.
        
        @param kwSet number of the keyword set (integer)
        @return string giving the keywords (string) or None
        """
        return QsciLexerMakefile.keywords(self, kwSet)
