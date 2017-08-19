# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the JavaScript status bar icon.
"""

#
# This is modeled after the code found in Qupzilla
# Copyright (C) 2014  David Rosca <nowrep@gmail.com>
#

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, Qt, QPoint
from PyQt5.QtWidgets import QGraphicsColorizeEffect, QMenu, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

from .StatusBarIcon import StatusBarIcon

import UI.PixmapCache


class JavaScriptIcon(StatusBarIcon):
    """
    Class implementing the JavaScript status bar icon.
    """
    def __init__(self, window):
        """
        Constructor
        
        @param window reference to the web browser window
        @type WebBrowserWindow
        """
        super(JavaScriptIcon, self).__init__(window)
        
        self.setToolTip(self.tr("Modify JavaScript settings temporarily for"
                                " a site or globally"))
        self.__icon = UI.PixmapCache.getPixmap("fileJavascript").scaled(16, 16)
        self.setPixmap(self.__icon)
        
        self._window.tabWidget().currentChanged.connect(self.__updateIcon)
        self._window.tabWidget().currentUrlChanged.connect(self.__updateIcon)
        self.clicked.connect(self.__showMenu)
        
        self.__updateIcon()
    
    def preferencesChanged(self):
        """
        Public method to handle changes of the settings.
        """
        self.__updateIcon()
    
    @pyqtSlot(QPoint)
    def __showMenu(self, pos):
        """
        Private slot to show the menu.
        
        @param pos position to show the menu at
        @type QPoint
        """
        boldFont = self.font()
        boldFont.setBold(True)
        
        menu = QMenu()
        menu.addAction(self.tr("Current Page Settings")).setFont(boldFont)
        
        if self._testCurrentPageWebAttribute(
                QWebEngineSettings.JavascriptEnabled):
            act = menu.addAction(self.tr("Disable JavaScript (temporarily)"),
                                 self.__toggleJavaScript)
        else:
            act = menu.addAction(self.tr("Enable JavaScript (temporarily)"),
                                 self.__toggleJavaScript)
        if self._currentPage() is not None and \
                self._currentPage().url().scheme() == "eric":
            # JavaScript is needed for eric: scheme
            act.setEnabled(False)
        
        menu.addSeparator()
        menu.addAction(self.tr("Global Settings")).setFont(boldFont)
        menu.addAction(self.tr("Manage JavaScript Settings"),
                       self.__showJavaScriptSettingsDialog)
        menu.exec_(pos)
    
    @pyqtSlot()
    def __updateIcon(self):
        """
        Private slot to update the icon.
        """
        if self._testCurrentPageWebAttribute(
                QWebEngineSettings.JavascriptEnabled):
            self.setGraphicsEffect(None)
        else:
            effect = QGraphicsColorizeEffect(self)
            effect.setColor(Qt.gray)
            self.setGraphicsEffect(effect)
    
    @pyqtSlot()
    def __toggleJavaScript(self):
        """
        Private slot to toggle the JavaScript setting.
        """
        if self._currentPage() is None:
            return
        
        current = self._testCurrentPageWebAttribute(
            QWebEngineSettings.JavascriptEnabled)
        self._currentPage().setJavaScriptEnabled(not current)
        
        self._window.currentBrowser().reload()
        
        self.__updateIcon()
    
    @pyqtSlot()
    def __showJavaScriptSettingsDialog(self):
        """
        Private slot to show the JavaScript settings dialog.
        
        Note: This is the JavaScript subset of the web browser configuration
        page.
        """
        from .JavaScriptSettingsDialog import JavaScriptSettingsDialog
        dlg = JavaScriptSettingsDialog(self._window)
        if dlg.exec_() == QDialog.Accepted:
            self._window.preferencesChanged()
