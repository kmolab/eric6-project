# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#


"""
Module implementing the helpbrowser using QWebView.
"""

from __future__ import unicode_literals
try:
    str = unicode       # __IGNORE_EXCEPTION__
except NameError:
    pass

from PyQt5.QtCore import pyqtSlot, QUrl, QTimer, QEventLoop, QPoint, QPointF
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineSettings, \
    QWebEngineScript
from PyQt5.QtWebChannel import QWebChannel

from WebBrowser.WebBrowserWindow import WebBrowserWindow

from .JavaScript.ExternalJsObject import ExternalJsObject

from .Tools.WebHitTestResult import WebHitTestResult

import Preferences
from Globals import qVersionTuple


class WebBrowserPage(QWebEnginePage):
    """
    Class implementing an enhanced web page.
    """
    if qVersionTuple() >= (5, 7, 0):
        # SafeJsWorld = QWebEngineScript.ApplicationWorld
        SafeJsWorld = QWebEngineScript.MainWorld
    else:
        SafeJsWorld = QWebEngineScript.MainWorld
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent parent widget of this window (QWidget)
        """
        super(WebBrowserPage, self).__init__(
            WebBrowserWindow.webProfile(), parent)
        
        self.__setupWebChannel()
        
        self.featurePermissionRequested.connect(
            self.__featurePermissionRequested)
        
        self.authenticationRequired.connect(
            WebBrowserWindow.networkManager().authentication)
        
        self.proxyAuthenticationRequired.connect(
            WebBrowserWindow.networkManager().proxyAuthentication)
        
        self.fullScreenRequested.connect(self.__fullScreenRequested)
        
        self.urlChanged.connect(self.__urlChanged)
        
        self.__printer = None
    
    def acceptNavigationRequest(self, url, type_, isMainFrame):
        """
        Public method to determine, if a request may be accepted.
        
        @param url URL to navigate to
        @type QUrl
        @param type_ type of the navigation request
        @type QWebEnginePage.NavigationType
        @param isMainFrame flag indicating, that the request originated from
            the main frame
        @type bool
        @return flag indicating acceptance
        @rtype bool
        """
        scheme = url.scheme()
        if scheme == "mailto":
            QDesktopServices.openUrl(url)
            return False
        
        # AdBlock
        if url.scheme() == "abp":
            if WebBrowserWindow.adBlockManager().addSubscriptionFromUrl(url):
                return False
        
        # GreaseMonkey
        if type_ == QWebEnginePage.NavigationTypeLinkClicked and \
           url.toString().endswith(".user.js"):
            WebBrowserWindow.greaseMonkeyManager().downloadScript(url)
            return False
        
        return QWebEnginePage.acceptNavigationRequest(self, url, type_,
                                                      isMainFrame)
    
    @pyqtSlot(QUrl)
    def __urlChanged(self, url):
        """
        Private slot to handle changes of the URL.
        
        @param url new URL
        @type QUrl
        """
        if not url.isEmpty() and url.scheme() == "eric" and \
                not self.isJavaScriptEnabled():
            self.setJavaScriptEnabled(True)
            self.triggerAction(QWebEnginePage.Reload)
    
    @classmethod
    def userAgent(cls, resolveEmpty=False):
        """
        Class method to get the global user agent setting.
        
        @param resolveEmpty flag indicating to resolve an empty
            user agent (boolean)
        @return user agent string (string)
        """
        agent = Preferences.getWebBrowser("UserAgent")
        if agent == "" and resolveEmpty:
            agent = cls.userAgentForUrl(QUrl())
        return agent
    
    @classmethod
    def setUserAgent(cls, agent):
        """
        Class method to set the global user agent string.
        
        @param agent new current user agent string (string)
        """
        Preferences.setWebBrowser("UserAgent", agent)
    
    @classmethod
    def userAgentForUrl(cls, url):
        """
        Class method to determine the user agent for the given URL.
        
        @param url URL to determine user agent for (QUrl)
        @return user agent string (string)
        """
        agent = WebBrowserWindow.userAgentsManager().userAgentForUrl(url)
        if agent == "":
            # no agent string specified for the given host -> use global one
            agent = Preferences.getWebBrowser("UserAgent")
            if agent == "":
                # no global agent string specified -> use default one
                agent = WebBrowserWindow.webProfile().httpUserAgent()
        return agent
    
    def __featurePermissionRequested(self, url, feature):
        """
        Private slot handling a feature permission request.
        
        @param url url requesting the feature
        @type QUrl
        @param feature requested feature
        @type QWebEnginePage.Feature
        """
        manager = WebBrowserWindow.featurePermissionManager()
        manager.requestFeaturePermission(self, url, feature)
    
    def execJavaScript(self, script, worldId=QWebEngineScript.MainWorld,
                       timeout=500):
        """
        Public method to execute a JavaScript function synchroneously.
        
        @param script JavaScript script source to be executed
        @type str
        @param worldId ID to run the script under
        @type int
        @param timeout max. time the script is given to execute
        @type int
        @return result of the script
        @rtype depending upon script result
        """
        loop = QEventLoop()
        resultDict = {"res": None}
        QTimer.singleShot(timeout, loop.quit)
        
        def resultCallback(res, resDict=resultDict):
            if loop and loop.isRunning():
                resDict["res"] = res
                loop.quit()
        
        self.runJavaScript(script, worldId, resultCallback)
        
        loop.exec_()
        return resultDict["res"]
    
    def runJavaScript(self, script, worldId=-1, callback=None):
        """
        Public method to run a script in the context of the page.
        
        @param script JavaScript script source to be executed
        @type str
        @param worldId ID to run the script under
        @type int
        @param callback callback function to be executed when the script has
            ended
        @type function
        """
        if qVersionTuple() >= (5, 7, 0) and worldId > -1:
            if callback is None:
                QWebEnginePage.runJavaScript(self, script, worldId)
            else:
                QWebEnginePage.runJavaScript(self, script, worldId, callback)
        else:
            if callback is None:
                QWebEnginePage.runJavaScript(self, script)
            else:
                QWebEnginePage.runJavaScript(self, script, callback)
    
    def setJavaScriptEnabled(self, enable):
        """
        Public method to enable JavaScript.
        
        @param enable flag indicating the enabled state to be set
        @type bool
        """
        if not self.url().isEmpty() and self.url().scheme() == "eric":
            enable = True
        
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled,
                                     enable)
    
    def isJavaScriptEnabled(self):
        """
        Public method to test, if JavaScript is enabled.
        
        @return flag indicating the state of the JavaScript support
        @rtype bool
        """
        return self.settings().testAttribute(
            QWebEngineSettings.JavascriptEnabled)
    
    def scroll(self, x, y):
        """
        Public method to scroll by the given amount of pixels.
        
        @param x horizontal scroll value
        @type int
        @param y vertical scroll value
        @type int
        """
        self.runJavaScript(
            "window.scrollTo(window.scrollX + {0}, window.scrollY + {1})"
            .format(x, y),
            WebBrowserPage.SafeJsWorld
        )
    
    def scrollTo(self, pos):
        """
        Public method to scroll to the given position.
        
        @param pos position to scroll to
        @type QPointF
        """
        self.runJavaScript(
            "window.scrollTo({0}, {1});".format(pos.x(), pos.y()),
            WebBrowserPage.SafeJsWorld
        )
    
    def mapToViewport(self, pos):
        """
        Public method to map a position to the viewport.
        
        @param pos position to be mapped
        @type QPoint
        @return viewport position
        @rtype QPoint
        """
        return QPoint(pos.x() // self.zoomFactor(),
                      pos.y() // self.zoomFactor())
    
    def hitTestContent(self, pos):
        """
        Public method to test the content at a specified position.
        
        @param pos position to execute the test at
        @type QPoint
        @return test result object
        @rtype WebHitTestResult
        """
        return WebHitTestResult(self, pos)
    
    def __setupWebChannel(self):
        """
        Private method to setup a web channel to our external object.
        """
        oldChannel = self.webChannel()
        newChannel = QWebChannel(self)
        newChannel.registerObject("eric_object", ExternalJsObject(self))
        self.setWebChannel(newChannel)
        
        if oldChannel:
            del oldChannel.registeredObjects["eric_object"]
            del oldChannel
    
    def certificateError(self, error):
        """
        Public method to handle SSL certificate errors.
        
        @param error object containing the certificate error information
        @type QWebEngineCertificateError
        @return flag indicating to ignore this error
        @rtype bool
        """
        return WebBrowserWindow.networkManager().certificateError(
            error, self.view())
    
    def __fullScreenRequested(self, request):
        """
        Private slot handling a full screen request.
        
        @param request reference to the full screen request
        @type QWebEngineFullScreenRequest
        """
        self.view().requestFullScreen(request.toggleOn())
        
        accepted = request.toggleOn() == self.view().isFullScreen()
        
        if accepted:
            request.accept()
        else:
            request.reject()
    
    def execPrintPage(self, printer, timeout=1000):
        """
        Public method to execute a synchronous print.
        
        @param printer reference to the printer object
        @type QPrinter
        @param timeout timeout value in milliseconds
        @type int
        @return flag indicating a successful print job
        @rtype bool
        """
        loop = QEventLoop()
        resultDict = {"res": None}
        QTimer.singleShot(timeout, loop.quit)
        
        def printCallback(res, resDict=resultDict):
            if loop and loop.isRunning():
                resDict["res"] = res
                loop.quit()
        
        self.print(printer, printCallback)
        
        loop.exec_()
        return resultDict["res"]
    
    ##############################################
    ## Methods below deal with JavaScript messages
    ##############################################
    
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
        self.view().mainWindow().javascriptConsole().javaScriptConsoleMessage(
            level, message, lineNumber, sourceId)
    
    ##################################################
    ## Methods below implement compatibility functions
    ##################################################
    
    if not hasattr(QWebEnginePage, "icon"):
        def icon(self):
            """
            Public method to get the web site icon.
            
            @return web site icon
            @rtype QIcon
            """
            return self.view().icon()
    
    if not hasattr(QWebEnginePage, "scrollPosition"):
        def scrollPosition(self):
            """
            Public method to get the scroll position of the web page.
            
            @return scroll position
            @rtype QPointF
            """
            pos = self.execJavaScript(
                "(function() {"
                "var res = {"
                "    x: 0,"
                "    y: 0,"
                "};"
                "res.x = window.scrollX;"
                "res.y = window.scrollY;"
                "return res;"
                "})()",
                WebBrowserPage.SafeJsWorld
            )
            if pos is not None:
                pos = QPointF(pos["x"], pos["y"])
            else:
                pos = QPointF(0.0, 0.0)
            
            return pos
