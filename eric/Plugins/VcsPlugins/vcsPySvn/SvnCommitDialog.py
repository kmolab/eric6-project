# -*- coding: utf-8 -*-

# Copyright (c) 2003 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the commit message.
"""

from __future__ import unicode_literals

import pysvn

from PyQt5.QtCore import pyqtSignal, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QDialogButtonBox

from .Ui_SvnCommitDialog import Ui_SvnCommitDialog

import Preferences


class SvnCommitDialog(QWidget, Ui_SvnCommitDialog):
    """
    Class implementing a dialog to enter the commit message.
    
    @signal accepted() emitted, if the dialog was accepted
    @signal rejected() emitted, if the dialog was rejected
    """
    accepted = pyqtSignal()
    rejected = pyqtSignal()
    
    def __init__(self, changelists, parent=None):
        """
        Constructor
        
        @param changelists list of available change lists (list of strings)
        @param parent parent widget (QWidget)
        """
        super(SvnCommitDialog, self).__init__(
            parent, Qt.WindowFlags(Qt.Window))
        self.setupUi(self)
        
        if pysvn.svn_version < (1, 5, 0) or pysvn.version < (1, 6, 0):
            self.changeListsGroup.hide()
        else:
            self.changeLists.addItems(sorted(changelists))
        
    def showEvent(self, evt):
        """
        Protected method called when the dialog is about to be shown.
        
        @param evt the event (QShowEvent)
        """
        self.recentCommitMessages = Preferences.toList(
            Preferences.Prefs.settings.value('Subversion/Commits'))
        self.recentComboBox.clear()
        self.recentComboBox.addItem("")
        self.recentComboBox.addItems(self.recentCommitMessages)
        
        self.logEdit.setFocus(Qt.OtherFocusReason)
        
    def logMessage(self):
        """
        Public method to retrieve the log message.
        
        This method has the side effect of saving the 20 most recent
        commit messages for reuse.
        
        @return the log message (string)
        """
        msg = self.logEdit.toPlainText()
        if msg:
            if msg in self.recentCommitMessages:
                self.recentCommitMessages.remove(msg)
            self.recentCommitMessages.insert(0, msg)
            no = int(Preferences.Prefs.settings.value(
                'Subversion/CommitMessages', 20))
            del self.recentCommitMessages[no:]
            Preferences.Prefs.settings.setValue(
                'Subversion/Commits', self.recentCommitMessages)
        return msg
        
    def hasChangelists(self):
        """
        Public method to check, if the user entered some changelists.
        
        @return flag indicating availability of changelists (boolean)
        """
        return len(self.changeLists.selectedItems()) > 0
        
    def changelistsData(self):
        """
        Public method to retrieve the changelists data.
        
        @return tuple containing the changelists (list of strings) and a flag
            indicating to keep changelists (boolean)
        """
        slists = [l.text().strip() for l in self.changeLists.selectedItems()
                  if l.text().strip() != ""]
        
        if len(slists) == 0:
            return [], False
        
        return slists, self.keepChangeListsCheckBox.isChecked()
        
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
        
        @param txt selected recent commit message (string)
        """
        if txt:
            self.logEdit.setPlainText(txt)
