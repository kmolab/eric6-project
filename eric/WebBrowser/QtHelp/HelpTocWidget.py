# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a window for showing the QtHelp TOC.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QUrl
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMenu, QApplication


class HelpTocWidget(QWidget):
    """
    Class implementing a window for showing the QtHelp TOC.
    
    @signal escapePressed() emitted when the ESC key was pressed
    @signal openUrl(QUrl, str) emitted to open an entry in the current tab
    @signal newTab(QUrl, str) emitted to open an entry in a new tab
    @signal newBackgroundTab(QUrl, str) emitted to open an entry in a
        new background tab
    @signal newWindow(QUrl, str) emitted to open an entry in a new window
    """
    escapePressed = pyqtSignal()
    openUrl = pyqtSignal(QUrl)
    newTab = pyqtSignal(QUrl)
    newBackgroundTab = pyqtSignal(QUrl)
    newWindow = pyqtSignal(QUrl)
    
    def __init__(self, engine, parent=None):
        """
        Constructor
        
        @param engine reference to the help engine (QHelpEngine)
        @param parent reference to the parent widget (QWidget)
        """
        super(HelpTocWidget, self).__init__(parent)
        
        self.__engine = engine
        self.__expandDepth = -2
        
        self.__tocWidget = self.__engine.contentWidget()
        self.__tocWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__tocWidget.setSortingEnabled(True)
        
        self.__layout = QVBoxLayout(self)
        self.__layout.addWidget(self.__tocWidget)
        
        self.__tocWidget.customContextMenuRequested.connect(
            self.__showContextMenu)
        self.__tocWidget.linkActivated.connect(self.__linkActivated)
        
        model = self.__tocWidget.model()
        model.contentsCreated.connect(self.__contentsCreated)
    
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
                self.newTab.emit(url)
            else:
                if modifiers & (Qt.ControlModifier | Qt.ShiftModifier) == \
                        (Qt.ControlModifier | Qt.ShiftModifier):
                    self.newBackgroundTab.emit(url)
                elif modifiers & Qt.ControlModifier:
                    self.newTab.emit(url)
                elif modifiers & Qt.ShiftModifier:
                    self.newWindow.emit(url)
                else:
                    self.openUrl.emit(url)
    
    def __contentsCreated(self):
        """
        Private slot to be run after the contents was generated.
        """
        self.__tocWidget.sortByColumn(0, Qt.AscendingOrder)
        self.__expandTOC()
    
    def __expandTOC(self):
        """
        Private slot to expand the table of contents.
        """
        if self.__expandDepth > -2:
            self.expandToDepth(self.__expandDepth)
            self.__expandDepth = -2
    
    def expandToDepth(self, depth):
        """
        Public slot to expand the table of contents to a specific depth.
        
        @param depth depth to expand to (integer)
        """
        self.__expandDepth = depth
        if depth == -1:
            self.__tocWidget.expandAll()
        else:
            self.__tocWidget.expandToDepth(depth)
    
    def focusInEvent(self, evt):
        """
        Protected method handling focus in events.
        
        @param evt reference to the focus event object (QFocusEvent)
        """
        if evt.reason() != Qt.MouseFocusReason:
            self.__tocWidget.setFocus()
    
    def keyPressEvent(self, evt):
        """
        Protected method handling key press events.
        
        @param evt reference to the key press event (QKeyEvent)
        """
        if evt.key() == Qt.Key_Escape:
            self.escapePressed.emit()
    
    def syncToContent(self, url):
        """
        Public method to sync the TOC to the displayed page.
        
        @param url URL of the displayed page (QUrl)
        @return flag indicating a successful synchronization (boolean)
        """
        idx = self.__tocWidget.indexOf(url)
        if not idx.isValid():
            return False
        self.__tocWidget.setCurrentIndex(idx)
        return True
    
    def __showContextMenu(self, pos):
        """
        Private slot showing the context menu.
        
        @param pos position to show the menu at (QPoint)
        """
        if not self.__tocWidget.indexAt(pos).isValid():
            return
        
        model = self.__tocWidget.model()
        itm = model.contentItemAt(self.__tocWidget.currentIndex())
        link = itm.url()
        if link.isEmpty() or not link.isValid():
            return
        
        menu = QMenu()
        curTab = menu.addAction(self.tr("Open Link"))
        newTab = menu.addAction(self.tr("Open Link in New Tab"))
        newBackgroundTab = menu.addAction(
            self.tr("Open Link in Background Tab"))
        newWindow = menu.addAction(self.tr("Open Link in New Window"))
        menu.move(self.__tocWidget.mapToGlobal(pos))
        
        act = menu.exec_()
        if act == curTab:
            self.openUrl.emit(link)
        elif act == newTab:
            self.newTab.emit(link)
        elif act == newBackgroundTab:
            self.newBackgroundTab.emit(link)
        elif act == newWindow:
            self.newWindow.emit(link)
