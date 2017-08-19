# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to manage history.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, Qt, QUrl
from PyQt5.QtGui import QFontMetrics, QCursor
from PyQt5.QtWidgets import QDialog, QMenu, QApplication

from E5Gui.E5TreeSortFilterProxyModel import E5TreeSortFilterProxyModel

from .HistoryModel import HistoryModel

from .Ui_HistoryDialog import Ui_HistoryDialog


class HistoryDialog(QDialog, Ui_HistoryDialog):
    """
    Class implementing a dialog to manage history.
    
    @signal openUrl(QUrl, str) emitted to open a URL in the current tab
    @signal newTab(QUrl, str) emitted to open a URL in a new tab
    @signal newBackgroundTab(QUrl, str) emitted to open a URL in a new
        background tab
    @signal newWindow(QUrl, str) emitted to open a URL in a new window
    @signal newPrivateWindow(QUrl, str) emitted to open a URL in a new
        private window
    """
    openUrl = pyqtSignal(QUrl, str)
    newTab = pyqtSignal(QUrl, str)
    newBackgroundTab = pyqtSignal(QUrl, str)
    newWindow = pyqtSignal(QUrl, str)
    newPrivateWindow = pyqtSignal(QUrl, str)
    
    def __init__(self, parent=None, manager=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget
        @param manager reference to the history manager object (HistoryManager)
        """
        super(HistoryDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        
        self.__historyManager = manager
        if self.__historyManager is None:
            import WebBrowser.WebBrowserWindow
            self.__historyManager = \
                WebBrowser.WebBrowserWindow.WebBrowserWindow.historyManager()
        
        self.__model = self.__historyManager.historyTreeModel()
        self.__proxyModel = E5TreeSortFilterProxyModel(self)
        self.__proxyModel.setSortRole(HistoryModel.DateTimeRole)
        self.__proxyModel.setFilterKeyColumn(-1)
        self.__proxyModel.setSourceModel(self.__model)
        self.historyTree.setModel(self.__proxyModel)
        self.historyTree.expandAll()
        fm = QFontMetrics(self.font())
        header = fm.width("m") * 40
        self.historyTree.header().resizeSection(0, header)
        self.historyTree.header().resizeSection(1, header)
        self.historyTree.header().setStretchLastSection(True)
        self.historyTree.setContextMenuPolicy(Qt.CustomContextMenu)
        
        self.historyTree.activated.connect(self.__activated)
        self.historyTree.customContextMenuRequested.connect(
            self.__customContextMenuRequested)
        
        self.searchEdit.textChanged.connect(
            self.__proxyModel.setFilterFixedString)
        self.removeButton.clicked.connect(self.historyTree.removeSelected)
        self.removeAllButton.clicked.connect(self.__historyManager.clear)
        
        self.__proxyModel.modelReset.connect(self.__modelReset)
    
    def __modelReset(self):
        """
        Private slot handling a reset of the tree view's model.
        """
        self.historyTree.expandAll()
    
    def __customContextMenuRequested(self, pos):
        """
        Private slot to handle the context menu request for the bookmarks tree.
        
        @param pos position the context menu was requested (QPoint)
        """
        menu = QMenu()
        idx = self.historyTree.indexAt(pos)
        idx = idx.sibling(idx.row(), 0)
        if idx.isValid() and \
            not self.historyTree.model().hasChildren(idx) and \
                len(self.historyTree.selectionModel().selectedRows()) == 1:
            menu.addAction(
                self.tr("&Open"),
                self.__openHistoryInCurrentTab)
            menu.addAction(
                self.tr("Open in New &Tab"),
                self.__openHistoryInNewTab)
            menu.addAction(
                self.tr("Open in New &Background Tab"),
                self.__openHistoryInNewBackgroundTab)
            menu.addAction(
                self.tr("Open in New &Window"),
                self.__openHistoryInNewWindow)
            menu.addAction(
                self.tr("Open in New Pri&vate Window"),
                self.__openHistoryInPrivateWindow)
            menu.addSeparator()
            menu.addAction(self.tr("&Copy"), self.__copyHistory)
        menu.addAction(self.tr("&Remove"), self.historyTree.removeSelected)
        menu.exec_(QCursor.pos())
    
    def __activated(self, idx):
        """
        Private slot to handle the activation of an entry.
        
        @param idx reference to the entry index (QModelIndex)
        """
        if QApplication.keyboardModifiers() & Qt.ControlModifier:
            self.__openHistoryInNewTab()
        elif QApplication.keyboardModifiers() & Qt.ShiftModifier:
            self.__openHistoryInNewWindow()
        else:
            self.__openHistoryInCurrentTab()
        
    def __openHistoryInCurrentTab(self):
        """
        Private slot to open a history entry in the current browser tab.
        """
        self.__openHistory()
    
    def __openHistoryInNewTab(self):
        """
        Private slot to open a history entry in a new browser tab.
        """
        self.__openHistory(newTab=True)
    
    def __openHistoryInNewBackgroundTab(self):
        """
        Private slot to open a history entry in a new background tab.
        """
        self.__openHistory(newTab=True, background=True)
    
    def __openHistoryInNewWindow(self):
        """
        Private slot to open a history entry in a new browser window.
        """
        self.__openHistory(newWindow=True)
    
    def __openHistoryInPrivateWindow(self):
        """
        Private slot to open a history entry in a new private browser window.
        """
        self.__openHistory(newWindow=True, privateWindow=True)
    
    def __openHistory(self, newTab=False, background=False,
                      newWindow=False, privateWindow=False):
        """
        Private method to open a history entry.
        
        @param newTab flag indicating to open the feed message in a new tab
        @type bool
        @param background flag indicating to open the bookmark in a new
            background tab
        @type bool
        @param newWindow flag indicating to open the bookmark in a new window
        @type bool
        @param privateWindow flag indicating to open the bookmark in a new
            private window
        @type bool
            (boolean)
        """
        idx = self.historyTree.currentIndex()
        if newTab:
            if background:
                self.newBackgroundTab.emit(
                    idx.data(HistoryModel.UrlRole),
                    idx.data(HistoryModel.TitleRole))
            else:
                self.newTab.emit(
                    idx.data(HistoryModel.UrlRole),
                    idx.data(HistoryModel.TitleRole))
        elif newWindow:
            if privateWindow:
                self.newPrivateWindow.emit(
                    idx.data(HistoryModel.UrlRole),
                    idx.data(HistoryModel.TitleRole))
            else:
                self.newWindow.emit(
                    idx.data(HistoryModel.UrlRole),
                    idx.data(HistoryModel.TitleRole))
        else:
            self.openUrl.emit(
                idx.data(HistoryModel.UrlRole),
                idx.data(HistoryModel.TitleRole))
    
    def __copyHistory(self):
        """
        Private slot to copy a history entry's URL to the clipboard.
        """
        idx = self.historyTree.currentIndex()
        if not idx.parent().isValid():
            return
        
        url = idx.data(HistoryModel.UrlStringRole)
        
        clipboard = QApplication.clipboard()
        clipboard.setText(url)
