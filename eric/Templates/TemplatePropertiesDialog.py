# -*- coding: utf-8 -*-

# Copyright (c) 2005 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the templates properties dialog.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QRegExp, Qt, pyqtSlot
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from .Ui_TemplatePropertiesDialog import Ui_TemplatePropertiesDialog

from E5Gui import E5MessageBox

import Preferences


class TemplatePropertiesDialog(QDialog, Ui_TemplatePropertiesDialog):
    """
    Class implementing the templates properties dialog.
    """
    def __init__(self, parent, groupMode=False, itm=None):
        """
        Constructor
        
        @param parent the parent widget (QWidget)
        @param groupMode flag indicating group mode (boolean)
        @param itm item (TemplateEntry or TemplateGroup) to
            read the data from
        """
        super(TemplatePropertiesDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.templateEdit.setFont(Preferences.getTemplates("EditorFont"))
        
        if not groupMode:
            self.nameEdit.setWhatsThis(self.tr(
                """<b>Template name<b><p>Enter the name of the template."""
                """ Templates may be autocompleted upon this name."""
                """ In order to support autocompletion. the template name"""
                """ must only consist of letters (a-z and A-Z),"""
                """ digits (0-9) and underscores (_).</p>"""
            ))
            self.__nameValidator = QRegExpValidator(QRegExp("[a-zA-Z0-9_]+"),
                                                    self.nameEdit)
            self.nameEdit.setValidator(self.__nameValidator)
        
        import QScintilla.Lexers
        self.languages = [("All", self.tr("All"))]
        supportedLanguages = QScintilla.Lexers.getSupportedLanguages()
        languages = sorted(supportedLanguages.keys())
        for language in languages:
            self.languages.append((language, supportedLanguages[language][0]))
        
        self.groupMode = groupMode
        if groupMode:
            self.groupLabel.setText(self.tr("Language:"))
            for lang, langDisp in self.languages:
                self.groupCombo.addItem(
                    QScintilla.Lexers.getLanguageIcon(lang, False),
                    langDisp)
            self.templateLabel.setEnabled(False)
            self.templateEdit.setEnabled(False)
            self.templateEdit.setPlainText(self.tr("GROUP"))
            self.helpButton.setEnabled(False)
            self.descriptionLabel.hide()
            self.descriptionEdit.hide()
        else:
            groups = []
            for group in parent.getGroupNames():
                groups.append(group)
            self.groupCombo.addItems(groups)
        
        if itm is not None:
            self.nameEdit.setText(itm.getName())
            if groupMode:
                language = itm.getLanguage()
                for lang, langDisp in self.languages:
                    if language == lang:
                        self.setSelectedGroup(langDisp)
                        break
            else:
                self.setSelectedGroup(itm.getGroupName())
                self.templateEdit.setPlainText(itm.getTemplateText())
                self.descriptionEdit.setText(itm.getDescription())
            
            self.nameEdit.selectAll()
        
        self.__helpDialog = None

    def keyPressEvent(self, ev):
        """
        Protected method to handle the user pressing the escape key.
        
        @param ev key event (QKeyEvent)
        """
        if ev.key() == Qt.Key_Escape:
            res = E5MessageBox.yesNo(
                self,
                self.tr("Close dialog"),
                self.tr("""Do you really want to close the dialog?"""))
            if not res:
                self.reject()
    
    @pyqtSlot()
    def on_helpButton_clicked(self):
        """
        Private slot to show some help.
        """
        if self.__helpDialog is None:
            from E5Gui.E5SimpleHelpDialog import E5SimpleHelpDialog
            self.__helpDialog = E5SimpleHelpDialog(
                title=self.tr("Template Help"),
                label=self.tr("<b>Template Help</b>"),
                helpStr=self.tr(
                    """<p>To use variables in a template, you just have to"""
                    """ enclose the variable name with $-characters. When"""
                    """ you use the template, you will then be asked for a"""
                    """ value for this variable.</p>"""
                    """<p>Example template: This is a $VAR$</p>"""
                    """<p>When you use this template you will be prompted"""
                    """ for a value for the variable $VAR$. Any occurrences"""
                    """ of $VAR$ will then be replaced with whatever you've"""
                    """ entered.</p>"""
                    """<p>If you need a single $-character in a template,"""
                    """ which is not used to enclose a variable, type"""
                    """ $$(two dollar characters) instead. They will"""
                    """ automatically be replaced with a single $-character"""
                    """ when you use the template.</p>"""
                    """<p>If you want a variables contents to be treated"""
                    """ specially, the variable name must be followed by a"""
                    """ ':' and one formatting specifier (e.g. $VAR:ml$)."""
                    """ The supported specifiers are:"""
                    """<table>"""
                    """<tr><td>ml</td><td>Specifies a multiline formatting."""
                    """ The first line of the variable contents is prefixed"""
                    """ with the string occurring before the variable on"""
                    """ the same line of the template. All other lines are"""
                    """ prefixed by the same amount of whitespace as the"""
                    """ line containing the variable."""
                    """</td></tr>"""
                    """<tr><td>rl</td><td>Specifies a repeated line"""
                    """ formatting. Each line of the variable contents is"""
                    """ prefixed with the string occurring before the"""
                    """ variable on the same line of the template."""
                    """</td></tr>"""
                    """</table></p>"""
                    """<p>The following predefined variables may be used"""
                    """ in a template:"""
                    """<table>"""
                    """<tr><td>date</td>"""
                    """<td>today's date in ISO format (YYYY-MM-DD)</td></tr>"""
                    """<tr><td>year</td>"""
                    """<td>the current year</td></tr>"""
                    """<tr><td>time</td>"""
                    """<td>current time in ISO format (hh:mm:ss)</td></tr>"""
                    """<tr><td>project_name</td>"""
                    """<td>the name of the project (if any)</td></tr>"""
                    """<tr><td>project_path</td>"""
                    """<td>the path of the project (if any)</td></tr>"""
                    """<tr><td>path_name</td>"""
                    """<td>full path of the current file</td></tr>"""
                    """<tr><td>path_name_rel</td>"""
                    """<td>project relative path of the current file</td>"""
                    """</tr>"""
                    """<tr><td>dir_name</td>"""
                    """<td>full path of the current file's directory</td>"""
                    """</tr>"""
                    """<tr><td>dir_name_rel</td>"""
                    """<td>project relative path of the current file's"""
                    """ directory</td></tr>"""
                    """<tr><td>file_name</td>"""
                    """<td>the current file's name (without directory)"""
                    """</td></tr>"""
                    """<tr><td>base_name</td>"""
                    """<td>like <i>file_name</i>, but without extension"""
                    """</td></tr>"""
                    """<tr><td>ext</td>"""
                    """<td>the extension of the current file</td></tr>"""
                    """<tr><td>cur_select</td>"""
                    """<td>the currently selected text</td></tr>"""
                    """<tr><td>insertion</td>"""
                    """<td>Sets insertion point for cursor after template is"""
                    """ inserted.</td>"""
                    """</tr>"""
                    """<tr><td>select_start</td>"""
                    """<td>Sets span of selected text in template after"""
                    """ template is inserted (used together with"""
                    """ 'select_end').</td></tr>"""
                    """<tr><td>select_end</td>"""
                    """<td>Sets span of selected text in template after"""
                    """ template is inserted (used together with"""
                    """ 'select_start')."""
                    """</td></tr>"""
                    """<tr><td>clipboard</td>"""
                    """<td>the text of the clipboard</td></tr>"""
                    """</table></p>"""
                    """<p>If you want to change the default delimiter to"""
                    """ anything different, please use the configuration"""
                    """ dialog to do so.</p>"""
                ),
                parent=self)
        self.__helpDialog.show()
        
    def setSelectedGroup(self, name):
        """
        Public method to select a group.
        
        @param name name of the group to be selected (string)
        """
        index = self.groupCombo.findText(name)
        self.groupCombo.setCurrentIndex(index)

    def getData(self):
        """
        Public method to get the data entered into the dialog.
        
        @return a tuple of two strings (name, language), if the dialog is in
            group mode, and a tuple of four strings (name, description, group
            name, template) otherwise.
        """
        if self.groupMode:
            return (self.nameEdit.text(),
                    self.languages[self.groupCombo.currentIndex()][0]
                    )
        else:
            return (self.nameEdit.text(),
                    self.descriptionEdit.text(),
                    self.groupCombo.currentText(),
                    self.templateEdit.toPlainText()
                    )
