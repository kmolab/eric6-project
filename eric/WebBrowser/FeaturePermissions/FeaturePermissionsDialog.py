# -*- coding: utf-8 -*-

# Copyright (c) 2015 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the feature permission dialog.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem, QTreeWidget, \
    QAbstractItemView
from PyQt5.QtWebEngineWidgets import QWebEnginePage

import UI.PixmapCache

from .Ui_FeaturePermissionsDialog import Ui_FeaturePermissionsDialog


class FeaturePermissionsDialog(QDialog, Ui_FeaturePermissionsDialog):
    """
    Class implementing the feature permission dialog.
    """
    def __init__(self, featurePermissions, parent=None):
        """
        Constructor
        
        @param featurePermissions dictionary with remembered feature
            permissions
        @type dict of dict of list
        @param parent reference to the parent widget
        @type QWidget
        """
        super(FeaturePermissionsDialog, self).__init__(parent)
        self.setupUi(self)
        
        # add the various lists
        
        self.geoList = QTreeWidget()
        self.geoList.setAlternatingRowColors(True)
        self.geoList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.geoList.setRootIsDecorated(False)
        self.geoList.setItemsExpandable(False)
        self.geoList.setAllColumnsShowFocus(True)
        self.geoList.setObjectName("geoList")
        self.geoList.setSortingEnabled(True)
        self.geoList.headerItem().setText(0, self.tr("Host"))
        self.geoList.headerItem().setText(1, self.tr("Permission"))
        self.tabWidget.addTab(
            self.geoList,
            UI.PixmapCache.getIcon("geolocation.png"),
            self.tr("Geolocation"))
        
        self.micList = QTreeWidget()
        self.micList.setAlternatingRowColors(True)
        self.micList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.micList.setRootIsDecorated(False)
        self.micList.setItemsExpandable(False)
        self.micList.setAllColumnsShowFocus(True)
        self.micList.setObjectName("micList")
        self.micList.setSortingEnabled(True)
        self.micList.headerItem().setText(0, self.tr("Host"))
        self.micList.headerItem().setText(1, self.tr("Permission"))
        self.tabWidget.addTab(
            self.micList,
            UI.PixmapCache.getIcon("audiocapture.png"),
            self.tr("Microphone"))
        
        self.camList = QTreeWidget()
        self.camList.setAlternatingRowColors(True)
        self.camList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.camList.setRootIsDecorated(False)
        self.camList.setItemsExpandable(False)
        self.camList.setAllColumnsShowFocus(True)
        self.camList.setObjectName("camList")
        self.camList.setSortingEnabled(True)
        self.camList.headerItem().setText(0, self.tr("Host"))
        self.camList.headerItem().setText(1, self.tr("Permission"))
        self.tabWidget.addTab(
            self.camList,
            UI.PixmapCache.getIcon("camera.png"),
            self.tr("Camera"))
        
        self.micCamList = QTreeWidget()
        self.micCamList.setAlternatingRowColors(True)
        self.micCamList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.micCamList.setRootIsDecorated(False)
        self.micCamList.setItemsExpandable(False)
        self.micCamList.setAllColumnsShowFocus(True)
        self.micCamList.setObjectName("micCamList")
        self.micCamList.setSortingEnabled(True)
        self.micCamList.headerItem().setText(0, self.tr("Host"))
        self.micCamList.headerItem().setText(1, self.tr("Permission"))
        self.tabWidget.addTab(
            self.micCamList,
            UI.PixmapCache.getIcon("audio-video.png"),
            self.tr("Microphone && Camera"))
        
        self.mouseLockList = QTreeWidget()
        self.mouseLockList.setAlternatingRowColors(True)
        self.mouseLockList.setSelectionMode(
            QAbstractItemView.ExtendedSelection)
        self.mouseLockList.setRootIsDecorated(False)
        self.mouseLockList.setItemsExpandable(False)
        self.mouseLockList.setAllColumnsShowFocus(True)
        self.mouseLockList.setObjectName("mouseLockList")
        self.mouseLockList.setSortingEnabled(True)
        self.mouseLockList.headerItem().setText(0, self.tr("Host"))
        self.mouseLockList.headerItem().setText(1, self.tr("Permission"))
        self.tabWidget.addTab(
            self.mouseLockList,
            UI.PixmapCache.getIcon("mouse.png"),
            self.tr("Mouse Lock"))
        
        self.setTabOrder(self.tabWidget, self.geoList)
        self.setTabOrder(self.geoList, self.micList)
        self.setTabOrder(self.micList, self.camList)
        self.setTabOrder(self.camList, self.micCamList)
        self.setTabOrder(self.micCamList, self.mouseLockList)
        self.setTabOrder(self.mouseLockList, self.removeButton)
        self.setTabOrder(self.removeButton, self.removeAllButton)
        
        self.__permissionStrings = {
            QWebEnginePage.PermissionGrantedByUser: self.tr("Allow"),
            QWebEnginePage.PermissionDeniedByUser: self.tr("Deny"),
        }
        
        self.__permissionsLists = {
            QWebEnginePage.Geolocation: self.geoList,
            QWebEnginePage.MediaAudioCapture: self.micList,
            QWebEnginePage.MediaVideoCapture: self.camList,
            QWebEnginePage.MediaAudioVideoCapture: self.micCamList,
            QWebEnginePage.MouseLock: self.mouseLockList,
        }
        
        for feature, permissionsList in self.__permissionsLists.items():
            for permission in featurePermissions[feature]:
                for host in featurePermissions[feature][permission]:
                    itm = QTreeWidgetItem(
                        permissionsList,
                        [host, self.__permissionStrings[permission]])
                    itm.setData(0, Qt.UserRole, permission)
        
        self.__previousCurrent = -1
        self.tabWidget.currentChanged.connect(self.__currentTabChanged)
        self.tabWidget.setCurrentIndex(0)
    
    @pyqtSlot(int)
    def __currentTabChanged(self, index):
        """
        Private slot handling changes of the selected tab.
        
        @param index index of the current tab
        @type int
        """
        if self.__previousCurrent >= 0:
            previousList = self.tabWidget.widget(self.__previousCurrent)
            previousList.itemSelectionChanged.disconnect(
                self.__itemSelectionChanged)
        
        self.__updateButtons()
        
        currentList = self.tabWidget.currentWidget()
        currentList.itemSelectionChanged.connect(self.__itemSelectionChanged)
        self.__previousCurrent = index
    
    def __updateButtons(self):
        """
        Private method to update the buttons.
        """
        currentList = self.tabWidget.currentWidget()
        self.removeAllButton.setEnabled(
            currentList.topLevelItemCount() > 0)
        self.removeButton.setEnabled(
            len(currentList.selectedItems()) > 0)
    
    @pyqtSlot()
    def __itemSelectionChanged(self):
        """
        Private slot handling changes in the current list of selected items.
        """
        self.__updateButtons()
    
    @pyqtSlot()
    def on_removeButton_clicked(self):
        """
        Private slot to remove selected entries.
        """
        currentList = self.tabWidget.currentWidget()
        for itm in currentList.selectedItems():
            row = currentList.indexOfTopLevelItem(itm)
            itm = currentList.takeTopLevelItem(row)
            del itm
        self.__updateButtons()
    
    @pyqtSlot()
    def on_removeAllButton_clicked(self):
        """
        Private slot to remove all entries.
        """
        currentList = self.tabWidget.currentWidget()
        while currentList.topLevelItemCount() > 0:
            itm = currentList.takeTopLevelItem(0)      # __IGNORE_WARNING__
            del itm
        self.__updateGeoButtons()
    
    def getData(self):
        """
        Public method to retrieve the dialog contents.
        
        @return new feature permission settings
        @rtype dict of dict of list
        """
        featurePermissions = {}
        for feature, permissionsList in self.__permissionsLists.items():
            featurePermissions[feature] = {
                QWebEnginePage.PermissionGrantedByUser: [],
                QWebEnginePage.PermissionDeniedByUser: [],
            }
            for row in range(permissionsList.topLevelItemCount()):
                itm = permissionsList.topLevelItem(row)
                host = itm.text(0)
                permission = itm.data(0, Qt.UserRole)
                featurePermissions[feature][permission].append(host)
        
        return featurePermissions
