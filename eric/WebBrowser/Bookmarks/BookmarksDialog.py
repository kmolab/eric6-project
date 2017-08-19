# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to manage bookmarks.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, Qt, QUrl, QModelIndex
from PyQt5.QtGui import QFontMetrics, QCursor
from PyQt5.QtWidgets import QDialog, QMenu, QApplication

from E5Gui.E5TreeSortFilterProxyModel import E5TreeSortFilterProxyModel

from .Ui_BookmarksDialog import Ui_BookmarksDialog


class BookmarksDialog(QDialog, Ui_BookmarksDialog):
    """
    Class implementing a dialog to manage bookmarks.
    
    @signal openUrl(QUrl, str) emitted to open a URL in the current tab
    @signal newTab(QUrl, str) emitted to open a URL in a new tab
    @signal newBackgroundTab(QUrl, str) emitted to open a URL in a new
        background tab
    @signal newWindow(QUrl, str) emitted to open a URL in a new window
    """
    openUrl = pyqtSignal(QUrl, str)
    newTab = pyqtSignal(QUrl, str)
    newBackgroundTab = pyqtSignal(QUrl, str)
    newWindow = pyqtSignal(QUrl, str)
    
    def __init__(self, parent=None, manager=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget
        @param manager reference to the bookmarks manager object
            (BookmarksManager)
        """
        super(BookmarksDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        
        self.__bookmarksManager = manager
        if self.__bookmarksManager is None:
            import WebBrowser.WebBrowserWindow
            self.__bookmarksManager = WebBrowser.WebBrowserWindow\
                .WebBrowserWindow.bookmarksManager()
        
        self.__bookmarksModel = self.__bookmarksManager.bookmarksModel()
        self.__proxyModel = E5TreeSortFilterProxyModel(self)
        self.__proxyModel.setFilterKeyColumn(-1)
        self.__proxyModel.setSourceModel(self.__bookmarksModel)
        
        self.searchEdit.textChanged.connect(
            self.__proxyModel.setFilterFixedString)
        
        self.bookmarksTree.setModel(self.__proxyModel)
        self.bookmarksTree.setExpanded(self.__proxyModel.index(0, 0), True)
        fm = QFontMetrics(self.font())
        header = fm.width("m") * 40
        self.bookmarksTree.header().resizeSection(0, header)
        self.bookmarksTree.header().setStretchLastSection(True)
        self.bookmarksTree.setContextMenuPolicy(Qt.CustomContextMenu)
        
        self.bookmarksTree.activated.connect(self.__activated)
        self.bookmarksTree.customContextMenuRequested.connect(
            self.__customContextMenuRequested)
        
        self.removeButton.clicked.connect(
            self.bookmarksTree.removeSelected)
        self.addFolderButton.clicked.connect(self.__newFolder)
        
        self.__expandNodes(self.__bookmarksManager.bookmarks())
    
    def closeEvent(self, evt):
        """
        Protected method to handle the closing of the dialog.
        
        @param evt reference to the event object (QCloseEvent) (ignored)
        """
        self.__shutdown()
    
    def reject(self):
        """
        Public method called when the dialog is rejected.
        """
        self.__shutdown()
        super(BookmarksDialog, self).reject()
    
    def __shutdown(self):
        """
        Private method to perform shutdown actions for the dialog.
        """
        if self.__saveExpandedNodes(self.bookmarksTree.rootIndex()):
            self.__bookmarksManager.changeExpanded()
    
    def __saveExpandedNodes(self, parent):
        """
        Private method to save the child nodes of an expanded node.
        
        @param parent index of the parent node (QModelIndex)
        @return flag indicating a change (boolean)
        """
        changed = False
        for row in range(self.__proxyModel.rowCount(parent)):
            child = self.__proxyModel.index(row, 0, parent)
            sourceIndex = self.__proxyModel.mapToSource(child)
            childNode = self.__bookmarksModel.node(sourceIndex)
            wasExpanded = childNode.expanded
            if self.bookmarksTree.isExpanded(child):
                childNode.expanded = True
                changed |= self.__saveExpandedNodes(child)
            else:
                childNode.expanded = False
            changed |= (wasExpanded != childNode.expanded)
        
        return changed
    
    def __expandNodes(self, node):
        """
        Private method to expand all child nodes of a node.
        
        @param node reference to the bookmark node to expand (BookmarkNode)
        """
        for childNode in node.children():
            if childNode.expanded:
                idx = self.__bookmarksModel.nodeIndex(childNode)
                idx = self.__proxyModel.mapFromSource(idx)
                self.bookmarksTree.setExpanded(idx, True)
                self.__expandNodes(childNode)
    
    def __customContextMenuRequested(self, pos):
        """
        Private slot to handle the context menu request for the bookmarks tree.
        
        @param pos position the context menu was requested (QPoint)
        """
        from .BookmarkNode import BookmarkNode
        
        menu = QMenu()
        idx = self.bookmarksTree.indexAt(pos)
        idx = idx.sibling(idx.row(), 0)
        sourceIndex = self.__proxyModel.mapToSource(idx)
        node = self.__bookmarksModel.node(sourceIndex)
        if idx.isValid() and node.type() != BookmarkNode.Folder:
            menu.addAction(
                self.tr("&Open"), self.__openBookmarkInCurrentTab)
            menu.addAction(
                self.tr("Open in New &Tab"), self.__openBookmarkInNewTab)
            menu.addAction(
                self.tr("Open in New &Background Tab"),
                self.__openBookmarkInNewBackgroundTab)
            menu.addAction(
                self.tr("Open in New &Window"), self.__openBookmarkInNewWindow)
            menu.addAction(
                self.tr("Open in New Pri&vate Window"),
                self.__openBookmarkInPrivateWindow)
            menu.addSeparator()
        act = menu.addAction(self.tr("Edit &Name"), self.__editName)
        act.setEnabled(idx.flags() & Qt.ItemIsEditable)
        if idx.isValid() and node.type() != BookmarkNode.Folder:
            menu.addAction(self.tr("Edit &Address"), self.__editAddress)
        menu.addSeparator()
        act = menu.addAction(
            self.tr("&Delete"), self.bookmarksTree.removeSelected)
        act.setEnabled(idx.flags() & Qt.ItemIsDragEnabled)
        menu.addSeparator()
        act = menu.addAction(self.tr("&Properties..."), self.__edit)
        act.setEnabled(idx.flags() & Qt.ItemIsEditable)
        menu.exec_(QCursor.pos())
    
    def __activated(self, idx):
        """
        Private slot to handle the activation of an entry.
        
        @param idx reference to the entry index (QModelIndex)
        """
        if QApplication.keyboardModifiers() & Qt.ControlModifier:
            self.__openBookmarkInNewTab()
        elif QApplication.keyboardModifiers() & Qt.ShiftModifier:
            self.__openBookmarkInNewWindow()
        else:
            self.__openBookmarkInCurrentTab()
        
    def __openBookmarkInCurrentTab(self):
        """
        Private slot to open a bookmark in the current browser tab.
        """
        self.__openBookmark()
    
    def __openBookmarkInNewTab(self):
        """
        Private slot to open a bookmark in a new browser tab.
        """
        self.__openBookmark(newTab=True)
    
    def __openBookmarkInNewBackgroundTab(self):
        """
        Private slot to open a bookmark in a new browser tab.
        """
        self.__openBookmark(newTab=True, background=True)
    
    def __openBookmarkInNewWindow(self):
        """
        Private slot to open a bookmark in a new browser window.
        """
        self.__openBookmark(newWindow=True)
    
    def __openBookmarkInPrivateWindow(self):
        """
        Private slot to open a bookmark in a new private browser window.
        """
        self.__openBookmark(newWindow=True, privateWindow=True)
    
    def __openBookmark(self, newTab=False, newWindow=False,
                       privateWindow=False, background=False):
        """
        Private method to open a bookmark.
        
        @param newTab flag indicating to open the bookmark in a new tab
        @type bool
        @param newWindow flag indicating to open the bookmark in a new window
        @type bool
        @param privateWindow flag indicating to open the bookmark in a new
            private window
        @type bool
        @param background flag indicating to open the bookmark in a new
            background tab
        @type bool
        """
        from .BookmarkNode import BookmarkNode
        from .BookmarksModel import BookmarksModel
        
        idx = self.bookmarksTree.currentIndex()
        sourceIndex = self.__proxyModel.mapToSource(idx)
        node = self.__bookmarksModel.node(sourceIndex)
        if not idx.parent().isValid() or \
           node is None or \
           node.type() == BookmarkNode.Folder:
            return
        
        if newWindow:
            from WebBrowser.WebBrowserWindow import WebBrowserWindow
            url = idx.sibling(idx.row(), 1).data(BookmarksModel.UrlRole)
            if privateWindow:
                WebBrowserWindow.mainWindow().newPrivateWindow(url)
            else:
                WebBrowserWindow.mainWindow().newWindow(url)
        else:
            if newTab:
                if background:
                    self.newBackgroundTab.emit(
                        idx.sibling(idx.row(), 1).data(BookmarksModel.UrlRole),
                        idx.sibling(idx.row(), 0).data(Qt.DisplayRole))
                else:
                    self.newTab.emit(
                        idx.sibling(idx.row(), 1).data(BookmarksModel.UrlRole),
                        idx.sibling(idx.row(), 0).data(Qt.DisplayRole))
            else:
                self.openUrl.emit(
                    idx.sibling(idx.row(), 1).data(BookmarksModel.UrlRole),
                    idx.sibling(idx.row(), 0).data(Qt.DisplayRole))
        self.__bookmarksManager.incVisitCount(node)
    
    def __editName(self):
        """
        Private slot to edit the name part of a bookmark.
        """
        idx = self.bookmarksTree.currentIndex()
        idx = idx.sibling(idx.row(), 0)
        self.bookmarksTree.edit(idx)
    
    def __editAddress(self):
        """
        Private slot to edit the address part of a bookmark.
        """
        idx = self.bookmarksTree.currentIndex()
        idx = idx.sibling(idx.row(), 1)
        self.bookmarksTree.edit(idx)
    
    def __edit(self):
        """
        Private slot to edit a bookmarks properties.
        """
        from .BookmarkPropertiesDialog import BookmarkPropertiesDialog
        
        idx = self.bookmarksTree.currentIndex()
        sourceIndex = self.__proxyModel.mapToSource(idx)
        node = self.__bookmarksModel.node(sourceIndex)
        dlg = BookmarkPropertiesDialog(node)
        dlg.exec_()
    
    def __newFolder(self):
        """
        Private slot to add a new bookmarks folder.
        """
        from .BookmarkNode import BookmarkNode
        
        currentIndex = self.bookmarksTree.currentIndex()
        idx = QModelIndex(currentIndex)
        sourceIndex = self.__proxyModel.mapToSource(idx)
        sourceNode = self.__bookmarksModel.node(sourceIndex)
        row = -1    # append new folder as the last item per default
        
        if sourceNode is not None and \
           sourceNode.type() != BookmarkNode.Folder:
            # If the selected item is not a folder, add a new folder to the
            # parent folder, but directly below the selected item.
            idx = idx.parent()
            row = currentIndex.row() + 1
        
        if not idx.isValid():
            # Select bookmarks menu as default.
            idx = self.__proxyModel.index(1, 0)
        
        idx = self.__proxyModel.mapToSource(idx)
        parent = self.__bookmarksModel.node(idx)
        node = BookmarkNode(BookmarkNode.Folder)
        node.title = self.tr("New Folder")
        self.__bookmarksManager.addBookmark(parent, node, row)
