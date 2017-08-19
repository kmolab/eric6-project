# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a QNetworkCookieJar subclass with various accept policies.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QSettings
from PyQt5.QtNetwork import QNetworkCookieJar, QNetworkCookie

from WebBrowser.WebBrowserWindow import WebBrowserWindow

from Utilities.AutoSaver import AutoSaver
import Utilities
import Preferences


class CookieJar(QNetworkCookieJar):
    """
    Class implementing a QNetworkCookieJar subclass with various accept
    policies.
    
    @signal cookiesChanged() emitted after the cookies have been changed
    """
    cookiesChanged = pyqtSignal()
    
    AcceptAlways = 0
    AcceptNever = 1
    AcceptOnlyFromSitesNavigatedTo = 2
    AcceptMax = 2

    KeepUntilExpire = 0
    KeepUntilExit = 1
    KeepMax = 1
    
    Allow = 0
    Block = 1
    AllowForSession = 2
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(CookieJar, self).__init__(parent)
        
        self.__loaded = False
        self.__acceptCookies = self.AcceptOnlyFromSitesNavigatedTo
        self.__saveTimer = AutoSaver(self, self.__save)
        
        self.__cookiesFile = os.path.join(Utilities.getConfigDir(),
                                          "web_browser", "cookies.ini")
        
        self.__store = WebBrowserWindow.webProfile().cookieStore()
        self.__store.cookieAdded.connect(self.__cookieAdded)
        self.__store.cookieRemoved.connect(self.__cookieRemoved)
        
        self.__load()
        self.__store.loadAllCookies()
    
    def close(self):
        """
        Public slot to close the cookie jar.
        """
        if not self.__loaded:
            self.__load()
        
        if self.__keepCookies == self.KeepUntilExit:
            self.clear()
        self.__saveTimer.saveIfNeccessary()
    
    def clear(self):
        """
        Public method to clear all cookies.
        """
        if not self.__loaded:
            self.__load()
        
        self.setAllCookies([])
        self.__store.deleteAllCookies()
        self.cookiesChanged.emit()
    
    def removeCookies(self, cookies):
        """
        Public method to remove a list of cookies.
        
        @param cookies list of cookies to be removed
        @type list of QNetworkCookie
        """
        wasBlocked = self.blockSignals(True)
        for cookie in cookies:
            self.__store.deleteCookie(cookie)
        self.blockSignals(wasBlocked)
        
        self.cookiesChanged.emit()
    
    def removeCookie(self, cookie):
        """
        Public method to remove a cookie.
        
        @param cookie cookie to be removed
        @type QNetworkCookie
        """
        self.__store.deleteCookie(cookie)
        self.cookiesChanged.emit()
    
    def __load(self):
        """
        Private method to load the cookies settings.
        """
        if self.__loaded:
            return
        
        cookieSettings = QSettings(self.__cookiesFile, QSettings.IniFormat)
        
        # load exceptions
        self.__exceptionsBlock = Preferences.toList(
            cookieSettings.value("Exceptions/block"))
        self.__exceptionsAllow = Preferences.toList(
            cookieSettings.value("Exceptions/allow"))
        self.__exceptionsAllowForSession = Preferences.toList(
            cookieSettings.value("Exceptions/allowForSession"))
        self.__exceptionsBlock.sort()
        self.__exceptionsAllow.sort()
        self.__exceptionsAllowForSession.sort()
        
        self.__acceptCookies = Preferences.getWebBrowser("AcceptCookies")
        self.__keepCookies = Preferences.getWebBrowser("KeepCookiesUntil")
        if self.__keepCookies == self.KeepUntilExit:
            self.clear()
        
        self.__filterTrackingCookies = Preferences.toBool(
            Preferences.getWebBrowser("FilterTrackingCookies"))
        
        self.__loaded = True
        self.cookiesChanged.emit()
    
    def __save(self):
        """
        Private method to save the cookies settings.
        """
        if not self.__loaded:
            return
        
        cookieSettings = QSettings(self.__cookiesFile, QSettings.IniFormat)
        
        cookieSettings.setValue("Exceptions/block", self.__exceptionsBlock)
        cookieSettings.setValue("Exceptions/allow", self.__exceptionsAllow)
        cookieSettings.setValue("Exceptions/allowForSession",
                                self.__exceptionsAllowForSession)
        
        Preferences.setWebBrowser("AcceptCookies", self.__acceptCookies)
        Preferences.setWebBrowser("KeepCookiesUntil", self.__keepCookies)
        Preferences.setWebBrowser("FilterTrackingCookies",
                                  self.__filterTrackingCookies)
    
    @pyqtSlot(QNetworkCookie)
    def __cookieAdded(self, cookie):
        """
        Private slot handling the addition of a cookie.
        
        @param cookie cookie which was added
        @type QNetworkCookie
        """
        if self.__rejectCookie(cookie, cookie.domain()):
            self.__store.deleteCookie(cookie)
            return
        
        self.insertCookie(cookie)
        self.cookiesChanged.emit()
    
    @pyqtSlot(QNetworkCookie)
    def __cookieRemoved(self, cookie):
        """
        Private slot handling the removal of a cookie.
        
        @param cookie cookie which was removed
        @type QNetworkCookie
        """
        if self.deleteCookie(cookie):
            self.cookiesChanged.emit()
    
    def __rejectCookie(self, cookie, cookieDomain):
        """
        Private method to test, if a cookie shall be rejected.
        
        @param cookie cookie to be tested
        @type QNetworkCookie
        @param cookieDomain domain of the cookie
        @type str
        @return flag indicating the cookie shall be rejected
        @rtype bool
        """
        if not self.__loaded:
            self.__load()
        
        if self.__acceptCookies == self.AcceptNever:
            res = self.__isOnDomainList(self.__exceptionsAllow, cookieDomain)
            if not res:
                return True
        
        if self.__acceptCookies == self.AcceptAlways:
            res = self.__isOnDomainList(self.__exceptionsBlock, cookieDomain)
            if res:
                return True
        
        if self.__acceptCookies == self.AcceptOnlyFromSitesNavigatedTo:
            mainWindow = WebBrowserWindow.mainWindow()
            if mainWindow is not None:
                browser = mainWindow.getWindow().currentBrowser()
                if browser is not None:
                    url = browser.url()
                    if url.isValid():
                        host = url.host()
                    else:
                        host = ""
                    res = self.__matchDomain(cookieDomain, host)
                    if not res:
                        return True
        
        if self.__filterTrackingCookies and cookie.name().startsWith(b"__utm"):
            return True
        
        return False
    
    def acceptPolicy(self):
        """
        Public method to get the accept policy.
        
        @return current accept policy
        """
        if not self.__loaded:
            self.__load()
        
        return self.__acceptCookies
    
    def setAcceptPolicy(self, policy):
        """
        Public method to set the accept policy.
        
        @param policy accept policy to be set
        """
        if not self.__loaded:
            self.__load()
        
        if policy > self.AcceptMax:
            return
        if policy == self.__acceptCookies:
            return
        
        self.__acceptCookies = policy
        self.__saveTimer.changeOccurred()
    
    def keepPolicy(self):
        """
        Public method to get the keep policy.
        
        @return keep policy
        """
        if not self.__loaded:
            self.__load()
        
        return self.__keepCookies
    
    def setKeepPolicy(self, policy):
        """
        Public method to set the keep policy.
        
        @param policy keep policy to be set
        """
        if not self.__loaded:
            self.__load()
        
        if policy > self.KeepMax:
            return
        if policy == self.__keepCookies:
            return
        
        self.__keepCookies = policy
        self.__saveTimer.changeOccurred()
    
    def blockedCookies(self):
        """
        Public method to return the list of blocked domains.
        
        @return list of blocked domains (list of strings)
        """
        if not self.__loaded:
            self.__load()
        
        return self.__exceptionsBlock
    
    def allowedCookies(self):
        """
        Public method to return the list of allowed domains.
        
        @return list of allowed domains (list of strings)
        """
        if not self.__loaded:
            self.__load()
        
        return self.__exceptionsAllow
    
    def allowForSessionCookies(self):
        """
        Public method to return the list of allowed session cookie domains.
        
        @return list of allowed session cookie domains (list of strings)
        """
        if not self.__loaded:
            self.__load()
        
        return self.__exceptionsAllowForSession
    
    def setBlockedCookies(self, list_):
        """
        Public method to set the list of blocked domains.
        
        @param list_ list of blocked domains (list of strings)
        """
        if not self.__loaded:
            self.__load()
        
        self.__exceptionsBlock = list_[:]
        self.__exceptionsBlock.sort()
        self.__saveTimer.changeOccurred()
    
    def setAllowedCookies(self, list_):
        """
        Public method to set the list of allowed domains.
        
        @param list_ list of allowed domains (list of strings)
        """
        if not self.__loaded:
            self.__load()
        
        self.__exceptionsAllow = list_[:]
        self.__exceptionsAllow.sort()
        self.__saveTimer.changeOccurred()
    
    def setAllowForSessionCookies(self, list_):
        """
        Public method to set the list of allowed session cookie domains.
        
        @param list_ list of allowed session cookie domains (list of strings)
        """
        if not self.__loaded:
            self.__load()
        
        self.__exceptionsAllowForSession = list_[:]
        self.__exceptionsAllowForSession.sort()
        self.__saveTimer.changeOccurred()
    
    def filterTrackingCookies(self):
        """
        Public method to get the filter tracking cookies flag.
        
        @return filter tracking cookies flag (boolean)
        """
        return self.__filterTrackingCookies
    
    def setFilterTrackingCookies(self, filterTrackingCookies):
        """
        Public method to set the filter tracking cookies flag.
        
        @param filterTrackingCookies filter tracking cookies flag (boolean)
        """
        if filterTrackingCookies == self.__filterTrackingCookies:
            return
        
        self.__filterTrackingCookies = filterTrackingCookies
        self.__saveTimer.changeOccurred()
    
    def __isOnDomainList(self, rules, domain):
        """
        Private method to check, if either the rule matches the domain exactly
        or the domain ends with ".rule".
        
        @param rules list of rules (list of strings)
        @param domain domain name to check (string)
        @return flag indicating a match (boolean)
        """
        for rule in rules:
            if rule.startswith("."):
                if domain.endswith(rule):
                    return True
                
                withoutDot = rule[1:]
                if domain == withoutDot:
                    return True
            else:
                domainEnding = domain[-(len(rule) + 1):]
                if domainEnding and \
                   domainEnding[0] == "." and \
                   domain.endswith(rule):
                    return True
                
                if rule == domain:
                    return True
        
        return False
    
    def __matchDomain(self, cookieDomain, siteDomain):
        """
        Private method to check, if a URLs host matches a cookie domain
        according to RFC 6265.
        
        @param cookieDomain domain of the cookie
        @type str
        @param siteDomain domain or host of an URL
        @type str
        @return flag indicating a match
        @rtype bool
        """
        if not siteDomain:
            # empty URLs always match
            return True
        
        if cookieDomain.startswith("."):
            cookieDomain = cookieDomain[1:]
        if siteDomain.startswith("."):
            siteDomain = siteDomain[1:]
        
        if cookieDomain == siteDomain:
            return True
        
        if not siteDomain.endswith(cookieDomain):
            return False
        
        index = siteDomain.find(cookieDomain)
        return index > 0 and siteDomain[index - 1] == "."
    
    def cookies(self):
        """
        Public method to get the cookies of the cookie jar.
        
        @return list of all cookies (list of QNetworkCookie)
        """
        if not self.__loaded:
            self.__load()
        
        return self.allCookies()
    
    def cookieDomains(self):
        """
        Public method to get a list of all domains used by the cookies.
        
        @return list of domain names
        @rtype list of str
        """
        domains = []
        for cookie in self.cookies():
            domain = cookie.domain()
            if domain not in domains:
                domains.append(domain)
        
        return domains
