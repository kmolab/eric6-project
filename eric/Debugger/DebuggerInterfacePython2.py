# -*- coding: utf-8 -*-

# Copyright (c) 2007 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Python debugger interface for the debug server.
"""

from __future__ import unicode_literals

import sys
import os

from PyQt5.QtCore import QObject, QTextCodec, QProcess, QProcessEnvironment, \
    QTimer
from PyQt5.QtWidgets import QInputDialog

from E5Gui.E5Application import e5App
from E5Gui import E5MessageBox

from . import DebugClientCapabilities

import Preferences
import Utilities

from eric6config import getConfig


ClientDefaultCapabilities = DebugClientCapabilities.HasAll


class DebuggerInterfacePython2(QObject):
    """
    Class implementing the Python 2 debugger interface for the debug server.
    """
    def __init__(self, debugServer, passive):
        """
        Constructor
        
        @param debugServer reference to the debug server (DebugServer)
        @param passive flag indicating passive connection mode (boolean)
        """
        super(DebuggerInterfacePython2, self).__init__()
        
        self.__isNetworked = True
        self.__autoContinue = False
        
        self.debugServer = debugServer
        self.passive = passive
        self.process = None
        
        self.qsock = None
        self.queue = []
        
        # set default values for capabilities of clients
        self.clientCapabilities = ClientDefaultCapabilities
        
        # set translation function
        self.translate = self.__identityTranslation
        
        self.codec = QTextCodec.codecForName(
            Preferences.getSystem("StringEncoding"))
        
        if passive:
            # set translation function
            if Preferences.getDebugger("PathTranslation"):
                self.translateRemote = \
                    Preferences.getDebugger("PathTranslationRemote")
                self.translateLocal = \
                    Preferences.getDebugger("PathTranslationLocal")
                self.translate = self.__remoteTranslation
            else:
                self.translate = self.__identityTranslation
        
        # attribute to remember the name of the executed script
        self.__scriptName = ""

    def __identityTranslation(self, fn, remote2local=True):
        """
        Private method to perform the identity path translation.
        
        @param fn filename to be translated (string)
        @param remote2local flag indicating the direction of translation
            (False = local to remote, True = remote to local [default])
        @return translated filename (string)
        """
        return fn
        
    def __remoteTranslation(self, fn, remote2local=True):
        """
        Private method to perform the path translation.
        
        @param fn filename to be translated (string)
        @param remote2local flag indicating the direction of translation
            (False = local to remote, True = remote to local [default])
        @return translated filename (string)
        """
        if remote2local:
            return fn.replace(self.translateRemote, self.translateLocal)
        else:
            return fn.replace(self.translateLocal, self.translateRemote)
        
    def __startProcess(self, program, arguments, environment=None):
        """
        Private method to start the debugger client process.
        
        @param program name of the executable to start (string)
        @param arguments arguments to be passed to the program (list of string)
        @param environment dictionary of environment settings to pass
            (dict of string)
        @return the process object (QProcess) or None
        """
        proc = QProcess()
        if environment is not None:
            env = QProcessEnvironment()
            for key, value in list(environment.items()):
                env.insert(key, value)
            proc.setProcessEnvironment(env)
        args = []
        for arg in arguments:
            args.append(arg)
        proc.start(program, args)
        if not proc.waitForStarted(10000):
            proc = None
        
        return proc
        
    def startRemote(self, port, runInConsole):
        """
        Public method to start a remote Python interpreter.
        
        @param port portnumber the debug server is listening on (integer)
        @param runInConsole flag indicating to start the debugger in a
            console window (boolean)
        @return client process object (QProcess), a flag to indicate
            a network connection (boolean) and the name of the interpreter
            in case of a local execution (string)
        """
        interpreter = Preferences.getDebugger("PythonInterpreter")
        if interpreter == "":
            E5MessageBox.critical(
                None,
                self.tr("Start Debugger"),
                self.tr(
                    """<p>No Python2 interpreter configured.</p>"""))
            return None, False, ""
        
        debugClientType = Preferences.getDebugger("DebugClientType")
        if debugClientType == "standard":
            debugClient = os.path.join(getConfig('ericDir'),
                                       "DebugClients", "Python",
                                       "DebugClient.py")
        else:
            debugClient = Preferences.getDebugger("DebugClient")
            if debugClient == "":
                debugClient = os.path.join(sys.path[0],
                                           "DebugClients", "Python",
                                           "DebugClient.py")
        
        redirect = str(Preferences.getDebugger("PythonRedirect"))
        noencoding = Preferences.getDebugger("PythonNoEncoding") and \
            '--no-encoding' or ''
        
        if Preferences.getDebugger("RemoteDbgEnabled"):
            ipaddr = self.debugServer.getHostAddress(False)
            rexec = Preferences.getDebugger("RemoteExecution")
            rhost = Preferences.getDebugger("RemoteHost")
            if rhost == "":
                rhost = "localhost"
            if rexec:
                args = Utilities.parseOptionString(rexec) + \
                    [rhost, interpreter, debugClient,
                        noencoding, str(port), redirect, ipaddr]
                args[0] = Utilities.getExecutablePath(args[0])
                process = self.__startProcess(args[0], args[1:])
                if process is None:
                    E5MessageBox.critical(
                        None,
                        self.tr("Start Debugger"),
                        self.tr(
                            """<p>The debugger backend could not be"""
                            """ started.</p>"""))
                
                # set translation function
                if Preferences.getDebugger("PathTranslation"):
                    self.translateRemote = \
                        Preferences.getDebugger("PathTranslationRemote")
                    self.translateLocal = \
                        Preferences.getDebugger("PathTranslationLocal")
                    self.translate = self.__remoteTranslation
                else:
                    self.translate = self.__identityTranslation
                return process, self.__isNetworked, ""
        
        # set translation function
        self.translate = self.__identityTranslation
        
        # setup the environment for the debugger
        if Preferences.getDebugger("DebugEnvironmentReplace"):
            clientEnv = {}
        else:
            clientEnv = os.environ.copy()
        envlist = Utilities.parseEnvironmentString(
            Preferences.getDebugger("DebugEnvironment"))
        for el in envlist:
            try:
                key, value = el.split('=', 1)
                if value.startswith('"') or value.startswith("'"):
                    value = value[1:-1]
                clientEnv[str(key)] = str(value)
            except ValueError:
                pass
        
        ipaddr = self.debugServer.getHostAddress(True)
        if runInConsole or Preferences.getDebugger("ConsoleDbgEnabled"):
            ccmd = Preferences.getDebugger("ConsoleDbgCommand")
            if ccmd:
                args = Utilities.parseOptionString(ccmd) + \
                    [interpreter, os.path.abspath(debugClient),
                        noencoding, str(port), '0', ipaddr]
                args[0] = Utilities.getExecutablePath(args[0])
                process = self.__startProcess(args[0], args[1:], clientEnv)
                if process is None:
                    E5MessageBox.critical(
                        None,
                        self.tr("Start Debugger"),
                        self.tr(
                            """<p>The debugger backend could not be"""
                            """ started.</p>"""))
                return process, self.__isNetworked, interpreter
        
        process = self.__startProcess(
            interpreter,
            [debugClient, noencoding, str(port), redirect, ipaddr],
            clientEnv)
        if process is None:
            E5MessageBox.critical(
                None,
                self.tr("Start Debugger"),
                self.tr(
                    """<p>The debugger backend could not be started.</p>"""))
        return process, self.__isNetworked, interpreter

    def startRemoteForProject(self, port, runInConsole):
        """
        Public method to start a remote Python interpreter for a project.
        
        @param port portnumber the debug server is listening on (integer)
        @param runInConsole flag indicating to start the debugger in a
            console window (boolean)
        @return client process object (QProcess), a flag to indicate
            a network connection (boolean) and the name of the interpreter
            in case of a local execution (string)
        """
        project = e5App().getObject("Project")
        if not project.isDebugPropertiesLoaded():
            return None, self.__isNetworked, ""
        
        # start debugger with project specific settings
        interpreter = project.getDebugProperty("INTERPRETER")
        debugClient = project.getDebugProperty("DEBUGCLIENT")
        
        redirect = str(project.getDebugProperty("REDIRECT"))
        noencoding = \
            project.getDebugProperty("NOENCODING") and '--no-encoding' or ''
        
        if project.getDebugProperty("REMOTEDEBUGGER"):
            ipaddr = self.debugServer.getHostAddress(False)
            rexec = project.getDebugProperty("REMOTECOMMAND")
            rhost = project.getDebugProperty("REMOTEHOST")
            if rhost == "":
                rhost = "localhost"
            if rexec:
                args = Utilities.parseOptionString(rexec) + \
                    [rhost, interpreter, os.path.abspath(debugClient),
                        noencoding, str(port), redirect, ipaddr]
                args[0] = Utilities.getExecutablePath(args[0])
                process = self.__startProcess(args[0], args[1:])
                if process is None:
                    E5MessageBox.critical(
                        None,
                        self.tr("Start Debugger"),
                        self.tr(
                            """<p>The debugger backend could not be"""
                            """ started.</p>"""))
                # set translation function
                if project.getDebugProperty("PATHTRANSLATION"):
                    self.translateRemote = \
                        project.getDebugProperty("REMOTEPATH")
                    self.translateLocal = \
                        project.getDebugProperty("LOCALPATH")
                    self.translate = self.__remoteTranslation
                else:
                    self.translate = self.__identityTranslation
                return process, self.__isNetworked, ""
        
        # set translation function
        self.translate = self.__identityTranslation
        
        # setup the environment for the debugger
        if project.getDebugProperty("ENVIRONMENTOVERRIDE"):
            clientEnv = {}
        else:
            clientEnv = os.environ.copy()
        envlist = Utilities.parseEnvironmentString(
            project.getDebugProperty("ENVIRONMENTSTRING"))
        for el in envlist:
            try:
                key, value = el.split('=', 1)
                if value.startswith('"') or value.startswith("'"):
                    value = value[1:-1]
                clientEnv[str(key)] = str(value)
            except ValueError:
                pass
        
        ipaddr = self.debugServer.getHostAddress(True)
        if runInConsole or project.getDebugProperty("CONSOLEDEBUGGER"):
            ccmd = project.getDebugProperty("CONSOLECOMMAND") or \
                Preferences.getDebugger("ConsoleDbgCommand")
            if ccmd:
                args = Utilities.parseOptionString(ccmd) + \
                    [interpreter, os.path.abspath(debugClient),
                        noencoding, str(port), '0', ipaddr]
                args[0] = Utilities.getExecutablePath(args[0])
                process = self.__startProcess(args[0], args[1:], clientEnv)
                if process is None:
                    E5MessageBox.critical(
                        None,
                        self.tr("Start Debugger"),
                        self.tr(
                            """<p>The debugger backend could not be"""
                            """ started.</p>"""))
                return process, self.__isNetworked, interpreter
        
        process = self.__startProcess(
            interpreter,
            [debugClient, noencoding, str(port), redirect, ipaddr],
            clientEnv)
        if process is None:
            E5MessageBox.critical(
                None,
                self.tr("Start Debugger"),
                self.tr(
                    """<p>The debugger backend could not be started.</p>"""))
        return process, self.__isNetworked, interpreter

    def getClientCapabilities(self):
        """
        Public method to retrieve the debug clients capabilities.
        
        @return debug client capabilities (integer)
        """
        return self.clientCapabilities
        
    def newConnection(self, sock):
        """
        Public slot to handle a new connection.
        
        @param sock reference to the socket object (QTcpSocket)
        @return flag indicating success (boolean)
        """
        # If we already have a connection, refuse this one.  It will be closed
        # automatically.
        if self.qsock is not None:
            return False
        
        sock.disconnected.connect(self.debugServer.startClient)
        sock.readyRead.connect(self.__parseClientLine)
        
        self.qsock = sock
        
        # Get the remote clients capabilities
        self.remoteCapabilities()
        return True
        
    def flush(self):
        """
        Public slot to flush the queue.
        """
        # Send commands that were waiting for the connection.
        for cmd in self.queue:
            self.qsock.write(cmd.encode('utf8', 'backslashreplace'))
        
        self.queue = []
        
    def shutdown(self):
        """
        Public method to cleanly shut down.
        
        It closes our socket and shuts down
        the debug client. (Needed on Win OS)
        """
        if self.qsock is None:
            return
        
        # do not want any slots called during shutdown
        self.qsock.disconnected.disconnect(self.debugServer.startClient)
        self.qsock.readyRead.disconnect(self.__parseClientLine)
        
        # close down socket, and shut down client as well.
        self.__sendJsonCommand("RequestShutdown", {})
        self.qsock.flush()
        self.qsock.close()
        
        # reinitialize
        self.qsock = None
        self.queue = []
        
    def isConnected(self):
        """
        Public method to test, if a debug client has connected.
        
        @return flag indicating the connection status (boolean)
        """
        return self.qsock is not None
        
    def remoteEnvironment(self, env):
        """
        Public method to set the environment for a program to debug, run, ...
        
        @param env environment settings (dictionary)
        """
        self.__sendJsonCommand("RequestEnvironment", {"environment": env})
        
    def remoteLoad(self, fn, argv, wd, traceInterpreter=False,
                   autoContinue=True, autoFork=False, forkChild=False):
        """
        Public method to load a new program to debug.
        
        @param fn the filename to debug (string)
        @param argv the commandline arguments to pass to the program (string)
        @param wd the working directory for the program (string)
        @keyparam traceInterpreter flag indicating if the interpreter library
            should be traced as well (boolean)
        @keyparam autoContinue flag indicating, that the debugger should not
            stop at the first executable line (boolean)
        @keyparam autoFork flag indicating the automatic fork mode (boolean)
        @keyparam forkChild flag indicating to debug the child after forking
            (boolean)
        """
        self.__autoContinue = autoContinue
        self.__scriptName = os.path.abspath(fn)
        
        wd = self.translate(wd, False)
        fn = self.translate(os.path.abspath(fn), False)
        self.__sendJsonCommand("RequestLoad", {
            "workdir": wd,
            "filename": fn,
            "argv": Utilities.parseOptionString(argv),
            "traceInterpreter": traceInterpreter,
            "autofork": autoFork,
            "forkChild": forkChild,
        })
        
    def remoteRun(self, fn, argv, wd, autoFork=False, forkChild=False):
        """
        Public method to load a new program to run.
        
        @param fn the filename to run (string)
        @param argv the commandline arguments to pass to the program (string)
        @param wd the working directory for the program (string)
        @keyparam autoFork flag indicating the automatic fork mode (boolean)
        @keyparam forkChild flag indicating to debug the child after forking
            (boolean)
        """
        self.__scriptName = os.path.abspath(fn)
        
        wd = self.translate(wd, False)
        fn = self.translate(os.path.abspath(fn), False)
        self.__sendJsonCommand("RequestRun", {
            "workdir": wd,
            "filename": fn,
            "argv": Utilities.parseOptionString(argv),
            "autofork": autoFork,
            "forkChild": forkChild,
        })
        
    def remoteCoverage(self, fn, argv, wd, erase=False):
        """
        Public method to load a new program to collect coverage data.
        
        @param fn the filename to run (string)
        @param argv the commandline arguments to pass to the program (string)
        @param wd the working directory for the program (string)
        @keyparam erase flag indicating that coverage info should be
            cleared first (boolean)
        """
        self.__scriptName = os.path.abspath(fn)
        
        wd = self.translate(wd, False)
        fn = self.translate(os.path.abspath(fn), False)
        self.__sendJsonCommand("RequestCoverage", {
            "workdir": wd,
            "filename": fn,
            "argv": Utilities.parseOptionString(argv),
            "erase": erase,
        })

    def remoteProfile(self, fn, argv, wd, erase=False):
        """
        Public method to load a new program to collect profiling data.
        
        @param fn the filename to run (string)
        @param argv the commandline arguments to pass to the program (string)
        @param wd the working directory for the program (string)
        @keyparam erase flag indicating that timing info should be cleared
            first (boolean)
        """
        self.__scriptName = os.path.abspath(fn)
        
        wd = self.translate(wd, False)
        fn = self.translate(os.path.abspath(fn), False)
        self.__sendJsonCommand("RequestProfile", {
            "workdir": wd,
            "filename": fn,
            "argv": Utilities.parseOptionString(argv),
            "erase": erase,
        })

    def remoteStatement(self, stmt):
        """
        Public method to execute a Python statement.
        
        @param stmt the Python statement to execute (string). It
              should not have a trailing newline.
        """
        self.__sendJsonCommand("ExecuteStatement", {
            "statement": stmt,
        })

    def remoteStep(self):
        """
        Public method to single step the debugged program.
        """
        self.__sendJsonCommand("RequestStep", {})

    def remoteStepOver(self):
        """
        Public method to step over the debugged program.
        """
        self.__sendJsonCommand("RequestStepOver", {})

    def remoteStepOut(self):
        """
        Public method to step out the debugged program.
        """
        self.__sendJsonCommand("RequestStepOut", {})

    def remoteStepQuit(self):
        """
        Public method to stop the debugged program.
        """
        self.__sendJsonCommand("RequestStepQuit", {})

    def remoteContinue(self, special=False):
        """
        Public method to continue the debugged program.
        
        @param special flag indicating a special continue operation (boolean)
        """
        self.__sendJsonCommand("RequestContinue", {
            "special": special,
        })

    def remoteMoveIP(self, line):
        """
        Public method to move the instruction pointer to a different line.
        
        @param line the new line, where execution should be continued
        """
        self.__sendJsonCommand("RequestMoveIP", {
            "newLine": line,
        })

    def remoteBreakpoint(self, fn, line, setBreakpoint, cond=None, temp=False):
        """
        Public method to set or clear a breakpoint.
        
        @param fn filename the breakpoint belongs to (string)
        @param line linenumber of the breakpoint (int)
        @param setBreakpoint flag indicating setting or resetting a
            breakpoint (boolean)
        @param cond condition of the breakpoint (string)
        @param temp flag indicating a temporary breakpoint (boolean)
        """
        self.__sendJsonCommand("RequestBreakpoint", {
            "filename": self.translate(fn, False),
            "line": line,
            "temporary": temp,
            "setBreakpoint": setBreakpoint,
            "condition": cond,
        })
        
    def remoteBreakpointEnable(self, fn, line, enable):
        """
        Public method to enable or disable a breakpoint.
        
        @param fn filename the breakpoint belongs to (string)
        @param line linenumber of the breakpoint (int)
        @param enable flag indicating enabling or disabling a breakpoint
            (boolean)
        """
        self.__sendJsonCommand("RequestBreakpointEnable", {
            "filename": self.translate(fn, False),
            "line": line,
            "enable": enable,
        })
        
    def remoteBreakpointIgnore(self, fn, line, count):
        """
        Public method to ignore a breakpoint the next couple of occurrences.
        
        @param fn filename the breakpoint belongs to (string)
        @param line linenumber of the breakpoint (int)
        @param count number of occurrences to ignore (int)
        """
        self.__sendJsonCommand("RequestBreakpointIgnore", {
            "filename": self.translate(fn, False),
            "line": line,
            "count": count,
        })
        
    def remoteWatchpoint(self, cond, setWatch, temp=False):
        """
        Public method to set or clear a watch expression.
        
        @param cond expression of the watch expression (string)
        @param setWatch flag indicating setting or resetting a watch expression
            (boolean)
        @param temp flag indicating a temporary watch expression (boolean)
        """
        # cond is combination of cond and special (s. watch expression viewer)
        self.__sendJsonCommand("RequestWatch", {
            "temporary": temp,
            "setWatch": setWatch,
            "condition": cond,
        })
    
    def remoteWatchpointEnable(self, cond, enable):
        """
        Public method to enable or disable a watch expression.
        
        @param cond expression of the watch expression (string)
        @param enable flag indicating enabling or disabling a watch expression
            (boolean)
        """
        # cond is combination of cond and special (s. watch expression viewer)
        self.__sendJsonCommand("RequestWatchEnable", {
            "condition": cond,
            "enable": enable,
        })
    
    def remoteWatchpointIgnore(self, cond, count):
        """
        Public method to ignore a watch expression the next couple of
        occurrences.
        
        @param cond expression of the watch expression (string)
        @param count number of occurrences to ignore (int)
        """
        # cond is combination of cond and special (s. watch expression viewer)
        self.__sendJsonCommand("RequestWatchIgnore", {
            "condition": cond,
            "count": count,
        })
    
    def remoteRawInput(self, s):
        """
        Public method to send the raw input to the debugged program.
        
        @param s the raw input (string)
        """
        self.__sendJsonCommand("RawInput", {
            "input": s,
        })
        
    def remoteThreadList(self):
        """
        Public method to request the list of threads from the client.
        """
        self.__sendJsonCommand("RequestThreadList", {})
        
    def remoteSetThread(self, tid):
        """
        Public method to request to set the given thread as current thread.
        
        @param tid id of the thread (integer)
        """
        self.__sendJsonCommand("RequestThreadSet", {
            "threadID": tid,
        })
        
    def remoteClientVariables(self, scope, filterList, framenr=0):
        """
        Public method to request the variables of the debugged program.
        
        @param scope the scope of the variables (0 = local, 1 = global)
        @param filterList list of variable types to filter out (list of int)
        @param framenr framenumber of the variables to retrieve (int)
        """
        self.__sendJsonCommand("RequestVariables", {
            "frameNumber": framenr,
            "scope": scope,
            "filters": filterList,
        })
        
    def remoteClientVariable(self, scope, filterList, var, framenr=0):
        """
        Public method to request the variables of the debugged program.
        
        @param scope the scope of the variables (0 = local, 1 = global)
        @param filterList list of variable types to filter out (list of int)
        @param var list encoded name of variable to retrieve (string)
        @param framenr framenumber of the variables to retrieve (int)
        """
        self.__sendJsonCommand("RequestVariable", {
            "variable": var,
            "frameNumber": framenr,
            "scope": scope,
            "filters": filterList,
        })
        
    def remoteClientSetFilter(self, scope, filterStr):
        """
        Public method to set a variables filter list.
        
        @param scope the scope of the variables (0 = local, 1 = global)
        @param filterStr regexp string for variable names to filter out
            (string)
        """
        self.__sendJsonCommand("RequestSetFilter", {
            "scope": scope,
            "filter": filterStr,
        })
        
    def setCallTraceEnabled(self, on):
        """
        Public method to set the call trace state.
        
        @param on flag indicating to enable the call trace function (boolean)
        """
        self.__sendJsonCommand("RequestCallTrace", {
            "enable": on,
        })
    
    def remoteBanner(self):
        """
        Public slot to get the banner info of the remote client.
        """
        self.__sendJsonCommand("RequestBanner", {})
        
    def remoteCapabilities(self):
        """
        Public slot to get the debug clients capabilities.
        """
        self.__sendJsonCommand("RequestCapabilities", {})
        
    def remoteCompletion(self, text):
        """
        Public slot to get the a list of possible commandline completions
        from the remote client.
        
        @param text the text to be completed (string)
        """
        self.__sendJsonCommand("RequestCompletion", {
            "text": text,
        })
        
    def remoteUTPrepare(self, fn, tn, tfn, failed, cov, covname, coverase):
        """
        Public method to prepare a new unittest run.
        
        @param fn the filename to load (string)
        @param tn the testname to load (string)
        @param tfn the test function name to load tests from (string)
        @param failed list of failed test, if only failed test should be run
            (list of strings)
        @param cov flag indicating collection of coverage data is requested
            (boolean)
        @param covname filename to be used to assemble the coverage caches
            filename (string)
        @param coverase flag indicating erasure of coverage data is requested
            (boolean)
        """
        self.__scriptName = os.path.abspath(fn)
        
        fn = self.translate(os.path.abspath(fn), False)
        self.__sendJsonCommand("RequestUTPrepare", {
            "filename": fn,
            "testname": tn,
            "testfunctionname": tfn,
            "failed": failed,
            "coverage": cov,
            "coveragefile": covname,
            "coverageerase": coverase,
        })
        
    def remoteUTRun(self):
        """
        Public method to start a unittest run.
        """
        self.__sendJsonCommand("RequestUTRun", {})
        
    def remoteUTStop(self):
        """
        Public method to stop a unittest run.
        """
        self.__sendJsonCommand("RequestUTStop", {})
        
    def __askForkTo(self):
        """
        Private method to ask the user which branch of a fork to follow.
        """
        selections = [self.tr("Parent Process"),
                      self.tr("Child process")]
        res, ok = QInputDialog.getItem(
            None,
            self.tr("Client forking"),
            self.tr("Select the fork branch to follow."),
            selections,
            0, False)
        if not ok or res == selections[0]:
            self.__sendJsonCommand("ResponseForkTo", {
                "target": "parent",
            })
        else:
            self.__sendJsonCommand("ResponseForkTo", {
                "target": "child",
            })
        
    def __parseClientLine(self):
        """
        Private method to handle data from the client.
        """
        while self.qsock and self.qsock.canReadLine():
            qs = self.qsock.readLine()
            if self.codec is not None:
                line = self.codec.toUnicode(qs)
            else:
                line = bytes(qs).decode()
            
##            print("Server: ", line)          ##debug
            
            self.__handleJsonCommand(line)
            continue
    
    def __handleJsonCommand(self, jsonStr):
        """
        Private method to handle a command or response serialized as a
        JSON string.
        
        @param jsonStr string containing the command or response received
            from the debug backend
        @type str
        """
        import json
        
        try:
            commandDict = json.loads(jsonStr.strip())
        except (TypeError, ValueError) as err:
            E5MessageBox.critical(
                None,
                self.tr("Debug Protocol Error"),
                self.tr("""<p>The response received from the debugger"""
                        """ backend could not be decoded. Please report"""
                        """ this issue with the received data to the"""
                        """ eric bugs email address.</p>"""
                        """<p>Error: {0}</p>"""
                        """<p>Data:<br/>{0}</p>""").format(
                    str(err), Utilities.html_encode(jsonStr.strip())),
                E5MessageBox.StandardButtons(
                    E5MessageBox.Ok))
            return
        
        method = commandDict["method"]
        params = commandDict["params"]
        
        if method == "ClientOutput":
            self.debugServer.signalClientOutput(params["text"])
        
        elif method in ["ResponseLine", "ResponseStack"]:
            # Check if obsolet thread was clicked
            if params["stack"] == []:
                # Request updated list
                self.remoteThreadList()
                return
            for s in params["stack"]:
                s[0] = self.translate(s[0], True)
            cf = params["stack"][0]
            if self.__autoContinue:
                self.__autoContinue = False
                QTimer.singleShot(0, self.remoteContinue)
            else:
                self.debugServer.signalClientLine(
                    cf[0], int(cf[1]),
                    method == "ResponseStack")
                self.debugServer.signalClientStack(params["stack"])
        
        elif method == "CallTrace":
            isCall = params["event"].lower() == "c"
            fromInfo = params["from"]
            toInfo = params["to"]
            self.debugServer.signalClientCallTrace(
                isCall,
                fromInfo["filename"], str(fromInfo["linenumber"]),
                fromInfo["codename"],
                toInfo["filename"], str(toInfo["linenumber"]),
                toInfo["codename"])
        
        elif method == "ResponseVariables":
            self.debugServer.signalClientVariables(
                params["scope"], params["variables"])
        
        elif method == "ResponseVariable":
            self.debugServer.signalClientVariable(
                params["scope"], [params["variable"]] + params["variables"])
        
        elif method == "ResponseThreadList":
            self.debugServer.signalClientThreadList(
                params["currentID"], params["threadList"])
        
        elif method == "ResponseThreadSet":
            self.debugServer.signalClientThreadSet()
        
        elif method == "ResponseCapabilities":
            self.clientCapabilities = params["capabilities"]
            self.debugServer.signalClientCapabilities(
                params["capabilities"], params["clientType"])
        
        elif method == "ResponseBanner":
            self.debugServer.signalClientBanner(
                params["version"],
                params["platform"],
                params["dbgclient"])
        
        elif method == "ResponseOK":
            self.debugServer.signalClientStatement(False)
        
        elif method == "ResponseContinue":
            self.debugServer.signalClientStatement(True)
        
        elif method == "RequestRaw":
            self.debugServer.signalClientRawInput(
                params["prompt"], params["echo"])
        
        elif method == "ResponseBPConditionError":
            fn = self.translate(params["filename"], True)
            self.debugServer.signalClientBreakConditionError(
                fn, params["line"])
        
        elif method == "ResponseClearBreakpoint":
            fn = self.translate(params["filename"], True)
            self.debugServer.signalClientClearBreak(fn, params["line"])
        
        elif method == "ResponseWatchConditionError":
            self.debugServer.signalClientWatchConditionError(
                params["condition"])
        
        elif method == "ResponseClearWatch":
            self.debugServer.signalClientClearWatch(params["condition"])
        
        elif method == "ResponseException":
            if params:
                exctype = params["type"]
                excmessage = params["message"]
                stack = params["stack"]
                if stack:
                    for stackEntry in stack:
                        stackEntry[0] = self.translate(stackEntry[0], True)
                    if stack[0] and stack[0][0] == "<string>":
                        for stackEntry in stack:
                            if stackEntry[0] == "<string>":
                                stackEntry[0] = self.__scriptName
                            else:
                                break
            else:
                exctype = ''
                excmessage = ''
                stack = []
            
            self.debugServer.signalClientException(
                exctype, excmessage, stack)
        
        elif method == "ResponseSyntax":
            self.debugServer.signalClientSyntaxError(
                params["message"], self.translate(params["filename"], True),
                params["linenumber"], params["characternumber"])
        
        elif method == "ResponseSignal":
            self.debugServer.signalClientSignal(
                params["message"], self.translate(params["filename"], True),
                params["linenumber"], params["function"], params["arguments"])
        
        elif method == "ResponseExit":
            self.__scriptName = ""
            self.debugServer.signalClientExit(
                params["status"], params["message"])
        
        elif method == "PassiveStartup":
            self.debugServer.passiveStartUp(
                self.translate(params["filename"], True), params["exceptions"])
        
        elif method == "ResponseCompletion":
            self.debugServer.signalClientCompletionList(
                params["completions"], params["text"])
        
        elif method == "ResponseUTPrepared":
            self.debugServer.clientUtPrepared(
                params["count"], params["exception"], params["message"])
        
        elif method == "ResponseUTFinished":
            self.debugServer.clientUtFinished()
        
        elif method == "ResponseUTStartTest":
            self.debugServer.clientUtStartTest(
                params["testname"], params["description"])
        
        elif method == "ResponseUTStopTest":
            self.debugServer.clientUtStopTest()
        
        elif method == "ResponseUTTestFailed":
            self.debugServer.clientUtTestFailed(
                params["testname"], params["traceback"], params["id"])
        
        elif method == "ResponseUTTestErrored":
            self.debugServer.clientUtTestErrored(
                params["testname"], params["traceback"], params["id"])
        
        elif method == "ResponseUTTestSkipped":
            self.debugServer.clientUtTestSkipped(
                params["testname"], params["reason"], params["id"])
        
        elif method == "ResponseUTTestFailedExpected":
            self.debugServer.clientUtTestFailedExpected(
                params["testname"], params["traceback"], params["id"])
        
        elif method == "ResponseUTTestSucceededUnexpected":
            self.debugServer.clientUtTestSucceededUnexpected(
                params["testname"], params["id"])
        
        elif method == "RequestForkTo":
            self.__askForkTo()

    def __sendJsonCommand(self, command, params):
        """
        Private method to send a single command to the client.
        
        @param command command name to be sent
        @type str
        @param params dictionary of named parameters for the command
        @type dict
        """
        import json
        
        commandDict = {
            "jsonrpc": "2.0",
            "method": command,
            "params": params,
        }
        cmd = json.dumps(commandDict) + '\n'
        if self.qsock is not None:
            self.qsock.write(cmd.encode('utf8', 'backslashreplace'))
        else:
            self.queue.append(cmd)
    

def createDebuggerInterfacePython2(debugServer, passive):
    """
    Module function to create a debugger interface instance.
    
        
    @param debugServer reference to the debug server
    @type DebugServer
    @param passive flag indicating passive connection mode
    @type bool
    @return instantiated debugger interface
    @rtype DebuggerInterfacePython
    """
    return DebuggerInterfacePython2(debugServer, passive)


def getRegistryData():
    """
    Module function to get characterizing data for the debugger interface.
    
    @return tuple containing  client type, client capabilities, client file
        type associations and reference to creation function
    @rtype tuple of (str, int, list of str, function)
    """
    exts = []
    for ext in Preferences.getDebugger("PythonExtensions").split():
        if ext.startswith("."):
            exts.append(ext)
        else:
            exts.append(".{0}".format(ext))
    
    if exts and Preferences.getDebugger("PythonInterpreter"):
        return ["Python2", ClientDefaultCapabilities, exts,
                createDebuggerInterfacePython2]
    else:
        return ["", 0, [], None]
