# -*- coding: utf-8 -*-

# Copyright (c) 2014 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#
# pylint: disable=C0103

"""
Module implementing the syntax check for Python 2/3.
"""

from __future__ import unicode_literals

try:  # Only for Py2
    import Queue as queue
except ImportError:
    import queue

import os
import sys
import multiprocessing


def initService():
    """
    Initialize the service and return the entry point.
    
    @return the entry point for the background client (function)
    """
    path = __file__
    for i in range(4):
        path = os.path.dirname(path)
    sys.path.insert(2, os.path.join(path, "ThirdParty", "Jasy"))
    return jsSyntaxCheck


def initBatchService():
    """
    Initialize the batch service and return the entry point.
    
    @return the entry point for the background client (function)
    """
    return jsSyntaxBatchCheck


def normalizeCode(codestring):
    """
    Function to normalize the given code.
    
    @param codestring code to be normalized (string)
    @return normalized code (string)
    """
    codestring = codestring.replace("\r\n", "\n").replace("\r", "\n")

    if codestring and codestring[-1] != '\n':
        codestring = codestring + '\n'

    # Check type for py2: if not str it's unicode
#    if sys.version_info[0] == 2:
#        try:
#            codestring = codestring.encode('utf-8')
#        except UnicodeError:
#            pass
    
    return codestring


def jsSyntaxCheck(file, codestring):
    """
    Function to check a Javascript source file for syntax errors.
    
    @param file source filename (string)
    @param codestring string containing the code to check (string)
    @return dictionary with the keys 'error' and 'warnings' which
            hold a list containing details about the error/ warnings
            (file name, line number, column, codestring (only at syntax
            errors), the message, a list with arguments for the message)
    """
    return __jsSyntaxCheck(file, codestring)


def jsSyntaxBatchCheck(argumentsList, send, fx, cancelled, maxProcesses=0):
    """
    Module function to check syntax for a batch of files.
    
    @param argumentsList list of arguments tuples as given for jsSyntaxCheck
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
                filename, result = doneQueue.get()
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
    for filename, args in iter(inputQueue.get, 'STOP'):
        source = args[0]
        result = __jsSyntaxCheck(filename, source)
        outputQueue.put((filename, result))


def __jsSyntaxCheck(file, codestring):
    """
    Function to check a Javascript source file for syntax errors.
    
    @param file source filename (string)
    @param codestring string containing the code to check (string)
    @return dictionary with the keys 'error' and 'warnings' which
            hold a list containing details about the error/ warnings
            (file name, line number, column, codestring (only at syntax
            errors), the message, a list with arguments for the message)
    """
    import jasy.js.parse.Parser as jsParser
    import jasy.js.tokenize.Tokenizer as jsTokenizer
    
    codestring = normalizeCode(codestring)
    
    try:
        jsParser.parse(codestring, file)
    except (jsParser.SyntaxError, jsTokenizer.ParseError) as exc:
        details = exc.args[0]
        error, details = details.splitlines()
        fn, line = details.strip().rsplit(":", 1)
        error = error.split(":", 1)[1].strip()
        
        cline = min(len(codestring.splitlines()), int(line)) - 1
        code = codestring.splitlines()[cline]
        return [{'error': (fn, int(line), 0, code, error)}]
    
    return [{}]
