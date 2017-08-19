# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter options used to start a project in
the VCS.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import QDir, pyqtSlot
from PyQt5.QtWidgets import QDialog, QDialogButtonBox

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_SvnOptionsDialog import Ui_SvnOptionsDialog
from .Config import ConfigSvnProtocols

import Utilities


class SvnOptionsDialog(QDialog, Ui_SvnOptionsDialog):
    """
    Class implementing a dialog to enter options used to start a project in the
    repository.
    """
    def __init__(self, vcs, project, parent=None):
        """
        Constructor
        
        @param vcs reference to the version control object
        @param project reference to the project object
        @param parent parent widget (QWidget)
        """
        super(SvnOptionsDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.vcsUrlPicker.setMode(E5PathPickerModes.DirectoryMode)
        
        self.project = project
        
        self.protocolCombo.addItems(ConfigSvnProtocols)
        
        hd = Utilities.toNativeSeparators(QDir.homePath())
        hd = os.path.join(hd, 'subversionroot')
        self.vcsUrlPicker.setText(hd)
        
        self.vcs = vcs
        
        self.localPath = hd
        self.networkPath = "localhost/"
        self.localProtocol = True
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
        
    @pyqtSlot()
    def on_vcsUrlPicker_pickerButtonClicked(self):
        """
        Private slot to display a repository browser dialog.
        """
        from .SvnRepoBrowserDialog import SvnRepoBrowserDialog
        dlg = SvnRepoBrowserDialog(self.vcs, mode="select", parent=self)
        dlg.start(
            self.protocolCombo.currentText() + self.vcsUrlPicker.text())
        if dlg.exec_() == QDialog.Accepted:
            url = dlg.getSelectedUrl()
            if url:
                protocol = url.split("://")[0]
                path = url.split("://")[1]
                self.protocolCombo.setCurrentIndex(
                    self.protocolCombo.findText(protocol + "://"))
                self.vcsUrlPicker.setText(path)
        
    @pyqtSlot(str)
    def on_protocolCombo_activated(self, protocol):
        """
        Private slot to switch the status of the directory selection button.
        
        @param protocol selected protocol (string)
        """
        if protocol == "file://":
            self.networkPath = self.vcsUrlPicker.text()
            self.vcsUrlPicker.setText(self.localPath)
            self.vcsUrlLabel.setText(self.tr("Pat&h:"))
            self.localProtocol = True
        else:
            if self.localProtocol:
                self.localPath = self.vcsUrlPicker.text()
                self.vcsUrlPicker.setText(self.networkPath)
                self.vcsUrlLabel.setText(self.tr("&URL:"))
                self.localProtocol = False
    
    @pyqtSlot(str)
    def on_vcsUrlPicker_textChanged(self, txt):
        """
        Private slot to handle changes of the URL.
        
        @param txt current text of the line edit (string)
        """
        enable = "://" not in txt
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(enable)
        
    def getData(self):
        """
        Public slot to retrieve the data entered into the dialog.
        
        @return a dictionary containing the data entered
        """
        scheme = self.protocolCombo.currentText()
        url = self.vcsUrlPicker.text()
        vcsdatadict = {
            "url": '{0}{1}'.format(scheme, url),
            "message": self.vcsLogEdit.text(),
            "standardLayout": self.layoutCheckBox.isChecked(),
        }
        return vcsdatadict
