# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter the data for printing a web page to PDF.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSlot, QMarginsF, QStandardPaths
from PyQt5.QtGui import QPageLayout, QPageSize
from PyQt5.QtPrintSupport import QPrinter, QPageSetupDialog
from PyQt5.QtWidgets import QDialog

from E5Gui.E5PathPicker import E5PathPickerModes

from .Ui_PrintToPdfDialog import Ui_PrintToPdfDialog


class PrintToPdfDialog(QDialog, Ui_PrintToPdfDialog):
    """
    Class implementing a dialog to enter the data for printing a web page to
    PDF.
    """
    def __init__(self, filePath, parent=None):
        """
        Constructor
        
        @param filePath path of the file to write into
        @type str
        @param parent reference to the parent widget
        @type QWidget
        """
        super(PrintToPdfDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.pdfFilePicker.setMode(E5PathPickerModes.SaveFileOverwriteMode)
        self.pdfFilePicker.setFilters(self.tr(
            "PDF Files (*.pdf);;"
            "All Files (*)"))
        if not os.path.isabs(filePath):
            documentsPath = QStandardPaths.writableLocation(
                QStandardPaths.DocumentsLocation)
            if documentsPath:
                filePath = os.path.join(documentsPath, filePath)
            else:
                filePath = os.path.abspath(filePath)
        self.pdfFilePicker.setText(filePath, toNative=True)
        
        self.__currentPageLayout = QPageLayout(
            QPageSize(QPageSize.A4), QPageLayout.Portrait,
            QMarginsF(0.0, 0.0, 0.0, 0.0))
        
        self.__updatePageLayoutLabel()
    
    @pyqtSlot()
    def on_pageLayoutButton_clicked(self):
        """
        Private slot to define the page layout.
        """
        printer = QPrinter()
        printer.setPageLayout(self.__currentPageLayout)
        
        dlg = QPageSetupDialog(printer, self)
        if dlg.exec_() == QDialog.Accepted:
            self.__currentPageLayout = printer.pageLayout()
            self.__updatePageLayoutLabel()
    
    def __updatePageLayoutLabel(self):
        """
        Private method to update the page layout label.
        """
        if self.__currentPageLayout.orientation() == QPageLayout.Portrait:
            orientation = self.tr("Portrait")
        else:
            orientation = self.tr("Landscape")
        self.pageLayoutLabel.setText(
            self.tr("{0}, {1}", "page size, page orientation").format(
                self.__currentPageLayout.pageSize().name(),
                orientation))
    
    def getData(self):
        """
        Public method to get the dialog data.
        
        @return tuple containing the file path and the page layout
        @rtype tuple of str and QPageLayout
        """
        return (
            self.pdfFilePicker.text(toNative=True),
            self.__currentPageLayout,
        )
