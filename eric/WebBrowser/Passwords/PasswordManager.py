# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the password manager.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, QObject, QByteArray, QUrl, \
    QCoreApplication, QXmlStreamReader
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineScript

from E5Gui import E5MessageBox
from E5Gui.E5ProgressDialog import E5ProgressDialog

from Utilities.AutoSaver import AutoSaver
import Utilities
import Utilities.crypto
import Preferences

import WebBrowser.WebBrowserWindow
from ..Tools import Scripts
from ..WebBrowserPage import WebBrowserPage


class PasswordManager(QObject):
    """
    Class implementing the password manager.
    
    @signal changed() emitted to indicate a change
    @signal passwordsSaved() emitted after the passwords were saved
    """
    changed = pyqtSignal()
    passwordsSaved = pyqtSignal()
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(PasswordManager, self).__init__(parent)
        
        # setup userscript to monitor forms
        script = QWebEngineScript()
        script.setName("_eric_passwordmonitor")
        script.setInjectionPoint(QWebEngineScript.DocumentReady)
        script.setWorldId(WebBrowserPage.SafeJsWorld)
        script.setRunsOnSubFrames(True)
        script.setSourceCode(Scripts.setupFormObserver())
        profile = WebBrowser.WebBrowserWindow.WebBrowserWindow.webProfile()
        profile.scripts().insert(script)
        
        self.__logins = {}
        self.__loginForms = {}
        self.__never = []
        self.__loaded = False
        self.__saveTimer = AutoSaver(self, self.save)
        
        self.changed.connect(self.__saveTimer.changeOccurred)
    
    def clear(self):
        """
        Public slot to clear the saved passwords.
        """
        if not self.__loaded:
            self.__load()
        
        self.__logins = {}
        self.__loginForms = {}
        self.__never = []
        self.__saveTimer.changeOccurred()
        self.__saveTimer.saveIfNeccessary()
        
        self.changed.emit()
    
    def getLogin(self, url, realm):
        """
        Public method to get the login credentials.
        
        @param url URL to get the credentials for (QUrl)
        @param realm realm to get the credentials for (string)
        @return tuple containing the user name (string) and password (string)
        """
        if not self.__loaded:
            self.__load()
        
        key = self.__createKey(url, realm)
        try:
            return self.__logins[key][0], Utilities.crypto.pwConvert(
                self.__logins[key][1], encode=False)
        except KeyError:
            return "", ""
    
    def setLogin(self, url, realm, username, password):
        """
        Public method to set the login credentials.
        
        @param url URL to set the credentials for (QUrl)
        @param realm realm to set the credentials for (string)
        @param username username for the login (string)
        @param password password for the login (string)
        """
        if not self.__loaded:
            self.__load()
        
        key = self.__createKey(url, realm)
        self.__logins[key] = (
            username,
            Utilities.crypto.pwConvert(password, encode=True)
        )
        self.changed.emit()
    
    def __createKey(self, url, realm):
        """
        Private method to create the key string for the login credentials.
        
        @param url URL to get the credentials for (QUrl)
        @param realm realm to get the credentials for (string)
        @return key string (string)
        """
        authority = url.authority()
        if authority.startswith("@"):
            authority = authority[1:]
        if realm:
            key = "{0}://{1} ({2})".format(
                url.scheme(), authority, realm)
        else:
            key = "{0}://{1}".format(url.scheme(), authority)
        return key
    
    def getFileName(self):
        """
        Public method to get the file name of the passwords file.
        
        @return name of the passwords file (string)
        """
        return os.path.join(Utilities.getConfigDir(),
                            "web_browser", "logins.xml")
    
    def save(self):
        """
        Public slot to save the login entries to disk.
        """
        if not self.__loaded:
            return
        
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        if not WebBrowserWindow.isPrivate():
            from .PasswordWriter import PasswordWriter
            loginFile = self.getFileName()
            writer = PasswordWriter()
            if not writer.write(
                    loginFile, self.__logins, self.__loginForms, self.__never):
                E5MessageBox.critical(
                    None,
                    self.tr("Saving login data"),
                    self.tr(
                        """<p>Login data could not be saved to"""
                        """ <b>{0}</b></p>"""
                    ).format(loginFile))
            else:
                self.passwordsSaved.emit()
    
    def __load(self):
        """
        Private method to load the saved login credentials.
        """
        if self.__loaded:
            return
        
        loginFile = self.getFileName()
        if os.path.exists(loginFile):
            from .PasswordReader import PasswordReader
            reader = PasswordReader()
            self.__logins, self.__loginForms, self.__never = \
                reader.read(loginFile)
            if reader.error() != QXmlStreamReader.NoError:
                E5MessageBox.warning(
                    None,
                    self.tr("Loading login data"),
                    self.tr("""Error when loading login data on"""
                            """ line {0}, column {1}:\n{2}""")
                    .format(reader.lineNumber(),
                            reader.columnNumber(),
                            reader.errorString()))
        
        self.__loaded = True
    
    def reload(self):
        """
        Public method to reload the login data.
        """
        if not self.__loaded:
            return
        
        self.__loaded = False
        self.__load()
    
    def close(self):
        """
        Public method to close the passwords manager.
        """
        self.__saveTimer.saveIfNeccessary()
    
    def removePassword(self, site):
        """
        Public method to remove a password entry.
        
        @param site web site name (string)
        """
        if site in self.__logins:
            del self.__logins[site]
            if site in self.__loginForms:
                del self.__loginForms[site]
            self.changed.emit()
    
    def allSiteNames(self):
        """
        Public method to get a list of all site names.
        
        @return sorted list of all site names (list of strings)
        """
        if not self.__loaded:
            self.__load()
        
        return sorted(self.__logins.keys())
    
    def sitesCount(self):
        """
        Public method to get the number of available sites.
        
        @return number of sites (integer)
        """
        if not self.__loaded:
            self.__load()
        
        return len(self.__logins)
    
    def siteInfo(self, site):
        """
        Public method to get a reference to the named site.
        
        @param site web site name (string)
        @return tuple containing the user name (string) and password (string)
        """
        if not self.__loaded:
            self.__load()
        
        if site not in self.__logins:
            return None
        
        return self.__logins[site][0], Utilities.crypto.pwConvert(
            self.__logins[site][1], encode=False)
    
    def formSubmitted(self, urlStr, userName, password, data, page):
        """
        Public method to record login data.
        
        @param urlStr form submission URL
        @type str
        @param userName name of the user
        @type str
        @param password user password
        @type str
        @param data data to be submitted
        @type QByteArray
        @param page reference to the calling page
        @type QWebEnginePage
        """
        # shall passwords be saved?
        if not Preferences.getUser("SavePasswords"):
            return
        
        if WebBrowser.WebBrowserWindow.WebBrowserWindow.isPrivate():
            return
        
        if not self.__loaded:
            self.__load()
        
        if urlStr in self.__never:
            return
        
        if userName and password:
            url = QUrl(urlStr)
            url = self.__stripUrl(url)
            key = self.__createKey(url, "")
            if key not in self.__loginForms:
                mb = E5MessageBox.E5MessageBox(
                    E5MessageBox.Question,
                    self.tr("Save password"),
                    self.tr(
                        """<b>Would you like to save this password?</b><br/>"""
                        """To review passwords you have saved and remove"""
                        """ them, use the password management dialog of the"""
                        """ Settings menu."""),
                    modal=True, parent=page.view())
                neverButton = mb.addButton(
                    self.tr("Never for this site"),
                    E5MessageBox.DestructiveRole)
                noButton = mb.addButton(
                    self.tr("Not now"), E5MessageBox.RejectRole)
                mb.addButton(E5MessageBox.Yes)
                mb.exec_()
                if mb.clickedButton() == neverButton:
                    self.__never.append(url.toString())
                    return
                elif mb.clickedButton() == noButton:
                    return
        
            self.__logins[key] = \
                (userName,
                 Utilities.crypto.pwConvert(password, encode=True))
            from .LoginForm import LoginForm
            form = LoginForm()
            form.url = url
            form.name = userName
            form.postData = Utilities.crypto.pwConvert(
                bytes(data).decode("utf-8"), encode=True)
            self.__loginForms[key] = form
            self.changed.emit()
    
    def __stripUrl(self, url):
        """
        Private method to strip off all unneeded parts of a URL.
        
        @param url URL to be stripped (QUrl)
        @return stripped URL (QUrl)
        """
        cleanUrl = QUrl(url)
        cleanUrl.setQuery("")
        cleanUrl.setUserInfo("")
        
        authority = cleanUrl.authority()
        if authority.startswith("@"):
            authority = authority[1:]
        cleanUrl = QUrl("{0}://{1}{2}".format(
            cleanUrl.scheme(), authority, cleanUrl.path()))
        cleanUrl.setFragment("")
        return cleanUrl
    
    def completePage(self, page):
        """
        Public slot to complete login forms with saved data.
        
        @param page reference to the web page (WebBrowserPage)
        """
        if page is None:
            return
        
        if not self.__loaded:
            self.__load()
        
        url = page.url()
        url = self.__stripUrl(url)
        key = self.__createKey(url, "")
        if key not in self.__loginForms or \
           key not in self.__logins:
            return
        
        form = self.__loginForms[key]
        if form.url != url:
            return
        
        postData = QByteArray(Utilities.crypto.pwConvert(
            form.postData, encode=False).encode("utf-8"))
        script = Scripts.completeFormData(postData)
        page.runJavaScript(script, WebBrowserPage.SafeJsWorld)
    
    def masterPasswordChanged(self, oldPassword, newPassword):
        """
        Public slot to handle the change of the master password.
        
        @param oldPassword current master password (string)
        @param newPassword new master password (string)
        """
        if not self.__loaded:
            self.__load()
        
        progress = E5ProgressDialog(
            self.tr("Re-encoding saved passwords..."),
            None, 0, len(self.__logins) + len(self.__loginForms),
            self.tr("%v/%m Passwords"),
            QApplication.activeModalWidget())
        progress.setMinimumDuration(0)
        progress.setWindowTitle(self.tr("Passwords"))
        count = 0
        
        # step 1: do the logins
        for key in self.__logins:
            progress.setValue(count)
            QCoreApplication.processEvents()
            username, pwHash = self.__logins[key]
            pwHash = Utilities.crypto.pwRecode(
                pwHash, oldPassword, newPassword)
            self.__logins[key] = (username, pwHash)
            count += 1
        
        # step 2: do the login forms
        for key in self.__loginForms:
            progress.setValue(count)
            QCoreApplication.processEvents()
            postData = self.__loginForms[key].postData
            postData = Utilities.crypto.pwRecode(
                postData, oldPassword, newPassword)
            self.__loginForms[key].postData = postData
            count += 1
        
        progress.setValue(len(self.__logins) + len(self.__loginForms))
        QCoreApplication.processEvents()
        self.changed.emit()
