# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the variables filter dialog.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QListWidgetItem

from Debugger.Config import ConfigVarTypeDispStrings, ConfigVarTypeFilters
import Preferences

from .Ui_VariablesFilterDialog import Ui_VariablesFilterDialog


class VariablesFilterDialog(QDialog, Ui_VariablesFilterDialog):
    """
    Class implementing the variables filter dialog.
    
    It opens a dialog window for the configuration of the variables type
    filter to be applied during a debugging session.
    """
    def __init__(self, parent=None, name=None, modal=False):
        """
        Constructor
        
        @param parent parent widget of this dialog (QWidget)
        @param name name of this dialog (string)
        @param modal flag to indicate a modal dialog (boolean)
        """
        super(VariablesFilterDialog, self).__init__(parent)
        if name:
            self.setObjectName(name)
        self.setModal(modal)
        self.setupUi(self)

        self.defaultButton = self.buttonBox.addButton(
            self.tr("Save Default"), QDialogButtonBox.ActionRole)
        
        #populate the list widgets and set the default selection
        for widget in self.localsList, self.globalsList:
            for varType, varTypeStr in ConfigVarTypeDispStrings.items():
                itm = QListWidgetItem(self.tr(varTypeStr), widget)
                itm.setData(Qt.UserRole, ConfigVarTypeFilters[varType])
                itm.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
                itm.setCheckState(Qt.Unchecked)
                widget.addItem(itm)
        
        lDefaultFilter, gDefaultFilter = Preferences.getVarFilters()
        self.setSelection(lDefaultFilter, gDefaultFilter)

    def getSelection(self):
        """
        Public slot to retrieve the current selections.
        
        @return A tuple of lists of integer values. The first list is the
            locals variables filter, the second the globals variables filter.
        """
        lList = []
        for row in range(self.localsList.count()):
            itm = self.localsList.item(row)
            if itm.checkState() == Qt.Unchecked:
                lList.append(itm.data(Qt.UserRole))
        
        gList = []
        for row in range(self.globalsList.count()):
            itm = self.globalsList.item(row)
            if itm.checkState() == Qt.Unchecked:
                gList.append(itm.data(Qt.UserRole))
        return (lList, gList)
    
    def setSelection(self, lList, gList):
        """
        Public slot to set the current selection.
        
        @param lList local variables filter (list of int)
        @param gList global variables filter (list of int)
        """
        for row in range(self.localsList.count()):
            itm = self.localsList.item(row)
            if itm.data(Qt.UserRole) in lList:
                itm.setCheckState(Qt.Unchecked)
            else:
                itm.setCheckState(Qt.Checked)
        
        for row in range(self.globalsList.count()):
            itm = self.globalsList.item(row)
            if itm.data(Qt.UserRole) in gList:
                itm.setCheckState(Qt.Unchecked)
            else:
                itm.setCheckState(Qt.Checked)

    def on_buttonBox_clicked(self, button):
        """
        Private slot called by a button of the button box clicked.
        
        @param button button that was clicked (QAbstractButton)
        """
        if button == self.defaultButton:
            Preferences.setVarFilters(self.getSelection())
