# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a widget to stack url bars.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QStackedWidget, QSizePolicy


class StackedUrlBar(QStackedWidget):
    """
    Class implementing a widget to stack URL bars.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(StackedUrlBar, self).__init__(parent)
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(200, 22)
    
    def currentUrlBar(self):
        """
        Public method to get a reference to the current URL bar.
        
        @return reference to the current URL bar (UrlBar)
        """
        return self.urlBar(self.currentIndex())
    
    def urlBar(self, index):
        """
        Public method to get a reference to the URL bar for a given index.
        
        @param index index of the url bar (integer)
        @return reference to the URL bar for the given index (UrlBar)
        """
        return self.widget(index)
    
    def moveBar(self, from_, to_):
        """
        Public slot to move an URL bar.
        
        @param from_ index of URL bar to be moved (integer)
        @param to_ index to move the URL bar to (integer)
        """
        fromBar = self.widget(from_)
        self.removeWidget(fromBar)
        self.insertWidget(to_, fromBar)
    
    def urlBars(self):
        """
        Public method to get a list of references to all URL bars.
        
        @return list of references to URL bars (list of UrlBar)
        """
        urlBars = []
        for index in range(self.count()):
            urlBars.append(self.widget(index))
        return urlBars
