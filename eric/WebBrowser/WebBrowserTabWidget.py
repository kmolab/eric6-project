# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the central widget showing the web pages.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QUrl, QDir, QFile, \
    QFileDevice, QTemporaryFile
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMenu, QToolButton, \
    QDialog, QApplication
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QAbstractPrintDialog

from E5Gui.E5TabWidget import E5TabWidget
from E5Gui import E5MessageBox
from E5Gui.E5Application import e5App

from .WebBrowserView import WebBrowserView
from .WebBrowserPage import WebBrowserPage
from .Tools import WebBrowserTools
from .Tools import FilePrinter
from . import WebInspector

import UI.PixmapCache

import Utilities
import Preferences
import Globals
from Globals import qVersionTuple

from eric6config import getConfig


class WebBrowserTabWidget(E5TabWidget):
    """
    Class implementing the central widget showing the web pages.
    
    @signal sourceChanged(WebBrowserView, QUrl) emitted after the URL of a
        browser has changed
    @signal currentUrlChanged(QUrl) emitted after the URL of the current
        browser has changed
    @signal titleChanged(WebBrowserView, str) emitted after the title of a
        browser has changed
    @signal showMessage(str) emitted to show a message in the main window
        status bar
    @signal browserOpened(QWidget) emitted after a new browser was created
    @signal browserClosed(QWidget) emitted after a browser was closed
    @signal browserZoomValueChanged(int) emitted to signal a change of the
        current browser's zoom level
    """
    sourceChanged = pyqtSignal(WebBrowserView, QUrl)
    currentUrlChanged = pyqtSignal(QUrl)
    titleChanged = pyqtSignal(WebBrowserView, str)
    showMessage = pyqtSignal(str)
    browserOpened = pyqtSignal(QWidget)
    browserClosed = pyqtSignal(QWidget)
    browserZoomValueChanged = pyqtSignal(int)
    
    def __init__(self, parent):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(WebBrowserTabWidget, self).__init__(parent, dnd=True)
        
        from .WebBrowserTabBar import WebBrowserTabBar
        self.__tabBar = WebBrowserTabBar(self)
        self.setCustomTabBar(True, self.__tabBar)
        
        self.__mainWindow = parent
        
        self.setUsesScrollButtons(True)
        self.setDocumentMode(True)
        self.setElideMode(Qt.ElideNone)
        
        from .ClosedTabsManager import ClosedTabsManager
        self.__closedTabsManager = ClosedTabsManager(self)
        self.__closedTabsManager.closedTabAvailable.connect(
            self.__closedTabAvailable)
        
        from .UrlBar.StackedUrlBar import StackedUrlBar
        self.__stackedUrlBar = StackedUrlBar(self)
        self.__tabBar.tabMoved.connect(self.__stackedUrlBar.moveBar)
        
        self.__tabContextMenuIndex = -1
        self.currentChanged[int].connect(self.__currentChanged)
        self.setTabContextMenuPolicy(Qt.CustomContextMenu)
        self.customTabContextMenuRequested.connect(self.__showContextMenu)
        
        self.__rightCornerWidget = QWidget(self)
        self.__rightCornerWidgetLayout = QHBoxLayout(self.__rightCornerWidget)
        self.__rightCornerWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.__rightCornerWidgetLayout.setSpacing(0)
        
        self.__navigationMenu = QMenu(self)
        self.__navigationMenu.aboutToShow.connect(self.__showNavigationMenu)
        self.__navigationMenu.triggered.connect(self.__navigationMenuTriggered)
        
        self.__navigationButton = QToolButton(self)
        self.__navigationButton.setIcon(
            UI.PixmapCache.getIcon("1downarrow.png"))
        self.__navigationButton.setToolTip(
            self.tr("Show a navigation menu"))
        self.__navigationButton.setPopupMode(QToolButton.InstantPopup)
        self.__navigationButton.setMenu(self.__navigationMenu)
        self.__navigationButton.setEnabled(False)
        self.__rightCornerWidgetLayout.addWidget(self.__navigationButton)
        
        self.__closedTabsMenu = QMenu(self)
        self.__closedTabsMenu.aboutToShow.connect(
            self.__aboutToShowClosedTabsMenu)
        
        self.__closedTabsButton = QToolButton(self)
        self.__closedTabsButton.setIcon(UI.PixmapCache.getIcon("trash.png"))
        self.__closedTabsButton.setToolTip(
            self.tr("Show a navigation menu for closed tabs"))
        self.__closedTabsButton.setPopupMode(QToolButton.InstantPopup)
        self.__closedTabsButton.setMenu(self.__closedTabsMenu)
        self.__closedTabsButton.setEnabled(False)
        self.__rightCornerWidgetLayout.addWidget(self.__closedTabsButton)
        
        self.__closeButton = QToolButton(self)
        self.__closeButton.setIcon(UI.PixmapCache.getIcon("close.png"))
        self.__closeButton.setToolTip(
            self.tr("Close the current web browser"))
        self.__closeButton.setEnabled(False)
        self.__closeButton.clicked.connect(self.closeBrowser)
        self.__rightCornerWidgetLayout.addWidget(self.__closeButton)
        if Preferences.getUI("SingleCloseButton") or \
           not hasattr(self, 'setTabsClosable'):
            self.__closeButton.show()
        else:
            self.setTabsClosable(True)
            self.tabCloseRequested.connect(self.closeBrowserAt)
            self.__closeButton.hide()
        
        self.setCornerWidget(self.__rightCornerWidget, Qt.TopRightCorner)
        
        self.__newTabButton = QToolButton(self)
        self.__newTabButton.setIcon(UI.PixmapCache.getIcon("plus.png"))
        self.__newTabButton.setToolTip(
            self.tr("Open a new web browser tab"))
        self.setCornerWidget(self.__newTabButton, Qt.TopLeftCorner)
        self.__newTabButton.clicked.connect(self.__newBrowser)
        
        self.__initTabContextMenu()
        
        self.__historyCompleter = None
        
        self.__pdfPrinter = None
    
    def __initTabContextMenu(self):
        """
        Private method to create the tab context menu.
        """
        self.__tabContextMenu = QMenu(self)
        self.tabContextNewAct = self.__tabContextMenu.addAction(
            UI.PixmapCache.getIcon("tabNew.png"),
            self.tr('New Tab'), self.newBrowser)
        self.__tabContextMenu.addSeparator()
        self.leftMenuAct = self.__tabContextMenu.addAction(
            UI.PixmapCache.getIcon("1leftarrow.png"),
            self.tr('Move Left'), self.__tabContextMenuMoveLeft)
        self.rightMenuAct = self.__tabContextMenu.addAction(
            UI.PixmapCache.getIcon("1rightarrow.png"),
            self.tr('Move Right'), self.__tabContextMenuMoveRight)
        self.__tabContextMenu.addSeparator()
        self.tabContextCloneAct = self.__tabContextMenu.addAction(
            self.tr("Duplicate Page"), self.__tabContextMenuClone)
        self.__tabContextMenu.addSeparator()
        self.tabContextCloseAct = self.__tabContextMenu.addAction(
            UI.PixmapCache.getIcon("tabClose.png"),
            self.tr('Close'), self.__tabContextMenuClose)
        self.tabContextCloseOthersAct = self.__tabContextMenu.addAction(
            UI.PixmapCache.getIcon("tabCloseOther.png"),
            self.tr("Close Others"), self.__tabContextMenuCloseOthers)
        self.__tabContextMenu.addAction(
            self.tr('Close All'), self.closeAllBrowsers)
        self.__tabContextMenu.addSeparator()
        # TODO: re-check this once printing on Windows is reliable
##        if qVersionTuple() >= (5, 8, 0) or (
##            not Globals.isWindowsPlatform() and qVersionTuple() < (5, 7, 0)):
        if not Globals.isWindowsPlatform() and (
                qVersionTuple() < (5, 7, 0) or qVersionTuple() >= (5, 8, 0)):
            self.__tabContextMenu.addAction(
                UI.PixmapCache.getIcon("printPreview.png"),
                self.tr('Print Preview'), self.__tabContextMenuPrintPreview)
        # TODO: re-check this once printing on Windows is reliable
##        if qVersionTuple() >= (5, 8, 0) or (
##            not Globals.isWindowsPlatform() or qVersionTuple() >= (5, 7, 0)):
        if not Globals.isWindowsPlatform() and qVersionTuple() >= (5, 7, 0):
            self.__tabContextMenu.addAction(
                UI.PixmapCache.getIcon("print.png"),
                self.tr('Print'), self.__tabContextMenuPrint)
        if Globals.isLinuxPlatform() or qVersionTuple() >= (5, 7, 0):
            self.__tabContextMenu.addAction(
                UI.PixmapCache.getIcon("printPdf.png"),
                self.tr('Print as PDF'), self.__tabContextMenuPrintPdf)
        self.__tabContextMenu.addSeparator()
        if hasattr(WebBrowserPage, "isAudioMuted"):
            self.__audioAct = self.__tabContextMenu.addAction(
                "", self.__tabContextMenuAudioMute)
            self.__tabContextMenu.addSeparator()
        else:
            self.__audioAct = None
        self.__tabContextMenu.addAction(
            UI.PixmapCache.getIcon("reload.png"),
            self.tr('Reload All'), self.reloadAllBrowsers)
        self.__tabContextMenu.addSeparator()
        self.__tabContextMenu.addAction(
            UI.PixmapCache.getIcon("addBookmark.png"),
            self.tr('Bookmark All Tabs'), self.__mainWindow.bookmarkAll)
        
        self.__tabBackContextMenu = QMenu(self)
        self.__tabBackContextMenu.addAction(
            self.tr('Close All'), self.closeAllBrowsers)
        self.__tabBackContextMenu.addAction(
            UI.PixmapCache.getIcon("reload.png"),
            self.tr('Reload All'), self.reloadAllBrowsers)
        self.__tabBackContextMenu.addAction(
            UI.PixmapCache.getIcon("addBookmark.png"),
            self.tr('Bookmark All Tabs'), self.__mainWindow.bookmarkAll)
        self.__tabBackContextMenu.addSeparator()
        self.__restoreClosedTabAct = self.__tabBackContextMenu.addAction(
            UI.PixmapCache.getIcon("trash.png"),
            self.tr('Restore Closed Tab'), self.restoreClosedTab)
        self.__restoreClosedTabAct.setEnabled(False)
        self.__restoreClosedTabAct.setData(0)
    
    def __showContextMenu(self, coord, index):
        """
        Private slot to show the tab context menu.
        
        @param coord the position of the mouse pointer (QPoint)
        @param index index of the tab the menu is requested for (integer)
        """
        coord = self.mapToGlobal(coord)
        if index == -1:
            self.__tabBackContextMenu.popup(coord)
        else:
            self.__tabContextMenuIndex = index
            self.leftMenuAct.setEnabled(index > 0)
            self.rightMenuAct.setEnabled(index < self.count() - 1)
            
            self.tabContextCloseOthersAct.setEnabled(self.count() > 1)
            
            if self.__audioAct is not None:
                if self.widget(self.__tabContextMenuIndex).page()\
                        .isAudioMuted():
                    self.__audioAct.setText(self.tr("Unmute Tab"))
                    self.__audioAct.setIcon(
                        UI.PixmapCache.getIcon("audioVolumeHigh.png"))
                else:
                    self.__audioAct.setText(self.tr("Mute Tab"))
                    self.__audioAct.setIcon(
                        UI.PixmapCache.getIcon("audioVolumeMuted.png"))
            
            self.__tabContextMenu.popup(coord)
    
    def __tabContextMenuMoveLeft(self):
        """
        Private method to move a tab one position to the left.
        """
        self.moveTab(self.__tabContextMenuIndex,
                     self.__tabContextMenuIndex - 1)
    
    def __tabContextMenuMoveRight(self):
        """
        Private method to move a tab one position to the right.
        """
        self.moveTab(self.__tabContextMenuIndex,
                     self.__tabContextMenuIndex + 1)
    
    def __tabContextMenuClone(self):
        """
        Private method to clone the selected tab.
        """
        idx = self.__tabContextMenuIndex
        if idx < 0:
            idx = self.currentIndex()
        if idx < 0 or idx > self.count():
            return
        
        url = self.widget(idx).url()
        self.newBrowser(url)
    
    def __tabContextMenuClose(self):
        """
        Private method to close the selected tab.
        """
        self.closeBrowserAt(self.__tabContextMenuIndex)
    
    def __tabContextMenuCloseOthers(self):
        """
        Private slot to close all other tabs.
        """
        index = self.__tabContextMenuIndex
        for i in list(range(self.count() - 1, index, -1)) + \
                list(range(index - 1, -1, -1)):
            self.closeBrowserAt(i)
    
    def __tabContextMenuPrint(self):
        """
        Private method to print the selected tab.
        """
        browser = self.widget(self.__tabContextMenuIndex)
        self.printBrowser(browser)
    
    def __tabContextMenuPrintPdf(self):
        """
        Private method to print the selected tab as PDF.
        """
        browser = self.widget(self.__tabContextMenuIndex)
        self.printBrowserPdf(browser)
    
    def __tabContextMenuPrintPreview(self):
        """
        Private method to show a print preview of the selected tab.
        """
        browser = self.widget(self.__tabContextMenuIndex)
        self.printPreviewBrowser(browser)
    
    def __tabContextMenuAudioMute(self):
        """
        Private method to mute or unmute the selected tab.
        """
        page = self.widget(self.__tabContextMenuIndex).page()
        muted = page.isAudioMuted()
        page.setAudioMuted(not muted)
    
    @pyqtSlot(bool)
    def __recentlyAudibleChanged(self, recentlyAudible):
        """
        Private slot to react on the audible state of a page.
        
        @param recentlyAudible flag indicating the new audible state
        @type bool
        """
        page = self.sender()
        if page is None:
            return
        
        browser = page.view()
        if browser is None:
            return
        
        index = self.indexOf(browser)
        icon = page.icon()
        
        if page.isAudioMuted() or (
                not page.isAudioMuted() and recentlyAudible):
            pix = QPixmap(32, 32)
            pix.fill(Qt.transparent)
            painter = QPainter(pix)
            icon.paint(painter, 0, 0, 22, 22)
            if page.isAudioMuted():
                audioIcon = UI.PixmapCache.getIcon("audioMuted.png")
            else:
                audioIcon = UI.PixmapCache.getIcon("audioPlaying.png")
            audioIcon.paint(painter, 13, 13, 18, 18)
            painter.end()
            self.setTabIcon(index, QIcon(pix))
        else:
            self.setTabIcon(index, icon)
    
    @pyqtSlot()
    def __newBrowser(self):
        """
        Private slot to open a new browser tab.
        """
        self.newBrowser()
    
    def newBrowser(self, link=None, position=-1, background=False,
                   restoreSession=False):
        """
        Public method to create a new web browser tab.
        
        @param link link to be shown
        @type str or QUrl
        @keyparam position position to create the new tab at or -1 to add it
            to the end
        @type int
        @keyparam background flag indicating to open the tab in the
            background
        @type bool
        @keyparam restoreSession flag indicating a restore session action
        @type bool
        @return reference to the new browser
        @rtype WebBrowserView
        """
        if link is None:
            linkName = ""
        elif isinstance(link, QUrl):
            linkName = link.toString()
        else:
            linkName = link
        
        from .UrlBar.UrlBar import UrlBar
        urlbar = UrlBar(self.__mainWindow, self)
        if self.__historyCompleter is None:
            import WebBrowser.WebBrowserWindow
            from .History.HistoryCompleter import HistoryCompletionModel, \
                HistoryCompleter
            self.__historyCompletionModel = HistoryCompletionModel(self)
            self.__historyCompletionModel.setSourceModel(
                WebBrowser.WebBrowserWindow.WebBrowserWindow.historyManager()
                .historyFilterModel())
            self.__historyCompleter = HistoryCompleter(
                self.__historyCompletionModel, self)
            self.__historyCompleter.activated[str].connect(self.__pathSelected)
        urlbar.setCompleter(self.__historyCompleter)
        urlbar.returnPressed.connect(self.__lineEditReturnPressed)
        if position == -1:
            self.__stackedUrlBar.addWidget(urlbar)
        else:
            self.__stackedUrlBar.insertWidget(position, urlbar)
        
        browser = WebBrowserView(self.__mainWindow, self)
        urlbar.setBrowser(browser)
        
        browser.sourceChanged.connect(self.__sourceChanged)
        browser.titleChanged.connect(self.__titleChanged)
        browser.highlighted.connect(self.showMessage)
        browser.backwardAvailable.connect(
            self.__mainWindow.setBackwardAvailable)
        browser.forwardAvailable.connect(self.__mainWindow.setForwardAvailable)
        browser.loadStarted.connect(self.__loadStarted)
        browser.loadFinished.connect(self.__loadFinished)
        browser.faviconChanged.connect(self.__iconChanged)
        browser.search.connect(self.newBrowser)
        browser.page().windowCloseRequested.connect(
            self.__windowCloseRequested)
        browser.zoomValueChanged.connect(self.browserZoomValueChanged)
        if hasattr(WebBrowserPage, "recentlyAudibleChanged"):
            browser.page().recentlyAudibleChanged.connect(
                self.__recentlyAudibleChanged)
        
        if position == -1:
            index = self.addTab(browser, self.tr("..."))
        else:
            index = self.insertTab(position, browser, self.tr("..."))
        if not background:
            self.setCurrentIndex(index)
        
        self.__mainWindow.closeAct.setEnabled(True)
        self.__mainWindow.closeAllAct.setEnabled(True)
        self.__closeButton.setEnabled(True)
        self.__navigationButton.setEnabled(True)
        
        if not restoreSession:
            if not linkName:
                if Preferences.getWebBrowser("NewTabBehavior") == 0:
                    linkName = "about:blank"
                elif Preferences.getWebBrowser("NewTabBehavior") == 1:
                    linkName = Preferences.getWebBrowser("HomePage")
                elif Preferences.getWebBrowser("NewTabBehavior") == 2:
                    linkName = "eric:speeddial"
        
        if linkName == "eric:blank":
            linkName = "about:blank"
        
        if linkName:
            browser.setSource(QUrl(linkName))
            if not browser.documentTitle():
                self.setTabText(index, self.__elide(linkName, Qt.ElideMiddle))
                self.setTabToolTip(index, linkName)
            else:
                self.setTabText(
                    index,
                    self.__elide(browser.documentTitle().replace("&", "&&")))
                self.setTabToolTip(index, browser.documentTitle())
        
        self.browserOpened.emit(browser)
        
        return browser
    
    def newBrowserAfter(self, browser, link=None, background=False):
        """
        Public method to create a new web browser tab after a given one.
        
        @param browser reference to the browser to add after (WebBrowserView)
        @param link link to be shown (string or QUrl)
        @keyparam background flag indicating to open the tab in the
            background (bool)
        @return reference to the new browser
        @rtype WebBrowserView
        """
        if browser:
            position = self.indexOf(browser) + 1
        else:
            position = -1
        return self.newBrowser(link, position, background)
    
    def __showNavigationMenu(self):
        """
        Private slot to show the navigation button menu.
        """
        self.__navigationMenu.clear()
        for index in range(self.count()):
            act = self.__navigationMenu.addAction(
                self.tabIcon(index), self.tabText(index))
            act.setData(index)
    
    def __navigationMenuTriggered(self, act):
        """
        Private slot called to handle the navigation button menu selection.
        
        @param act reference to the selected action (QAction)
        """
        index = act.data()
        if index is not None:
            self.setCurrentIndex(index)
    
    def __windowCloseRequested(self):
        """
        Private slot to handle the windowCloseRequested signal of a browser.
        """
        page = self.sender()
        if page is None:
            return
        
        browser = page.view()
        if browser is None:
            return
        
        index = self.indexOf(browser)
        self.closeBrowserAt(index)
    
    def reloadAllBrowsers(self):
        """
        Public slot to reload all browsers.
        """
        for index in range(self.count()):
            browser = self.widget(index)
            browser and browser.reload()
    
    @pyqtSlot()
    def closeBrowser(self):
        """
        Public slot called to handle the close action.
        """
        self.closeBrowserAt(self.currentIndex())
    
    def closeAllBrowsers(self, shutdown=False):
        """
        Public slot called to handle the close all action.
        
        @param shutdown flag indicating a shutdown action
        @type bool
        """
        for index in range(self.count() - 1, -1, -1):
            self.closeBrowserAt(index, shutdown=shutdown)
    
    def closeBrowserAt(self, index, shutdown=False):
        """
        Public slot to close a browser based on its index.
        
        @param index index of browser to close
        @type int
        @param shutdown flag indicating a shutdown action
        @type bool
        """
        browser = self.widget(index)
        if browser is None:
            return
        
        urlbar = self.__stackedUrlBar.widget(index)
        self.__stackedUrlBar.removeWidget(urlbar)
        urlbar.deleteLater()
        del urlbar
        
        self.__closedTabsManager.recordBrowser(browser, index)
        
        browser.closeWebInspector()
        WebInspector.unregisterView(browser)
        self.removeTab(index)
        self.browserClosed.emit(browser)
        browser.deleteLater()
        del browser
        
        if self.count() == 0 and not shutdown:
            self.newBrowser()
        else:
            self.currentChanged[int].emit(self.currentIndex())
    
    def currentBrowser(self):
        """
        Public method to get a reference to the current browser.
        
        @return reference to the current browser (WebBrowserView)
        """
        return self.currentWidget()
    
    def browserAt(self, index):
        """
        Public method to get a reference to the browser with the given index.
        
        @param index index of the browser to get (integer)
        @return reference to the indexed browser (WebBrowserView)
        """
        return self.widget(index)
    
    def browsers(self):
        """
        Public method to get a list of references to all browsers.
        
        @return list of references to browsers (list of WebBrowserView)
        """
        li = []
        for index in range(self.count()):
            li.append(self.widget(index))
        return li
    
    @pyqtSlot()
    def printBrowser(self, browser=None):
        """
        Public slot called to print the displayed page.
        
        @param browser reference to the browser to be printed (WebBrowserView)
        """
        if browser is None:
            browser = self.currentBrowser()
        
        printer = QPrinter(mode=QPrinter.HighResolution)
        if Preferences.getPrinter("ColorMode"):
            printer.setColorMode(QPrinter.Color)
        else:
            printer.setColorMode(QPrinter.GrayScale)
        if Preferences.getPrinter("FirstPageFirst"):
            printer.setPageOrder(QPrinter.FirstPageFirst)
        else:
            printer.setPageOrder(QPrinter.LastPageFirst)
        printer.setPageMargins(
            Preferences.getPrinter("LeftMargin") * 10,
            Preferences.getPrinter("TopMargin") * 10,
            Preferences.getPrinter("RightMargin") * 10,
            Preferences.getPrinter("BottomMargin") * 10,
            QPrinter.Millimeter
        )
        printerName = Preferences.getPrinter("PrinterName")
        if printerName:
            printer.setPrinterName(printerName)
        printer.setResolution(Preferences.getPrinter("Resolution"))
        documentName = WebBrowserTools.getFileNameFromUrl(browser.url())
        printer.setDocName(documentName)
        
        printDialog = QPrintDialog(printer, self)
        printDialog.setOptions(QAbstractPrintDialog.PrintToFile |
                               QAbstractPrintDialog.PrintShowPageSize)
        if not Globals.isWindowsPlatform():
            if FilePrinter.isCupsAvailable():
                printDialog.setOption(QAbstractPrintDialog.PrintCollateCopies)
            printDialog.setOption(QAbstractPrintDialog.PrintPageRange)
        if printDialog.exec_() == QDialog.Accepted:
            if hasattr(browser.page(), "print"):
                # Qt >= 5.8.0
                browser.page().execPrintPage(printer, 10 * 1000)
            elif hasattr(browser.page(), "printToPdf"):
                # Qt >= 5.7.0
                if printer.outputFormat() == QPrinter.PdfFormat:
                    # print to PDF file selected
                    browser.page().printToPdf(
                        lambda pdf: self.__pdfGeneratedForSave(
                            printer.outputFileName(), pdf),
                        printer.pageLayout())
                else:
                    # print to printer
                    self.__pdfPrinter = printer
                    browser.page().printToPdf(
                        self.__pdfGeneratedForPrinting,
                        printer.pageLayout())
            else:
                browser.render(printer)
    
    @pyqtSlot()
    def printBrowserPdf(self, browser=None):
        """
        Public slot called to print the displayed page to PDF.
        
        @param browser reference to the browser to be printed (HelpBrowser)
        """
        if browser is None:
            browser = self.currentBrowser()
        
        name = WebBrowserTools.getFileNameFromUrl(browser.url())
        if name:
            name = name.rsplit('.', 1)[0]
            name += '.pdf'
        if hasattr(browser.page(), "printToPdf"):
            from .Tools.PrintToPdfDialog import PrintToPdfDialog
            if not name:
                name = "printout.pdf"
            dlg = PrintToPdfDialog(name, self)
            if dlg.exec_() == QDialog.Accepted:
                filePath, pageLayout = dlg.getData()
                if filePath:
                    if os.path.exists(filePath):
                        res = E5MessageBox.warning(
                            self,
                            self.tr("Print to PDF"),
                            self.tr("""<p>The file <b>{0}</b> exists"""
                                    """ already. Shall it be"""
                                    """ overwritten?</p>""").format(filePath),
                            E5MessageBox.StandardButtons(
                                E5MessageBox.No |
                                E5MessageBox.Yes),
                            E5MessageBox.No)
                        if res == E5MessageBox.No:
                            return
                    browser.page().printToPdf(
                        lambda pdf: self.__pdfGeneratedForSave(filePath, pdf),
                        pageLayout)
        elif Globals.isLinuxPlatform():
            printer = QPrinter(mode=QPrinter.HighResolution)
            if Preferences.getPrinter("ColorMode"):
                printer.setColorMode(QPrinter.Color)
            else:
                printer.setColorMode(QPrinter.GrayScale)
            printerName = Preferences.getPrinter("PrinterName")
            if printerName:
                printer.setPrinterName(printerName)
            printer.setOutputFormat(QPrinter.PdfFormat)
            if name:
                printer.setOutputFileName(name)
            printer.setResolution(Preferences.getPrinter("Resolution"))
            
            printDialog = QPrintDialog(printer, self)
            if printDialog.exec_() == QDialog.Accepted:
                browser.render(printer)
    
    def __pdfGeneratedForSave(self, filePath, pdfData):
        """
        Private slot to save the generated PDF data to a file.
        
        @param filePath path to save the PDF to
        @type str
        @param pdfData generated PDF document
        @type QByteArray
        """
        if pdfData.size() == 0:
            return
        
        pdfFile = QFile(filePath)
        if pdfFile.open(QFile.WriteOnly):
            pdfFile.write(pdfData)
            pdfFile.close()
        if pdfFile.error() != QFileDevice.NoError:
            E5MessageBox.critical(
                self,
                self.tr("Print to PDF"),
                self.tr("""<p>The PDF could not be written to file <b>{0}"""
                        """</b>.</p><p><b>Error:</b> {1}</p>""").format(
                    filePath, pdfFile.errorString()),
                E5MessageBox.StandardButtons(
                    E5MessageBox.Ok))
    
    def __pdfGeneratedForPrinting(self, pdfData):
        """
        Private slot to print the generated PDF data.
        
        @param pdfData generated PDF document
        @type QByteArray
        """
        if self.__pdfPrinter is None or pdfData.isEmpty():
            return
        
        tempFile = QTemporaryFile(QDir.tempPath() + "/ericBrowserXXXXXX.pdf")
        tempFile.setAutoRemove(False)
        if tempFile.open():
            bytesWritten = tempFile.write(pdfData)
            tempFile.close()
            if bytesWritten == pdfData.size():
                if Globals.isWindowsPlatform():
                    printerName = self.__pdfPrinter.printerName()
                    import ctypes
                    ctypes.windll.shell32.ShellExecuteW(
                        None, "printto", tempFile.fileName(),
                        '"{0}"'.format(printerName), None, 0)
                else:
                    FilePrinter.printFile(
                        self.__pdfPrinter, tempFile.fileName(),
                        FilePrinter.FilePrinter.SystemDeletesFiles,
                        FilePrinter.FilePrinter.SystemSelectsPages)
            else:
                tempFile.remove()
        
        self.__pdfPrinter = None
    
    @pyqtSlot()
    def printPreviewBrowser(self, browser=None):
        """
        Public slot called to show a print preview of the displayed file.
        
        @param browser reference to the browser to be printed (WebBrowserView)
        """
        from PyQt5.QtPrintSupport import QPrintPreviewDialog
        
        if browser is None:
            browser = self.currentBrowser()
        
        printer = QPrinter(mode=QPrinter.HighResolution)
        if Preferences.getPrinter("ColorMode"):
            printer.setColorMode(QPrinter.Color)
        else:
            printer.setColorMode(QPrinter.GrayScale)
        if Preferences.getPrinter("FirstPageFirst"):
            printer.setPageOrder(QPrinter.FirstPageFirst)
        else:
            printer.setPageOrder(QPrinter.LastPageFirst)
        printer.setPageMargins(
            Preferences.getPrinter("LeftMargin") * 10,
            Preferences.getPrinter("TopMargin") * 10,
            Preferences.getPrinter("RightMargin") * 10,
            Preferences.getPrinter("BottomMargin") * 10,
            QPrinter.Millimeter
        )
        printerName = Preferences.getPrinter("PrinterName")
        if printerName:
            printer.setPrinterName(printerName)
        printer.setResolution(Preferences.getPrinter("Resolution"))
        
        preview = QPrintPreviewDialog(printer, self)
        preview.resize(800, 750)
        if qVersionTuple() >= (5, 8, 0):
            preview.paintRequested.connect(
                lambda p: self.__printPreviewRequested(p, browser))
        else:
            preview.paintRequested.connect(lambda p: browser.render(p))
        preview.exec_()
    
    def __printPreviewRequested(self, printer, browser):
        """
        Private slot to generate the print preview.
        
        @param printer reference to the printer object
        @type QPrinter
        @param browser reference to the browser to be printed
        @type WebBrowserView
        """
        QApplication.setOverrideCursor(Qt.WaitCursor)
        browser.page().execPrintPage(printer, 10 * 1000)
        QApplication.restoreOverrideCursor()
    
    def __sourceChanged(self, url):
        """
        Private slot to handle a change of a browsers source.
        
        @param url URL of the new site (QUrl)
        """
        browser = self.sender()
        
        if browser is not None:
            self.sourceChanged.emit(browser, url)
            
            if browser == self.currentBrowser():
                self.currentUrlChanged.emit(url)
    
    def __titleChanged(self, title):
        """
        Private slot to handle a change of a browsers title.
        
        @param title new title (string)
        """
        browser = self.sender()
        
        if browser is not None and isinstance(browser, QWidget):
            index = self.indexOf(browser)
            if title == "":
                title = browser.url().toString()
            
            self.setTabText(index, self.__elide(title.replace("&", "&&")))
            self.setTabToolTip(index, title)
        
            self.titleChanged.emit(browser, title)
    
    def __elide(self, txt, mode=Qt.ElideRight, length=40):
        """
        Private method to elide some text.
        
        @param txt text to be elided (string)
        @keyparam mode elide mode (Qt.TextElideMode)
        @keyparam length amount of characters to be used (integer)
        @return the elided text (string)
        """
        if mode == Qt.ElideNone or len(txt) < length:
            return txt
        elif mode == Qt.ElideLeft:
            return "...{0}".format(txt[-length:])
        elif mode == Qt.ElideMiddle:
            return "{0}...{1}".format(txt[:length // 2], txt[-(length // 2):])
        elif mode == Qt.ElideRight:
            return "{0}...".format(txt[:length])
        else:
            # just in case
            return txt
    
    def preferencesChanged(self):
        """
        Public slot to handle a change of preferences.
        """
        for browser in self.browsers():
            browser.preferencesChanged()
        
        for urlbar in self.__stackedUrlBar.urlBars():
            urlbar.preferencesChanged()
        
        if Preferences.getUI("SingleCloseButton"):
            self.setTabsClosable(False)
            try:
                self.tabCloseRequested.disconnect(self.closeBrowserAt)
            except TypeError:
                pass
            self.__closeButton.show()
        else:
            self.setTabsClosable(True)
            self.tabCloseRequested.connect(self.closeBrowserAt)
            self.__closeButton.hide()
    
    def __loadStarted(self):
        """
        Private method to handle the loadStarted signal.
        """
        browser = self.sender()
        
        if browser is not None:
            index = self.indexOf(browser)
            anim = self.animationLabel(
                index, os.path.join(getConfig("ericPixDir"), "loading.gif"),
                100)
            if not anim:
                loading = QIcon(os.path.join(getConfig("ericPixDir"),
                                "loading.gif"))
                self.setTabIcon(index, loading)
            else:
                self.setTabIcon(index, QIcon())
            self.setTabText(index, self.tr("Loading..."))
            self.setTabToolTip(index, self.tr("Loading..."))
            self.showMessage.emit(self.tr("Loading..."))
            
            self.__mainWindow.setLoadingActions(True)
    
    def __loadFinished(self, ok):
        """
        Private method to handle the loadFinished signal.
        
        @param ok flag indicating the result (boolean)
        """
        browser = self.sender()
        if not isinstance(browser, WebBrowserView):
            return
        
        if browser is not None:
            import WebBrowser.WebBrowserWindow
            index = self.indexOf(browser)
            self.resetAnimation(index)
            self.setTabIcon(
                index, WebBrowser.WebBrowserWindow.WebBrowserWindow.icon(
                    browser.url()))
            if ok:
                self.showMessage.emit(self.tr("Finished loading"))
            else:
                self.showMessage.emit(self.tr("Failed to load"))
            
            self.__mainWindow.setLoadingActions(False)
    
    def __iconChanged(self):
        """
        Private slot to handle a change of the web site icon.
        """
        browser = self.sender()
        
        if browser is not None and isinstance(browser, QWidget):
            self.setTabIcon(
                self.indexOf(browser),
                browser.icon())
            self.__mainWindow.bookmarksManager().faviconChanged(browser.url())
    
    def getSourceFileList(self):
        """
        Public method to get a list of all opened Qt help files.
        
        @return dictionary with tab id as key and host/namespace as value
        """
        sourceList = {}
        for i in range(self.count()):
            browser = self.widget(i)
            if browser is not None and \
               browser.source().isValid():
                sourceList[i] = browser.source().host()
        
        return sourceList
    
    def shallShutDown(self):
        """
        Public method to check, if the application should be shut down.
        
        @return flag indicating a shut down (boolean)
        """
        if self.count() > 1 and Preferences.getWebBrowser(
                "WarnOnMultipleClose"):
            mb = E5MessageBox.E5MessageBox(
                E5MessageBox.Information,
                self.tr("Are you sure you want to close the window?"),
                self.tr("""Are you sure you want to close the window?\n"""
                        """You have %n tab(s) open.""", "", self.count()),
                modal=True,
                parent=self)
            if self.__mainWindow.fromEric:
                quitButton = mb.addButton(
                    self.tr("&Close"), E5MessageBox.AcceptRole)
                quitButton.setIcon(UI.PixmapCache.getIcon("close.png"))
            else:
                quitButton = mb.addButton(
                    self.tr("&Quit"), E5MessageBox.AcceptRole)
                quitButton.setIcon(UI.PixmapCache.getIcon("exit.png"))
            closeTabButton = mb.addButton(
                self.tr("C&lose Current Tab"), E5MessageBox.AcceptRole)
            closeTabButton.setIcon(UI.PixmapCache.getIcon("tabClose.png"))
            mb.addButton(E5MessageBox.Cancel)
            mb.exec_()
            if mb.clickedButton() == quitButton:
                return True
            else:
                if mb.clickedButton() == closeTabButton:
                    self.closeBrowser()
                return False
        
        return True
    
    def stackedUrlBar(self):
        """
        Public method to get a reference to the stacked url bar.
        
        @return reference to the stacked url bar (StackedUrlBar)
        """
        return self.__stackedUrlBar
    
    def currentUrlBar(self):
        """
        Public method to get a reference to the current url bar.
        
        @return reference to the current url bar (UrlBar)
        """
        return self.__stackedUrlBar.currentWidget()
    
    def __lineEditReturnPressed(self):
        """
        Private slot to handle the entering of an URL.
        """
        edit = self.sender()
        url = self.__guessUrlFromPath(edit.text())
        if e5App().keyboardModifiers() == Qt.AltModifier:
            self.newBrowser(url)
        else:
            self.currentBrowser().setSource(url)
            self.currentBrowser().setFocus()
    
    def __pathSelected(self, path):
        """
        Private slot called when a URL is selected from the completer.
        
        @param path path to be shown (string)
        """
        url = self.__guessUrlFromPath(path)
        self.currentBrowser().setSource(url)
    
    def __guessUrlFromPath(self, path):
        """
        Private method to guess an URL given a path string.
        
        @param path path string to guess an URL for (string)
        @return guessed URL (QUrl)
        """
        manager = self.__mainWindow.openSearchManager()
        path = Utilities.fromNativeSeparators(path)
        url = manager.convertKeywordSearchToUrl(path)
        if url.isValid():
            return url
        
        try:
            url = QUrl.fromUserInput(path)
        except AttributeError:
            url = QUrl(path)
        
        if url.scheme() == "about" and \
           url.path() == "home":
            url = QUrl("eric:home")
        
        if url.scheme() in ["s", "search"]:
            url = manager.currentEngine().searchUrl(url.path().strip())
        
        if url.scheme() != "" and \
           (url.host() != "" or url.path() != ""):
            return url
        
        urlString = Preferences.getWebBrowser("DefaultScheme") + path.strip()
        url = QUrl.fromEncoded(urlString.encode("utf-8"), QUrl.TolerantMode)
        
        return url
    
    def __currentChanged(self, index):
        """
        Private slot to handle an index change.
        
        @param index new index (integer)
        """
        self.__stackedUrlBar.setCurrentIndex(index)
        
        browser = self.browserAt(index)
        if browser is not None:
            if browser.url() == "" and browser.hasFocus():
                self.__stackedUrlBar.currentWidget.setFocus()
            elif browser.url() != "":
                browser.setFocus()
    
    def restoreClosedTab(self):
        """
        Public slot to restore the most recently closed tab.
        """
        if not self.canRestoreClosedTab():
            return
        
        act = self.sender()
        tab = self.__closedTabsManager.getClosedTabAt(act.data())
        
        self.newBrowser(tab.url.toString(), position=tab.position)
    
    def canRestoreClosedTab(self):
        """
        Public method to check, if closed tabs can be restored.
        
        @return flag indicating that closed tabs can be restored (boolean)
        """
        return self.__closedTabsManager.isClosedTabAvailable()
    
    def restoreAllClosedTabs(self):
        """
        Public slot to restore all closed tabs.
        """
        if not self.canRestoreClosedTab():
            return
        
        for tab in self.__closedTabsManager.allClosedTabs():
            self.newBrowser(tab.url.toString(), position=tab.position)
        self.__closedTabsManager.clearList()
    
    def clearClosedTabsList(self):
        """
        Public slot to clear the list of closed tabs.
        """
        self.__closedTabsManager.clearList()
    
    def __aboutToShowClosedTabsMenu(self):
        """
        Private slot to populate the closed tabs menu.
        """
        fm = self.__closedTabsMenu.fontMetrics()
        maxWidth = fm.width('m') * 40
        
        self.__closedTabsMenu.clear()
        index = 0
        for tab in self.__closedTabsManager.allClosedTabs():
            title = fm.elidedText(tab.title, Qt.ElideRight, maxWidth)
            self.__closedTabsMenu.addAction(
                self.__mainWindow.icon(tab.url), title,
                self.restoreClosedTab).setData(index)
            index += 1
        self.__closedTabsMenu.addSeparator()
        self.__closedTabsMenu.addAction(
            self.tr("Restore All Closed Tabs"), self.restoreAllClosedTabs)
        self.__closedTabsMenu.addAction(
            self.tr("Clear List"), self.clearClosedTabsList)
    
    def closedTabsManager(self):
        """
        Public slot to get a reference to the closed tabs manager.
        
        @return reference to the closed tabs manager (ClosedTabsManager)
        """
        return self.__closedTabsManager
    
    def __closedTabAvailable(self, avail):
        """
        Private slot to handle changes of the availability of closed tabs.
        
        @param avail flag indicating the availability of closed tabs (boolean)
        """
        self.__closedTabsButton.setEnabled(avail)
        self.__restoreClosedTabAct.setEnabled(avail)
    
    ####################################################
    ## Methods below implement session related functions
    ####################################################
    
    def getSessionData(self):
        """
        Public method to populate the session data.
        
        @return dictionary containing the session data
        @rtype dict
        """
        sessionData = {}
        
        # 1. current index
        sessionData["CurrentTabIndex"] = self.currentIndex()
        
        # 2. tab data
        sessionData["Tabs"] = []
        for index in range(self.count()):
            browser = self.widget(index)
            data = browser.getSessionData()
            sessionData["Tabs"].append(data)
        
        return sessionData
    
    def loadFromSessionData(self, sessionData):
        """
        Public method to load the session data.
        
        @param sessionData dictionary containing the session data as
            generated by getSessionData()
        @type dict
        """
        tabCount = self.count()
        
        # 1. load tab data
        if "Tabs" in sessionData:
            loadTabOnActivate = \
                Preferences.getWebBrowser("LoadTabOnActivation")
            for data in sessionData["Tabs"]:
                browser = self.newBrowser(restoreSession=True)
                if loadTabOnActivate:
                    browser.storeSessionData(data)
                    title, urlStr, icon = browser.extractSessionMetaData(data)
                    index = self.indexOf(browser)
                    self.setTabText(index, title)
                    self.setTabIcon(index, icon)
                else:
                    browser.loadFromSessionData(data)
        
        # 2. set tab index
        if "CurrentTabIndex" in sessionData and \
                sessionData["CurrentTabIndex"] >= 0:
            index = tabCount + sessionData["CurrentTabIndex"]
            self.setCurrentIndex(index)
            self.browserAt(index).activateSession()
