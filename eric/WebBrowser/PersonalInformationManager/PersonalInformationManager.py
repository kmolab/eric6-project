# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a personal information manager used to complete form
fields.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import Qt, QObject, QPoint
from PyQt5.QtWidgets import QDialog, QMenu

import Preferences
import UI.PixmapCache

from ..WebBrowserPage import WebBrowserPage


class PersonalInformationManager(QObject):
    """
    Class implementing the personal information manager used to complete form
    fields.
    """
    FullName = 0
    LastName = 1
    FirstName = 2
    Email = 3
    Mobile = 4
    Phone = 5
    Address = 6
    City = 7
    Zip = 8
    State = 9
    Country = 10
    HomePage = 11
    Special1 = 12
    Special2 = 13
    Special3 = 14
    Special4 = 15
    Max = 16
    Invalid = 256
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(PersonalInformationManager, self).__init__(parent)
        
        self.__loaded = False
        self.__allInfo = {}
        self.__infoMatches = {}
        self.__translations = {}
        
        self.__view = None
        self.__clickedPos = QPoint()
    
    def __loadSettings(self):
        """
        Private method to load the settings.
        """
        self.__allInfo[self.FullName] = \
            Preferences.getWebBrowser("PimFullName")
        self.__allInfo[self.LastName] = \
            Preferences.getWebBrowser("PimLastName")
        self.__allInfo[self.FirstName] = \
            Preferences.getWebBrowser("PimFirstName")
        self.__allInfo[self.Email] = Preferences.getWebBrowser("PimEmail")
        self.__allInfo[self.Mobile] = Preferences.getWebBrowser("PimMobile")
        self.__allInfo[self.Phone] = Preferences.getWebBrowser("PimPhone")
        self.__allInfo[self.Address] = Preferences.getWebBrowser("PimAddress")
        self.__allInfo[self.City] = Preferences.getWebBrowser("PimCity")
        self.__allInfo[self.Zip] = Preferences.getWebBrowser("PimZip")
        self.__allInfo[self.State] = Preferences.getWebBrowser("PimState")
        self.__allInfo[self.Country] = Preferences.getWebBrowser("PimCountry")
        self.__allInfo[self.HomePage] = \
            Preferences.getWebBrowser("PimHomePage")
        self.__allInfo[self.Special1] = \
            Preferences.getWebBrowser("PimSpecial1")
        self.__allInfo[self.Special2] = \
            Preferences.getWebBrowser("PimSpecial2")
        self.__allInfo[self.Special3] = \
            Preferences.getWebBrowser("PimSpecial3")
        self.__allInfo[self.Special4] = \
            Preferences.getWebBrowser("PimSpecial4")
        
        self.__translations[self.FullName] = self.tr("Full Name")
        self.__translations[self.LastName] = self.tr("Last Name")
        self.__translations[self.FirstName] = self.tr("First Name")
        self.__translations[self.Email] = self.tr("E-mail")
        self.__translations[self.Mobile] = self.tr("Mobile")
        self.__translations[self.Phone] = self.tr("Phone")
        self.__translations[self.Address] = self.tr("Address")
        self.__translations[self.City] = self.tr("City")
        self.__translations[self.Zip] = self.tr("ZIP Code")
        self.__translations[self.State] = self.tr("State/Region")
        self.__translations[self.Country] = self.tr("Country")
        self.__translations[self.HomePage] = self.tr("Home Page")
        self.__translations[self.Special1] = self.tr("Custom 1")
        self.__translations[self.Special2] = self.tr("Custom 2")
        self.__translations[self.Special3] = self.tr("Custom 3")
        self.__translations[self.Special4] = self.tr("Custom 4")
        
        self.__infoMatches[self.FullName] = ["fullname", "realname"]
        self.__infoMatches[self.LastName] = ["lastname", "surname"]
        self.__infoMatches[self.FirstName] = ["firstname", "name"]
        self.__infoMatches[self.Email] = ["email", "e-mail", "mail"]
        self.__infoMatches[self.Mobile] = ["mobile", "mobilephone"]
        self.__infoMatches[self.Phone] = ["phone", "telephone"]
        self.__infoMatches[self.Address] = ["address"]
        self.__infoMatches[self.City] = ["city"]
        self.__infoMatches[self.Zip] = ["zip"]
        self.__infoMatches[self.State] = ["state", "region"]
        self.__infoMatches[self.Country] = ["country"]
        self.__infoMatches[self.HomePage] = ["homepage", "www"]
        
        self.__loaded = True
    
    def showConfigurationDialog(self):
        """
        Public method to show the configuration dialog.
        """
        from .PersonalDataDialog import PersonalDataDialog
        dlg = PersonalDataDialog()
        if dlg.exec_() == QDialog.Accepted:
            dlg.storeData()
            self.__loadSettings()
    
    def createSubMenu(self, menu, view, hitTestResult):
        """
        Public method to create the personal information sub-menu.
        
        @param menu reference to the main menu (QMenu)
        @param view reference to the view (HelpBrowser)
        @param hitTestResult reference to the hit test result
            (WebHitTestResult)
        """
        self.__view = view
        self.__clickedPos = hitTestResult.pos()
        
        if not hitTestResult.isContentEditable():
            return
        
        if not self.__loaded:
            self.__loadSettings()
        
        submenu = QMenu(self.tr("Insert Personal Information"), menu)
        submenu.setIcon(UI.PixmapCache.getIcon("pim.png"))
        
        for key, info in sorted(self.__allInfo.items()):
            if info:
                act = submenu.addAction(
                    self.__translations[key], self.__insertData)
                act.setData(info)
        
        submenu.addSeparator()
        submenu.addAction(self.tr("Edit Personal Information"),
                          self.showConfigurationDialog)
        
        menu.addMenu(submenu)
        menu.addSeparator()
    
    def __insertData(self):
        """
        Private slot to insert the selected personal information.
        """
        if self.__view is None or self.__clickedPos.isNull():
            return
        
        act = self.sender()
        if act is None:
            return
        
        info = act.data()
        info = info.replace('"', '\\"')
        
        source = """
            var e = document.elementFromPoint({0}, {1});
            if (e) {{
                var v = e.value.substring(0, e.selectionStart);
                v += "{2}" + e.value.substring(e.selectionEnd);
                e.value = v;
            }}""".format(self.__clickedPos.x(), self.__clickedPos.y(), info)
        self.__view.page().runJavaScript(source, WebBrowserPage.SafeJsWorld)
    
    def viewKeyPressEvent(self, view, evt):
        """
        Protected method to handle key press events we are interested in.
        
        @param view reference to the view (HelpBrowser)
        @param evt reference to the key event (QKeyEvent)
        @return flag indicating handling of the event (boolean)
        """
        if view is None:
            return False
        
        isEnter = evt.key() in [Qt.Key_Return, Qt.Key_Enter]
        isControlModifier = evt.modifiers() & Qt.ControlModifier
        if not isEnter or not isControlModifier:
            return False
        
        if not self.__loaded:
            self.__loadSettings()
        
        source = """
            var inputs = document.getElementsByTagName('input');
            var table = {0};
            for (var i = 0; i < inputs.length; ++i) {{
                var input = inputs[i];
                if (input.type != 'text' || input.name == '')
                    continue;
                for (var key in table) {{
                    if (!table.hasOwnProperty(key))
                        continue;
                    if (key == input.name || input.name.indexOf(key) != -1) {{
                        input.value = table[key];
                        break;
                    }}
                }}
            }}""".format(self.__matchingJsTable())
        view.page().runJavaScript(source, WebBrowserPage.SafeJsWorld)
        
        return True
    
    def connectPage(self, page):
        """
        Public method to allow the personal information manager to connect to
        the page.
        
        @param page reference to the web page (HelpWebPage)
        """
        page.loadFinished.connect(self.__pageLoadFinished)
    
    def __pageLoadFinished(self, ok):
        """
        Private slot to handle the completion of a page load.
        
        @param ok flag indicating a successful load (boolean)
        """
        page = self.sender()
        if page is None or not ok:
            return
        
        if not self.__loaded:
            self.__loadSettings()
        
        source = """
            var inputs = document.getElementsByTagName('input');
            var table = {0};
            for (var i = 0; i < inputs.length; ++i) {{
                var input = inputs[i];
                if (input.type != 'text' || input.name == '')
                    continue;
                for (var key in table) {{
                    if (!table.hasOwnProperty(key) || table[key] == '')
                        continue;
                    if (key == input.name || input.name.indexOf(key) != -1) {{
                        input.style['-webkit-appearance'] = 'none';
                        input.style['-webkit-box-shadow'] =
                            'inset 0 0 2px 1px #000EEE';
                        break;
                    }}
                }}
            }}""".format(self.__matchingJsTable())
        page.runJavaScript(source, WebBrowserPage.SafeJsWorld)
    
    def __matchingJsTable(self):
        """
        Private method to create the common part of the JavaScript sources.
        
        @return JavaScript source
        @rtype str
        """
        values = []
        for key, names in self.__infoMatches.items():
            for name in names:
                value = self.__allInfo[key].replace('"', '\\"')
                values.append('"{0}":"{1}"'.format(name, value))
        return "{{ {0} }}".format(",".join(values))
