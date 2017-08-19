# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\WizardPlugins\PyRegExpWizard\PyRegExpWizardDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyRegExpWizardDialog(object):
    def setupUi(self, PyRegExpWizardDialog):
        PyRegExpWizardDialog.setObjectName("PyRegExpWizardDialog")
        PyRegExpWizardDialog.resize(750, 700)
        PyRegExpWizardDialog.setProperty("sizeGripEnabled", True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PyRegExpWizardDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.versionGroup = QtWidgets.QGroupBox(PyRegExpWizardDialog)
        self.versionGroup.setObjectName("versionGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.versionGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.py2Button = QtWidgets.QRadioButton(self.versionGroup)
        self.py2Button.setStatusTip("")
        self.py2Button.setChecked(False)
        self.py2Button.setObjectName("py2Button")
        self.horizontalLayout.addWidget(self.py2Button)
        self.py3Button = QtWidgets.QRadioButton(self.versionGroup)
        self.py3Button.setChecked(True)
        self.py3Button.setObjectName("py3Button")
        self.horizontalLayout.addWidget(self.py3Button)
        spacerItem = QtWidgets.QSpacerItem(535, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.versionGroup)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.variableLabel = QtWidgets.QLabel(PyRegExpWizardDialog)
        self.variableLabel.setObjectName("variableLabel")
        self.hboxlayout.addWidget(self.variableLabel)
        self.variableLineEdit = QtWidgets.QLineEdit(PyRegExpWizardDialog)
        self.variableLineEdit.setObjectName("variableLineEdit")
        self.hboxlayout.addWidget(self.variableLineEdit)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.importCheckBox = QtWidgets.QCheckBox(PyRegExpWizardDialog)
        self.importCheckBox.setObjectName("importCheckBox")
        self.verticalLayout.addWidget(self.importCheckBox)
        self.variableLine = QtWidgets.QFrame(PyRegExpWizardDialog)
        self.variableLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.variableLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.variableLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.variableLine.setObjectName("variableLine")
        self.verticalLayout.addWidget(self.variableLine)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.commentButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.commentButton.setObjectName("commentButton")
        self.hboxlayout1.addWidget(self.commentButton)
        self.charButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.charButton.setObjectName("charButton")
        self.hboxlayout1.addWidget(self.charButton)
        self.anycharButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.anycharButton.setObjectName("anycharButton")
        self.hboxlayout1.addWidget(self.anycharButton)
        self.repeatButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.repeatButton.setObjectName("repeatButton")
        self.hboxlayout1.addWidget(self.repeatButton)
        self.nonGroupButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.nonGroupButton.setObjectName("nonGroupButton")
        self.hboxlayout1.addWidget(self.nonGroupButton)
        self.groupButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.groupButton.setObjectName("groupButton")
        self.hboxlayout1.addWidget(self.groupButton)
        self.namedGroupButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.namedGroupButton.setObjectName("namedGroupButton")
        self.hboxlayout1.addWidget(self.namedGroupButton)
        self.namedReferenceButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.namedReferenceButton.setObjectName("namedReferenceButton")
        self.hboxlayout1.addWidget(self.namedReferenceButton)
        self.altnButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.altnButton.setObjectName("altnButton")
        self.hboxlayout1.addWidget(self.altnButton)
        self.beglineButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.beglineButton.setObjectName("beglineButton")
        self.hboxlayout1.addWidget(self.beglineButton)
        self.endlineButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.endlineButton.setObjectName("endlineButton")
        self.hboxlayout1.addWidget(self.endlineButton)
        self.wordboundButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.wordboundButton.setObjectName("wordboundButton")
        self.hboxlayout1.addWidget(self.wordboundButton)
        self.nonwordboundButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.nonwordboundButton.setObjectName("nonwordboundButton")
        self.hboxlayout1.addWidget(self.nonwordboundButton)
        self.poslookaheadButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.poslookaheadButton.setObjectName("poslookaheadButton")
        self.hboxlayout1.addWidget(self.poslookaheadButton)
        self.neglookaheadButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.neglookaheadButton.setObjectName("neglookaheadButton")
        self.hboxlayout1.addWidget(self.neglookaheadButton)
        self.poslookbehindButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.poslookbehindButton.setObjectName("poslookbehindButton")
        self.hboxlayout1.addWidget(self.poslookbehindButton)
        self.neglookbehindButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.neglookbehindButton.setObjectName("neglookbehindButton")
        self.hboxlayout1.addWidget(self.neglookbehindButton)
        spacerItem1 = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.undoButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.undoButton.setObjectName("undoButton")
        self.hboxlayout1.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QToolButton(PyRegExpWizardDialog)
        self.redoButton.setObjectName("redoButton")
        self.hboxlayout1.addWidget(self.redoButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.hboxlayout1)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1 = QtWidgets.QLabel(PyRegExpWizardDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.regexpTextEdit = QtWidgets.QTextEdit(PyRegExpWizardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.regexpTextEdit.sizePolicy().hasHeightForWidth())
        self.regexpTextEdit.setSizePolicy(sizePolicy)
        self.regexpTextEdit.setAcceptRichText(False)
        self.regexpTextEdit.setObjectName("regexpTextEdit")
        self.gridlayout.addWidget(self.regexpTextEdit, 0, 1, 1, 1)
        self.resultTable = QtWidgets.QTableWidget(PyRegExpWizardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.resultTable.sizePolicy().hasHeightForWidth())
        self.resultTable.setSizePolicy(sizePolicy)
        self.resultTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)
        self.gridlayout.addWidget(self.resultTable, 3, 0, 1, 2)
        self.gridlayout1 = QtWidgets.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")
        self.multilineCheckBox = QtWidgets.QCheckBox(PyRegExpWizardDialog)
        self.multilineCheckBox.setObjectName("multilineCheckBox")
        self.gridlayout1.addWidget(self.multilineCheckBox, 0, 1, 1, 1)
        self.unicodeCheckBox = QtWidgets.QCheckBox(PyRegExpWizardDialog)
        self.unicodeCheckBox.setObjectName("unicodeCheckBox")
        self.gridlayout1.addWidget(self.unicodeCheckBox, 1, 2, 1, 1)
        self.verboseCheckBox = QtWidgets.QCheckBox(PyRegExpWizardDialog)
        self.verboseCheckBox.setObjectName("verboseCheckBox")
        self.gridlayout1.addWidget(self.verboseCheckBox, 1, 0, 1, 1)
        self.caseSensitiveCheckBox = QtWidgets.QCheckBox(PyRegExpWizardDialog)
        self.caseSensitiveCheckBox.setChecked(True)
        self.caseSensitiveCheckBox.setObjectName("caseSensitiveCheckBox")
        self.gridlayout1.addWidget(self.caseSensitiveCheckBox, 0, 0, 1, 1)
        self.localeCheckBox = QtWidgets.QCheckBox(PyRegExpWizardDialog)
        self.localeCheckBox.setEnabled(False)
        self.localeCheckBox.setObjectName("localeCheckBox")
        self.gridlayout1.addWidget(self.localeCheckBox, 1, 1, 1, 1)
        self.dotallCheckBox = QtWidgets.QCheckBox(PyRegExpWizardDialog)
        self.dotallCheckBox.setObjectName("dotallCheckBox")
        self.gridlayout1.addWidget(self.dotallCheckBox, 0, 2, 1, 1)
        self.gridlayout.addLayout(self.gridlayout1, 2, 0, 1, 2)
        self.textLabel2 = QtWidgets.QLabel(PyRegExpWizardDialog)
        self.textLabel2.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textTextEdit = QtWidgets.QTextEdit(PyRegExpWizardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textTextEdit.sizePolicy().hasHeightForWidth())
        self.textTextEdit.setSizePolicy(sizePolicy)
        self.textTextEdit.setAcceptRichText(False)
        self.textTextEdit.setObjectName("textTextEdit")
        self.gridlayout.addWidget(self.textTextEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(PyRegExpWizardDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PyRegExpWizardDialog)
        QtCore.QMetaObject.connectSlotsByName(PyRegExpWizardDialog)
        PyRegExpWizardDialog.setTabOrder(self.py2Button, self.py3Button)
        PyRegExpWizardDialog.setTabOrder(self.py3Button, self.variableLineEdit)
        PyRegExpWizardDialog.setTabOrder(self.variableLineEdit, self.importCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.importCheckBox, self.commentButton)
        PyRegExpWizardDialog.setTabOrder(self.commentButton, self.charButton)
        PyRegExpWizardDialog.setTabOrder(self.charButton, self.anycharButton)
        PyRegExpWizardDialog.setTabOrder(self.anycharButton, self.repeatButton)
        PyRegExpWizardDialog.setTabOrder(self.repeatButton, self.nonGroupButton)
        PyRegExpWizardDialog.setTabOrder(self.nonGroupButton, self.groupButton)
        PyRegExpWizardDialog.setTabOrder(self.groupButton, self.namedGroupButton)
        PyRegExpWizardDialog.setTabOrder(self.namedGroupButton, self.namedReferenceButton)
        PyRegExpWizardDialog.setTabOrder(self.namedReferenceButton, self.altnButton)
        PyRegExpWizardDialog.setTabOrder(self.altnButton, self.beglineButton)
        PyRegExpWizardDialog.setTabOrder(self.beglineButton, self.endlineButton)
        PyRegExpWizardDialog.setTabOrder(self.endlineButton, self.wordboundButton)
        PyRegExpWizardDialog.setTabOrder(self.wordboundButton, self.nonwordboundButton)
        PyRegExpWizardDialog.setTabOrder(self.nonwordboundButton, self.poslookaheadButton)
        PyRegExpWizardDialog.setTabOrder(self.poslookaheadButton, self.neglookaheadButton)
        PyRegExpWizardDialog.setTabOrder(self.neglookaheadButton, self.poslookbehindButton)
        PyRegExpWizardDialog.setTabOrder(self.poslookbehindButton, self.neglookbehindButton)
        PyRegExpWizardDialog.setTabOrder(self.neglookbehindButton, self.undoButton)
        PyRegExpWizardDialog.setTabOrder(self.undoButton, self.redoButton)
        PyRegExpWizardDialog.setTabOrder(self.redoButton, self.regexpTextEdit)
        PyRegExpWizardDialog.setTabOrder(self.regexpTextEdit, self.textTextEdit)
        PyRegExpWizardDialog.setTabOrder(self.textTextEdit, self.caseSensitiveCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.caseSensitiveCheckBox, self.verboseCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.verboseCheckBox, self.multilineCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.multilineCheckBox, self.localeCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.localeCheckBox, self.dotallCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.dotallCheckBox, self.unicodeCheckBox)
        PyRegExpWizardDialog.setTabOrder(self.unicodeCheckBox, self.resultTable)
        PyRegExpWizardDialog.setTabOrder(self.resultTable, self.buttonBox)

    def retranslateUi(self, PyRegExpWizardDialog):
        _translate = QtCore.QCoreApplication.translate
        PyRegExpWizardDialog.setWindowTitle(_translate("PyRegExpWizardDialog", "Python re Wizard"))
        self.versionGroup.setTitle(_translate("PyRegExpWizardDialog", "Python Version"))
        self.py2Button.setText(_translate("PyRegExpWizardDialog", "Python 2"))
        self.py3Button.setText(_translate("PyRegExpWizardDialog", "Python 3"))
        self.variableLabel.setText(_translate("PyRegExpWizardDialog", "Variable Name:"))
        self.importCheckBox.setText(_translate("PyRegExpWizardDialog", "Include import statement"))
        self.commentButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Comment: (?#)</b>\n"
"<p>Insert some comment inside your regexp.</p>"))
        self.commentButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Comment: (?#)</b>\n"
"<p>Insert some comment inside your regexp.The regex engine ignores everything after the (?# until the first closing round bracket. \n"
"The following example could clarify the regexp which match a valid date: </p>\n"
"<p>(?#year)(19|20)\\d\\d[- /.](?#month)(0[1-9]|1[012])[- /.](?#day)(0[1-9]|[12][0-9]|3[01])</p>"))
        self.charButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog.</p>"))
        self.charButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog. This dialog will help to edit the range of characters and add some specific conditions.</p>s"))
        self.anycharButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp.</p>"))
        self.anycharButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp. The dot matches a single character, except line break characters (by default). \n"
"E.g. \'gr.y\' matches \'gray\', \'grey\', \'gr%y\', etc. Use the dot sparingly. Often, a character class or negated\n"
"character class is faster and more precise.</p>"))
        self.repeatButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.repeatButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.nonGroupButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets.</p>"))
        self.nonGroupButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets. It can be used to apply a regexp quantifier (eg. \'?\' or \'+\') to the entire\n"
"group of characters inside the brakets. E.g. the regex \'Set(?:Value)?\' matches \'Set\' or \'SetValue\'. The \'?:\' inside the brakets\n"
"means that the content of the match (called the backreference) is not stored for further use.</p>"))
        self.groupButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets.</p>"))
        self.groupButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets. They can be used to apply a regexp quantifier (e.g. \'?\' or \'+\') to the entire group of \n"
"characters inside the brakets. E.g. the regex \'Set(Value)?\' matches \'Set\' or \'SetValue\'. Contrary to non-capturing parentheses, \n"
"the backreference matched inside the brakets is stored for further use (i.e. \'Value\' in the second example above). \n"
"One can access the backereference with the \'\\1\' expression. </p>\n"
"<p>E.g. \'([a-c])x\\1x\\1\' will match \'axaxa\', \'bxbxb\' and \'cxcxc\'.</p>"))
        self.namedGroupButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Named group: (?P&lt;<i>groupname</i>&gt;)</b>\n"
"<p>Select to insert some named group brackets.</p>"))
        self.namedGroupButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Named group: (?P&lt;<i>groupname</i>&gt;)</b>\n"
"<p>Select to insert some named group brackets. Usage is similar to standard group parentheses as the matched \n"
"backreference is also stored for further usage. The difference is that a name is given to the match. This is useful when \n"
"the work to do on the match becomes a bit complicated. One can access the backreference via the group name (i.e (?P=<i>groupname</i>)).\n"
"E.g. (?P<foo>[abc])x(?P=foo)x(?P=foo)x matches \'axaxax\',\'bxbxbx\' or \'cxcxcx\' (\'foo\' is the group name)</p>"))
        self.namedReferenceButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Reference named group: (?P=<i>groupname</i>)</b>\n"
"<p>Select to insert a reference to named group previously declared.</p>"))
        self.namedReferenceButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Reference named group: (?P=<i>groupname</i>)</b>\n"
"<p>Select to insert a reference to named group previously declared. Each reference group refers to the match\n"
" found by the corresponding named group. In the following example, (?P=foo) may refer to the charaters \'a\',\'b\' or \'c\'.</p>\n"
"<p>E.g. (?P<foo>[abc])x(?P=foo)x(?P=foo)x matches \'axaxax\',\'bxbxbx\' or \'cxcxcx\'.</p>"))
        self.altnButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. </p>"))
        self.altnButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. The alternation is used to match a single regular expression out of \n"
"several possible regular expressions. E.g. \'cat|dog|mouse|fish\' matches words containing the word \'cat\', \'dog\',\'mouse\' or \'fish\'.\n"
"Be aware that in the above example, the alternatives refer to whole or part of words. If you want to match exactly the\n"
" words \'cat\', \'dog\', ... you should express the fact that you only want to match complete words: \'\\b(cat|dog|mouse|fish)\\b\'</p>"))
        self.beglineButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^).</p>"))
        self.beglineButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^). It is used to find some expressions at the begining of lines.\n"
"E.g. \'^[A-Z]\' match lines starting with a capitalized character. </p>"))
        self.endlineButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($).</p>"))
        self.endlineButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($). It is used to find some expressions at the end of lines.</p>"))
        self.wordboundButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b).</p>"))
        self.wordboundButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b). This character is used to express the fact that word \n"
"must begin or end at this position. E.g. \'\\bcat\\b\' matches exactly the word \'cat\' while \'concatenation\' is ignored.</p>"))
        self.nonwordboundButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b.</p>"))
        self.nonwordboundButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b. \\B matches at every position where \\b \n"
"does not. Effectively, \\B matches at any position between two word characters as well as at any position between two non-word characters.</p>"))
        self.poslookaheadButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets.</p>"))
        self.poslookaheadButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets. Basically, positive lookhead is used to match a character only if followed by another one.\n"
"Writting \'q(?=u)\' means that you want to match the \'q\' character only if it is followed by \'u\'. In this statement \'u\' is a trivial \n"
"regexp which may be replaced by a more complex expression; q(?=[abc])\' will match a \'q\' if followed by either \'a\', \'b\' or \'c\'.</p>"))
        self.neglookaheadButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets.</p>"))
        self.neglookaheadButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets. Basically, negative lookhead is used to match a character only if it is not\n"
"followed by a another one. Writting \'q(?!u)\' means that you want to match \'q\' only if it is not followed by \'u\'. In this statement, \'u\' is a\n"
"trivial regexp which may be replaced by a more complex expression; \'q(?![abc])\' will match a \'q\' if it is followed by anything else than \'a\', \'b\' or \'c\'.</p>"))
        self.poslookbehindButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Positive lookbehind: (?&lt;=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookbehind brackets.</p>"))
        self.poslookbehindButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Positive lookbehind: (?&lt;=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookbehind brackets. Lookbehind has the same effect as lookahead, but works backwards. \n"
"It is used to match a character only if preceded by another one. Writting \'(?&lt;=u)q\' means that you want to match the \'q\' character \n"
"only if it is preceded by \'u\'. As with lookhead, \'u\' may be replaced by a more complex expression; \'(?&lt;=[abc])q\' will match a \'q\' if preceded by either \'a\', \'b\' or \'c\'.</p>"))
        self.neglookbehindButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Negative lookbehind (?&lt;!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookbehind brackets.</p>"))
        self.neglookbehindButton.setWhatsThis(_translate("PyRegExpWizardDialog", "<b>Negative lookbehind (?&lt;!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookbehind brackets. Lookbehind has the same effect as lookahead, \n"
"but works backwards. It is used to match a character only if not preceded by another one. Writting \'(?&lt;!u)q\' means that you want to match the \'q\' \n"
"character only if it is not preceded by \'u\'. As other lookaround, \'u\' may be replaced by a more complex \n"
"expression; \'(?&lt;![abc])q\' will match a \'q\' only if not preceded by either \'a\', \'b\' nor \'c\'.</p>"))
        self.undoButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Undo last edit</b>"))
        self.redoButton.setToolTip(_translate("PyRegExpWizardDialog", "<b>Redo last edit</b>"))
        self.textLabel1.setText(_translate("PyRegExpWizardDialog", "Regexp:"))
        self.multilineCheckBox.setToolTip(_translate("PyRegExpWizardDialog", "\"^\" matches beginning of line, \"$\" matches end of line"))
        self.multilineCheckBox.setText(_translate("PyRegExpWizardDialog", "Match Linebreaks"))
        self.unicodeCheckBox.setText(_translate("PyRegExpWizardDialog", "ASCII"))
        self.verboseCheckBox.setText(_translate("PyRegExpWizardDialog", "Verbose Regexp"))
        self.caseSensitiveCheckBox.setText(_translate("PyRegExpWizardDialog", "Case Sensitive"))
        self.localeCheckBox.setText(_translate("PyRegExpWizardDialog", "Observe Locale"))
        self.dotallCheckBox.setToolTip(_translate("PyRegExpWizardDialog", "\".\" matches linebreaks as well"))
        self.dotallCheckBox.setText(_translate("PyRegExpWizardDialog", "Dot matches Linebreak"))
        self.textLabel2.setText(_translate("PyRegExpWizardDialog", "Text:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyRegExpWizardDialog = QtWidgets.QWidget()
    ui = Ui_PyRegExpWizardDialog()
    ui.setupUi(PyRegExpWizardDialog)
    PyRegExpWizardDialog.show()
    sys.exit(app.exec_())

