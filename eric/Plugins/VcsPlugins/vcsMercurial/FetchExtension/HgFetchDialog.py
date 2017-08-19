# -*- coding: utf-8 -*-

# Copyright (c) 2011 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter data to be used for a fetch operation.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_HgFetchDialog import Ui_HgFetchDialog


class HgFetchDialog(QDialog, Ui_HgFetchDialog):
    """
    Class implementing a dialog to enter data to be used for a fetch operation.
    """
    def __init__(self, vcs, parent=None):
        """
        Constructor
        
        @param vcs reference to the Mercurial vcs object
        @type Hg
        @param parent reference to the parent widget
        @type QWidget
        """
        super(HgFetchDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.__vcs = vcs
        
        commitMessages = self.__vcs.getPlugin().getPreferences('Commits')
        self.recentComboBox.clear()
        self.recentComboBox.addItem("")
        for message in commitMessages:
            abbrMsg = message[:60]
            if len(message) > 60:
                abbrMsg += "..."
            self.recentComboBox.addItem(abbrMsg, message)
    
    @pyqtSlot(str)
    def on_recentComboBox_activated(self, txt):
        """
        Private slot to select a commit message from recent ones.
        
        @param txt text of the selected entry (string)
        """
        if txt:
            self.messageEdit.setPlainText(self.recentComboBox.currentData())
    
    def getData(self):
        """
        Public method to get the data for the fetch operation.
        
        @return tuple with the commit message and a flag indicating to switch
            the merge order (string, boolean)
        """
        msg = self.messageEdit.toPlainText()
        if msg:
            commitMessages = self.__vcs.getPlugin().getPreferences('Commits')
            if msg in commitMessages:
                commitMessages.remove(msg)
            commitMessages.insert(0, msg)
            no = self.__vcs.getPlugin().getPreferences("CommitMessages")
            del commitMessages[no:]
            self.__vcs.getPlugin().setPreferences(
                'Commits', commitMessages)
        
        return msg, self.switchCheckBox.isChecked()
