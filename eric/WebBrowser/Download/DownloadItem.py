# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a widget controlling a download.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QTime, QUrl, \
    QStandardPaths, QFileInfo
from PyQt5.QtGui import QPalette, QDesktopServices
from PyQt5.QtWidgets import QWidget, QStyle, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem

from E5Gui import E5FileDialog

from .Ui_DownloadItem import Ui_DownloadItem

from .DownloadUtilities import timeString, dataString
from WebBrowser.WebBrowserWindow import WebBrowserWindow

import UI.PixmapCache
import Utilities.MimeTypes
import Globals
from Globals import qVersionTuple


class DownloadItem(QWidget, Ui_DownloadItem):
    """
    Class implementing a widget controlling a download.
    
    @signal statusChanged() emitted upon a status change of a download
    @signal downloadFinished() emitted when a download finished
    @signal progress(int, int) emitted to signal the download progress
    """
    statusChanged = pyqtSignal()
    downloadFinished = pyqtSignal()
    progress = pyqtSignal(int, int)
    
    Downloading = 0
    DownloadSuccessful = 1
    DownloadCancelled = 2
    
    def __init__(self, downloadItem=None, parent=None):
        """
        Constructor
        
        @param downloadItem reference to the download object containing the
        download data.
        @keyparam parent reference to the parent widget (QWidget)
        @type QWebEngineDownloadItem
        """
        super(DownloadItem, self).__init__(parent)
        self.setupUi(self)
        
        p = self.infoLabel.palette()
        p.setColor(QPalette.Text, Qt.darkGray)
        self.infoLabel.setPalette(p)
        
        self.progressBar.setMaximum(0)
        
        self.stopButton.setIcon(UI.PixmapCache.getIcon("stopLoading.png"))
        self.openButton.setIcon(UI.PixmapCache.getIcon("open.png"))
        self.openButton.setEnabled(False)
        self.openButton.setVisible(False)
        
        self.__state = DownloadItem.Downloading
        
        icon = self.style().standardIcon(QStyle.SP_FileIcon)
        self.fileIcon.setPixmap(icon.pixmap(48, 48))
        
        self.__downloadItem = downloadItem
        self.__pageUrl = \
            WebBrowserWindow.mainWindow().getWindow().currentBrowser().url()
        self.__bytesReceived = 0
        self.__bytesTotal = -1
        self.__downloadTime = QTime()
        self.__fileName = ""
        self.__originalFileName = ""
        self.__finishedDownloading = False
        self.__gettingFileName = False
        self.__canceledFileSelect = False
        self.__autoOpen = False
        
        self.__initialize()
    
    def __initialize(self):
        """
        Private method to initialize the widget.
        """
        if self.__downloadItem is None:
            return
        
        self.__finishedDownloading = False
        self.__bytesReceived = 0
        self.__bytesTotal = -1
        
        # start timer for the download estimation
        self.__downloadTime.start()
        
        # attach to the download item object
        self.__url = self.__downloadItem.url()
        self.__downloadItem.downloadProgress.connect(self.__downloadProgress)
        self.__downloadItem.finished.connect(self.__finished)
        
        # reset info
        self.infoLabel.clear()
        self.progressBar.setValue(0)
        if self.__downloadItem.state() == \
           QWebEngineDownloadItem.DownloadRequested:
            self.__getFileName()
            if not self.__fileName:
                self.__downloadItem.cancel()
            else:
                self.__downloadItem.setPath(self.__fileName)
                self.__downloadItem.accept()
        else:
            fileName = self.__downloadItem.path()
            self.__setFileName(fileName)
    
    def __getFileName(self):
        """
        Private method to get the file name to save to from the user.
        """
        if self.__gettingFileName:
            return
        
        if qVersionTuple() >= (5, 8, 0):
            savePage = self.__downloadItem.type() == \
                QWebEngineDownloadItem.SavePage
        elif qVersionTuple() >= (5, 7, 0):
            savePage = self.__downloadItem.savePageFormat() != \
                QWebEngineDownloadItem.UnknownSaveFormat
        else:
            savePage = self.__downloadItem.path().lower().endswith(
                (".mhtml", ".mht"))
        
        documentLocation = QStandardPaths.writableLocation(
            QStandardPaths.DocumentsLocation)
        downloadDirectory = WebBrowserWindow\
            .downloadManager().downloadDirectory()
        
        if self.__fileName:
            fileName = self.__fileName
            originalFileName = self.__originalFileName
            self.__toDownload = True
            ask = False
        else:
            defaultFileName, originalFileName = \
                self.__saveFileName(
                    documentLocation if savePage else downloadDirectory)
            fileName = defaultFileName
            self.__originalFileName = originalFileName
            ask = True
        self.__autoOpen = False
        
        if not savePage:
            from .DownloadAskActionDialog import DownloadAskActionDialog
            url = self.__downloadItem.url()
            mimetype = Utilities.MimeTypes.mimeType(originalFileName)
            dlg = DownloadAskActionDialog(
                QFileInfo(originalFileName).fileName(),
                mimetype,
                "{0}://{1}".format(url.scheme(), url.authority()),
                self)
            
            if dlg.exec_() == QDialog.Rejected or dlg.getAction() == "cancel":
                self.progressBar.setVisible(False)
                self.on_stopButton_clicked()
                self.filenameLabel.setText(
                    self.tr("Download canceled: {0}").format(
                        QFileInfo(defaultFileName).fileName()))
                self.__canceledFileSelect = True
                return
            
            if dlg.getAction() == "scan":
                self.__mainWindow.requestVirusTotalScan(url)
                
                self.progressBar.setVisible(False)
                self.on_stopButton_clicked()
                self.filenameLabel.setText(
                    self.tr("VirusTotal scan scheduled: {0}").format(
                        QFileInfo(defaultFileName).fileName()))
                self.__canceledFileSelect = True
                return
        
            self.__autoOpen = dlg.getAction() == "open"
            
            tempLocation = QStandardPaths.writableLocation(
                QStandardPaths.TempLocation)
            fileName = tempLocation + '/' + \
                QFileInfo(fileName).completeBaseName()
            
            if ask and not self.__autoOpen:
                self.__gettingFileName = True
                fileName = E5FileDialog.getSaveFileName(
                    None,
                    self.tr("Save File"),
                    defaultFileName,
                    "")
                self.__gettingFileName = False
        else:
            # save page file name and format selection for Qt < 5.8.0
            self.__autoOpen = False
            
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
            self.__gettingFileName = True
            fileName, selectedFilter = E5FileDialog.getSaveFileNameAndFilter(
                None,
                self.tr("Save Web Page"),
                defaultFileName,
                ";;".join(filterList),
                None)
            self.__gettingFileName = False
            if fileName:
                index = filterList.index(selectedFilter)
                if index == 0:
                    self.__downloadItem.setSavePageFormat(
                        QWebEngineDownloadItem.MimeHtmlSaveFormat)
                elif index == 1:
                    self.__downloadItem.setSavePageFormat(
                        QWebEngineDownloadItem.SingleHtmlSaveFormat)
                else:
                    self.__downloadItem.setSavePageFormat(
                        QWebEngineDownloadItem.CompleteHtmlSaveFormat)
                extension = os.path.splitext(fileName)[1]
                if not extension:
                    # add the platform specific default extension
                    if Globals.isWindowsPlatform():
                        extensionsIndex = 1
                    else:
                        extensionsIndex = 0
                    extensions = extensionsList[index]
                    fileName += extensions[extensionsIndex]
        
        if not fileName:
            self.progressBar.setVisible(False)
            self.on_stopButton_clicked()
            self.filenameLabel.setText(
                self.tr("Download canceled: {0}")
                    .format(QFileInfo(defaultFileName).fileName()))
            self.__canceledFileSelect = True
            return
        
        self.__setFileName(fileName)
    
    def __setFileName(self, fileName):
        """
        Private method to set the file name to save the download into.
        
        @param fileName name of the file to save into
        @type str
        """
        fileInfo = QFileInfo(fileName)
        WebBrowserWindow.downloadManager()\
            .setDownloadDirectory(fileInfo.absoluteDir().absolutePath())
        self.filenameLabel.setText(fileInfo.fileName())
        
        self.__fileName = fileName
        
        # check file path for saving
        saveDirPath = QFileInfo(self.__fileName).dir()
        if not saveDirPath.exists():
            if not saveDirPath.mkpath(saveDirPath.absolutePath()):
                self.progressBar.setVisible(False)
                self.on_stopButton_clicked()
                self.infoLabel.setText(self.tr(
                    "Download directory ({0}) couldn't be created.")
                    .format(saveDirPath.absolutePath()))
                return
        
        self.filenameLabel.setText(QFileInfo(self.__fileName).fileName())
    
    def __saveFileName(self, directory):
        """
        Private method to calculate a name for the file to download.
        
        @param directory name of the directory to store the file into (string)
        @return proposed filename and original filename (string, string)
        """
        path = self.__downloadItem.path()
        info = QFileInfo(path)
        baseName = info.completeBaseName()
        endName = info.suffix()
        
        origName = baseName
        if endName:
            origName += '.' + endName
        
        name = os.path.join(directory, baseName)
        if endName:
            name += '.' + endName
        return name, origName
    
    def __open(self):
        """
        Private slot to open the downloaded file.
        """
        info = QFileInfo(self.__fileName)
        url = QUrl.fromLocalFile(info.absoluteFilePath())
        QDesktopServices.openUrl(url)
    
    @pyqtSlot()
    def on_stopButton_clicked(self):
        """
        Private slot to stop the download.
        """
        self.cancelDownload()
    
    def cancelDownload(self):
        """
        Public slot to stop the download.
        """
        self.setUpdatesEnabled(False)
        self.stopButton.setEnabled(False)
        self.stopButton.setVisible(False)
        self.openButton.setEnabled(False)
        self.openButton.setVisible(False)
        self.setUpdatesEnabled(True)
        self.__state = DownloadItem.DownloadCancelled
        self.__downloadItem.cancel()
        self.downloadFinished.emit()
    
    @pyqtSlot()
    def on_openButton_clicked(self):
        """
        Private slot to open the downloaded file.
        """
        self.openFile()
    
    def openFile(self):
        """
        Public slot to open the downloaded file.
        """
        info = QFileInfo(self.__fileName)
        url = QUrl.fromLocalFile(info.absoluteFilePath())
        QDesktopServices.openUrl(url)
    
    def openFolder(self):
        """
        Public slot to open the folder containing the downloaded file.
        """
        info = QFileInfo(self.__fileName)
        url = QUrl.fromLocalFile(info.absolutePath())
        QDesktopServices.openUrl(url)
    
    def __downloadProgress(self, bytesReceived, bytesTotal):
        """
        Private method to show the download progress.
        
        @param bytesReceived number of bytes received (integer)
        @param bytesTotal number of total bytes (integer)
        """
        self.__bytesReceived = bytesReceived
        self.__bytesTotal = bytesTotal
        currentValue = 0
        totalValue = 0
        if bytesTotal > 0:
            currentValue = bytesReceived * 100 / bytesTotal
            totalValue = 100
        self.progressBar.setValue(currentValue)
        self.progressBar.setMaximum(totalValue)
        
        self.progress.emit(currentValue, totalValue)
        self.__updateInfoLabel()
    
    def bytesTotal(self):
        """
        Public method to get the total number of bytes of the download.
        
        @return total number of bytes (integer)
        """
        if self.__bytesTotal == -1:
            self.__bytesTotal = self.__downloadItem.totalBytes()
        return self.__bytesTotal
    
    def bytesReceived(self):
        """
        Public method to get the number of bytes received.
        
        @return number of bytes received (integer)
        """
        return self.__bytesReceived
    
    def remainingTime(self):
        """
        Public method to get an estimation for the remaining time.
        
        @return estimation for the remaining time (float)
        """
        if not self.downloading():
            return -1.0
        
        if self.bytesTotal() == -1:
            return -1.0
        
        cSpeed = self.currentSpeed()
        if cSpeed != 0:
            timeRemaining = (self.bytesTotal() - self.bytesReceived()) / cSpeed
        else:
            timeRemaining = 1
        
        # ETA should never be 0
        if timeRemaining == 0:
            timeRemaining = 1
        
        return timeRemaining
    
    def currentSpeed(self):
        """
        Public method to get an estimation for the download speed.
        
        @return estimation for the download speed (float)
        """
        if not self.downloading():
            return -1.0
        
        return self.__bytesReceived * 1000.0 / self.__downloadTime.elapsed()
    
    def __updateInfoLabel(self):
        """
        Private method to update the info label.
        """
        bytesTotal = self.bytesTotal()
        running = not self.downloadedSuccessfully()
        
        speed = self.currentSpeed()
        timeRemaining = self.remainingTime()
        
        info = ""
        if running:
            remaining = ""
            
            if bytesTotal > 0:
                remaining = timeString(timeRemaining)
            
            info = self.tr("{0} of {1} ({2}/sec)\n{3}")\
                .format(
                    dataString(self.__bytesReceived),
                    bytesTotal == -1 and self.tr("?") or
                    dataString(bytesTotal),
                    dataString(int(speed)),
                    remaining)
        else:
            if self.__bytesReceived == bytesTotal or bytesTotal == -1:
                info = self.tr("{0} downloaded")\
                    .format(dataString(self.__bytesReceived))
            else:
                info = self.tr("{0} of {1} - Stopped")\
                    .format(dataString(self.__bytesReceived),
                            dataString(bytesTotal))
        self.infoLabel.setText(info)
    
    def downloading(self):
        """
        Public method to determine, if a download is in progress.
        
        @return flag indicating a download is in progress (boolean)
        """
        return self.__state == DownloadItem.Downloading
    
    def downloadedSuccessfully(self):
        """
        Public method to check for a successful download.
        
        @return flag indicating a successful download (boolean)
        """
        return self.__state == DownloadItem.DownloadSuccessful
    
    def downloadCanceled(self):
        """
        Public method to check, if the download was cancelled.
        
        @return flag indicating a canceled download (boolean)
        """
        return self.__state == DownloadItem.DownloadCancelled
    
    def __finished(self):
        """
        Private slot to handle the download finished.
        """
        self.__finishedDownloading = True
        
        noError = (self.__downloadItem.state() ==
                   QWebEngineDownloadItem.DownloadCompleted)
        
        self.progressBar.setVisible(False)
        self.stopButton.setEnabled(False)
        self.stopButton.setVisible(False)
        self.openButton.setEnabled(noError)
        self.openButton.setVisible(noError)
        self.__state = DownloadItem.DownloadSuccessful
        self.__updateInfoLabel()
        self.statusChanged.emit()
        self.downloadFinished.emit()
        
        if self.__autoOpen:
            self.__open()
    
    def canceledFileSelect(self):
        """
        Public method to check, if the user canceled the file selection.
        
        @return flag indicating cancellation (boolean)
        """
        return self.__canceledFileSelect
    
    def setIcon(self, icon):
        """
        Public method to set the download icon.
        
        @param icon reference to the icon to be set (QIcon)
        """
        self.fileIcon.setPixmap(icon.pixmap(48, 48))
    
    def fileName(self):
        """
        Public method to get the name of the output file.
        
        @return name of the output file (string)
        """
        return self.__fileName
    
    def absoluteFilePath(self):
        """
        Public method to get the absolute path of the output file.
        
        @return absolute path of the output file (string)
        """
        return QFileInfo(self.__fileName).absoluteFilePath()
    
    def getData(self):
        """
        Public method to get the relevant download data.
        
        @return tuple of URL, save location, flag and the
            URL of the related web page (QUrl, string, boolean,QUrl)
        """
        return (self.__url, QFileInfo(self.__fileName).filePath(),
                self.downloadedSuccessfully(), self.__pageUrl)
    
    def setData(self, data):
        """
        Public method to set the relevant download data.
        
        @param data tuple of URL, save location, flag and the
            URL of the related web page (QUrl, string, boolean, QUrl)
        """
        self.__url = data[0]
        self.__fileName = data[1]
        self.__pageUrl = data[3]
        
        self.filenameLabel.setText(QFileInfo(self.__fileName).fileName())
        self.infoLabel.setText(self.__fileName)
        
        self.stopButton.setEnabled(False)
        self.stopButton.setVisible(False)
        self.openButton.setEnabled(data[2])
        self.openButton.setVisible(data[2])
        if data[2]:
            self.__state = DownloadItem.DownloadSuccessful
        else:
            self.__state = DownloadItem.DownloadCancelled
        self.progressBar.setVisible(False)
    
    def getInfoData(self):
        """
        Public method to get the text of the info label.
        
        @return text of the info label (string)
        """
        return self.infoLabel.text()
    
    def getPageUrl(self):
        """
        Public method to get the URL of the download page.
        
        @return URL of the download page (QUrl)
        """
        return self.__pageUrl
