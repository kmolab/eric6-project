# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the TLD Extractor.
"""

#
# This is a Python port of the TLDExtractor of Qupzilla
# Copyright (C) 2014  Razi Alavizadeh <s.r.alavizadeh@gmail.com>
#

from __future__ import unicode_literals

import collections

from PyQt5.QtCore import QObject, QUrl, QFile, QFileInfo, QRegExp, qWarning

from E5Gui import E5MessageBox

from .data import tld_rc          # __IGNORE_WARNING__


class E5TldHostParts(object):
    """
    Class implementing the host parts helper.
    """
    def __init__(self):
        """
        Constructor
        """
        self.host = ""
        self.tld = ""
        self.domain = ""
        self.registrableDomain = ""
        self.subdomain = ""


class E5TldExtractor(QObject):
    """
    Class implementing the TLD Extractor.
    
    Note: The module function instance() should be used to get a reference
    to a global object to avoid overhead.
    """
    def __init__(self, withPrivate=False, parent=None):
        """
        Constructor
        
        @param withPrivate flag indicating to load private TLDs as well
        @type bool
        @param parent reference to the parent object
        @type QObject
        """
        super(E5TldExtractor, self).__init__(parent)
        
        self.__withPrivate = withPrivate
        self.__dataFileName = ""
        self.__dataSearchPaths = []
        
        self.__tldDict = collections.defaultdict(list)
        # dict with list of str as values
        
        self.setDataSearchPaths()
    
    def isDataLoaded(self):
        """
        Public method to check, if the TLD data ia already loaded.
        
        @return flag indicating data is loaded
        @rtype bool
        """
        return bool(self.__tldDict)
    
    def tld(self, host):
        """
        Public method to get the top level domain for a host.
        
        @param host host name to get TLD for
        @type str
        @return TLD for host
        @rtype str
        """
        if not host or host.startswith("."):
            return ""
        
        cleanHost = self.__normalizedHost(host)
        
        tldPart = cleanHost[cleanHost.rfind(".") + 1:]
        cleanHost = bytes(QUrl.toAce(cleanHost)).decode("utf-8")
        
        self.__loadData()
        
        if tldPart not in self.__tldDict:
            return tldPart
        
        tldRules = self.__tldDict[tldPart][:]
        
        if tldPart not in tldRules:
            tldRules.append(tldPart)
        
        maxLabelCount = 0
        isWildcardTLD = False
        
        for rule in tldRules:
            labelCount = rule.count(".") + 1
            
            if rule.startswith("!"):
                rule = rule[1:]
                
                rule = bytes(QUrl.toAce(rule)).decode("utf-8")
                
                # matches with exception TLD
                if cleanHost.endswith(rule):
                    tldPart = rule[rule.find(".") + 1:]
                    break
            
            if rule.startswith("*"):
                rule = rule[1:]
                
                if rule.startswith("."):
                    rule = rule[1:]
                
                isWildcardTLD = True
            else:
                isWildcardTLD = False
            
            rule = bytes(QUrl.toAce(rule)).decode("utf-8")
            testRule = "." + rule
            testUrl = "." + cleanHost
            
            if labelCount > maxLabelCount and testUrl.endswith(testRule):
                tldPart = rule
                maxLabelCount = labelCount
                
                if isWildcardTLD:
                    temp = cleanHost
                    temp = temp[:temp.rfind(tldPart)]
                    
                    if temp.endswith("."):
                        temp = temp[:-1]
                    
                    temp = temp[temp.rfind(".") + 1:]
                    
                    if temp:
                        tldPart = temp + "." + rule
                    else:
                        tldPart = rule
        
        temp = self.__normalizedHost(host)
        tldPart = ".".join(
            temp.split(".")[temp.count(".") - tldPart.count("."):])
        
        return tldPart
    
    def domain(self, host):
        """
        Public method to get the domain for a host.
        
        @param host host name to get the domain for
        @type str
        @return domain for host
        @rtype str
        """
        tldPart = self.tld(host)
        
        return self.__domainHelper(host, tldPart)
    
    def registrableDomain(self, host):
        """
        Public method to get the registrable domain for a host.
        
        @param host host name to get the registrable domain for
        @type str
        @return registrable domain for host
        @rtype str
        """
        tldPart = self.tld(host)
        
        return self.__registrableDomainHelper(
            self.__domainHelper(host, tldPart), tldPart)
    
    def subdomain(self, host):
        """
        Public method to get the subdomain for a host.
        
        @param host host name to get the subdomain for
        @type str
        @return subdomain for host
        @rtype str
        """
        return self.__subdomainHelper(host, self.registrableDomain(host))
    
    def splitParts(self, host):
        """
        Public method to split a host address into its parts.
        
        @param host host address to be split
        @type str
        @return splitted host address
        @rtype E5TldHostParts
        """
        hostParts = E5TldHostParts()
        hostParts.host = host
        hostParts.tld = self.tld(host)
        hostParts.domain = self.__domainHelper(host, hostParts.tld)
        hostParts.registrableDomain = self.__registrableDomainHelper(
            hostParts.domain, hostParts.tld)
        hostParts.subdomain = self.__subdomainHelper(
            host, hostParts.registrableDomain)
        
        return hostParts
    
    def dataSearchPaths(self):
        """
        Public method to get the search paths for the TLD data file.
        
        @return search paths for the TLD data file
        @rtype list of str
        """
        return self.__dataSearchPaths[:]
    
    def setDataSearchPaths(self, searchPaths=None):
        """
        Public method to set the search paths for the TLD data file.
        
        @param searchPaths search paths for the TLD data file or None,
            if the default search paths shall be set
        @type list of str
        """
        if searchPaths:
            self.__dataSearchPaths = searchPaths[:]
            self.__dataSearchPaths.extend(self.__defaultDataSearchPaths())
        else:
            self.__dataSearchPaths = self.__defaultDataSearchPaths()[:]
        
        # remove duplicates
        paths = []
        for p in self.__dataSearchPaths:
            if p not in paths:
                paths.append(p)
        self.__dataSearchPaths = paths
    
    def __defaultDataSearchPaths(self):
        """
        Private method to get the default search paths for the TLD data file.
        
        @return default search paths for the TLD data file
        @rtype list of str
        """
        return [":"]
    
    def getTldDownloadUrl(self):
        """
        Public method to get the TLD data file download URL.
        
        @return download URL
        @rtype QUrl
        """
        return QUrl(
            "http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/"
            "effective_tld_names.dat?raw=1")
    
    def __loadData(self):
        """
        Private method to load the TLD data.
        """
        if self.isDataLoaded():
            return
        
        dataFileName = ""
        parsedDataFileExist = False
        
        for path in self.__dataSearchPaths:
            dataFileName = QFileInfo(path + "/effective_tld_names.dat")\
                .absoluteFilePath()
            if QFileInfo(dataFileName).exists():
                parsedDataFileExist = True
                break
        
        if not parsedDataFileExist:
            tldDataFileDownloadLink = \
                "http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/" \
                "effective_tld_names.dat?raw=1"
            E5MessageBox.information(
                None,
                self.tr("TLD Data File not found"),
                self.tr("""<p>The file 'effective_tld_names.dat' was not"""
                        """ found!<br/>You can download it from """
                        """'<a href="{0}"><b>here</b></a>' to one of the"""
                        """ following paths:</p><ul>{1}</ul>""").format(
                    tldDataFileDownloadLink,
                    "".join(["<li>{0}</li>".format(p)
                             for p in self.__dataSearchPaths]))
            )
            return
        
        self.__dataFileName = dataFileName
        if not self.__parseData(dataFileName,
                                loadPrivateDomains=self.__withPrivate):
            qWarning(
                "E5TldExtractor: There are some parse errors for file: {0}"
                .format(dataFileName))
    
    def __parseData(self, dataFile, loadPrivateDomains=False):
        """
        Private method to parse TLD data.
        
        @param dataFile name of the file containing the TLD data
        @type str
        @param loadPrivateDomains flag indicating to load private domains
        @type bool
        @return flag indicating success
        @rtype bool
        """
        # start with a fresh dictionary
        self.__tldDict = collections.defaultdict(list)
        
        file = QFile(dataFile)
        
        if not file.open(QFile.ReadOnly | QFile.Text):
            return False
        
        seekToEndOfPrivateDomains = False
        
        while not file.atEnd():
            line = bytes(file.readLine()).decode("utf-8").strip()
            if not line:
                continue
            
            if line.startswith("."):
                line = line[1:]
            
            if line.startswith("//"):
                if "===END PRIVATE DOMAINS===" in line:
                    seekToEndOfPrivateDomains = False
                
                if not loadPrivateDomains and \
                        "===BEGIN PRIVATE DOMAINS===" in line:
                    seekToEndOfPrivateDomains = True
                
                continue
            
            if seekToEndOfPrivateDomains:
                continue
            
            # only data up to the first whitespace is used
            line = line.split(None, 1)[0]
            
            if "." not in line:
                self.__tldDict[line].append(line)
            else:
                key = line[line.rfind(".") + 1:]
                self.__tldDict[key].append(line)
        
        return self.isDataLoaded()
    
    def __domainHelper(self, host, tldPart):
        """
        Private method to get the domain name without TLD.
        
        @param host host address
        @type str
        @param tldPart TLD part of the host address
        @type str
        @return domain name
        @rtype str
        """
        if not host or not tldPart:
            return ""
        
        temp = self.__normalizedHost(host)
        temp = temp[:temp.rfind(tldPart)]
        
        if temp.endswith("."):
            temp = temp[:-1]
        
        return temp[temp.rfind(".") + 1:]
    
    def __registrableDomainHelper(self, domainPart, tldPart):
        """
        Private method to get the registrable domain (i.e. domain plus TLD).
        
        @param domainPart domain part of a host address
        @type str
        @param tldPart TLD part of a host address
        @type str
        @return registrable domain name
        @rtype str
        """
        if not tldPart or not domainPart:
            return ""
        else:
            return "{0}.{1}".format(domainPart, tldPart)
    
    def __subdomainHelper(self, host, registrablePart):
        """
        Private method to get the subdomain of a host address (i.e. domain part
        without the registrable domain name).
        
        @param host host address
        @type str
        @param registrablePart registrable domain part of the host address
        @type str
        @return subdomain name
        @rtype str
        """
        if not host or not registrablePart:
            return ""
        
        subdomain = self.__normalizedHost(host)
        
        subdomain = subdomain[:subdomain.rfind(registrablePart)]
        
        if subdomain.endswith("."):
            subdomain = subdomain[:-1]
        
        return subdomain
    
    def __normalizedHost(self, host):
        """
        Private method to get the normalized host for a host address.
        
        @param host host address to be normalized
        @type str
        @return normalized host address
        @rtype str
        """
        return host.lower()
    
    #################################################################
    ## Methods below are for testing purposes
    #################################################################
    
    def test(self):
        """
        Public method to execute the tests.
        
        @return flag indicating the test result
        @rtype bool
        """
        self.__withPrivate = True
        self.__loadData()
        if not self.__tldDict:
            return False
        
        testDataFileName = ""
        testDataFileExist = False
        
        for path in self.__dataSearchPaths:
            testDataFileName = QFileInfo(path + "/test_psl.txt")\
                .absoluteFilePath()
            if QFileInfo(testDataFileName).exists():
                testDataFileExist = True
                break
        
        if not testDataFileExist:
            testFileDownloadLink = \
                "http://mxr.mozilla.org/mozilla-central/source/netwerk/test/" \
                "unit/data/test_psl.txt?raw=1"
            E5MessageBox.information(
                None,
                self.tr("TLD Data File not found"),
                self.tr("""<p>The file 'test_psl.txt' was not found!"""
                        """<br/>You can download it from '<a href="{0}">"""
                        """<b>here</b></a>' to one of the following"""
                        """ paths:</p><ul>{1}</ul>""").format(
                    testFileDownloadLink,
                    "".join(["<li>{0}</li>".format(p)
                             for p in self.__dataSearchPaths]))
            )
            return False
        
        file = QFile(testDataFileName)
        
        if not file.open(QFile.ReadOnly | QFile.Text):
            return False
        
        testRegExp = QRegExp(
            "checkPublicSuffix\\(('([^']+)'|null), ('([^']+)'|null)\\);")
        allTestSuccess = True
        
        while not file.atEnd():
            line = bytes(file.readLine()).decode("utf-8").strip()
            if not line or line.startswith("//"):
                continue
            
            if testRegExp.indexIn(line) == -1:
                allTestSuccess = False
            else:
                hostName = testRegExp.cap(2)
                registrableName = testRegExp.cap(4)
                
                if not self.__checkPublicSuffix(hostName, registrableName):
                    allTestSuccess = False
        
        if allTestSuccess:
            qWarning("E5TldExtractor: Test passed successfully.")
        else:
            qWarning("E5TldExtractor: Test finished with some errors!")
        
        # reset the TLD dictionary
        self.__tldDict = collections.defaultdict(list)
        
        return allTestSuccess
    
    def __checkPublicSuffix(self, host, registrableName):
        """
        Private method to test a host name against a registrable name.
        
        @param host host name to test
        @type str
        @param registrableName registrable domain name to test against
        @type str
        @return flag indicating the check result
        @rtype bool
        """
        regName = self.registrableDomain(host)
        if regName != registrableName:
            qWarning(
                "E5TldExtractor Test Error: hostName: {0}\n"
                "    Correct registrableName:    {1}\n"
                "    Calculated registrableName: {2}".format(
                    host, registrableName, regName))
            return False
        
        return True


_TLDExtractor = None


def instance(withPrivate=False):
    """
    Global function to get a reference to the TLD extractor and create it, if
    it hasn't been yet.
    
    @param withPrivate flag indicating to load private TLDs as well
    @type bool
    @return reference to the zoom manager object
    @rtype E5TldExtractor
    """
    global _TLDExtractor
    
    if _TLDExtractor is None:
        _TLDExtractor = E5TldExtractor(withPrivate=withPrivate)
    
    return _TLDExtractor
