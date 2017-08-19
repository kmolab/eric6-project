#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Eric6 Web Browser.

This is the main Python script that performs the necessary initialization
of the web browser and starts the Qt event loop. This is a standalone version
of the integrated web browser. It is based on QtWebEngine.
"""

from __future__ import unicode_literals

import Toolbox.PyQt4ImportHook  # __IGNORE_WARNING__

try:  # Only for Py2
    import Globals.compatibility_fixes     # __IGNORE_WARNING__
except (ImportError):
    pass

try:
    import sip
    sip.setdestroyonexit(False)
except AttributeError:
    pass

import sys
import os

from Globals import qVersionTuple


if qVersionTuple() < (5, 6, 0):
    from PyQt5.QtCore import QTimer
    from PyQt5.QtWidgets import QApplication
    from E5Gui import E5MessageBox
    app = QApplication([])
    QTimer.singleShot(0, lambda: E5MessageBox.critical(
        None,
        "eric6 Web Browser",
        "You need at least Qt Version 5.6.0 to execute the web browser.")
    )
    app.exec_()
    sys.exit(100)

SettingsDir = None

for arg in sys.argv[:]:
    if arg.startswith("--config="):
        import Globals
        configDir = arg.replace("--config=", "")
        Globals.setConfigDir(configDir)
        sys.argv.remove(arg)
    elif arg.startswith("--settings="):
        from PyQt5.QtCore import QSettings
        SettingsDir = os.path.expanduser(arg.replace("--settings=", ""))
        if not os.path.isdir(SettingsDir):
            os.makedirs(SettingsDir)
        QSettings.setPath(QSettings.IniFormat, QSettings.UserScope,
                          SettingsDir)
        sys.argv.remove(arg)

# make ThirdParty package available as a packages repository
sys.path.insert(2, os.path.join(os.path.dirname(__file__),
                                "ThirdParty", "Pygments"))

try:
    from PyQt5 import QtWebEngineWidgets    # __IGNORE_WARNING__
except ImportError:
    from PyQt5.QtCore import QTimer
    from PyQt5.QtWidgets import QApplication
    from E5Gui import E5MessageBox          # __IGNORE_WARNING__
    app = QApplication([])
    QTimer.singleShot(0, lambda: E5MessageBox.critical(
        None,
        "eric6 Web Browser",
        "QtWebEngineWidgets is not installed but needed to execute the"
        " web browser."))
    app.exec_()
    sys.exit(100)

import Globals
from Globals import AppInfo

from Toolbox import Startup


def createMainWidget(argv):
    """
    Function to create the main widget.
    
    @param argv list of commandline parameters (list of strings)
    @return reference to the main widget (QWidget)
    """
    from WebBrowser.WebBrowserWindow import WebBrowserWindow
    
    searchWord = None
    private = False
    qthelp = False
    
    for arg in reversed(argv):
        if arg.startswith("--search="):
            searchWord = argv[1].split("=", 1)[1]
            argv.remove(arg)
        elif arg == "--private":
            private = True
            argv.remove(arg)
        elif arg == "--qthelp":
            qthelp = True
            argv.remove(arg)
        elif arg.startswith("--"):
            argv.remove(arg)
    
    try:
        home = argv[1]
    except IndexError:
        home = ""
    
    browser = WebBrowserWindow(home, '.', None, 'web_browser',
                               searchWord=searchWord, private=private,
                               settingsDir=SettingsDir, qthelp=qthelp)
    return browser


def main():
    """
    Main entry point into the application.
    """
    options = [
        ("--config=configDir",
         "use the given directory as the one containing the config files"),
        ("--private", "start the browser in private browsing mode"),
        ("--qthelp", "start the browser with support for QtHelp"),
        ("--search=word", "search for the given word"),
        ("--settings=settingsDir",
         "use the given directory to store the settings files"),
    ]
    appinfo = AppInfo.makeAppInfo(sys.argv,
                                  "eric6 Web Browser",
                                  "file",
                                  "web browser",
                                  options)
    
    if not Globals.checkBlacklistedVersions():
        sys.exit(100)
    
    res = Startup.simpleAppStartup(sys.argv,
                                   appinfo,
                                   createMainWidget,
                                   installErrorHandler=True)
    sys.exit(res)

if __name__ == '__main__':
    main()
