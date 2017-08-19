# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a scheme handler for the eric: scheme.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, QByteArray, QBuffer, QIODevice, \
    QTextStream, QUrlQuery
from PyQt5.QtWidgets import qApp
from PyQt5.QtWebEngineCore import QWebEngineUrlSchemeHandler

from ..Tools.WebBrowserTools import readAllFileContents


class EricSchemeHandler(QWebEngineUrlSchemeHandler):
    """
    Class implementing a scheme handler for the eric: scheme.
    """
    SupportedPages = [
        "adblock",          # error page for URLs blocked by AdBlock
        "home", "start", "startpage",       # eric home page
        "speeddial",                        # eric speeddial
    ]
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object
        @type QObject
        """
        super(EricSchemeHandler, self).__init__(parent)
        
        self.__replies = []
    
    def requestStarted(self, job):
        """
        Public method handling the URL request.
        
        @param job URL request job
        @type QWebEngineUrlRequestJob
        """
        if job.requestUrl().path() in self.SupportedPages:
            reply = EricSchemeReply(job)
            reply.closed.connect(self.__replyClosed)
            self.__replies.append(reply)
            job.reply(b"text/html", reply)
        else:
            job.reply(QByteArray(), QBuffer())
            # job.fail(QWebEngineUrlRequestJob.UrlNotFound)
    
    def __replyClosed(self):
        """
        Private slot handling the closed signal of a reply.
        """
        reply = self.sender()
        if reply and reply in self.__replies:
            self.__replies.remove(reply)


class EricSchemeReply(QIODevice):
    """
    Class implementing a reply for a requested eric: page.
    
    @signal closed emitted to signal that the web engine has read
        the data
    """
    closed = pyqtSignal()
    
    _speedDialPage = ""
    
    def __init__(self, job, parent=None):
        """
        Constructor
        
        @param job reference to the URL request
        @type QWebEngineUrlRequestJob
        @param parent reference to the parent object
        @type QObject
        """
        super(EricSchemeReply, self).__init__(parent)
        
        self.__loaded = False
        self.__job = job
        
        self.__pageName = self.__job.requestUrl().path()
        self.__buffer = QBuffer()
        
        self.open(QIODevice.ReadOnly)
        self.__buffer.open(QIODevice.ReadWrite)
        self.__loadPage()
    
    def __loadPage(self):
        """
        Private method to load the requested page.
        """
        if self.__loaded:
            return
        
        stream = QTextStream(self.__buffer)
        stream.setCodec("utf-8")
        
        if self.__pageName == "adblock":
            stream << self.__adBlockPage()
        elif self.__pageName in ["home", "start", "startpage"]:
            stream << self.__startPage()
        elif self.__pageName == "speeddial":
            stream << self.__speedDialPage()
        
        stream.flush()
        self.__buffer.reset()
        self.__loaded = True
    
    def bytesAvailable(self):
        """
        Public method to get the number of available bytes.
        
        @return number of available bytes
        @rtype int
        """
        return self.__buffer.bytesAvailable()
    
    def readData(self, maxlen):
        """
        Public method to retrieve data from the reply object.
        
        @param maxlen maximum number of bytes to read (integer)
        @return string containing the data (bytes)
        """
        return self.__buffer.read(maxlen)
    
    def close(self):
        """
        Public method used to cloase the reply.
        """
        super(EricSchemeReply, self).close()
        self.closed.emit()
    
    def __adBlockPage(self):
        """
        Private method to build the AdBlock page.
        
        @return built AdBlock page
        @rtype str
        """
        query = QUrlQuery(self.__job.requestUrl())
        rule = query.queryItemValue("rule")
        subscription = query.queryItemValue("subscription")
        title = self.tr("Content blocked by AdBlock Plus")
        message = self.tr(
            "Blocked by rule: <i>{0} ({1})</i>").format(rule, subscription)
        
        page = readAllFileContents(":/html/adblockPage.html")
        page = page.replace(
            "@FAVICON@", "qrc:icons/adBlockPlus16.png")
        page = page.replace(
            "@IMAGE@", "qrc:icons/adBlockPlus64.png")
        page = page.replace("@TITLE@", title)
        page = page.replace("@MESSAGE@", message)
        
        return page
    
    def __startPage(self):
        """
        Private method to build the Start page.
        
        @return built Start page
        @rtype str
        """
        page = readAllFileContents(":/html/startPage.html")
        page = page.replace("@FAVICON@", "qrc:icons/ericWeb16.png")
        page = page.replace("@IMAGE@", "qrc:icons/ericWeb32.png")
        page = page.replace("@TITLE@",
                            self.tr("Welcome to eric6 Web Browser!"))
        page = page.replace("@ERIC_LINK@", self.tr("About eric6"))
        page = page.replace("@HEADER_TITLE@", self.tr("eric6 Web Browser"))
        page = page.replace("@SUBMIT@", self.tr("Search!"))
        if qApp.isLeftToRight():
            ltr = "LTR"
        else:
            ltr = "RTL"
        page = page.replace("@QT_LAYOUT_DIRECTION@", ltr)
        
        return page
    
    def __speedDialPage(self):
        """
        Private method to create the Speeddial page.
        
        @return prepared speeddial page (QByteArray)
        """
        if not self._speedDialPage:
            page = readAllFileContents(":/html/speeddialPage.html")
            page = page.replace("@FAVICON@", "qrc:icons/ericWeb16.png")
            page = page.replace("@IMG_PLUS@", "qrc:icons/plus.png")
            page = page.replace("@IMG_CLOSE@", "qrc:icons/close.png")
            page = page.replace("@IMG_EDIT@", "qrc:icons/edit.png")
            page = page.replace("@IMG_RELOAD@", "qrc:icons/reload.png")
            page = page.replace("@IMG_SETTINGS@", "qrc:icons/setting.png")
            page = page.replace("@LOADING-IMG@", "qrc:icons/loading.gif")
            page = page.replace("@BOX-BORDER@",
                                "qrc:icons/box-border-small.png")
            
            page = page.replace("@JQUERY@", "qrc:javascript/jquery.js")
            page = page.replace("@JQUERY-UI@", "qrc:javascript/jquery-ui.js")
            
            page = page.replace("@SITE-TITLE@", self.tr("Speed Dial"))
            page = page.replace("@URL@", self.tr("URL"))
            page = page.replace("@TITLE@", self.tr("Title"))
            page = page.replace("@APPLY@", self.tr("Apply"))
            page = page.replace("@CLOSE@", self.tr("Close"))
            page = page.replace("@NEW-PAGE@", self.tr("New Page"))
            page = page.replace("@TITLE-EDIT@", self.tr("Edit"))
            page = page.replace("@TITLE-REMOVE@", self.tr("Remove"))
            page = page.replace("@TITLE-RELOAD@", self.tr("Reload"))
            page = page.replace("@TITLE-WARN@",
                                self.tr("Are you sure to remove this"
                                        " speed dial?"))
            page = page.replace("@TITLE-WARN-REL@",
                                self.tr("Are you sure you want to reload"
                                        " all speed dials?"))
            page = page.replace("@TITLE-FETCHTITLE@",
                                self.tr("Load title from page"))
            page = page.replace("@SETTINGS-TITLE@",
                                self.tr("Speed Dial Settings"))
            page = page.replace("@ADD-TITLE@", self.tr("Add New Page"))
            page = page.replace("@TXT_NRROWS@",
                                self.tr("Maximum pages in a row:"))
            page = page.replace("@TXT_SDSIZE@",
                                self.tr("Change size of pages:"))
            
            self._speedDialPage = page
        
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        dial = WebBrowserWindow.speedDial()
        page = (
            self._speedDialPage
            .replace("@INITIAL-SCRIPT@", dial.initialScript())
            .replace("@ROW-PAGES@", str(dial.pagesInRow()))
            .replace("@SD-SIZE@", str(dial.sdSize()))
        )
        
        return page
