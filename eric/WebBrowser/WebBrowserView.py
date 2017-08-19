# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#


"""
Module implementing the web browser using QWebEngineView.
"""

from __future__ import unicode_literals
try:
    str = unicode           # __IGNORE_EXCEPTION__
except NameError:
    pass

import os

from PyQt5.QtCore import pyqtSignal, QUrl, QFileInfo, Qt, QTimer, QEvent, \
    QPoint, QPointF, QDateTime, QStandardPaths, QByteArray, QIODevice, \
    QDataStream
from PyQt5.QtGui import QDesktopServices, QClipboard, QIcon, \
    QContextMenuEvent, QPixmap
from PyQt5.QtWidgets import qApp, QStyle, QMenu, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, \
    QWebEngineDownloadItem

from E5Gui import E5MessageBox, E5FileDialog

from WebBrowser.WebBrowserWindow import WebBrowserWindow
from .WebBrowserPage import WebBrowserPage

from .Tools.WebIconLoader import WebIconLoader
from .Tools import Scripts

from . import WebInspector
from .Tools.WebBrowserTools import readAllFileContents, pixmapToDataUrl

import Preferences
import UI.PixmapCache
import Utilities
from Globals import qVersionTuple


class WebBrowserView(QWebEngineView):
    """
    Class implementing the web browser view widget.
    
    @signal sourceChanged(QUrl) emitted after the current URL has changed
    @signal forwardAvailable(bool) emitted after the current URL has changed
    @signal backwardAvailable(bool) emitted after the current URL has changed
    @signal highlighted(str) emitted, when the mouse hovers over a link
    @signal search(QUrl) emitted, when a search is requested
    @signal zoomValueChanged(int) emitted to signal a change of the zoom value
    @signal faviconChanged() emitted to signal a changed web site icon
    """
    sourceChanged = pyqtSignal(QUrl)
    forwardAvailable = pyqtSignal(bool)
    backwardAvailable = pyqtSignal(bool)
    highlighted = pyqtSignal(str)
    search = pyqtSignal(QUrl)
    zoomValueChanged = pyqtSignal(int)
    faviconChanged = pyqtSignal()
    
    ZoomLevels = [
        30, 40, 50, 67, 80, 90,
        100,
        110, 120, 133, 150, 170, 200, 220, 233, 250, 270, 285, 300,
    ]
    ZoomLevelDefault = 100
    
    def __init__(self, mainWindow, parent=None, name=""):
        """
        Constructor
        
        @param mainWindow reference to the main window (WebBrowserWindow)
        @param parent parent widget of this window (QWidget)
        @param name name of this window (string)
        """
        super(WebBrowserView, self).__init__(parent)
        self.setObjectName(name)
        
        self.__rwhvqt = None
        self.installEventFilter(self)
        
        self.__speedDial = WebBrowserWindow.speedDial()
        
        self.__page = WebBrowserPage(self)
        self.setPage(self.__page)
        
        self.__mw = mainWindow
        self.__isLoading = False
        self.__progress = 0
        self.__siteIconLoader = None
        self.__siteIcon = QIcon()
        self.__menu = QMenu(self)
        self.__clickedPos = QPoint()
        self.__firstLoad = False
        self.__preview = QPixmap()
        
        self.__currentZoom = 100
        self.__zoomLevels = WebBrowserView.ZoomLevels[:]
        
        self.iconUrlChanged.connect(self.__iconUrlChanged)
        self.urlChanged.connect(self.__urlChanged)
        self.page().linkHovered.connect(self.__linkHovered)
        
        self.loadStarted.connect(self.__loadStarted)
        self.loadProgress.connect(self.__loadProgress)
        self.loadFinished.connect(self.__loadFinished)
        self.renderProcessTerminated.connect(self.__renderProcessTerminated)
        
        self.__mw.openSearchManager().currentEngineChanged.connect(
            self.__currentEngineChanged)
        
        self.setAcceptDrops(True)
        
        self.__rss = []
        
        self.__clickedFrame = None
        
        self.__mw.personalInformationManager().connectPage(self.page())
        
        self.__inspector = None
        WebInspector.registerView(self)
        
        self.__restoreData = None
        
        if qVersionTuple() >= (5, 8, 0):
            if self.parentWidget() is not None:
                self.parentWidget().installEventFilter(self)
            
            lay = self.layout()
            lay.currentChanged.connect(
                lambda: QTimer.singleShot(0, self.__setRwhvqt))
            self.__setRwhvqt()
        
        self.grabGesture(Qt.PinchGesture)
    
    def __setRwhvqt(self):
        """
        Private slot to set widget that receives input events.
        """
        self.grabGesture(Qt.PinchGesture)
        self.__rwhvqt = self.focusProxy()
        if self.__rwhvqt:
            self.__rwhvqt.grabGesture(Qt.PinchGesture)
            self.__rwhvqt.installEventFilter(self)
        else:
            print("Focus proxy is null!")   # __IGNORE_WARNING_M801__
    
    def __currentEngineChanged(self):
        """
        Private slot to track a change of the current search engine.
        """
        if self.url().toString() == "eric:home":
            self.reload()
    
    def mainWindow(self):
        """
        Public method to get a reference to the main window.
        
        @return reference to the main window
        @rtype WebBrowserWindow
        """
        return self.__mw
    
    def load(self, url):
        """
        Public method to load a web site.
        
        @param url URL to be loaded
        @type QUrl
        """
        super(WebBrowserView, self).load(url)
        
        if not self.__firstLoad:
            self.__firstLoad = True
            WebInspector.pushView(self)
    
    def setSource(self, name, newTab=False):
        """
        Public method used to set the source to be displayed.
        
        @param name filename to be shown (QUrl)
        @param newTab flag indicating to open the URL in a new tab (bool)
        """
        if name is None or not name.isValid():
            return
        
        if newTab:
            # open in a new tab
            self.__mw.newTab(name)
            return
        
        if not name.scheme():
            if not os.path.exists(name.toString()):
                name.setScheme(Preferences.getWebBrowser("DefaultScheme"))
            else:
                if Utilities.isWindowsPlatform():
                    name.setUrl("file:///" + Utilities.fromNativeSeparators(
                        name.toString()))
                else:
                    name.setUrl("file://" + name.toString())
        
        if len(name.scheme()) == 1 or \
           name.scheme() == "file":
            # name is a local file
            if name.scheme() and len(name.scheme()) == 1:
                # it is a local path on win os
                name = QUrl.fromLocalFile(name.toString())
            
            if not QFileInfo(name.toLocalFile()).exists():
                E5MessageBox.critical(
                    self,
                    self.tr("eric6 Web Browser"),
                    self.tr(
                        """<p>The file <b>{0}</b> does not exist.</p>""")
                    .format(name.toLocalFile()))
                return

            if name.toLocalFile().lower().endswith((".pdf", ".chm")):
                started = QDesktopServices.openUrl(name)
                if not started:
                    E5MessageBox.critical(
                        self,
                        self.tr("eric6 Web Browser"),
                        self.tr(
                            """<p>Could not start a viewer"""
                            """ for file <b>{0}</b>.</p>""")
                        .format(name.path()))
                return
        elif name.scheme() in ["mailto"]:
            started = QDesktopServices.openUrl(name)
            if not started:
                E5MessageBox.critical(
                    self,
                    self.tr("eric6 Web Browser"),
                    self.tr(
                        """<p>Could not start an application"""
                        """ for URL <b>{0}</b>.</p>""")
                    .format(name.toString()))
            return
        else:
            if name.toString().lower().endswith((".pdf", ".chm")):
                started = QDesktopServices.openUrl(name)
                if not started:
                    E5MessageBox.critical(
                        self,
                        self.tr("eric6 Web Browser"),
                        self.tr(
                            """<p>Could not start a viewer"""
                            """ for file <b>{0}</b>.</p>""")
                        .format(name.path()))
                return
        
        self.load(name)

    def source(self):
        """
        Public method to return the URL of the loaded page.
        
        @return URL loaded in the help browser (QUrl)
        """
        return self.url()
    
    def documentTitle(self):
        """
        Public method to return the title of the loaded page.
        
        @return title (string)
        """
        return self.title()
    
    def backward(self):
        """
        Public slot to move backwards in history.
        """
        self.triggerPageAction(QWebEnginePage.Back)
        self.__urlChanged(self.history().currentItem().url())
    
    def forward(self):
        """
        Public slot to move forward in history.
        """
        self.triggerPageAction(QWebEnginePage.Forward)
        self.__urlChanged(self.history().currentItem().url())
    
    def home(self):
        """
        Public slot to move to the first page loaded.
        """
        homeUrl = QUrl(Preferences.getWebBrowser("HomePage"))
        self.setSource(homeUrl)
        self.__urlChanged(self.history().currentItem().url())
    
    def reload(self):
        """
        Public slot to reload the current page.
        """
        self.triggerPageAction(QWebEnginePage.Reload)
    
    def reloadBypassingCache(self):
        """
        Public slot to reload the current page bypassing the cache.
        """
        self.triggerPageAction(QWebEnginePage.ReloadAndBypassCache)
    
    def copy(self):
        """
        Public slot to copy the selected text.
        """
        self.triggerPageAction(QWebEnginePage.Copy)
    
    def cut(self):
        """
        Public slot to cut the selected text.
        """
        self.triggerPageAction(QWebEnginePage.Cut)
    
    def paste(self):
        """
        Public slot to paste text from the clipboard.
        """
        self.triggerPageAction(QWebEnginePage.Paste)
    
    def undo(self):
        """
        Public slot to undo the last edit action.
        """
        self.triggerPageAction(QWebEnginePage.Undo)
    
    def redo(self):
        """
        Public slot to redo the last edit action.
        """
        self.triggerPageAction(QWebEnginePage.Redo)
    
    def selectAll(self):
        """
        Public slot to select all text.
        """
        self.triggerPageAction(QWebEnginePage.SelectAll)
    
    def unselect(self):
        """
        Public slot to clear the current selection.
        """
        if qVersionTuple() >= (5, 7, 0):
            self.triggerPageAction(QWebEnginePage.Unselect)
        else:
            self.page().runJavaScript(
                "window.getSelection().empty()",
                WebBrowserPage.SafeJsWorld)
    
    def isForwardAvailable(self):
        """
        Public method to determine, if a forward move in history is possible.
        
        @return flag indicating move forward is possible (boolean)
        """
        return self.history().canGoForward()
    
    def isBackwardAvailable(self):
        """
        Public method to determine, if a backwards move in history is possible.
        
        @return flag indicating move backwards is possible (boolean)
        """
        return self.history().canGoBack()
    
    def __levelForZoom(self, zoom):
        """
        Private method determining the zoom level index given a zoom factor.
        
        @param zoom zoom factor (integer)
        @return index of zoom factor (integer)
        """
        try:
            index = self.__zoomLevels.index(zoom)
        except ValueError:
            for index in range(len(self.__zoomLevels)):
                if zoom <= self.__zoomLevels[index]:
                    break
        return index
    
    def setZoomValue(self, value, saveValue=True):
        """
        Public method to set the zoom value.
        
        @param value zoom value (integer)
        @keyparam saveValue flag indicating to save the zoom value with the
            zoom manager
        @type bool
        """
        if value != self.__currentZoom:
            self.setZoomFactor(value / 100.0)
            self.__currentZoom = value
            if saveValue and not self.__mw.isPrivate():
                from .ZoomManager import ZoomManager
                ZoomManager.instance().setZoomValue(self.url(), value)
            self.zoomValueChanged.emit(value)
    
    def zoomValue(self):
        """
        Public method to get the current zoom value.
        
        @return zoom value (integer)
        """
        val = self.zoomFactor() * 100
        return int(val)
    
    def zoomIn(self):
        """
        Public slot to zoom into the page.
        """
        index = self.__levelForZoom(self.__currentZoom)
        if index < len(self.__zoomLevels) - 1:
            self.setZoomValue(self.__zoomLevels[index + 1])
    
    def zoomOut(self):
        """
        Public slot to zoom out of the page.
        """
        index = self.__levelForZoom(self.__currentZoom)
        if index > 0:
            self.setZoomValue(self.__zoomLevels[index - 1])
    
    def zoomReset(self):
        """
        Public method to reset the zoom factor.
        """
        index = self.__levelForZoom(WebBrowserView.ZoomLevelDefault)
        self.setZoomValue(self.__zoomLevels[index])
    
    def mapToViewport(self, pos):
        """
        Public method to map a position to the viewport.
        
        @param pos position to be mapped
        @type QPoint
        @return viewport position
        @rtype QPoint
        """
        return self.page().mapToViewport(pos)
    
    def hasSelection(self):
        """
        Public method to determine, if there is some text selected.
        
        @return flag indicating text has been selected (boolean)
        """
        return self.selectedText() != ""
    
    def findNextPrev(self, txt, case, backwards, callback):
        """
        Public slot to find the next occurrence of a text.
        
        @param txt text to search for (string)
        @param case flag indicating a case sensitive search (boolean)
        @param backwards flag indicating a backwards search (boolean)
        @param callback reference to a function with a bool parameter
        @type function(bool) or None
        """
        findFlags = QWebEnginePage.FindFlags()
        if case:
            findFlags |= QWebEnginePage.FindCaseSensitively
        if backwards:
            findFlags |= QWebEnginePage.FindBackward
        
        if callback is None:
            self.findText(txt, findFlags)
        else:
            self.findText(txt, findFlags, callback)
    
    def contextMenuEvent(self, evt):
        """
        Protected method called to create a context menu.
        
        This method is overridden from QWebEngineView.
        
        @param evt reference to the context menu event object
            (QContextMenuEvent)
        """
        pos = evt.pos()
        reason = evt.reason()
        QTimer.singleShot(
            0,
            lambda: self._contextMenuEvent(QContextMenuEvent(reason, pos)))
        # needs to be done this way because contextMenuEvent is blocking
        # the main loop
    
    def _contextMenuEvent(self, evt):
        """
        Protected method called to create a context menu.
        
        This method is overridden from QWebEngineView.
        
        @param evt reference to the context menu event object
            (QContextMenuEvent)
        """
        self.__menu.clear()
        
        hitTest = self.page().hitTestContent(evt.pos())
        
        self.__createContextMenu(self.__menu, hitTest)
        
        if not hitTest.isContentEditable() and not hitTest.isContentSelected():
            self.__menu.addSeparator()
            self.__menu.addAction(self.__mw.adBlockIcon().menuAction())
        
        if Preferences.getWebBrowser("WebInspectorEnabled"):
            self.__menu.addSeparator()
            self.__menu.addAction(
                UI.PixmapCache.getIcon("webInspector.png"),
                self.tr("Inspect Element..."), self.__webInspector)
        
        if not self.__menu.isEmpty():
            pos = evt.globalPos()
            self.__menu.popup(QPoint(pos.x(), pos.y() + 1))
    
    def __createContextMenu(self, menu, hitTest):
        """
        Private method to populate the context menu.
        
        @param menu reference to the menu to be populated
        @type QMenu
        @param hitTest reference to the hit test object
        @type WebHitTestResult
        """
        spellCheckActionCount = 0
        if qVersionTuple() >= (5, 7, 0):
            contextMenuData = self.page().contextMenuData()
            hitTest.updateWithContextMenuData(contextMenuData)
            
            if qVersionTuple() >= (5, 8, 0) and \
               bool(contextMenuData.misspelledWord()):
                boldFont = menu.font()
                boldFont.setBold(True)
                
                for suggestion in contextMenuData.spellCheckerSuggestions():
                    act = menu.addAction(
                        suggestion,
                        self.__replaceMisspelledWord)
                    act.setFont(boldFont)
                
                if bool(menu.actions()):
                    menu.addAction(self.tr("No suggestions")).setEnabled(False)
                
                menu.addSeparator()
                spellCheckActionCount = len(menu.actions())
        
        if not hitTest.linkUrl().isEmpty() and \
                hitTest.linkUrl().scheme() != "javascript":
            self.__createLinkContextMenu(menu, hitTest)
        
        if not hitTest.imageUrl().isEmpty():
            self.__createImageContextMenu(menu, hitTest)
        
        if not hitTest.mediaUrl().isEmpty():
            self.__createMediaContextMenu(menu, hitTest)
        
        if hitTest.isContentEditable():
            # check, if only spell checker actions were added
            if len(menu.actions()) == spellCheckActionCount:
                menu.addAction(self.__mw.undoAct)
                menu.addAction(self.__mw.redoAct)
                menu.addSeparator()
                menu.addAction(self.__mw.cutAct)
                menu.addAction(self.__mw.copyAct)
                menu.addAction(self.__mw.pasteAct)
                menu.addSeparator()
                self.__mw.personalInformationManager().createSubMenu(
                    menu, self, hitTest)
            
            if hitTest.tagName() == "input":
                menu.addSeparator()
                act = menu.addAction("")
                act.setVisible(False)
                self.__checkForForm(act, hitTest.pos())
        
        if self.selectedText():
            self.__createSelectedTextContextMenu(menu, hitTest)
        
        if self.__menu.isEmpty():
            self.__createPageContextMenu(menu)
    
    def __createLinkContextMenu(self, menu, hitTest):
        """
        Private method to populate the context menu for URLs.
        
        @param menu reference to the menu to be populated
        @type QMenu
        @param hitTest reference to the hit test object
        @type WebHitTestResult
        """
        if not menu.isEmpty():
            menu.addSeparator()
        
        menu.addAction(
            UI.PixmapCache.getIcon("openNewTab.png"),
            self.tr("Open Link in New Tab\tCtrl+LMB"),
            self.__openLinkInNewTab).setData(hitTest.linkUrl())
        menu.addAction(
            UI.PixmapCache.getIcon("newWindow.png"),
            self.tr("Open Link in New Window"),
            self.__openLinkInNewWindow).setData(hitTest.linkUrl())
        menu.addAction(
            UI.PixmapCache.getIcon("privateMode.png"),
            self.tr("Open Link in New Private Window"),
            self.__openLinkInNewPrivateWindow).setData(hitTest.linkUrl())
        menu.addSeparator()
        menu.addAction(
            UI.PixmapCache.getIcon("download.png"),
            self.tr("Save Lin&k"), self.__downloadLink)
        menu.addAction(
            UI.PixmapCache.getIcon("bookmark22.png"),
            self.tr("Bookmark this Link"), self.__bookmarkLink)\
            .setData(hitTest.linkUrl())
        menu.addSeparator()
        menu.addAction(
            UI.PixmapCache.getIcon("editCopy.png"),
            self.tr("Copy Link to Clipboard"), self.__copyLink)\
            .setData(hitTest.linkUrl())
        menu.addAction(
            UI.PixmapCache.getIcon("mailSend.png"),
            self.tr("Send Link"),
            self.__sendLink).setData(hitTest.linkUrl())
        if Preferences.getWebBrowser("VirusTotalEnabled") and \
           Preferences.getWebBrowser("VirusTotalServiceKey") != "":
            menu.addAction(
                UI.PixmapCache.getIcon("virustotal.png"),
                self.tr("Scan Link with VirusTotal"),
                self.__virusTotal).setData(hitTest.linkUrl())
        
    def __createImageContextMenu(self, menu, hitTest):
        """
        Private method to populate the context menu for images.
        
        @param menu reference to the menu to be populated
        @type QMenu
        @param hitTest reference to the hit test object
        @type WebHitTestResult
        """
        if not menu.isEmpty():
            menu.addSeparator()
        
        menu.addAction(
            UI.PixmapCache.getIcon("openNewTab.png"),
            self.tr("Open Image in New Tab"),
            self.__openLinkInNewTab).setData(hitTest.imageUrl())
        menu.addSeparator()
        menu.addAction(
            UI.PixmapCache.getIcon("download.png"),
            self.tr("Save Image"), self.__downloadImage)
        menu.addAction(
            self.tr("Copy Image to Clipboard"), self.__copyImage)
        menu.addAction(
            UI.PixmapCache.getIcon("editCopy.png"),
            self.tr("Copy Image Location to Clipboard"),
            self.__copyLink).setData(hitTest.imageUrl())
        menu.addAction(
            UI.PixmapCache.getIcon("mailSend.png"),
            self.tr("Send Image Link"),
            self.__sendLink).setData(hitTest.imageUrl())
        
        if hitTest.imageUrl().scheme() in ["http", "https"]:
            menu.addSeparator()
            engine = WebBrowserWindow.imageSearchEngine()
            searchEngineName = engine.searchEngine()
            menu.addAction(
                UI.PixmapCache.getIcon("{0}.png".format(
                    searchEngineName.lower())),
                self.tr("Search image in {0}").format(searchEngineName),
                self.__searchImage).setData(
                    engine.getSearchQuery(hitTest.imageUrl()))
            self.__imageSearchMenu = menu.addMenu(
                self.tr("Search image with..."))
            for searchEngineName in engine.searchEngineNames():
                self.__imageSearchMenu.addAction(
                    UI.PixmapCache.getIcon("{0}.png".format(
                        searchEngineName.lower())),
                    self.tr("Search image in {0}").format(searchEngineName),
                    self.__searchImage).setData(
                        engine.getSearchQuery(
                            hitTest.imageUrl(), searchEngineName))
        
        menu.addSeparator()
        menu.addAction(
            UI.PixmapCache.getIcon("adBlockPlus.png"),
            self.tr("Block Image"), self.__blockImage)\
            .setData(hitTest.imageUrl().toString())
        if Preferences.getWebBrowser("VirusTotalEnabled") and \
           Preferences.getWebBrowser("VirusTotalServiceKey") != "":
            menu.addAction(
                UI.PixmapCache.getIcon("virustotal.png"),
                self.tr("Scan Image with VirusTotal"),
                self.__virusTotal).setData(hitTest.imageUrl())
    
    def __createMediaContextMenu(self, menu, hitTest):
        """
        Private method to populate the context menu for media elements.
        
        @param menu reference to the menu to be populated
        @type QMenu
        @param hitTest reference to the hit test object
        @type WebHitTestResult
        """
        if not menu.isEmpty():
            menu.addSeparator()
        
        if hitTest.mediaPaused():
            menu.addAction(
                UI.PixmapCache.getIcon("mediaPlaybackStart.png"),
                self.tr("Play"), self.__pauseMedia)
        else:
            menu.addAction(
                UI.PixmapCache.getIcon("mediaPlaybackPause.png"),
                self.tr("Pause"), self.__pauseMedia)
        if hitTest.mediaMuted():
            menu.addAction(
                UI.PixmapCache.getIcon("audioVolumeHigh.png"),
                self.tr("Unmute"), self.__muteMedia)
        else:
            menu.addAction(
                UI.PixmapCache.getIcon("audioVolumeMuted.png"),
                self.tr("Mute"), self.__muteMedia)
        menu.addSeparator()
        menu.addAction(
            UI.PixmapCache.getIcon("editCopy.png"),
            self.tr("Copy Media Address to Clipboard"),
            self.__copyLink).setData(hitTest.mediaUrl())
        menu.addAction(
            UI.PixmapCache.getIcon("mailSend.png"),
            self.tr("Send Media Address"), self.__sendLink)\
            .setData(hitTest.mediaUrl())
        menu.addAction(
            UI.PixmapCache.getIcon("download.png"),
            self.tr("Save Media"), self.__downloadMedia)
    
    def __createSelectedTextContextMenu(self, menu, hitTest):
        """
        Private method to populate the context menu for selected text.
        
        @param menu reference to the menu to be populated
        @type QMenu
        @param hitTest reference to the hit test object
        @type WebHitTestResult
        """
        if not menu.isEmpty():
            menu.addSeparator()
        
        menu.addAction(self.__mw.copyAct)
        menu.addSeparator()
        menu.addAction(
            UI.PixmapCache.getIcon("mailSend.png"),
            self.tr("Send Text"),
            self.__sendLink).setData(self.selectedText())
        
        engineName = self.__mw.openSearchManager().currentEngineName()
        if engineName:
            menu.addAction(self.tr("Search with '{0}'").format(engineName),
                           self.__searchDefaultRequested)
        
        from .OpenSearch.OpenSearchEngineAction import \
            OpenSearchEngineAction
        
        self.__searchMenu = menu.addMenu(self.tr("Search with..."))
        engineNames = self.__mw.openSearchManager().allEnginesNames()
        for engineName in engineNames:
            engine = self.__mw.openSearchManager().engine(engineName)
            act = OpenSearchEngineAction(engine, self.__searchMenu)
            act.setData(engineName)
            self.__searchMenu.addAction(act)
        self.__searchMenu.triggered.connect(self.__searchRequested)
        
        menu.addSeparator()
        
        from .WebBrowserLanguagesDialog import WebBrowserLanguagesDialog
        languages = Preferences.toList(
            Preferences.Prefs.settings.value(
                "WebBrowser/AcceptLanguages",
                WebBrowserLanguagesDialog.defaultAcceptLanguages()))
        if languages:
            language = languages[0]
            langCode = language.split("[")[1][:2]
            googleTranslatorUrl = QUrl(
                "http://translate.google.com/#auto|{0}|{1}".format(
                    langCode, self.selectedText()))
            menu.addAction(
                UI.PixmapCache.getIcon("translate.png"),
                self.tr("Google Translate"), self.__openLinkInNewTab)\
                .setData(googleTranslatorUrl)
            wiktionaryUrl = QUrl(
                "http://{0}.wiktionary.org/wiki/Special:Search?search={1}"
                .format(langCode, self.selectedText()))
            menu.addAction(
                UI.PixmapCache.getIcon("wikipedia.png"),
                self.tr("Dictionary"), self.__openLinkInNewTab)\
                .setData(wiktionaryUrl)
            menu.addSeparator()
        
        guessedUrl = QUrl.fromUserInput(self.selectedText().strip())
        if self.__isUrlValid(guessedUrl):
            menu.addAction(
                self.tr("Go to web address"),
                self.__openLinkInNewTab).setData(guessedUrl)
    
    def __createPageContextMenu(self, menu):
        """
        Private method to populate the basic context menu.
        
        @param menu reference to the menu to be populated
        @type QMenu
        """
        menu.addAction(self.__mw.newTabAct)
        menu.addAction(self.__mw.newAct)
        menu.addSeparator()
        if self.__mw.saveAsAct is not None:
            menu.addAction(self.__mw.saveAsAct)
            menu.addSeparator()
        
        if self.url().toString() == "eric:speeddial":
            # special menu for the spedd dial page
            menu.addAction(self.__mw.backAct)
            menu.addAction(self.__mw.forwardAct)
            menu.addSeparator()
            menu.addAction(
                UI.PixmapCache.getIcon("plus.png"),
                self.tr("Add New Page"), self.__addSpeedDial)
            menu.addAction(
                UI.PixmapCache.getIcon("preferences-general.png"),
                self.tr("Configure Speed Dial"), self.__configureSpeedDial)
            menu.addSeparator()
            menu.addAction(
                UI.PixmapCache.getIcon("reload.png"),
                self.tr("Reload All Dials"), self.__reloadAllSpeedDials)
            menu.addSeparator()
            menu.addAction(
                self.tr("Reset to Default Dials"), self.__resetSpeedDials)
            return
        
        menu.addAction(
            UI.PixmapCache.getIcon("bookmark22.png"),
            self.tr("Bookmark this Page"), self.addBookmark)
        menu.addAction(
            UI.PixmapCache.getIcon("editCopy.png"),
            self.tr("Copy Page Link"), self.__copyLink).setData(self.url())
        menu.addAction(
            UI.PixmapCache.getIcon("mailSend.png"),
            self.tr("Send Page Link"), self.__sendLink).setData(self.url())
        menu.addSeparator()
        
        from .UserAgent.UserAgentMenu import UserAgentMenu
        self.__userAgentMenu = UserAgentMenu(self.tr("User Agent"),
                                             url=self.url())
        menu.addMenu(self.__userAgentMenu)
        menu.addSeparator()
        menu.addAction(self.__mw.backAct)
        menu.addAction(self.__mw.forwardAct)
        menu.addAction(self.__mw.homeAct)
        menu.addAction(self.__mw.reloadAct)
        menu.addAction(self.__mw.stopAct)
        menu.addSeparator()
        menu.addAction(self.__mw.zoomInAct)
        menu.addAction(self.__mw.zoomResetAct)
        menu.addAction(self.__mw.zoomOutAct)
        menu.addSeparator()
        menu.addAction(self.__mw.selectAllAct)
        menu.addSeparator()
        menu.addAction(self.__mw.findAct)
        menu.addSeparator()
        menu.addAction(self.__mw.pageSourceAct)
        menu.addSeparator()
        menu.addAction(self.__mw.siteInfoAct)
        if self.url().scheme() in ["http", "https"]:
            menu.addSeparator()
            
            w3url = QUrl.fromEncoded(
                b"http://validator.w3.org/check?uri=" +
                QUrl.toPercentEncoding(bytes(self.url().toEncoded()).decode()))
            menu.addAction(
                UI.PixmapCache.getIcon("w3.png"),
                self.tr("Validate Page"), self.__openLinkInNewTab)\
                .setData(w3url)
            
            from .WebBrowserLanguagesDialog import WebBrowserLanguagesDialog
            languages = Preferences.toList(
                Preferences.Prefs.settings.value(
                    "WebBrowser/AcceptLanguages",
                    WebBrowserLanguagesDialog.defaultAcceptLanguages()))
            if languages:
                language = languages[0]
                langCode = language.split("[")[1][:2]
                googleTranslatorUrl = QUrl.fromEncoded(
                    b"http://translate.google.com/translate?sl=auto&tl=" +
                    langCode.encode() +
                    b"&u=" +
                    QUrl.toPercentEncoding(
                        bytes(self.url().toEncoded()).decode()))
                menu.addAction(
                    UI.PixmapCache.getIcon("translate.png"),
                    self.tr("Google Translate"), self.__openLinkInNewTab)\
                    .setData(googleTranslatorUrl)
        
    def __checkForForm(self, act, pos):
        """
        Private method to check the given position for an open search form.
        
        @param act reference to the action to be populated upon success
        @type QAction
        @param pos position to be tested
        @type QPoint
        """
        self.__clickedPos = self.mapToViewport(pos)
        
        from .Tools import Scripts
        script = Scripts.getFormData(self.__clickedPos)
        self.page().runJavaScript(
            script,
            WebBrowserPage.SafeJsWorld,
            lambda res: self.__checkForFormCallback(res, act))
    
    def __checkForFormCallback(self, res, act):
        """
        Private method handling the __checkForForm result.
        
        @param res result dictionary generated by JavaScript
        @type dict
        @param act reference to the action to be populated upon success
        @type QAction
        """
        if act is None or not bool(res):
            return
        
        url = QUrl(res["action"])
        method = res["method"]
        
        if not url.isEmpty() and method in ["get", "post"]:
            act.setVisible(True)
            act.setText(self.tr("Add to web search toolbar"))
            act.triggered.connect(self.__addSearchEngine)
    
    def __isUrlValid(self, url):
        """
        Private method to check a URL for validity.
        
        @param url URL to be checked (QUrl)
        @return flag indicating a valid URL (boolean)
        """
        return url.isValid() and \
            bool(url.host()) and \
            bool(url.scheme()) and \
            "." in url.host()
    
    def __replaceMisspelledWord(self):
        """
        Private slot to replace a misspelled word under the context menu.
        """
        act = self.sender()
        suggestion = act.text()
        self.page().replaceMisspelledWord(suggestion)
    
    def __openLinkInNewTab(self):
        """
        Private method called by the context menu to open a link in a new
        tab.
        """
        act = self.sender()
        url = act.data()
        if url.isEmpty():
            return
        
        self.setSource(url, newTab=True)
    
    def __openLinkInNewWindow(self):
        """
        Private slot called by the context menu to open a link in a new
        window.
        """
        act = self.sender()
        url = act.data()
        if url.isEmpty():
            return
        
        self.__mw.newWindow(url)
    
    def __openLinkInNewPrivateWindow(self):
        """
        Private slot called by the context menu to open a link in a new
        private window.
        """
        act = self.sender()
        url = act.data()
        if url.isEmpty():
            return
        
        self.__mw.newPrivateWindow(url)
    
    def __bookmarkLink(self):
        """
        Private slot to bookmark a link via the context menu.
        """
        act = self.sender()
        url = act.data()
        if url.isEmpty():
            return
        
        from .Bookmarks.AddBookmarkDialog import AddBookmarkDialog
        dlg = AddBookmarkDialog()
        dlg.setUrl(bytes(url.toEncoded()).decode())
        dlg.exec_()
    
    def __sendLink(self):
        """
        Private slot to send a link via email.
        """
        act = self.sender()
        data = act.data()
        if isinstance(data, QUrl) and data.isEmpty():
            return
        
        if isinstance(data, QUrl):
            data = data.toString()
        QDesktopServices.openUrl(QUrl("mailto:?body=" + data))
    
    def __copyLink(self):
        """
        Private slot to copy a link to the clipboard.
        """
        act = self.sender()
        data = act.data()
        if isinstance(data, QUrl) and data.isEmpty():
            return
        
        if isinstance(data, QUrl):
            data = data.toString()
        QApplication.clipboard().setText(data)
    
    def __downloadLink(self):
        """
        Private slot to download a link and save it to disk.
        """
        self.triggerPageAction(QWebEnginePage.DownloadLinkToDisk)
    
    def __downloadImage(self):
        """
        Private slot to download an image and save it to disk.
        """
        self.triggerPageAction(QWebEnginePage.DownloadImageToDisk)
    
    def __copyImage(self):
        """
        Private slot to copy an image to the clipboard.
        """
        self.triggerPageAction(QWebEnginePage.CopyImageToClipboard)
    
    def __blockImage(self):
        """
        Private slot to add a block rule for an image URL.
        """
        act = self.sender()
        url = act.data()
        dlg = WebBrowserWindow.adBlockManager().showDialog()
        dlg.addCustomRule(url)
    
    def __searchImage(self):
        """
        Private slot to search for an image URL.
        """
        act = self.sender()
        url = act.data()
        self.setSource(url, newTab=True)
    
    def __downloadMedia(self):
        """
        Private slot to download a media and save it to disk.
        """
        self.triggerPageAction(QWebEnginePage.DownloadMediaToDisk)
    
    def __pauseMedia(self):
        """
        Private slot to pause or play the selected media.
        """
        self.triggerPageAction(QWebEnginePage.ToggleMediaPlayPause)
    
    def __muteMedia(self):
        """
        Private slot to (un)mute the selected media.
        """
        self.triggerPageAction(QWebEnginePage.ToggleMediaMute)
    
    def __virusTotal(self):
        """
        Private slot to scan the selected URL with VirusTotal.
        """
        act = self.sender()
        url = act.data()
        self.__mw.requestVirusTotalScan(url)
    
    def __searchDefaultRequested(self):
        """
        Private slot to search for some text with the current search engine.
        """
        searchText = self.selectedText()
        
        if not searchText:
            return
        
        engine = self.__mw.openSearchManager().currentEngine()
        if engine:
            self.search.emit(engine.searchUrl(searchText))
    
    def __searchRequested(self, act):
        """
        Private slot to search for some text with a selected search engine.
        
        @param act reference to the action that triggered this slot (QAction)
        """
        searchText = self.selectedText()
        
        if not searchText:
            return
        
        engineName = act.data()
        if engineName:
            engine = self.__mw.openSearchManager().engine(engineName)
        else:
            engine = self.__mw.openSearchManager().currentEngine()
        if engine:
            self.search.emit(engine.searchUrl(searchText))
    
    def __addSearchEngine(self):
        """
        Private slot to add a new search engine.
        """
        from .Tools import Scripts
        script = Scripts.getFormData(self.__clickedPos)
        self.page().runJavaScript(
            script,
            WebBrowserPage.SafeJsWorld,
            lambda res: self.__mw.openSearchManager().addEngineFromForm(
                res, self))
    
    def __webInspector(self):
        """
        Private slot to show the web inspector window.
        """
        if self.__inspector is None:
            from .WebInspector import WebInspector
            self.__inspector = WebInspector()
            self.__inspector.setView(self, True)
            self.__inspector.show()
        else:
            self.closeWebInspector()
    
    def closeWebInspector(self):
        """
        Public slot to close the web inspector.
        """
        if self.__inspector is not None:
            if self.__inspector.isVisible():
                self.__inspector.hide()
            WebInspector.unregisterView(self.__inspector)
            self.__inspector.deleteLater()
            self.__inspector = None
    
    def addBookmark(self):
        """
        Public slot to bookmark the current page.
        """
        from .Tools import Scripts
        script = Scripts.getAllMetaAttributes()
        self.page().runJavaScript(
            script, WebBrowserPage.SafeJsWorld, self.__addBookmarkCallback)
    
    def __addBookmarkCallback(self, res):
        """
        Private callback method of __addBookmark().
        
        @param res reference to the result list containing all
            meta attributes
        @type list
        """
        description = ""
        for meta in res:
            if meta["name"] == "description":
                description = meta["content"]
        
        from .Bookmarks.AddBookmarkDialog import AddBookmarkDialog
        dlg = AddBookmarkDialog()
        dlg.setUrl(bytes(self.url().toEncoded()).decode())
        dlg.setTitle(self.title())
        dlg.setDescription(description)
        dlg.exec_()
    
    def dragEnterEvent(self, evt):
        """
        Protected method called by a drag enter event.
        
        @param evt reference to the drag enter event (QDragEnterEvent)
        """
        evt.acceptProposedAction()
    
    def dragMoveEvent(self, evt):
        """
        Protected method called by a drag move event.
        
        @param evt reference to the drag move event (QDragMoveEvent)
        """
        evt.ignore()
        if evt.source() != self:
            if len(evt.mimeData().urls()) > 0:
                evt.acceptProposedAction()
            else:
                url = QUrl(evt.mimeData().text())
                if url.isValid():
                    evt.acceptProposedAction()
        
        if not evt.isAccepted():
            super(WebBrowserView, self).dragMoveEvent(evt)
    
    def dropEvent(self, evt):
        """
        Protected method called by a drop event.
        
        @param evt reference to the drop event (QDropEvent)
        """
        super(WebBrowserView, self).dropEvent(evt)
        if not evt.isAccepted() and \
           evt.source() != self and \
           evt.possibleActions() & Qt.CopyAction:
            url = QUrl()
            if len(evt.mimeData().urls()) > 0:
                url = evt.mimeData().urls()[0]
            if not url.isValid():
                url = QUrl(evt.mimeData().text())
            if url.isValid():
                self.setSource(url)
                evt.acceptProposedAction()
    
    def _mousePressEvent(self, evt):
        """
        Protected method called by a mouse press event.
        
        @param evt reference to the mouse event (QMouseEvent)
        """
        if WebBrowserWindow.autoScroller().mousePress(self, evt):
            evt.accept()
            return
        
        self.__mw.setEventMouseButtons(evt.buttons())
        self.__mw.setEventKeyboardModifiers(evt.modifiers())
        
        if evt.button() == Qt.XButton1:
            self.pageAction(QWebEnginePage.Back).trigger()
            evt.accept()
        elif evt.button() == Qt.XButton2:
            self.pageAction(QWebEnginePage.Forward).trigger()
            evt.accept()
    
    def _mouseReleaseEvent(self, evt):
        """
        Protected method called by a mouse release event.
        
        @param evt reference to the mouse event (QMouseEvent)
        """
        if WebBrowserWindow.autoScroller().mouseRelease(evt):
            evt.accept()
            return
        
        accepted = evt.isAccepted()
        self.__page.event(evt)
        if not evt.isAccepted() and \
           self.__mw.eventMouseButtons() & Qt.MidButton:
            url = QUrl(QApplication.clipboard().text(QClipboard.Selection))
            if not url.isEmpty() and \
               url.isValid() and \
               url.scheme() != "":
                self.__mw.setEventMouseButtons(Qt.NoButton)
                self.__mw.setEventKeyboardModifiers(Qt.NoModifier)
                self.setSource(url)
        evt.setAccepted(accepted)
    
    def _mouseMoveEvent(self, evt):
        """
        Protected method to handle mouse move events.
        
        @param evt reference to the mouse event (QMouseEvent)
        """
        if self.__mw and self.__mw.isFullScreen():
            if self.__mw.isFullScreenNavigationVisible():
                self.__mw.hideFullScreenNavigation()
            elif evt.y() < 10:
                # mouse is within 10px to the top
                self.__mw.showFullScreenNavigation()
        
        if WebBrowserWindow.autoScroller().mouseMove(evt):
            evt.accept()
    
    def _wheelEvent(self, evt):
        """
        Protected method to handle wheel events.
        
        @param evt reference to the wheel event (QWheelEvent)
        """
        if WebBrowserWindow.autoScroller().wheel():
            evt.accept()
            return
        
        delta = evt.angleDelta().y()
        if evt.modifiers() & Qt.ControlModifier:
            if delta < 0:
                self.zoomOut()
            else:
                self.zoomIn()
            evt.accept()
        
        elif evt.modifiers() & Qt.ShiftModifier:
            if delta < 0:
                self.backward()
            else:
                self.forward()
            evt.accept()
    
    def _keyPressEvent(self, evt):
        """
        Protected method called by a key press.
        
        @param evt reference to the key event (QKeyEvent)
        """
        if self.__mw.personalInformationManager().viewKeyPressEvent(self, evt):
            evt.accept()
            return
        
        if evt.key() == Qt.Key_ZoomIn:
            self.zoomIn()
            evt.accept()
        elif evt.key() == Qt.Key_ZoomOut:
            self.zoomOut()
            evt.accept()
        elif evt.key() == Qt.Key_Plus:
            if evt.modifiers() & Qt.ControlModifier:
                self.zoomIn()
                evt.accept()
        elif evt.key() == Qt.Key_Minus:
            if evt.modifiers() & Qt.ControlModifier:
                self.zoomOut()
                evt.accept()
        elif evt.key() == Qt.Key_0:
            if evt.modifiers() & Qt.ControlModifier:
                self.zoomReset()
                evt.accept()
        elif evt.key() == Qt.Key_M:
            if evt.modifiers() & Qt.ControlModifier:
                self.__muteMedia()
                evt.accept()
    
    def _keyReleaseEvent(self, evt):
        """
        Protected method called by a key release.
        
        @param evt reference to the key event (QKeyEvent)
        """
        if evt.key() == Qt.Key_Escape:
            if self.isFullScreen():
                self.triggerPageAction(QWebEnginePage.ExitFullScreen)
                evt.accept()
                self.requestFullScreen(False)
    
    def _gestureEvent(self, evt):
        """
        Protected method handling gesture events.
        
        @param evt reference to the gesture event (QGestureEvent
        """
        pinch = evt.gesture(Qt.PinchGesture)
        if pinch:
            if pinch.state() == Qt.GestureStarted:
                pinch.setTotalScaleFactor(self.__currentZoom / 100.0)
            elif pinch.state() == Qt.GestureUpdated:
                scaleFactor = pinch.totalScaleFactor()
                self.setZoomValue(int(scaleFactor * 100))
            evt.accept()
    
    def eventFilter(self, obj, evt):
        """
        Public method to process event for other objects.
        
        @param obj reference to object to process events for
        @type QObject
        @param evt reference to event to be processed
        @type QEvent
        @return flag indicating that the event should be filtered out
        @rtype bool
        """
        # find the render widget receiving events for the web page
        if qVersionTuple() < (5, 8, 0):
            if obj is self and evt.type() == QEvent.ChildAdded:
                child = evt.child()
                if child and child.inherits(
                        "QtWebEngineCore::"
                        "RenderWidgetHostViewQtDelegateWidget"):
                    self.__rwhvqt = child
                    self.grabGesture(Qt.PinchGesture)
                    self.__rwhvqt.grabGesture(Qt.PinchGesture)
                    self.__rwhvqt.installEventFilter(self)
        else:
            if obj is self and evt.type() == QEvent.ParentChange and \
               self.parentWidget() is not None:
                self.parentWidget().installEventFilter(self)
        
        # forward events to WebBrowserView
        if obj is self.__rwhvqt and \
           evt.type() in [QEvent.KeyPress, QEvent.KeyRelease,
                          QEvent.MouseButtonPress, QEvent.MouseButtonRelease,
                          QEvent.MouseMove, QEvent.Wheel, QEvent.Gesture]:
            wasAccepted = evt.isAccepted()
            evt.setAccepted(False)
            if evt.type() == QEvent.KeyPress:
                self._keyPressEvent(evt)
            elif evt.type() == QEvent.KeyRelease:
                self._keyReleaseEvent(evt)
            elif evt.type() == QEvent.MouseButtonPress:
                self._mousePressEvent(evt)
            elif evt.type() == QEvent.MouseButtonRelease:
                self._mouseReleaseEvent(evt)
            elif evt.type() == QEvent.MouseMove:
                self._mouseMoveEvent(evt)
            elif evt.type() == QEvent.Wheel:
                self._wheelEvent(evt)
            elif evt.type() == QEvent.Gesture:
                self._gestureEvent(evt)
            ret = evt.isAccepted()
            evt.setAccepted(wasAccepted)
            return ret
        
        if obj is self.parentWidget() and \
           evt.type() in [QEvent.KeyPress, QEvent.KeyRelease]:
            wasAccepted = evt.isAccepted()
            evt.setAccepted(False)
            if evt.type() == QEvent.KeyPress:
                self._keyPressEvent(evt)
            elif evt.type() == QEvent.KeyRelease:
                self._keyReleaseEvent(evt)
            ret = evt.isAccepted()
            evt.setAccepted(wasAccepted)
            return ret
        
        # block already handled events
        if obj is self:
            if evt.type() in [QEvent.KeyPress, QEvent.KeyRelease,
                              QEvent.MouseButtonPress,
                              QEvent.MouseButtonRelease,
                              QEvent.MouseMove, QEvent.Wheel, QEvent.Gesture]:
                return True
            
            elif evt.type() == QEvent.Hide:
                if self.isFullScreen():
                    self.triggerPageAction(QWebEnginePage.ExitFullScreen)
        
        return super(WebBrowserView, self).eventFilter(obj, evt)
    
    def event(self, evt):
        """
        Public method handling events.
        
        @param evt reference to the event (QEvent)
        @return flag indicating, if the event was handled (boolean)
        """
        if evt.type() == QEvent.Gesture:
            self._gestureEvent(evt)
            return True
        
        return super(WebBrowserView, self).event(evt)
    
    def inputWidget(self):
        """
        Public method to get a reference to the render widget.
        
        @return reference to the render widget
        @rtype QWidget
        """
        return self.__rwhvqt
    
    def clearHistory(self):
        """
        Public slot to clear the history.
        """
        self.history().clear()
        self.__urlChanged(self.history().currentItem().url())
    
    ###########################################################################
    ## Signal converters below
    ###########################################################################
    
    def __urlChanged(self, url):
        """
        Private slot to handle the urlChanged signal.
        
        @param url the new url (QUrl)
        """
        self.sourceChanged.emit(url)
        
        self.forwardAvailable.emit(self.isForwardAvailable())
        self.backwardAvailable.emit(self.isBackwardAvailable())
    
    def __iconUrlChanged(self, url):
        """
        Private slot to handle the iconUrlChanged signal.
        
        @param url URL to get web site icon from
        @type QUrl
        """
        self.__siteIcon = QIcon()
        if self.__siteIconLoader is not None:
            self.__siteIconLoader.deleteLater()
        self.__siteIconLoader = WebIconLoader(url, self)
        self.__siteIconLoader.iconLoaded.connect(self.__iconLoaded)
    
    def __iconLoaded(self, icon):
        """
        Private slot handling the loaded web site icon.
        
        @param icon web site icon
        @type QIcon
        """
        self.__siteIcon = icon
        
        from .Tools import WebIconProvider
        WebIconProvider.instance().saveIcon(self)
        
        self.faviconChanged.emit()
    
    def icon(self):
        """
        Public method to get the web site icon.
        
        @return web site icon
        @rtype QIcon
        """
        if not self.__siteIcon.isNull():
            return QIcon(self.__siteIcon)
        
        from .Tools import WebIconProvider
        return WebIconProvider.instance().iconForUrl(self.url())
    
    def __linkHovered(self, link):
        """
        Private slot to handle the linkHovered signal.
        
        @param link the URL of the link (string)
        """
        self.highlighted.emit(link)
    
    ###########################################################################
    ## Signal handlers below
    ###########################################################################
    
    def __renderProcessTerminated(self, status, exitCode):
        """
        Private slot handling a crash of the web page render process.
        
        @param status termination status
        @type QWebEnginePage.RenderProcessTerminationStatus
        @param exitCode exit code of the process
        @type int
        """
        if status == QWebEnginePage.NormalTerminationStatus:
            return
        
        QTimer.singleShot(0, lambda: self.__showTabCrashPage(status))
    
    def __showTabCrashPage(self, status):
        """
        Private slot to show the tab crash page.
        
        @param status termination status
        @type QWebEnginePage.RenderProcessTerminationStatus
        """
        self.page().deleteLater()
        self.__page = WebBrowserPage(self)
        self.setPage(self.__page)
        
        html = readAllFileContents(":/html/tabCrashPage.html")
        html = html.replace("@IMAGE@", pixmapToDataUrl(
            qApp.style().standardIcon(QStyle.SP_MessageBoxWarning).pixmap(
                48, 48)).toString())
        html = html.replace("@FAVICON@", pixmapToDataUrl(
            qApp.style() .standardIcon(QStyle.SP_MessageBoxWarning).pixmap(
                16, 16)).toString())
        html = html.replace(
            "@TITLE@", self.tr("Render Process terminated abnormally"))
        html = html.replace(
            "@H1@", self.tr("Render Process terminated abnormally"))
        if status == QWebEnginePage.CrashedTerminationStatus:
            msg = self.tr("The render process crashed while"
                          " loading this page.")
        elif status == QWebEnginePage.KilledTerminationStatus:
            msg = self.tr("The render process was killed.")
        else:
            msg = self.tr("The render process terminated while"
                          " loading this page.")
        html = html.replace("@LI-1@", msg)
        html = html.replace(
            "@LI-2@",
            self.tr(
                "Try reloading the page or closing some tabs to make more"
                " memory available."))
        self.page().setHtml(html, self.url())
    
    def __loadStarted(self):
        """
        Private method to handle the loadStarted signal.
        """
        self.__isLoading = True
        self.__progress = 0
    
    def __loadProgress(self, progress):
        """
        Private method to handle the loadProgress signal.
        
        @param progress progress value (integer)
        """
        self.__progress = progress
    
    def __loadFinished(self, ok):
        """
        Private method to handle the loadFinished signal.
        
        @param ok flag indicating the result (boolean)
        """
        self.__isLoading = False
        self.__progress = 0
        
        QApplication.processEvents()
        QTimer.singleShot(200, self.__renderPreview)
        
        from .ZoomManager import ZoomManager
        zoomValue = ZoomManager.instance().zoomValue(self.url())
        self.setZoomValue(zoomValue)
        
        if ok:
            self.__mw.historyManager().addHistoryEntry(self)
            self.__mw.adBlockManager().page().hideBlockedPageEntries(
                self.page())
            self.__mw.passwordManager().completePage(self.page())
            
            self.page().runJavaScript(
                "document.lastModified", WebBrowserPage.SafeJsWorld,
                lambda res: self.__adjustBookmark(res))
    
    def __adjustBookmark(self, lastModified):
        """
        Private slot to adjust the 'lastModified' value of bookmarks.
        
        @param lastModified last modified value
        @type str
        """
        modified = QDateTime.fromString(lastModified, "MM/dd/yyyy hh:mm:ss")
        if modified.isValid():
            from WebBrowser.WebBrowserWindow import WebBrowserWindow
            from .Bookmarks.BookmarkNode import BookmarkNode
            manager = WebBrowserWindow.bookmarksManager()
            for bookmark in manager.bookmarksForUrl(self.url()):
                manager.setTimestamp(bookmark, BookmarkNode.TsModified,
                                     modified)
    
    def isLoading(self):
        """
        Public method to get the loading state.
        
        @return flag indicating the loading state (boolean)
        """
        return self.__isLoading
    
    def progress(self):
        """
        Public method to get the load progress.
        
        @return load progress (integer)
        """
        return self.__progress
    
    def __renderPreview(self):
        """
        Private slot to render a preview pixmap after the page was loaded.
        """
        from .WebBrowserSnap import renderTabPreview
        w = 600     # some default width, the preview gets scaled when shown
        h = int(w * self.height() / self.width())
        self.__preview = renderTabPreview(self, w, h)
    
    def getPreview(self):
        """
        Public method to get the preview pixmap.
        
        @return preview pixmap
        @rtype QPixmap
        """
        return self.__preview
    
    def saveAs(self):
        """
        Public method to save the current page to a file.
        """
        url = self.url()
        if url.isEmpty():
            return
        
        if qVersionTuple() >= (5, 8, 0):
            # since Qt 5.8.0
            fileName, savePageFormat = self.__getSavePageFileNameAndFormat()
            if fileName:
                self.page().save(fileName, savePageFormat)
        else:
            self.triggerPageAction(QWebEnginePage.SavePage)
    
    def __getSavePageFileNameAndFormat(self):
        """
        Private method to get the file name to save the page to.
        
        @return tuple containing the file name to save to and the
            save page format
        @rtype tuple of (str, QWebEngineDownloadItem.SavePageFormat)
        """
        documentLocation = QStandardPaths.writableLocation(
            QStandardPaths.DocumentsLocation)
        filterList = [
            self.tr("Web Archive (*.mhtml *.mht)"),
            self.tr("HTML File (*.html *.htm)"),
            self.tr("HTML File with all resources (*.html *.htm)"),
        ]
        extensionsList = [
            # tuple of extensions for *nix and Windows
            # keep in sync with filters list
            (".mhtml", ".mht"),
            (".html", ".htm"),
            (".html", ".htm"),
        ]
        if self.url().fileName():
            defaultFileName = os.path.join(documentLocation,
                                           self.url().fileName())
        else:
            defaultFileName = os.path.join(documentLocation,
                                           self.page().title())
            if Utilities.isWindowsPlatform():
                defaultFileName += ".mht"
            else:
                defaultFileName += ".mhtml"

        fileName = ""
        saveFormat = QWebEngineDownloadItem.MimeHtmlSaveFormat
        
        fileName, selectedFilter = E5FileDialog.getSaveFileNameAndFilter(
            None,
            self.tr("Save Web Page"),
            defaultFileName,
            ";;".join(filterList),
            None)
        if fileName:
            index = filterList.index(selectedFilter)
            if index == 0:
                saveFormat = QWebEngineDownloadItem.MimeHtmlSaveFormat
            elif index == 1:
                saveFormat = QWebEngineDownloadItem.SingleHtmlSaveFormat
            else:
                saveFormat = QWebEngineDownloadItem.CompleteHtmlSaveFormat
            
            extension = os.path.splitext(fileName)[1]
            if not extension:
                # add the platform specific default extension
                if Utilities.isWindowsPlatform():
                    extensionsIndex = 1
                else:
                    extensionsIndex = 0
                extensions = extensionsList[index]
                fileName += extensions[extensionsIndex]
        
        return fileName, saveFormat
    
    ###########################################################################
    ## Miscellaneous methods below
    ###########################################################################
    
    def createWindow(self, windowType):
        """
        Public method called, when a new window should be created.
        
        @param windowType type of the requested window
            (QWebEnginePage.WebWindowType)
        @return reference to the created browser window (WebBrowserView)
        """
        if windowType in [QWebEnginePage.WebBrowserTab,
                          QWebEnginePage.WebDialog]:
            return self.__mw.newTab(addNextTo=self)
        elif windowType == QWebEnginePage.WebBrowserWindow:
            return self.__mw.newWindow().currentBrowser()
        else:
            return self.__mw.newTab(addNextTo=self, background=True)
    
    def preferencesChanged(self):
        """
        Public method to indicate a change of the settings.
        """
        self.reload()
    
    ###########################################################################
    ## RSS related methods below
    ###########################################################################
    
    def checkRSS(self):
        """
        Public method to check, if the loaded page contains feed links.
        
        @return flag indicating the existence of feed links (boolean)
        """
        self.__rss = []
        
        script = Scripts.getFeedLinks()
        feeds = self.page().execJavaScript(script)
        
        if feeds is not None:
            for feed in feeds:
                if feed["url"] and feed["title"]:
                    self.__rss.append((feed["title"], feed["url"]))
        
        return len(self.__rss) > 0
    
    def getRSS(self):
        """
        Public method to get the extracted RSS feeds.
        
        @return list of RSS feeds (list of tuples of two strings)
        """
        return self.__rss
    
    def hasRSS(self):
        """
        Public method to check, if the loaded page has RSS links.
        
        @return flag indicating the presence of RSS links (boolean)
        """
        return len(self.__rss) > 0
    
    ###########################################################################
    ## Full Screen handling below
    ###########################################################################
    
    def isFullScreen(self):
        """
        Public method to check, if full screen mode is active.
        
        @return flag indicating full screen mode
        @rtype bool
        """
        return self.__mw.isFullScreen()
    
    def requestFullScreen(self, enable):
        """
        Public method to request full screen mode.
        
        @param enable flag indicating full screen mode on or off
        @type bool
        """
        if enable:
            self.__mw.enterHtmlFullScreen()
        else:
            self.__mw.showNormal()
    
    ###########################################################################
    ## Speed Dial slots below
    ###########################################################################
    
    def __addSpeedDial(self):
        """
        Private slot to add a new speed dial.
        """
        self.__page.runJavaScript("addSpeedDial();",
                                  WebBrowserPage.SafeJsWorld)
    
    def __configureSpeedDial(self):
        """
        Private slot to configure the speed dial.
        """
        self.page().runJavaScript("configureSpeedDial();",
                                  WebBrowserPage.SafeJsWorld)
    
    def __reloadAllSpeedDials(self):
        """
        Private slot to reload all speed dials.
        """
        self.page().runJavaScript("reloadAll();", WebBrowserPage.SafeJsWorld)
    
    def __resetSpeedDials(self):
        """
        Private slot to reset all speed dials to the default pages.
        """
        self.__speedDial.resetDials()
    
    ###########################################################################
    ## Methods below implement session related functions
    ###########################################################################
    
    def storeSessionData(self, data):
        """
        Public method to store session data to be restored later on.
        
        @param data dictionary with session data to be restored
        @type dict
        """
        self.__restoreData = data
    
    def __showEventSlot(self):
        """
        Private slot to perform actions when the view is shown and the event
        loop is running.
        """
        if self.__restoreData:
            sessionData, self.__restoreData = self.__restoreData, None
            self.loadFromSessionData(sessionData)
    
    def showEvent(self, evt):
        """
        Protected method to handle show events.
        
        @param evt reference to the show event object
        @type QShowEvent
        """
        super(WebBrowserView, self).showEvent(evt)
        self.activateSession()
    
    def activateSession(self):
        """
        Public slot to activate a restored session.
        """
        if self.__restoreData and not self.__mw.isClosing():
            QTimer.singleShot(0, self.__showEventSlot)
    
    def getSessionData(self):
        """
        Public method to populate the session data.
        
        @return dictionary containing the session data
        @rtype dict
        """
        if self.__restoreData:
            # page has not been shown yet
            return self.__restoreData
        
        sessionData = {}
        page = self.page()
        
        # 1. zoom factor
        sessionData["ZoomFactor"] = page.zoomFactor()
        
        # 2. scroll position
        scrollPos = page.scrollPosition()
        sessionData["ScrollPosition"] = {
            "x": scrollPos.x(),
            "y": scrollPos.y(),
        }
        
        # 3. page history
        historyArray = QByteArray()
        stream = QDataStream(historyArray, QIODevice.WriteOnly)
        stream << page.history()
        sessionData["History"] = str(
            historyArray.toBase64(QByteArray.Base64UrlEncoding),
            encoding="ascii")
        sessionData["HistoryIndex"] = page.history().currentItemIndex()
        
        # 4. current URL and title
        sessionData["Url"] = self.url().toString()
        sessionData["Title"] = self.title()
        
        # 5. web icon
        iconArray = QByteArray()
        stream = QDataStream(iconArray, QIODevice.WriteOnly)
        stream << page.icon()
        sessionData["Icon"] = str(iconArray.toBase64(), encoding="ascii")
        
        return sessionData
    
    def loadFromSessionData(self, sessionData):
        """
        Public method to load the session data.
        
        @param sessionData dictionary containing the session data as
            generated by getSessionData()
        @type dict
        """
        page = self.page()
        # blank the page
        page.setUrl(QUrl("about:blank"))
        
        # 1. page history
        if "History" in sessionData:
            historyArray = QByteArray.fromBase64(
                sessionData["History"].encode("ascii"),
                QByteArray.Base64UrlEncoding)
            stream = QDataStream(historyArray, QIODevice.ReadOnly)
            stream >> page.history()
            
            if "HistoryIndex" in sessionData:
                item = page.history().itemAt(sessionData["HistoryIndex"])
                if item is not None:
                    page.history().goToItem(item)
        
        # 2. zoom factor
        if "ZoomFactor" in sessionData:
            page.setZoomFactor(sessionData["ZoomFactor"])
        
        # 3. scroll position
        if "ScrollPosition" in sessionData:
            scrollPos = sessionData["ScrollPosition"]
            page.scrollTo(QPointF(scrollPos["x"], scrollPos["y"]))
    
    def extractSessionMetaData(self, sessionData):
        """
        Public method to extract some session meta data elements needed by the
        tab widget in case of deferred loading.
        
        @param sessionData dictionary containing the session data as
            generated by getSessionData()
        @type dict
        @return tuple containing the title, URL and web icon
        @rtype tuple of (str, str, QIcon)
        """
        if "Title" in sessionData:
            title = sessionData["Title"]
        else:
            title = ""
        
        if "Url" in sessionData:
            urlStr = sessionData["Url"]
        else:
            urlStr = ""
        
        if "Icon" in sessionData:
            iconArray = QByteArray.fromBase64(
                sessionData["Icon"].encode("ascii"))
            stream = QDataStream(iconArray, QIODevice.ReadOnly)
            icon = QIcon()
            stream >> icon
        else:
            from .Tools import WebIconProvider
            icon = WebIconProvider.instance().iconForUrl(
                QUrl.fromUserInput(urlStr))
        
        return title, urlStr, icon
