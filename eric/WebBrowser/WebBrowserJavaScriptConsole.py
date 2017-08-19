# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a JavaScript console widget.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QTextEdit, QMenu
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class WebBrowserJavaScriptConsole(QTextEdit):
    """
    Class implementing a JavaScript console widget.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(WebBrowserJavaScriptConsole, self).__init__(parent)
        self.setAcceptRichText(False)
        self.setLineWrapMode(QTextEdit.NoWrap)
        self.setReadOnly(True)
        
        # create the context menu
        self.__menu = QMenu(self)
        self.__menu.addAction(self.tr('Clear'), self.clear)
        self.__menu.addAction(self.tr('Copy'), self.copy)
        self.__menu.addSeparator()
        self.__menu.addAction(self.tr('Select All'), self.selectAll)
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__handleShowContextMenu)
        
        self.__levelStrings = {
            QWebEnginePage.InfoMessageLevel: self.tr("Info"),
            QWebEnginePage.WarningMessageLevel: self.tr("Warning"),
            QWebEnginePage.ErrorMessageLevel: self.tr("Error"),
        }
    
    def __handleShowContextMenu(self, coord):
        """
        Private slot to show the context menu.
        
        @param coord the position of the mouse pointer (QPoint)
        """
        coord = self.mapToGlobal(coord)
        self.__menu.popup(coord)
    
    def __appendText(self, txt):
        """
        Private method to append text to the end.
        
        @param txt text to insert (string)
        """
        tc = self.textCursor()
        tc.movePosition(QTextCursor.End)
        self.setTextCursor(tc)
        self.insertPlainText(txt)
        self.ensureCursorVisible()
    
    def keyPressEvent(self, evt):
        """
        Protected method handling key press events.
        
        @param evt key press event (QKeyEvent)
        """
        if evt.modifiers() == Qt.ControlModifier:
            if evt.key() == Qt.Key_C:
                self.copy()
                evt.accept()
                return
            elif evt.key() == Qt.Key_A:
                self.selectAll()
                evt.accept()
                return
    
    def javaScriptConsoleMessage(self, level, message, lineNumber, sourceId):
        """
        Public method to show a console message.
        
        @param level severity
        @type QWebEnginePage.JavaScriptConsoleMessageLevel
        @param message message to be shown
        @type str
        @param lineNumber line number of an error
        @type int
        @param sourceId source URL causing the error
        @type str
        """
        txt = self.tr("[{0}] {1}").format(
            self.__levelStrings[level], message)
        self.__appendText(txt)
        
        if lineNumber:
            self.__appendText(self.tr(" at line {0}\n").format(lineNumber))
        else:
            self.__appendText("\n")
        
        if sourceId:
            self.__appendText(self.tr("URL: {0}\n").format(sourceId))
