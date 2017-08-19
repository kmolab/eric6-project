# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the histedit extension interface.
"""

from __future__ import unicode_literals

import os
import sys

from PyQt5.QtWidgets import QDialog

from ..HgExtension import HgExtension
from ..HgDialog import HgDialog


class Histedit(HgExtension):
    """
    Class implementing the histedit extension interface.
    """
    def __init__(self, vcs):
        """
        Constructor
        
        @param vcs reference to the Mercurial vcs object
        @type Hg
        """
        super(Histedit, self).__init__(vcs)
    
    def hgHisteditStart(self, name, rev=""):
        """
        Public method to start a histedit session.
        
        @param name file/directory name
        @type str
        @keyparam rev revision to start histedit at
        @type str
        @return flag indicating that the project should be reread
        @rtype bool
        """
        # find the root of the repo
        repodir = self.vcs.splitPath(name)[0]
        while not os.path.isdir(os.path.join(repodir, self.vcs.adminDir)):
            repodir = os.path.dirname(repodir)
            if os.path.splitdrive(repodir)[1] == os.sep:
                return False
        
        from .HgHisteditConfigDialog import HgHisteditConfigDialog
        res = False
        dlg = HgHisteditConfigDialog(self.vcs.hgGetTagsList(repodir),
                                     self.vcs.hgGetBranchesList(repodir),
                                     self.vcs.hgGetBookmarksList(repodir),
                                     rev)
        if dlg.exec_() == QDialog.Accepted:
            rev, force, keep = dlg.getData()
            
            args = self.vcs.initCommand("histedit")
            args.append("-v")
            if keep:
                args.append("--keep")
            if rev:
                if rev == "--outgoing":
                    if force:
                        args.append("--force")
                else:
                    args.append("--rev")
                args.append(rev)
            
            editor = os.path.join(
                os.path.dirname(__file__), "HgHisteditEditor.py")
            env = {"HGEDITOR": "{0} {1}".format(sys.executable, editor)}
            
            dia = HgDialog(
                self.tr("Starting histedit session"),
                self.vcs,
                useClient=False)
            res = dia.startProcess(args, repodir, environment=env)
            if res:
                dia.exec_()
                res = dia.hasAddOrDelete()
                self.vcs.checkVCSStatus()
        return res
    
    def hgHisteditContinue(self, name):
        """
        Public method to continue an interrupted histedit session.
        
        @param name file/directory name
        @type str
        @return flag indicating that the project should be reread
        @rtype bool
        """
        # find the root of the repo
        repodir = self.vcs.splitPath(name)[0]
        while not os.path.isdir(os.path.join(repodir, self.vcs.adminDir)):
            repodir = os.path.dirname(repodir)
            if os.path.splitdrive(repodir)[1] == os.sep:
                return False
        
        args = self.vcs.initCommand("histedit")
        args.append("--continue")
        args.append("-v")
        
        editor = os.path.join(
            os.path.dirname(__file__), "HgHisteditEditor.py")
        env = {"HGEDITOR": "{0} {1}".format(sys.executable, editor)}
        
        dia = HgDialog(
            self.tr("Continue histedit session"),
            self.vcs,
            useClient=False)
        res = dia.startProcess(args, repodir, environment=env)
        if res:
            dia.exec_()
            res = dia.hasAddOrDelete()
            self.vcs.checkVCSStatus()
        return res
    
    def hgHisteditAbort(self, name):
        """
        Public method to abort an interrupted histedit session.
        
        @param name file/directory name
        @type str
        @return flag indicating that the project should be reread
        @rtype bool
        """
        # find the root of the repo
        repodir = self.vcs.splitPath(name)[0]
        while not os.path.isdir(os.path.join(repodir, self.vcs.adminDir)):
            repodir = os.path.dirname(repodir)
            if os.path.splitdrive(repodir)[1] == os.sep:
                return False
        
        args = self.vcs.initCommand("histedit")
        args.append("--abort")
        args.append("-v")
        
        editor = os.path.join(
            os.path.dirname(__file__), "HgHisteditEditor.py")
        env = {"HGEDITOR": "{0} {1}".format(sys.executable, editor)}
        
        dia = HgDialog(
            self.tr("Abort histedit session"),
            self.vcs,
            useClient=False)
        res = dia.startProcess(args, repodir, environment=env)
        if res:
            dia.exec_()
            res = dia.hasAddOrDelete()
            self.vcs.checkVCSStatus()
        return res
    
    def hgHisteditEditPlan(self, name):
        """
        Public method to edit the remaining actions list of an interrupted
        histedit session.
        
        @param name file/directory name
        @type str
        @return flag indicating that the project should be reread
        @rtype bool
        """
        # find the root of the repo
        repodir = self.vcs.splitPath(name)[0]
        while not os.path.isdir(os.path.join(repodir, self.vcs.adminDir)):
            repodir = os.path.dirname(repodir)
            if os.path.splitdrive(repodir)[1] == os.sep:
                return False
        
        args = self.vcs.initCommand("histedit")
        args.append("--edit-plan")
        args.append("-v")
        
        editor = os.path.join(
            os.path.dirname(__file__), "HgHisteditEditor.py")
        env = {"HGEDITOR": "{0} {1}".format(sys.executable, editor)}
        
        dia = HgDialog(
            self.tr("Edit Plan"),
            self.vcs,
            useClient=False)
        res = dia.startProcess(args, repodir, environment=env)
        if res:
            dia.exec_()
            res = dia.hasAddOrDelete()
            self.vcs.checkVCSStatus()
        return res
