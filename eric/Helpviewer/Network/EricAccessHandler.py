# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a scheme access handler for Python resources.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QFile, QByteArray

import Utilities

from .SchemeAccessHandler import SchemeAccessHandler


class EricAccessHandler(SchemeAccessHandler):
    """
    Class implementing a scheme access handler for Python resources.
    """
    _homePage = None
    _speedDialPage = None
    
    def createRequest(self, op, request, outgoingData=None):
        """
        Public method to create a request.
        
        @param op the operation to be performed
            (QNetworkAccessManager.Operation)
        @param request reference to the request object (QNetworkRequest)
        @param outgoingData reference to an IODevice containing data to be sent
            (QIODevice)
        @return reference to the created reply object (QNetworkReply)
        """
        from .NetworkReply import NetworkReply
        from .NetworkProtocolUnknownErrorReply import \
            NetworkProtocolUnknownErrorReply

        if request.url().toString() == "eric:home":
            return NetworkReply(request, self.__createHomePage(),
                                "text/html", self.parent())
        elif request.url().toString() == "eric:speeddial":
            return NetworkReply(request, self.__createSpeedDialPage(),
                                "text/html", self.parent())
        
        return NetworkProtocolUnknownErrorReply("eric", self.parent())
    
    def __createHomePage(self):
        """
        Private method to create the Home page.
        
        @return prepared home page (QByteArray)
        """
        if self._homePage is None:
            htmlFile = QFile(":/html/startPage.html")
            htmlFile.open(QFile.ReadOnly)
            html = htmlFile.readAll()
            
            html.replace("@IMAGE@", b"qrc:icons/ericWeb32.png")
            html.replace("@FAVICON@", b"qrc:icons/ericWeb16.png")
            
            self._homePage = html
        
        return QByteArray(self._homePage)
    
    def __createSpeedDialPage(self):
        """
        Private method to create the Speeddial page.
        
        @return prepared speeddial page (QByteArray)
        """
        if self._speedDialPage is None:
            htmlFile = QFile(":/html/speeddialPage.html")
            htmlFile.open(QFile.ReadOnly)
            html = bytes(htmlFile.readAll()).decode()
            
            html = html.replace("@FAVICON@", "qrc:icons/ericWeb16.png")
            html = html.replace("@IMG_PLUS@", "qrc:icons/plus.png")
            html = html.replace("@IMG_CLOSE@", "qrc:icons/close.png")
            html = html.replace("@IMG_EDIT@", "qrc:icons/edit.png")
            html = html.replace("@IMG_RELOAD@", "qrc:icons/reload.png")
            html = html.replace("@IMG_SETTINGS@", "qrc:icons/setting.png")
            html = html.replace("@LOADING-IMG@", "qrc:icons/loading.gif")
            html = html.replace("@BOX-BORDER@",
                                "qrc:icons/box-border-small.png")
            
            html = html.replace("@JQUERY@", "qrc:javascript/jquery.js")
            html = html.replace("@JQUERY-UI@", "qrc:javascript/jquery-ui.js")
            
            html = html.replace("@SITE-TITLE@", self.tr("Speed Dial"))
            html = html.replace("@URL@", self.tr("URL"))
            html = html.replace("@TITLE@", self.tr("Title"))
            html = html.replace("@APPLY@", self.tr("Apply"))
            html = html.replace("@CLOSE@", self.tr("Close"))
            html = html.replace("@NEW-PAGE@", self.tr("New Page"))
            html = html.replace("@TITLE-EDIT@", self.tr("Edit"))
            html = html.replace("@TITLE-REMOVE@", self.tr("Remove"))
            html = html.replace("@TITLE-RELOAD@", self.tr("Reload"))
            html = html.replace("@TITLE-WARN@",
                                self.tr("Are you sure to remove this"
                                        " speed dial?"))
            html = html.replace("@TITLE-WARN-REL@",
                                self.tr("Are you sure you want to reload"
                                        " all speed dials?"))
            html = html.replace("@TITLE-FETCHTITLE@",
                                self.tr("Load title from page"))
            html = html.replace("@SETTINGS-TITLE@",
                                self.tr("Speed Dial Settings"))
            html = html.replace("@ADD-TITLE@", self.tr("Add New Page"))
            html = html.replace("@TXT_NRROWS@",
                                self.tr("Maximum pages in a row:"))
            html = html.replace("@TXT_SDSIZE@",
                                self.tr("Change size of pages:"))
            
            self._speedDialPage = Utilities.html_uencode(html)
        
        import Helpviewer.HelpWindow
        html = QByteArray(self._speedDialPage.encode("utf-8"))
        dial = Helpviewer.HelpWindow.HelpWindow.speedDial()
        
        html.replace("@INITIAL-SCRIPT@", dial.initialScript().encode("utf-8"))
        html.replace("@ROW-PAGES@", str(dial.pagesInRow()).encode("utf-8"))
        html.replace("@SD-SIZE@", str(dial.sdSize()).encode("utf-8"))
        
        return html
