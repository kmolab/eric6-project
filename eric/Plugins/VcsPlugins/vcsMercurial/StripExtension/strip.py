# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the strip extension interface.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtWidgets import QDialog

from ..HgExtension import HgExtension
from ..HgDialog import HgDialog


class Strip(HgExtension):
    """
    Class implementing the strip extension interface.
    """
    def __init__(self, vcs):
        """
        Constructor
        
        @param vcs reference to the Mercurial vcs object
        @type Hg
        """
        super(Strip, self).__init__(vcs)
    
    def hgStrip(self, name, rev=""):
        """
        Public method to strip revisions from a repository.
        
        @param name file/directory name
        @type str
        @keyparam rev revision to strip from
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
        
        from .HgStripDialog import HgStripDialog
        res = False
        dlg = HgStripDialog(self.vcs.hgGetTagsList(repodir),
                            self.vcs.hgGetBranchesList(repodir),
                            self.vcs.hgGetBookmarksList(repodir),
                            rev)
        if dlg.exec_() == QDialog.Accepted:
            rev, bookmark, force, noBackup, keep = dlg.getData()
            
            args = self.vcs.initCommand("strip")
            if bookmark:
                args.append("--bookmark")
                args.append(bookmark)
            if force:
                args.append("--force")
            if noBackup:
                args.append("--no-backup")
            if keep:
                args.append("--keep")
            args.append("-v")
            args.append(rev)
            
            dia = HgDialog(
                self.tr("Stripping changesets from repository"),
                self.vcs)
            res = dia.startProcess(args, repodir)
            if res:
                dia.exec_()
                res = dia.hasAddOrDelete()
                self.vcs.checkVCSStatus()
        return res
