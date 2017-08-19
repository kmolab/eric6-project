# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a network manager class.
"""

from __future__ import unicode_literals

import json

from PyQt5.QtCore import pyqtSignal, QByteArray
from PyQt5.QtWidgets import qApp, QStyle, QDialog
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkProxy, \
    QNetworkProxyFactory, QNetworkRequest
from PyQt5.QtWebEngineWidgets import QWebEnginePage

from E5Gui import E5MessageBox

from E5Network.E5NetworkProxyFactory import proxyAuthenticationRequired
try:
    from E5Network.E5SslErrorHandler import E5SslErrorHandler
    SSL_AVAILABLE = True
except ImportError:
    SSL_AVAILABLE = False

from WebBrowser.WebBrowserWindow import WebBrowserWindow
from .NetworkUrlInterceptor import NetworkUrlInterceptor
from ..Tools.WebBrowserTools import readAllFileContents, pixmapToDataUrl

from Utilities.AutoSaver import AutoSaver
import Preferences


class NetworkManager(QNetworkAccessManager):
    """
    Class implementing a network manager.
    
    @signal changed() emitted to indicate a change
    """
    changed = pyqtSignal()
    
    def __init__(self, engine, parent=None):
        """
        Constructor
        
        @param engine reference to the help engine (QHelpEngine)
        @param parent reference to the parent object (QObject)
        """
        super(NetworkManager, self).__init__(parent)
        
        if not WebBrowserWindow._fromEric:
            from E5Network.E5NetworkProxyFactory import E5NetworkProxyFactory
            
            self.__proxyFactory = E5NetworkProxyFactory()
            QNetworkProxyFactory.setApplicationProxyFactory(
                self.__proxyFactory)
            
            QNetworkProxyFactory.setUseSystemConfiguration(
                Preferences.getUI("UseSystemProxy"))
        
        self.languagesChanged()
        
        if SSL_AVAILABLE:
            self.__sslErrorHandler = E5SslErrorHandler(self)
            self.sslErrors.connect(self.__sslErrorHandler.sslErrorsReplySlot)
        
        self.__temporarilyIgnoredSslErrors = {}
        self.__permanentlyIgnoredSslErrors = {}
        # dictionaries of permanently and temporarily ignored SSL errors
        
        self.__loaded = False
        self.__saveTimer = AutoSaver(self, self.__save)
        
        self.changed.connect(self.__saveTimer.changeOccurred)
        self.proxyAuthenticationRequired.connect(proxyAuthenticationRequired)
        self.authenticationRequired.connect(
            lambda reply, auth: self.authentication(reply.url(), auth))
        
        from .EricSchemeHandler import EricSchemeHandler
        self.__ericSchemeHandler = EricSchemeHandler()
        WebBrowserWindow.webProfile().installUrlSchemeHandler(
            QByteArray(b"eric"), self.__ericSchemeHandler)
        
        if engine:
            from .QtHelpSchemeHandler import QtHelpSchemeHandler
            self.__qtHelpSchemeHandler = QtHelpSchemeHandler(engine)
            WebBrowserWindow.webProfile().installUrlSchemeHandler(
                QByteArray(b"qthelp"), self.__qtHelpSchemeHandler)
        
        self.__interceptor = NetworkUrlInterceptor(self)
        WebBrowserWindow.webProfile().setRequestInterceptor(self.__interceptor)
        
        WebBrowserWindow.cookieJar()
    
    def __save(self):
        """
        Private slot to save the permanent SSL error exceptions.
        """
        if not self.__loaded:
            return
        
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        if not WebBrowserWindow.isPrivate():
            dbString = json.dumps(self.__permanentlyIgnoredSslErrors)
            Preferences.setWebBrowser("SslExceptionsDB", dbString)
    
    def __load(self):
        """
        Private method to load the permanent SSL error exceptions.
        """
        if self.__loaded:
            return
        
        dbString = Preferences.getWebBrowser("SslExceptionsDB")
        if dbString:
            try:
                db = json.loads(dbString)
                self.__permanentlyIgnoredSslErrors = db
            except ValueError:
                # ignore silently
                pass
        
        self.__loaded = True
    
    def shutdown(self):
        """
        Public method to shut down the network manager.
        """
        self.__saveTimer.saveIfNeccessary()
        self.__loaded = False
        self.__temporarilyIgnoredSslErrors = {}
        self.__permanentlyIgnoredSslErrors = {}
    
    def showSslErrorExceptionsDialog(self):
        """
        Public method to show the SSL error exceptions dialog.
        """
        self.__load()
        
        from .SslErrorExceptionsDialog import SslErrorExceptionsDialog
        dlg = SslErrorExceptionsDialog(self.__permanentlyIgnoredSslErrors)
        if dlg.exec_() == QDialog.Accepted:
            self.__permanentlyIgnoredSslErrors = dlg.getSslErrorExceptions()
            self.changed.emit()
    
    def clearSslExceptions(self):
        """
        Public method to clear the permanent SSL certificate error exceptions.
        """
        self.__load()
        
        self.__permanentlyIgnoredSslErrors = {}
        self.changed.emit()
        self.__saveTimer.saveIfNeccessary()
    
    def certificateError(self, error, view):
        """
        Public method to handle SSL certificate errors.
        
        @param error object containing the certificate error information
        @type QWebEngineCertificateError
        @param view reference to a view to be used as parent for the dialog
        @type QWidget
        @return flag indicating to ignore this error
        @rtype bool
        """
        self.__load()
        
        host = error.url().host()
        
        if host in self.__temporarilyIgnoredSslErrors and \
                error.error() in self.__temporarilyIgnoredSslErrors[host]:
            return True
        
        if host in self.__permanentlyIgnoredSslErrors and \
                error.error() in self.__permanentlyIgnoredSslErrors[host]:
            return True
        
        title = self.tr("SSL Certificate Error")
        msgBox = E5MessageBox.E5MessageBox(
            E5MessageBox.Warning,
            title,
            self.tr("""<b>{0}</b>"""
                    """<p>The page you are trying to access has errors"""
                    """ in the SSL certificate.</p>"""
                    """<ul><li>{1}</li></ul>"""
                    """<p>Would you like to make an exception?</p>""")
            .format(title, error.errorDescription()),
            modal=True, parent=view)
        permButton = msgBox.addButton(self.tr("&Permanent accept"),
                                      E5MessageBox.AcceptRole)
        tempButton = msgBox.addButton(self.tr("&Temporary accept"),
                                      E5MessageBox.AcceptRole)
        msgBox.addButton(self.tr("&Reject"), E5MessageBox.RejectRole)
        msgBox.exec_()
        if msgBox.clickedButton() == permButton:
            if host not in self.__permanentlyIgnoredSslErrors:
                self.__permanentlyIgnoredSslErrors[host] = []
            self.__permanentlyIgnoredSslErrors[host].append(error.error())
            self.changed.emit()
            return True
        elif msgBox.clickedButton() == tempButton:
            if host not in self.__temporarilyIgnoredSslErrors:
                self.__temporarilyIgnoredSslErrors[host] = []
            self.__temporarilyIgnoredSslErrors[host].append(error.error())
            return True
        else:
            return False
    
    def authentication(self, url, auth):
        """
        Public slot to handle an authentication request.
        
        @param url URL requesting authentication (QUrl)
        @param auth reference to the authenticator object (QAuthenticator)
        """
        urlRoot = "{0}://{1}"\
            .format(url.scheme(), url.authority())
        realm = auth.realm()
        if not realm and 'realm' in auth.options():
            realm = auth.option("realm")
        if realm:
            info = self.tr("<b>Enter username and password for '{0}', "
                           "realm '{1}'</b>").format(urlRoot, realm)
        else:
            info = self.tr("<b>Enter username and password for '{0}'</b>")\
                .format(urlRoot)
        
        from UI.AuthenticationDialog import AuthenticationDialog
        import WebBrowser.WebBrowserWindow
        
        dlg = AuthenticationDialog(info, auth.user(),
                                   Preferences.getUser("SavePasswords"),
                                   Preferences.getUser("SavePasswords"))
        if Preferences.getUser("SavePasswords"):
            username, password = \
                WebBrowser.WebBrowserWindow.WebBrowserWindow.passwordManager()\
                .getLogin(url, realm)
            if username:
                dlg.setData(username, password)
        if dlg.exec_() == QDialog.Accepted:
            username, password = dlg.getData()
            auth.setUser(username)
            auth.setPassword(password)
            if Preferences.getUser("SavePasswords") and dlg.shallSave():
                WebBrowser.WebBrowserWindow.WebBrowserWindow.passwordManager()\
                    .setLogin(url, realm, username, password)
        else:
            page = self.sender()
            if isinstance(page, QWebEnginePage):
                self.__showAuthenticationErrorPage(page, url)
    
    def __showAuthenticationErrorPage(self, page, url):
        """
        Private method to show an authentication error page.
        
        @param page reference to the page
        @type QWebEnginePage
        @param url reference to the URL requesting authentication
        @type QUrl
        """
        html = readAllFileContents(":/html/authenticationErrorPage.html")
        html = html.replace("@IMAGE@", pixmapToDataUrl(
            qApp.style().standardIcon(QStyle.SP_MessageBoxCritical).pixmap(
                48, 48)).toString())
        html = html.replace("@FAVICON@", pixmapToDataUrl(
            qApp.style() .standardIcon(QStyle.SP_MessageBoxCritical).pixmap(
                16, 16)).toString())
        html = html.replace("@TITLE@", self.tr("Authentication required"))
        html = html.replace("@H1@", self.tr("Authentication required"))
        html = html.replace(
            "@LI-1@",
            self.tr("Authentication is required to access:"))
        html = html.replace(
            "@LI-2@",
            '<a href="{0}">{0}</a>'.format(url.toString()))
        page.setHtml(html, url)
    
    def proxyAuthentication(self, requestUrl, auth, proxyHost):
        """
        Public slot to handle a proxy authentication request.
        
        @param requestUrl requested URL
        @type QUrl
        @param auth reference to the authenticator object
        @type QAuthenticator
        @param proxyHost name of the proxy host
        @type str
        """
        proxy = QNetworkProxy.applicationProxy()
        if proxy.user() and proxy.password():
            auth.setUser(proxy.user())
            auth.setPassword(proxy.password())
            return
        
        proxyAuthenticationRequired(proxy, auth)
    
    def languagesChanged(self):
        """
        Public slot to (re-)load the list of accepted languages.
        """
        from WebBrowser.WebBrowserLanguagesDialog import \
            WebBrowserLanguagesDialog
        languages = Preferences.toList(
            Preferences.Prefs.settings.value(
                "WebBrowser/AcceptLanguages",
                WebBrowserLanguagesDialog.defaultAcceptLanguages()))
        self.__acceptLanguage = WebBrowserLanguagesDialog.httpString(languages)
        
        WebBrowserWindow.webProfile().setHttpAcceptLanguage(
            self.__acceptLanguage)
    
    def installUrlInterceptor(self, interceptor):
        """
        Public method to install an URL interceptor.
        
        @param interceptor URL interceptor to be installed
        @type UrlInterceptor
        """
        self.__interceptor.installUrlInterceptor(interceptor)
    
    def removeUrlInterceptor(self, interceptor):
        """
        Public method to remove an URL interceptor.
        
        @param interceptor URL interceptor to be removed
        @type UrlInterceptor
        """
        self.__interceptor.removeUrlInterceptor(interceptor)
    
    def preferencesChanged(self):
        """
        Public slot to handle a change of preferences.
        """
        self.__interceptor.preferencesChanged()
            
        if not WebBrowserWindow._fromEric:
            QNetworkProxyFactory.setUseSystemConfiguration(
                Preferences.getUI("UseSystemProxy"))
    
    def createRequest(self, op, request, data):
        """
        Public method to launch a network action.
        
        @param op operation to be performed
        @type QNetworkAccessManager.Operation
        @param request request to be operated on
        @type QNetworkRequest
        @param data reference to the data to be sent
        @type QIODevice
        @return reference to the network reply
        @rtype QNetworkReply
        """
        req = QNetworkRequest(request)
        req.setAttribute(QNetworkRequest.SpdyAllowedAttribute, True)
        req.setAttribute(QNetworkRequest.FollowRedirectsAttribute, True)
        
        return super(NetworkManager, self).createRequest(op, req, data)
