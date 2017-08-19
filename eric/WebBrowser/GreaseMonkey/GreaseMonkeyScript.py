# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the GreaseMonkey script.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QUrl, QRegExp, \
    QByteArray, QCryptographicHash
from PyQt5.QtWebEngineWidgets import QWebEngineScript

from .GreaseMonkeyJavaScript import bootstrap_js, values_js
from .GreaseMonkeyDownloader import GreaseMonkeyDownloader

from ..Tools.DelayedFileWatcher import DelayedFileWatcher
from ..WebBrowserPage import WebBrowserPage

from Globals import qVersionTuple


class GreaseMonkeyScript(QObject):
    """
    Class implementing the GreaseMonkey script.
    
    @signal scriptChanged() emitted to indicate a script change
    @signal updatingChanged(bool) emitted to indicate a change of the
        updating state
    """
    DocumentStart = 0
    DocumentEnd = 1
    DocumentIdle = 2
    
    scriptChanged = pyqtSignal()
    updatingChanged = pyqtSignal(bool)
    
    def __init__(self, manager, path):
        """
        Constructor
        
        @param manager reference to the manager object (GreaseMonkeyManager)
        @param path path of the Javascript file (string)
        """
        super(GreaseMonkeyScript, self).__init__(manager)
        
        self.__manager = manager
        self.__fileWatcher = DelayedFileWatcher(parent=None)
        
        self.__name = ""
        self.__namespace = "GreaseMonkeyNS"
        self.__description = ""
        self.__version = ""
        
        self.__include = []
        self.__exclude = []
        self.__require = []
        
        self.__downloadUrl = QUrl()
        self.__updateUrl = QUrl()
        self.__startAt = GreaseMonkeyScript.DocumentEnd
        
        self.__script = ""
        self.__fileName = path
        self.__enabled = True
        self.__valid = False
        self.__noFrames = False
        
        self.__updating = False
        
        self.__downloaders = []
        
        self.__parseScript()
        
        self.__fileWatcher.delayedFileChanged.connect(
            self.__watchedFileChanged)
    
    def isValid(self):
        """
        Public method to check the validity of the script.
        
        @return flag indicating a valid script (boolean)
        """
        return self.__valid
    
    def name(self):
        """
        Public method to get the name of the script.
        
        @return name of the script (string)
        """
        return self.__name
    
    def nameSpace(self):
        """
        Public method to get the name space of the script.
        
        @return name space of the script (string)
        """
        return self.__namespace
    
    def fullName(self):
        """
        Public method to get the full name of the script.
        
        @return full name of the script (string)
        """
        return "{0}/{1}".format(self.__namespace, self.__name)
    
    def description(self):
        """
        Public method to get the description of the script.
        
        @return description of the script (string)
        """
        return self.__description
    
    def version(self):
        """
        Public method to get the version of the script.
        
        @return version of the script (string)
        """
        return self.__version
    
    def downloadUrl(self):
        """
        Public method to get the download URL of the script.
        
        @return download URL of the script (QUrl)
        """
        return QUrl(self.__downloadUrl)
    
    def updateUrl(self):
        """
        Public method to get the update URL of the script.
        
        @return update URL of the script (QUrl)
        """
        return QUrl(self.__updateUrl)
    
    def startAt(self):
        """
        Public method to get the start point of the script.
        
        @return start point of the script (DocumentStart or DocumentEnd)
        """
        return self.__startAt
    
    def noFrames(self):
        """
        Public method to get the noFrames flag.
        
        @return flag indicating to not run on sub frames
        @rtype bool
        """
        return self.__noFrames
    
    def isEnabled(self):
        """
        Public method to check, if the script is enabled.
        
        @return flag indicating an enabled state (boolean)
        """
        return self.__enabled and self.__valid
    
    def setEnabled(self, enable):
        """
        Public method to enable a script.
        
        @param enable flag indicating the new enabled state (boolean)
        """
        self.__enabled = enable
    
    def include(self):
        """
        Public method to get the list of included URLs.
        
        @return list of included URLs (list of strings)
        """
        return self.__include[:]
    
    def exclude(self):
        """
        Public method to get the list of excluded URLs.
        
        @return list of excluded URLs (list of strings)
        """
        return self.__exclude[:]
    
    def require(self):
        """
        Public method to get the list of required scripts.
        
        @return list of required scripts (list of strings)
        """
        return self.__require[:]
    
    def fileName(self):
        """
        Public method to get the path of the Javascript file.
        
        @return path of the Javascript file (string)
        """
        return self.__fileName
    
    def isUpdating(self):
        """
        Public method to get the updating flag.
        
        @return updating flag
        @rtype bool
        """
        return self.__updating
    
    @pyqtSlot(str)
    def __watchedFileChanged(self, fileName):
        """
        Private slot handling changes of the script file.
        
        @param fileName path of the script file
        @type str
        """
        if self.__fileName == fileName:
            self.__reloadScript()
    
    def __parseScript(self):
        """
        Private method to parse the given script and populate the data
        structure.
        """
        self.__name = ""
        self.__namespace = "GreaseMonkeyNS"
        self.__description = ""
        self.__version = ""
        
        self.__include = []
        self.__exclude = []
        self.__require = []
        
        self.__downloadUrl = QUrl()
        self.__updateUrl = QUrl()
        self.__startAt = GreaseMonkeyScript.DocumentEnd
        
        self.__script = ""
        self.__enabled = True
        self.__valid = False
        self.__noFrames = False
        
        try:
            f = open(self.__fileName, "r", encoding="utf-8")
            fileData = f.read()
            f.close()
        except (IOError, OSError):
            # silently ignore because it shouldn't happen
            return
        
        if self.__fileName not in self.__fileWatcher.files():
            self.__fileWatcher.addPath(self.__fileName)
        
        rx = QRegExp("// ==UserScript==(.*)// ==/UserScript==")
        rx.indexIn(fileData)
        metaDataBlock = rx.cap(1).strip()
        
        if metaDataBlock == "":
            # invalid script file
            return
        
        for line in metaDataBlock.splitlines():
            if not line.strip():
                continue
            
            if not line.startswith("// @"):
                continue
            
            line = line[3:].replace("\t", " ")
            index = line.find(" ")
            if index < 0:
                continue
            
            key = line[:index].strip()
            value = line[index + 1:].strip()
            
            # Ignored values: @resource, @unwrap
            
            if not key or not value:
                continue
            
            if key == "@name":
                self.__name = value
            
            elif key == "@namespace":
                self.__namespace = value
            
            elif key == "@description":
                self.__description = value
            
            elif key == "@version":
                self.__version = value
            
            elif key in ["@include", "@match"]:
                self.__include.append(value)
            
            elif key in ["@exclude", "@exclude_match"]:
                self.__exclude.append(value)
            
            elif key == "@require":
                self.__require.append(value)
            
            elif key == "@run-at":
                if value == "document-end":
                    self.__startAt = GreaseMonkeyScript.DocumentEnd
                elif value == "document-start":
                    self.__startAt = GreaseMonkeyScript.DocumentStart
                elif value == "document-idle":
                    self.__startAt = GreaseMonkeyScript.DocumentIdle
            
            elif key == "@downloadURL" and self.__downloadUrl.isEmpty():
                self.__downloadUrl = QUrl(value)
            
            elif key == "@updateURL" and self.__updateUrl.isEmpty():
                self.__updateUrl = QUrl(value)
        
        if not self.__include:
            self.__include.append("*")
        
        nspace = bytes(QCryptographicHash.hash(
            QByteArray(self.fullName().encode("utf-8")),
            QCryptographicHash.Md4).toHex()).decode("ascii")
        valuesScript = values_js.format(nspace)
        if qVersionTuple() < (5, 8, 0):
            runCheck = """
                for (var value of {0}) {{
                    var re = new RegExp(value);
                    if (re.test(window.location.href)) {{
                        return;
                    }}
                }}
                __eric_includes = false;
                for (var value of {1}) {{
                    var re = new RegExp(value);
                    if (re.test(window.location.href)) {{
                        __eric_includes = true;
                        break;
                    }}
                }}
                if (!__eric_includes) {{
                    return;
                }}
                delete __eric_includes;""".format(
                self.__toJavaScriptList(self.__exclude[:]),
                self.__toJavaScriptList(self.__include[:])
            )
            self.__script = "(function(){{{0}\n{1}\n{2}\n{3}\n}})();".format(
                runCheck, valuesScript,
                self.__manager.requireScripts(self.__require), fileData
            )
        else:
            self.__script = "(function(){{{0}\n{1}\n{2}\n}})();".format(
                valuesScript, self.__manager.requireScripts(self.__require),
                fileData
            )
        self.__valid = True
    
    def webScript(self):
        """
        Public method to create a script object.
        
        @return prepared script object
        @rtype QWebEngineScript
        @exception ValueError raised to indicate an unsupported start point
        """
        if qVersionTuple() < (5, 8, 0):
            if self.startAt() == GreaseMonkeyScript.DocumentStart:
                injectionPoint = QWebEngineScript.DocumentCreation
            elif self.startAt() == GreaseMonkeyScript.DocumentEnd:
                injectionPoint = QWebEngineScript.DocumentReady
            elif self.startAt() == GreaseMonkeyScript.DocumentIdle:
                injectionPoint = QWebEngineScript.Deferred
            else:
                raise ValueError("Wrong script start point.")
        
        script = QWebEngineScript()
        script.setSourceCode("{0}\n{1}".format(
            bootstrap_js, self.__script
        ))
        script.setName(self.fullName())
        if qVersionTuple() < (5, 8, 0):
            script.setInjectionPoint(injectionPoint)
        script.setWorldId(WebBrowserPage.SafeJsWorld)
        script.setRunsOnSubFrames(not self.__noFrames)
        return script
    
    def __toJavaScriptList(self, patterns):
        """
        Private method to convert a list of str to a string containing a valid
        JavaScript list definition.
        
        @param patterns list of match patterns
        @type list of str
        @return JavaScript script containing the list
        @rtype str
        """
        if qVersionTuple() >= (5, 8, 0):
            script = ""
        else:
            patternList = []
            for pattern in patterns:
                if pattern.startswith("/") and pattern.endswith("/") and \
                        len(pattern) > 1:
                    pattern = pattern[1:-1]
                else:
                    pattern = pattern.replace(".", "\\.").replace("*", ".*")
                pattern = "'{0}'".format(pattern)
                patternList.append(pattern)
            
            script = "[{0}]".format(",".join(patternList))
        return script
    
    def updateScript(self):
        """
        Public method to updated the script.
        """
        if not self.__downloadUrl.isValid() or self.__updating:
            return
        
        self.__updating = True
        self.updatingChanged.emit(self.__updating)
        
        downloader = GreaseMonkeyDownloader(
            self.__downloadUrl,
            self.__manager,
            GreaseMonkeyDownloader.DownloadMainScript)
        downloader.updateScript(self.__fileName)
        downloader.finished.connect(self.__downloaderFinished)
        downloader.error.connect(self.__downloaderError)
        self.__downloaders.append(downloader)
        
        self.__downloadRequires()
    
    def __downloaderFinished(self):
        """
        Private slot to handle a finished download.
        """
        downloader = self.sender()
        if downloader in self.__downloaders:
            self.__downloaders.remove(downloader)
        self.__updating = False
        self.updatingChanged.emit(self.__updating)
    
    def __downloaderError(self):
        """
        Private slot to handle a downloader error.
        """
        downloader = self.sender()
        if downloader in self.__downloaders:
            self.__downloaders.remove(downloader)
        self.__updating = False
        self.updatingChanged.emit(self.__updating)
    
    def __reloadScript(self):
        """
        Private method to reload the script.
        """
        self.__parseScript()
        
        self.__manager.removeScript(self, False)
        self.__manager.addScript(self)
        
        self.scriptChanged.emit()
    
    def __downloadRequires(self):
        """
        Private method to download the required scripts.
        """
        for urlStr in self.__require:
            if not self.__manager.requireScripts([urlStr]):
                downloader = GreaseMonkeyDownloader(
                    QUrl(urlStr),
                    self.__manager,
                    GreaseMonkeyDownloader.DownloadRequireScript)
                downloader.finished.connect(self.__requireDownloaded)
                downloader.error.connect(self.__requireDownloadError)
                self.__downloaders.append(downloader)
    
    def __requireDownloaded(self):
        """
        Private slot to handle a finished download of a required script.
        """
        downloader = self.sender()
        if downloader in self.__downloaders:
            self.__downloaders.remove(downloader)
        
        self.__reloadScript()
    
    def __requireDownloadError(self):
        """
        Private slot to handle a downloader error.
        """
        downloader = self.sender()
        if downloader in self.__downloaders:
            self.__downloaders.remove(downloader)
