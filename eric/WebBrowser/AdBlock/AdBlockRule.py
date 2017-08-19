# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the AdBlock rule class.
"""

from __future__ import unicode_literals

import re

from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInfo

from Globals import qVersionTuple


def toSecondLevelDomain(url):
    """
    Module function to get a second level domain from the given URL.
    
    @param url URL to extract domain from (QUrl)
    @return name of second level domain (string)
    """
    topLevelDomain = url.topLevelDomain()
    urlHost = url.host()
    
    if not topLevelDomain or not urlHost:
        return ""
    
    domain = urlHost[:len(urlHost) - len(topLevelDomain)]
    if domain.count(".") == 0:
        return urlHost
    
    while domain.count(".") != 0:
        domain = domain[domain.find(".") + 1:]
    
    return domain + topLevelDomain


class AdBlockRule(object):
    """
    Class implementing the AdBlock rule.
    """
    def __init__(self, filterRule="", subscription=None):
        """
        Constructor
        
        @param filterRule filter string of the rule (string)
        @param subscription reference to the subscription object
            (AdBlockSubscription)
        """
        self.__subscription = subscription
        
        self.__regExp = QRegExp()
        self.__options = []
        self.__blockedDomains = []
        self.__allowedDomains = []
        
        self.__enabled = True
        self.__cssRule = False
        self.__exception = False
        self.__internalDisabled = False
        self.__domainRestricted = False
        self.__useRegExp = False
        self.__useDomainMatch = False
        self.__useEndsMatch = False
        self.__thirdParty = False
        self.__thirdPartyException = False
        self.__object = False
        self.__objectException = False
        self.__subdocument = False
        self.__subdocumentException = False
        self.__xmlhttprequest = False
        self.__xmlhttprequestException = False
        self.__document = False
        self.__elemhide = False
        self.__caseSensitivity = Qt.CaseInsensitive
        self.__image = False
        self.__imageException = False
        self.__script = False
        self.__scriptException = False
        self.__stylesheet = False
        self.__stylesheetException = False
        self.__objectSubrequest = False
        self.__objectSubrequestException = False
        self.__stringMatchRule = False
        
        self.setFilter(filterRule)
    
    def subscription(self):
        """
        Public method to get the subscription this rule belongs to.
        
        @return subscription of the rule (AdBlockSubscription)
        """
        return self.__subscription
    
    def filter(self):
        """
        Public method to get the rule filter string.
        
        @return rule filter string (string)
        """
        return self.__filter
    
    def setFilter(self, filterRule):
        """
        Public method to set the rule filter string.
        
        @param filterRule rule filter string (string)
        """
        self.__filter = filterRule
        self.__parseFilter()
    
    def __parseFilter(self):
        """
        Private method to parse the filter pattern.
        """
        parsedLine = self.__filter
        
        # empty rule or just a comment
        if not parsedLine.strip() or parsedLine.startswith(("!", "[Adblock")):
            self.__enabled = False
            return
        
        # CSS element hiding rule
        if "##" in parsedLine or "#@#" in parsedLine:
            self.__cssRule = True
            pos = parsedLine.find("#")
            
            # domain restricted rule
            if not parsedLine.startswith("##"):
                domains = parsedLine[:pos]
                self.__parseDomains(domains, ",")
            
            self.__exception = parsedLine[pos + 1] == "@"
            
            if self.__exception:
                self.__cssSelector = parsedLine[pos + 3:]
            else:
                self.__cssSelector = parsedLine[pos + 2:]
            # CSS rule cannot have more options -> stop parsing
            return
        
        # Exception always starts with @@
        if parsedLine.startswith("@@"):
            self.__exception = True
            parsedLine = parsedLine[2:]
        
        # Parse all options following '$' character
        optionsIndex = parsedLine.find("$")
        if optionsIndex >= 0:
            options = parsedLine[optionsIndex + 1:].split(",")
            
            handledOptions = 0
            for option in options:
                if option.startswith("domain="):
                    self.__parseDomains(option[7:], "|")
                    handledOptions += 1
                elif option == "match-case":
                    self.__caseSensitivity = Qt.CaseSensitive
                    handledOptions += 1
                elif option.endswith("third-party"):
                    self.__thirdParty = True
                    self.__thirdPartyException = option.startswith("~")
                    handledOptions += 1
                elif option.endswith("object"):
                    self.__object = True
                    self.__objectException = option.startswith("~")
                    handledOptions += 1
                elif option.endswith("subdocument"):
                    self.__subdocument = True
                    self.__subdocumentException = option.startswith("~")
                    handledOptions += 1
                elif option.endswith("xmlhttprequest"):
                    self.__xmlhttprequest = True
                    self.__xmlhttprequestException = option.startswith("~")
                    handledOptions += 1
                elif option.endswith("image"):
                    self.__image = True
                    self.__imageException = option.startswith("~")
                elif option.endswith("script"):
                    self.__script = True
                    self.__scriptException = option.startswith("~")
                elif option.endswith("stylesheet"):
                    self.__stylesheet = True
                    self.__stylesheetException = option.startswith("~")
                elif option.endswith("object-subrequest"):
                    self.__objectSubrequest = True
                    self.__objectSubrequestException = option.startswith("~")
                elif option == "document" and self.__exception:
                    self.__document = True
                    handledOptions += 1
                elif option == "elemhide" and self.__exception:
                    self.__elemhide = True
                    handledOptions += 1
                elif option == "collapse":
                    # Hiding placeholders of blocked elements
                    handledOptions += 1
            
            # If we don't handle all options, it's safer to just disable
            # this rule
            if handledOptions != len(options):
                self.__internalDisabled = True
                return
            
            parsedLine = parsedLine[:optionsIndex]
        
        # Rule is classic regexp
        if parsedLine.startswith("/") and parsedLine.endswith("/"):
            parsedLine = parsedLine[1:-1]
            self.__useRegExp = True
            self.__regExp = QRegExp(parsedLine, self.__caseSensitivity,
                                    QRegExp.RegExp)
            return
        
        # Remove starting / ending wildcards
        if parsedLine.startswith("*"):
            parsedLine = parsedLine[1:]
        if parsedLine.endswith("*"):
            parsedLine = parsedLine[:-1]
        
        # Fast string matching for domain can be used
        if parsedLine.startswith("||") and \
           parsedLine.endswith("^") and \
           QRegExp("[/:?=&\\*]").indexIn(parsedLine) == -1:
            parsedLine = parsedLine[2:-1]
            self.__useDomainMatch = True
            self.__matchString = parsedLine
            return
        
        # If rule contains '|' only at the end, string matching can be used
        if parsedLine.endswith("|") and \
           QRegExp("[\\^\\*]").indexIn(parsedLine) == -1 and \
           parsedLine.count("|") == 1:
            parsedLine = parsedLine[:-1]
            self.__useEndsMatch = True
            self.__matchString = parsedLine
            return
        
        # If there is still a wildcard (*) or separator (^) or (|),
        # the rule must be modified to comply with QRegExp.
        if "*" in parsedLine or "^" in parsedLine or "|" in parsedLine:
            pattern = self.__convertPatternToRegExp(parsedLine)
            self.__useRegExp = True
            self.__regExp = QRegExp(pattern, self.__caseSensitivity,
                                    QRegExp.RegExp)
            return
        
        # no regexp required
        self.__useRegExp = False
        self.__matchString = parsedLine
        self.__stringMatchRule = True
    
    def __parseDomains(self, domains, separator):
        """
        Private method to parse a string with a domain list.
        
        @param domains list of domains (string)
        @param separator separator character used by the list (string)
        """
        domainsList = domains.split(separator)
        
        for domain in domainsList:
            if not domain:
                continue
            if domain.startswith("~"):
                self.__blockedDomains.append(domain[1:])
            else:
                self.__allowedDomains.append(domain)
        
        self.__domainRestricted = \
            bool(self.__blockedDomains) or bool(self.__allowedDomains)
    
    def networkMatch(self, request, domain, encodedUrl):
        """
        Public method to check the rule for a match.
        
        @param request reference to the network request
        @type QWebEngineUrlRequestInfo
        @param domain domain name
        @type str
        @param encodedUrl string encoded URL to be checked
        @type str
        @return flag indicating a match
        @rtype bool
        """
        if self.__cssRule or not self.__enabled or self.__internalDisabled:
            return False
        
        matched = self.__stringMatch(domain, encodedUrl)
        
        if matched:
            # check domain restrictions
            if self.__domainRestricted and \
                    not self.matchDomain(request.firstPartyUrl().host()):
                return False
            
            # check third-party restrictions
            if self.__thirdParty and not self.matchThirdParty(request):
                return False
            
            # check object restrictions
            if self.__object and not self.matchObject(request):
                return False
            
            # check subdocument restrictions
            if self.__subdocument and not self.matchSubdocument(request):
                return False
            
            # check xmlhttprequest restriction
            if self.__xmlhttprequest and not self.matchXmlHttpRequest(request):
                return False
            
            # check image restriction
            if self.__image and not self.matchImage(request):
                return False
            
            # check script restriction
            if self.__script and not self.matchScript(request):
                return False
            
            # check stylesheet restriction
            if self.__stylesheet and not self.matchStyleSheet(request):
                return False
            
            # check object-subrequest restriction
            if self.__objectSubrequest and \
                    not self.matchObjectSubrequest(request):
                return False
        
        return matched
    
    def urlMatch(self, url):
        """
        Public method to check an URL against the rule.
        
        @param url URL to check (QUrl)
        @return flag indicating a match (boolean)
        """
        if not self.__document and not self.__elemhide:
            return False
        
        encodedUrl = bytes(url.toEncoded()).decode()
        domain = url.host()
        return self.__stringMatch(domain, encodedUrl)
    
    def __stringMatch(self, domain, encodedUrl):
        """
        Private method to match a domain string.
        
        @param domain domain to match
        @type str
        @param encodedUrl URL in encoded form
        @type str
        @return flag indicating a match
        @rtype bool
        """
        if self.__cssRule or not self.__enabled or self.__internalDisabled:
            return False
        
        matched = False
        
        if self.__useRegExp:
            matched = self.__regExp.indexIn(encodedUrl) != -1
        elif self.__useDomainMatch:
            matched = domain.endswith(self.__matchString)
        elif self.__useEndsMatch:
            if self.__caseSensitivity == Qt.CaseInsensitive:
                matched = encodedUrl.lower().endswith(
                    self.__matchString.lower())
            else:
                matched = encodedUrl.endswith(self.__matchString)
        else:
            if self.__caseSensitivity == Qt.CaseInsensitive:
                matched = self.__matchString.lower() in encodedUrl.lower()
            else:
                matched = self.__matchString in encodedUrl
        
        return matched
    
    def matchDomain(self, domain):
        """
        Public method to match a domain.
        
        @param domain domain name to check (string)
        @return flag indicating a match (boolean)
        """
        if not self.__enabled:
            return False
        
        if not self.__domainRestricted:
            return True
        
        if len(self.__blockedDomains) == 0:
            for dom in self.__allowedDomains:
                if domain.endswith(dom):
                    return True
        elif len(self.__allowedDomains) == 0:
            for dom in self.__blockedDomains:
                if domain.endswith(dom):
                    return False
            return True
        else:
            for dom in self.__blockedDomains:
                if domain.endswith(dom):
                    return False
            for dom in self.__allowedDomains:
                if domain.endswith(dom):
                    return True
        
        return False
    
    def matchThirdParty(self, req):
        """
        Public slot to match a third-party rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        # Third-party matching should be performed on second-level domains
        firstPartyHost = toSecondLevelDomain(req.firstPartyUrl())
        host = toSecondLevelDomain(req.requestUrl())
        
        match = firstPartyHost != host
        
        if self.__thirdPartyException:
            return not match
        else:
            return match
    
    def matchObject(self, req):
        """
        Public slot to match an object rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        match = (
            req.resourceType() == QWebEngineUrlRequestInfo.ResourceTypeObject)
        
        if self.__objectException:
            return not match
        else:
            return match
    
    def matchSubdocument(self, req):
        """
        Public slot to match a sub-document rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        match = (
            req.resourceType() ==
            QWebEngineUrlRequestInfo.ResourceTypeSubFrame)
        
        if self.__subdocumentException:
            return not match
        else:
            return match
    
    def matchXmlHttpRequest(self, req):
        """
        Public slot to match a XmlHttpRequest rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        match = (
            req.resourceType() == QWebEngineUrlRequestInfo.ResourceTypeXhr)
        
        if self.__xmlhttprequestException:
            return not match
        else:
            return match
    
    def matchImage(self, req):
        """
        Public slot to match an Image rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        match = (
            req.resourceType() == QWebEngineUrlRequestInfo.ResourceTypeImage)
        
        if self.__imageException:
            return not match
        else:
            return match
    
    def matchScript(self, req):
        """
        Public slot to match a Script rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        match = (
            req.resourceType() == QWebEngineUrlRequestInfo.ResourceTypeScript)
        
        if self.__scriptException:
            return not match
        else:
            return match
    
    def matchStyleSheet(self, req):
        """
        Public slot to match a StyleSheet rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        match = (
            req.resourceType() ==
            QWebEngineUrlRequestInfo.ResourceTypeStylesheet)
        
        if self.__stylesheetException:
            return not match
        else:
            return match
    
    def matchObjectSubrequest(self, req):
        """
        Public slot to match an Object Subrequest rule.
        
        @param req request object to check (QWebEngineUrlRequestInfo)
        @return flag indicating a match (boolean)
        """
        match = (
            req.resourceType() ==
            QWebEngineUrlRequestInfo.ResourceTypeSubResource)
        if qVersionTuple() >= (5, 7, 0):
            match = match or (
                req.resourceType() ==
                QWebEngineUrlRequestInfo.ResourceTypePluginResource)
        
        if self.__objectSubrequestException:
            return not match
        else:
            return match
    
    def isException(self):
        """
        Public method to check, if the rule defines an exception.
        
        @return flag indicating an exception (boolean)
        """
        return self.__exception
    
    def setException(self, exception):
        """
        Public method to set the rule's exception flag.
        
        @param exception flag indicating an exception rule (boolean)
        """
        self.__exception = exception
    
    def isEnabled(self):
        """
        Public method to check, if the rule is enabled.
        
        @return flag indicating enabled state (boolean)
        """
        return self.__enabled
    
    def setEnabled(self, enabled):
        """
        Public method to set the rule's enabled state.
        
        @param enabled flag indicating the new enabled state (boolean)
        """
        self.__enabled = enabled
        if not enabled:
            self.__filter = "!" + self.__filter
        else:
            self.__filter = self.__filter[1:]
    
    def isCSSRule(self):
        """
        Public method to check, if the rule is a CSS rule.
        
        @return flag indicating a CSS rule (boolean)
        """
        return self.__cssRule
    
    def cssSelector(self):
        """
        Public method to get the CSS selector of the rule.
        
        @return CSS selector (string)
        """
        return self.__cssSelector
    
    def isDocument(self):
        """
        Public method to check, if this is a document rule.
        
        @return flag indicating a document rule (boolean)
        """
        return self.__document
    
    def isElementHiding(self):
        """
        Public method to check, if this is an element hiding rule.
        
        @return flag indicating an element hiding rule (boolean)
        """
        return self.__elemhide
    
    def isDomainRestricted(self):
        """
        Public method to check, if this rule is restricted by domain.
        
        @return flag indicating a domain restriction (boolean)
        """
        return self.__domainRestricted
    
    def isComment(self):
        """
        Public method to check, if this is a comment.
        
        @return flag indicating a comment (boolean)
        """
        return self.__filter.startswith("!")
    
    def isHeader(self):
        """
        Public method to check, if this is a header.
        
        @return flag indicating a header (boolean)
        """
        return self.__filter.startswith("[Adblock")
    
    def isSlow(self):
        """
        Public method to check, if this is a slow rule.
        
        @return flag indicating a slow rule (boolean)
        """
        return self.__useRegExp
    
    def isInternalDisabled(self):
        """
        Public method to check, if this rule was disabled internally.
        
        @return flag indicating an internally disabled rule (boolean)
        """
        return self.__internalDisabled
    
    def __convertPatternToRegExp(self, wildcardPattern):
        """
        Private method to convert a wildcard pattern to a regular expression.
        
        @param wildcardPattern string containing the wildcard pattern (string)
        @return string containing a regular expression (string)
        """
        pattern = wildcardPattern
        
        # remove multiple wildcards
        pattern = re.sub(r"\*+", "*", pattern)
        # remove anchors following separator placeholder
        pattern = re.sub(r"\^\|$", "^", pattern)
        # remove leading wildcards
        pattern = re.sub(r"^(\*)", "", pattern)
        # remove trailing wildcards
        pattern = re.sub(r"(\*)$", "", pattern)
        # escape special symbols
        pattern = re.sub(r"(\W)", r"\\\1", pattern)
        # process extended anchor at expression start
        pattern = re.sub(
            r"^\\\|\\\|",
            r"^[\w\-]+:\/+(?!\/)(?:[^\/]+\.)?", pattern)
        # process separator placeholders
        pattern = re.sub(r"\\\^", r"(?:[^\w\d\-.%]|$)", pattern)
        # process anchor at expression start
        pattern = re.sub(r"^\\\|", "^", pattern)
        # process anchor at expression end
        pattern = re.sub(r"\\\|$", "$", pattern)
        # replace wildcards by .*
        pattern = re.sub(r"\\\*", ".*", pattern)
        
        return pattern
