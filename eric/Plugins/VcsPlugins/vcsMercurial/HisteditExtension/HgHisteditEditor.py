#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the main script for histedit.

Depending on the file name given by the Mercurial histedit command one
of two possible dialogs will be shown.
"""

from __future__ import unicode_literals

import sys
import os

sys.path.insert(1, os.path.join(
    os.path.dirname(__file__), "..", "..", "..", ".."))
# four times up is the eric6 package directory

import Toolbox.PyQt4ImportHook  # __IGNORE_WARNING__

try:  # Only for Py2
    import Globals.compatibility_fixes     # __IGNORE_WARNING__
except (ImportError):
    pass

for arg in sys.argv[:]:
    if arg.startswith("--config="):
        import Globals
        configDir = arg.replace("--config=", "")
        Globals.setConfigDir(configDir)
        sys.argv.remove(arg)
    elif arg.startswith("--settings="):
        from PyQt5.QtCore import QSettings
        settingsDir = os.path.expanduser(arg.replace("--settings=", ""))
        if not os.path.isdir(settingsDir):
            os.makedirs(settingsDir)
        QSettings.setPath(QSettings.IniFormat, QSettings.UserScope,
                          settingsDir)
        sys.argv.remove(arg)

from Globals import AppInfo

from Toolbox import Startup


def createMainWidget(argv):
    """
    Function to create the main widget.
    
    @param argv list of commandline parameters
    @type list of str
    @return reference to the main widget or None in case of an error
    @rtype QWidget or None
    """
    if len(argv) > 1:
        fileName = os.path.basename(argv[1])
        if fileName.startswith("hg-histedit-"):
            from HgHisteditPlanEditor import HgHisteditPlanEditor
            return HgHisteditPlanEditor(argv[1])
        elif fileName.startswith("hg-editor-"):
            from HgHisteditCommitEditor import HgHisteditCommitEditor
            return HgHisteditCommitEditor(argv[1])
    
    return None


def main():
    """
    Main entry point into the application.
    """
    options = [
        ("--config=configDir",
         "use the given directory as the one containing the config files"),
        ("--settings=settingsDir",
         "use the given directory to store the settings files"),
        ("", "name of file to edit")
    ]
    appinfo = AppInfo.makeAppInfo(sys.argv,
                                  "Mercurial Histedit Editor",
                                  "",
                                  "Editor for the Mercurial histedit command",
                                  options)
    res = Startup.simpleAppStartup(sys.argv,
                                   appinfo,
                                   createMainWidget)
    sys.exit(res)

if __name__ == '__main__':
    main()
