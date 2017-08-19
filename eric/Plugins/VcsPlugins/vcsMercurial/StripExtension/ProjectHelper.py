# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the strip extension project helper.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QMenu

from E5Gui.E5Action import E5Action
from E5Gui import E5MessageBox

from ..HgExtensionProjectHelper import HgExtensionProjectHelper

import UI.PixmapCache


class StripProjectHelper(HgExtensionProjectHelper):
    """
    Class implementing the strip extension project helper.
    """
    def __init__(self):
        """
        Constructor
        """
        super(StripProjectHelper, self).__init__()
    
    def initActions(self):
        """
        Public method to generate the action objects.
        """
        self.hgStripAct = E5Action(
            self.tr('Strip changesets'),
            UI.PixmapCache.getIcon("fileDelete.png"),
            self.tr('Strip changesets'),
            0, 0, self, 'mercurial_strip')
        self.hgStripAct.setStatusTip(self.tr(
            'Strip changesets from a repository'
        ))
        self.hgStripAct.setWhatsThis(self.tr(
            """<b>Strip changesets</b>"""
            """<p>This deletes a changeset and all its descendants"""
            """ from a repository. Each removed changeset will be"""
            """ stored in .hg/strip-backup as a bundle file.</p>"""
        ))
        self.hgStripAct.triggered.connect(self.__hgStrip)
        self.actions.append(self.hgStripAct)
    
    def initMenu(self, mainMenu):
        """
        Public method to generate the extension menu.
        
        @param mainMenu reference to the main menu
        @type QMenu
        @return populated menu (QMenu)
        """
        menu = QMenu(self.menuTitle(), mainMenu)
        menu.setIcon(UI.PixmapCache.getIcon("fileDelete.png"))
        menu.setTearOffEnabled(True)
        
        menu.addAction(self.hgStripAct)
        
        return menu
    
    def menuTitle(self):
        """
        Public method to get the menu title.
        
        @return title of the menu
        @rtype str
        """
        return self.tr("Strip")
    
    def __hgStrip(self):
        """
        Private slot used to strip revisions from a repository.
        """
        shouldReopen = self.vcs.getExtensionObject("strip")\
            .hgStrip(self.project.getProjectPath())
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Strip"),
                self.tr("""The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                self.project.reopenProject()
