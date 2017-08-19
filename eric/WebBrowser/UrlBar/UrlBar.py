# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the URL bar widget.
"""

from __future__ import unicode_literals
try:
    str = unicode       # __IGNORE_EXCEPTION__
except NameError:
    pass

from PyQt5.QtCore import pyqtSlot, Qt, QPointF, QUrl, QDateTime, QTimer
from PyQt5.QtGui import QColor, QPalette, QLinearGradient, QIcon
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage

from E5Gui.E5LineEdit import E5LineEdit
from E5Gui.E5LineEditButton import E5LineEditButton

from WebBrowser.WebBrowserWindow import WebBrowserWindow

from .FavIconLabel import FavIconLabel
import UI.PixmapCache
import Preferences


class UrlBar(E5LineEdit):
    """
    Class implementing a line edit for entering URLs.
    """
    def __init__(self, mainWindow, parent=None):
        """
        Constructor
        
        @param mainWindow reference to the main window (HelpWindow)
        @param parent reference to the parent widget (HelpBrowser)
        """
        E5LineEdit.__init__(self, parent)
        self.setInactiveText(self.tr("Enter the URL here."))
        self.setWhatsThis(self.tr("Enter the URL here."))
        
        self.__mw = mainWindow
        self.__browser = None
        self.__privateMode = WebBrowserWindow.isPrivate()
        
        self.__bmActiveIcon = UI.PixmapCache.getIcon("bookmark16.png")
        self.__bmInactiveIcon = QIcon(
            self.__bmActiveIcon.pixmap(16, 16, QIcon.Disabled))
        
        self.__favicon = FavIconLabel(self)
        self.addWidget(self.__favicon, E5LineEdit.LeftSide)
        
        self.__rssButton = E5LineEditButton(self)
        self.__rssButton.setIcon(UI.PixmapCache.getIcon("rss16.png"))
        self.addWidget(self.__rssButton, E5LineEdit.RightSide)
        self.__rssButton.setVisible(False)
        
        self.__bookmarkButton = E5LineEditButton(self)
        self.addWidget(self.__bookmarkButton, E5LineEdit.RightSide)
        self.__bookmarkButton.setVisible(False)
        
        self.__clearButton = E5LineEditButton(self)
        self.__clearButton.setIcon(UI.PixmapCache.getIcon("clearLeft.png"))
        self.addWidget(self.__clearButton, E5LineEdit.RightSide)
        self.__clearButton.setVisible(False)
        
        self.__bookmarkButton.clicked.connect(self.__showBookmarkInfo)
        self.__rssButton.clicked.connect(self.__rssClicked)
        self.__clearButton.clicked.connect(self.clear)
        self.textChanged.connect(self.__textChanged)
        
        self.__mw.bookmarksManager().entryChanged.connect(
            self.__bookmarkChanged)
        self.__mw.bookmarksManager().entryAdded.connect(
            self.__bookmarkChanged)
        self.__mw.bookmarksManager().entryRemoved.connect(
            self.__bookmarkChanged)
        self.__mw.speedDial().pagesChanged.connect(
            self.__bookmarkChanged)
    
    def setBrowser(self, browser):
        """
        Public method to set the browser connection.
        
        @param browser reference to the browser widget (WebBrowserView)
        """
        self.__browser = browser
        self.__favicon.setBrowser(browser)
        
        self.__browser.urlChanged.connect(self.__browserUrlChanged)
        self.__browser.loadProgress.connect(self.update)
        self.__browser.loadFinished.connect(self.__loadFinished)
        self.__browser.loadStarted.connect(self.__loadStarted)
    
    def browser(self):
        """
        Public method to get the associated browser.
       
        @return reference to the associated browser (HelpBrowser)
        """
        return self.__browser
    
    def __browserUrlChanged(self, url):
        """
        Private slot to handle a URL change of the associated browser.
        
        @param url new URL of the browser (QUrl)
        """
        strUrl = url.toString()
        if strUrl in ["eric:speeddial", "eric:home",
                      "about:blank", "about:config"]:
            strUrl = ""
        
        if self.text() != strUrl:
            self.setText(strUrl)
        self.setCursorPosition(0)
    
    def __loadStarted(self):
        """
        Private slot to perform actions before the page is loaded.
        """
        self.__bookmarkButton.setVisible(False)
        self.__rssButton.setVisible(False)
    
    def __checkBookmark(self):
        """
        Private slot to check the current URL for the bookmarked state.
        """
        manager = self.__mw.bookmarksManager()
        if manager.bookmarkForUrl(self.__browser.url()) is not None:
            self.__bookmarkButton.setIcon(self.__bmActiveIcon)
            bookmarks = manager.bookmarksForUrl(self.__browser.url())
            from WebBrowser.Bookmarks.BookmarkNode import BookmarkNode
            for bookmark in bookmarks:
                manager.setTimestamp(bookmark, BookmarkNode.TsVisited,
                                     QDateTime.currentDateTime())
        elif self.__mw.speedDial()\
                .pageForUrl(self.__browser.url()).url != "":
            self.__bookmarkButton.setIcon(self.__bmActiveIcon)
        else:
            self.__bookmarkButton.setIcon(self.__bmInactiveIcon)
    
    def __loadFinished(self, ok):
        """
        Private slot to set some data after the page was loaded.
        
        @param ok flag indicating a successful load (boolean)
        """
        if self.__browser.url().scheme() in ["eric", "about"]:
            self.__bookmarkButton.setVisible(False)
        else:
            self.__checkBookmark()
            self.__bookmarkButton.setVisible(True)
        
        if ok:
            QTimer.singleShot(0, self.__setRssButton)
    
    def __textChanged(self, txt):
        """
        Private slot to handle changes of the text.
        
        @param txt current text (string)
        """
        self.__clearButton.setVisible(txt != "")
    
    def preferencesChanged(self):
        """
        Public slot to handle a change of preferences.
        """
        self.update()
    
    def __showBookmarkInfo(self):
        """
        Private slot to show a dialog with some bookmark info.
        """
        from .BookmarkActionSelectionDialog import \
            BookmarkActionSelectionDialog
        url = self.__browser.url()
        dlg = BookmarkActionSelectionDialog(url)
        if dlg.exec_() == QDialog.Accepted:
            action = dlg.getAction()
            if action == BookmarkActionSelectionDialog.AddBookmark:
                self.__browser.addBookmark()
            elif action == BookmarkActionSelectionDialog.EditBookmark:
                bookmark = self.__mw.bookmarksManager()\
                    .bookmarkForUrl(url)
                from .BookmarkInfoDialog import BookmarkInfoDialog
                dlg = BookmarkInfoDialog(bookmark, self.__browser)
                dlg.exec_()
            elif action == BookmarkActionSelectionDialog.AddSpeeddial:
                self.__mw.speedDial().addPage(
                    url, self.__browser.title())
            elif action == BookmarkActionSelectionDialog.RemoveSpeeddial:
                self.__mw.speedDial().removePage(url)
    
    @pyqtSlot()
    def __bookmarkChanged(self):
        """
        Private slot to handle bookmark or speed dial changes.
        """
        self.__checkBookmark()
    
    def paintEvent(self, evt):
        """
        Protected method handling a paint event.
        
        @param evt reference to the paint event (QPaintEvent)
        """
        if self.__privateMode:
            backgroundColor = QColor(220, 220, 220)     # light gray
            foregroundColor = Qt.black
        else:
            backgroundColor = QApplication.palette().color(QPalette.Base)
            foregroundColor = QApplication.palette().color(QPalette.Text)
        
        if self.__browser is not None:
            p = self.palette()
            progress = self.__browser.progress()
            if progress == 0 or progress == 100:
                if self.__browser.url().scheme() == "https":
                    backgroundColor = Preferences.getWebBrowser(
                        "SaveUrlColor")
                p.setBrush(QPalette.Base, backgroundColor)
                p.setBrush(QPalette.Text, foregroundColor)
            else:
                if self.__browser.url().scheme() == "https":
                    backgroundColor = Preferences.getWebBrowser(
                        "SaveUrlColor")
                highlight = QApplication.palette().color(QPalette.Highlight)
                r = (highlight.red() + 2 * backgroundColor.red()) // 3
                g = (highlight.green() + 2 * backgroundColor.green()) // 3
                b = (highlight.blue() + 2 * backgroundColor.blue()) // 3
                
                loadingColor = QColor(r, g, b)
                if abs(loadingColor.lightness() -
                        backgroundColor.lightness()) < 20:
                    # special handling for special color schemes (e.g Gaia)
                    r = (2 * highlight.red() + backgroundColor.red()) // 3
                    g = (2 * highlight.green() + backgroundColor.green()) // 3
                    b = (2 * highlight.blue() + backgroundColor.blue()) // 3
                    loadingColor = QColor(r, g, b)
                
                gradient = QLinearGradient(
                    QPointF(0, 0), QPointF(self.width(), 0))
                gradient.setColorAt(0, loadingColor)
                gradient.setColorAt(progress / 100.0 - 0.000001, loadingColor)
                gradient.setColorAt(progress / 100.0, backgroundColor)
                p.setBrush(QPalette.Base, gradient)
            
            self.setPalette(p)
        
        E5LineEdit.paintEvent(self, evt)
    
    def focusOutEvent(self, evt):
        """
        Protected method to handle focus out event.
        
        @param evt reference to the focus event (QFocusEvent)
        """
        if self.text() == "" and self.__browser is not None:
            self.__browserUrlChanged(self.__browser.url())
        E5LineEdit.focusOutEvent(self, evt)
    
    def mousePressEvent(self, evt):
        """
        Protected method called by a mouse press event.
        
        @param evt reference to the mouse event (QMouseEvent)
        """
        if evt.button() == Qt.XButton1:
            self.__mw.currentBrowser().triggerPageAction(
                QWebEnginePage.Back)
        elif evt.button() == Qt.XButton2:
            self.__mw.currentBrowser().triggerPageAction(
                QWebEnginePage.Forward)
        else:
            super(UrlBar, self).mousePressEvent(evt)
    
    def mouseDoubleClickEvent(self, evt):
        """
        Protected method to handle mouse double click events.
        
        @param evt reference to the mouse event (QMouseEvent)
        """
        if evt.button() == Qt.LeftButton:
            self.selectAll()
        else:
            E5LineEdit.mouseDoubleClickEvent(self, evt)
    
    def keyPressEvent(self, evt):
        """
        Protected method to handle key presses.
        
        @param evt reference to the key press event (QKeyEvent)
        """
        if evt.key() == Qt.Key_Escape:
            if self.__browser is not None:
                self.setText(
                    str(self.__browser.url().toEncoded(), encoding="utf-8"))
                self.selectAll()
            completer = self.completer()
            if completer:
                completer.popup().hide()
            return
        
        currentText = self.text().strip()
        if evt.key() in [Qt.Key_Enter, Qt.Key_Return] and \
           not currentText.lower().startswith("http://"):
            append = ""
            if evt.modifiers() == Qt.KeyboardModifiers(Qt.ControlModifier):
                append = ".com"
            elif evt.modifiers() == Qt.KeyboardModifiers(
                    Qt.ControlModifier | Qt.ShiftModifier):
                append = ".org"
            elif evt.modifiers() == Qt.KeyboardModifiers(Qt.ShiftModifier):
                append = ".net"
            
            if append != "":
                url = QUrl("http://www." + currentText)
                host = url.host()
                if not host.lower().endswith(append):
                    host += append
                    url.setHost(host)
                    self.setText(url.toString())
        
        E5LineEdit.keyPressEvent(self, evt)
    
    def dragEnterEvent(self, evt):
        """
        Protected method to handle drag enter events.
        
        @param evt reference to the drag enter event (QDragEnterEvent)
        """
        mimeData = evt.mimeData()
        if mimeData.hasUrls() or mimeData.hasText():
            evt.acceptProposedAction()
        
        E5LineEdit.dragEnterEvent(self, evt)
    
    def dropEvent(self, evt):
        """
        Protected method to handle drop events.
        
        @param evt reference to the drop event (QDropEvent)
        """
        mimeData = evt.mimeData()
        
        url = QUrl()
        if mimeData.hasUrls():
            url = mimeData.urls()[0]
        elif mimeData.hasText():
            url = QUrl.fromEncoded(mimeData.text().encode("utf-8"),
                                   QUrl.TolerantMode)
        
        if url.isEmpty() or not url.isValid():
            E5LineEdit.dropEvent(self, evt)
            return
        
        self.setText(str(url.toEncoded(), encoding="utf-8"))
        self.selectAll()
        
        evt.acceptProposedAction()
    
    def __setRssButton(self):
        """
        Private slot to show the RSS button.
        """
        self.__rssButton.setVisible(self.__browser.checkRSS())
    
    def __rssClicked(self):
        """
        Private slot to handle clicking the RSS icon.
        """
        from WebBrowser.Feeds.FeedsDialog import FeedsDialog
        feeds = self.__browser.getRSS()
        dlg = FeedsDialog(feeds, self.__browser)
        dlg.exec_()
