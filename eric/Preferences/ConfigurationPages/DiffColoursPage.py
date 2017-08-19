# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Diff colours configuration page.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QColorDialog

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_DiffColoursPage import Ui_DiffColoursPage

import Preferences


class DiffColoursPage(ConfigurationPageBase, Ui_DiffColoursPage):
    """
    Class implementing the Diff colours configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(DiffColoursPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("DiffColoursPage")
        
        self.__coloursDict = {}
        
        monospacedFont = Preferences.getEditorOtherFonts("MonospacedFont")
        self.__allSamples = (
            self.textSample, self.addedSample, self.removedSample,
            self.replacedSample, self.contextSample, self.headerSample,
            self.whitespaceSample)
        for sample in self.__allSamples:
            sample.setFont(monospacedFont)
        
        # set initial values
        self.__initColour("TextColor", self.textButton,
                          self.__updateSampleTextColour,
                          self.__selectTextColour, self.textSample)
        self.__initColour("AddedColor", self.addedButton,
                          self.__updateSampleBackgroundColour,
                          self.__selectBackgroundColour, self.addedSample)
        self.__initColour("RemovedColor", self.removedButton,
                          self.__updateSampleBackgroundColour,
                          self.__selectBackgroundColour, self.removedSample)
        self.__initColour("ReplacedColor", self.replacedButton,
                          self.__updateSampleBackgroundColour,
                          self.__selectBackgroundColour, self.replacedSample)
        self.__initColour("ContextColor", self.contextButton,
                          self.__updateSampleBackgroundColour,
                          self.__selectBackgroundColour, self.contextSample)
        self.__initColour("HeaderColor", self.headerButton,
                          self.__updateSampleBackgroundColour,
                          self.__selectBackgroundColour, self.headerSample)
        self.__initColour("BadWhitespaceColor", self.whitespaceButton,
                          self.__updateSampleBackgroundColour,
                          self.__selectBackgroundColour, self.whitespaceSample)
    
    def save(self):
        """
        Public slot to save the Diff colours configuration.
        """
        for key in self.__coloursDict:
            Preferences.setDiffColour(key, self.__coloursDict[key][0])
    
    def __initColour(self, colourKey, button, initSlot, selectSlot,
                     sampleWidget):
        """
        Private method to initialize a colour selection button.
        
        @param colourKey key of the diff colour
        @type str
        @param button reference to the button
        @type QPushButton
        @param initSlot slot to be called to initialize the sample
        @type func
        @param selectSlot slot to be called to select the colour
        @type func
        @param sampleWidget reference to the sample widget
        @type QLineEdit
        """
        colour = Preferences.getDiffColour(colourKey)
        button.setProperty("colorKey", colourKey)
        button.clicked.connect(selectSlot)
        self.__coloursDict[colourKey] = [colour, sampleWidget]
        if initSlot:
            initSlot(colourKey)
    
    @pyqtSlot()
    def __selectTextColour(self):
        """
        Private slot to select the text colour.
        """
        button = self.sender()
        colorKey = button.property("colorKey")
        
        colour = QColorDialog.getColor(self.__coloursDict[colorKey][0], self)
        if colour.isValid():
            self.__coloursDict[colorKey][0] = colour
            self.__updateSampleTextColour(colorKey)
    
    @pyqtSlot()
    def __selectBackgroundColour(self):
        """
        Private slot to select a background colour.
        """
        button = self.sender()
        colorKey = button.property("colorKey")
        
        colour = QColorDialog.getColor(self.__coloursDict[colorKey][0], self,
                                       "", QColorDialog.ShowAlphaChannel)
        if colour.isValid():
            self.__coloursDict[colorKey][0] = colour
            self.__updateSampleBackgroundColour(colorKey)
    
    @pyqtSlot()
    def __updateSampleTextColour(self, colourKey):
        """
        Private slot to update the text colour of all samples.
        
        @param colourKey key of the diff colour
        @type str
        """
        colour = self.__coloursDict[colourKey][0]
        for sample in self.__allSamples:
            pl = sample.palette()
            pl.setColor(QPalette.Text, colour)
            sample.setPalette(pl)
            sample.repaint()
    
    def __updateSampleBackgroundColour(self, colourKey):
        """
        Private slot to update the background colour of a sample.
        
        @param colourKey key of the diff colour
        @type str
        """
        sample = self.__coloursDict[colourKey][1]
        if sample:
            colour = self.__coloursDict[colourKey][0]
            pl = sample.palette()
            pl.setColor(QPalette.Base, colour)
            sample.setPalette(pl)
            sample.repaint()


def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = DiffColoursPage()
    return page
