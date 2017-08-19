# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the AdBlock manager.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSignal, QObject, QUrl, QUrlQuery, QFile, \
    QByteArray
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInfo

from E5Gui import E5MessageBox

from .AdBlockSubscription import AdBlockSubscription
from .AdBlockUrlInterceptor import AdBlockUrlInterceptor

from Utilities.AutoSaver import AutoSaver
import Utilities
import Preferences


class AdBlockManager(QObject):
    """
    Class implementing the AdBlock manager.
    
    @signal rulesChanged() emitted after some rule has changed
    @signal requiredSubscriptionLoaded(subscription) emitted to indicate
        loading of a required subscription is finished (AdBlockSubscription)
    """
    rulesChanged = pyqtSignal()
    requiredSubscriptionLoaded = pyqtSignal(AdBlockSubscription)
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object (QObject)
        """
        super(AdBlockManager, self).__init__(parent)
        
        self.__loaded = False
        self.__subscriptionsLoaded = False
        self.__enabled = False
        self.__adBlockDialog = None
        self.__adBlockExceptionsDialog = None
        self.__adBlockNetwork = None
        self.__adBlockPage = None
        self.__subscriptions = []
        self.__exceptedHosts = Preferences.getWebBrowser("AdBlockExceptions")
        self.__saveTimer = AutoSaver(self, self.save)
        self.__limitedEasyList = Preferences.getWebBrowser(
            "AdBlockUseLimitedEasyList")
        
        self.__defaultSubscriptionUrlString = \
            "abp:subscribe?location=" \
            "https://easylist-downloads.adblockplus.org/easylist.txt&"\
            "title=EasyList"
        self.__customSubscriptionUrlString = \
            bytes(self.__customSubscriptionUrl().toEncoded()).decode()
        
        self.rulesChanged.connect(self.__saveTimer.changeOccurred)
        self.rulesChanged.connect(self.__rulesChanged)
        
        self.__interceptor = AdBlockUrlInterceptor(self)
        
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        WebBrowserWindow.networkManager().installUrlInterceptor(
            self.__interceptor)
    
    def __rulesChanged(self):
        """
        Private slot handling a change of the AdBlock rules.
        """
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        WebBrowserWindow.mainWindow().reloadUserStyleSheet()
    
    def close(self):
        """
        Public method to close the open search engines manager.
        """
        self.__adBlockDialog and self.__adBlockDialog.close()
        self.__adBlockExceptionsDialog and \
            self.__adBlockExceptionsDialog.close()
        
        self.__saveTimer.saveIfNeccessary()
    
    def isEnabled(self):
        """
        Public method to check, if blocking ads is enabled.
        
        @return flag indicating the enabled state (boolean)
        """
        if not self.__loaded:
            self.load()
        
        return self.__enabled
    
    def setEnabled(self, enabled):
        """
        Public slot to set the enabled state.
        
        @param enabled flag indicating the enabled state (boolean)
        """
        if self.isEnabled() == enabled:
            return
        
        from WebBrowser.WebBrowserWindow import WebBrowserWindow
        self.__enabled = enabled
        for mainWindow in WebBrowserWindow.mainWindows():
            mainWindow.adBlockIcon().setEnabled(enabled)
        if enabled:
            self.__loadSubscriptions()
        self.rulesChanged.emit()
    
    def block(self, info):
        """
        Public method to check, if a request should be blocked.
        
        @param info request info aobject
        @type QWebEngineUrlRequestInfo
        @return flag indicating to block the request
        @rtype bool
        """
        urlString = bytes(info.requestUrl().toEncoded()).decode().lower()
        urlDomain = info.requestUrl().host().lower()
        urlScheme = info.requestUrl().scheme().lower()
        refererHost = info.firstPartyUrl().host().lower()
        
        if not self.isEnabled() or not self.__canRunOnScheme(urlScheme):
            return False
        
        if self.isHostExcepted(urlDomain) or self.isHostExcepted(refererHost):
            return False
            
        res = False
        
        for subscription in self.subscriptions():
            if subscription.isEnabled():
                if subscription.adBlockDisabledForUrl(info.requestUrl()):
                    continue
                
                blockedRule = subscription.match(info, urlDomain, urlString)
                if blockedRule:
                    res = True
                    if info.resourceType() == \
                            QWebEngineUrlRequestInfo.ResourceTypeMainFrame:
                        url = QUrl("eric:adblock")
                        query = QUrlQuery()
                        query.addQueryItem("rule", blockedRule.filter())
                        query.addQueryItem(
                            "subscription", blockedRule.subscription().title())
                        url.setQuery(query)
                        info.redirect(url)
                        res = False
                    else:
                        info.block(True)
                    break
        
        return res
    
    def __canRunOnScheme(self, scheme):
        """
        Private method to check, if AdBlock can be performed on the scheme.
        
        @param scheme scheme to check (string)
        @return flag indicating, that AdBlock can be performed (boolean)
        """
        return scheme not in ["data", "eric", "qthelp", "qrc", "file", "abp"]
    
    def page(self):
        """
        Public method to get a reference to the page block object.
        
        @return reference to the page block object (AdBlockPage)
        """
        if self.__adBlockPage is None:
            from .AdBlockPage import AdBlockPage
            self.__adBlockPage = AdBlockPage(self)
        return self.__adBlockPage
    
    def __customSubscriptionLocation(self):
        """
        Private method to generate the path for custom subscriptions.
        
        @return URL for custom subscriptions (QUrl)
        """
        dataDir = os.path.join(Utilities.getConfigDir(), "web_browser",
                               "subscriptions")
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)
        fileName = os.path.join(dataDir, "adblock_subscription_custom")
        return QUrl.fromLocalFile(fileName)
    
    def __customSubscriptionUrl(self):
        """
        Private method to generate the URL for custom subscriptions.
        
        @return URL for custom subscriptions (QUrl)
        """
        location = self.__customSubscriptionLocation()
        encodedUrl = bytes(location.toEncoded()).decode()
        url = QUrl("abp:subscribe?location={0}&title={1}".format(
            encodedUrl, self.tr("Custom Rules")))
        return url
    
    def customRules(self):
        """
        Public method to get a subscription for custom rules.
        
        @return subscription object for custom rules (AdBlockSubscription)
        """
        location = self.__customSubscriptionLocation()
        for subscription in self.__subscriptions:
            if subscription.location() == location:
                return subscription
        
        url = self.__customSubscriptionUrl()
        customAdBlockSubscription = AdBlockSubscription(url, True, self)
        self.addSubscription(customAdBlockSubscription)
        return customAdBlockSubscription
    
    def subscriptions(self):
        """
        Public method to get all subscriptions.
        
        @return list of subscriptions (list of AdBlockSubscription)
        """
        if not self.__loaded:
            self.load()
        
        return self.__subscriptions[:]
    
    def subscription(self, location):
        """
        Public method to get a subscription based on its location.
        
        @param location location of the subscription to search for (string)
        @return subscription or None (AdBlockSubscription)
        """
        if location != "":
            for subscription in self.__subscriptions:
                if subscription.location().toString() == location:
                    return subscription
        
        return None
    
    def updateAllSubscriptions(self):
        """
        Public method to update all subscriptions.
        """
        for subscription in self.__subscriptions:
            subscription.updateNow()
    
    def removeSubscription(self, subscription, emitSignal=True):
        """
        Public method to remove an AdBlock subscription.
        
        @param subscription AdBlock subscription to be removed
            (AdBlockSubscription)
        @param emitSignal flag indicating to send a signal (boolean)
        """
        if subscription is None:
            return
        
        if subscription.url().toString().startswith(
            (self.__defaultSubscriptionUrlString,
             self.__customSubscriptionUrlString)):
            return
        
        try:
            self.__subscriptions.remove(subscription)
            rulesFileName = subscription.rulesFileName()
            QFile.remove(rulesFileName)
            requiresSubscriptions = self.getRequiresSubscriptions(subscription)
            for requiresSubscription in requiresSubscriptions:
                self.removeSubscription(requiresSubscription, False)
            if emitSignal:
                self.rulesChanged.emit()
        except ValueError:
            pass
    
    def addSubscriptionFromUrl(self, url):
        """
        Public method to ad an AdBlock subscription given the abp URL.
        
        @param url URL to subscribe an AdBlock subscription
        @type QUrl
        @return flag indicating success
        @rtype bool
        """
        if url.path() != "subscribe":
            return False
        
        title = QUrl.fromPercentEncoding(
            QByteArray(QUrlQuery(url).queryItemValue("title").encode()))
        if not title:
            return False
        
        res = E5MessageBox.yesNo(
            None,
            self.tr("Subscribe?"),
            self.tr(
                """<p>Subscribe to this AdBlock subscription?</p>"""
                """<p>{0}</p>""").format(title))
        if res:
            from .AdBlockSubscription import AdBlockSubscription
            from WebBrowser.WebBrowserWindow import WebBrowserWindow
            
            dlg = WebBrowserWindow.adBlockManager().showDialog()
            subscription = AdBlockSubscription(
                url, False,
                WebBrowserWindow.adBlockManager())
            WebBrowserWindow.adBlockManager().addSubscription(subscription)
            dlg.addSubscription(subscription, False)
            dlg.setFocus()
            dlg.raise_()
    
    def addSubscription(self, subscription):
        """
        Public method to add an AdBlock subscription.
        
        @param subscription AdBlock subscription to be added
            (AdBlockSubscription)
        """
        if subscription is None:
            return
        
        self.__subscriptions.insert(-1, subscription)
        
        subscription.rulesChanged.connect(self.rulesChanged)
        subscription.changed.connect(self.rulesChanged)
        subscription.enabledChanged.connect(self.rulesChanged)
        
        self.rulesChanged.emit()
    
    def save(self):
        """
        Public method to save the AdBlock subscriptions.
        """
        if not self.__loaded:
            return
        
        Preferences.setWebBrowser("AdBlockEnabled", self.__enabled)
        if self.__subscriptionsLoaded:
            subscriptions = []
            requiresSubscriptions = []
            # intermediate store for subscription requiring others
            for subscription in self.__subscriptions:
                if subscription is None:
                    continue
                urlString = bytes(subscription.url().toEncoded()).decode()
                if "requiresLocation" in urlString:
                    requiresSubscriptions.append(urlString)
                else:
                    subscriptions.append(urlString)
                subscription.saveRules()
            for subscription in requiresSubscriptions:
                subscriptions.insert(-1, subscription)  # custom should be last
            Preferences.setWebBrowser("AdBlockSubscriptions", subscriptions)
    
    def load(self):
        """
        Public method to load the AdBlock subscriptions.
        """
        if self.__loaded:
            return
        
        self.__loaded = True
        
        self.__enabled = Preferences.getWebBrowser("AdBlockEnabled")
        if self.__enabled:
            self.__loadSubscriptions()
    
    def __loadSubscriptions(self):
        """
        Private method to load the set of subscriptions.
        """
        if self.__subscriptionsLoaded:
            return
        
        subscriptions = Preferences.getWebBrowser("AdBlockSubscriptions")
        if subscriptions:
            for subscription in subscriptions:
                if subscription.startswith(
                        self.__defaultSubscriptionUrlString):
                    break
            else:
                subscriptions.insert(0, self.__defaultSubscriptionUrlString)
            for subscription in subscriptions:
                if subscription.startswith(self.__customSubscriptionUrlString):
                    break
            else:
                subscriptions.append(self.__customSubscriptionUrlString)
        else:
            subscriptions = [self.__defaultSubscriptionUrlString,
                             self.__customSubscriptionUrlString]
        for subscription in subscriptions:
            url = QUrl.fromEncoded(subscription.encode("utf-8"))
            adBlockSubscription = AdBlockSubscription(
                url,
                subscription.startswith(self.__customSubscriptionUrlString),
                self,
                subscription.startswith(self.__defaultSubscriptionUrlString))
            adBlockSubscription.rulesChanged.connect(self.rulesChanged)
            adBlockSubscription.changed.connect(self.rulesChanged)
            adBlockSubscription.enabledChanged.connect(self.rulesChanged)
            self.__subscriptions.append(adBlockSubscription)
        
        self.__subscriptionsLoaded = True
    
    def loadRequiredSubscription(self, location, title):
        """
        Public method to load a subscription required by another one.
        
        @param location location of the required subscription (string)
        @param title title of the required subscription (string)
        """
        # Step 1: check, if the subscription is in the list of subscriptions
        urlString = "abp:subscribe?location={0}&title={1}".format(
            location, title)
        for subscription in self.__subscriptions:
            if subscription.url().toString().startswith(urlString):
                # We found it!
                return
        
        # Step 2: if it is not, get it
        url = QUrl.fromEncoded(urlString.encode("utf-8"))
        adBlockSubscription = AdBlockSubscription(url, False, self)
        self.addSubscription(adBlockSubscription)
        self.requiredSubscriptionLoaded.emit(adBlockSubscription)
    
    def getRequiresSubscriptions(self, subscription):
        """
        Public method to get a list of subscriptions, that require the given
        one.
        
        @param subscription subscription to check for (AdBlockSubscription)
        @return list of subscription requiring the given one (list of
            AdBlockSubscription)
        """
        subscriptions = []
        location = subscription.location().toString()
        for subscription in self.__subscriptions:
            if subscription.requiresLocation() == location:
                subscriptions.append(subscription)
        
        return subscriptions
    
    def showDialog(self):
        """
        Public slot to show the AdBlock subscription management dialog.
        
        @return reference to the dialog (AdBlockDialog)
        """
        if self.__adBlockDialog is None:
            from .AdBlockDialog import AdBlockDialog
            self.__adBlockDialog = AdBlockDialog(self)
        
        self.__adBlockDialog.show()
        return self.__adBlockDialog
    
    def elementHidingRules(self, url):
        """
        Public method to get the element hiding rules.
        
        
        @param url URL to get hiding rules for (QUrl)
        @return element hiding rules (string)
        """
        if not self.isEnabled() or not self.__canRunOnScheme(url.scheme()):
            return ""
        
        rules = ""
        
        for subscription in self.__subscriptions:
            rules += subscription.elementHidingRules()
        
        if rules:
            # remove last ",
            rules = rules[:-1]
        
        return rules
    
    def elementHidingRulesForDomain(self, url):
        """
        Public method to get the element hiding rules for a domain.
        
        @param url URL to get hiding rules for (QUrl)
        @return element hiding rules (string)
        """
        if not self.isEnabled():
            return ""
        
        rules = ""
        
        for subscription in self.__subscriptions:
            if subscription.elemHideDisabledForUrl(url):
                continue
            
            rules += subscription.elementHidingRulesForDomain(url.host())
        
        if rules:
            # remove last ","
            rules = rules[:-1]
        
        rules += "{display:none !important;}\n"
        
        return rules
    
    def exceptions(self):
        """
        Public method to get a list of excepted hosts.
        
        @return list of excepted hosts (list of string)
        """
        return self.__exceptedHosts
    
    def setExceptions(self, hosts):
        """
        Public method to set the list of excepted hosts.
        
        @param hosts list of excepted hosts (list of string)
        """
        self.__exceptedHosts = [host.lower() for host in hosts]
        Preferences.setWebBrowser("AdBlockExceptions", self.__exceptedHosts)
    
    def addException(self, host):
        """
        Public method to add an exception.
        
        @param host to be excepted (string)
        """
        host = host.lower()
        if host and host not in self.__exceptedHosts:
            self.__exceptedHosts.append(host)
            Preferences.setWebBrowser(
                "AdBlockExceptions", self.__exceptedHosts)
    
    def removeException(self, host):
        """
        Public method to remove an exception.
        
        @param host to be removed from the list of exceptions (string)
        """
        host = host.lower()
        if host in self.__exceptedHosts:
            self.__exceptedHosts.remove(host)
            Preferences.setWebBrowser(
                "AdBlockExceptions", self.__exceptedHosts)
    
    def isHostExcepted(self, host):
        """
        Public slot to check, if a host is excepted.
        
        @param host host to check (string)
        @return flag indicating an exception (boolean)
        """
        host = host.lower()
        return host in self.__exceptedHosts
    
    def showExceptionsDialog(self):
        """
        Public method to show the AdBlock Exceptions dialog.
        
        @return reference to the exceptions dialog (AdBlockExceptionsDialog)
        """
        if self.__adBlockExceptionsDialog is None:
            from .AdBlockExceptionsDialog import AdBlockExceptionsDialog
            self.__adBlockExceptionsDialog = AdBlockExceptionsDialog()
        
        self.__adBlockExceptionsDialog.load(self.__exceptedHosts)
        self.__adBlockExceptionsDialog.show()
        return self.__adBlockExceptionsDialog
    
    def useLimitedEasyList(self):
        """
        Public method to test, if limited EasyList rules shall be used.
        
        @return flag indicating limited EasyList rules
        @rtype bool
        """
        return self.__limitedEasyList
    
    def setUseLimitedEasyList(self, limited):
        """
        Public method to set the limited EasyList flag.
        
        @param limited flag indicating to use limited EasyList
        @type bool
        """
        self.__limitedEasyList = limited
        
        for subscription in self.__subscriptions:
            if subscription.url().toString().startswith(
                    self.__defaultSubscriptionUrlString):
                subscription.updateNow()
        
        Preferences.setWebBrowser("AdBlockUseLimitedEasyList", limited)
    
    def getDefaultSubscriptionUrl(self):
        """
        Public method to get the default subscription URL.
        
        @return default subscription URL
        @rtype str
        """
        return self.__defaultSubscriptionUrlString
