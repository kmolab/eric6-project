# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a button alternating between reload and stop.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt

from E5Gui.E5ToolButton import E5ToolButton

import UI.PixmapCache


class ReloadStopButton(E5ToolButton):
    """
    Class implementing a button alternating between reload and stop.
    
    @signal reloadClicked() emitted to initiate a reload action
    @signal stopClicked() emitted to initiate a stop action
    """
    reloadClicked = pyqtSignal()
    stopClicked = pyqtSignal()
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ReloadStopButton, self).__init__(parent)
        
        self.setObjectName("navigation_reloadstop_button")
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.setFocusPolicy(Qt.NoFocus)
        self.setAutoRaise(True)
        
        self.__loading = False
        
        self.clicked.connect(self.__buttonClicked)
        
        self.__updateButton()
    
    @pyqtSlot()
    def __buttonClicked(self):
        """
        Private slot handling a user clicking the button.
        """
        if self.__loading:
            self.stopClicked.emit()
        else:
            self.reloadClicked.emit()
    
    @pyqtSlot()
    def __updateButton(self):
        """
        Private slot to update the button.
        """
        if self.__loading:
            self.setIcon(UI.PixmapCache.getIcon("stopLoading.png"))
            self.setToolTip(self.tr("Stop loading"))
        else:
            self.setIcon(UI.PixmapCache.getIcon("reload.png"))
            self.setToolTip(self.tr("Reload the current screen"))
    
    def setLoading(self, loading):
        """
        Public method to set the loading state.
        
        @param loading flag indicating the new loading state
        @type bool
        """
        self.__loading = loading
        self.__updateButton()
