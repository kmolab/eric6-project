# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a window for showing the QtHelp index.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QUrl
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QApplication, \
    QMenu


class HelpSearchWidget(QWidget):
    """
    Class implementing a window for showing the QtHelp index.
    
    @signal linkActivated(QUrl) emitted when a search result entry is activated
    @signal escapePressed() emitted when the ESC key was pressed
    """
    linkActivated = pyqtSignal(QUrl)
    escapePressed = pyqtSignal()
    
    def __init__(self, engine, mainWindow, parent=None):
        """
        Constructor
        
        @param engine reference to the help search engine (QHelpSearchEngine)
        @param mainWindow reference to the main window object (QMainWindow)
        @param parent reference to the parent widget (QWidget)
        """
        super(HelpSearchWidget, self).__init__(parent)
        
        self.__engine = engine
        self.__mw = mainWindow
        
        self.__layout = QVBoxLayout(self)
        
        self.__result = self.__engine.resultWidget()
        self.__query = self.__engine.queryWidget()
        
        self.__layout.addWidget(self.__query)
        self.__layout.addWidget(self.__result)
        
        self.setFocusProxy(self.__query)
        
        self.__query.search.connect(self.__search)
        self.__result.requestShowLink.connect(self.__linkActivated)
        
        self.__engine.searchingStarted.connect(self.__searchingStarted)
        self.__engine.searchingFinished.connect(self.__searchingFinished)
        
        self.__browser = self.__result.findChildren(QTextBrowser)[0]
    
    def __search(self):
        """
        Private slot to perform a search of the database.
        """
        query = self.__query.query()
        self.__engine.search(query)
    
    def __searchingStarted(self):
        """
        Private slot to handle the start of a search.
        """
        QApplication.setOverrideCursor(Qt.WaitCursor)
    
    def __searchingFinished(self, hits):
        """
        Private slot to handle the end of the search.
        
        @param hits number of hits (integer) (unused)
        """
        QApplication.restoreOverrideCursor()
    
    @pyqtSlot(QUrl)
    def __linkActivated(self, url):
        """
        Private slot handling the activation of an entry.
        
        @param url URL of the activated entry
        @type QUrl
        """
        if not url.isEmpty() and url.isValid():
            buttons = QApplication.mouseButtons()
            modifiers = QApplication.keyboardModifiers()
            
            if buttons & Qt.MidButton:
                self.__mw.newTab(url)
            else:
                if modifiers & Qt.ControlModifier:
                    self.__mw.newTab(url)
                else:
                    self.linkActivated.emit(url)
    
    def keyPressEvent(self, evt):
        """
        Protected method handling key press events.
        
        @param evt reference to the key press event (QKeyEvent)
        """
        if evt.key() == Qt.Key_Escape:
            self.escapePressed.emit()
        else:
            evt.ignore()
    
    def contextMenuEvent(self, evt):
        """
        Protected method handling context menu events.
        
        @param evt reference to the context menu event (QContextMenuEvent)
        """
        point = evt.globalPos()
        
        if self.__browser:
            point = self.__browser.mapFromGlobal(point)
            if not self.__browser.rect().contains(point, True):
                return
            link = QUrl(self.__browser.anchorAt(point))
        else:
            point = self.__result.mapFromGlobal(point)
            link = self.__result.linkAt(point)
        
        if link.isEmpty() or not link.isValid():
            return
        
        menu = QMenu()
        curTab = menu.addAction(self.tr("Open Link"))
        newTab = menu.addAction(self.tr("Open Link in New Tab"))
        menu.move(evt.globalPos())
        act = menu.exec_()
        if act == curTab:
            self.linkActivated.emit(link)
        elif act == newTab:
            self.__mw.newTab(link)
