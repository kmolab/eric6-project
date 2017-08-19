# -*- coding: utf-8 -*-

# Copyright (c) 2015 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a statusbar icon tracking the network status.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtNetwork import QNetworkConfigurationManager
from PyQt5.QtWidgets import QLabel

import UI.PixmapCache
import Preferences


class E5NetworkIcon(QLabel):
    """
    Class implementing a statusbar icon tracking the network status.
    
    @signal onlineStateChanged(online) emitted to indicate a change of the
        network state
    """
    onlineStateChanged = pyqtSignal(bool)
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(E5NetworkIcon, self).__init__(parent)
        
        if Preferences.getUI("DynamicOnlineCheck"):
            self.__networkManager = QNetworkConfigurationManager(self)
            self.__online = self.__networkManager.isOnline()
            self.__onlineStateChanged(self.__online)
            
            self.__networkManager.onlineStateChanged.connect(
                self.__onlineStateChanged)
        else:
            self.__online = True
            self.__onlineStateChanged(self.__online)
    
    @pyqtSlot(bool)
    def __onlineStateChanged(self, online):
        """
        Private slot handling online state changes.
        
        @param online flag indicating the online status
        @type bool
        """
        if online:
            self.setPixmap(UI.PixmapCache.getPixmap("network-online.png"))
        else:
            self.setPixmap(UI.PixmapCache.getPixmap("network-offline.png"))
        
        tooltip = self.tr("<p>Shows the network status<br/><br/>"
                          "<b>Network:</b> {0}</p>")
        
        if online:
            tooltip = tooltip.format(self.tr("Connected"))
        else:
            tooltip = tooltip.format(self.tr("Offline"))
        
        self.setToolTip(tooltip)
        
        if online != self.__online:
            self.__online = online
            self.onlineStateChanged.emit(online)
    
    def isOnline(self):
        """
        Public method to get the online state.
        
        @return online state
        @rtype bool
        """
        return self.__online
