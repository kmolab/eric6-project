# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to select QtHelp documentation sets to be
installed.
"""

from __future__ import unicode_literals
try:
    str = unicode
except NameError:
    pass

import os
import shutil

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QTreeWidgetItem

from E5Gui import E5MessageBox

from .Ui_QtHelpDocumentationSelectionDialog import \
    Ui_QtHelpDocumentationSelectionDialog


class QtHelpDocumentationSelectionDialog(
        QDialog, Ui_QtHelpDocumentationSelectionDialog):
    """
    Class implementing a dialog to select QtHelp documentation sets to be
    installed.
    """
    AddMode = "Add"
    ManageMode = "Manage"
    
    def __init__(self, helpDocuments, mode, parent=None):
        """
        Constructor
        
        @param helpDocuments dictionary containing the lists of help documents
            to be shown
        @type dict of lists of str
        @param mode mode of the dialog
        @type str
        @param parent reference to the parent widget
        @type QWidget
        """
        super(QtHelpDocumentationSelectionDialog, self).__init__(parent)
        self.setupUi(self)
        
        if mode == QtHelpDocumentationSelectionDialog.AddMode:
            self.buttonBox.button(QDialogButtonBox.Close).hide()
        else:
            self.buttonBox.button(QDialogButtonBox.Ok).hide()
            self.buttonBox.button(QDialogButtonBox.Cancel).hide()
        
        for category in helpDocuments:
            parentItem = QTreeWidgetItem(self.documentationList, [category])
            for document in helpDocuments[category]:
                item = QTreeWidgetItem(parentItem,
                                       [os.path.basename(document)])
                item.setData(0, Qt.UserRole, document)
                parentItem.setData(0, Qt.UserRole, os.path.dirname(document))
        self.documentationList.sortItems(0, Qt.AscendingOrder)
        
        self.on_documentationList_itemSelectionChanged()
    
    @pyqtSlot()
    def on_documentationList_itemSelectionChanged(self):
        """
        Private slot handling the selection of items.
        """
        selectedCategoriesCount = 0
        selectedDocumentSetCount = 0
        for itm in self.documentationList.selectedItems():
            if itm.parent() is None:
                selectedCategoriesCount += 1
            else:
                selectedDocumentSetCount += 1
        
        self.deleteButton.setEnabled(selectedDocumentSetCount > 0)
        self.deleteCategoryButton.setEnabled(selectedCategoriesCount > 0)
    
    @pyqtSlot()
    def on_deleteButton_clicked(self):
        """
        Private slot to delete the selected documentation sets.
        """
        yes = E5MessageBox.yesNo(
            self,
            self.tr("Delete Documentation Sets"),
            self.tr("""Shall the selected documentation sets really be"""
                    """ deleted?"""))
        if yes:
            for itm in self.documentationList.selectedItems():
                if itm.parent is None:
                    # it is a category item, skip it
                    continue
                
                category = itm.parent()
                fileName = itm.data(0, Qt.UserRole)
                try:
                    os.remove(fileName)
                except OSError as err:
                    E5MessageBox.warning(
                        self,
                        self.tr("Delete Documentation Sets"),
                        self.tr("""<p>The documentation set <b>{0}</b> could"""
                                """ not be deleted.</p><p>Reason: {1}</p>""")
                        .format(fileName, str(err)))
                    continue
                
                category.removeChild(itm)
                del itm
                
                if category.childCount() == 0:
                    self.__deleteCategory(category)
    
    @pyqtSlot()
    def on_deleteCategoryButton_clicked(self):
        """
        Private slot to delete the selected documentation set categories.
        """
        yes = E5MessageBox.yesNo(
            self,
            self.tr("Delete Documentation Sets"),
            self.tr("""Shall the selected documentation set categories"""
                    """ really be deleted?"""))
        if yes:
            categories = []
            for itm in self.documentationList.selectedItems():
                if itm.parent() is None:
                    categories.append(itm)
            for category in categories:
                self.__deleteCategory(category)
    
    @pyqtSlot()
    def on_deleteAllButton_clicked(self):
        """
        Private slot to delete all documentation sets.
        """
        yes = E5MessageBox.yesNo(
            self,
            self.tr("Delete Documentation Sets"),
            self.tr("""Shall all documentation sets really be deleted?"""))
        if yes:
            categories = []
            for index in range(self.documentationList.topLevelItemCount()):
                categories.append(
                    self.documentationList.topLevelItem(index))
            for category in categories:
                self.__deleteCategory(category)
    
    def __deleteCategory(self, category):
        """
        Private method to delete a category.
        
        @param category reference to the category item
        @type QTreeWidgetItem
        """
        categoryDir = category.data(0, Qt.UserRole)
        shutil.rmtree(categoryDir, True)
        
        self.documentationList.takeTopLevelItem(
            self.documentationList.indexOfTopLevelItem(category))
        del category
    
    def getData(self):
        """
        Public method to retrieve the selected help documents.
        
        @return list of QtHelp documentation sets to be installed
        @rtype list of str
        """
        documents = []
        for item in self.documentationList.selectedItems():
            fileName = item.data(0, Qt.UserRole)
            if fileName:
                documents.append(fileName)
        return documents
