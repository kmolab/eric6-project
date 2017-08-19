# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the search box for the shell, terminal and log viewer.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

import UI.PixmapCache


class SearchWidget(QWidget):
    """
    Class implementing the search box for the shell, terminal and log viewer.
    
    @signal searchNext(text, caseSensitive, wholeWord) emitted when the user
        pressed the next button (string, boolean, boolean)
    @signal searchPrevious(text, caseSensitive, wholeWord) emitted when the
        user pressed the previous button (string, boolean, boolean)
    """
    searchNext = pyqtSignal(str, bool, bool)
    searchPrevious = pyqtSignal(str, bool, bool)
    
    def __init__(self, mainWindow, parent=None, spacer=True, showLine=False):
        """
        Constructor
        
        @param mainWindow reference to the main window (QWidget)
        @param parent reference to the parent widget (QWidget)
        @param spacer flag indicating to add a vertical spacer to the
            main layout (boolean)
        @param showLine flag indicating to show all widget in one row (boolean)
        """
        super(SearchWidget, self).__init__(parent)
        
        if showLine:
            from .Ui_SearchWidgetLine import Ui_SearchWidgetLine
            self.__ui = Ui_SearchWidgetLine()
        else:
            from .Ui_SearchWidget import Ui_SearchWidget
            self.__ui = Ui_SearchWidget()
        self.__ui.setupUi(self)
        if not showLine:
            if spacer:
                spacerItem = QSpacerItem(
                    20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
                self.__ui.verticalLayout.addItem(spacerItem)
            else:
                # change the size policy of the search combo if the spacer is
                # not wanted, i.e. it is below the to be searched widget
                sizePolicy = self.__ui.findtextCombo.sizePolicy()
                sizePolicy.setHorizontalPolicy(QSizePolicy.Expanding)
                self.__ui.findtextCombo.setSizePolicy(sizePolicy)
        
        self.__mainWindow = mainWindow
        self.__findBackwards = True
        
        self.__ui.closeButton.setIcon(
            UI.PixmapCache.getIcon("close.png"))
        self.__ui.findPrevButton.setIcon(
            UI.PixmapCache.getIcon("1leftarrow.png"))
        self.__ui.findNextButton.setIcon(
            UI.PixmapCache.getIcon("1rightarrow.png"))
        
        self.findHistory = []
        
        self.__ui.findtextCombo.setCompleter(None)
        self.__ui.findtextCombo.lineEdit().returnPressed.connect(
            self.__findByReturnPressed)
        
        msh = self.minimumSizeHint()
        self.resize(max(self.width(), msh.width()), msh.height())
    
    @pyqtSlot()
    def on_closeButton_clicked(self):
        """
        Private slot to close the widget.
        """
        self.close()
    
    def keyPressEvent(self, event):
        """
        Protected slot to handle key press events.
        
        @param event reference to the key press event (QKeyEvent)
        """
        if event.key() == Qt.Key_Escape:
            self.__mainWindow.setFocus(Qt.ActiveWindowFocusReason)
            event.accept()
            self.close()
    
    @pyqtSlot()
    def on_findNextButton_clicked(self):
        """
        Private slot to find the next occurrence.
        """
        txt = self.__ui.findtextCombo.currentText()
        if not txt and not self.isVisible():
            self.showFind()
            return
        
        self.__findBackwards = False
        
        # This moves any previous occurrence of this statement to the head
        # of the list and updates the combobox
        if txt in self.findHistory:
            self.findHistory.remove(txt)
        self.findHistory.insert(0, txt)
        self.__ui.findtextCombo.clear()
        self.__ui.findtextCombo.addItems(self.findHistory)
        
        self.searchNext.emit(
            txt,
            self.__ui.caseCheckBox.isChecked(),
            self.__ui.wordCheckBox.isChecked())
    
    @pyqtSlot()
    def on_findPrevButton_clicked(self):
        """
        Private slot to find the previous occurrence.
        """
        txt = self.__ui.findtextCombo.currentText()
        if not txt and not self.isVisible():
            self.showFind()
            return
        
        self.__findBackwards = True
        
        # This moves any previous occurrence of this statement to the head
        # of the list and updates the combobox
        if txt in self.findHistory:
            self.findHistory.remove(txt)
        self.findHistory.insert(0, txt)
        self.__ui.findtextCombo.clear()
        self.__ui.findtextCombo.addItems(self.findHistory)
        
        self.searchPrevious.emit(
            txt,
            self.__ui.caseCheckBox.isChecked(),
            self.__ui.wordCheckBox.isChecked())
    
    @pyqtSlot(str)
    def on_findtextCombo_editTextChanged(self, txt):
        """
        Private slot to enable/disable the find buttons.
        
        @param txt text of the combobox (string)
        """
        self.__setSearchButtons(txt != "")
    
    def __setSearchButtons(self, enabled):
        """
        Private slot to set the state of the search buttons.
        
        @param enabled flag indicating the state (boolean)
        """
        self.__ui.findPrevButton.setEnabled(enabled)
        self.__ui.findNextButton.setEnabled(enabled)
    
    def __findByReturnPressed(self):
        """
        Private slot to handle the returnPressed signal of the findtext
        combobox.
        """
        if self.__findBackwards:
            self.on_findPrevButton_clicked()
        else:
            self.on_findNextButton_clicked()

    def showFind(self, txt=""):
        """
        Public method to display this widget.
        
        @param txt text to be shown in the combo (string)
        """
        self.__ui.findtextCombo.clear()
        self.__ui.findtextCombo.addItems(self.findHistory)
        self.__ui.findtextCombo.setEditText(txt)
        self.__ui.findtextCombo.setFocus()
        
        self.__setSearchButtons(txt != "")
        
        self.show()
    
    def searchStringFound(self, found):
        """
        Public slot to indicate that the search string was found.
        
        @param found flag indicating success (boolean)
        """
        if found:
            self.__ui.statusLabel.clear()
        else:
            txt = self.__ui.findtextCombo.currentText()
            self.__ui.statusLabel.setText(
                self.tr("'{0}' was not found.").format(txt))
