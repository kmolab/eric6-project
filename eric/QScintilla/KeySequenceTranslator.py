# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing functions to map QScintilla keyboard commands to
QKeySequence standard keys.
"""

from __future__ import unicode_literals

from PyQt5.QtGui import QKeySequence
from PyQt5.Qsci import QsciScintilla

from Globals import qVersionTuple

__all__ = ["s2qTranslate"]

Scintilla2QKeySequence = {
    QsciScintilla.SCI_CHARLEFT: QKeySequence.MoveToPreviousChar,
    QsciScintilla.SCI_CHARRIGHT: QKeySequence.MoveToNextChar,
    QsciScintilla.SCI_LINEUP: QKeySequence.MoveToPreviousLine,
    QsciScintilla.SCI_LINEDOWN: QKeySequence.MoveToNextLine,
    QsciScintilla.SCI_WORDPARTLEFT: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDPARTRIGHT: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDLEFT: QKeySequence.MoveToNextWord,
    QsciScintilla.SCI_WORDRIGHT: QKeySequence.MoveToPreviousWord,
    QsciScintilla.SCI_VCHOME: QKeySequence.MoveToStartOfLine,
    QsciScintilla.SCI_HOMEDISPLAY: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEEND: QKeySequence.MoveToEndOfLine,
    QsciScintilla.SCI_LINESCROLLDOWN: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINESCROLLUP: QKeySequence.UnknownKey,
    QsciScintilla.SCI_PARAUP: QKeySequence.MoveToStartOfBlock,
    QsciScintilla.SCI_PARADOWN: QKeySequence.MoveToEndOfBlock,
    QsciScintilla.SCI_PAGEUP: QKeySequence.MoveToPreviousPage,
    QsciScintilla.SCI_PAGEDOWN: QKeySequence.MoveToNextPage,
    QsciScintilla.SCI_DOCUMENTSTART: QKeySequence.MoveToStartOfDocument,
    QsciScintilla.SCI_DOCUMENTEND: QKeySequence.MoveToEndOfDocument,
    QsciScintilla.SCI_TAB: QKeySequence.UnknownKey,
    QsciScintilla.SCI_BACKTAB: QKeySequence.UnknownKey,
    QsciScintilla.SCI_CHARLEFTEXTEND: QKeySequence.SelectPreviousChar,
    QsciScintilla.SCI_CHARRIGHTEXTEND: QKeySequence.SelectNextChar,
    QsciScintilla.SCI_LINEUPEXTEND: QKeySequence.SelectPreviousLine,
    QsciScintilla.SCI_LINEDOWNEXTEND: QKeySequence.SelectNextLine,
    QsciScintilla.SCI_WORDPARTLEFTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDPARTRIGHTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDLEFTEXTEND: QKeySequence.SelectPreviousWord,
    QsciScintilla.SCI_WORDRIGHTEXTEND: QKeySequence.SelectNextWord,
    QsciScintilla.SCI_VCHOMEEXTEND: QKeySequence.SelectStartOfLine,
    QsciScintilla.SCI_LINEENDEXTEND: QKeySequence.SelectEndOfLine,
    QsciScintilla.SCI_PARAUPEXTEND: QKeySequence.SelectStartOfBlock,
    QsciScintilla.SCI_PARADOWNEXTEND: QKeySequence.SelectEndOfBlock,
    QsciScintilla.SCI_PAGEUPEXTEND: QKeySequence.SelectPreviousPage,
    QsciScintilla.SCI_PAGEDOWNEXTEND: QKeySequence.SelectNextPage,
    QsciScintilla.SCI_DOCUMENTSTARTEXTEND: QKeySequence.SelectStartOfDocument,
    QsciScintilla.SCI_DOCUMENTENDEXTEND: QKeySequence.SelectEndOfDocument,
    QsciScintilla.SCI_DELETEBACK: QKeySequence.UnknownKey,
    QsciScintilla.SCI_DELETEBACKNOTLINE: QKeySequence.UnknownKey,
    QsciScintilla.SCI_CLEAR: QKeySequence.Delete,
    QsciScintilla.SCI_DELWORDLEFT: QKeySequence.DeleteStartOfWord,
    QsciScintilla.SCI_DELWORDRIGHT: QKeySequence.DeleteEndOfWord,
    QsciScintilla.SCI_DELLINELEFT: QKeySequence.UnknownKey,
    QsciScintilla.SCI_DELLINERIGHT: QKeySequence.DeleteEndOfLine,
    QsciScintilla.SCI_NEWLINE: QKeySequence.InsertLineSeparator,
    QsciScintilla.SCI_LINEDELETE: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEDUPLICATE: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINETRANSPOSE: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINECUT: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINECOPY: QKeySequence.UnknownKey,
    QsciScintilla.SCI_EDITTOGGLEOVERTYPE: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEENDDISPLAY: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEENDDISPLAYEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_FORMFEED: QKeySequence.UnknownKey,
    QsciScintilla.SCI_CANCEL: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEDOWNRECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEUPRECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_CHARLEFTRECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_CHARRIGHTRECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_VCHOMERECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEENDRECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_PAGEUPRECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_PAGEDOWNRECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_SELECTIONDUPLICATE: QKeySequence.UnknownKey,
    QsciScintilla.SCI_SCROLLTOSTART: QKeySequence.UnknownKey,
    QsciScintilla.SCI_SCROLLTOEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_VERTICALCENTRECARET: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDRIGHTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDRIGHTENDEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDLEFTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_WORDLEFTENDEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_HOME: QKeySequence.UnknownKey,
    QsciScintilla.SCI_HOMEEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_HOMERECTEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_HOMEDISPLAYEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_HOMEWRAP: QKeySequence.UnknownKey,
    QsciScintilla.SCI_HOMEWRAPEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_VCHOMEWRAP: QKeySequence.UnknownKey,
    QsciScintilla.SCI_VCHOMEWRAPEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEENDWRAP: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LINEENDWRAPEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_STUTTEREDPAGEUP: QKeySequence.UnknownKey,
    QsciScintilla.SCI_STUTTEREDPAGEUPEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_STUTTEREDPAGEDOWN: QKeySequence.UnknownKey,
    QsciScintilla.SCI_STUTTEREDPAGEDOWNEXTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_DELWORDRIGHTEND: QKeySequence.UnknownKey,
    QsciScintilla.SCI_MOVESELECTEDLINESUP: QKeySequence.UnknownKey,
    QsciScintilla.SCI_MOVESELECTEDLINESDOWN: QKeySequence.UnknownKey,
    QsciScintilla.SCI_LOWERCASE: QKeySequence.UnknownKey,
    QsciScintilla.SCI_UPPERCASE: QKeySequence.UnknownKey,
}
if qVersionTuple() >= (5, 2, 0):
    Scintilla2QKeySequence[QsciScintilla.SCI_LINEDELETE] = \
        QKeySequence.DeleteCompleteLine,
if qVersionTuple() >= (5, 5, 0):
    Scintilla2QKeySequence[QsciScintilla.SCI_DELETEBACK] = \
        QKeySequence.Backspace


def s2qTranslate(scintillaCommand):
    """
    Function to translate a QScintilla command to a QKeySequence.
    
    @param scintillaCommand QScintilla command
    @type int
    @return Qt key sequence
    @rtype QKeySequence.StandardKey
    """
    assert scintillaCommand in Scintilla2QKeySequence
    return Scintilla2QKeySequence[scintillaCommand]
