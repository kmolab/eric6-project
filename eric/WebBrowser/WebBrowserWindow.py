# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the web browser main window.
"""

from __future__ import unicode_literals
try:
    str = unicode           # __IGNORE_EXCEPTION__
except NameError:
    pass

import os
import shutil
import sys

from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QByteArray, QSize, QTimer, \
    QUrl, QTextCodec, QProcess, QEvent
from PyQt5.QtGui import QDesktopServices, QKeySequence, QFont, QFontMetrics
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QDockWidget, \
    QComboBox, QLabel, QMenu, QToolButton, QLineEdit, QApplication, \
    QWhatsThis, QDialog, QHBoxLayout, QProgressBar, QInputDialog, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEnginePage, \
    QWebEngineProfile, QWebEngineScript
try:
    from PyQt5.QtHelp import QHelpEngine, QHelpEngineCore, QHelpSearchQuery
    QTHELP_AVAILABLE = True
except ImportError:
    QTHELP_AVAILABLE = False

from E5Gui.E5Action import E5Action
from E5Gui import E5MessageBox, E5FileDialog, E5ErrorMessage
from E5Gui.E5MainWindow import E5MainWindow
from E5Gui.E5Application import e5App
from E5Gui.E5ZoomWidget import E5ZoomWidget

from E5Network.E5NetworkIcon import E5NetworkIcon

import Preferences
from Preferences import Shortcuts

import Utilities
import Globals
from Globals import qVersionTuple

import UI.PixmapCache
import UI.Config
from UI.Info import Version

from .data import icons_rc          # __IGNORE_WARNING__
from .data import html_rc           # __IGNORE_WARNING__
from .data import javascript_rc     # __IGNORE_WARNING__


from .Tools import Scripts, WebBrowserTools, WebIconProvider

from .ZoomManager import ZoomManager

from eric6config import getConfig


class WebBrowserWindow(E5MainWindow):
    """
    Class implementing the web browser main window.
    
    @signal webBrowserWindowOpened(window) emitted after a new web browser
        window was opened
    @signal webBrowserWindowClosed(window) emitted after the window was
        requested to close
    @signal webBrowserOpened(browser) emitted after a new web browser tab was
        created
    @signal webBrowserClosed(browser) emitted after a web browser tab was
        closed
    """
    webBrowserWindowClosed = pyqtSignal(E5MainWindow)
    webBrowserWindowOpened = pyqtSignal(E5MainWindow)
    webBrowserOpened = pyqtSignal(QWidget)
    webBrowserClosed = pyqtSignal(QWidget)
    
    BrowserWindows = []

    _fromEric = False
    _useQtHelp = QTHELP_AVAILABLE
    _isPrivate = False
    
    _webProfile = None
    _networkManager = None
    _cookieJar = None
    _helpEngine = None
    _bookmarksManager = None
    _historyManager = None
    _passwordManager = None
    _adblockManager = None
    _downloadManager = None
    _feedsManager = None
    _userAgentsManager = None
    _syncManager = None
    _speedDial = None
    _personalInformationManager = None
    _greaseMonkeyManager = None
    _notification = None
    _featurePermissionManager = None
    _flashCookieManager = None
    _imageSearchEngine = None
    _autoScroller = None
    _tabManager = None
    _sessionManager = None
    
    _performingStartup = True
    _performingShutdown = False
    _lastActiveWindow = None
    
    def __init__(self, home, path, parent, name, fromEric=False,
                 initShortcutsOnly=False, searchWord=None,
                 private=False, qthelp=False, settingsDir="",
                 restoreSession=False):
        """
        Constructor
        
        @param home the URL to be shown
        @type str
        @param path the path of the working dir (usually '.')
        @type str
        @param parent parent widget of this window
        @type QWidget
        @param name name of this window
        @type str
        @param fromEric flag indicating whether it was called from within
            eric6
        @type bool
        @keyparam initShortcutsOnly flag indicating to just initialize the
            keyboard shortcuts
        @type bool
        @keyparam searchWord word to search for
        @type str
        @keyparam private flag indicating a private browsing window
        @type bool
        @keyparam qthelp flag indicating to enable the QtHelp support
        @type bool
        @keyparam settingsDir directory to be used for the settings files
        @type str
        @keyparam restoreSession flag indicating a restore session action
        @type bool
        """
        self.__hideNavigationTimer = None
        
        super(WebBrowserWindow, self).__init__(parent)
        self.setObjectName(name)
        if private:
            self.setWindowTitle(self.tr("eric6 Web Browser (Private Mode)"))
        else:
            self.setWindowTitle(self.tr("eric6 Web Browser"))
        
        self.__settingsDir = settingsDir
        self.__fromEric = fromEric
        WebBrowserWindow._fromEric = fromEric
        self.__initShortcutsOnly = initShortcutsOnly
        self.setWindowIcon(UI.PixmapCache.getIcon("ericWeb.png"))

        self.__mHistory = []
        self.__lastConfigurationPageName = ""
        
        WebBrowserWindow._isPrivate = private
        
        self.__eventMouseButtons = Qt.NoButton
        self.__eventKeyboardModifiers = Qt.NoModifier
        
        if self.__initShortcutsOnly:
            WebBrowserWindow.setUseQtHelp(
                self.__fromEric or qthelp or bool(searchWord))
            self.__initActions()
        else:
            if Preferences.getWebBrowser("WebInspectorEnabled"):
                os.putenv(
                    "QTWEBENGINE_REMOTE_DEBUGGING",
                    str(Preferences.getWebBrowser("WebInspectorPort")))
            
            WebBrowserWindow.setUseQtHelp(
                self.__fromEric or qthelp or bool(searchWord))
            
            self.webProfile(private)
            self.networkManager()
            
            self.__htmlFullScreen = False
            self.__windowStates = Qt.WindowNoState
            self.__isClosing = False
            
            from .SearchWidget import SearchWidget
            from .QtHelp.HelpTocWidget import HelpTocWidget
            from .QtHelp.HelpIndexWidget import HelpIndexWidget
            from .QtHelp.HelpSearchWidget import HelpSearchWidget
            from .WebBrowserView import WebBrowserView
            from .WebBrowserTabWidget import WebBrowserTabWidget
            from .AdBlock.AdBlockIcon import AdBlockIcon
            from .StatusBar.JavaScriptIcon import JavaScriptIcon
            from .StatusBar.ImagesIcon import ImagesIcon
            from .VirusTotal.VirusTotalApi import VirusTotalAPI
            from .Navigation.NavigationBar import NavigationBar
            from .Navigation.NavigationContainer import NavigationContainer
            from .Bookmarks.BookmarksToolBar import BookmarksToolBar
            
            if not self.__fromEric:
                self.setStyle(Preferences.getUI("Style"),
                              Preferences.getUI("StyleSheet"))
                
                # initialize some SSL stuff
                from E5Network.E5SslUtilities import initSSL
                initSSL()
            
            if WebBrowserWindow._useQtHelp:
                self.__helpEngine = QHelpEngine(
                    WebBrowserWindow.getQtHelpCollectionFileName(),
                    self)
                self.__removeOldDocumentation()
                self.__helpEngine.warning.connect(self.__warning)
            else:
                self.__helpEngine = None
            self.__helpInstaller = None
            
            self.__zoomWidget = E5ZoomWidget(
                UI.PixmapCache.getPixmap("zoomOut.png"),
                UI.PixmapCache.getPixmap("zoomIn.png"),
                UI.PixmapCache.getPixmap("zoomReset.png"), self)
            self.statusBar().addPermanentWidget(self.__zoomWidget)
            self.__zoomWidget.setMapping(
                WebBrowserView.ZoomLevels, WebBrowserView.ZoomLevelDefault)
            self.__zoomWidget.valueChanged.connect(self.__zoomValueChanged)
            
            self.__tabWidget = WebBrowserTabWidget(self)
            self.__tabWidget.currentChanged[int].connect(self.__currentChanged)
            self.__tabWidget.titleChanged.connect(self.__titleChanged)
            self.__tabWidget.showMessage.connect(self.statusBar().showMessage)
            self.__tabWidget.browserZoomValueChanged.connect(
                self.__zoomWidget.setValue)
            self.__tabWidget.browserClosed.connect(self.webBrowserClosed)
            self.__tabWidget.browserOpened.connect(self.webBrowserOpened)
            
            self.__searchWidget = SearchWidget(self, self)
            
            self.__setIconDatabasePath()
            
            bookmarksModel = self.bookmarksManager().bookmarksModel()
            self.__bookmarksToolBar = BookmarksToolBar(self, bookmarksModel,
                                                       self)
            self.__bookmarksToolBar.setIconSize(UI.Config.ToolBarIconSize)
            self.__bookmarksToolBar.openUrl.connect(self.openUrl)
            self.__bookmarksToolBar.newTab.connect(self.openUrlNewTab)
            self.__bookmarksToolBar.newWindow.connect(self.openUrlNewWindow)
            
            self.__navigationBar = NavigationBar(self)
            
            self.__navigationContainer = NavigationContainer(self)
            self.__navigationContainer.addWidget(self.__navigationBar)
            self.__navigationContainer.addWidget(self.__bookmarksToolBar)
            
            centralWidget = QWidget()
            layout = QVBoxLayout()
            layout.setContentsMargins(1, 1, 1, 1)
            layout.setSpacing(0)
            layout.addWidget(self.__navigationContainer)
            layout.addWidget(self.__tabWidget)
            layout.addWidget(self.__searchWidget)
            self.__tabWidget.setSizePolicy(
                QSizePolicy.Preferred, QSizePolicy.Expanding)
            centralWidget.setLayout(layout)
            self.setCentralWidget(centralWidget)
            self.__searchWidget.hide()
            
            if WebBrowserWindow._useQtHelp:
                # setup the TOC widget
                self.__tocWindow = HelpTocWidget(self.__helpEngine)
                self.__tocDock = QDockWidget(self.tr("Contents"), self)
                self.__tocDock.setObjectName("TocWindow")
                self.__tocDock.setWidget(self.__tocWindow)
                self.addDockWidget(Qt.LeftDockWidgetArea, self.__tocDock)
                
                # setup the index widget
                self.__indexWindow = HelpIndexWidget(self.__helpEngine)
                self.__indexDock = QDockWidget(self.tr("Index"), self)
                self.__indexDock.setObjectName("IndexWindow")
                self.__indexDock.setWidget(self.__indexWindow)
                self.addDockWidget(Qt.LeftDockWidgetArea, self.__indexDock)
                
                # setup the search widget
                self.__searchWord = searchWord
                self.__indexing = False
                self.__indexingProgress = None
                self.__searchEngine = self.__helpEngine.searchEngine()
                self.__searchEngine.indexingStarted.connect(
                    self.__indexingStarted)
                self.__searchEngine.indexingFinished.connect(
                    self.__indexingFinished)
                self.__searchWindow = HelpSearchWidget(self.__searchEngine)
                self.__searchDock = QDockWidget(self.tr("Search"), self)
                self.__searchDock.setObjectName("SearchWindow")
                self.__searchDock.setWidget(self.__searchWindow)
                self.addDockWidget(Qt.LeftDockWidgetArea, self.__searchDock)
            
            # JavaScript Console window
            from .WebBrowserJavaScriptConsole import \
                WebBrowserJavaScriptConsole
            self.__javascriptConsole = WebBrowserJavaScriptConsole(self)
            self.__javascriptConsoleDock = QDockWidget(
                self.tr("JavaScript Console"))
            self.__javascriptConsoleDock.setObjectName("JavascriptConsole")
            self.__javascriptConsoleDock.setAllowedAreas(
                Qt.BottomDockWidgetArea | Qt.TopDockWidgetArea)
            self.__javascriptConsoleDock.setWidget(self.__javascriptConsole)
            self.addDockWidget(Qt.BottomDockWidgetArea,
                               self.__javascriptConsoleDock)
            
            if Preferences.getWebBrowser("SaveGeometry"):
                g = Preferences.getGeometry("WebBrowserGeometry")
            else:
                g = QByteArray()
            if g.isEmpty():
                s = QSize(800, 800)
                self.resize(s)
            else:
                self.restoreGeometry(g)
            
            WebBrowserWindow.BrowserWindows.append(self)
            
            self.__initWebEngineSettings()
            
            # initialize some of our class objects
            self.passwordManager()
            self.historyManager()
            self.greaseMonkeyManager()
            
            # initialize the actions
            self.__initActions()
            
            # initialize the menus
            self.__initMenus()
            self.__initSuperMenu()
            if Preferences.getWebBrowser("MenuBarVisible"):
                self.__navigationBar.superMenuButton().hide()
            else:
                self.menuBar().hide()
            
            # save references to toolbars in order to hide them
            # when going full screen
            self.__toolbars = {}
            # initialize toolbars
            if Preferences.getWebBrowser("ShowToolbars"):
                self.__initToolbars()
            self.__bookmarksToolBar.setVisible(
                Preferences.getWebBrowser("BookmarksToolBarVisible"))
            
            syncMgr = self.syncManager()
            syncMgr.syncMessage.connect(self.statusBar().showMessage)
            syncMgr.syncError.connect(self.statusBar().showMessage)
            
            restoreSessionData = {}
            if WebBrowserWindow._performingStartup and not home:
                startupBehavior = Preferences.getWebBrowser("StartupBehavior")
                if not private and startupBehavior in [3, 4]:
                    if startupBehavior == 3:
                        # restore last session
                        restoreSessionFile = \
                            self.sessionManager().lastActiveSessionFile()
                    elif startupBehavior == 4:
                        # select session
                        restoreSessionFile = \
                            self.sessionManager().selectSession()
                    sessionData = \
                        self.sessionManager().readSessionFromFile(
                            restoreSessionFile)
                    if self.sessionManager().isValidSession(sessionData):
                        restoreSessionData = sessionData
                        restoreSession = True
                else:
                    if Preferences.getWebBrowser("StartupBehavior") == 0:
                        home = "about:blank"
                    elif Preferences.getWebBrowser("StartupBehavior") == 1:
                        home = Preferences.getWebBrowser("HomePage")
                    elif Preferences.getWebBrowser("StartupBehavior") == 2:
                        home = "eric:speeddial"
            
            if not restoreSession:
                self.__tabWidget.newBrowser(home)
                self.__tabWidget.currentBrowser().setFocus()
            WebBrowserWindow._performingStartup = False
            
            self.__imagesIcon = ImagesIcon(self)
            self.statusBar().addPermanentWidget(self.__imagesIcon)
            self.__javaScriptIcon = JavaScriptIcon(self)
            self.statusBar().addPermanentWidget(self.__javaScriptIcon)
            
            self.__adBlockIcon = AdBlockIcon(self)
            self.statusBar().addPermanentWidget(self.__adBlockIcon)
            self.__adBlockIcon.setEnabled(
                Preferences.getWebBrowser("AdBlockEnabled"))
            self.__tabWidget.currentChanged[int].connect(
                self.__adBlockIcon.currentChanged)
            self.__tabWidget.sourceChanged.connect(
                self.__adBlockIcon.sourceChanged)
            
            self.__tabManagerIcon = self.tabManager().createStatusBarIcon()
            self.statusBar().addPermanentWidget(self.__tabManagerIcon)
            
            self.networkIcon = E5NetworkIcon(self)
            self.statusBar().addPermanentWidget(self.networkIcon)
            
            if not Preferences.getWebBrowser("StatusBarVisible"):
                self.statusBar().hide()
            
            QDesktopServices.setUrlHandler("http", self.__linkActivated)
            QDesktopServices.setUrlHandler("https", self.__linkActivated)
            
            # setup connections
            self.__activating = False
            if WebBrowserWindow._useQtHelp:
                # TOC window
                self.__tocWindow.escapePressed.connect(
                    self.__activateCurrentBrowser)
                self.__tocWindow.openUrl.connect(self.openUrl)
                self.__tocWindow.newTab.connect(self.openUrlNewTab)
                self.__tocWindow.newBackgroundTab.connect(
                    self.openUrlNewBackgroundTab)
                self.__tocWindow.newWindow.connect(self.openUrlNewWindow)
                
                # index window
                self.__indexWindow.escapePressed.connect(
                    self.__activateCurrentBrowser)
                self.__indexWindow.openUrl.connect(self.openUrl)
                self.__indexWindow.newTab.connect(self.openUrlNewTab)
                self.__indexWindow.newBackgroundTab.connect(
                    self.openUrlNewBackgroundTab)
                self.__indexWindow.newWindow.connect(self.openUrlNewWindow)
                
                # search window
                self.__searchWindow.escapePressed.connect(
                    self.__activateCurrentBrowser)
                self.__searchWindow.openUrl.connect(self.openUrl)
                self.__searchWindow.newTab.connect(self.openUrlNewTab)
                self.__searchWindow.newBackgroundTab.connect(
                    self.openUrlNewBackgroundTab)
                self.__searchWindow.newWindow.connect(self.openUrlNewWindow)
            
            state = Preferences.getWebBrowser("WebBrowserState")
            self.restoreState(state)
            
            self.__initHelpDb()
            
            self.__virusTotal = VirusTotalAPI(self)
            self.__virusTotal.submitUrlError.connect(
                self.__virusTotalSubmitUrlError)
            self.__virusTotal.urlScanReport.connect(
                self.__virusTotalUrlScanReport)
            self.__virusTotal.fileScanReport.connect(
                self.__virusTotalFileScanReport)
            
            self.flashCookieManager()
            
            if WebBrowserWindow._useQtHelp:
                QTimer.singleShot(0, self.__lookForNewDocumentation)
                if self.__searchWord is not None:
                    QTimer.singleShot(0, self.__searchForWord)
            
            e5App().focusChanged.connect(self.__appFocusChanged)
            
            self.__toolbarStates = self.saveState()
            
            self.__hideNavigationTimer = QTimer(self)
            self.__hideNavigationTimer.setInterval(1000)
            self.__hideNavigationTimer.setSingleShot(True)
            self.__hideNavigationTimer.timeout.connect(self.__hideNavigation)
            
            self.__forcedClose = False
            
            if restoreSessionData:
                self.sessionManager().restoreSessionFromData(
                    self, restoreSessionData)
            
            self.sessionManager().activateTimer()
            
            QTimer.singleShot(0, syncMgr.loadSettings)
    
    def __del__(self):
        """
        Special method called during object destruction.
        
        Note: This empty variant seems to get rid of the Qt message
        'Warning: QBasicTimer::start: QBasicTimer can only be used with
        threads started with QThread'
        """
        pass
    
    def tabWidget(self):
        """
        Public method to get a reference to the tab widget.
        
        @return reference to the tab widget
        @rtype WebBrowserTabWidget
        """
        return self.__tabWidget
    
    def fromEric(self):
        """
        Public method to check, if the web browser was called from within the
        eric IDE.
        
        @return flag indicating that the browserw as opened from within eric
        @rtype bool
        """
        return self.__fromEric
    
    def __setIconDatabasePath(self, enable=True):
        """
        Private method to set the favicons path.
        
        @param enable flag indicating to enabled icon storage (boolean)
        """
        if enable:
            iconDatabasePath = os.path.join(Utilities.getConfigDir(),
                                            "web_browser", "favicons")
            if not os.path.exists(iconDatabasePath):
                os.makedirs(iconDatabasePath)
        else:
            iconDatabasePath = ""   # setting an empty path disables it
        
        WebIconProvider.instance().setIconDatabasePath(iconDatabasePath)
        
    def __initWebEngineSettings(self):
        """
        Private method to set the global web settings.
        """
        settings = QWebEngineSettings.defaultSettings()
        
        settings.setFontFamily(
            QWebEngineSettings.StandardFont,
            Preferences.getWebBrowser("StandardFontFamily"))
        settings.setFontFamily(
            QWebEngineSettings.FixedFont,
            Preferences.getWebBrowser("FixedFontFamily"))
        settings.setFontFamily(
            QWebEngineSettings.SerifFont,
            Preferences.getWebBrowser("SerifFontFamily"))
        settings.setFontFamily(
            QWebEngineSettings.SansSerifFont,
            Preferences.getWebBrowser("SansSerifFontFamily"))
        settings.setFontFamily(
            QWebEngineSettings.CursiveFont,
            Preferences.getWebBrowser("CursiveFontFamily"))
        settings.setFontFamily(
            QWebEngineSettings.FantasyFont,
            Preferences.getWebBrowser("FantasyFontFamily"))
        
        settings.setFontSize(
            QWebEngineSettings.DefaultFontSize,
            Preferences.getWebBrowser("DefaultFontSize"))
        settings.setFontSize(
            QWebEngineSettings.DefaultFixedFontSize,
            Preferences.getWebBrowser("DefaultFixedFontSize"))
        settings.setFontSize(
            QWebEngineSettings.MinimumFontSize,
            Preferences.getWebBrowser("MinimumFontSize"))
        settings.setFontSize(
            QWebEngineSettings.MinimumLogicalFontSize,
            Preferences.getWebBrowser("MinimumLogicalFontSize"))
        
        styleSheet = Preferences.getWebBrowser("UserStyleSheet")
        self.__setUserStyleSheet(styleSheet)
        
        settings.setAttribute(
            QWebEngineSettings.AutoLoadImages,
            Preferences.getWebBrowser("AutoLoadImages"))
        settings.setAttribute(
            QWebEngineSettings.JavascriptEnabled,
            True)
        # JavaScript is needed for the web browser functionality
        settings.setAttribute(
            QWebEngineSettings.JavascriptCanOpenWindows,
            Preferences.getWebBrowser("JavaScriptCanOpenWindows"))
        settings.setAttribute(
            QWebEngineSettings.JavascriptCanAccessClipboard,
            Preferences.getWebBrowser("JavaScriptCanAccessClipboard"))
        settings.setAttribute(
            QWebEngineSettings.PluginsEnabled,
            Preferences.getWebBrowser("PluginsEnabled"))
        
        if self.isPrivate():
            settings.setAttribute(
                QWebEngineSettings.LocalStorageEnabled, False)
        else:
            settings.setAttribute(
                QWebEngineSettings.LocalStorageEnabled,
                Preferences.getWebBrowser("LocalStorageEnabled"))
        settings.setDefaultTextEncoding(
            Preferences.getWebBrowser("DefaultTextEncoding"))
        
        settings.setAttribute(
            QWebEngineSettings.SpatialNavigationEnabled,
            Preferences.getWebBrowser("SpatialNavigationEnabled"))
        settings.setAttribute(
            QWebEngineSettings.LinksIncludedInFocusChain,
            Preferences.getWebBrowser("LinksIncludedInFocusChain"))
        settings.setAttribute(
            QWebEngineSettings.LocalContentCanAccessRemoteUrls,
            Preferences.getWebBrowser("LocalContentCanAccessRemoteUrls"))
        settings.setAttribute(
            QWebEngineSettings.LocalContentCanAccessFileUrls,
            Preferences.getWebBrowser("LocalContentCanAccessFileUrls"))
        settings.setAttribute(
            QWebEngineSettings.XSSAuditingEnabled,
            Preferences.getWebBrowser("XSSAuditingEnabled"))
        settings.setAttribute(
            QWebEngineSettings.ScrollAnimatorEnabled,
            Preferences.getWebBrowser("ScrollAnimatorEnabled"))
        settings.setAttribute(
            QWebEngineSettings.ErrorPageEnabled,
            Preferences.getWebBrowser("ErrorPageEnabled"))
        settings.setAttribute(
            QWebEngineSettings.FullScreenSupportEnabled,
            Preferences.getWebBrowser("FullScreenSupportEnabled"))
        
        try:
            # Qt 5.7
            settings.setAttribute(
                QWebEngineSettings.ScreenCaptureEnabled,
                Preferences.getWebBrowser("ScreenCaptureEnabled"))
            settings.setAttribute(
                QWebEngineSettings.WebGLEnabled,
                Preferences.getWebBrowser("WebGLEnabled"))
        except (AttributeError, KeyError):
            pass
        
        try:
            # Qt 5.8
            settings.setAttribute(
                QWebEngineSettings.FocusOnNavigationEnabled,
                Preferences.getWebBrowser("FocusOnNavigationEnabled"))
            settings.setAttribute(
                QWebEngineSettings.PrintElementBackgrounds,
                Preferences.getWebBrowser("PrintElementBackgrounds"))
            settings.setAttribute(
                QWebEngineSettings.AllowRunningInsecureContent,
                Preferences.getWebBrowser("AllowRunningInsecureContent"))
        except (AttributeError, KeyError):
            pass
    
    def __initActions(self):
        """
        Private method to define the user interface actions.
        """
        # list of all actions
        self.__actions = []
        
        self.newTabAct = E5Action(
            self.tr('New Tab'),
            UI.PixmapCache.getIcon("tabNew.png"),
            self.tr('&New Tab'),
            QKeySequence(self.tr("Ctrl+T", "File|New Tab")),
            0, self, 'webbrowser_file_new_tab')
        self.newTabAct.setStatusTip(self.tr('Open a new web browser tab'))
        self.newTabAct.setWhatsThis(self.tr(
            """<b>New Tab</b>"""
            """<p>This opens a new web browser tab.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.newTabAct.triggered.connect(self.newTab)
        self.__actions.append(self.newTabAct)
        
        self.newAct = E5Action(
            self.tr('New Window'),
            UI.PixmapCache.getIcon("newWindow.png"),
            self.tr('New &Window'),
            QKeySequence(self.tr("Ctrl+N", "File|New Window")),
            0, self, 'webbrowser_file_new_window')
        self.newAct.setStatusTip(self.tr('Open a new web browser window'))
        self.newAct.setWhatsThis(self.tr(
            """<b>New Window</b>"""
            """<p>This opens a new web browser window in the current"""
            """ privacy mode.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.newAct.triggered.connect(self.newWindow)
        self.__actions.append(self.newAct)
        
        self.newPrivateAct = E5Action(
            self.tr('New Private Window'),
            UI.PixmapCache.getIcon("privateMode.png"),
            self.tr('New &Private Window'),
            QKeySequence(self.tr("Ctrl+Shift+P", "File|New Private Window")),
            0, self, 'webbrowser_file_new_private_window')
        self.newPrivateAct.setStatusTip(self.tr(
            'Open a new private web browser window'))
        self.newPrivateAct.setWhatsThis(self.tr(
            """<b>New Private Window</b>"""
            """<p>This opens a new private web browser window by starting"""
            """ a new web browser instance in private mode.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.newPrivateAct.triggered.connect(self.newPrivateWindow)
        self.__actions.append(self.newPrivateAct)
        
        self.openAct = E5Action(
            self.tr('Open File'),
            UI.PixmapCache.getIcon("open.png"),
            self.tr('&Open File'),
            QKeySequence(self.tr("Ctrl+O", "File|Open")),
            0, self, 'webbrowser_file_open')
        self.openAct.setStatusTip(self.tr('Open a file for display'))
        self.openAct.setWhatsThis(self.tr(
            """<b>Open File</b>"""
            """<p>This opens a new file for display."""
            """ It pops up a file selection dialog.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.openAct.triggered.connect(self.__openFile)
        self.__actions.append(self.openAct)
        
        self.openTabAct = E5Action(
            self.tr('Open File in New Tab'),
            UI.PixmapCache.getIcon("openNewTab.png"),
            self.tr('Open File in New &Tab'),
            QKeySequence(self.tr("Shift+Ctrl+O", "File|Open in new tab")),
            0, self, 'webbrowser_file_open_tab')
        self.openTabAct.setStatusTip(
            self.tr('Open a file for display in a new tab'))
        self.openTabAct.setWhatsThis(self.tr(
            """<b>Open File in New Tab</b>"""
            """<p>This opens a new file for display in a new tab."""
            """ It pops up a file selection dialog.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.openTabAct.triggered.connect(self.__openFileNewTab)
        self.__actions.append(self.openTabAct)
        
        if hasattr(QWebEnginePage, "SavePage"):
            self.saveAsAct = E5Action(
                self.tr('Save As'),
                UI.PixmapCache.getIcon("fileSaveAs.png"),
                self.tr('&Save As...'),
                QKeySequence(self.tr("Shift+Ctrl+S", "File|Save As")),
                0, self, 'webbrowser_file_save_as')
            self.saveAsAct.setStatusTip(
                self.tr('Save the current page to disk'))
            self.saveAsAct.setWhatsThis(self.tr(
                """<b>Save As...</b>"""
                """<p>Saves the current page to disk.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.saveAsAct.triggered.connect(self.__savePageAs)
            self.__actions.append(self.saveAsAct)
        else:
            self.saveAsAct = None
        
        self.savePageScreenAct = E5Action(
            self.tr('Save Page Screen'),
            UI.PixmapCache.getIcon("fileSavePixmap.png"),
            self.tr('Save Page Screen...'),
            0, 0, self, 'webbrowser_file_save_page_screen')
        self.savePageScreenAct.setStatusTip(
            self.tr('Save the current page as a screen shot'))
        self.savePageScreenAct.setWhatsThis(self.tr(
            """<b>Save Page Screen...</b>"""
            """<p>Saves the current page as a screen shot.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.savePageScreenAct.triggered.connect(self.__savePageScreen)
        self.__actions.append(self.savePageScreenAct)
        
        self.saveVisiblePageScreenAct = E5Action(
            self.tr('Save Visible Page Screen'),
            UI.PixmapCache.getIcon("fileSaveVisiblePixmap.png"),
            self.tr('Save Visible Page Screen...'),
            0, 0, self, 'webbrowser_file_save_visible_page_screen')
        self.saveVisiblePageScreenAct.setStatusTip(
            self.tr('Save the visible part of the current page as a'
                    ' screen shot'))
        self.saveVisiblePageScreenAct.setWhatsThis(self.tr(
            """<b>Save Visible Page Screen...</b>"""
            """<p>Saves the visible part of the current page as a"""
            """ screen shot.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.saveVisiblePageScreenAct.triggered.connect(
                self.__saveVisiblePageScreen)
        self.__actions.append(self.saveVisiblePageScreenAct)
        
        bookmarksManager = self.bookmarksManager()
        self.importBookmarksAct = E5Action(
            self.tr('Import Bookmarks'),
            self.tr('&Import Bookmarks...'),
            0, 0, self, 'webbrowser_file_import_bookmarks')
        self.importBookmarksAct.setStatusTip(
            self.tr('Import bookmarks from other browsers'))
        self.importBookmarksAct.setWhatsThis(self.tr(
            """<b>Import Bookmarks</b>"""
            """<p>Import bookmarks from other browsers.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.importBookmarksAct.triggered.connect(
                bookmarksManager.importBookmarks)
        self.__actions.append(self.importBookmarksAct)
        
        self.exportBookmarksAct = E5Action(
            self.tr('Export Bookmarks'),
            self.tr('&Export Bookmarks...'),
            0, 0, self, 'webbrowser_file_export_bookmarks')
        self.exportBookmarksAct.setStatusTip(
            self.tr('Export the bookmarks into a file'))
        self.exportBookmarksAct.setWhatsThis(self.tr(
            """<b>Export Bookmarks</b>"""
            """<p>Export the bookmarks into a file.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.exportBookmarksAct.triggered.connect(
                bookmarksManager.exportBookmarks)
        self.__actions.append(self.exportBookmarksAct)
        
        # TODO: re-check this once printing on Windows is reliable
##        if qVersionTuple() >= (5, 8, 0) or (
##            not Globals.isWindowsPlatform() or qVersionTuple() >= (5, 7, 0)):
        if not Globals.isWindowsPlatform() and qVersionTuple() >= (5, 7, 0):
            self.printAct = E5Action(
                self.tr('Print'),
                UI.PixmapCache.getIcon("print.png"),
                self.tr('&Print'),
                QKeySequence(self.tr("Ctrl+P", "File|Print")),
                0, self, 'webbrowser_file_print')
            self.printAct.setStatusTip(self.tr('Print the displayed help'))
            self.printAct.setWhatsThis(self.tr(
                """<b>Print</b>"""
                """<p>Print the displayed help text.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.printAct.triggered.connect(self.__tabWidget.printBrowser)
            self.__actions.append(self.printAct)
        else:
            self.printAct = None
        
        if Globals.isLinuxPlatform() or qVersionTuple() >= (5, 7, 0):
            self.printPdfAct = E5Action(
                self.tr('Print as PDF'),
                UI.PixmapCache.getIcon("printPdf.png"),
                self.tr('Print as PDF'),
                0, 0, self, 'webbrowser_file_print_pdf')
            self.printPdfAct.setStatusTip(self.tr(
                'Print the displayed help as PDF'))
            self.printPdfAct.setWhatsThis(self.tr(
                """<b>Print as PDF</b>"""
                """<p>Print the displayed help text as a PDF file.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.printPdfAct.triggered.connect(
                    self.__tabWidget.printBrowserPdf)
            self.__actions.append(self.printPdfAct)
        else:
            self.printPdfAct = None
        
        # TODO: re-check this once printing on Windows is reliable
##        if qVersionTuple() >= (5, 8, 0) or (
##            not Globals.isWindowsPlatform() and qVersionTuple() < (5, 7, 0)):
        if not Globals.isWindowsPlatform() and (
                qVersionTuple() < (5, 7, 0) or qVersionTuple() >= (5, 8, 0)):
            self.printPreviewAct = E5Action(
                self.tr('Print Preview'),
                UI.PixmapCache.getIcon("printPreview.png"),
                self.tr('Print Preview'),
                0, 0, self, 'webbrowser_file_print_preview')
            self.printPreviewAct.setStatusTip(self.tr(
                'Print preview of the displayed help'))
            self.printPreviewAct.setWhatsThis(self.tr(
                """<b>Print Preview</b>"""
                """<p>Print preview of the displayed help text.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.printPreviewAct.triggered.connect(
                    self.__tabWidget.printPreviewBrowser)
            self.__actions.append(self.printPreviewAct)
        else:
            self.printPreviewAct = None
        
        self.sendPageLinkAct = E5Action(
            self.tr('Send Page Link'),
            UI.PixmapCache.getIcon("mailSend.png"),
            self.tr('Send Page Link'),
            0, 0, self, 'webbrowser_send_page_link')
        self.sendPageLinkAct.setStatusTip(self.tr(
            'Send the link of the current page via email'))
        self.sendPageLinkAct.setWhatsThis(self.tr(
            """<b>Send Page Link</b>"""
            """<p>Send the link of the current page via email.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.sendPageLinkAct.triggered.connect(self.__sendPageLink)
        self.__actions.append(self.sendPageLinkAct)
        
        self.closeAct = E5Action(
            self.tr('Close'),
            UI.PixmapCache.getIcon("close.png"),
            self.tr('&Close'),
            QKeySequence(self.tr("Ctrl+W", "File|Close")),
            0, self, 'webbrowser_file_close')
        self.closeAct.setStatusTip(self.tr(
            'Close the current help window'))
        self.closeAct.setWhatsThis(self.tr(
            """<b>Close</b>"""
            """<p>Closes the current web browser window.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.closeAct.triggered.connect(self.__tabWidget.closeBrowser)
        self.__actions.append(self.closeAct)
        
        self.closeAllAct = E5Action(
            self.tr('Close All'),
            self.tr('Close &All'),
            0, 0, self, 'webbrowser_file_close_all')
        self.closeAllAct.setStatusTip(self.tr('Close all help windows'))
        self.closeAllAct.setWhatsThis(self.tr(
            """<b>Close All</b>"""
            """<p>Closes all web browser windows except the first one.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.closeAllAct.triggered.connect(
                self.__tabWidget.closeAllBrowsers)
        self.__actions.append(self.closeAllAct)
        
        self.exitAct = E5Action(
            self.tr('Quit'),
            UI.PixmapCache.getIcon("exit.png"),
            self.tr('&Quit'),
            QKeySequence(self.tr("Ctrl+Q", "File|Quit")),
            0, self, 'webbrowser_file_quit')
        self.exitAct.setStatusTip(self.tr('Quit the eric6 Web Browser'))
        self.exitAct.setWhatsThis(self.tr(
            """<b>Quit</b>"""
            """<p>Quit the eric6 Web Browser.</p>"""
        ))
        if not self.__initShortcutsOnly:
            if self.__fromEric:
                self.exitAct.triggered.connect(self.close)
            else:
                self.exitAct.triggered.connect(self.shutdown)
        self.__actions.append(self.exitAct)
        
        self.backAct = E5Action(
            self.tr('Backward'),
            UI.PixmapCache.getIcon("back.png"),
            self.tr('&Backward'),
            QKeySequence(self.tr("Alt+Left", "Go|Backward")),
            0, self, 'webbrowser_go_backward')
        self.backAct.setStatusTip(self.tr('Move one screen backward'))
        self.backAct.setWhatsThis(self.tr(
            """<b>Backward</b>"""
            """<p>Moves one screen backward. If none is"""
            """ available, this action is disabled.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.backAct.triggered.connect(self.__backward)
        self.__actions.append(self.backAct)
        
        self.forwardAct = E5Action(
            self.tr('Forward'),
            UI.PixmapCache.getIcon("forward.png"),
            self.tr('&Forward'),
            QKeySequence(self.tr("Alt+Right", "Go|Forward")),
            0, self, 'webbrowser_go_foreward')
        self.forwardAct.setStatusTip(self.tr(
            'Move one screen forward'))
        self.forwardAct.setWhatsThis(self.tr(
            """<b>Forward</b>"""
            """<p>Moves one screen forward. If none is"""
            """ available, this action is disabled.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.forwardAct.triggered.connect(self.__forward)
        self.__actions.append(self.forwardAct)
        
        self.homeAct = E5Action(
            self.tr('Home'),
            UI.PixmapCache.getIcon("home.png"),
            self.tr('&Home'),
            QKeySequence(self.tr("Ctrl+Home", "Go|Home")),
            0, self, 'webbrowser_go_home')
        self.homeAct.setStatusTip(self.tr(
            'Move to the initial screen'))
        self.homeAct.setWhatsThis(self.tr(
            """<b>Home</b>"""
            """<p>Moves to the initial screen.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.homeAct.triggered.connect(self.__home)
        self.__actions.append(self.homeAct)
        
        self.reloadAct = E5Action(
            self.tr('Reload'),
            UI.PixmapCache.getIcon("reload.png"),
            self.tr('&Reload'),
            QKeySequence(self.tr("Ctrl+R", "Go|Reload")),
            QKeySequence(self.tr("F5", "Go|Reload")),
            self, 'webbrowser_go_reload')
        self.reloadAct.setStatusTip(self.tr(
            'Reload the current screen'))
        self.reloadAct.setWhatsThis(self.tr(
            """<b>Reload</b>"""
            """<p>Reloads the current screen.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.reloadAct.triggered.connect(self.__reload)
        self.__actions.append(self.reloadAct)
        
        self.stopAct = E5Action(
            self.tr('Stop'),
            UI.PixmapCache.getIcon("stopLoading.png"),
            self.tr('&Stop'),
            QKeySequence(self.tr("Ctrl+.", "Go|Stop")),
            QKeySequence(self.tr("Esc", "Go|Stop")),
            self, 'webbrowser_go_stop')
        self.stopAct.setStatusTip(self.tr('Stop loading'))
        self.stopAct.setWhatsThis(self.tr(
            """<b>Stop</b>"""
            """<p>Stops loading of the current tab.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.stopAct.triggered.connect(self.__stopLoading)
        self.__actions.append(self.stopAct)
        
        self.copyAct = E5Action(
            self.tr('Copy'),
            UI.PixmapCache.getIcon("editCopy.png"),
            self.tr('&Copy'),
            QKeySequence(self.tr("Ctrl+C", "Edit|Copy")),
            0, self, 'webbrowser_edit_copy')
        self.copyAct.setStatusTip(self.tr('Copy the selected text'))
        self.copyAct.setWhatsThis(self.tr(
            """<b>Copy</b>"""
            """<p>Copy the selected text to the clipboard.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.copyAct.triggered.connect(self.__copy)
        self.__actions.append(self.copyAct)
        
        self.cutAct = E5Action(
            self.tr('Cut'),
            UI.PixmapCache.getIcon("editCut.png"),
            self.tr('Cu&t'),
            QKeySequence(self.tr("Ctrl+X", "Edit|Cut")),
            0, self, 'webbrowser_edit_cut')
        self.cutAct.setStatusTip(self.tr('Cut the selected text'))
        self.cutAct.setWhatsThis(self.tr(
            """<b>Cut</b>"""
            """<p>Cut the selected text to the clipboard.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.cutAct.triggered.connect(self.__cut)
        self.__actions.append(self.cutAct)
        
        self.pasteAct = E5Action(
            self.tr('Paste'),
            UI.PixmapCache.getIcon("editPaste.png"),
            self.tr('&Paste'),
            QKeySequence(self.tr("Ctrl+V", "Edit|Paste")),
            0, self, 'webbrowser_edit_paste')
        self.pasteAct.setStatusTip(self.tr('Paste text from the clipboard'))
        self.pasteAct.setWhatsThis(self.tr(
            """<b>Paste</b>"""
            """<p>Paste some text from the clipboard.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.pasteAct.triggered.connect(self.__paste)
        self.__actions.append(self.pasteAct)
        
        self.undoAct = E5Action(
            self.tr('Undo'),
            UI.PixmapCache.getIcon("editUndo.png"),
            self.tr('&Undo'),
            QKeySequence(self.tr("Ctrl+Z", "Edit|Undo")),
            0, self, 'webbrowser_edit_undo')
        self.undoAct.setStatusTip(self.tr('Undo the last edit action'))
        self.undoAct.setWhatsThis(self.tr(
            """<b>Undo</b>"""
            """<p>Undo the last edit action.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.undoAct.triggered.connect(self.__undo)
        self.__actions.append(self.undoAct)
        
        self.redoAct = E5Action(
            self.tr('Redo'),
            UI.PixmapCache.getIcon("editRedo.png"),
            self.tr('&Redo'),
            QKeySequence(self.tr("Ctrl+Shift+Z", "Edit|Redo")),
            0, self, 'webbrowser_edit_redo')
        self.redoAct.setStatusTip(self.tr('Redo the last edit action'))
        self.redoAct.setWhatsThis(self.tr(
            """<b>Redo</b>"""
            """<p>Redo the last edit action.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.redoAct.triggered.connect(self.__redo)
        self.__actions.append(self.redoAct)
        
        self.selectAllAct = E5Action(
            self.tr('Select All'),
            UI.PixmapCache.getIcon("editSelectAll.png"),
            self.tr('&Select All'),
            QKeySequence(self.tr("Ctrl+A", "Edit|Select All")),
            0, self, 'webbrowser_edit_select_all')
        self.selectAllAct.setStatusTip(self.tr('Select all text'))
        self.selectAllAct.setWhatsThis(self.tr(
            """<b>Select All</b>"""
            """<p>Select all text of the current browser.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.selectAllAct.triggered.connect(self.__selectAll)
        self.__actions.append(self.selectAllAct)
        
        self.unselectAct = E5Action(
            self.tr('Unselect'),
            self.tr('Unselect'),
            QKeySequence(self.tr("Alt+Ctrl+A", "Edit|Unselect")),
            0, self, 'webbrowser_edit_unselect')
        self.unselectAct.setStatusTip(self.tr('Clear current selection'))
        self.unselectAct.setWhatsThis(self.tr(
            """<b>Unselect</b>"""
            """<p>Clear the selection of the current browser.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.unselectAct.triggered.connect(self.__unselect)
        self.__actions.append(self.unselectAct)
        
        self.findAct = E5Action(
            self.tr('Find...'),
            UI.PixmapCache.getIcon("find.png"),
            self.tr('&Find...'),
            QKeySequence(self.tr("Ctrl+F", "Edit|Find")),
            0, self, 'webbrowser_edit_find')
        self.findAct.setStatusTip(self.tr('Find text in page'))
        self.findAct.setWhatsThis(self.tr(
            """<b>Find</b>"""
            """<p>Find text in the current page.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.findAct.triggered.connect(self.__find)
        self.__actions.append(self.findAct)
        
        self.findNextAct = E5Action(
            self.tr('Find next'),
            UI.PixmapCache.getIcon("findNext.png"),
            self.tr('Find &next'),
            QKeySequence(self.tr("F3", "Edit|Find next")),
            0, self, 'webbrowser_edit_find_next')
        self.findNextAct.setStatusTip(self.tr(
            'Find next occurrence of text in page'))
        self.findNextAct.setWhatsThis(self.tr(
            """<b>Find next</b>"""
            """<p>Find the next occurrence of text in the current page.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.findNextAct.triggered.connect(self.__searchWidget.findNext)
        self.__actions.append(self.findNextAct)
        
        self.findPrevAct = E5Action(
            self.tr('Find previous'),
            UI.PixmapCache.getIcon("findPrev.png"),
            self.tr('Find &previous'),
            QKeySequence(self.tr("Shift+F3", "Edit|Find previous")),
            0, self, 'webbrowser_edit_find_previous')
        self.findPrevAct.setStatusTip(
            self.tr('Find previous occurrence of text in page'))
        self.findPrevAct.setWhatsThis(self.tr(
            """<b>Find previous</b>"""
            """<p>Find the previous occurrence of text in the current"""
            """ page.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.findPrevAct.triggered.connect(
                self.__searchWidget.findPrevious)
        self.__actions.append(self.findPrevAct)
        
        self.bookmarksManageAct = E5Action(
            self.tr('Manage Bookmarks'),
            self.tr('&Manage Bookmarks...'),
            QKeySequence(self.tr("Ctrl+Shift+B", "Help|Manage bookmarks")),
            0, self, 'webbrowser_bookmarks_manage')
        self.bookmarksManageAct.setStatusTip(self.tr(
            'Open a dialog to manage the bookmarks.'))
        self.bookmarksManageAct.setWhatsThis(self.tr(
            """<b>Manage Bookmarks...</b>"""
            """<p>Open a dialog to manage the bookmarks.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.bookmarksManageAct.triggered.connect(
                self.__showBookmarksDialog)
        self.__actions.append(self.bookmarksManageAct)
        
        self.bookmarksAddAct = E5Action(
            self.tr('Add Bookmark'),
            UI.PixmapCache.getIcon("addBookmark.png"),
            self.tr('Add &Bookmark...'),
            QKeySequence(self.tr("Ctrl+D", "Help|Add bookmark")),
            0, self, 'webbrowser_bookmark_add')
        self.bookmarksAddAct.setIconVisibleInMenu(False)
        self.bookmarksAddAct.setStatusTip(self.tr(
            'Open a dialog to add a bookmark.'))
        self.bookmarksAddAct.setWhatsThis(self.tr(
            """<b>Add Bookmark</b>"""
            """<p>Open a dialog to add the current URL as a bookmark.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.bookmarksAddAct.triggered.connect(self.__addBookmark)
        self.__actions.append(self.bookmarksAddAct)
        
        self.bookmarksAddFolderAct = E5Action(
            self.tr('Add Folder'),
            self.tr('Add &Folder...'),
            0, 0, self, 'webbrowser_bookmark_show_all')
        self.bookmarksAddFolderAct.setStatusTip(self.tr(
            'Open a dialog to add a new bookmarks folder.'))
        self.bookmarksAddFolderAct.setWhatsThis(self.tr(
            """<b>Add Folder...</b>"""
            """<p>Open a dialog to add a new bookmarks folder.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.bookmarksAddFolderAct.triggered.connect(
                self.__addBookmarkFolder)
        self.__actions.append(self.bookmarksAddFolderAct)
        
        self.bookmarksAllTabsAct = E5Action(
            self.tr('Bookmark All Tabs'),
            self.tr('Bookmark All Tabs...'),
            0, 0, self, 'webbrowser_bookmark_all_tabs')
        self.bookmarksAllTabsAct.setStatusTip(self.tr(
            'Bookmark all open tabs.'))
        self.bookmarksAllTabsAct.setWhatsThis(self.tr(
            """<b>Bookmark All Tabs...</b>"""
            """<p>Open a dialog to add a new bookmarks folder for"""
            """ all open tabs.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.bookmarksAllTabsAct.triggered.connect(self.bookmarkAll)
        self.__actions.append(self.bookmarksAllTabsAct)
        
        self.whatsThisAct = E5Action(
            self.tr('What\'s This?'),
            UI.PixmapCache.getIcon("whatsThis.png"),
            self.tr('&What\'s This?'),
            QKeySequence(self.tr("Shift+F1", "Help|What's This?'")),
            0, self, 'webbrowser_help_whats_this')
        self.whatsThisAct.setStatusTip(self.tr('Context sensitive help'))
        self.whatsThisAct.setWhatsThis(self.tr(
            """<b>Display context sensitive help</b>"""
            """<p>In What's This? mode, the mouse cursor shows an arrow"""
            """ with a question mark, and you can click on the interface"""
            """ elements to get a short description of what they do and how"""
            """ to use them. In dialogs, this feature can be accessed using"""
            """ the context help button in the titlebar.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.whatsThisAct.triggered.connect(self.__whatsThis)
        self.__actions.append(self.whatsThisAct)
        
        self.aboutAct = E5Action(
            self.tr('About'),
            self.tr('&About'),
            0, 0, self, 'webbrowser_help_about')
        self.aboutAct.setStatusTip(self.tr(
            'Display information about this software'))
        self.aboutAct.setWhatsThis(self.tr(
            """<b>About</b>"""
            """<p>Display some information about this software.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.aboutAct.triggered.connect(self.__about)
        self.__actions.append(self.aboutAct)
        
        self.aboutQtAct = E5Action(
            self.tr('About Qt'),
            self.tr('About &Qt'),
            0, 0, self, 'webbrowser_help_about_qt')
        self.aboutQtAct.setStatusTip(
            self.tr('Display information about the Qt toolkit'))
        self.aboutQtAct.setWhatsThis(self.tr(
            """<b>About Qt</b>"""
            """<p>Display some information about the Qt toolkit.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.aboutQtAct.triggered.connect(self.__aboutQt)
        self.__actions.append(self.aboutQtAct)
        
        self.zoomInAct = E5Action(
            self.tr('Zoom in'),
            UI.PixmapCache.getIcon("zoomIn.png"),
            self.tr('Zoom &in'),
            QKeySequence(self.tr("Ctrl++", "View|Zoom in")),
            QKeySequence(self.tr("Zoom In", "View|Zoom in")),
            self, 'webbrowser_view_zoom_in')
        self.zoomInAct.setStatusTip(self.tr('Zoom in on the web page'))
        self.zoomInAct.setWhatsThis(self.tr(
            """<b>Zoom in</b>"""
            """<p>Zoom in on the web page."""
            """ This makes the web page bigger.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.zoomInAct.triggered.connect(self.__zoomIn)
        self.__actions.append(self.zoomInAct)
        
        self.zoomOutAct = E5Action(
            self.tr('Zoom out'),
            UI.PixmapCache.getIcon("zoomOut.png"),
            self.tr('Zoom &out'),
            QKeySequence(self.tr("Ctrl+-", "View|Zoom out")),
            QKeySequence(self.tr("Zoom Out", "View|Zoom out")),
            self, 'webbrowser_view_zoom_out')
        self.zoomOutAct.setStatusTip(self.tr('Zoom out on the web page'))
        self.zoomOutAct.setWhatsThis(self.tr(
            """<b>Zoom out</b>"""
            """<p>Zoom out on the web page."""
            """ This makes the web page smaller.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.zoomOutAct.triggered.connect(self.__zoomOut)
        self.__actions.append(self.zoomOutAct)
        
        self.zoomResetAct = E5Action(
            self.tr('Zoom reset'),
            UI.PixmapCache.getIcon("zoomReset.png"),
            self.tr('Zoom &reset'),
            QKeySequence(self.tr("Ctrl+0", "View|Zoom reset")),
            0, self, 'webbrowser_view_zoom_reset')
        self.zoomResetAct.setStatusTip(self.tr(
            'Reset the zoom of the web page'))
        self.zoomResetAct.setWhatsThis(self.tr(
            """<b>Zoom reset</b>"""
            """<p>Reset the zoom of the web page. """
            """This sets the zoom factor to 100%.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.zoomResetAct.triggered.connect(self.__zoomReset)
        self.__actions.append(self.zoomResetAct)
        
        self.pageSourceAct = E5Action(
            self.tr('Show page source'),
            self.tr('Show page source'),
            QKeySequence(self.tr('Ctrl+U')), 0,
            self, 'webbrowser_show_page_source')
        self.pageSourceAct.setStatusTip(self.tr(
            'Show the page source in an editor'))
        self.pageSourceAct.setWhatsThis(self.tr(
            """<b>Show page source</b>"""
            """<p>Show the page source in an editor.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.pageSourceAct.triggered.connect(self.__showPageSource)
        self.__actions.append(self.pageSourceAct)
        self.addAction(self.pageSourceAct)
        
        self.fullScreenAct = E5Action(
            self.tr('Full Screen'),
            UI.PixmapCache.getIcon("windowFullscreen.png"),
            self.tr('&Full Screen'),
            0, 0,
            self, 'webbrowser_view_full_screen')
        if Globals.isMacPlatform():
            self.fullScreenAct.setShortcut(
                QKeySequence(self.tr("Meta+Ctrl+F")))
        else:
            self.fullScreenAct.setShortcut(QKeySequence(self.tr('F11')))
        if not self.__initShortcutsOnly:
            self.fullScreenAct.triggered.connect(self.toggleFullScreen)
        self.__actions.append(self.fullScreenAct)
        self.addAction(self.fullScreenAct)
        
        self.nextTabAct = E5Action(
            self.tr('Show next tab'),
            self.tr('Show next tab'),
            QKeySequence(self.tr('Ctrl+Alt+Tab')), 0,
            self, 'webbrowser_view_next_tab')
        if not self.__initShortcutsOnly:
            self.nextTabAct.triggered.connect(self.__nextTab)
        self.__actions.append(self.nextTabAct)
        self.addAction(self.nextTabAct)
        
        self.prevTabAct = E5Action(
            self.tr('Show previous tab'),
            self.tr('Show previous tab'),
            QKeySequence(self.tr('Shift+Ctrl+Alt+Tab')), 0,
            self, 'webbrowser_view_previous_tab')
        if not self.__initShortcutsOnly:
            self.prevTabAct.triggered.connect(self.__prevTab)
        self.__actions.append(self.prevTabAct)
        self.addAction(self.prevTabAct)
        
        self.switchTabAct = E5Action(
            self.tr('Switch between tabs'),
            self.tr('Switch between tabs'),
            QKeySequence(self.tr('Ctrl+1')), 0,
            self, 'webbrowser_switch_tabs')
        if not self.__initShortcutsOnly:
            self.switchTabAct.triggered.connect(self.__switchTab)
        self.__actions.append(self.switchTabAct)
        self.addAction(self.switchTabAct)
        
        self.prefAct = E5Action(
            self.tr('Preferences'),
            UI.PixmapCache.getIcon("configure.png"),
            self.tr('&Preferences...'), 0, 0, self, 'webbrowser_preferences')
        self.prefAct.setStatusTip(self.tr(
            'Set the prefered configuration'))
        self.prefAct.setWhatsThis(self.tr(
            """<b>Preferences</b>"""
            """<p>Set the configuration items of the application"""
            """ with your prefered values.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.prefAct.triggered.connect(self.__showPreferences)
        self.__actions.append(self.prefAct)
        
        self.acceptedLanguagesAct = E5Action(
            self.tr('Languages'),
            UI.PixmapCache.getIcon("flag.png"),
            self.tr('&Languages...'), 0, 0,
            self, 'webbrowser_accepted_languages')
        self.acceptedLanguagesAct.setStatusTip(self.tr(
            'Configure the accepted languages for web pages'))
        self.acceptedLanguagesAct.setWhatsThis(self.tr(
            """<b>Languages</b>"""
            """<p>Configure the accepted languages for web pages.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.acceptedLanguagesAct.triggered.connect(
                self.__showAcceptedLanguages)
        self.__actions.append(self.acceptedLanguagesAct)
        
        self.cookiesAct = E5Action(
            self.tr('Cookies'),
            UI.PixmapCache.getIcon("cookie.png"),
            self.tr('C&ookies...'), 0, 0, self, 'webbrowser_cookies')
        self.cookiesAct.setStatusTip(self.tr(
            'Configure cookies handling'))
        self.cookiesAct.setWhatsThis(self.tr(
            """<b>Cookies</b>"""
            """<p>Configure cookies handling.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.cookiesAct.triggered.connect(
                self.__showCookiesConfiguration)
        self.__actions.append(self.cookiesAct)
        
        self.flashCookiesAct = E5Action(
            self.tr('Flash Cookies'),
            UI.PixmapCache.getIcon("flashCookie.png"),
            self.tr('&Flash Cookies...'), 0, 0, self,
            'webbrowser_flash_cookies')
        self.flashCookiesAct.setStatusTip(self.tr(
            'Manage flash cookies'))
        self.flashCookiesAct.setWhatsThis(self.tr(
            """<b>Flash Cookies</b>"""
            """<p>Show a dialog to manage the flash cookies.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.flashCookiesAct.triggered.connect(
                self.__showFlashCookiesManagement)
        self.__actions.append(self.flashCookiesAct)
        
        self.personalDataAct = E5Action(
            self.tr('Personal Information'),
            UI.PixmapCache.getIcon("pim.png"),
            self.tr('Personal Information...'),
            0, 0,
            self, 'webbrowser_personal_information')
        self.personalDataAct.setStatusTip(self.tr(
            'Configure personal information for completing form fields'))
        self.personalDataAct.setWhatsThis(self.tr(
            """<b>Personal Information...</b>"""
            """<p>Opens a dialog to configure the personal information"""
            """ used for completing form fields.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.personalDataAct.triggered.connect(
                self.__showPersonalInformationDialog)
        self.__actions.append(self.personalDataAct)
        
        self.greaseMonkeyAct = E5Action(
            self.tr('GreaseMonkey Scripts'),
            UI.PixmapCache.getIcon("greaseMonkey.png"),
            self.tr('GreaseMonkey Scripts...'),
            0, 0,
            self, 'webbrowser_greasemonkey')
        self.greaseMonkeyAct.setStatusTip(self.tr(
            'Configure the GreaseMonkey Scripts'))
        self.greaseMonkeyAct.setWhatsThis(self.tr(
            """<b>GreaseMonkey Scripts...</b>"""
            """<p>Opens a dialog to configure the available GreaseMonkey"""
            """ Scripts.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.greaseMonkeyAct.triggered.connect(
                self.__showGreaseMonkeyConfigDialog)
        self.__actions.append(self.greaseMonkeyAct)
        
        self.editMessageFilterAct = E5Action(
            self.tr('Edit Message Filters'),
            UI.PixmapCache.getIcon("warning.png"),
            self.tr('Edit Message Filters...'), 0, 0, self,
            'webbrowser_manage_message_filters')
        self.editMessageFilterAct.setStatusTip(self.tr(
            'Edit the message filters used to suppress unwanted messages'))
        self.editMessageFilterAct.setWhatsThis(self.tr(
            """<b>Edit Message Filters</b>"""
            """<p>Opens a dialog to edit the message filters used to"""
            """ suppress unwanted messages been shown in an error"""
            """ window.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.editMessageFilterAct.triggered.connect(
                E5ErrorMessage.editMessageFilters)
        self.__actions.append(self.editMessageFilterAct)
        
        self.featurePermissionAct = E5Action(
            self.tr('Edit HTML5 Feature Permissions'),
            UI.PixmapCache.getIcon("featurePermission.png"),
            self.tr('Edit HTML5 Feature Permissions...'), 0, 0, self,
            'webbrowser_edit_feature_permissions')
        self.featurePermissionAct.setStatusTip(self.tr(
            'Edit the remembered HTML5 feature permissions'))
        self.featurePermissionAct.setWhatsThis(self.tr(
            """<b>Edit HTML5 Feature Permissions</b>"""
            """<p>Opens a dialog to edit the remembered HTML5"""
            """ feature permissions.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.featurePermissionAct.triggered.connect(
                self.__showFeaturePermissionDialog)
        self.__actions.append(self.featurePermissionAct)
        
        if WebBrowserWindow._useQtHelp or self.__initShortcutsOnly:
            self.syncTocAct = E5Action(
                self.tr('Sync with Table of Contents'),
                UI.PixmapCache.getIcon("syncToc.png"),
                self.tr('Sync with Table of Contents'),
                0, 0, self, 'webbrowser_sync_toc')
            self.syncTocAct.setStatusTip(self.tr(
                'Synchronizes the table of contents with current page'))
            self.syncTocAct.setWhatsThis(self.tr(
                """<b>Sync with Table of Contents</b>"""
                """<p>Synchronizes the table of contents with current"""
                """ page.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.syncTocAct.triggered.connect(self.__syncTOC)
            self.__actions.append(self.syncTocAct)
            
            self.showTocAct = E5Action(
                self.tr('Table of Contents'),
                self.tr('Table of Contents'),
                0, 0, self, 'webbrowser_show_toc')
            self.showTocAct.setStatusTip(self.tr(
                'Shows the table of contents window'))
            self.showTocAct.setWhatsThis(self.tr(
                """<b>Table of Contents</b>"""
                """<p>Shows the table of contents window.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.showTocAct.triggered.connect(self.__showTocWindow)
            self.__actions.append(self.showTocAct)
            
            self.showIndexAct = E5Action(
                self.tr('Index'),
                self.tr('Index'),
                0, 0, self, 'webbrowser_show_index')
            self.showIndexAct.setStatusTip(self.tr(
                'Shows the index window'))
            self.showIndexAct.setWhatsThis(self.tr(
                """<b>Index</b>"""
                """<p>Shows the index window.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.showIndexAct.triggered.connect(self.__showIndexWindow)
            self.__actions.append(self.showIndexAct)
            
            self.showSearchAct = E5Action(
                self.tr('Search'),
                self.tr('Search'),
                0, 0, self, 'webbrowser_show_search')
            self.showSearchAct.setStatusTip(self.tr(
                'Shows the search window'))
            self.showSearchAct.setWhatsThis(self.tr(
                """<b>Search</b>"""
                """<p>Shows the search window.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.showSearchAct.triggered.connect(
                    self.__showSearchWindow)
            self.__actions.append(self.showSearchAct)
            
            self.manageQtHelpDocsAct = E5Action(
                self.tr('Manage QtHelp Documents'),
                self.tr('Manage QtHelp &Documents'),
                0, 0, self, 'webbrowser_qthelp_documents')
            self.manageQtHelpDocsAct.setStatusTip(self.tr(
                'Shows a dialog to manage the QtHelp documentation set'))
            self.manageQtHelpDocsAct.setWhatsThis(self.tr(
                """<b>Manage QtHelp Documents</b>"""
                """<p>Shows a dialog to manage the QtHelp documentation"""
                """ set.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.manageQtHelpDocsAct.triggered.connect(
                    self.__manageQtHelpDocumentation)
            self.__actions.append(self.manageQtHelpDocsAct)
            
            self.manageQtHelpFiltersAct = E5Action(
                self.tr('Manage QtHelp Filters'),
                self.tr('Manage QtHelp &Filters'),
                0, 0, self, 'webbrowser_qthelp_filters')
            self.manageQtHelpFiltersAct.setStatusTip(self.tr(
                'Shows a dialog to manage the QtHelp filters'))
            self.manageQtHelpFiltersAct.setWhatsThis(self.tr(
                """<b>Manage QtHelp Filters</b>"""
                """<p>Shows a dialog to manage the QtHelp filters.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.manageQtHelpFiltersAct.triggered.connect(
                    self.__manageQtHelpFilters)
            self.__actions.append(self.manageQtHelpFiltersAct)
            
            self.reindexDocumentationAct = E5Action(
                self.tr('Reindex Documentation'),
                self.tr('&Reindex Documentation'),
                0, 0, self, 'webbrowser_qthelp_reindex')
            self.reindexDocumentationAct.setStatusTip(self.tr(
                'Reindexes the documentation set'))
            self.reindexDocumentationAct.setWhatsThis(self.tr(
                """<b>Reindex Documentation</b>"""
                """<p>Reindexes the documentation set.</p>"""
            ))
            if not self.__initShortcutsOnly:
                self.reindexDocumentationAct.triggered.connect(
                    self.__searchEngine.reindexDocumentation)
            self.__actions.append(self.reindexDocumentationAct)
        
        self.clearPrivateDataAct = E5Action(
            self.tr('Clear private data'),
            UI.PixmapCache.getIcon("clearPrivateData.png"),
            self.tr('Clear private data'),
            0, 0,
            self, 'webbrowser_clear_private_data')
        self.clearPrivateDataAct.setStatusTip(self.tr(
            'Clear private data'))
        self.clearPrivateDataAct.setWhatsThis(self.tr(
            """<b>Clear private data</b>"""
            """<p>Clears the private data like browsing history, search"""
            """ history or the favicons database.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.clearPrivateDataAct.triggered.connect(
                self.__clearPrivateData)
        self.__actions.append(self.clearPrivateDataAct)
        
        self.clearIconsAct = E5Action(
            self.tr('Clear icons database'),
            self.tr('Clear &icons database'),
            0, 0,
            self, 'webbrowser_clear_icons_db')
        self.clearIconsAct.setStatusTip(self.tr(
            'Clear the database of favicons'))
        self.clearIconsAct.setWhatsThis(self.tr(
            """<b>Clear icons database</b>"""
            """<p>Clears the database of favicons of previously visited"""
            """ URLs.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.clearIconsAct.triggered.connect(self.__clearIconsDatabase)
        self.__actions.append(self.clearIconsAct)
        
        self.manageIconsAct = E5Action(
            self.tr('Manage saved Favicons'),
            UI.PixmapCache.getIcon("icons.png"),
            self.tr('Manage saved Favicons'),
            0, 0,
            self, 'webbrowser_manage_icons_db')
        self.manageIconsAct.setStatusTip(self.tr(
            'Show a dialog to manage the saved favicons'))
        self.manageIconsAct.setWhatsThis(self.tr(
            """<b>Manage saved Favicons</b>"""
            """<p>This shows a dialog to manage the saved favicons of"""
            """ previously visited URLs.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.manageIconsAct.triggered.connect(self.__showWebIconsDialog)
        self.__actions.append(self.manageIconsAct)
        
        self.searchEnginesAct = E5Action(
            self.tr('Configure Search Engines'),
            self.tr('Configure Search &Engines...'),
            0, 0,
            self, 'webbrowser_search_engines')
        self.searchEnginesAct.setStatusTip(self.tr(
            'Configure the available search engines'))
        self.searchEnginesAct.setWhatsThis(self.tr(
            """<b>Configure Search Engines...</b>"""
            """<p>Opens a dialog to configure the available search"""
            """ engines.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.searchEnginesAct.triggered.connect(
                self.__showEnginesConfigurationDialog)
        self.__actions.append(self.searchEnginesAct)
        
        self.passwordsAct = E5Action(
            self.tr('Manage Saved Passwords'),
            UI.PixmapCache.getIcon("passwords.png"),
            self.tr('Manage Saved Passwords...'),
            0, 0,
            self, 'webbrowser_manage_passwords')
        self.passwordsAct.setStatusTip(self.tr(
            'Manage the saved passwords'))
        self.passwordsAct.setWhatsThis(self.tr(
            """<b>Manage Saved Passwords...</b>"""
            """<p>Opens a dialog to manage the saved passwords.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.passwordsAct.triggered.connect(self.__showPasswordsDialog)
        self.__actions.append(self.passwordsAct)
        
        self.adblockAct = E5Action(
            self.tr('Ad Block'),
            UI.PixmapCache.getIcon("adBlockPlus.png"),
            self.tr('&Ad Block...'),
            0, 0,
            self, 'webbrowser_adblock')
        self.adblockAct.setStatusTip(self.tr(
            'Configure AdBlock subscriptions and rules'))
        self.adblockAct.setWhatsThis(self.tr(
            """<b>Ad Block...</b>"""
            """<p>Opens a dialog to configure AdBlock subscriptions and"""
            """ rules.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.adblockAct.triggered.connect(self.__showAdBlockDialog)
        self.__actions.append(self.adblockAct)
        
        self.certificateErrorsAct = E5Action(
            self.tr('Manage SSL Certificate Errors'),
            UI.PixmapCache.getIcon("certificates.png"),
            self.tr('Manage SSL Certificate Errors...'),
            0, 0,
            self, 'webbrowser_manage_certificate_errors')
        self.certificateErrorsAct.setStatusTip(self.tr(
            'Manage the accepted SSL certificate Errors'))
        self.certificateErrorsAct.setWhatsThis(self.tr(
            """<b>Manage SSL Certificate Errors...</b>"""
            """<p>Opens a dialog to manage the accepted SSL"""
            """ certificate errors.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.certificateErrorsAct.triggered.connect(
                self.__showCertificateErrorsDialog)
        self.__actions.append(self.certificateErrorsAct)
        
        self.showDownloadManagerAct = E5Action(
            self.tr('Downloads'),
            self.tr('Downloads'),
            0, 0, self, 'webbrowser_show_downloads')
        self.showDownloadManagerAct.setStatusTip(self.tr(
            'Shows the downloads window'))
        self.showDownloadManagerAct.setWhatsThis(self.tr(
            """<b>Downloads</b>"""
            """<p>Shows the downloads window.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.showDownloadManagerAct.triggered.connect(
                self.__showDownloadsWindow)
        self.__actions.append(self.showDownloadManagerAct)
        
        self.feedsManagerAct = E5Action(
            self.tr('RSS Feeds Dialog'),
            UI.PixmapCache.getIcon("rss22.png"),
            self.tr('&RSS Feeds Dialog...'),
            QKeySequence(self.tr("Ctrl+Shift+F", "Help|RSS Feeds Dialog")),
            0, self, 'webbrowser_rss_feeds')
        self.feedsManagerAct.setStatusTip(self.tr(
            'Open a dialog showing the configured RSS feeds.'))
        self.feedsManagerAct.setWhatsThis(self.tr(
            """<b>RSS Feeds Dialog...</b>"""
            """<p>Open a dialog to show the configured RSS feeds."""
            """ It can be used to mange the feeds and to show their"""
            """ contents.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.feedsManagerAct.triggered.connect(self.__showFeedsManager)
        self.__actions.append(self.feedsManagerAct)
        
        self.siteInfoAct = E5Action(
            self.tr('Siteinfo Dialog'),
            UI.PixmapCache.getIcon("helpAbout.png"),
            self.tr('&Siteinfo Dialog...'),
            QKeySequence(self.tr("Ctrl+Shift+I", "Help|Siteinfo Dialog")),
            0, self, 'webbrowser_siteinfo')
        self.siteInfoAct.setStatusTip(self.tr(
            'Open a dialog showing some information about the current site.'))
        self.siteInfoAct.setWhatsThis(self.tr(
            """<b>Siteinfo Dialog...</b>"""
            """<p>Opens a dialog showing some information about the current"""
            """ site.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.siteInfoAct.triggered.connect(self.__showSiteinfoDialog)
        self.__actions.append(self.siteInfoAct)
        
        self.userAgentManagerAct = E5Action(
            self.tr('Manage User Agent Settings'),
            self.tr('Manage &User Agent Settings'),
            0, 0, self, 'webbrowser_user_agent_settings')
        self.userAgentManagerAct.setStatusTip(self.tr(
            'Shows a dialog to manage the User Agent settings'))
        self.userAgentManagerAct.setWhatsThis(self.tr(
            """<b>Manage User Agent Settings</b>"""
            """<p>Shows a dialog to manage the User Agent settings.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.userAgentManagerAct.triggered.connect(
                self.__showUserAgentsDialog)
        self.__actions.append(self.userAgentManagerAct)
        
        self.synchronizationAct = E5Action(
            self.tr('Synchronize data'),
            UI.PixmapCache.getIcon("sync.png"),
            self.tr('&Synchronize Data...'),
            0, 0, self, 'webbrowser_synchronize_data')
        self.synchronizationAct.setStatusTip(self.tr(
            'Shows a dialog to synchronize data via the network'))
        self.synchronizationAct.setWhatsThis(self.tr(
            """<b>Synchronize Data...</b>"""
            """<p>This shows a dialog to synchronize data via the"""
            """ network.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.synchronizationAct.triggered.connect(
                self.__showSyncDialog)
        self.__actions.append(self.synchronizationAct)
        
        self.zoomValuesAct = E5Action(
            self.tr('Manage Saved Zoom Values'),
            UI.PixmapCache.getIcon("zoomReset.png"),
            self.tr('Manage Saved Zoom Values...'),
            0, 0,
            self, 'webbrowser_manage_zoom_values')
        self.zoomValuesAct.setStatusTip(self.tr(
            'Manage the saved zoom values'))
        self.zoomValuesAct.setWhatsThis(self.tr(
            """<b>Manage Saved Zoom Values...</b>"""
            """<p>Opens a dialog to manage the saved zoom values.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.zoomValuesAct.triggered.connect(self.__showZoomValuesDialog)
        self.__actions.append(self.zoomValuesAct)
        
        self.showJavaScriptConsoleAct = E5Action(
            self.tr('JavaScript Console'),
            self.tr('JavaScript Console'),
            0, 0, self, 'webbrowser_show_javascript_console')
        self.showJavaScriptConsoleAct.setStatusTip(self.tr(
            'Toggle the JavaScript console window'))
        self.showJavaScriptConsoleAct.setWhatsThis(self.tr(
            """<b>JavaScript Console</b>"""
            """<p>This toggles the JavaScript console window.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.showJavaScriptConsoleAct.triggered.connect(
                self.__toggleJavaScriptConsole)
        self.__actions.append(self.showJavaScriptConsoleAct)
        
        self.showTabManagerAct = E5Action(
            self.tr('Tab Manager'),
            self.tr('Tab Manager'),
            0, 0, self, 'webbrowser_show_tab_manager')
        self.showTabManagerAct.setStatusTip(self.tr(
            'Shows the tab manager window'))
        self.showTabManagerAct.setWhatsThis(self.tr(
            """<b>Tab Manager</b>"""
            """<p>Shows the tab manager window.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.showTabManagerAct.triggered.connect(self.__showTabManager)
        self.__actions.append(self.showTabManagerAct)
        
        self.showSessionsManagerAct = E5Action(
            self.tr('Session Manager'),
            self.tr('Session Manager...'),
            0, 0, self, 'webbrowser_show_session_manager')
        self.showSessionsManagerAct.setStatusTip(self.tr(
            'Shows the session manager window'))
        self.showSessionsManagerAct.setWhatsThis(self.tr(
            """<b>Session Manager</b>"""
            """<p>Shows the session manager window.</p>"""
        ))
        if not self.__initShortcutsOnly:
            self.showSessionsManagerAct.triggered.connect(
                self.__showSessionManagerDialog)
        self.__actions.append(self.showSessionsManagerAct)
        
        self.virustotalScanCurrentAct = E5Action(
            self.tr("Scan current site"),
            UI.PixmapCache.getIcon("virustotal.png"),
            self.tr("Scan current site"),
            0, 0,
            self, 'webbrowser_virustotal_scan_site')
        if not self.__initShortcutsOnly:
            self.virustotalScanCurrentAct.triggered.connect(
                self.__virusTotalScanCurrentSite)
        self.__actions.append(self.virustotalScanCurrentAct)
        
        self.virustotalIpReportAct = E5Action(
            self.tr("IP Address Report"),
            UI.PixmapCache.getIcon("virustotal.png"),
            self.tr("IP Address Report"),
            0, 0,
            self, 'webbrowser_virustotal_ip_report')
        if not self.__initShortcutsOnly:
            self.virustotalIpReportAct.triggered.connect(
                self.__virusTotalIpAddressReport)
        self.__actions.append(self.virustotalIpReportAct)
        
        self.virustotalDomainReportAct = E5Action(
            self.tr("Domain Report"),
            UI.PixmapCache.getIcon("virustotal.png"),
            self.tr("Domain Report"),
            0, 0,
            self, 'webbrowser_virustotal_domain_report')
        if not self.__initShortcutsOnly:
            self.virustotalDomainReportAct.triggered.connect(
                self.__virusTotalDomainReport)
        self.__actions.append(self.virustotalDomainReportAct)
        
        if not Preferences.getWebBrowser("VirusTotalEnabled") or \
           Preferences.getWebBrowser("VirusTotalServiceKey") == "":
            self.virustotalScanCurrentAct.setEnabled(False)
            self.virustotalIpReportAct.setEnabled(False)
            self.virustotalDomainReportAct.setEnabled(False)
        
        self.backAct.setEnabled(False)
        self.forwardAct.setEnabled(False)
        
        # now read the keyboard shortcuts for the actions
        Shortcuts.readShortcuts(
            helpViewer=self, helpViewerCategory="webBrowser")
    
    def getActions(self):
        """
        Public method to get a list of all actions.
        
        @return list of all actions (list of E5Action)
        """
        return self.__actions[:]
        
    def __initMenus(self):
        """
        Private method to create the menus.
        """
        mb = self.menuBar()
        
        menu = mb.addMenu(self.tr('&File'))
        menu.addAction(self.newTabAct)
        menu.addAction(self.newAct)
        menu.addAction(self.newPrivateAct)
        menu.addAction(self.openAct)
        menu.addAction(self.openTabAct)
        menu.addSeparator()
        if not self.isPrivate():
            sessionsMenu = menu.addMenu(self.tr("Sessions"))
            sessionsMenu.aboutToShow.connect(
                self.sessionManager().aboutToShowSessionsMenu)
            menu.addAction(self.showSessionsManagerAct)
            menu.addSeparator()
        if self.saveAsAct is not None:
            menu.addAction(self.saveAsAct)
        menu.addAction(self.savePageScreenAct)
        menu.addAction(self.saveVisiblePageScreenAct)
        menu.addSeparator()
        if self.printPreviewAct:
            menu.addAction(self.printPreviewAct)
        if self.printAct:
            menu.addAction(self.printAct)
        if self.printPdfAct:
            menu.addAction(self.printPdfAct)
        menu.addAction(self.sendPageLinkAct)
        menu.addSeparator()
        menu.addAction(self.closeAct)
        menu.addAction(self.closeAllAct)
        menu.addSeparator()
        menu.addAction(self.exitAct)
        self.addActions(menu.actions())
        
        menu = mb.addMenu(self.tr('&Edit'))
        menu.addAction(self.undoAct)
        menu.addAction(self.redoAct)
        menu.addSeparator()
        menu.addAction(self.copyAct)
        menu.addAction(self.cutAct)
        menu.addAction(self.pasteAct)
        menu.addSeparator()
        menu.addAction(self.selectAllAct)
        menu.addAction(self.unselectAct)
        menu.addSeparator()
        menu.addAction(self.findAct)
        menu.addAction(self.findNextAct)
        menu.addAction(self.findPrevAct)
        self.addActions(menu.actions())
        
        menu = mb.addMenu(self.tr('&View'))
        menu.addAction(self.stopAct)
        menu.addAction(self.reloadAct)
        if WebBrowserWindow._useQtHelp:
            menu.addSeparator()
            menu.addAction(self.syncTocAct)
        menu.addSeparator()
        menu.addAction(self.zoomInAct)
        menu.addAction(self.zoomResetAct)
        menu.addAction(self.zoomOutAct)
        menu.addSeparator()
        self.__textEncodingMenu = menu.addMenu(
            self.tr("Text Encoding"))
        self.__textEncodingMenu.aboutToShow.connect(
            self.__aboutToShowTextEncodingMenu)
        self.__textEncodingMenu.triggered.connect(self.__setTextEncoding)
        menu.addSeparator()
        menu.addAction(self.pageSourceAct)
        menu.addAction(self.fullScreenAct)
        self.addActions(menu.actions())
        
        from .History.HistoryMenu import HistoryMenu
        self.historyMenu = HistoryMenu(self, self.__tabWidget)
        self.historyMenu.setTitle(self.tr('H&istory'))
        self.historyMenu.openUrl.connect(self.openUrl)
        self.historyMenu.newTab.connect(self.openUrlNewTab)
        self.historyMenu.newBackgroundTab.connect(self.openUrlNewBackgroundTab)
        self.historyMenu.newWindow.connect(self.openUrlNewWindow)
        self.historyMenu.newPrivateWindow.connect(self.openUrlNewPrivateWindow)
        mb.addMenu(self.historyMenu)
        
        historyActions = []
        historyActions.append(self.backAct)
        historyActions.append(self.forwardAct)
        historyActions.append(self.homeAct)
        self.historyMenu.setInitialActions(historyActions)
        self.addActions(historyActions)
        
        from .Bookmarks.BookmarksMenu import BookmarksMenuBarMenu
        self.bookmarksMenu = BookmarksMenuBarMenu(self)
        self.bookmarksMenu.setTitle(self.tr('&Bookmarks'))
        self.bookmarksMenu.openUrl.connect(self.openUrl)
        self.bookmarksMenu.newTab.connect(self.openUrlNewTab)
        self.bookmarksMenu.newWindow.connect(self.openUrlNewWindow)
        mb.addMenu(self.bookmarksMenu)
        
        bookmarksActions = []
        bookmarksActions.append(self.bookmarksManageAct)
        bookmarksActions.append(self.bookmarksAddAct)
        bookmarksActions.append(self.bookmarksAllTabsAct)
        bookmarksActions.append(self.bookmarksAddFolderAct)
        bookmarksActions.append("--SEPARATOR--")
        bookmarksActions.append(self.importBookmarksAct)
        bookmarksActions.append(self.exportBookmarksAct)
        self.bookmarksMenu.setInitialActions(bookmarksActions)
        
        menu = mb.addMenu(self.tr('&Settings'))
        menu.addAction(self.prefAct)
        menu.addAction(self.acceptedLanguagesAct)
        menu.addAction(self.cookiesAct)
        menu.addAction(self.flashCookiesAct)
        menu.addAction(self.personalDataAct)
        menu.addAction(self.greaseMonkeyAct)
        menu.addAction(self.featurePermissionAct)
        menu.addSeparator()
        menu.addAction(self.editMessageFilterAct)
        menu.addSeparator()
        menu.addAction(self.searchEnginesAct)
        menu.addSeparator()
        menu.addAction(self.passwordsAct)
        menu.addAction(self.certificateErrorsAct)
        menu.addSeparator()
        menu.addAction(self.zoomValuesAct)
        menu.addAction(self.manageIconsAct)
        menu.addSeparator()
        menu.addAction(self.adblockAct)
        menu.addSeparator()
        self.__settingsMenu = menu
        self.__settingsMenu.aboutToShow.connect(
            self.__aboutToShowSettingsMenu)
        
        from .UserAgent.UserAgentMenu import UserAgentMenu
        self.__userAgentMenu = UserAgentMenu(self.tr("Global User Agent"))
        menu.addMenu(self.__userAgentMenu)
        menu.addAction(self.userAgentManagerAct)
        menu.addSeparator()
        
        if WebBrowserWindow._useQtHelp:
            menu.addAction(self.manageQtHelpDocsAct)
            menu.addAction(self.manageQtHelpFiltersAct)
            menu.addAction(self.reindexDocumentationAct)
            menu.addSeparator()
        menu.addAction(self.clearPrivateDataAct)
        menu.addAction(self.clearIconsAct)
        
        menu = mb.addMenu(self.tr("&Tools"))
        menu.addAction(self.feedsManagerAct)
        menu.addAction(self.siteInfoAct)
        menu.addSeparator()
        menu.addAction(self.synchronizationAct)
        menu.addSeparator()
        vtMenu = menu.addMenu(UI.PixmapCache.getIcon("virustotal.png"),
                              self.tr("&VirusTotal"))
        vtMenu.addAction(self.virustotalScanCurrentAct)
        vtMenu.addAction(self.virustotalIpReportAct)
        vtMenu.addAction(self.virustotalDomainReportAct)
        
        menu = mb.addMenu(self.tr("&Windows"))
        menu.addAction(self.showDownloadManagerAct)
        menu.addAction(self.showJavaScriptConsoleAct)
        menu.addAction(self.showTabManagerAct)
        if WebBrowserWindow._useQtHelp:
            menu.addSeparator()
            menu.addAction(self.showTocAct)
            menu.addAction(self.showIndexAct)
            menu.addAction(self.showSearchAct)
        menu.addSeparator()
        self.__toolbarsMenu = menu.addMenu(self.tr("&Toolbars"))
        self.__toolbarsMenu.aboutToShow.connect(self.__showToolbarsMenu)
        self.__toolbarsMenu.triggered.connect(self.__TBMenuTriggered)
        
        mb.addSeparator()
        
        menu = mb.addMenu(self.tr('&Help'))
        menu.addAction(self.aboutAct)
        menu.addAction(self.aboutQtAct)
        menu.addSeparator()
        menu.addAction(self.whatsThisAct)
        self.addActions(menu.actions())
    
    def __initSuperMenu(self):
        """
        Private method to create the super menu and attach it to the super
        menu button.
        """
        self.__superMenu = QMenu(self)
        
        self.__superMenu.addAction(self.newTabAct)
        self.__superMenu.addAction(self.newAct)
        self.__superMenu.addAction(self.newPrivateAct)
        self.__superMenu.addAction(self.openAct)
        self.__superMenu.addAction(self.openTabAct)
        self.__superMenu.addSeparator()
        
        if not self.isPrivate():
            sessionsMenu = self.__superMenu.addMenu(self.tr("Sessions"))
            sessionsMenu.aboutToShow.connect(
                self.sessionManager().aboutToShowSessionsMenu)
            self.__superMenu.addAction(self.showSessionsManagerAct)
            self.__superMenu.addSeparator()
        
        menu = self.__superMenu.addMenu(self.tr("Save"))
        if self.saveAsAct:
            menu.addAction(self.saveAsAct)
        menu.addAction(self.savePageScreenAct)
        menu.addAction(self.saveVisiblePageScreenAct)
        
        if self.printPreviewAct or self.printAct or self.printPdfAct:
            menu = self.__superMenu.addMenu(self.tr("Print"))
            if self.printPreviewAct:
                menu.addAction(self.printPreviewAct)
            if self.printAct:
                menu.addAction(self.printAct)
            if self.printPdfAct:
                menu.addAction(self.printPdfAct)
        
        self.__superMenu.addAction(self.sendPageLinkAct)
        self.__superMenu.addSeparator()
        self.__superMenu.addAction(self.selectAllAct)
        self.__superMenu.addAction(self.findAct)
        self.__superMenu.addSeparator()
        act = self.__superMenu.addAction(UI.PixmapCache.getIcon("history.png"),
                                         self.tr("Show All History..."))
        act.triggered.connect(self.historyMenu.showHistoryDialog)
        self.__superMenu.addAction(self.bookmarksManageAct)
        self.__superMenu.addSeparator()
        self.__superMenu.addAction(self.prefAct)
        
        menu = self.__superMenu.addMenu(self.tr('Settings'))
        menu.addAction(self.acceptedLanguagesAct)
        menu.addAction(self.cookiesAct)
        menu.addAction(self.flashCookiesAct)
        menu.addAction(self.personalDataAct)
        menu.addAction(self.greaseMonkeyAct)
        menu.addAction(self.featurePermissionAct)
        menu.addSeparator()
        menu.addAction(self.editMessageFilterAct)
        menu.addSeparator()
        menu.addAction(self.searchEnginesAct)
        menu.addSeparator()
        menu.addAction(self.passwordsAct)
        menu.addAction(self.certificateErrorsAct)
        menu.addSeparator()
        menu.addAction(self.zoomValuesAct)
        menu.addAction(self.manageIconsAct)
        menu.addSeparator()
        menu.addAction(self.adblockAct)
        menu.addSeparator()
        menu.addMenu(self.__userAgentMenu)
        menu.addAction(self.userAgentManagerAct)
        menu.addSeparator()
        if WebBrowserWindow._useQtHelp:
            menu.addAction(self.manageQtHelpDocsAct)
            menu.addAction(self.manageQtHelpFiltersAct)
            menu.addAction(self.reindexDocumentationAct)
            menu.addSeparator()
        menu.addAction(self.clearPrivateDataAct)
        menu.addAction(self.clearIconsAct)
        menu.aboutToShow.connect(
            self.__aboutToShowSettingsMenu)

        self.__superMenu.addSeparator()
        
        menu = self.__superMenu.addMenu(self.tr('&View'))
        menu.addMenu(self.__toolbarsMenu)
        windowsMenu = menu.addMenu(self.tr("&Windows"))
        windowsMenu.addAction(self.showDownloadManagerAct)
        windowsMenu.addAction(self.showJavaScriptConsoleAct)
        windowsMenu.addAction(self.showTabManagerAct)
        if WebBrowserWindow._useQtHelp:
            windowsMenu.addSeparator()
            windowsMenu.addAction(self.showTocAct)
            windowsMenu.addAction(self.showIndexAct)
            windowsMenu.addAction(self.showSearchAct)
        menu.addSeparator()
        menu.addAction(self.stopAct)
        menu.addAction(self.reloadAct)
        if WebBrowserWindow._useQtHelp:
            menu.addSeparator()
            menu.addAction(self.syncTocAct)
        menu.addSeparator()
        menu.addAction(self.zoomInAct)
        menu.addAction(self.zoomResetAct)
        menu.addAction(self.zoomOutAct)
        menu.addSeparator()
        menu.addMenu(self.__textEncodingMenu)
        menu.addSeparator()
        menu.addAction(self.pageSourceAct)
        menu.addAction(self.fullScreenAct)
        
        self.__superMenu.addMenu(self.historyMenu)
        self.__superMenu.addMenu(self.bookmarksMenu)
        
        menu = self.__superMenu.addMenu(self.tr("&Tools"))
        menu.addAction(self.feedsManagerAct)
        menu.addAction(self.siteInfoAct)
        menu.addSeparator()
        menu.addAction(self.synchronizationAct)
        menu.addSeparator()
        vtMenu = menu.addMenu(UI.PixmapCache.getIcon("virustotal.png"),
                              self.tr("&VirusTotal"))
        vtMenu.addAction(self.virustotalScanCurrentAct)
        vtMenu.addAction(self.virustotalIpReportAct)
        vtMenu.addAction(self.virustotalDomainReportAct)
        
        self.__superMenu.addSeparator()
        self.__superMenu.addAction(self.aboutAct)
        self.__superMenu.addAction(self.aboutQtAct)
        self.__superMenu.addSeparator()
        self.__superMenu.addAction(self.exitAct)
        
        self.__navigationBar.superMenuButton().setMenu(self.__superMenu)
    
    def __initToolbars(self):
        """
        Private method to create the toolbars.
        """
        filetb = self.addToolBar(self.tr("File"))
        filetb.setObjectName("FileToolBar")
        filetb.setIconSize(UI.Config.ToolBarIconSize)
        filetb.addAction(self.newTabAct)
        filetb.addAction(self.newAct)
        filetb.addAction(self.newPrivateAct)
        filetb.addAction(self.openAct)
        filetb.addAction(self.openTabAct)
        filetb.addSeparator()
        if self.saveAsAct is not None:
            filetb.addAction(self.saveAsAct)
        filetb.addAction(self.savePageScreenAct)
        filetb.addSeparator()
        if self.printPreviewAct:
            filetb.addAction(self.printPreviewAct)
        if self.printAct:
            filetb.addAction(self.printAct)
        if self.printPdfAct:
            filetb.addAction(self.printPdfAct)
        if self.printPreviewAct or self.printAct or self.printPdfAct:
            filetb.addSeparator()
        filetb.addAction(self.closeAct)
        filetb.addAction(self.exitAct)
        self.__toolbars["file"] = (filetb.windowTitle(), filetb)
        
        self.savePageScreenMenu = QMenu(self)
        self.savePageScreenMenu.addAction(self.savePageScreenAct)
        self.savePageScreenMenu.addAction(self.saveVisiblePageScreenAct)
        savePageScreenButton = filetb.widgetForAction(self.savePageScreenAct)
        savePageScreenButton.setMenu(self.savePageScreenMenu)
        savePageScreenButton.setPopupMode(QToolButton.MenuButtonPopup)
        
        edittb = self.addToolBar(self.tr("Edit"))
        edittb.setObjectName("EditToolBar")
        edittb.setIconSize(UI.Config.ToolBarIconSize)
        edittb.addAction(self.undoAct)
        edittb.addAction(self.redoAct)
        edittb.addSeparator()
        edittb.addAction(self.copyAct)
        edittb.addAction(self.cutAct)
        edittb.addAction(self.pasteAct)
        edittb.addSeparator()
        edittb.addAction(self.selectAllAct)
        self.__toolbars["edit"] = (edittb.windowTitle(), edittb)
        
        viewtb = self.addToolBar(self.tr("View"))
        viewtb.setObjectName("ViewToolBar")
        viewtb.setIconSize(UI.Config.ToolBarIconSize)
        viewtb.addAction(self.zoomInAct)
        viewtb.addAction(self.zoomResetAct)
        viewtb.addAction(self.zoomOutAct)
        viewtb.addSeparator()
        viewtb.addAction(self.fullScreenAct)
        self.__toolbars["view"] = (viewtb.windowTitle(), viewtb)
        
        findtb = self.addToolBar(self.tr("Find"))
        findtb.setObjectName("FindToolBar")
        findtb.setIconSize(UI.Config.ToolBarIconSize)
        findtb.addAction(self.findAct)
        findtb.addAction(self.findNextAct)
        findtb.addAction(self.findPrevAct)
        self.__toolbars["find"] = (findtb.windowTitle(), findtb)
        
        if WebBrowserWindow._useQtHelp:
            filtertb = self.addToolBar(self.tr("Filter"))
            filtertb.setObjectName("FilterToolBar")
            self.filterCombo = QComboBox()
            self.filterCombo.setMinimumWidth(
                QFontMetrics(QFont()).width("ComboBoxWithEnoughWidth"))
            filtertb.addWidget(QLabel(self.tr("Filtered by: ")))
            filtertb.addWidget(self.filterCombo)
            self.__helpEngine.setupFinished.connect(self.__setupFilterCombo)
            self.filterCombo.activated[str].connect(
                self.__filterQtHelpDocumentation)
            self.__setupFilterCombo()
            self.__toolbars["filter"] = (filtertb.windowTitle(), filtertb)
        
        settingstb = self.addToolBar(self.tr("Settings"))
        settingstb.setObjectName("SettingsToolBar")
        settingstb.setIconSize(UI.Config.ToolBarIconSize)
        settingstb.addAction(self.prefAct)
        settingstb.addAction(self.acceptedLanguagesAct)
        settingstb.addAction(self.cookiesAct)
        settingstb.addAction(self.flashCookiesAct)
        settingstb.addAction(self.personalDataAct)
        settingstb.addAction(self.greaseMonkeyAct)
        settingstb.addAction(self.featurePermissionAct)
        self.__toolbars["settings"] = (settingstb.windowTitle(), settingstb)
        
        toolstb = self.addToolBar(self.tr("Tools"))
        toolstb.setObjectName("ToolsToolBar")
        toolstb.setIconSize(UI.Config.ToolBarIconSize)
        toolstb.addAction(self.feedsManagerAct)
        toolstb.addAction(self.siteInfoAct)
        toolstb.addSeparator()
        toolstb.addAction(self.synchronizationAct)
        self.__toolbars["tools"] = (toolstb.windowTitle(), toolstb)
        
        helptb = self.addToolBar(self.tr("Help"))
        helptb.setObjectName("HelpToolBar")
        helptb.setIconSize(UI.Config.ToolBarIconSize)
        helptb.addAction(self.whatsThisAct)
        self.__toolbars["help"] = (helptb.windowTitle(), helptb)
        
        self.addToolBarBreak()
        vttb = self.addToolBar(self.tr("VirusTotal"))
        vttb.setObjectName("VirusTotalToolBar")
        vttb.setIconSize(UI.Config.ToolBarIconSize)
        vttb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        vttb.addAction(self.virustotalScanCurrentAct)
        vttb.addAction(self.virustotalIpReportAct)
        vttb.addAction(self.virustotalDomainReportAct)
        self.__toolbars["virustotal"] = (vttb.windowTitle(), vttb)
        
    def __nextTab(self):
        """
        Private slot used to show the next tab.
        """
        fwidget = QApplication.focusWidget()
        while fwidget and not hasattr(fwidget, 'nextTab'):
            fwidget = fwidget.parent()
        if fwidget:
            fwidget.nextTab()
        
    def __prevTab(self):
        """
        Private slot used to show the previous tab.
        """
        fwidget = QApplication.focusWidget()
        while fwidget and not hasattr(fwidget, 'prevTab'):
            fwidget = fwidget.parent()
        if fwidget:
            fwidget.prevTab()
        
    def __switchTab(self):
        """
        Private slot used to switch between the current and the previous
        current tab.
        """
        fwidget = QApplication.focusWidget()
        while fwidget and not hasattr(fwidget, 'switchTab'):
            fwidget = fwidget.parent()
        if fwidget:
            fwidget.switchTab()
        
    def __whatsThis(self):
        """
        Private slot called in to enter Whats This mode.
        """
        QWhatsThis.enterWhatsThisMode()
        
    def __titleChanged(self, browser, title):
        """
        Private slot called to handle a change of a browser's title.
        
        @param browser reference to the browser (WebBrowserView)
        @param title new title (string)
        """
        self.historyManager().updateHistoryEntry(
            browser.url().toString(), title)
    
    @pyqtSlot()
    def newTab(self, link=None, addNextTo=None, background=False):
        """
        Public slot called to open a new web browser tab.
        
        @param link file to be displayed in the new window (string or QUrl)
        @param addNextTo reference to the browser to open the tab after
            (WebBrowserView)
        @keyparam background flag indicating to open the tab in the
            background (bool)
        @return reference to the new browser
        @rtype WebBrowserView
        """
        if addNextTo:
            return self.__tabWidget.newBrowserAfter(
                addNextTo, link, background=background)
        else:
            return self.__tabWidget.newBrowser(link, background=background)
    
    @pyqtSlot()
    def newWindow(self, link=None, restoreSession=False):
        """
        Public slot called to open a new web browser window.
        
        @param link URL to be displayed in the new window
        @type str or QUrl
        @param restoreSession flag indicating a restore session action
        @type bool
        @return reference to the new window
        @rtype WebBrowserWindow
        """
        if link is None:
            linkName = ""
        elif isinstance(link, QUrl):
            linkName = link.toString()
        else:
            linkName = link
        h = WebBrowserWindow(linkName, ".", self.parent(), "webbrowser",
                             self.__fromEric, private=self.isPrivate(),
                             restoreSession=restoreSession)
        h.show()
        
        self.webBrowserWindowOpened.emit(h)
        
        return h
    
    @pyqtSlot()
    def newPrivateWindow(self, link=None):
        """
        Public slot called to open a new private web browser window.
        
        @param link URL to be displayed in the new window
        @type str or QUrl
        """
        if link is None:
            linkName = ""
        elif isinstance(link, QUrl):
            linkName = link.toString()
        else:
            linkName = link
        
        applPath = os.path.join(getConfig("ericDir"), "eric6_browser.py")
        args = []
        args.append(applPath)
        args.append("--config={0}".format(Utilities.getConfigDir()))
        if self.__settingsDir:
            args.append("--settings={0}".format(self.__settingsDir))
        args.append("--private")
        if linkName:
            args.append(linkName)
        
        if not os.path.isfile(applPath) or \
                not QProcess.startDetached(sys.executable, args):
            E5MessageBox.critical(
                self,
                self.tr('New Private Window'),
                self.tr(
                    '<p>Could not start the process.<br>'
                    'Ensure that it is available as <b>{0}</b>.</p>'
                ).format(applPath),
                self.tr('OK'))
    
    def __openFile(self):
        """
        Private slot called to open a file.
        """
        fn = E5FileDialog.getOpenFileName(
            self,
            self.tr("Open File"),
            "",
            self.tr("HTML Files (*.html *.htm *.mhtml *.mht);;"
                    "PDF Files (*.pdf);;"
                    "CHM Files (*.chm);;"
                    "All Files (*)"
                    ))
        if fn:
            if Utilities.isWindowsPlatform():
                url = "file:///" + Utilities.fromNativeSeparators(fn)
            else:
                url = "file://" + fn
            self.currentBrowser().setSource(QUrl(url))
        
    def __openFileNewTab(self):
        """
        Private slot called to open a file in a new tab.
        """
        fn = E5FileDialog.getOpenFileName(
            self,
            self.tr("Open File"),
            "",
            self.tr("HTML Files (*.html *.htm *.mhtml *.mht);;"
                    "PDF Files (*.pdf);;"
                    "CHM Files (*.chm);;"
                    "All Files (*)"
                    ))
        if fn:
            if Utilities.isWindowsPlatform():
                url = "file:///" + Utilities.fromNativeSeparators(fn)
            else:
                url = "file://" + fn
            self.newTab(url)
        
    def __savePageAs(self):
        """
        Private slot to save the current page.
        """
        browser = self.currentBrowser()
        if browser is not None:
            browser.saveAs()
    
    @pyqtSlot()
    def __savePageScreen(self, visibleOnly=False):
        """
        Private slot to save the current page as a screen shot.
        
        @param visibleOnly flag indicating to just save the visible part
            of the page (boolean)
        """
        from .PageScreenDialog import PageScreenDialog
        self.__pageScreen = PageScreenDialog(
            self.currentBrowser(), visibleOnly=visibleOnly)
        self.__pageScreen.show()
        
    @pyqtSlot()
    def __saveVisiblePageScreen(self):
        """
        Private slot to save the visible part of the current page as a screen
        shot.
        """
        self.__savePageScreen(visibleOnly=True)
        
    def __about(self):
        """
        Private slot to show the about information.
        """
        chromeVersion, webengineVersion = \
            WebBrowserTools.getWebEngineVersions()
        E5MessageBox.about(
            self,
            self.tr("eric6 Web Browser"),
            self.tr(
                """<b>eric6 Web Browser - {0}</b>"""
                """<p>The eric6 Web Browser is a combined help file and HTML"""
                """ browser. It is part of the eric6 development"""
                """ toolset.</p>"""
                """<p>It is based on QtWebEngine {1} and Chrome {2}.</p>"""
            ).format(Version, webengineVersion, chromeVersion))
        
    def __aboutQt(self):
        """
        Private slot to show info about Qt.
        """
        E5MessageBox.aboutQt(self, self.tr("eric6 Web Browser"))

    def setBackwardAvailable(self, b):
        """
        Public slot called when backward references are available.
        
        @param b flag indicating availability of the backwards action (boolean)
        """
        self.backAct.setEnabled(b)
        self.__navigationBar.backButton().setEnabled(b)
        
    def setForwardAvailable(self, b):
        """
        Public slot called when forward references are available.
        
        @param b flag indicating the availability of the forwards action
            (boolean)
        """
        self.forwardAct.setEnabled(b)
        self.__navigationBar.forwardButton().setEnabled(b)
        
    def setLoadingActions(self, b):
        """
        Public slot to set the loading dependent actions.
        
        @param b flag indicating the loading state to consider (boolean)
        """
        self.reloadAct.setEnabled(not b)
        self.stopAct.setEnabled(b)
        
        self.__navigationBar.reloadStopButton().setLoading(b)
        
    def __addBookmark(self):
        """
        Private slot called to add the displayed file to the bookmarks.
        """
        from .WebBrowserPage import WebBrowserPage
        
        view = self.currentBrowser()
        view.addBookmark()
        urlStr = bytes(view.url().toEncoded()).decode()
        title = view.title()
        
        script = Scripts.getAllMetaAttributes()
        view.page().runJavaScript(
            script,
            WebBrowserPage.SafeJsWorld,
            lambda res: self.__addBookmarkCallback(urlStr, title, res))
    
    def __addBookmarkCallback(self, url, title, res):
        """
        Private callback method of __addBookmark().
        
        @param url URL for the bookmark
        @type str
        @param title title for the bookmark
        @type str
        @param res result of the JavaScript
        @type list
        """
        description = ""
        for meta in res:
            if meta["name"] == "description":
                description = meta["content"]
        
        from .Bookmarks.AddBookmarkDialog import AddBookmarkDialog
        dlg = AddBookmarkDialog()
        dlg.setUrl(url)
        dlg.setTitle(title)
        dlg.setDescription(description)
        menu = self.bookmarksManager().menu()
        idx = self.bookmarksManager().bookmarksModel().nodeIndex(menu)
        dlg.setCurrentIndex(idx)
        dlg.exec_()
        
    def __addBookmarkFolder(self):
        """
        Private slot to add a new bookmarks folder.
        """
        from .Bookmarks.AddBookmarkDialog import AddBookmarkDialog
        dlg = AddBookmarkDialog()
        menu = self.bookmarksManager().menu()
        idx = self.bookmarksManager().bookmarksModel().nodeIndex(menu)
        dlg.setCurrentIndex(idx)
        dlg.setFolder(True)
        dlg.exec_()
        
    def __showBookmarksDialog(self):
        """
        Private slot to show the bookmarks dialog.
        """
        from .Bookmarks.BookmarksDialog import BookmarksDialog
        self.__bookmarksDialog = BookmarksDialog(self)
        self.__bookmarksDialog.openUrl.connect(self.openUrl)
        self.__bookmarksDialog.newTab.connect(self.openUrlNewTab)
        self.__bookmarksDialog.newBackgroundTab.connect(
            self.openUrlNewBackgroundTab)
        self.__bookmarksDialog.show()
        
    def bookmarkAll(self):
        """
        Public slot to bookmark all open tabs.
        """
        from .WebBrowserPage import WebBrowserPage
        from .Bookmarks.AddBookmarkDialog import AddBookmarkDialog
        
        dlg = AddBookmarkDialog()
        dlg.setFolder(True)
        dlg.setTitle(self.tr("Saved Tabs"))
        dlg.exec_()
        
        folder = dlg.addedNode()
        if folder is None:
            return
        
        for view in self.__tabWidget.browsers():
            urlStr = bytes(view.url().toEncoded()).decode()
            title = view.title()
            
            script = Scripts.getAllMetaAttributes()
            view.page().runJavaScript(
                script,
                WebBrowserPage.SafeJsWorld,
                lambda res: self.__bookmarkAllCallback(folder, urlStr,
                                                       title, res))
    
    def __bookmarkAllCallback(self, folder, url, title, res):
        """
        Private callback method of __addBookmark().
        
        @param folder reference to the bookmarks folder
        @type BookmarkNode
        @param url URL for the bookmark
        @type str
        @param title title for the bookmark
        @type str
        @param res result of the JavaScript
        @type list
        """
        description = ""
        for meta in res:
            if meta["name"] == "description":
                description = meta["content"]
        
        from .Bookmarks.BookmarkNode import BookmarkNode
        bookmark = BookmarkNode(BookmarkNode.Bookmark)
        bookmark.url = url
        bookmark.title = title
        bookmark.desc = description
        
        self.bookmarksManager().addBookmark(folder, bookmark)
        
    def __find(self):
        """
        Private slot to handle the find action.
        
        It opens the search dialog in order to perform the various
        search actions and to collect the various search info.
        """
        self.__searchWidget.showFind()
        
    def forceClose(self):
        """
        Public method to force closing the window.
        """
        self.__forcedClose = True
        self.close()
    
    def closeEvent(self, e):
        """
        Protected event handler for the close event.
        
        @param e the close event (QCloseEvent)
            <br />This event is simply accepted after the history has been
            saved and all window references have been deleted.
        """
        res = self.__shutdownWindow()
        
        if res:
            e.accept()
            self.webBrowserWindowClosed.emit(self)
        else:
            e.ignore()
    
    def isClosing(self):
        """
        Public method to test, if the window is closing.
        
        @return flag indicating that the window is closing
        @rtype bool
        """
        return self.__isClosing
    
    def __shutdownWindow(self):
        """
        Private method to shut down a web browser window.
        
        @return flag indicating successful shutdown (boolean)
        """
        if not WebBrowserWindow._performingShutdown and not self.__forcedClose:
            if not self.__tabWidget.shallShutDown():
                return False
        
        self.__isClosing = True
        
        if not self.__fromEric:
            if not WebBrowserWindow._performingShutdown and \
                    len(WebBrowserWindow.BrowserWindows) == 1:
                # shut down the session manager in case the last window is
                # about to be closed
                self.sessionManager().shutdown()
        
        self.__bookmarksToolBar.setModel(None)
        
        self.__virusTotal.close()
        
        self.__navigationBar.searchEdit().openSearchManager().close()
        
        if WebBrowserWindow._useQtHelp:
            self.__searchEngine.cancelIndexing()
            self.__searchEngine.cancelSearching()
            
            if self.__helpInstaller:
                self.__helpInstaller.stop()
        
        self.__navigationBar.searchEdit().saveSearches()
        
        self.__tabWidget.closeAllBrowsers(shutdown=True)
        
        state = self.saveState()
        Preferences.setWebBrowser("WebBrowserState", state)

        if Preferences.getWebBrowser("SaveGeometry"):
            if not self.isFullScreen():
                Preferences.setGeometry("WebBrowserGeometry",
                                        self.saveGeometry())
        else:
            Preferences.setGeometry("WebBrowserGeometry", QByteArray())
        
        try:
            if self.__fromEric or len(WebBrowserWindow.BrowserWindows) > 1:
                del WebBrowserWindow.BrowserWindows[
                    WebBrowserWindow.BrowserWindows.index(self)]
        except ValueError:
            pass
        
        if not self.__fromEric:
            Preferences.syncPreferences()
            if not WebBrowserWindow._performingShutdown and \
                    len(WebBrowserWindow.BrowserWindows) == 0:
                # shut down the browser in case the last window was
                # simply closed
                self.shutdown()
        
        return True
    
    def __shallShutDown(self):
        """
        Private method to check, if the application should be shut down.
        
        @return flag indicating a shut down
        @rtype bool
        """
        if Preferences.getWebBrowser("WarnOnMultipleClose"):
            windowCount = len(WebBrowserWindow.BrowserWindows)
            tabCount = 0
            for browser in WebBrowserWindow.BrowserWindows:
                tabCount += browser.tabWidget().count()
            
            if windowCount > 1 or tabCount > 1:
                mb = E5MessageBox.E5MessageBox(
                    E5MessageBox.Information,
                    self.tr("Are you sure you want to close the web browser?"),
                    self.tr("""Are you sure you want to close the web"""
                            """ browser?\n"""
                            """You have {0} windows with {1} tabs open.""")
                    .format(windowCount, tabCount),
                    modal=True,
                    parent=self)
                if self.fromEric:
                    quitButton = mb.addButton(
                        self.tr("&Close"), E5MessageBox.AcceptRole)
                    quitButton.setIcon(UI.PixmapCache.getIcon("close.png"))
                else:
                    quitButton = mb.addButton(
                        self.tr("&Quit"), E5MessageBox.AcceptRole)
                    quitButton.setIcon(UI.PixmapCache.getIcon("exit.png"))
                mb.addButton(E5MessageBox.Cancel)
                mb.exec_()
                return mb.clickedButton() == quitButton
        
        return True
    
    def shutdown(self):
        """
        Public method to shut down the web browser.
        
        @return flag indicating successful shutdown (boolean)
        """
        if not self.__shallShutDown():
            return False
        
        if not self.downloadManager().allowQuit():
            return False
        
        WebBrowserWindow._performingShutdown = True
        
        self.sessionManager().shutdown()
        
        self.downloadManager().shutdown()
        
        self.cookieJar().close()
        
        self.bookmarksManager().close()
        
        self.historyManager().close()
        
        self.passwordManager().close()
        
        self.adBlockManager().close()
        
        self.userAgentsManager().close()
        
        self.speedDial().close()
        
        self.syncManager().close()
        
        ZoomManager.instance().close()
        
        WebIconProvider.instance().close()
        
        self.flashCookieManager().shutdown()
        
        if len(WebBrowserWindow.BrowserWindows) == 1:
            # it is the last window
            self.tabManager().close()
        
        self.networkManager().shutdown()
        
        for browser in WebBrowserWindow.BrowserWindows:
            if browser != self:
                browser.close()
        self.close()
        
        return True

    def __backward(self):
        """
        Private slot called to handle the backward action.
        """
        self.currentBrowser().backward()
    
    def __forward(self):
        """
        Private slot called to handle the forward action.
        """
        self.currentBrowser().forward()
    
    def __home(self):
        """
        Private slot called to handle the home action.
        """
        self.currentBrowser().home()
    
    def __reload(self):
        """
        Private slot called to handle the reload action.
        """
        self.currentBrowser().reloadBypassingCache()
    
    def __stopLoading(self):
        """
        Private slot called to handle loading of the current page.
        """
        self.currentBrowser().stop()
    
    def __zoomValueChanged(self, value):
        """
        Private slot to handle value changes of the zoom widget.
        
        @param value zoom value (integer)
        """
        self.currentBrowser().setZoomValue(value)
    
    def __zoomIn(self):
        """
        Private slot called to handle the zoom in action.
        """
        self.currentBrowser().zoomIn()
        self.__zoomWidget.setValue(self.currentBrowser().zoomValue())
    
    def __zoomOut(self):
        """
        Private slot called to handle the zoom out action.
        """
        self.currentBrowser().zoomOut()
        self.__zoomWidget.setValue(self.currentBrowser().zoomValue())
    
    def __zoomReset(self):
        """
        Private slot called to handle the zoom reset action.
        """
        self.currentBrowser().zoomReset()
        self.__zoomWidget.setValue(self.currentBrowser().zoomValue())
    
    def toggleFullScreen(self):
        """
        Public slot called to toggle the full screen mode.
        """
        if self.__htmlFullScreen:
            self.currentBrowser().triggerPageAction(
                QWebEnginePage.ExitFullScreen)
            return
        
        if self.isFullScreen():
            # switch back to normal
            self.showNormal()
        else:
            # switch to full screen
            self.showFullScreen()
    
    def enterHtmlFullScreen(self):
        """
        Public method to switch to full screen initiated by the
        HTML page.
        """
        self.showFullScreen()
        self.__htmlFullScreen = True
    
    def isFullScreenNavigationVisible(self):
        """
        Public method to check, if full screen navigation is active.
        
        @return flag indicating visibility of the navigation container in full
            screen mode
        @rtype bool
        """
        return self.isFullScreen() and self.__navigationContainer.isVisible()
    
    def showFullScreenNavigation(self):
        """
        Public slot to show full screen navigation.
        """
        if self.__htmlFullScreen:
            return
        
        if self.__hideNavigationTimer.isActive():
            self.__hideNavigationTimer.stop()
        
        self.__navigationContainer.show()
        self.__tabWidget.tabBar().show()
    
    def hideFullScreenNavigation(self):
        """
        Public slot to hide full screen navigation.
        """
        if not self.__hideNavigationTimer.isActive():
            self.__hideNavigationTimer.start()
    
    def __hideNavigation(self):
        """
        Private slot to hide full screen navigation by timer.
        """
        browser = self.currentBrowser()
        mouseInBrowser = browser and browser.underMouse()
        
        if self.isFullScreen() and mouseInBrowser:
            self.__navigationContainer.hide()
            self.__tabWidget.tabBar().hide()
    
    def __copy(self):
        """
        Private slot called to handle the copy action.
        """
        self.currentBrowser().copy()
    
    def __cut(self):
        """
        Private slot called to handle the cut action.
        """
        self.currentBrowser().cut()
    
    def __paste(self):
        """
        Private slot called to handle the paste action.
        """
        self.currentBrowser().paste()
    
    def __undo(self):
        """
        Private slot to handle the undo action.
        """
        self.currentBrowser().undo()
    
    def __redo(self):
        """
        Private slot to handle the redo action.
        """
        self.currentBrowser().redo()
    
    def __selectAll(self):
        """
        Private slot to handle the select all action.
        """
        self.currentBrowser().selectAll()
    
    def __unselect(self):
        """
        Private slot to clear the selection of the current browser.
        """
        self.currentBrowser().unselect()
    
    @classmethod
    def isPrivate(cls):
        """
        Class method to check the private browsing mode.
        
        @return flag indicating private browsing mode
        @rtype bool
        """
        return cls._isPrivate
    
    def currentBrowser(self):
        """
        Public method to get a reference to the current web browser.
        
        @return reference to the current help browser (WebBrowserView)
        """
        return self.__tabWidget.currentBrowser()
    
    def browserAt(self, index):
        """
        Public method to get a reference to the web browser with the given
        index.
        
        @param index index of the browser to get (integer)
        @return reference to the indexed web browser (WebBrowserView)
        """
        return self.__tabWidget.browserAt(index)
    
    def browsers(self):
        """
        Public method to get a list of references to all web browsers.
        
        @return list of references to web browsers (list of WebBrowserView)
        """
        return self.__tabWidget.browsers()
    
    def __currentChanged(self, index):
        """
        Private slot to handle the currentChanged signal.
        
        @param index index of the current tab (integer)
        """
        if index > -1:
            cb = self.currentBrowser()
            if cb is not None:
                self.setForwardAvailable(cb.isForwardAvailable())
                self.setBackwardAvailable(cb.isBackwardAvailable())
                self.setLoadingActions(cb.isLoading())
                
                # set value of zoom widget
                self.__zoomWidget.setValue(cb.zoomValue())
    
    def __showPreferences(self):
        """
        Private slot to set the preferences.
        """
        from Preferences.ConfigurationDialog import ConfigurationDialog
        dlg = ConfigurationDialog(
            self, 'Configuration', True, fromEric=self.__fromEric,
            displayMode=ConfigurationDialog.WebBrowserMode)
        dlg.preferencesChanged.connect(self.preferencesChanged)
        dlg.masterPasswordChanged.connect(self.masterPasswordChanged)
        dlg.show()
        if self.__lastConfigurationPageName:
            dlg.showConfigurationPageByName(self.__lastConfigurationPageName)
        else:
            dlg.showConfigurationPageByName("empty")
        dlg.exec_()
        QApplication.processEvents()
        if dlg.result() == QDialog.Accepted:
            dlg.setPreferences()
            Preferences.syncPreferences()
            self.preferencesChanged()
        self.__lastConfigurationPageName = dlg.getConfigurationPageName()
    
    def preferencesChanged(self):
        """
        Public slot to handle a change of preferences.
        """
        if not self.__fromEric:
            self.setStyle(Preferences.getUI("Style"),
                          Preferences.getUI("StyleSheet"))
        
        self.__initWebEngineSettings()
        
        self.networkManager().preferencesChanged()
        
        self.historyManager().preferencesChanged()
        
        self.__tabWidget.preferencesChanged()
        
        self.__navigationBar.searchEdit().preferencesChanged()
        
        self.autoScroller().preferencesChanged()
        
        profile = self.webProfile()
        if not self.isPrivate():
            if Preferences.getWebBrowser("DiskCacheEnabled"):
                profile.setHttpCacheType(QWebEngineProfile.DiskHttpCache)
                profile.setHttpCacheMaximumSize(
                    Preferences.getWebBrowser("DiskCacheSize") * 1024 * 1024)
            else:
                profile.setHttpCacheType(QWebEngineProfile.MemoryHttpCache)
                profile.setHttpCacheMaximumSize(0)
        
        if qVersionTuple() >= (5, 8, 0):
            profile.setSpellCheckEnabled(
                Preferences.getWebBrowser("SpellCheckEnabled"))
            profile.setSpellCheckLanguages(
                Preferences.getWebBrowser("SpellCheckLanguages"))
        
        self.__virusTotal.preferencesChanged()
        if not Preferences.getWebBrowser("VirusTotalEnabled") or \
           Preferences.getWebBrowser("VirusTotalServiceKey") == "":
            self.virustotalScanCurrentAct.setEnabled(False)
            self.virustotalIpReportAct.setEnabled(False)
            self.virustotalDomainReportAct.setEnabled(False)
        else:
            self.virustotalScanCurrentAct.setEnabled(True)
            self.virustotalIpReportAct.setEnabled(True)
            self.virustotalDomainReportAct.setEnabled(True)
        
        self.__javaScriptIcon.preferencesChanged()
        
        self.sessionManager().preferencesChanged()
    
    def masterPasswordChanged(self, oldPassword, newPassword):
        """
        Public slot to handle the change of the master password.
        
        @param oldPassword current master password (string)
        @param newPassword new master password (string)
        """
        from Preferences.ConfigurationDialog import ConfigurationDialog
        self.passwordManager().masterPasswordChanged(oldPassword, newPassword)
        if self.__fromEric and isinstance(self.sender(), ConfigurationDialog):
            # we were called from our local configuration dialog
            Preferences.convertPasswords(oldPassword, newPassword)
            Utilities.crypto.changeRememberedMaster(newPassword)
    
    def __showAcceptedLanguages(self):
        """
        Private slot to configure the accepted languages for web pages.
        """
        from .WebBrowserLanguagesDialog import WebBrowserLanguagesDialog
        dlg = WebBrowserLanguagesDialog(self)
        dlg.exec_()
        self.networkManager().languagesChanged()
    
    def __showCookiesConfiguration(self):
        """
        Private slot to configure the cookies handling.
        """
        from .CookieJar.CookiesConfigurationDialog import \
            CookiesConfigurationDialog
        dlg = CookiesConfigurationDialog(self)
        dlg.exec_()
    
    def __showFlashCookiesManagement(self):
        """
        Private slot to show the flash cookies management dialog.
        """
        self.flashCookieManager().showFlashCookieManagerDialog()
    
    @classmethod
    def setUseQtHelp(cls, use):
        """
        Class method to set the QtHelp usage.
        
        @param use flag indicating usage (boolean)
        """
        if use:
            cls._useQtHelp = use and QTHELP_AVAILABLE
        else:
            cls._useQtHelp = False
    
    @classmethod
    def helpEngine(cls):
        """
        Class method to get a reference to the help engine.
        
        @return reference to the help engine (QHelpEngine)
        """
        if cls._useQtHelp:
            if cls._helpEngine is None:
                cls._helpEngine = QHelpEngine(
                    WebBrowserWindow.getQtHelpCollectionFileName())
            return cls._helpEngine
        else:
            return None
    
    @classmethod
    def getQtHelpCollectionFileName(cls):
        """
        Class method to determine the name of the QtHelp collection file.
        
        @return path of the QtHelp collection file
        @rtype str
        """
        qthelpDir = os.path.join(Utilities.getConfigDir(), "qthelp")
        if not os.path.exists(qthelpDir):
            os.makedirs(qthelpDir)
        return os.path.join(qthelpDir, "eric6help.qhc")
    
    @classmethod
    def networkManager(cls):
        """
        Class method to get a reference to the network manager object.
        
        @return reference to the network access manager (NetworkManager)
        """
        if cls._networkManager is None:
            from .Network.NetworkManager import NetworkManager
            cls._networkManager = NetworkManager(cls.helpEngine())
        
        return cls._networkManager
    
    @classmethod
    def cookieJar(cls):
        """
        Class method to get a reference to the cookie jar.
        
        @return reference to the cookie jar (CookieJar)
        """
        if cls._cookieJar is None:
            from .CookieJar.CookieJar import CookieJar
            cls._cookieJar = CookieJar()
        
        return cls._cookieJar
        
    def __clearIconsDatabase(self):
        """
        Private slot to clear the favicons databse.
        """
        WebIconProvider.instance().clear()
    
    def __showWebIconsDialog(self):
        """
        Private slot to show a dialog to manage the favicons database.
        """
        WebIconProvider.instance().showWebIconDialog()
        
    @pyqtSlot(QUrl)
    def __linkActivated(self, url):
        """
        Private slot to handle the selection of a link.
        
        @param url URL to be shown (QUrl)
        """
        if not self.__activating:
            self.__activating = True
            cb = self.currentBrowser()
            if cb is None:
                self.newTab(url)
            else:
                cb.setUrl(url)
            self.__activating = False
    
    def __activateCurrentBrowser(self):
        """
        Private slot to activate the current browser.
        """
        self.currentBrowser().setFocus()
        
    def __syncTOC(self):
        """
        Private slot to synchronize the TOC with the currently shown page.
        """
        if WebBrowserWindow._useQtHelp:
            QApplication.setOverrideCursor(Qt.WaitCursor)
            url = self.currentBrowser().source()
            self.__showTocWindow()
            if not self.__tocWindow.syncToContent(url):
                self.statusBar().showMessage(
                    self.tr("Could not find an associated content."), 5000)
            QApplication.restoreOverrideCursor()
        
    def __showTocWindow(self):
        """
        Private method to show the table of contents window.
        """
        if WebBrowserWindow._useQtHelp:
            self.__activateDock(self.__tocWindow)
        
    def __showIndexWindow(self):
        """
        Private method to show the index window.
        """
        if WebBrowserWindow._useQtHelp:
            self.__activateDock(self.__indexWindow)
        
    def __showSearchWindow(self):
        """
        Private method to show the search window.
        """
        if WebBrowserWindow._useQtHelp:
            self.__activateDock(self.__searchWindow)
        
    def __activateDock(self, widget):
        """
        Private method to activate the dock widget of the given widget.
        
        @param widget reference to the widget to be activated (QWidget)
        """
        widget.parent().show()
        widget.parent().raise_()
        widget.setFocus()
        
    def __setupFilterCombo(self):
        """
        Private slot to setup the filter combo box.
        """
        if WebBrowserWindow._useQtHelp:
            curFilter = self.filterCombo.currentText()
            if not curFilter:
                curFilter = self.__helpEngine.currentFilter()
            self.filterCombo.clear()
            self.filterCombo.addItems(self.__helpEngine.customFilters())
            idx = self.filterCombo.findText(curFilter)
            if idx < 0:
                idx = 0
            self.filterCombo.setCurrentIndex(idx)
        
    def __filterQtHelpDocumentation(self, customFilter):
        """
        Private slot to filter the QtHelp documentation.
        
        @param customFilter name of filter to be applied (string)
        """
        if self.__helpEngine:
            self.__helpEngine.setCurrentFilter(customFilter)
        
    def __manageQtHelpDocumentation(self):
        """
        Private slot to manage the QtHelp documentation database.
        """
        if WebBrowserWindow._useQtHelp:
            from .QtHelp.QtHelpDocumentationDialog import \
                QtHelpDocumentationDialog
            dlg = QtHelpDocumentationDialog(self.__helpEngine, self)
            dlg.exec_()
            if dlg.hasChanges():
                for i in sorted(dlg.getTabsToClose(), reverse=True):
                    self.__tabWidget.closeBrowserAt(i)
                self.__helpEngine.setupData()
        
    def getSourceFileList(self):
        """
        Public method to get a list of all opened source files.
        
        @return dictionary with tab id as key and host/namespace as value
        """
        return self.__tabWidget.getSourceFileList()
    
    def __manageQtHelpFilters(self):
        """
        Private slot to manage the QtHelp filters.
        """
        if WebBrowserWindow._useQtHelp:
            from .QtHelp.QtHelpFiltersDialog import QtHelpFiltersDialog
            dlg = QtHelpFiltersDialog(self.__helpEngine, self)
            dlg.exec_()
        
    def __indexingStarted(self):
        """
        Private slot to handle the start of the indexing process.
        """
        if WebBrowserWindow._useQtHelp:
            self.__indexing = True
            if self.__indexingProgress is None:
                self.__indexingProgress = QWidget()
                layout = QHBoxLayout(self.__indexingProgress)
                layout.setContentsMargins(0, 0, 0, 0)
                sizePolicy = QSizePolicy(QSizePolicy.Preferred,
                                         QSizePolicy.Maximum)
                
                label = QLabel(self.tr("Updating search index"))
                label.setSizePolicy(sizePolicy)
                layout.addWidget(label)
                
                progressBar = QProgressBar()
                progressBar.setRange(0, 0)
                progressBar.setTextVisible(False)
                progressBar.setFixedHeight(16)
                progressBar.setSizePolicy(sizePolicy)
                layout.addWidget(progressBar)
                
                self.statusBar().insertPermanentWidget(
                    0, self.__indexingProgress)
        
    def __indexingFinished(self):
        """
        Private slot to handle the start of the indexing process.
        """
        if WebBrowserWindow._useQtHelp:
            self.statusBar().removeWidget(self.__indexingProgress)
            self.__indexingProgress = None
            self.__indexing = False
            if self.__searchWord is not None:
                self.__searchForWord()
        
    def __searchForWord(self):
        """
        Private slot to search for a word.
        """
        if WebBrowserWindow._useQtHelp and not self.__indexing and \
                self.__searchWord is not None:
            self.__searchDock.show()
            self.__searchDock.raise_()
            query = QHelpSearchQuery(QHelpSearchQuery.DEFAULT,
                                     [self.__searchWord])
            self.__searchEngine.search([query])
            self.__searchWord = None
        
    def search(self, word):
        """
        Public method to search for a word.
        
        @param word word to search for (string)
        """
        if WebBrowserWindow._useQtHelp:
            self.__searchWord = word
            self.__searchForWord()
        
    def __removeOldDocumentation(self):
        """
        Private slot to remove non-existing documentation from the help engine.
        """
        for namespace in self.__helpEngine.registeredDocumentations():
            docFile = self.__helpEngine.documentationFileName(namespace)
            if not os.path.exists(docFile):
                self.__helpEngine.unregisterDocumentation(namespace)
        
    def __lookForNewDocumentation(self):
        """
        Private slot to look for new documentation to be loaded into the
        help database.
        """
        if WebBrowserWindow._useQtHelp:
            from .QtHelp.HelpDocsInstaller import HelpDocsInstaller
            self.__helpInstaller = HelpDocsInstaller(
                self.__helpEngine.collectionFile())
            self.__helpInstaller.errorMessage.connect(
                self.__showInstallationError)
            self.__helpInstaller.docsInstalled.connect(self.__docsInstalled)
            
            self.statusBar().showMessage(
                self.tr("Looking for Documentation..."))
            self.__helpInstaller.installDocs()
        
    def __showInstallationError(self, message):
        """
        Private slot to show installation errors.
        
        @param message message to be shown (string)
        """
        E5MessageBox.warning(
            self,
            self.tr("eric6 Web Browser"),
            message)
        
    def __docsInstalled(self, installed):
        """
        Private slot handling the end of documentation installation.
        
        @param installed flag indicating that documents were installed
            (boolean)
        """
        if WebBrowserWindow._useQtHelp:
            if installed:
                self.__helpEngine.setupData()
            self.statusBar().clearMessage()
        
    def __initHelpDb(self):
        """
        Private slot to initialize the documentation database.
        """
        if WebBrowserWindow._useQtHelp:
            if not self.__helpEngine.setupData():
                return
            
            unfiltered = self.tr("Unfiltered")
            if unfiltered not in self.__helpEngine.customFilters():
                hc = QHelpEngineCore(self.__helpEngine.collectionFile())
                hc.setupData()
                hc.addCustomFilter(unfiltered, [])
                hc = None
                del hc
                
                self.__helpEngine.blockSignals(True)
                self.__helpEngine.setCurrentFilter(unfiltered)
                self.__helpEngine.blockSignals(False)
                self.__helpEngine.setupData()
        
    def __warning(self, msg):
        """
        Private slot handling warnings from the help engine.
        
        @param msg message sent by the help  engine (string)
        """
        E5MessageBox.warning(
            self,
            self.tr("Help Engine"), msg)
        
    def __aboutToShowSettingsMenu(self):
        """
        Private slot to show the Settings menu.
        """
        self.editMessageFilterAct.setEnabled(
            E5ErrorMessage.messageHandlerInstalled())
        
    def __clearPrivateData(self):
        """
        Private slot to clear the private data.
        """
        from .WebBrowserClearPrivateDataDialog import \
            WebBrowserClearPrivateDataDialog
        dlg = WebBrowserClearPrivateDataDialog(self)
        if dlg.exec_() == QDialog.Accepted:
            # browsing history, search history, favicons, disk cache, cookies,
            # passwords, web databases, downloads, Flash cookies
            (history, searches, favicons, cache, cookies,
             passwords, databases, downloads, flashCookies, zoomValues,
             sslExceptions, historyPeriod) = dlg.getData()
            if history:
                self.historyManager().clear(historyPeriod)
                self.__tabWidget.clearClosedTabsList()
                self.webProfile().clearAllVisitedLinks()
            if searches:
                self.__navigationBar.searchEdit().clear()
            if downloads:
                self.downloadManager().cleanup()
                self.downloadManager().hide()
            if favicons:
                self.__clearIconsDatabase()
            if cache:
                try:
                    self.webProfile().clearHttpCache()
                except AttributeError:
                    cachePath = self.webProfile().cachePath()
                    if cachePath:
                        shutil.rmtree(cachePath)
            if cookies:
                self.cookieJar().clear()
                self.webProfile().cookieStore().deleteAllCookies()
            if passwords:
                self.passwordManager().clear()
            if flashCookies:
                self.flashCookieManager().removeAllCookies()
            if zoomValues:
                ZoomManager.instance().clear()
            if sslExceptions:
                self.networkManager().clearSslExceptions()
        
    def __showEnginesConfigurationDialog(self):
        """
        Private slot to show the search engines configuration dialog.
        """
        from .OpenSearch.OpenSearchDialog import OpenSearchDialog
        
        dlg = OpenSearchDialog(self)
        dlg.exec_()
        
    def searchEnginesAction(self):
        """
        Public method to get a reference to the search engines configuration
        action.
        
        @return reference to the search engines configuration action (QAction)
        """
        return self.searchEnginesAct
        
    def __showPasswordsDialog(self):
        """
        Private slot to show the passwords management dialog.
        """
        from .Passwords.PasswordsDialog import PasswordsDialog
        
        dlg = PasswordsDialog(self)
        dlg.exec_()
    
    def __showCertificateErrorsDialog(self):
        """
        Private slot to show the certificate errors management dialog.
        """
        self.networkManager().showSslErrorExceptionsDialog()
    
    def __showAdBlockDialog(self):
        """
        Private slot to show the AdBlock configuration dialog.
        """
        self.adBlockManager().showDialog()
        
    def __showPersonalInformationDialog(self):
        """
        Private slot to show the Personal Information configuration dialog.
        """
        self.personalInformationManager().showConfigurationDialog()
        
    def __showGreaseMonkeyConfigDialog(self):
        """
        Private slot to show the GreaseMonkey scripts configuration dialog.
        """
        self.greaseMonkeyManager().showConfigurationDialog()
        
    def __showFeaturePermissionDialog(self):
        """
        Private slot to show the feature permission dialog.
        """
        self.featurePermissionManager().showFeaturePermissionsDialog()
        
    def __showZoomValuesDialog(self):
        """
        Private slot to show the zoom values management dialog.
        """
        from .ZoomManager.ZoomValuesDialog import ZoomValuesDialog
        
        dlg = ZoomValuesDialog(self)
        dlg.exec_()
    
    def __showDownloadsWindow(self):
        """
        Private slot to show the downloads dialog.
        """
        self.downloadManager().show()
        
    def __showPageSource(self):
        """
        Private slot to show the source of the current page in an editor.
        """
        self.currentBrowser().page().toHtml(self.__showPageSourceCallback)
        
    def __showPageSourceCallback(self, src):
        """
        Private method to show the source of the current page in an editor.
        
        @param src source of the web page
        @type str
        """
        from QScintilla.MiniEditor import MiniEditor
        editor = MiniEditor(parent=self)
        editor.setText(src, "Html")
        editor.setLanguage("dummy.html")
        editor.show()
    
    def __toggleJavaScriptConsole(self):
        """
        Private slot to toggle the JavaScript console.
        """
        if self.__javascriptConsoleDock.isVisible():
            self.__javascriptConsoleDock.hide()
        else:
            self.__javascriptConsoleDock.show()
    
    def javascriptConsole(self):
        """
        Public method to get a reference to the JavaScript console widget.
        
        @return reference to the JavaScript console
        @rtype WebBrowserJavaScriptConsole
        """
        return self.__javascriptConsole
    
    @classmethod
    def icon(cls, url):
        """
        Class method to get the icon for an URL.
        
        @param url URL to get icon for (QUrl)
        @return icon for the URL (QIcon)
        """
        return WebIconProvider.instance().iconForUrl(url)

    @classmethod
    def bookmarksManager(cls):
        """
        Class method to get a reference to the bookmarks manager.
        
        @return reference to the bookmarks manager (BookmarksManager)
        """
        if cls._bookmarksManager is None:
            from .Bookmarks.BookmarksManager import BookmarksManager
            cls._bookmarksManager = BookmarksManager()
        
        return cls._bookmarksManager
    
    def openUrl(self, url, title=None):
        """
        Public slot to load a URL in the current tab.
        
        @param url URL to be opened (QUrl)
        @param title title of the bookmark (string)
        """
        self.__linkActivated(url)
    
    def openUrlNewTab(self, url, title=None):
        """
        Public slot to load a URL in a new tab.
        
        @param url URL to be opened (QUrl)
        @param title title of the bookmark (string)
        """
        self.newTab(url)
    
    def openUrlNewBackgroundTab(self, url, title=None):
        """
        Public slot to load a URL in a new background tab.
        
        @param url URL to be opened (QUrl)
        @param title title of the bookmark (string)
        """
        self.newTab(url, background=True)
    
    def openUrlNewWindow(self, url, title=None):
        """
        Public slot to load a URL in a new window.
        
        @param url URL to be opened (QUrl)
        @param title title of the bookmark (string)
        """
        self.newWindow(url)
    
    def openUrlNewPrivateWindow(self, url, title=None):
        """
        Public slot to load a URL in a new private window.
        
        @param url URL to be opened (QUrl)
        @param title title of the bookmark (string)
        """
        self.newPrivateWindow(url)
    
    def __sendPageLink(self):
        """
        Private slot to send the link of the current page via email.
        """
        url = self.currentBrowser().url()
        if not url.isEmpty():
            urlStr = url.toString()
            QDesktopServices.openUrl(QUrl("mailto:?body=" + urlStr))
    
    @classmethod
    def historyManager(cls):
        """
        Class method to get a reference to the history manager.
        
        @return reference to the history manager (HistoryManager)
        """
        if cls._historyManager is None:
            from .History.HistoryManager import HistoryManager
            cls._historyManager = HistoryManager()
        
        return cls._historyManager
        
    @classmethod
    def passwordManager(cls):
        """
        Class method to get a reference to the password manager.
        
        @return reference to the password manager (PasswordManager)
        """
        if cls._passwordManager is None:
            from .Passwords.PasswordManager import PasswordManager
            cls._passwordManager = PasswordManager()
        
        return cls._passwordManager
    
    @classmethod
    def adBlockManager(cls):
        """
        Class method to get a reference to the AdBlock manager.
        
        @return reference to the AdBlock manager (AdBlockManager)
        """
        if cls._adblockManager is None:
            from .AdBlock.AdBlockManager import AdBlockManager
            cls._adblockManager = AdBlockManager()
        
        return cls._adblockManager
    
    def adBlockIcon(self):
        """
        Public method to get a reference to the AdBlock icon.
        
        @return reference to the AdBlock icon (AdBlockIcon)
        """
        return self.__adBlockIcon
    
    @classmethod
    def downloadManager(cls):
        """
        Class method to get a reference to the download manager.
        
        @return reference to the download manager (DownloadManager)
        """
        if cls._downloadManager is None:
            from .Download.DownloadManager import DownloadManager
            cls._downloadManager = DownloadManager()
        
        return cls._downloadManager
        
    @classmethod
    def personalInformationManager(cls):
        """
        Class method to get a reference to the personal information manager.
        
        @return reference to the personal information manager
            (PersonalInformationManager)
        """
        if cls._personalInformationManager is None:
            from .PersonalInformationManager.PersonalInformationManager \
                import PersonalInformationManager
            cls._personalInformationManager = PersonalInformationManager()
        
        return cls._personalInformationManager
        
    @classmethod
    def greaseMonkeyManager(cls):
        """
        Class method to get a reference to the GreaseMonkey manager.
        
        @return reference to the GreaseMonkey manager (GreaseMonkeyManager)
        """
        if cls._greaseMonkeyManager is None:
            from .GreaseMonkey.GreaseMonkeyManager import GreaseMonkeyManager
            cls._greaseMonkeyManager = GreaseMonkeyManager()
        
        return cls._greaseMonkeyManager
        
    @classmethod
    def featurePermissionManager(cls):
        """
        Class method to get a reference to the feature permission manager.
        
        @return reference to the feature permission manager
        @rtype FeaturePermissionManager
        """
        if cls._featurePermissionManager is None:
            from .FeaturePermissions.FeaturePermissionManager import \
                FeaturePermissionManager
            cls._featurePermissionManager = FeaturePermissionManager()
        
        return cls._featurePermissionManager
        
    @classmethod
    def flashCookieManager(cls):
        """
        Class method to get a reference to the flash cookies manager.
        
        @return reference to the flash cookies manager
        @rtype FlashCookieManager
        """
        if cls._flashCookieManager is None:
            from .FlashCookieManager.FlashCookieManager import \
                FlashCookieManager
            cls._flashCookieManager = FlashCookieManager()
        
        return cls._flashCookieManager
        
    @classmethod
    def imageSearchEngine(cls):
        """
        Class method to get a reference to the image search engine.
        
        @return reference to the image finder object
        @rtype ImageSearchEngine
        """
        if cls._imageSearchEngine is None:
            from .ImageSearch.ImageSearchEngine import \
                ImageSearchEngine
            cls._imageSearchEngine = ImageSearchEngine()
        
        return cls._imageSearchEngine
        
    @classmethod
    def autoScroller(cls):
        """
        Class method to get a reference to the auto scroller.
        
        @return reference to the auto scroller object
        @rtype AutoScroller
        """
        if cls._autoScroller is None:
            from .AutoScroll.AutoScroller import AutoScroller
            cls._autoScroller = AutoScroller()
        
        return cls._autoScroller
        
    @classmethod
    def tabManager(cls):
        """
        Class method to get a reference to the tab manager widget.
        
        @return reference to the tab manager widget
        @rtype TabManagerWidget
        """
        if cls._tabManager is None:
            from .TabManager.TabManagerWidget import TabManagerWidget
            cls._tabManager = TabManagerWidget(cls.mainWindow())
            
            # do the connections
            for window in cls.mainWindows():
                cls._tabManager.mainWindowCreated(window, False)
            
            cls._tabManager.delayedRefreshTree()
        
        return cls._tabManager
    
    def __showTabManager(self):
        """
        Private method to show the tab manager window.
        """
        self.tabManager().raiseTabManager()
    
    @classmethod
    def mainWindow(cls):
        """
        Class method to get a reference to the main window.
        
        @return reference to the main window (WebBrowserWindow)
        """
        if cls.BrowserWindows:
            return cls.BrowserWindows[0]
        else:
            return None
    
    @classmethod
    def mainWindows(cls):
        """
        Class method to get references to all main windows.
        
        @return references to all main window (list of WebBrowserWindow)
        """
        return cls.BrowserWindows
    
    @pyqtSlot()
    def __appFocusChanged(self):
        """
        Private slot to handle a change of the focus.
        """
        focusWindow = e5App().activeWindow()
        if isinstance(focusWindow, WebBrowserWindow):
            WebBrowserWindow._lastActiveWindow = focusWindow
    
    @classmethod
    def getWindow(cls):
        """
        Class method to get a reference to the most recent active
        web browser window.
        
        @return reference to most recent web browser window
        @rtype WebBrowserWindow
        """
        if cls._lastActiveWindow:
            return cls._lastActiveWindow
        
        return cls.mainWindow()
    
    def openSearchManager(self):
        """
        Public method to get a reference to the opensearch manager object.
        
        @return reference to the opensearch manager object (OpenSearchManager)
        """
        return self.__navigationBar.searchEdit().openSearchManager()
    
    def __createTextEncodingAction(self, codec, defaultCodec, parentMenu):
        """
        Private method to create an action for the text encoding menu.
        
        @param codec name of the codec to create an action for
        @type str
        @param defaultCodec name of the default codec
        @type str
        @param parentMenu reference to the parent menu
        @type QMenu
        """
        act = QAction(codec, parentMenu)
        act.setData(codec)
        act.setCheckable(True)
        if defaultCodec == codec:
            act.setChecked(True)
        
        parentMenu.addAction(act)
    
    def __createTextEncodingSubmenu(self, title, codecNames, parentMenu):
        """
        Private method to create a text encoding sub menu.
        
        @param title title of the menu
        @type str
        @param codecNames list of codec names for the menu
        @type list of str
        @param parentMenu reference to the parent menu
        @type QMenu
        """
        if codecNames:
            defaultCodec = \
                QWebEngineSettings.defaultSettings().defaultTextEncoding()\
                .lower()
            
            menu = QMenu(title, parentMenu)
            for codec in codecNames:
                self.__createTextEncodingAction(codec, defaultCodec, menu)
            
            parentMenu.addMenu(menu)
    
    def __aboutToShowTextEncodingMenu(self):
        """
        Private slot to populate the text encoding menu.
        """
        self.__textEncodingMenu.clear()
        
        codecs = []
        for mib in QTextCodec.availableMibs():
            codec = str(QTextCodec.codecForMib(mib).name(),
                        encoding="utf-8").lower()
            if codec not in codecs:
                codecs.append(codec)
        codecs.sort()
        
        defaultTextEncoding = \
            QWebEngineSettings.defaultSettings().defaultTextEncoding().lower()
        if defaultTextEncoding in codecs:
            currentCodec = defaultTextEncoding
        else:
            currentCodec = "system"
        
        isoCodecs = []
        winCodecs = []
        isciiCodecs = []
        uniCodecs = []
        ibmCodecs = []
        otherCodecs = []
        
        for codec in codecs:
            if codec.startswith(("iso", "latin")):
                isoCodecs.append(codec)
            elif codec.startswith(("windows")):
                winCodecs.append(codec)
            elif codec.startswith("iscii"):
                isciiCodecs.append(codec)
            elif codec.startswith("utf"):
                uniCodecs.append(codec)
            elif codec.startswith(("ibm")):
                ibmCodecs.append(codec)
            elif codec == "system":
                self.__createTextEncodingAction(codec, currentCodec,
                                                self.__textEncodingMenu)
            else:
                otherCodecs.append(codec)
        
        if not self.__textEncodingMenu.isEmpty():
            self.__textEncodingMenu.addSeparator()
        self.__createTextEncodingSubmenu(self.tr("ISO"), isoCodecs,
                                         self.__textEncodingMenu)
        self.__createTextEncodingSubmenu(self.tr("Unicode"), uniCodecs,
                                         self.__textEncodingMenu)
        self.__createTextEncodingSubmenu(self.tr("Windows"), winCodecs,
                                         self.__textEncodingMenu)
        self.__createTextEncodingSubmenu(self.tr("ISCII"), isciiCodecs,
                                         self.__textEncodingMenu)
        self.__createTextEncodingSubmenu(self.tr("IBM"), ibmCodecs,
                                         self.__textEncodingMenu)
        self.__createTextEncodingSubmenu(self.tr("Other"), otherCodecs,
                                         self.__textEncodingMenu)
    
    def __setTextEncoding(self, act):
        """
        Private slot to set the selected text encoding as the default for
        this session.
        
        @param act reference to the selected action (QAction)
        """
        codec = act.data()
        if codec == "":
            QWebEngineSettings.defaultSettings().setDefaultTextEncoding("")
        else:
            QWebEngineSettings.defaultSettings().setDefaultTextEncoding(codec)
    
    def __populateToolbarsMenu(self, menu):
        """
        Private method to populate the toolbars menu.
        
        @param menu reference to the menu to be populated
        @type QMenu
        """
        menu.clear()
        
        act = menu.addAction(self.tr("Menu Bar"))
        act.setCheckable(True)
        act.setChecked(not self.menuBar().isHidden())
        act.setData("menubar")
        
        act = menu.addAction(self.tr("Bookmarks"))
        act.setCheckable(True)
        act.setChecked(not self.__bookmarksToolBar.isHidden())
        act.setData("bookmarks")
        
        act = menu.addAction(self.tr("Status Bar"))
        act.setCheckable(True)
        act.setChecked(not self.statusBar().isHidden())
        act.setData("statusbar")
        
        if Preferences.getWebBrowser("ShowToolbars"):
            menu.addSeparator()
            for name, (text, tb) in sorted(self.__toolbars.items(),
                                           key=lambda t: t[1][0]):
                act = menu.addAction(text)
                act.setCheckable(True)
                act.setChecked(not tb.isHidden())
                act.setData(name)
            menu.addSeparator()
            act = menu.addAction(self.tr("&Show all"))
            act.setData("__SHOW__")
            act = menu.addAction(self.tr("&Hide all"))
            act.setData("__HIDE__")
    
    def createPopupMenu(self):
        """
        Public method to create the toolbars menu for Qt.
        
        @return toolbars menu
        @rtype QMenu
        """
        menu = QMenu(self)
        menu.triggered.connect(self.__TBMenuTriggered)
        
        self.__populateToolbarsMenu(menu)
        
        return menu

    def __showToolbarsMenu(self):
        """
        Private slot to display the Toolbars menu.
        """
        self.__populateToolbarsMenu(self.__toolbarsMenu)

    def __TBMenuTriggered(self, act):
        """
        Private method to handle the toggle of a toolbar via the Window->
        Toolbars submenu or the toolbars popup menu.
        
        @param act reference to the action that was triggered
        @type QAction
        """
        name = act.data()
        if name:
            if name == "bookmarks":
                # special handling of bookmarks toolbar
                self.__setBookmarksToolbarVisibility(act.isChecked())
            
            elif name == "menubar":
                # special treatment of the menu bar
                self.__setMenuBarVisibility(act.isChecked())
            
            elif name == "statusbar":
                # special treatment of the status bar
                self.__setStatusBarVisible(act.isChecked())
            
            elif name == "__SHOW__":
                for text, tb in list(self.__toolbars.values()):
                    tb.show()
            
            elif name == "__HIDE__":
                for text, tb in list(self.__toolbars.values()):
                    tb.hide()
            
            else:
                tb = self.__toolbars[name][1]
                if act.isChecked():
                    tb.show()
                else:
                    tb.hide()
    
    def __setBookmarksToolbarVisibility(self, visible):
        """
        Private method to set the visibility of the bookmarks toolbar.
        
        @param visible flag indicating the toolbar visibility
        @type bool
        """
        if visible:
            self.__bookmarksToolBar.show()
        else:
            self.__bookmarksToolBar.hide()
        
        # save state for next invokation
        Preferences.setWebBrowser("BookmarksToolBarVisible", visible)
    
    def __setMenuBarVisibility(self, visible):
        """
        Private method to set the visibility of the menu bar.
        
        @param visible flag indicating the menu bar visibility
        @type bool
        """
        if visible:
            self.menuBar().show()
            self.__navigationBar.superMenuButton().hide()
        else:
            self.menuBar().hide()
            self.__navigationBar.superMenuButton().show()
        
        Preferences.setWebBrowser("MenuBarVisible", visible)
    
    def __setStatusBarVisible(self, visible):
        """
        Private method to set the visibility of the status bar.
        
        @param visible flag indicating the status bar visibility
        @type bool
        """
        self.statusBar().setVisible(visible)
        
        Preferences.setWebBrowser("StatusBarVisible", visible)
    
    def eventMouseButtons(self):
        """
        Public method to get the last recorded mouse buttons.
        
        @return mouse buttons (Qt.MouseButtons)
        """
        return self.__eventMouseButtons
    
    def eventKeyboardModifiers(self):
        """
        Public method to get the last recorded keyboard modifiers.
        
        @return keyboard modifiers (Qt.KeyboardModifiers)
        """
        return self.__eventKeyboardModifiers
    
    def setEventMouseButtons(self, buttons):
        """
        Public method to record mouse buttons.
        
        @param buttons mouse buttons to record (Qt.MouseButtons)
        """
        self.__eventMouseButtons = buttons
    
    def setEventKeyboardModifiers(self, modifiers):
        """
        Public method to record keyboard modifiers.
        
        @param modifiers keyboard modifiers to record (Qt.KeyboardModifiers)
        """
        self.__eventKeyboardModifiers = modifiers
    
    def mousePressEvent(self, evt):
        """
        Protected method called by a mouse press event.
        
        @param evt reference to the mouse event (QMouseEvent)
        """
        if evt.button() == Qt.XButton1:
            self.currentBrowser().triggerPageAction(QWebEnginePage.Back)
        elif evt.button() == Qt.XButton2:
            self.currentBrowser().triggerPageAction(QWebEnginePage.Forward)
        else:
            super(WebBrowserWindow, self).mousePressEvent(evt)
    
    @classmethod
    def feedsManager(cls):
        """
        Class method to get a reference to the RSS feeds manager.
        
        @return reference to the RSS feeds manager (FeedsManager)
        """
        if cls._feedsManager is None:
            from .Feeds.FeedsManager import FeedsManager
            cls._feedsManager = FeedsManager()
        
        return cls._feedsManager
    
    def __showFeedsManager(self):
        """
        Private slot to show the feeds manager dialog.
        """
        feedsManager = self.feedsManager()
        feedsManager.openUrl.connect(self.openUrl)
        feedsManager.newTab.connect(self.openUrlNewTab)
        feedsManager.newBackgroundTab.connect(self.openUrlNewBackgroundTab)
        feedsManager.newWindow.connect(self.openUrlNewWindow)
        feedsManager.newPrivateWindow.connect(self.openUrlNewPrivateWindow)
        feedsManager.rejected.connect(self.__feedsManagerClosed)
        feedsManager.show()
    
    def __feedsManagerClosed(self):
        """
        Private slot to handle closing the feeds manager dialog.
        """
        feedsManager = self.sender()
        feedsManager.openUrl.disconnect(self.openUrl)
        feedsManager.newTab.disconnect(self.openUrlNewTab)
        feedsManager.newBackgroundTab.disconnect(self.openUrlNewBackgroundTab)
        feedsManager.newWindow.disconnect(self.openUrlNewWindow)
        feedsManager.newPrivateWindow.disconnect(self.openUrlNewPrivateWindow)
        feedsManager.rejected.disconnect(self.__feedsManagerClosed)
    
    def __showSiteinfoDialog(self):
        """
        Private slot to show the site info dialog.
        """
        from .SiteInfo.SiteInfoDialog import SiteInfoDialog
        self.__siteinfoDialog = SiteInfoDialog(self.currentBrowser(), self)
        self.__siteinfoDialog.show()

    @classmethod
    def userAgentsManager(cls):
        """
        Class method to get a reference to the user agents manager.
        
        @return reference to the user agents manager (UserAgentManager)
        """
        if cls._userAgentsManager is None:
            from .UserAgent.UserAgentManager import UserAgentManager
            cls._userAgentsManager = UserAgentManager()
        
        return cls._userAgentsManager
    
    def __showUserAgentsDialog(self):
        """
        Private slot to show the user agents management dialog.
        """
        from .UserAgent.UserAgentsDialog import UserAgentsDialog
        
        dlg = UserAgentsDialog(self)
        dlg.exec_()
    
    @classmethod
    def syncManager(cls):
        """
        Class method to get a reference to the data synchronization manager.
        
        @return reference to the data synchronization manager (SyncManager)
        """
        if cls._syncManager is None:
            from .Sync.SyncManager import SyncManager
            cls._syncManager = SyncManager()
        
        return cls._syncManager
    
    def __showSyncDialog(self):
        """
        Private slot to show the synchronization dialog.
        """
        self.syncManager().showSyncDialog()
    
    @classmethod
    def speedDial(cls):
        """
        Class methdo to get a reference to the speed dial.
        
        @return reference to the speed dial (SpeedDial)
        """
        if cls._speedDial is None:
            from .SpeedDial.SpeedDial import SpeedDial
            cls._speedDial = SpeedDial()
        
        return cls._speedDial
    
    def keyPressEvent(self, evt):
        """
        Protected method to handle key presses.
        
        @param evt reference to the key press event (QKeyEvent)
        """
        number = -1
        key = evt.key()
        
        if key == Qt.Key_1:
            number = 1
        elif key == Qt.Key_2:
            number = 2
        elif key == Qt.Key_3:
            number = 3
        elif key == Qt.Key_4:
            number = 4
        elif key == Qt.Key_5:
            number = 5
        elif key == Qt.Key_6:
            number = 6
        elif key == Qt.Key_7:
            number = 7
        elif key == Qt.Key_8:
            number = 8
        elif key == Qt.Key_9:
            number = 9
        elif key == Qt.Key_0:
            number = 10
        
        if number != -1:
            if evt.modifiers() == Qt.KeyboardModifiers(Qt.AltModifier):
                if number == 10:
                    number = self.__tabWidget.count()
                self.__tabWidget.setCurrentIndex(number - 1)
                return
            
            if evt.modifiers() == Qt.KeyboardModifiers(Qt.MetaModifier):
                url = self.speedDial().urlForShortcut(number - 1)
                if url.isValid():
                    self.__linkActivated(url)
                    return
        
        super(WebBrowserWindow, self).keyPressEvent(evt)
    
    def event(self, evt):
        """
        Public method handling events.
        
        @param evt reference to the event
        @type QEvent
        @return flag indicating a handled event
        @rtype bool
        """
        if evt.type() == QEvent.WindowStateChange:
            if not bool(evt.oldState() & Qt.WindowFullScreen) and \
               bool(self.windowState() & Qt.WindowFullScreen):
                # enter full screen mode
                self.__windowStates = evt.oldState()
                self.__toolbarStates = self.saveState()
                self.menuBar().hide()
                self.statusBar().hide()
                self.__searchWidget.hide()
                self.__tabWidget.tabBar().hide()
                if Preferences.getWebBrowser("ShowToolbars"):
                    for title, toolbar in self.__toolbars.values():
                        if toolbar is not self.__bookmarksToolBar:
                            toolbar.hide()
                self.__navigationBar.exitFullScreenButton().setVisible(True)
                self.__navigationContainer.hide()
            
            elif bool(evt.oldState() & Qt.WindowFullScreen) and \
                    not bool(self.windowState() & Qt.WindowFullScreen):
                # leave full screen mode
                self.setWindowState(self.__windowStates)
                self.__htmlFullScreen = False
                if Preferences.getWebBrowser("MenuBarVisible"):
                    self.menuBar().show()
                if Preferences.getWebBrowser("StatusBarVisible"):
                    self.statusBar().show()
                self.restoreState(self.__toolbarStates)
                self.__tabWidget.tabBar().show()
                self.__navigationBar.exitFullScreenButton().setVisible(False)
                self.__navigationContainer.show()
            
            if self.__hideNavigationTimer:
                self.__hideNavigationTimer.stop()
        
        return super(WebBrowserWindow, self).event(evt)
    
    ###########################################################################
    ## Interface to VirusTotal below                                         ##
    ###########################################################################
    
    def __virusTotalScanCurrentSite(self):
        """
        Private slot to ask VirusTotal for a scan of the URL of the current
        browser.
        """
        cb = self.currentBrowser()
        if cb is not None:
            url = cb.url()
            if url.scheme() in ["http", "https", "ftp"]:
                self.requestVirusTotalScan(url)
    
    def requestVirusTotalScan(self, url):
        """
        Public method to submit a request to scan an URL by VirusTotal.
        
        @param url URL to be scanned (QUrl)
        """
        self.__virusTotal.submitUrl(url)
    
    def __virusTotalSubmitUrlError(self, msg):
        """
        Private slot to handle an URL scan submission error.
        
        @param msg error message (str)
        """
        E5MessageBox.critical(
            self,
            self.tr("VirusTotal Scan"),
            self.tr("""<p>The VirusTotal scan could not be"""
                    """ scheduled.<p>\n<p>Reason: {0}</p>""").format(msg))
    
    def __virusTotalUrlScanReport(self, url):
        """
        Private slot to initiate the display of the URL scan report page.
        
        @param url URL of the URL scan report page (string)
        """
        self.newTab(url)
    
    def __virusTotalFileScanReport(self, url):
        """
        Private slot to initiate the display of the file scan report page.
        
        @param url URL of the file scan report page (string)
        """
        self.newTab(url)
    
    def __virusTotalIpAddressReport(self):
        """
        Private slot to retrieve an IP address report.
        """
        ip, ok = QInputDialog.getText(
            self,
            self.tr("IP Address Report"),
            self.tr("Enter a valid IPv4 address in dotted quad notation:"),
            QLineEdit.Normal)
        if ok and ip:
            if ip.count(".") == 3:
                self.__virusTotal.getIpAddressReport(ip)
            else:
                E5MessageBox.information(
                    self,
                    self.tr("IP Address Report"),
                    self.tr("""The given IP address is not in dotted quad"""
                            """ notation."""))
    
    def __virusTotalDomainReport(self):
        """
        Private slot to retrieve a domain report.
        """
        domain, ok = QInputDialog.getText(
            self,
            self.tr("Domain Report"),
            self.tr("Enter a valid domain name:"),
            QLineEdit.Normal)
        if ok and domain:
            self.__virusTotal.getDomainReport(domain)
    
    ###########################################################################
    ## Style sheet handling below                                            ##
    ###########################################################################
    
    def reloadUserStyleSheet(self):
        """
        Public method to reload the user style sheet.
        """
        styleSheet = Preferences.getWebBrowser("UserStyleSheet")
        self.__setUserStyleSheet(styleSheet)
    
    def __setUserStyleSheet(self, styleSheetFile):
        """
        Private method to set a user style sheet.
        
        @param styleSheetFile name of the user style sheet file (string)
        """
        name = "_eric_userstylesheet"
        userStyle = ""
        
        userStyle += WebBrowserTools.readAllFileContents(styleSheetFile)\
            .replace("\n", "")
        
        oldScript = self.webProfile().scripts().findScript(name)
        if not oldScript.isNull():
            self.webProfile().scripts().remove(oldScript)
        
        if userStyle:
            from .WebBrowserPage import WebBrowserPage

            script = QWebEngineScript()
            script.setName(name)
            script.setInjectionPoint(QWebEngineScript.DocumentCreation)
            script.setWorldId(WebBrowserPage.SafeJsWorld)
            script.setRunsOnSubFrames(True)
            script.setSourceCode(Scripts.setStyleSheet(userStyle))
            self.webProfile().scripts().insert(script)
    
    ##########################################
    ## Support for desktop notifications below
    ##########################################
    
    @classmethod
    def showNotification(cls, icon, heading, text):
        """
        Class method to show a desktop notification.
        
        @param icon icon to be shown in the notification (QPixmap)
        @param heading heading of the notification (string)
        @param text text of the notification (string)
        """
        if cls._fromEric:
            e5App().getObject("UserInterface").showNotification(
                icon, heading, text)
        else:
            if Preferences.getUI("NotificationsEnabled"):
                if cls._notification is None:
                    from UI.NotificationWidget import NotificationWidget
                    cls._notification = NotificationWidget()
                cls._notification.setPixmap(icon)
                cls._notification.setHeading(heading)
                cls._notification.setText(text)
                cls._notification.setTimeout(
                    Preferences.getUI("NotificationTimeout"))
                cls._notification.move(
                    Preferences.getUI("NotificationPosition"))
                cls._notification.show()
    
    @classmethod
    def notificationsEnabled(cls):
        """
        Class method to check, if notifications are enabled.
        
        @return flag indicating, if notifications are enabled (boolean)
        """
        if cls._fromEric:
            return e5App().getObject("UserInterface").notificationsEnabled()
        else:
            return Preferences.getUI("NotificationsEnabled")
    
    ###################################
    ## Support for download files below
    ###################################
    
    @classmethod
    def downloadRequested(cls, download):
        """
        Class method to handle a download request.
        
        @param download reference to the download data
        @type QWebEngineDownloadItem
        """
        cls.downloadManager().download(download)
    
    ########################################
    ## Support for web engine profiles below
    ########################################
    
    @classmethod
    def webProfile(cls, private=False):
        """
        Class method handling the web engine profile.
        
        @param private flag indicating the privacy mode
        @type bool
        @return reference to the web profile object
        @rtype QWebEngineProfile
        """
        if cls._webProfile is None:
            if private:
                cls._webProfile = QWebEngineProfile()
            else:
                cls._webProfile = QWebEngineProfile.defaultProfile()
            cls._webProfile.downloadRequested.connect(
                cls.downloadRequested)
            
            # add the default user agent string
            userAgent = cls._webProfile.httpUserAgent()
            cls._webProfile.defaultUserAgent = userAgent
            
            if not private:
                if Preferences.getWebBrowser("DiskCacheEnabled"):
                    cls._webProfile.setHttpCacheType(
                        QWebEngineProfile.DiskHttpCache)
                    cls._webProfile.setHttpCacheMaximumSize(
                        Preferences.getWebBrowser("DiskCacheSize") *
                        1024 * 1024)
                    cls._webProfile.setCachePath(os.path.join(
                        Utilities.getConfigDir(), "web_browser"))
                else:
                    cls._webProfile.setHttpCacheType(
                        QWebEngineProfile.MemoryHttpCache)
                    cls._webProfile.setHttpCacheMaximumSize(0)
                cls._webProfile.setPersistentStoragePath(os.path.join(
                    Utilities.getConfigDir(), "web_browser",
                    "persistentstorage"))
                cls._webProfile.setPersistentCookiesPolicy(
                    QWebEngineProfile.AllowPersistentCookies)
            
            if qVersionTuple() >= (5, 8, 0):
                cls._webProfile.setSpellCheckEnabled(
                    Preferences.getWebBrowser("SpellCheckEnabled"))
                cls._webProfile.setSpellCheckLanguages(
                    Preferences.getWebBrowser("SpellCheckLanguages"))
            
            # Setup QWebChannel user script
            from .WebBrowserPage import WebBrowserPage

            script = QWebEngineScript()
            script.setName("_eric_webchannel")
            script.setInjectionPoint(QWebEngineScript.DocumentCreation)
            script.setWorldId(WebBrowserPage.SafeJsWorld)
            script.setRunsOnSubFrames(True)
            script.setSourceCode(Scripts.setupWebChannel())
            cls._webProfile.scripts().insert(script)
        
        return cls._webProfile
    
    ####################################################
    ## Methods below implement session related functions
    ####################################################
    
    @classmethod
    def sessionManager(cls):
        """
        Class method to get a reference to the session manager.
        
        @return reference to the session manager
        @rtype SessionManager
        """
        if cls._sessionManager is None and not cls._isPrivate:
            from .Session.SessionManager import SessionManager
            cls._sessionManager = SessionManager()
        
        return cls._sessionManager
    
    def __showSessionManagerDialog(self):
        """
        Private slot to show the session manager dialog.
        """
        self.sessionManager().showSessionManagerDialog()
