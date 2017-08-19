# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to select which private data to clear.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QDialog

from .Ui_WebBrowserClearPrivateDataDialog import \
    Ui_WebBrowserClearPrivateDataDialog


class WebBrowserClearPrivateDataDialog(QDialog,
                                       Ui_WebBrowserClearPrivateDataDialog):
    """
    Class implementing a dialog to select which private data to clear.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(WebBrowserClearPrivateDataDialog, self).__init__(parent)
        self.setupUi(self)
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    def getData(self):
        """
        Public method to get the data from the dialog.
        
        @return tuple with flags indicating which data to clear
            (browsing history, search history, favicons, disk cache, cookies,
            passwords, web databases, downloads, flash, zoom values, SSL
            certificate error exceptions) and the selected history period in
            milliseconds (tuple of booleans and integer)
        """
        index = self.historyCombo.currentIndex()
        if index == 0:
            # last hour
            historyPeriod = 60 * 60 * 1000
        elif index == 1:
            # last day
            historyPeriod = 24 * 60 * 60 * 1000
        elif index == 2:
            # last week
            historyPeriod = 7 * 24 * 60 * 60 * 1000
        elif index == 3:
            # last four weeks
            historyPeriod = 4 * 7 * 24 * 60 * 60 * 1000
        elif index == 4:
            # clear all
            historyPeriod = 0
        
        return (self.historyCheckBox.isChecked(),
                self.searchCheckBox.isChecked(),
                self.iconsCheckBox.isChecked(),
                self.cacheCheckBox.isChecked(),
                self.cookiesCheckBox.isChecked(),
                self.passwordsCheckBox.isChecked(),
                self.databasesCheckBox.isChecked(),
                self.downloadsCheckBox.isChecked(),
                self.flashCookiesCheckBox.isChecked(),
                self.zoomCheckBox.isChecked(),
                self.sslExceptionsCheckBox.isChecked(),
                historyPeriod)
