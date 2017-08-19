# -*- coding: utf-8 -*-

# Copyright (c) 2010 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the commit message.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt, QDateTime
from PyQt5.QtWidgets import QWidget, QDialogButtonBox

from .Ui_HgCommitDialog import Ui_HgCommitDialog


class HgCommitDialog(QWidget, Ui_HgCommitDialog):
    """
    Class implementing a dialog to enter the commit message.
    
    @signal accepted() emitted, if the dialog was accepted
    @signal rejected() emitted, if the dialog was rejected
    """
    accepted = pyqtSignal()
    rejected = pyqtSignal()
    
    def __init__(self, vcs, msg, mq, parent=None):
        """
        Constructor
        
        @param vcs reference to the vcs object
        @param msg initial message (string)
        @param mq flag indicating a queue commit (boolean)
        @param parent parent widget (QWidget)
        """
        super(HgCommitDialog, self).__init__(parent, Qt.WindowFlags(Qt.Window))
        self.setupUi(self)
        
        self.__vcs = vcs
        
        self.logEdit.setPlainText(msg)
        
        if mq:
            self.amendCheckBox.setVisible(False)
            self.subrepoCheckBox.setVisible(False)
        else:
            self.subrepoCheckBox.setVisible(vcs.hasSubrepositories())
    
    def showEvent(self, evt):
        """
        Protected method called when the dialog is about to be shown.
        
        @param evt the event (QShowEvent)
        """
        commitMessages = self.__vcs.getPlugin().getPreferences('Commits')
        self.recentComboBox.clear()
        self.recentComboBox.addItem("")
        for message in commitMessages:
            abbrMsg = message[:60]
            if len(message) > 60:
                abbrMsg += "..."
            self.recentComboBox.addItem(abbrMsg, message)
        
        commitAuthors = self.__vcs.getPlugin().getPreferences('CommitAuthors')
        self.authorComboBox.clear()
        self.authorComboBox.addItem("")
        self.authorComboBox.addItems(commitAuthors)
        
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        self.logEdit.setFocus(Qt.OtherFocusReason)
    
    def on_buttonBox_clicked(self, button):
        """
        Private slot called by a button of the button box clicked.
        
        @param button button that was clicked (QAbstractButton)
        """
        if button == self.buttonBox.button(QDialogButtonBox.Cancel):
            self.logEdit.clear()
    
    def on_buttonBox_accepted(self):
        """
        Private slot called by the buttonBox accepted signal.
        """
        self.close()
        self.accepted.emit()
    
    def on_buttonBox_rejected(self):
        """
        Private slot called by the buttonBox rejected signal.
        """
        self.close()
        self.rejected.emit()
    
    @pyqtSlot(str)
    def on_recentComboBox_activated(self, txt):
        """
        Private slot to select a commit message from recent ones.
        
        @param txt text of the selected entry (string)
        """
        if txt:
            self.logEdit.setPlainText(self.recentComboBox.currentData())
    
    def getCommitData(self):
        """
        Public method to retrieve the entered data for the commit.
        
        @return tuple containing the log message, a flag indicating to amend
            the last commit, a flag indicating to commit subrepositories as
            well, name of the author and date/time of the commit
        @rtype tuple of str, bool, bool, str, str
        """
        msg = self.logEdit.toPlainText()
        if msg:
            commitMessages = self.__vcs.getPlugin().getPreferences('Commits')
            if msg in commitMessages:
                commitMessages.remove(msg)
            commitMessages.insert(0, msg)
            no = self.__vcs.getPlugin().getPreferences("CommitMessages")
            del commitMessages[no:]
            self.__vcs.getPlugin().setPreferences(
                'Commits', commitMessages)
        
        author = self.authorComboBox.currentText()
        if author:
            commitAuthors = \
                self.__vcs.getPlugin().getPreferences('CommitAuthors')
            if author in commitAuthors:
                commitAuthors.remove(author)
            commitAuthors.insert(0, author)
            no = self.__vcs.getPlugin().getPreferences("CommitAuthorsLimit")
            del commitAuthors[no:]
            self.__vcs.getPlugin().setPreferences(
                'CommitAuthors', commitAuthors)
        
        if self.dateTimeGroup.isChecked():
            dateTime = \
                self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm")
        else:
            dateTime = ""
        
        return (
            msg,
            self.amendCheckBox.isChecked(),
            self.subrepoCheckBox.isChecked(),
            author,
            dateTime,
        )
