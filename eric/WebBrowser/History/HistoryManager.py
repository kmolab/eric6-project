# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the history manager.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QFileInfo, QDateTime, QDate, \
    QTime, QUrl, QTimer, QFile, QIODevice, QByteArray, QDataStream, \
    QTemporaryFile, QObject

from E5Gui import E5MessageBox

from Utilities.AutoSaver import AutoSaver
import Utilities
import Preferences

HISTORY_VERSION_42 = 42
HISTORY_VERSION_60 = 60
HISTORY_VERSIONS = [HISTORY_VERSION_60, HISTORY_VERSION_42]


class HistoryEntry(object):
    """
    Class implementing a history entry.
    """
    def __init__(self, url=None, dateTime=None, title=None, visitCount=None):
        """
        Constructor
        
        @param url URL of the history entry (string)
        @param dateTime date and time this entry was created (QDateTime)
        @param title title string for the history entry (string)
        @param visitCount number of visits of this URL (int)
        """
        self.url = url and url or ""
        self.dateTime = dateTime and dateTime or QDateTime()
        self.title = title and title or ""
        self.visitCount = visitCount and visitCount or 0
    
    def __eq__(self, other):
        """
        Special method determining equality.
        
        @param other reference to the history entry to compare against
            (HistoryEntry)
        @return flag indicating equality (boolean)
        """
        return other.title == self.title and \
            other.url == self.url and \
            other.dateTime == self.dateTime
    
    def __lt__(self, other):
        """
        Special method determining less relation.
        
        Note: History is sorted in reverse order by date and time
        
        @param other reference to the history entry to compare against
            (HistoryEntry)
        @return flag indicating less (boolean)
        """
        return self.dateTime > other.dateTime
    
    def userTitle(self):
        """
        Public method to get the title of the history entry.
        
        @return title of the entry (string)
        """
        if not self.title:
            page = QFileInfo(QUrl(self.url).path()).fileName()
            if page:
                return page
            return self.url
        return self.title
    
    def isValid(self):
        """
        Public method to determine validity.
        
        @return flag indicating validity
        @rtype bool
        """
        return bool(self.url) and self.dateTime.isValid()


class HistoryManager(QObject):
    """
    Class implementing the history manager.
    
    @signal historyCleared() emitted after the history has been cleared
    @signal historyReset() emitted after the history has been reset
    @signal entryAdded(HistoryEntry) emitted after a history entry has been
        added
    @signal entryRemoved(HistoryEntry) emitted after a history entry has been
        removed
    @signal entryUpdated(int) emitted after a history entry has been updated
    @signal historySaved() emitted after the history was saved
    """
    historyCleared = pyqtSignal()
    historyReset = pyqtSignal()
    entryAdded = pyqtSignal(HistoryEntry)
    entryRemoved = pyqtSignal(HistoryEntry)
    entryUpdated = pyqtSignal(int)
    historySaved = pyqtSignal()
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(HistoryManager, self).__init__(parent)
        
        self.__saveTimer = AutoSaver(self, self.save)
        self.__daysToExpire = Preferences.getWebBrowser("HistoryLimit")
        self.__history = []
        self.__lastSavedUrl = ""
        
        self.__expiredTimer = QTimer(self)
        self.__expiredTimer.setSingleShot(True)
        self.__expiredTimer.timeout.connect(self.__checkForExpired)
        
        self.__frequencyTimer = QTimer(self)
        self.__frequencyTimer.setSingleShot(True)
        self.__frequencyTimer.timeout.connect(self.__refreshFrequencies)
        
        self.entryAdded.connect(self.__saveTimer.changeOccurred)
        self.entryRemoved.connect(self.__saveTimer.changeOccurred)
        
        self.__load()
        
        from .HistoryModel import HistoryModel
        from .HistoryFilterModel import HistoryFilterModel
        from .HistoryTreeModel import HistoryTreeModel
        
        self.__historyModel = HistoryModel(self, self)
        self.__historyFilterModel = \
            HistoryFilterModel(self.__historyModel, self)
        self.__historyTreeModel = \
            HistoryTreeModel(self.__historyFilterModel, self)
        
        self.__startFrequencyTimer()
    
    def close(self):
        """
        Public method to close the history manager.
        """
        # remove history items on application exit
        if self.__daysToExpire == -2:
            self.clear()
        self.__saveTimer.saveIfNeccessary()
    
    def history(self):
        """
        Public method to return the history.
        
        @return reference to the list of history entries (list of HistoryEntry)
        """
        return self.__history[:]
    
    def setHistory(self, history, loadedAndSorted=False):
        """
        Public method to set a new history.
        
        @param history reference to the list of history entries to be set
            (list of HistoryEntry)
        @param loadedAndSorted flag indicating that the list is sorted
            (boolean)
        """
        self.__history = history[:]
        if not loadedAndSorted:
            self.__history.sort()
        
        self.__checkForExpired()
        
        if loadedAndSorted:
            try:
                self.__lastSavedUrl = self.__history[0].url
            except IndexError:
                self.__lastSavedUrl = ""
        else:
            self.__lastSavedUrl = ""
            self.__saveTimer.changeOccurred()
        self.historyReset.emit()
    
    def __findFirstHistoryEntry(self, url):
        """
        Private method to find the first entry for the given URL.
        
        @param url URL to search for
        @type str
        @return first entry for the given URL
        @rtype HistoryEntry
        """
        for index in range(len(self.__history)):
            if url == self.__history[index].url:
                return self.__history[index]
        
        # not found, return an empty entry
        return HistoryEntry()
    
    def __updateVisitCount(self, url, count):
        """
        Private method to update the visit count for all entries of the
        given URL.
        
        @param url URL to be updated
        @type str
        @param count new visit count
        @type int
        """
        for index in range(len(self.__history)):
            if url == self.__history[index].url:
                self.__history[index].visitCount = count
    
    def addHistoryEntry(self, view):
        """
        Public method to add a history entry.
        
        @param view reference to the view to add an entry for
        @type WebBrowserView
        """
        import WebBrowser.WebBrowserWindow
        if WebBrowser.WebBrowserWindow.WebBrowserWindow.isPrivate():
            return
        
        url = view.url()
        title = view.title()
        
        if url.scheme() not in ["eric", "about", "data", "chrome"]:
            cleanUrlStr = self.__cleanUrlStr(url)
            firstEntry = self.__findFirstHistoryEntry(cleanUrlStr)
            if firstEntry.isValid():
                visitCount = firstEntry.visitCount + 1
                self.__updateVisitCount(cleanUrlStr, visitCount)
            else:
                visitCount = 1
            itm = HistoryEntry(cleanUrlStr,
                               QDateTime.currentDateTime(),
                               title,
                               visitCount)
            self.__history.insert(0, itm)
            self.entryAdded.emit(itm)
            if len(self.__history) == 1:
                self.__checkForExpired()
    
    def updateHistoryEntry(self, url, title):
        """
        Public method to update a history entry.
        
        @param url URL of the entry to update (string)
        @param title title of the entry to update (string)
        """
        if QUrl(url).scheme() not in ["eric", "about", "data", "chrome"]:
            cleanUrlStr = self.__cleanUrlStr(QUrl(url))
            for index in range(len(self.__history)):
                if cleanUrlStr == self.__history[index].url:
                    self.__history[index].title = title
                    self.__saveTimer.changeOccurred()
                    if not self.__lastSavedUrl:
                        self.__lastSavedUrl = self.__history[index].url
                    self.entryUpdated.emit(index)
                    break
    
    def removeHistoryEntry(self, url, title=""):
        """
        Public method to remove a history entry.
        
        @param url URL of the entry to remove (QUrl)
        @param title title of the entry to remove (string)
        """
        if url.scheme() not in ["eric", "about", "data", "chrome"]:
            cleanUrlStr = self.__cleanUrlStr(url)
            for index in range(len(self.__history)):
                if cleanUrlStr == self.__history[index].url and \
                   (not title or title == self.__history[index].title):
                    itm = self.__history[index]
                    self.__lastSavedUrl = ""
                    self.__history.remove(itm)
                    self.entryRemoved.emit(itm)
                    break
    
    def __cleanUrl(self, url):
        """
        Private method to generate a clean URL usable for the history entry.
        
        @param url original URL
        @type QUrl
        @return cleaned URL
        @rtype QUrl
        """
        cleanurl = QUrl(url)
        if cleanurl.password():
            # don't save the password in the history
            cleanurl.setPassword("")
        if cleanurl.host():
            # convert host to lower case
            cleanurl.setHost(url.host().lower())
        
        return cleanurl
    
    def __cleanUrlStr(self, url):
        """
        Private method to generate a clean URL usable for the history entry.
        
        @param url original URL
        @type QUrl
        @return cleaned URL
        @rtype str
        """
        cleanurl = self.__cleanUrl(url)
        return cleanurl.toString()
    
    def historyModel(self):
        """
        Public method to get a reference to the history model.
        
        @return reference to the history model (HistoryModel)
        """
        return self.__historyModel
    
    def historyFilterModel(self):
        """
        Public method to get a reference to the history filter model.
        
        @return reference to the history filter model (HistoryFilterModel)
        """
        return self.__historyFilterModel
    
    def historyTreeModel(self):
        """
        Public method to get a reference to the history tree model.
        
        @return reference to the history tree model (HistoryTreeModel)
        """
        return self.__historyTreeModel
    
    def __checkForExpired(self):
        """
        Private slot to check entries for expiration.
        """
        if self.__daysToExpire < 0 or len(self.__history) == 0:
            return
        
        now = QDateTime.currentDateTime()
        nextTimeout = 0
        
        while self.__history:
            checkForExpired = QDateTime(self.__history[-1].dateTime)
            checkForExpired.setDate(
                checkForExpired.date().addDays(self.__daysToExpire))
            if now.daysTo(checkForExpired) > 7:
                nextTimeout = 7 * 86400
            else:
                nextTimeout = now.secsTo(checkForExpired)
            if nextTimeout > 0:
                break
            
            itm = self.__history.pop(-1)
            self.__lastSavedUrl = ""
            self.entryRemoved.emit(itm)
        self.__saveTimer.saveIfNeccessary()
        
        if nextTimeout > 0:
            self.__expiredTimer.start(nextTimeout * 1000)
    
    def daysToExpire(self):
        """
        Public method to get the days for entry expiration.
        
        @return days for entry expiration (integer)
        """
        return self.__daysToExpire
    
    def setDaysToExpire(self, limit):
        """
        Public method to set the days for entry expiration.
        
        @param limit days for entry expiration (integer)
        """
        if self.__daysToExpire == limit:
            return
        
        self.__daysToExpire = limit
        self.__checkForExpired()
        self.__saveTimer.changeOccurred()
    
    def preferencesChanged(self):
        """
        Public method to indicate a change of preferences.
        """
        self.setDaysToExpire(Preferences.getWebBrowser("HistoryLimit"))
    
    @pyqtSlot()
    def clear(self, period=0):
        """
        Public slot to clear the complete history.
        
        @param period history period in milliseconds to be cleared (integer)
        """
        if period == 0:
            self.__history = []
            self.historyReset.emit()
        else:
            breakMS = QDateTime.currentMSecsSinceEpoch() - period
            while self.__history and \
                (QDateTime(self.__history[0].dateTime).toMSecsSinceEpoch() >
                 breakMS):
                itm = self.__history.pop(0)
                self.entryRemoved.emit(itm)
        self.__lastSavedUrl = ""
        self.__saveTimer.changeOccurred()
        self.__saveTimer.saveIfNeccessary()
        self.historyCleared.emit()
    
    def getFileName(self):
        """
        Public method to get the file name of the history file.
        
        @return name of the history file (string)
        """
        return os.path.join(Utilities.getConfigDir(), "web_browser", "history")
    
    def reload(self):
        """
        Public method to reload the history.
        """
        self.__load()
    
    def __load(self):
        """
        Private method to load the saved history entries from disk.
        """
        historyFile = QFile(self.getFileName())
        if not historyFile.exists():
            return
        if not historyFile.open(QIODevice.ReadOnly):
            E5MessageBox.warning(
                None,
                self.tr("Loading History"),
                self.tr(
                    """<p>Unable to open history file <b>{0}</b>.<br/>"""
                    """Reason: {1}</p>""")
                .format(historyFile.fileName, historyFile.errorString()))
            return
        
        history = []
        
        # double check, that the history file is sorted as it is read
        needToSort = False
        lastInsertedItem = HistoryEntry()
        data = QByteArray(historyFile.readAll())
        stream = QDataStream(data, QIODevice.ReadOnly)
        stream.setVersion(QDataStream.Qt_4_6)
        while not stream.atEnd():
            ver = stream.readUInt32()
            if ver not in HISTORY_VERSIONS:
                continue
            itm = HistoryEntry()
            itm.url = Utilities.readStringFromStream(stream)
            stream >> itm.dateTime
            itm.title = Utilities.readStringFromStream(stream)
            if ver == HISTORY_VERSION_60:
                itm.visitCount = stream.readUInt32()
            
            if not itm.dateTime.isValid():
                continue
            
            if itm == lastInsertedItem:
                if not lastInsertedItem.title and len(history) > 0:
                    history[0].title = itm.title
                continue
            
            if ver == HISTORY_VERSION_42:
                firstEntry = self.__findFirstHistoryEntry(itm.url)
                if firstEntry.isValid():
                    visitCount = firstEntry.visitCount + 1
                    self.__updateVisitCount(itm.url, visitCount)
                else:
                    visitCount = 1
                itm.visitCount = visitCount
            
            if not needToSort and history and lastInsertedItem < itm:
                needToSort = True
            
            history.insert(0, itm)
            lastInsertedItem = itm
        historyFile.close()
        
        if needToSort:
            history.sort()
        
        self.setHistory(history, True)
        
        # if the history had to be sorted, rewrite the history sorted
        if needToSort:
            self.__lastSavedUrl = ""
            self.__saveTimer.changeOccurred()
    
    def save(self):
        """
        Public slot to save the history entries to disk.
        """
        historyFile = QFile(self.getFileName())
        if not historyFile.exists():
            self.__lastSavedUrl = ""
        
        saveAll = self.__lastSavedUrl == ""
        first = len(self.__history) - 1
        if not saveAll:
            # find the first one to save
            for index in range(len(self.__history)):
                if self.__history[index].url == self.__lastSavedUrl:
                    first = index - 1
                    break
        if first == len(self.__history) - 1:
            saveAll = True
        
        if saveAll:
            # use a temporary file when saving everything
            f = QTemporaryFile()
            f.setAutoRemove(False)
            opened = f.open()
        else:
            f = historyFile
            opened = f.open(QIODevice.Append)
        
        if not opened:
            E5MessageBox.warning(
                None,
                self.tr("Saving History"),
                self.tr(
                    """<p>Unable to open history file <b>{0}</b>.<br/>"""
                    """Reason: {1}</p>""")
                .format(f.fileName(), f.errorString()))
            return
        
        for index in range(first, -1, -1):
            data = QByteArray()
            stream = QDataStream(data, QIODevice.WriteOnly)
            stream.setVersion(QDataStream.Qt_4_6)
            itm = self.__history[index]
            stream.writeUInt32(HISTORY_VERSION_60)
            stream.writeString(itm.url.encode("utf-8"))
            stream << itm.dateTime
            stream.writeString(itm.title.encode('utf-8'))
            stream.writeUInt32(itm.visitCount)
            f.write(data)
        
        f.close()
        if saveAll:
            if historyFile.exists() and not historyFile.remove():
                E5MessageBox.warning(
                    None,
                    self.tr("Saving History"),
                    self.tr(
                        """<p>Error removing old history file <b>{0}</b>."""
                        """<br/>Reason: {1}</p>""")
                    .format(historyFile.fileName(),
                            historyFile.errorString()))
            if not f.copy(historyFile.fileName()):
                E5MessageBox.warning(
                    None,
                    self.tr("Saving History"),
                    self.tr(
                        """<p>Error moving new history file over old one """
                        """(<b>{0}</b>).<br/>Reason: {1}</p>""")
                    .format(historyFile.fileName(), f.errorString()))
            f.remove()  # get rid of the temporary file
        self.historySaved.emit()
        try:
            self.__lastSavedUrl = self.__history[0].url
        except IndexError:
            self.__lastSavedUrl = ""
    
    def __refreshFrequencies(self):
        """
        Private slot to recalculate the refresh frequencies.
        """
        self.__historyFilterModel.recalculateFrequencies()
        self.__startFrequencyTimer()
    
    def __startFrequencyTimer(self):
        """
        Private method to start the timer to recalculate the frequencies.
        """
        tomorrow = QDateTime(QDate.currentDate().addDays(1), QTime(3, 0))
        self.__frequencyTimer.start(
            QDateTime.currentDateTime().secsTo(tomorrow) * 1000)
