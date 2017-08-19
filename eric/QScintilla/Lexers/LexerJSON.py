# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a JSON lexer with some additional methods.
"""

from __future__ import unicode_literals

from PyQt5.Qsci import QsciLexerJSON

from .Lexer import Lexer
import Preferences


class LexerJSON(Lexer, QsciLexerJSON):
    """
    Subclass to implement some additional lexer dependent methods.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent parent widget of this lexer
        """
        QsciLexerJSON.__init__(self, parent)
        Lexer.__init__(self)
        
        self.commentString = "//"
        self.streamCommentString = {
            'start': '/* ',
            'end': ' */'
        }

    def initProperties(self):
        """
        Public slot to initialize the properties.
        """
        self.setHighlightComments(
            Preferences.getEditor("JSONHightlightComments"))
        self.setHighlightEscapeSequences(
            Preferences.getEditor("JSONHighlightEscapeSequences"))
        self.setFoldCompact(
            Preferences.getEditor("AllFoldCompact"))
    
    def isCommentStyle(self, style):
        """
        Public method to check, if a style is a comment style.
        
        @param style style to check (integer)
        @return flag indicating a comment style (boolean)
        """
        return style in [QsciLexerJSON.CommentLine,
                         QsciLexerJSON.CommentBlock]
    
    def isStringStyle(self, style):
        """
        Public method to check, if a style is a string style.
        
        @param style style to check (integer)
        @return flag indicating a string style (boolean)
        """
        return style in [QsciLexerJSON.String,
                         QsciLexerJSON.UnclosedString]
    
    def defaultKeywords(self, kwSet):
        """
        Public method to get the default keywords.
        
        @param kwSet number of the keyword set (integer)
        @return string giving the keywords (string) or None
        """
        return QsciLexerJSON.keywords(self, kwSet)
    
    def maximumKeywordSet(self):
        """
        Public method to get the maximum keyword set.
        
        @return maximum keyword set (integer)
        """
        return 2
