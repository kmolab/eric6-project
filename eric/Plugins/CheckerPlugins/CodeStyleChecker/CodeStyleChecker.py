# -*- coding: utf-8 -*-

# Copyright (c) 2011 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the code style checker.
"""

try:  # Only for Py2
    import Queue as queue
except ImportError:
    import queue

import sys
import multiprocessing

import pycodestyle
from NamingStyleChecker import NamingStyleChecker

# register the name checker
pycodestyle.register_check(NamingStyleChecker, NamingStyleChecker.Codes)

from DocStyleChecker import DocStyleChecker
from MiscellaneousChecker import MiscellaneousChecker
from ComplexityChecker import ComplexityChecker


def initService():
    """
    Initialize the service and return the entry point.
    
    @return the entry point for the background client (function)
    """
    return codeStyleCheck


def initBatchService():
    """
    Initialize the batch service and return the entry point.
    
    @return the entry point for the background client (function)
    """
    return codeStyleBatchCheck


class CodeStyleCheckerReport(pycodestyle.BaseReport):
    """
    Class implementing a special report to be used with our dialog.
    """
    def __init__(self, options):
        """
        Constructor
        
        @param options options for the report (optparse.Values)
        """
        super(CodeStyleCheckerReport, self).__init__(options)
        
        self.__repeat = options.repeat
        self.errors = []
    
    def error_args(self, line_number, offset, code, check, *args):
        """
        Public method to collect the error messages.
        
        @param line_number line number of the issue (integer)
        @param offset position within line of the issue (integer)
        @param code message code (string)
        @param check reference to the checker function (function)
        @param args arguments for the message (list)
        @return error code (string)
        """
        code = super(CodeStyleCheckerReport, self).error_args(
            line_number, offset, code, check, *args)
        if code and (self.counters[code] == 1 or self.__repeat):
            self.errors.append(
                (self.filename, line_number, offset, (code, args))
            )
        return code


def extractLineFlags(line, startComment="#", endComment="", flagsLine=False):
    """
    Function to extract flags starting and ending with '__' from a line
    comment.
    
    @param line line to extract flags from (string)
    @keyparam startComment string identifying the start of the comment (string)
    @keyparam endComment string identifying the end of a comment (string)
    @keyparam flagsLine flag indicating to check for a flags only line (bool)
    @return list containing the extracted flags (list of strings)
    """
    flags = []
    
    if not flagsLine or (
       flagsLine and line.strip().startswith(startComment)):
        pos = line.rfind(startComment)
        if pos >= 0:
            comment = line[pos + len(startComment):].strip()
            if endComment:
                endPos = line.rfind(endComment)
                if endPos >= 0:
                    comment = comment[:endPos]
            flags = [f.strip() for f in comment.split()
                     if (f.startswith("__") and f.endswith("__"))]
    return flags


def ignoreCode(code, lineFlags):
    """
    Function to check, if the given code should be ignored as per line flags.
    
    @param code error code to be checked
    @type str
    @param lineFlags list of line flags to check against
    @type list of str
    @return flag indicating to ignore the code
    @rtype bool
    """
    if lineFlags:
        
        if "__IGNORE_WARNING__" in lineFlags:
            # ignore all warning codes
            return True
        
        for flag in lineFlags:
            # check individual warning code
            if flag.startswith("__IGNORE_WARNING_"):
                ignoredCode = flag[2:-2].rsplit("_", 1)[-1]
                if code.startswith(ignoredCode):
                    return True
    
    return False


def codeStyleCheck(filename, source, args):
    """
    Do the code style check and/ or fix found errors.
    
    @param filename source filename (string)
    @param source string containing the code to check (string)
    @param args arguments used by the codeStyleCheck function (list of
        excludeMessages (str), includeMessages (str), repeatMessages
        (bool), fixCodes (str), noFixCodes (str), fixIssues (bool),
        maxLineLength (int), hangClosing (bool), docType (str), errors
        (list of str), eol (str), encoding (str), backup (bool))
    @return tuple of stats (dict) and results (tuple for each found violation
        of style (tuple of lineno (int), position (int), text (str), ignored
            (bool), fixed (bool), autofixing (bool), fixedMsg (str)))
    """
    return __checkCodeStyle(filename, source, args)


def codeStyleBatchCheck(argumentsList, send, fx, cancelled, maxProcesses=0):
    """
    Module function to check code style for a batch of files.
    
    @param argumentsList list of arguments tuples as given for codeStyleCheck
    @type list
    @param send reference to send function
    @type func
    @param fx registered service name
    @type str
    @param cancelled reference to function checking for a cancellation
    @type func
    @param maxProcesses number of processes to be used
    @type int
    """
    if maxProcesses == 0:
        # determine based on CPU count
        try:
            NumberOfProcesses = multiprocessing.cpu_count()
            if NumberOfProcesses >= 1:
                NumberOfProcesses -= 1
        except NotImplementedError:
            NumberOfProcesses = 1
    else:
        NumberOfProcesses = maxProcesses

    # Create queues
    taskQueue = multiprocessing.Queue()
    doneQueue = multiprocessing.Queue()

    # Submit tasks (initially two time number of processes
    initialTasks = 2 * NumberOfProcesses
    for task in argumentsList[:initialTasks]:
        taskQueue.put(task)

    # Start worker processes
    for i in range(NumberOfProcesses):
        multiprocessing.Process(target=worker, args=(taskQueue, doneQueue))\
            .start()

    # Get and send results
    endIndex = len(argumentsList) - initialTasks
    for i in range(len(argumentsList)):
        resultSent = False
        wasCancelled = False
        
        while not resultSent:
            try:
                # get result (waiting max. 3 seconds and send it to frontend
                filename, result = doneQueue.get(timeout=3)
                send(fx, filename, result)
                resultSent = True
            except queue.Empty:
                # ignore empty queue, just carry on
                if cancelled():
                    wasCancelled = True
                    break
        
        if wasCancelled or cancelled():
            # just exit the loop ignoring the results of queued tasks
            break
        
        if i < endIndex:
            taskQueue.put(argumentsList[i + initialTasks])

    # Tell child processes to stop
    for i in range(NumberOfProcesses):
        taskQueue.put('STOP')


def worker(inputQueue, outputQueue):
    """
    Module function acting as the parallel worker for the style check.
    
    @param inputQueue input queue (multiprocessing.Queue)
    @param outputQueue output queue (multiprocessing.Queue)
    """
    for filename, source, args in iter(inputQueue.get, 'STOP'):
        result = __checkCodeStyle(filename, source, args)
        outputQueue.put((filename, result))


def __checkCodeStyle(filename, source, args):
    """
    Private module function to perform the code style check and/or fix
    found errors.
    
    @param filename source filename (string)
    @param source string containing the code to check (string)
    @param args arguments used by the codeStyleCheck function (list of
        excludeMessages (str), includeMessages (str), repeatMessages
        (bool), fixCodes (str), noFixCodes (str), fixIssues (bool),
        maxLineLength (int), hangClosing (bool), docType (str), dictionary
        with arguments for the code complexity checker (dict), dictionary
        with arguments for the miscellaneous checker (dict), errors (list
        of str), eol (str), encoding (str), backup (bool))
    @return tuple of statistics (dict) and results (tuple for each found
        violation of style (tuple of lineno (int), position (int), text (str),
        ignored (bool), fixed (bool), autofixing (bool), fixedMsg (str)))
    """
    (excludeMessages, includeMessages, repeatMessages, fixCodes, noFixCodes,
     fixIssues, maxLineLength, hangClosing, docType, codeComplexityArgs,
     miscellaneousArgs, errors, eol, encoding, backup) = args
    
    stats = {}

    if fixIssues:
        from CodeStyleFixer import CodeStyleFixer
        fixer = CodeStyleFixer(
            filename, source, fixCodes, noFixCodes,
            maxLineLength, True, eol, backup)  # always fix in place
    else:
        fixer = None
    
    if not errors:
        # avoid 'Encoding declaration in unicode string' exception on Python2
        if sys.version_info[0] == 2:
            if encoding == 'utf-8-bom':
                enc = 'utf-8'
            else:
                enc = encoding
            source = [line.encode(enc) for line in source]
        
        if includeMessages:
            select = [s.strip() for s in
                      includeMessages.split(',') if s.strip()]
        else:
            select = []
        if excludeMessages:
            ignore = [i.strip() for i in
                      excludeMessages.split(',') if i.strip()]
        else:
            ignore = []
        
        # check coding style
        styleGuide = pycodestyle.StyleGuide(
            reporter=CodeStyleCheckerReport,
            repeat=repeatMessages,
            select=select,
            ignore=ignore,
            max_line_length=maxLineLength,
            hang_closing=hangClosing,
        )
        report = styleGuide.check_files([filename])
        stats.update(report.counters)
        errors = report.errors

        # check documentation style
        docStyleChecker = DocStyleChecker(
            source, filename, select, ignore, [], repeatMessages,
            maxLineLength=maxLineLength, docType=docType)
        docStyleChecker.run()
        stats.update(docStyleChecker.counters)
        errors += docStyleChecker.errors
        
        # miscellaneous additional checks
        miscellaneousChecker = MiscellaneousChecker(
            source, filename, select, ignore, [], repeatMessages,
            miscellaneousArgs)
        miscellaneousChecker.run()
        stats.update(miscellaneousChecker.counters)
        errors += miscellaneousChecker.errors
        
        # check code complexity
        complexityChecker = ComplexityChecker(
            source, filename, select, ignore, codeComplexityArgs)
        complexityChecker.run()
        stats.update(complexityChecker.counters)
        errors += complexityChecker.errors
    
    errorsDict = {}
    for fname, lineno, position, text in errors:
        if lineno > len(source):
            lineno = len(source)
        # inverse processing of messages and fixes
        errorLine = errorsDict.setdefault(lineno, [])
        errorLine.append([position, text])
    deferredFixes = {}
    results = []
    for lineno, errors in errorsDict.items():
        errors.sort(key=lambda x: x[0], reverse=True)
        for position, text in errors:
            if source:
                code = text[0]
                lineFlags = extractLineFlags(source[lineno - 1].strip())
                try:
                    lineFlags += extractLineFlags(source[lineno].strip(),
                                                  flagsLine=True)
                except IndexError:
                    pass
                if not ignoreCode(code, lineFlags):
                    if fixer:
                        res, msg, id_ = fixer.fixIssue(lineno, position, text)
                        if res == -1:
                            itm = [lineno, position, text]
                            deferredFixes[id_] = itm
                        else:
                            itm = [lineno, position, text, False,
                                   res == 1, True, msg]
                    else:
                        itm = [lineno, position, text, False,
                               False, False, '']
                    results.append(itm)
                else:
                    results.append([lineno, position, text, True,
                                    False, False, ''])
            else:
                results.append([lineno, position, text, False,
                                False, False, ''])
    
    if fixer:
        deferredResults = fixer.finalize()
        for id_ in deferredResults:
            fixed, msg = deferredResults[id_]
            itm = deferredFixes[id_]
            itm.extend([False, fixed == 1, True, msg])

        errMsg = fixer.saveFile(encoding)
        if errMsg:
            for result in results:
                result[-1] = errMsg

    return stats, results

#
# eflag: noqa = M702
