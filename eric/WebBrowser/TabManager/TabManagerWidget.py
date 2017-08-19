# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a window for managing the web browser tabs.
"""

#
# Modeled after the tab manager plug-in of Qupzilla
# Copyright (C) 2013  S. Razi Alavizadeh <s.r.alavizadeh@gmail.com>
#

from __future__ import unicode_literals

import os
import collections

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QPoint, QTimer, QRect
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTreeWidget, \
    QTreeWidgetItem, QMenu, QStyle, QAction

import E5Network
from E5Network import E5TldExtractor

from E5Gui.E5Application import e5App
from E5Gui.E5ClickableLabel import E5ClickableLabel

import Utilities
import UI.PixmapCache
import Preferences


class TabManagerWidget(QWidget):
    """
    Class implementing a window for managing the web browser tabs.
    
    @signal groupTypeChanged(int) emitted when the 'Group By' value was changed
    """
    GroupByWindow = 0
    GroupByDomain = 1
    GroupByHost = 2
    
    WebBrowserRole = Qt.UserRole + 1
    WebWindowRole = Qt.UserRole + 2
    
    groupTypeChanged = pyqtSignal(int)
    
    _tldExtractor = None
    
    def __init__(self, mainWindow, parent=None, defaultWidget=False):
        """
        Constructor
        
        @param mainWindow reference to the main window
        @type WebBrowserWindow
        @param parent reference to the parent widget
        @type QWidget
        @param defaultWidget flag indicating the default widget
        @type bool
        """
        super(TabManagerWidget, self).__init__(parent)
        self.setWindowFlags(Qt.Window)
        
        self.__layout = QVBoxLayout(self)
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__tree = QTreeWidget(self)
        self.__tree.setHeaderHidden(True)
        self.__tree.setExpandsOnDoubleClick(False)
        self.__tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.__layout.addWidget(self.__tree)
        
        self.setWindowTitle(self.tr("Tab Manager"))
        
        self.__mw = mainWindow
        self.__page = None
        
        self.__isRefreshing = False
        self.__refreshBlocked = False
        self.__waitForRefresh = False
        self.__isDefaultWidget = defaultWidget
        self.__groupType = Preferences.getWebBrowser("TabManagerGroupByType")
        
        if TabManagerWidget._tldExtractor is None:
            TabManagerWidget._tldExtractor = E5TldExtractor.instance()
            TabManagerWidget._tldExtractor.setDataSearchPaths([
                os.path.join(Utilities.getConfigDir(), "web_browser")])
        
        self.__tree.itemDoubleClicked.connect(self.__itemDoubleClicked)
        self.__tree.customContextMenuRequested.connect(
            self.__customContextMenuRequested)
        
        self.resize(400, 600)
    
    def closeSelectedBrowsers(self, browsersDict):
        """
        Public method to close the selected browsers.
        
        @param browsersDict dictionary containing the browsers per window
        @type dict with WebBrowserWindow as key and list of WebBrowserView
            as value
        """
        if not browsersDict:
            return
        
        for mainWindow in browsersDict:
            tabWidget = mainWindow.tabWidget()
            for browser in browsersDict[mainWindow]:
                tabWidget.closeBrowserAt(tabWidget.indexOf(browser))
    
    def bookmarkSelectedBrowsers(self, browsersDict):
        """
        Public method to bookmark the selected browsers.
        
        @param browsersDict dictionary containing the browsers per window
        @type dict with WebBrowserWindow as key and list of WebBrowserView
            as value
        """
        if not browsersDict:
            return
        
        from ..Bookmarks.BookmarkNode import BookmarkNode
        from ..Bookmarks.AddBookmarkDialog import AddBookmarkDialog
        
        dlg = AddBookmarkDialog()
        dlg.setFolder(True)
        dlg.setTitle(self.tr("Saved Tabs"))
        dlg.exec_()
        
        folder = dlg.addedNode()
        if folder is None:
            return
        
        for mainWin in browsersDict:
            for browser in browsersDict[mainWin]:
                if not browser.url().isEmpty() and \
                        not browser.url().scheme() == "eric":
                    bookmark = BookmarkNode(BookmarkNode.Bookmark)
                    bookmark.url = bytes(browser.url().toEncoded()).decode()
                    bookmark.title = browser.title()
                    
                    self.__mw.bookmarksManager().addBookmark(folder, bookmark)
    
    def __setGroupType(self, groupType):
        """
        Private method to set the 'Group By' type.
        
        @param groupType 'Group By' type to be set
        @type int (0 - 2)
        """
        self.__groupType = groupType
        Preferences.setWebBrowser("TabManagerGroupByType", groupType)
    
    def domainFromUrl(self, url, useHostName=False):
        """
        Public method to extract the domain from an URL.
        
        @param url URL to extract the domain from
        @type QUrl
        @param useHostName flag indicating to use the host name
        @type bool
        @return domain name
        @rtype str
        """
        appendStr = ":"
        urlString = url.toString()
        
        if url.scheme() == "file":
            return self.tr("Local File System:")
        elif url.scheme() == "eric" or not urlString:
            return self.tr("eric Web Browser:")
        elif url.scheme() == "ftp":
            appendStr = self.tr(" [FTP]:")
        
        host = url.host()
        if not host:
            return urlString + appendStr
        
        if useHostName or E5Network.isValidAddress(host):
            if host.lower().startswith("www."):
                host = host[4:]
        else:
            registeredDomain = \
                TabManagerWidget._tldExtractor.registrableDomain(host)
            if registeredDomain:
                host = registeredDomain
        
        return host + appendStr
    
    def delayedRefreshTree(self, page=None):
        """
        Public slot to do a delyed refresh of the tree.
        
        @param page reference to the web page
        @type WebBrowserPage
        """
        if self.__refreshBlocked or self.__waitForRefresh:
            return
        
        if self.__isRefreshing and not page:
            return
        
        self.__page = page
        self.__waitForRefresh = True
        QTimer.singleShot(50, self.__refreshTree)
    
    def changeGroupType(self, act):
        """
        Public slot to change the 'Group By' type.
        
        @param act reference to the action that was triggered
        @type QAction
        """
        if act is None:
            return
        
        groupType = act.data()
        if self.__groupType != groupType:
            self.__setGroupType(groupType)
            self.delayedRefreshTree()
            self.groupTypeChanged.emit(self.__groupType)
    
    def __createEmptyItem(self, parent=None, addToTree=True):
        """
        Private method to create an empty tree item.
        
        @param parent reference to the parent item
        @type QTreeWidgetItem or QTreeWidget
        @param addToTree flag indicating to add the item to the tree
        @type bool
        @return created item
        @rtype QTreeWidgetItem
        """
        if addToTree:
            if parent:
                parentItem = parent
            else:
                parentItem = self.__tree.invisibleRootItem()
        else:
            parentItem = None
        itm = QTreeWidgetItem(parentItem)
        flags = itm.flags()
        if parent:
            flags |= Qt.ItemIsUserCheckable
        else:
            flags |= Qt.ItemIsUserCheckable | Qt.ItemIsTristate
        itm.setFlags(itm.flags() | flags)
        itm.setCheckState(0, Qt.Unchecked)
        
        return itm
    
    def __groupByDomainName(self, useHostName=False):
        """
        Private method to group the tree items by domain name.
        
        @param useHostName flag indicating to use the host name
        @type bool
        """
        windows = self.__mw.mainWindows()
        
        tabsGroupedByDomain = {}
        
        for mainWin in windows:
            for browser in mainWin.tabWidget().browsers():
                if self.__page == browser.page():
                    self.__page = None
                    continue
                domain = self.domainFromUrl(browser.url(), useHostName)
                
                if domain not in tabsGroupedByDomain:
                    groupItem = self.__createEmptyItem(None, False)
                    groupItem.setText(0, domain)
                    groupItem.setToolTip(0, domain)
                    font = groupItem.font(0)
                    font.setBold(True)
                    groupItem.setFont(0, font)
                    tabsGroupedByDomain[domain] = groupItem
                groupItem = tabsGroupedByDomain[domain]
                
                tabItem = self.__createEmptyItem(groupItem)
                if browser == mainWin.tabWidget().currentBrowser():
                    font = tabItem.font(0)
                    font.setBold(True)
                    tabItem.setFont(0, font)
                if not browser.isLoading():
                    tabItem.setIcon(0, browser.icon())
                else:
                    tabItem.setIcon(0, UI.PixmapCache.getIcon("loading.png"))
                tabItem.setText(0, browser.title())
                tabItem.setToolTip(0, browser.title())
                
                tabItem.setData(0, TabManagerWidget.WebBrowserRole, browser)
                tabItem.setData(0, TabManagerWidget.WebWindowRole, mainWin)
                
                self.__makeWebBrowserViewConnections(browser)
        
        self.__tree.insertTopLevelItems(0, tabsGroupedByDomain.values())
    
    def __groupByWindow(self):
        """
        Private method to group the tree items by window.
        """
        windows = self.__mw.mainWindows()
        
        self.__isRefreshing = True
        
        winCount = 0
        for mainWin in windows:
            winCount += 1
            winItem = self.__createEmptyItem()
            winItem.setText(0, self.tr("Window {0}").format(winCount))
            winItem.setToolTip(0, self.tr("Double click to switch"))
            if mainWin == self.__mw:
                font = winItem.font(0)
                font.setBold(True)
                winItem.setFont(0, font)
            winItem.setData(0, TabManagerWidget.WebWindowRole, mainWin)
            
            for browser in mainWin.tabWidget().browsers():
                if self.__page == browser.page():
                    self.__page = None
                    continue
                
                tabItem = self.__createEmptyItem(winItem)
                if browser == mainWin.tabWidget().currentBrowser():
                    font = tabItem.font(0)
                    font.setBold(True)
                    tabItem.setFont(0, font)
                if not browser.isLoading():
                    tabItem.setIcon(0, browser.icon())
                else:
                    tabItem.setIcon(0, UI.PixmapCache.getIcon("loading.png"))
                tabItem.setText(0, browser.title())
                tabItem.setToolTip(0, browser.title())
                
                tabItem.setData(0, TabManagerWidget.WebBrowserRole, browser)
                tabItem.setData(0, TabManagerWidget.WebWindowRole, mainWin)
                
                self.__makeWebBrowserViewConnections(browser)
    
    def __makeWebBrowserViewConnections(self, view):
        """
        Private method to create the signal connections to the web view.
        
        @param view reference to the web view
        @type WebBrowserView
        """
        if view:
            view.page().loadFinished.connect(self.delayedRefreshTree)
            view.page().loadStarted.connect(self.delayedRefreshTree)
            view.titleChanged.connect(self.delayedRefreshTree)
            view.faviconChanged.connect(self.delayedRefreshTree)
    
    @pyqtSlot()
    def __refreshTree(self):
        """
        Private slot to referesh the tree.
        """
        if self.__refreshBlocked:
            return
        
        if self.__isRefreshing and not self.__page:
            return
        
        # store selected items
        selectedBrowsers = []
        for index in range(self.__tree.topLevelItemCount()):
            winItem = self.__tree.topLevelItem(index)
            if winItem.checkState(0) == Qt.Unchecked:
                continue
            
            for row in range(winItem.childCount()):
                tabItem = winItem.child(row)
                if tabItem.checkState(0) == Qt.Unchecked:
                    continue
                selectedBrowsers.append(
                    tabItem.data(0, TabManagerWidget.WebBrowserRole))
        
        self.__tree.clear()
        
        if self.__groupType == TabManagerWidget.GroupByHost:
            self.__groupByDomainName(True)
        elif self.__groupType == TabManagerWidget.GroupByDomain:
            self.__groupByDomainName()
        else:
            # default is group by window
            self.__setGroupType(TabManagerWidget.GroupByWindow)
            self.__groupByWindow()
        
        # restore selected items
        for index in range(self.__tree.topLevelItemCount()):
            winItem = self.__tree.topLevelItem(index)
            
            for row in range(winItem.childCount()):
                tabItem = winItem.child(row)
                if tabItem.data(0, TabManagerWidget.WebBrowserRole) in \
                        selectedBrowsers:
                    tabItem.setCheckState(0, Qt.Checked)
        
        self.__tree.expandAll()
        self.__isRefreshing = False
        self.__waitForRefresh = False
    
    @pyqtSlot()
    def __processActions(self):
        """
        Private slot to process the actions.
        """
        if self.sender() is None:
            return
        
        self.__refreshBlocked = True
        
        selectedBrowsers = collections.defaultdict(list)
        
        command = self.sender().objectName()
        
        for index in range(self.__tree.topLevelItemCount()):
            winItem = self.__tree.topLevelItem(index)
            if winItem.checkState(0) == Qt.Unchecked:
                continue
            
            for row in range(winItem.childCount()):
                tabItem = winItem.child(row)
                if tabItem.checkState(0) == Qt.Unchecked:
                    continue
                
                mainWin = tabItem.data(0, TabManagerWidget.WebWindowRole)
                browser = tabItem.data(0, TabManagerWidget.WebBrowserRole)
                
                selectedBrowsers[mainWin].append(browser)
            
            winItem.setCheckState(0, Qt.Unchecked)
        
        if selectedBrowsers:
            if command == "closeSelection":
                self.closeSelectedBrowsers(selectedBrowsers)
            elif command == "bookmarkSelection":
                self.bookmarkSelectedBrowsers(selectedBrowsers)
        
        self.__refreshBlocked = False
        self.delayedRefreshTree()
    
    @pyqtSlot(QTreeWidgetItem, int)
    def __itemDoubleClicked(self, itm, column):
        """
        Private slot to handle double clicking a tree item.
        
        @param itm reference to the item having been double clicked
        @type QTreeWidgetItem
        @param column column of the double click
        @type int
        """
        if not itm:
            return
        
        mainWin = itm.data(0, TabManagerWidget.WebWindowRole)
        browser = itm.data(0, TabManagerWidget.WebBrowserRole)
        
        if not mainWin:
            return
        
        if mainWin.isMinimized():
            mainWin.showNormal()
        else:
            mainWin.show()
        mainWin.activateWindow()
        mainWin.raise_()
        mainWin.setFocus()
        
        tabWidget = mainWin.tabWidget()
        if browser and browser != tabWidget.currentWidget():
            tabWidget.setCurrentWidget(browser)
            browser.setFocus()
    
    @pyqtSlot()
    def __isBrowserSelected(self):
        """
        Private slot to check, if any browser entry is selected.
        
        @return flag indicating the existence of a selected entry
        @rtype bool
        """
        selected = False
        for topRow in range(self.__tree.topLevelItemCount()):
            topItm = self.__tree.topLevelItem(topRow)
            if topItm.checkState(0) != Qt.Unchecked:
                selected = True
                break
        
        return selected
    
    @pyqtSlot(QPoint)
    def __customContextMenuRequested(self, pos):
        """
        Private slot to show the context menu.
        
        @param pos position the menu should be shown at
        @type QPoint
        """
        menu = QMenu()
        groupTypeSubMenu = QMenu(self.tr("Group by"))
        act = groupTypeSubMenu.addAction(self.tr("&Window"))
        act.setData(TabManagerWidget.GroupByWindow)
        act.setCheckable(True)
        act.setChecked(self.__groupType == TabManagerWidget.GroupByWindow)
        
        act = groupTypeSubMenu.addAction(self.tr("&Domain"))
        act.setData(TabManagerWidget.GroupByDomain)
        act.setCheckable(True)
        act.setChecked(self.__groupType == TabManagerWidget.GroupByDomain)
        
        act = groupTypeSubMenu.addAction(self.tr("&Host"))
        act.setData(TabManagerWidget.GroupByHost)
        act.setCheckable(True)
        act.setChecked(self.__groupType == TabManagerWidget.GroupByHost)
        groupTypeSubMenu.triggered.connect(self.changeGroupType)
        
        menu.addMenu(groupTypeSubMenu)
        
        menu.addSeparator()
        
        if self.__isBrowserSelected():
            menu.addAction(
                UI.PixmapCache.getIcon("bookmark22.png"),
                self.tr("&Bookmark checked tabs"),
                self.__processActions).setObjectName("bookmarkSelection")
            menu.addAction(
                UI.PixmapCache.getIcon("tabClose.png"),
                self.tr("&Close checked tabs"),
                self.__processActions).setObjectName("closeSelection")
        
        menu.exec_(self.__tree.viewport().mapToGlobal(pos))
    
    def mainWindowCreated(self, mainWin, refresh=True):
        """
        Public method to act on the creation of a new web browser window.
        
        @param mainWin reference to the web browser window
        @type WebBrowserWindow
        @param refresh flag indicating to refresh the widget
        @type bool
        """
        mainWin.webBrowserWindowClosed.connect(self.delayedRefreshTree)
        mainWin.webBrowserWindowOpened.connect(self.mainWindowCreated)
        mainWin.webBrowserOpened.connect(self.delayedRefreshTree)
        mainWin.webBrowserClosed.connect(self.delayedRefreshTree)
        mainWin.tabWidget().currentUrlChanged.connect(self.delayedRefreshTree)
        mainWin.tabWidget().currentChanged.connect(self.delayedRefreshTree)
    
    def createStatusBarIcon(self):
        """
        Public method to create a status bar icon.
        
        @return generated icon
        @rtype E5ClickableLabel
        """
        icon = E5ClickableLabel()
        icon.setPixmap(
            UI.PixmapCache.getPixmap("tabManager.png").scaled(16, 16))
        icon.setToolTip(self.tr("Show Tab Manager"))
        icon.clicked.connect(self.raiseTabManager)
        
        return icon
    
    def raiseTabManager(self):
        """
        Public slot to show the tab manager.
        """
        window = None
        icon = self.sender()
        if icon:
            if isinstance(icon, E5ClickableLabel):
                window = icon.window()
            elif isinstance(icon, QAction):
                window = icon.parentWidget()
        
        if window is not None:
            titleBarHeight = self.style().pixelMetric(QStyle.PM_TitleBarHeight)
            
            y = max(0, window.frameGeometry().top() + titleBarHeight + 1)
            
            desktop = e5App().desktop()
            desktopGeometry = desktop.availableGeometry(self)
            windowFrameGeometry = window.frameGeometry()
            if (desktopGeometry.width() - windowFrameGeometry.right() - 1 >
                    self.frameGeometry().width()):
                x = windowFrameGeometry.right() + 1
            else:
                x = windowFrameGeometry.x() - 1 \
                    - self.frameGeometry().width()
            
            newGeo = QRect(x, y, self.width(), window.height())
            self.setGeometry(newGeo)
        
        self.activateWindow()
        self.showNormal()
        self.raise_()
