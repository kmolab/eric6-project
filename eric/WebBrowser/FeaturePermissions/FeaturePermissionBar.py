# -*- coding: utf-8 -*-

# Copyright (c) 2015 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the feature permission bar widget.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEnginePage

from E5Gui.E5AnimatedWidget import E5AnimatedWidget

import UI.PixmapCache


class FeaturePermissionBar(E5AnimatedWidget):
    """
    Class implementing the feature permission bar widget.
    """
    DefaultHeight = 30
    
    def __init__(self, page, origin, feature, manager):
        """
        Constructor
        
        @param page reference to the web page
        @type QWebView
        @param origin security origin requesting the feature
        @type QUrl
        @param feature requested feature
        @type QWebPage.Feature
        @param manager reference to the feature permissions manager
        @type FeaturePermissionManager
        """
        super(FeaturePermissionBar, self).__init__(parent=page.view())
        
        self.__origin = QUrl(origin)
        self.__feature = feature
        self.__page = page
        self.__manager = manager
        
        self.__permissionFeatureTexts = {
            QWebEnginePage.Geolocation:
                self.tr("{0} wants to use your position."),
            QWebEnginePage.MediaAudioCapture:
                self.tr("{0} wants to use your microphone."),
            QWebEnginePage.MediaVideoCapture:
                self.tr("{0} wants to use your camera."),
            QWebEnginePage.MediaAudioVideoCapture:
                self.tr("{0} wants to use your microphone and camera."),
            QWebEnginePage.MouseLock:
                self.tr("{0} wants to lock your mouse."),
        }
        self.__permissionFeatureIconNames = {
            QWebEnginePage.Geolocation: "geolocation.png",
            QWebEnginePage.MediaAudioCapture: "audiocapture.png",
            QWebEnginePage.MediaVideoCapture: "camera.png",
            QWebEnginePage.MediaAudioVideoCapture: "audio-video.png",
            QWebEnginePage.MouseLock: "mouse.png",
        }
        
        self.setAutoFillBackground(True)
        self.__layout = QHBoxLayout()
        self.setLayout(self.__layout)
        self.__layout.setContentsMargins(9, 0, 0, 0)
        self.__iconLabel = QLabel(self)
        self.__layout.addWidget(self.__iconLabel)
        self.__messageLabel = QLabel(self)
        self.__layout.addWidget(self.__messageLabel)
        self.__layout.addStretch()
        self.__rememberButton = QPushButton(self.tr("Remember"), self)
        self.__rememberButton.setCheckable(True)
        self.__allowButton = QPushButton(self.tr("Allow"), self)
        self.__denyButton = QPushButton(self.tr("Deny"), self)
        self.__discardButton = QPushButton(UI.PixmapCache.getIcon("close.png"),
                                           "", self)
        self.__allowButton.clicked.connect(self.__permissionGranted)
        self.__denyButton.clicked.connect(self.__permissionDenied)
        self.__discardButton.clicked.connect(self.__permissionUnknown)
        self.__layout.addWidget(self.__rememberButton)
        self.__layout.addWidget(self.__allowButton)
        self.__layout.addWidget(self.__denyButton)
        self.__layout.addWidget(self.__discardButton)
        
        try:
            self.__iconLabel.setPixmap(UI.PixmapCache.getPixmap(
                self.__permissionFeatureIconNames[self.__feature]))
        except KeyError:
            pass
        
        try:
            self.__messageLabel.setText(
                self.__permissionFeatureTexts[self.__feature].format(
                    self.__origin.host()))
        except KeyError:
            self.__messageLabel.setText(
                self.tr("{0} wants to use an unknown feature.").format(
                    self.__origin.host()))
        
        self.__page.loadStarted.connect(self.hide)
        
        self.resize(self.__page.view().width(), self.height())
        self.startAnimation()
    
    @pyqtSlot()
    def hide(self):
        """
        Public slot to hide the animated widget.
        """
        self.__page.loadStarted.disconnect(self.hide)
        super(FeaturePermissionBar, self).hide()
    
    def __permissionDenied(self):
        """
        Private slot handling the user pressing the deny button.
        """
        if self.__page is None or self.__manager is None:
            return
        
        self.__page.setFeaturePermission(
            self.__origin, self.__feature,
            QWebEnginePage.PermissionDeniedByUser)
        
        if self.__rememberButton.isChecked():
            self.__manager.rememberFeaturePermission(
                self.__page.url().host(), self.__feature,
                QWebEnginePage.PermissionDeniedByUser)
        
        self.hide()
    
    def __permissionGranted(self):
        """
        Private slot handling the user pressing the allow button.
        """
        if self.__page is None or self.__manager is None:
            return
        
        self.__page.setFeaturePermission(
            self.__origin, self.__feature,
            QWebEnginePage.PermissionGrantedByUser)
        
        if self.__rememberButton.isChecked():
            self.__manager.rememberFeaturePermission(
                self.__page.url().host(), self.__feature,
                QWebEnginePage.PermissionGrantedByUser)
        
        self.hide()
    
    def __permissionUnknown(self):
        """
        Private slot handling the user closing the dialog without.
        """
        if self.__page is None or self.__manager is None:
            return
        
        self.__page.setFeaturePermission(
            self.__origin, self.__feature,
            QWebEnginePage.PermissionUnknown)
        
        self.hide()
