# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\WizardPlugins\QRegExpWizard\QRegExpWizardDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QRegExpWizardWidget(object):
    def setupUi(self, QRegExpWizardWidget):
        QRegExpWizardWidget.setObjectName("QRegExpWizardWidget")
        QRegExpWizardWidget.resize(749, 600)
        QRegExpWizardWidget.setProperty("sizeGripEnabled", True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QRegExpWizardWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.variableLabel = QtWidgets.QLabel(QRegExpWizardWidget)
        self.variableLabel.setObjectName("variableLabel")
        self.hboxlayout.addWidget(self.variableLabel)
        self.variableLineEdit = QtWidgets.QLineEdit(QRegExpWizardWidget)
        self.variableLineEdit.setObjectName("variableLineEdit")
        self.hboxlayout.addWidget(self.variableLineEdit)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.variableLine = QtWidgets.QFrame(QRegExpWizardWidget)
        self.variableLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.variableLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.variableLine.setObjectName("variableLine")
        self.verticalLayout.addWidget(self.variableLine)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(QRegExpWizardWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.syntaxCombo = QtWidgets.QComboBox(QRegExpWizardWidget)
        self.syntaxCombo.setObjectName("syntaxCombo")
        self.horizontalLayout_3.addWidget(self.syntaxCombo)
        spacerItem = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.undoButton = QtWidgets.QToolButton(QRegExpWizardWidget)
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout_3.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QToolButton(QRegExpWizardWidget)
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout_3.addWidget(self.redoButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.regexpButtonsFrame = QtWidgets.QFrame(QRegExpWizardWidget)
        self.regexpButtonsFrame.setObjectName("regexpButtonsFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.regexpButtonsFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.charButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.charButton.setObjectName("charButton")
        self.horizontalLayout.addWidget(self.charButton)
        self.anycharButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.anycharButton.setObjectName("anycharButton")
        self.horizontalLayout.addWidget(self.anycharButton)
        self.repeatButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.repeatButton.setObjectName("repeatButton")
        self.horizontalLayout.addWidget(self.repeatButton)
        self.nonGroupButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.nonGroupButton.setObjectName("nonGroupButton")
        self.horizontalLayout.addWidget(self.nonGroupButton)
        self.groupButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.groupButton.setObjectName("groupButton")
        self.horizontalLayout.addWidget(self.groupButton)
        self.altnButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.altnButton.setObjectName("altnButton")
        self.horizontalLayout.addWidget(self.altnButton)
        self.beglineButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.beglineButton.setObjectName("beglineButton")
        self.horizontalLayout.addWidget(self.beglineButton)
        self.endlineButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.endlineButton.setObjectName("endlineButton")
        self.horizontalLayout.addWidget(self.endlineButton)
        self.wordboundButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.wordboundButton.setObjectName("wordboundButton")
        self.horizontalLayout.addWidget(self.wordboundButton)
        self.nonwordboundButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.nonwordboundButton.setObjectName("nonwordboundButton")
        self.horizontalLayout.addWidget(self.nonwordboundButton)
        self.poslookaheadButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.poslookaheadButton.setObjectName("poslookaheadButton")
        self.horizontalLayout.addWidget(self.poslookaheadButton)
        self.neglookaheadButton = QtWidgets.QToolButton(self.regexpButtonsFrame)
        self.neglookaheadButton.setObjectName("neglookaheadButton")
        self.horizontalLayout.addWidget(self.neglookaheadButton)
        spacerItem2 = QtWidgets.QSpacerItem(356, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.regexpButtonsFrame)
        self.wildcardButtonsFrame = QtWidgets.QFrame(QRegExpWizardWidget)
        self.wildcardButtonsFrame.setObjectName("wildcardButtonsFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wildcardButtonsFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wildcardCharButton = QtWidgets.QToolButton(self.wildcardButtonsFrame)
        self.wildcardCharButton.setObjectName("wildcardCharButton")
        self.horizontalLayout_2.addWidget(self.wildcardCharButton)
        self.wildcardAnycharButton = QtWidgets.QToolButton(self.wildcardButtonsFrame)
        self.wildcardAnycharButton.setObjectName("wildcardAnycharButton")
        self.horizontalLayout_2.addWidget(self.wildcardAnycharButton)
        self.wildcardRepeatButton = QtWidgets.QToolButton(self.wildcardButtonsFrame)
        self.wildcardRepeatButton.setObjectName("wildcardRepeatButton")
        self.horizontalLayout_2.addWidget(self.wildcardRepeatButton)
        spacerItem3 = QtWidgets.QSpacerItem(635, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.wildcardButtonsFrame)
        self.w3cButtonsFrame = QtWidgets.QFrame(QRegExpWizardWidget)
        self.w3cButtonsFrame.setObjectName("w3cButtonsFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.w3cButtonsFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.w3cCharButton = QtWidgets.QToolButton(self.w3cButtonsFrame)
        self.w3cCharButton.setObjectName("w3cCharButton")
        self.horizontalLayout_4.addWidget(self.w3cCharButton)
        self.w3cAnycharButton = QtWidgets.QToolButton(self.w3cButtonsFrame)
        self.w3cAnycharButton.setObjectName("w3cAnycharButton")
        self.horizontalLayout_4.addWidget(self.w3cAnycharButton)
        self.w3cRepeatButton = QtWidgets.QToolButton(self.w3cButtonsFrame)
        self.w3cRepeatButton.setObjectName("w3cRepeatButton")
        self.horizontalLayout_4.addWidget(self.w3cRepeatButton)
        self.w3cGroupButton = QtWidgets.QToolButton(self.w3cButtonsFrame)
        self.w3cGroupButton.setObjectName("w3cGroupButton")
        self.horizontalLayout_4.addWidget(self.w3cGroupButton)
        self.w3cAltnButton = QtWidgets.QToolButton(self.w3cButtonsFrame)
        self.w3cAltnButton.setObjectName("w3cAltnButton")
        self.horizontalLayout_4.addWidget(self.w3cAltnButton)
        spacerItem4 = QtWidgets.QSpacerItem(573, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.w3cButtonsFrame)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtWidgets.QLabel(QRegExpWizardWidget)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(QRegExpWizardWidget)
        self.textLabel2.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.regexpLineEdit = QtWidgets.QLineEdit(QRegExpWizardWidget)
        self.regexpLineEdit.setObjectName("regexpLineEdit")
        self.gridlayout.addWidget(self.regexpLineEdit, 0, 1, 1, 1)
        self.textTextEdit = QtWidgets.QTextEdit(QRegExpWizardWidget)
        self.textTextEdit.setObjectName("textTextEdit")
        self.gridlayout.addWidget(self.textTextEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.caseSensitiveCheckBox = QtWidgets.QCheckBox(QRegExpWizardWidget)
        self.caseSensitiveCheckBox.setChecked(True)
        self.caseSensitiveCheckBox.setObjectName("caseSensitiveCheckBox")
        self.hboxlayout1.addWidget(self.caseSensitiveCheckBox)
        self.minimalCheckBox = QtWidgets.QCheckBox(QRegExpWizardWidget)
        self.minimalCheckBox.setObjectName("minimalCheckBox")
        self.hboxlayout1.addWidget(self.minimalCheckBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.hboxlayout1)
        self.resultTable = QtWidgets.QTableWidget(QRegExpWizardWidget)
        self.resultTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)
        self.verticalLayout.addWidget(self.resultTable)
        self.buttonBox = QtWidgets.QDialogButtonBox(QRegExpWizardWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.variableLabel.setBuddy(self.variableLineEdit)
        self.textLabel1.setBuddy(self.regexpLineEdit)
        self.textLabel2.setBuddy(self.textTextEdit)

        self.retranslateUi(QRegExpWizardWidget)
        self.undoButton.clicked.connect(self.regexpLineEdit.undo)
        self.redoButton.clicked.connect(self.regexpLineEdit.redo)
        QtCore.QMetaObject.connectSlotsByName(QRegExpWizardWidget)
        QRegExpWizardWidget.setTabOrder(self.variableLineEdit, self.syntaxCombo)
        QRegExpWizardWidget.setTabOrder(self.syntaxCombo, self.undoButton)
        QRegExpWizardWidget.setTabOrder(self.undoButton, self.redoButton)
        QRegExpWizardWidget.setTabOrder(self.redoButton, self.charButton)
        QRegExpWizardWidget.setTabOrder(self.charButton, self.anycharButton)
        QRegExpWizardWidget.setTabOrder(self.anycharButton, self.repeatButton)
        QRegExpWizardWidget.setTabOrder(self.repeatButton, self.nonGroupButton)
        QRegExpWizardWidget.setTabOrder(self.nonGroupButton, self.groupButton)
        QRegExpWizardWidget.setTabOrder(self.groupButton, self.altnButton)
        QRegExpWizardWidget.setTabOrder(self.altnButton, self.beglineButton)
        QRegExpWizardWidget.setTabOrder(self.beglineButton, self.endlineButton)
        QRegExpWizardWidget.setTabOrder(self.endlineButton, self.wordboundButton)
        QRegExpWizardWidget.setTabOrder(self.wordboundButton, self.nonwordboundButton)
        QRegExpWizardWidget.setTabOrder(self.nonwordboundButton, self.poslookaheadButton)
        QRegExpWizardWidget.setTabOrder(self.poslookaheadButton, self.neglookaheadButton)
        QRegExpWizardWidget.setTabOrder(self.neglookaheadButton, self.wildcardCharButton)
        QRegExpWizardWidget.setTabOrder(self.wildcardCharButton, self.wildcardAnycharButton)
        QRegExpWizardWidget.setTabOrder(self.wildcardAnycharButton, self.wildcardRepeatButton)
        QRegExpWizardWidget.setTabOrder(self.wildcardRepeatButton, self.w3cCharButton)
        QRegExpWizardWidget.setTabOrder(self.w3cCharButton, self.w3cAnycharButton)
        QRegExpWizardWidget.setTabOrder(self.w3cAnycharButton, self.w3cRepeatButton)
        QRegExpWizardWidget.setTabOrder(self.w3cRepeatButton, self.w3cGroupButton)
        QRegExpWizardWidget.setTabOrder(self.w3cGroupButton, self.w3cAltnButton)
        QRegExpWizardWidget.setTabOrder(self.w3cAltnButton, self.regexpLineEdit)
        QRegExpWizardWidget.setTabOrder(self.regexpLineEdit, self.textTextEdit)
        QRegExpWizardWidget.setTabOrder(self.textTextEdit, self.caseSensitiveCheckBox)
        QRegExpWizardWidget.setTabOrder(self.caseSensitiveCheckBox, self.minimalCheckBox)
        QRegExpWizardWidget.setTabOrder(self.minimalCheckBox, self.resultTable)
        QRegExpWizardWidget.setTabOrder(self.resultTable, self.buttonBox)

    def retranslateUi(self, QRegExpWizardWidget):
        _translate = QtCore.QCoreApplication.translate
        QRegExpWizardWidget.setWindowTitle(_translate("QRegExpWizardWidget", "QRegExp Wizard"))
        self.variableLabel.setText(_translate("QRegExpWizardWidget", "&Variable Name:"))
        self.label.setText(_translate("QRegExpWizardWidget", "Pattern Syntax:"))
        self.syntaxCombo.setToolTip(_translate("QRegExpWizardWidget", "Select the pattern syntax"))
        self.undoButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Undo last edit</b>"))
        self.redoButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Redo last edit</b>"))
        self.charButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog.</p>"))
        self.charButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog. This dialog will help to edit the range of characters and add some specific conditions.</p>"))
        self.anycharButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp.</p>"))
        self.anycharButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp. The dot matches a single character, except line break characters (by default). \n"
"E.g. \'gr.y\' matches \'gray\', \'grey\', \'gr%y\', etc. Use the dot sparingly. Often, a character class or negated\n"
"character class is faster and more precise.</p>"))
        self.repeatButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.repeatButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.nonGroupButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets.</p>"))
        self.nonGroupButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets. It can be used to apply a regexp quantifier (eg. \'?\' or \'+\') to the entire\n"
"group of characters inside the brakets. E.g. the regex \'Set(?:Value)?\' matches \'Set\' or \'SetValue\'. The \'?:\' inside the brakets\n"
"means that the content of the match (called the backreference) is not stored for further use.</p>"))
        self.groupButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets.</p>"))
        self.groupButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets. They can be used to apply a regexp quantifier (e.g. \'?\' or \'+\') to the entire group of \n"
"characters inside the brakets. E.g. the regex \'Set(Value)?\' matches \'Set\' or \'SetValue\'. Contrary to non-capturing parentheses, \n"
"the backreference matched inside the brakets is stored for further use (i.e. \'Value\' in the second example above). \n"
"One can access the backereference with the \'\\1\' expression. </p>\n"
"<p>E.g. \'([a-c])x\\1x\\1\' will match \'axaxa\', \'bxbxb\' and \'cxcxc\'.</p>"))
        self.altnButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. </p>"))
        self.altnButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. The alternation is used to match a single regular expression out of \n"
"several possible regular expressions. E.g. \'cat|dog|mouse|fish\' matches words containing the word \'cat\', \'dog\',\'mouse\' or \'fish\'.\n"
"Be aware that in the above example, the alternatives refer to whole or part of words. If you want to match exactly the\n"
" words \'cat\', \'dog\', ... you should express the fact that you only want to match complete words: \'\\b(cat|dog|mouse|fish)\\b\'</p>"))
        self.beglineButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^).</p>"))
        self.beglineButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^). It is used to find some expressions at the begining of lines.\n"
"E.g. \'^[A-Z]\' match lines starting with a capitalized character. </p>"))
        self.endlineButton.setToolTip(_translate("QRegExpWizardWidget", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($).</p>"))
        self.endlineButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($). It is used to find some expressions at the end of lines.</p>"))
        self.wordboundButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b).</p>"))
        self.wordboundButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b). This character is used to express the fact that word \n"
"must begin or end at this position. E.g. \'\\bcat\\b\' matches exactly the word \'cat\' while \'concatenation\' is ignored.</p>"))
        self.nonwordboundButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b.</p>"))
        self.nonwordboundButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b. \\B matches at every position where \\b \n"
"does not. Effectively, \\B matches at any position between two word characters as well as at any position between two non-word characters.</p>"))
        self.poslookaheadButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets.</p>"))
        self.poslookaheadButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets. Basically, positive lookhead is used to match a character only if followed by another one.\n"
"Writting \'q(?=u)\' means that you want to match the \'q\' character only if it is followed by \'u\'. In this statement \'u\' is a trivial \n"
"regexp which may be replaced by a more complex expression; q(?=[abc])\' will match a \'q\' if followed by either \'a\', \'b\' or \'c\'.</p>"))
        self.neglookaheadButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets.</p>"))
        self.neglookaheadButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets. Basically, negative lookhead is used to match a character only if it is not\n"
"followed by a another one. Writting \'q(?!u)\' means that you want to match \'q\' only if it is not followed by \'u\'. In this statement, \'u\' is a\n"
"trivial regexp which may be replaced by a more complex expression; \'q(?![abc])\' will match a \'q\' if it is followed by anything else than \'a\', \'b\' or \'c\'.</p>"))
        self.wildcardCharButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog.</p>"))
        self.wildcardCharButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog. This dialog will help to edit the range of characters and add some specific conditions.</p>"))
        self.wildcardAnycharButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a question mark (?) in your regexp.</p>"))
        self.wildcardAnycharButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a question mark (?) in your regexp. The question mark matches a single character. \n"
"E.g. \'gr?y\' matches \'gray\', \'grey\', \'gr%y\', etc.</p>"))
        self.wildcardRepeatButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Repeat contents</b>\n"
"<p>Inserts a repetition (*) character into the regexp.</p>"))
        self.wildcardRepeatButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Repeat contents</b>\n"
"<p>Inserts a repetition (*) character into the regexp. That will match zero or more of any character.</p>"))
        self.w3cCharButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog.</p>"))
        self.w3cCharButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog. This dialog will help to edit the range of characters and add some specific conditions.</p>"))
        self.w3cAnycharButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp.</p>"))
        self.w3cAnycharButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp. The dot matches a single character, except line break characters (by default). \n"
"E.g. \'gr.y\' matches \'gray\', \'grey\', \'gr%y\', etc. Use the dot sparingly. Often, a character class or negated\n"
"character class is faster and more precise.</p>"))
        self.w3cRepeatButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.w3cRepeatButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.w3cGroupButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets.</p>"))
        self.w3cGroupButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets. They can be used to apply a regexp quantifier (e.g. \'?\' or \'+\') to the entire group of \n"
"characters inside the brakets. E.g. the regex \'Set(Value)?\' matches \'Set\' or \'SetValue\'.</p>"))
        self.w3cAltnButton.setToolTip(_translate("QRegExpWizardWidget", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. </p>"))
        self.w3cAltnButton.setWhatsThis(_translate("QRegExpWizardWidget", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. The alternation is used to match a single regular expression out of \n"
"several possible regular expressions. E.g. \'cat|dog|mouse|fish\' matches words containing the word \'cat\', \'dog\',\'mouse\' or \'fish\'.</p>"))
        self.textLabel1.setText(_translate("QRegExpWizardWidget", "&Regexp:"))
        self.textLabel2.setText(_translate("QRegExpWizardWidget", "&Text:"))
        self.caseSensitiveCheckBox.setText(_translate("QRegExpWizardWidget", "Case &Sensitive"))
        self.caseSensitiveCheckBox.setShortcut(_translate("QRegExpWizardWidget", "Alt+S"))
        self.minimalCheckBox.setText(_translate("QRegExpWizardWidget", "&Minimal"))
        self.minimalCheckBox.setShortcut(_translate("QRegExpWizardWidget", "Alt+M"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QRegExpWizardWidget = QtWidgets.QWidget()
    ui = Ui_QRegExpWizardWidget()
    ui.setupUi(QRegExpWizardWidget)
    QRegExpWizardWidget.show()
    sys.exit(app.exec_())

