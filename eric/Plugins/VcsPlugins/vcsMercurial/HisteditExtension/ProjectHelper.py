# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the histedit extension project helper.
"""

from __future__ import unicode_literals

from PyQt5.QtWidgets import QMenu

from E5Gui.E5Action import E5Action
from E5Gui import E5MessageBox

from ..HgExtensionProjectHelper import HgExtensionProjectHelper

import UI.PixmapCache


class HisteditProjectHelper(HgExtensionProjectHelper):
    """
    Class implementing the histedit extension project helper.
    """
    def __init__(self):
        """
        Constructor
        """
        super(HisteditProjectHelper, self).__init__()
    
    def initActions(self):
        """
        Public method to generate the action objects.
        """
        self.hgHisteditStartAct = E5Action(
            self.tr('Start'),
            UI.PixmapCache.getIcon("vcsEditHistory.png"),
            self.tr('Start'),
            0, 0, self, 'mercurial_histedit_start')
        self.hgHisteditStartAct.setStatusTip(self.tr(
            'Start a new changeset history editing session'
        ))
        self.hgHisteditStartAct.setWhatsThis(self.tr(
            """<b>Start</b>"""
            """<p>This starts a new history editing session. A dialog"""
            """ will be presented to modify the edit plan.</p>"""
        ))
        self.hgHisteditStartAct.triggered.connect(self.__hgHisteditStart)
        self.actions.append(self.hgHisteditStartAct)
        
        self.hgHisteditContinueAct = E5Action(
            self.tr('Continue'),
            self.tr('Continue'),
            0, 0, self, 'mercurial_histedit_continue')
        self.hgHisteditContinueAct.setStatusTip(self.tr(
            'Continue an interrupted changeset history editing session'
        ))
        self.hgHisteditContinueAct.setWhatsThis(self.tr(
            """<b>Continue</b>"""
            """<p>This continues an interrupted history editing session.</p>"""
        ))
        self.hgHisteditContinueAct.triggered.connect(self.__hgHisteditContinue)
        self.actions.append(self.hgHisteditContinueAct)
        
        self.hgHisteditAbortAct = E5Action(
            self.tr('Abort'),
            self.tr('Abort'),
            0, 0, self, 'mercurial_histedit_abort')
        self.hgHisteditAbortAct.setStatusTip(self.tr(
            'Abort an interrupted changeset history editing session'
        ))
        self.hgHisteditAbortAct.setWhatsThis(self.tr(
            """<b>Abort</b>"""
            """<p>This aborts an interrupted history editing session.</p>"""
        ))
        self.hgHisteditAbortAct.triggered.connect(self.__hgHisteditAbort)
        self.actions.append(self.hgHisteditAbortAct)
        
        self.hgHisteditEditPlanAct = E5Action(
            self.tr('Edit Plan'),
            self.tr('Edit Plan'),
            0, 0, self, 'mercurial_histedit_edit_plan')
        self.hgHisteditEditPlanAct.setStatusTip(self.tr(
            'Edit the remaining actions list'
        ))
        self.hgHisteditEditPlanAct.setWhatsThis(self.tr(
            """<b>Edit Plan</b>"""
            """<p>This opens an editor to edit the remaining actions list"""
            """ of an interrupted history editing session.</p>"""
        ))
        self.hgHisteditEditPlanAct.triggered.connect(self.__hgHisteditEditPlan)
        self.actions.append(self.hgHisteditEditPlanAct)
    
    def initMenu(self, mainMenu):
        """
        Public method to generate the extension menu.
        
        @param mainMenu reference to the main menu
        @type QMenu
        @return populated menu (QMenu)
        """
        menu = QMenu(self.menuTitle(), mainMenu)
        menu.setIcon(UI.PixmapCache.getIcon("vcsEditHistory.png"))
        menu.setTearOffEnabled(True)
        
        menu.addAction(self.hgHisteditStartAct)
        menu.addSeparator()
        menu.addAction(self.hgHisteditContinueAct)
        menu.addAction(self.hgHisteditAbortAct)
        menu.addSeparator()
        menu.addAction(self.hgHisteditEditPlanAct)
        
        return menu
    
    def menuTitle(self):
        """
        Public method to get the menu title.
        
        @return title of the menu
        @rtype str
        """
        return self.tr("Edit History")
    
    def __hgHisteditStart(self):
        """
        Private slot used to start a history editing session.
        """
        shouldReopen = self.vcs.getExtensionObject("histedit")\
            .hgHisteditStart(self.project.getProjectPath())
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Start History Editing"),
                self.tr("""The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                self.project.reopenProject()
    
    def __hgHisteditContinue(self):
        """
        Private slot used to continue an interrupted history editing session.
        """
        shouldReopen = self.vcs.getExtensionObject("histedit")\
            .hgHisteditContinue(self.project.getProjectPath())
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Continue History Editing"),
                self.tr("""The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                self.project.reopenProject()
    
    def __hgHisteditAbort(self):
        """
        Private slot used to abort an interrupted history editing session.
        """
        shouldReopen = self.vcs.getExtensionObject("histedit")\
            .hgHisteditAbort(self.project.getProjectPath())
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Abort History Editing"),
                self.tr("""The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                self.project.reopenProject()
    
    def __hgHisteditEditPlan(self):
        """
        Private slot used to edit the remaining actions list of an interrupted
        history editing session.
        """
        shouldReopen = self.vcs.getExtensionObject("histedit")\
            .hgHisteditEditPlan(self.project.getProjectPath())
        if shouldReopen:
            res = E5MessageBox.yesNo(
                None,
                self.tr("Edit Plan"),
                self.tr("""The project should be reread. Do this now?"""),
                yesDefault=True)
            if res:
                self.project.reopenProject()
