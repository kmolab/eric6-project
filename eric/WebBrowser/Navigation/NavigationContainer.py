# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the navigation container widget.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy


class NavigationContainer(QWidget):
    """
    Class implementing the navigation container widget.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(NavigationContainer, self).__init__(parent)
        self.setObjectName("navigationcontainer")
        
        self.__layout = QVBoxLayout(self)
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)
        
        self.setLayout(self.__layout)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
    
    def addWidget(self, widget):
        """
        Public method to add a widget to the container.
        
        @param widget reference to the widget to be added
        @type QWidget
        """
        self.__layout.addWidget(widget)
