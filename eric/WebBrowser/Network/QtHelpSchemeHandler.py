# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a scheme access handler for QtHelp.
"""

from __future__ import unicode_literals

import mimetypes
import os

from PyQt5.QtCore import pyqtSignal, QByteArray, QIODevice, QBuffer
from PyQt5.QtWebEngineCore import QWebEngineUrlSchemeHandler, \
    QWebEngineUrlRequestJob

QtDocPath = "qthelp://org.qt-project."

ExtensionMap = {
    ".bmp": "image/bmp",
    ".css": "text/css",
    ".gif": "image/gif",
    ".html": "text/html",
    ".htm": "text/html",
    ".ico": "image/x-icon",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".js": "application/x-javascript",
    ".mng": "video/x-mng",
    ".pbm": "image/x-portable-bitmap",
    ".pgm": "image/x-portable-graymap",
    ".pdf": "application/pdf",
    ".png": "image/png",
    ".ppm": "image/x-portable-pixmap",
    ".rss": "application/rss+xml",
    ".svg": "image/svg+xml",
    ".svgz": "image/svg+xml",
    ".text": "text/plain",
    ".tif": "image/tiff",
    ".tiff": "image/tiff",
    ".txt": "text/plain",
    ".xbm": "image/x-xbitmap",
    ".xml": "text/xml",
    ".xpm": "image/x-xpm",
    ".xsl": "text/xsl",
    ".xhtml": "application/xhtml+xml",
    ".wml": "text/vnd.wap.wml",
    ".wmlc": "application/vnd.wap.wmlc",
}


class QtHelpSchemeHandler(QWebEngineUrlSchemeHandler):
    """
    Class implementing a scheme handler for the qthelp: scheme.
    """
    def __init__(self, engine, parent=None):
        """
        Constructor
        
        @param engine reference to the help engine
        @type QHelpEngine
        @param parent reference to the parent object
        @type QObject
        """
        super(QtHelpSchemeHandler, self).__init__(parent)
        
        self.__engine = engine
        
        self.__replies = []
    
    def requestStarted(self, job):
        """
        Public method handling the URL request.
        
        @param job URL request job
        @type QWebEngineUrlRequestJob
        """
        if job.requestUrl().scheme() == "qthelp":
            reply = QtHelpSchemeReply(job, self.__engine)
            reply.closed.connect(self.__replyClosed)
            self.__replies.append(reply)
            job.reply(reply.mimeType(), reply)
        else:
            job.fail(QWebEngineUrlRequestJob.UrlInvalid)
    
    def __replyClosed(self):
        """
        Private slot handling the closed signal of a reply.
        """
        reply = self.sender()
        if reply and reply in self.__replies:
            self.__replies.remove(reply)


class QtHelpSchemeReply(QIODevice):
    """
    Class implementing a reply for a requested qthelp: page.
    
    @signal closed emitted to signal that the web engine has read
        the data
    """
    closed = pyqtSignal()
    
    def __init__(self, job, engine, parent=None):
        """
        Constructor
        
        @param job reference to the URL request
        @type QWebEngineUrlRequestJob
        @param engine reference to the help engine
        @type QHelpEngine
        @param parent reference to the parent object
        @type QObject
        """
        super(QtHelpSchemeReply, self).__init__(parent)
        
        url = job.requestUrl()
        strUrl = url.toString()
        
        self.__buffer = QBuffer()
        
        # For some reason the url to load maybe wrong (passed from web engine)
        # though the css file and the references inside should work that way.
        # One possible problem might be that the css is loaded at the same
        # level as the html, thus a path inside the css like
        # (../images/foo.png) might cd out of the virtual folder
        if not engine.findFile(url).isValid():
            if strUrl.startswith(QtDocPath):
                newUrl = job.requestUrl()
                if not newUrl.path().startswith("/qdoc/"):
                    newUrl.setPath("/qdoc" + newUrl.path())
                    url = newUrl
                    strUrl = url.toString()
        
        self.__mimeType = mimetypes.guess_type(strUrl)[0]
        if self.__mimeType is None:
            # do our own (limited) guessing
            self.__mimeType = self.__mimeFromUrl(url)
        
        if engine.findFile(url).isValid():
            data = engine.fileData(url)
        else:
            data = QByteArray(self.tr(
                """<html>"""
                """<head><title>Error 404...</title></head>"""
                """<body><div align="center"><br><br>"""
                """<h1>The page could not be found</h1><br>"""
                """<h3>'{0}'</h3></div></body>"""
                """</html>""").format(strUrl)
                .encode("utf-8"))
        
        self.__buffer.setData(data)
        self.__buffer.open(QIODevice.ReadOnly)
        self.open(QIODevice.ReadOnly)
    
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
        super(QtHelpSchemeReply, self).close()
        self.closed.emit()
    
    def __mimeFromUrl(self, url):
        """
        Private method to guess the mime type given an URL.
        
        @param url URL to guess the mime type from (QUrl)
        @return mime type for the given URL (string)
        """
        path = url.path()
        ext = os.path.splitext(path)[1].lower()
        if ext in ExtensionMap:
            return ExtensionMap[ext]
        else:
            return "application/octet-stream"
    
    def mimeType(self):
        """
        Public method to get the reply mime type.
        
        @return mime type of the reply
        @rtype bytes
        """
        return self.__mimeType.encode("utf-8")
