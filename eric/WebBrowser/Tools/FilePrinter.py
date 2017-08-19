# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing an object for printing of files.
"""

#
# This code is inspired by and ported from Qupzilla.
# Original Copyright (C) 2016 by Kevin Kofler <kevin.kofler@chello.at>
#

from __future__ import unicode_literals

from PyQt5.QtCore import QFile, QStandardPaths, QProcess
from PyQt5.QtPrintSupport import QPrinter, QPrintEngine

import Globals
from Globals import qVersionTuple


_FilePrintJobs = []


class FilePrinter(object):
    """
    Class implementing methods for printing on *nix systems.
    """
    #
    # Whether file(s) get deleted by the application or by the print system.
    #
    ApplicationDeletesFiles = 0
    SystemDeletesFiles = 1
    
    #
    # Whether pages to be printed are selected by the application or the print
    # system.
    #
    # If application side, then the generated file will only contain those
    # pages selected by the user, so FilePrinter will print all the pages in
    # the file.
    #
    #  If system side, then the file will contain all the pages in the
    # document, and the print system will print the users selected print range
    # from out of the file.
    #
    # Note: system side only works in CUPS, not LPR.
    #
    ApplicationSelectsPages = 0
    SystemSelectsPages = 1
    
    def __init__(self):
        """
        Constructor
        """
        self.__paperSizesMap = {
            QPrinter.A0: "A0",
            QPrinter.A1: "A1",
            QPrinter.A2: "A2",
            QPrinter.A3: "A3",
            QPrinter.A4: "A4",
            QPrinter.A5: "A5",
            QPrinter.A6: "A6",
            QPrinter.A7: "A7",
            QPrinter.A8: "A8",
            QPrinter.A9: "A9",
            QPrinter.B0: "B0",
            QPrinter.B1: "B1",
            QPrinter.B2: "B2",
            QPrinter.B3: "B3",
            QPrinter.B4: "B4",
            QPrinter.B5: "B5",
            QPrinter.B6: "B6",
            QPrinter.B7: "B7",
            QPrinter.B8: "B8",
            QPrinter.B9: "B9",
            QPrinter.B10: "B10",
            QPrinter.C5E: "C5",
            QPrinter.Comm10E: "Comm10",
            QPrinter.DLE: "DL",
            QPrinter.Executive: "Executive",
            QPrinter.Folio: "Folio",
            QPrinter.Ledger: "Ledger",
            QPrinter.Legal: "Legal",
            QPrinter.Letter: "Letter",
            QPrinter.Tabloid: "Tabloid",
        }
        
        self.__paperSourcesMap = {
            QPrinter.Auto: "",
            QPrinter.Cassette: "Cassette",
            QPrinter.Envelope: "Envelope",
            QPrinter.EnvelopeManual: "EnvelopeManual",
            QPrinter.FormSource: "FormSource",
            QPrinter.LargeCapacity: "LargeCapacity",
            QPrinter.LargeFormat: "LargeFormat",
            QPrinter.Lower: "Lower",
            QPrinter.MaxPageSource: "MaxPageSource",
            QPrinter.Middle: "Middle",
            QPrinter.Manual: "Manual",
            QPrinter.OnlyOne: "OnlyOne",
            QPrinter.Tractor: "Tractor",
            QPrinter.SmallFormat: "SmallFormat",
        }
        
        self.__process = None
        self.__doDeleteFile = FilePrinter.ApplicationDeletesFiles
        self.__fileName = ""
    
    def _doPrintFile(self, printer, fileName, fileDeletePolicy,
                     pageSelectPolicy, pageRange):
        """
        Protected method to print a file.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @param fileName name (path) of the file to be printed
        @type str
        @param fileDeletePolicy policy determining who deletes the file to be
            printed (application or system)
        @type int (0 or 1)
        @param pageSelectPolicy policy determining who selects the pages to be
            printed (application or system)
        @type int (0 or 1)
        @param pageRange string determining the page range(s) to be printed, if
            SystemSelectsPages was given for pageSelectPolicy and user chose
            Selection in print dialog
        @type str
        @return flag indicating successful print job submission
        @rtype bool
        """
        if not QFile.exists(fileName):
            return False
        
        self.__fileName = fileName
        self.__doDeleteFile = (
            fileDeletePolicy == FilePrinter.SystemDeletesFiles)
        
        if printer.printerState() in [QPrinter.Aborted, QPrinter.Error]:
            if self.__doDeleteFile:
                QFile.remove(fileName)
            return False
        
        #
        # Print via lpr/lp command
        #
        
        #
        # Decide what executable to use to print with, need the CUPS version
        # of lpr if available. Some distros name the CUPS version of lpr as
        # lpr-cups or lpr.cups so try those first before default to lpr, or
        # failing that to lp.
        if QStandardPaths.findExecutable("lpr-cups"):
            exe = "lpr-cups"
        elif QStandardPaths.findExecutable("lpr.cups"):
            exe = "lpr.cups"
        elif QStandardPaths.findExecutable("lpr"):
            exe = "lpr"
        elif QStandardPaths.findExecutable("lp"):
            exe = "lp"
        else:
            if self.__doDeleteFile:
                QFile.remove(fileName)
            return False
        
        useCupsOptions = isCupsAvailable()
        argsList = self._printArguments(
            printer, fileDeletePolicy, pageSelectPolicy, useCupsOptions,
            pageRange, exe)
        argsList.append(fileName)
        
        self.__process = QProcess()
        if qVersionTuple() < (5, 6, 0):
            self.__process.error.connect(self.__processError)
        else:
            self.__process.errorOccurred.connect(self.__processError)
        self.__process.finished.connect(self.__processFinished)
        self.__process.start(exe, argsList)
        if not self.__process.waitForStarted(10000):
            # it failed to start
            self.__doCleanup(self.__doDeleteFile)
            return False
        
        return True
    
    def __doCleanup(self, deleteFile):
        """
        Private method to perform some internal cleanup actions.
        
        @param deleteFile flag indicating to delete the print file
        @type bool
        """
        if deleteFile:
            QFile.remove(self.__fileName)
        
        self.__process.deleteLater()
        self.__process = None
        
        if self in _FilePrintJobs:
            _FilePrintJobs.remove(self)
    
    def __processError(self, error):
        """
        Private slot handling process errors.
        
        @param error error value
        @type QProcess.ProcessError
        """
        self.__doCleanup(self.__doDeleteFile)
    
    def __processFinished(self, exitCode, exitStatus):
        """
        Private slot handling the end of the process.
        
        @param exitCode exit code of the process
        @type int
        @param exitStatus exit status of the process
        @type QProcess.ExitStatus
        """
        self.__doCleanup(self.__doDeleteFile and (
            exitStatus != QProcess.NormalExit or exitCode != 0))
    
    def _printArguments(self, printer, fileDeletePolicy, pageSelectPolicy,
                        useCupsOptions, pageRange, variant):
        """
        Protected method to assemble the command line arguments for the print
        command.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @param fileDeletePolicy policy determining who deletes the file to be
            printed (application or system)
        @type int (0 or 1)
        @param pageSelectPolicy policy determining who selects the pages to be
            printed (application or system)
        @type int (0 or 1)
        @param useCupsOptions flag indicating to assemble the arguments for
            CUPS
        @type bool
        @param pageRange string determining the page range(s) to be printed, if
            SystemSelectsPages was given for pageSelectPolicy and user chose
            Selection in print dialog
        @type str
        @param variant string identifying the print command variant
        @type str
        @return assembled command line arguments for the print command
        @rtype list of str
        """
        if variant.startswith("lpr"):
            variant = "lpr"
        
        args = []
        args.extend(self._destination(printer, variant))
        args.extend(self._copies(printer, variant))
        args.extend(self._jobname(printer, variant))
        args.extend(self._pages(printer, pageSelectPolicy, pageRange,
                    useCupsOptions, variant))
        if useCupsOptions:
            args.extend(self._cupsOptions(printer))
        args.extend(self._deleteFile(printer, fileDeletePolicy, variant))
        if variant == "lp":
            args.append("--")
        
        return args
    
    def _destination(self, printer, variant):
        """
        Protected method to assemble the printer destination arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @param variant string identifying the print command variant
        @type str
        @return assembled printer destination arguments
        @rtype list of str
        """
        if variant == "lp":
            return ["-d", printer.printerName()]
        elif variant == "lpr":
            return ["-P", printer.printerName()]
        else:
            return []
    
    def _copies(self, printer, variant):
        """
        Protected method to assemble the number of copies arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @param variant string identifying the print command variant
        @type str
        @return assembled number of copies arguments
        @rtype list of str
        """
        copies = printer.copyCount()
        if variant == "lp":
            return ["-n", str(copies)]
        elif variant == "lpr":
            return ["-#{0}".format(copies)]
        else:
            return []
    
    def _jobname(self, printer, variant):
        """
        Protected method to assemble the jobname arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @param variant string identifying the print command variant
        @type str
        @return assembled jobname arguments
        @rtype list of str
        """
        if printer.docName():
            if variant == "lp":
                return ["-t", printer.docName()]
            elif variant == "lpr":
                shortenedDocName = printer.docName()[:255]
                return ["-J", shortenedDocName]
        
        return []
    
    def _deleteFile(self, printer, fileDeletePolicy, variant):
        """
        Protected method to assemble the jobname arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @param fileDeletePolicy policy determining who deletes the file to be
            printed (application or system)
        @type int (0 or 1)
        @param variant string identifying the print command variant
        @type str
        @return assembled jobname arguments
        @rtype list of str
        """
        if fileDeletePolicy == FilePrinter.SystemDeletesFiles and \
                variant == "lpr":
            return ["-r"]
        else:
            return []
    
    def _pages(self, printer, pageSelectPolicy, pageRange, useCupsOptions,
               variant):
        """
        Protected method to assemble the page range(s) arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @param pageSelectPolicy policy determining who selects the pages to be
            printed (application or system)
        @type int (0 or 1)
        @param pageRange string determining the page range(s) to be printed, if
            SystemSelectsPages was given for pageSelectPolicy and user chose
            Selection in print dialog
        @type str
        @param useCupsOptions flag indicating to assemble the arguments for
            CUPS
        @type bool
        @param variant string identifying the print command variant
        @type str
        @return assembled page range(s) arguments
        @rtype list of str
        """
        if pageSelectPolicy == FilePrinter.SystemSelectsPages:
            if printer.printRange() == QPrinter.Selection and bool(pageRange):
                if variant == "lp":
                    return ["-P", pageRange]
                elif variant == "lpr":
                    return ["-o", "page-ranges={0}".format(pageRange)]
            
            if printer.printRange() == QPrinter.PageRange:
                if variant == "lp":
                    return ["-P", "{0}-{1}".format(
                        printer.fromPage(), printer.toPage())]
                elif variant == "lpr":
                    return ["-o", "page-ranges={0}-{1}".format(
                        printer.fromPage(), printer.toPage())]
        
        return []       # all pages
    
    def _cupsOptions(self, printer):
        """
        Protected method to assemble the CUPS specific arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return assembled CUPS arguments
        @rtype list of str
        """
        options = []
        options.extend(self._optionMedia(printer))
        options.extend(self._optionDoubleSidedPrinting(printer))
        options.extend(self._optionPageOrder(printer))
        options.extend(self._optionCollateCopies(printer))
        options.extend(self._optionCupsProperties(printer))
        
        return options
    
    def _optionMedia(self, printer):
        """
        Protected method to assemble the print media arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return assembled print media arguments
        @rtype list of str
        """
        pageSize = self._mediaPageSize(printer)
        paperSource = self._mediaPaperSource(printer)
        
        if pageSize and paperSource:
            return ["-o", "media={0},{1}".format(pageSize, paperSource)]
        
        elif pageSize:
            return ["-o", "media={0}".format(pageSize)]
        
        elif paperSource:
            return ["-o", "media={0}".format(paperSource)]
        
        return []
    
    def _mediaPageSize(self, printer):
        """
        Protected method to get the page size argument.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return page size argument
        @rtype str
        """
        pageSize = printer.pageSize()
        if pageSize in self.__paperSizesMap:
            return self.__paperSizesMap[pageSize]
        else:
            return ""
    
    def _mediaPaperSource(self, printer):
        """
        Protected method to get the paper source argument.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return paper source argument
        @rtype str
        """
        paperSource = printer.paperSource()
        if paperSource in self.__paperSourcesMap:
            return self.__paperSourcesMap[paperSource]
        else:
            return ""
    
    def _optionDoubleSidedPrinting(self, printer):
        """
        Protected method to assemble the double sided printing arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return assembled double sided printing arguments
        @rtype list of str
        """
        duplex = printer.duplex()
        
        if duplex == QPrinter.DuplexNone:
            return ["-o", "sides=one-sided"]
        elif duplex == QPrinter.DuplexAuto:
            if printer.orientation() == QPrinter.Landscape:
                return ["-o", "sides=two-sided-short-edge"]
            else:
                return ["-o", "sides=two-sided-long-edge"]
        elif duplex == QPrinter.DuplexLongSide:
            return ["-o", "sides=two-sided-long-edge"]
        elif duplex == QPrinter.DuplexShortSide:
            return ["-o", "sides=two-sided-short-edge"]
        else:
            return []       # use printer default
    
    def _optionPageOrder(self, printer):
        """
        Protected method to assemble the page order arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return assembled page order arguments
        @rtype list of str
        """
        if printer.pageOrder() == QPrinter.LastPageFirst:
            return ["-o", "outputorder=reverse"]
        else:
            return ["-o", "outputorder=normal"]
    
    def _optionCollateCopies(self, printer):
        """
        Protected method to assemble the collate copies arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return assembled collate copies arguments
        @rtype list of str
        """
        if printer.collateCopies():
            return ["-o", "Collate=True"]
        else:
            return ["-o", "Collate=False"]
    
    def _optionCupsProperties(self, printer):
        """
        Protected method to assemble the CUPS properties arguments.
        
        @param printer reference to the printer to print to
        @type QPrinter
        @return assembled CUPS properties arguments
        @rtype list of str
        """
        options = Globals.toList(printer.printEngine().property(
            QPrintEngine.PrintEnginePropertyKey(0xfe00)))
        
        cupsOptions = []
        index = 0
        while index < len(options):
            if options[index + 1]:
                cupsOptions.extend(["-o", "{0}={1}".format(
                    options[index], options[index + 1])])
            else:
                cupsOptions.extend(["-o", options[index]])
            index += 2
        
        return cupsOptions


def isCupsAvailable():
    """
    Static method to test the availability of CUPS.
    
    @return flag indicating the availability of CUPS
    @rtype bool
    """
    if Globals.isMacPlatform():
        # OS X/MacOS always have CUPS
        return True
    elif Globals.isLinuxPlatform():
        testPrinter = QPrinter()
        return testPrinter.supportsMultipleCopies()
    else:
        return False


def printFile(printer, fileName,
              fileDeletePolicy=FilePrinter.ApplicationDeletesFiles,
              pageSelectPolicy=FilePrinter.ApplicationSelectsPages,
              pageRange=""):
    """
    Static method to print a file.
    
    Note: Only CUPS and LPR on *nix systems is supported.
    
    @param printer reference to the printer to print to
    @type QPrinter
    @param fileName name (path) of the file to be printed
    @type str
    @param fileDeletePolicy policy determining who deletes the file to be
        printed (application or system)
    @type int (0 or 1)
    @param pageSelectPolicy policy determining who selects the pages to be
        printed (application or system)
    @type int (0 or 1)
    @param pageRange string determining the page range(s) to be printed, if
        SystemSelectsPages was given for pageSelectPolicy and user chose
        Selection in print dialog
    @type str
    """
    fp = FilePrinter()
    if fp._doPrintFile(printer, fileName, fileDeletePolicy, pageSelectPolicy,
                       pageRange):
        _FilePrintJobs.append(fp)
