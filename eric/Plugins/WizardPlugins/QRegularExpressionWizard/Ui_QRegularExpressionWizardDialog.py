# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\WizardPlugins\QRegularExpressionWizard\QRegularExpressionWizardDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QRegularExpressionWizardDialog(object):
    def setupUi(self, QRegularExpressionWizardDialog):
        QRegularExpressionWizardDialog.setObjectName("QRegularExpressionWizardDialog")
        QRegularExpressionWizardDialog.resize(800, 700)
        QRegularExpressionWizardDialog.setProperty("sizeGripEnabled", True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QRegularExpressionWizardDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.variableLabel = QtWidgets.QLabel(QRegularExpressionWizardDialog)
        self.variableLabel.setObjectName("variableLabel")
        self.hboxlayout.addWidget(self.variableLabel)
        self.variableLineEdit = QtWidgets.QLineEdit(QRegularExpressionWizardDialog)
        self.variableLineEdit.setObjectName("variableLineEdit")
        self.hboxlayout.addWidget(self.variableLineEdit)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.variableLine = QtWidgets.QFrame(QRegularExpressionWizardDialog)
        self.variableLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.variableLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.variableLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.variableLine.setObjectName("variableLine")
        self.verticalLayout.addWidget(self.variableLine)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commentButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.commentButton.setObjectName("commentButton")
        self.horizontalLayout.addWidget(self.commentButton)
        self.charButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.charButton.setObjectName("charButton")
        self.horizontalLayout.addWidget(self.charButton)
        self.anycharButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.anycharButton.setObjectName("anycharButton")
        self.horizontalLayout.addWidget(self.anycharButton)
        self.repeatButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.repeatButton.setObjectName("repeatButton")
        self.horizontalLayout.addWidget(self.repeatButton)
        self.nonGroupButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.nonGroupButton.setObjectName("nonGroupButton")
        self.horizontalLayout.addWidget(self.nonGroupButton)
        self.atomicGroupButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.atomicGroupButton.setObjectName("atomicGroupButton")
        self.horizontalLayout.addWidget(self.atomicGroupButton)
        self.groupButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.groupButton.setObjectName("groupButton")
        self.horizontalLayout.addWidget(self.groupButton)
        self.namedGroupButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.namedGroupButton.setObjectName("namedGroupButton")
        self.horizontalLayout.addWidget(self.namedGroupButton)
        self.namedReferenceButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.namedReferenceButton.setObjectName("namedReferenceButton")
        self.horizontalLayout.addWidget(self.namedReferenceButton)
        self.altnButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.altnButton.setObjectName("altnButton")
        self.horizontalLayout.addWidget(self.altnButton)
        self.beglineButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.beglineButton.setObjectName("beglineButton")
        self.horizontalLayout.addWidget(self.beglineButton)
        self.endlineButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.endlineButton.setObjectName("endlineButton")
        self.horizontalLayout.addWidget(self.endlineButton)
        self.wordboundButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.wordboundButton.setObjectName("wordboundButton")
        self.horizontalLayout.addWidget(self.wordboundButton)
        self.nonwordboundButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.nonwordboundButton.setObjectName("nonwordboundButton")
        self.horizontalLayout.addWidget(self.nonwordboundButton)
        self.poslookaheadButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.poslookaheadButton.setObjectName("poslookaheadButton")
        self.horizontalLayout.addWidget(self.poslookaheadButton)
        self.neglookaheadButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.neglookaheadButton.setObjectName("neglookaheadButton")
        self.horizontalLayout.addWidget(self.neglookaheadButton)
        self.poslookbehindButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.poslookbehindButton.setObjectName("poslookbehindButton")
        self.horizontalLayout.addWidget(self.poslookbehindButton)
        self.neglookbehindButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.neglookbehindButton.setObjectName("neglookbehindButton")
        self.horizontalLayout.addWidget(self.neglookbehindButton)
        spacerItem = QtWidgets.QSpacerItem(16, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.undoButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout.addWidget(self.undoButton)
        self.redoButton = QtWidgets.QToolButton(QRegularExpressionWizardDialog)
        self.redoButton.setObjectName("redoButton")
        self.horizontalLayout.addWidget(self.redoButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textLabel1 = QtWidgets.QLabel(QRegularExpressionWizardDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout_2.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.regexpTextEdit = QtWidgets.QTextEdit(QRegularExpressionWizardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.regexpTextEdit.sizePolicy().hasHeightForWidth())
        self.regexpTextEdit.setSizePolicy(sizePolicy)
        self.regexpTextEdit.setAcceptRichText(False)
        self.regexpTextEdit.setObjectName("regexpTextEdit")
        self.gridLayout_2.addWidget(self.regexpTextEdit, 0, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(QRegularExpressionWizardDialog)
        self.textLabel2.setAlignment(QtCore.Qt.AlignTop)
        self.textLabel2.setObjectName("textLabel2")
        self.gridLayout_2.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textTextEdit = QtWidgets.QTextEdit(QRegularExpressionWizardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textTextEdit.sizePolicy().hasHeightForWidth())
        self.textTextEdit.setSizePolicy(sizePolicy)
        self.textTextEdit.setAcceptRichText(False)
        self.textTextEdit.setObjectName("textTextEdit")
        self.gridLayout_2.addWidget(self.textTextEdit, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.caseInsensitiveCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardDialog)
        self.caseInsensitiveCheckBox.setObjectName("caseInsensitiveCheckBox")
        self.gridLayout.addWidget(self.caseInsensitiveCheckBox, 0, 0, 1, 1)
        self.multilineCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardDialog)
        self.multilineCheckBox.setObjectName("multilineCheckBox")
        self.gridLayout.addWidget(self.multilineCheckBox, 0, 1, 1, 1)
        self.dotallCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardDialog)
        self.dotallCheckBox.setObjectName("dotallCheckBox")
        self.gridLayout.addWidget(self.dotallCheckBox, 0, 2, 1, 1)
        self.extendedCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardDialog)
        self.extendedCheckBox.setObjectName("extendedCheckBox")
        self.gridLayout.addWidget(self.extendedCheckBox, 1, 0, 1, 1)
        self.greedinessCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardDialog)
        self.greedinessCheckBox.setObjectName("greedinessCheckBox")
        self.gridLayout.addWidget(self.greedinessCheckBox, 1, 1, 1, 1)
        self.unicodeCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardDialog)
        self.unicodeCheckBox.setObjectName("unicodeCheckBox")
        self.gridLayout.addWidget(self.unicodeCheckBox, 1, 2, 1, 1)
        self.captureCheckBox = QtWidgets.QCheckBox(QRegularExpressionWizardDialog)
        self.captureCheckBox.setObjectName("captureCheckBox")
        self.gridLayout.addWidget(self.captureCheckBox, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)
        self.resultTable = QtWidgets.QTableWidget(QRegularExpressionWizardDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.resultTable.sizePolicy().hasHeightForWidth())
        self.resultTable.setSizePolicy(sizePolicy)
        self.resultTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)
        self.gridLayout_2.addWidget(self.resultTable, 3, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(QRegularExpressionWizardDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QRegularExpressionWizardDialog)
        QtCore.QMetaObject.connectSlotsByName(QRegularExpressionWizardDialog)
        QRegularExpressionWizardDialog.setTabOrder(self.variableLineEdit, self.commentButton)
        QRegularExpressionWizardDialog.setTabOrder(self.commentButton, self.charButton)
        QRegularExpressionWizardDialog.setTabOrder(self.charButton, self.anycharButton)
        QRegularExpressionWizardDialog.setTabOrder(self.anycharButton, self.repeatButton)
        QRegularExpressionWizardDialog.setTabOrder(self.repeatButton, self.nonGroupButton)
        QRegularExpressionWizardDialog.setTabOrder(self.nonGroupButton, self.atomicGroupButton)
        QRegularExpressionWizardDialog.setTabOrder(self.atomicGroupButton, self.groupButton)
        QRegularExpressionWizardDialog.setTabOrder(self.groupButton, self.namedGroupButton)
        QRegularExpressionWizardDialog.setTabOrder(self.namedGroupButton, self.namedReferenceButton)
        QRegularExpressionWizardDialog.setTabOrder(self.namedReferenceButton, self.altnButton)
        QRegularExpressionWizardDialog.setTabOrder(self.altnButton, self.beglineButton)
        QRegularExpressionWizardDialog.setTabOrder(self.beglineButton, self.endlineButton)
        QRegularExpressionWizardDialog.setTabOrder(self.endlineButton, self.wordboundButton)
        QRegularExpressionWizardDialog.setTabOrder(self.wordboundButton, self.nonwordboundButton)
        QRegularExpressionWizardDialog.setTabOrder(self.nonwordboundButton, self.poslookaheadButton)
        QRegularExpressionWizardDialog.setTabOrder(self.poslookaheadButton, self.neglookaheadButton)
        QRegularExpressionWizardDialog.setTabOrder(self.neglookaheadButton, self.poslookbehindButton)
        QRegularExpressionWizardDialog.setTabOrder(self.poslookbehindButton, self.neglookbehindButton)
        QRegularExpressionWizardDialog.setTabOrder(self.neglookbehindButton, self.undoButton)
        QRegularExpressionWizardDialog.setTabOrder(self.undoButton, self.redoButton)
        QRegularExpressionWizardDialog.setTabOrder(self.redoButton, self.regexpTextEdit)
        QRegularExpressionWizardDialog.setTabOrder(self.regexpTextEdit, self.textTextEdit)
        QRegularExpressionWizardDialog.setTabOrder(self.textTextEdit, self.caseInsensitiveCheckBox)
        QRegularExpressionWizardDialog.setTabOrder(self.caseInsensitiveCheckBox, self.multilineCheckBox)
        QRegularExpressionWizardDialog.setTabOrder(self.multilineCheckBox, self.dotallCheckBox)
        QRegularExpressionWizardDialog.setTabOrder(self.dotallCheckBox, self.extendedCheckBox)
        QRegularExpressionWizardDialog.setTabOrder(self.extendedCheckBox, self.greedinessCheckBox)
        QRegularExpressionWizardDialog.setTabOrder(self.greedinessCheckBox, self.unicodeCheckBox)
        QRegularExpressionWizardDialog.setTabOrder(self.unicodeCheckBox, self.captureCheckBox)
        QRegularExpressionWizardDialog.setTabOrder(self.captureCheckBox, self.resultTable)
        QRegularExpressionWizardDialog.setTabOrder(self.resultTable, self.buttonBox)

    def retranslateUi(self, QRegularExpressionWizardDialog):
        _translate = QtCore.QCoreApplication.translate
        QRegularExpressionWizardDialog.setWindowTitle(_translate("QRegularExpressionWizardDialog", "QRegularExpression Wizard"))
        self.variableLabel.setText(_translate("QRegularExpressionWizardDialog", "Variable Name:"))
        self.commentButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Comment: (?#)</b>\n"
"<p>Insert some comment inside your regexp.</p>"))
        self.commentButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Comment: (?#)</b>\n"
"<p>Insert some comment inside your regexp.The regex engine ignores everything after the (?# until the first closing round bracket. \n"
"The following example could clarify the regexp which match a valid date: </p>\n"
"<p>(?#year)(19|20)\\d\\d[- /.](?#month)(0[1-9]|1[012])[- /.](?#day)(0[1-9]|[12][0-9]|3[01])</p>"))
        self.charButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog.</p>"))
        self.charButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Single character of a range (e.g. [abcd])</b><p>Select a single character of a range via a specific dialog. This dialog will help to edit the range of characters and add some specific conditions.</p>s"))
        self.anycharButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp.</p>"))
        self.anycharButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Any character: \'.\'</b>\n"
"<p>Select to insert a dot (.) in your regexp. The dot matches a single character, except line break characters (by default). \n"
"E.g. \'gr.y\' matches \'gray\', \'grey\', \'gr%y\', etc. Use the dot sparingly. Often, a character class or negated\n"
"character class is faster and more precise.</p>"))
        self.repeatButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.repeatButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Repeat contents</b>\n"
"<p>Select a repetition condition via a specific dialog. This dialog will help to specify the allowed range for repetitions.</p>"))
        self.nonGroupButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets.</p>"))
        self.nonGroupButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Non capturing parentheses: (?:)</b>\n"
"<p>Select to insert some non capturing brackets. It can be used to apply a regexp quantifier (eg. \'?\' or \'+\') to the entire\n"
"group of characters inside the brakets. E.g. the regex \'Set(?:Value)?\' matches \'Set\' or \'SetValue\'. The \'?:\' inside the brakets\n"
"means that the content of the match (called the backreference) is not stored for further use.</p>"))
        self.atomicGroupButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Atomic non capturing parentheses: (?>)</b>\n"
"<p>Select to insert some atomic non capturing brackets.</p>"))
        self.atomicGroupButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Atomic non capturing parentheses: (?>)</b>\n"
"<p>Select to insert some atomic non capturing brackets. It can be used to apply a regexp quantifier (eg. \'?\' or \'+\') to the entire\n"
"group of characters inside the brakets. E.g. the regex \'Set(?>Value)?\' matches \'Set\' or \'SetValue\'. The \'?>\' inside the brakets\n"
"means that the content of the match (called the backreference) is not stored for further use.</p>"))
        self.groupButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets.</p>"))
        self.groupButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Group: ()</b>\n"
"<p>Select to insert some capturing brackets. They can be used to apply a regexp quantifier (e.g. \'?\' or \'+\') to the entire group of \n"
"characters inside the brakets. E.g. the regex \'Set(Value)?\' matches \'Set\' or \'SetValue\'. Contrary to non-capturing parentheses, \n"
"the backreference matched inside the brakets is stored for further use (i.e. \'Value\' in the second example above). \n"
"One can access the backereference with the \'\\1\' expression. </p>\n"
"<p>E.g. \'([a-c])x\\1x\\1\' will match \'axaxa\', \'bxbxb\' and \'cxcxc\'.</p>"))
        self.namedGroupButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Named group: (?P&lt;<i>groupname</i>&gt;)</b>\n"
"<p>Select to insert some named group brackets.</p>"))
        self.namedGroupButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Named group: (?P&lt;<i>groupname</i>&gt;)</b>\n"
"<p>Select to insert some named group brackets. Usage is similar to standard group parentheses as the matched \n"
"backreference is also stored for further usage. The difference is that a name is given to the match. This is useful when \n"
"the work to do on the match becomes a bit complicated. One can access the backreference via the group name (i.e (?P=<i>groupname</i>)).\n"
"E.g. (?P<foo>[abc])x(?P=foo)x(?P=foo)x matches \'axaxax\',\'bxbxbx\' or \'cxcxcx\' (\'foo\' is the group name)</p>"))
        self.namedReferenceButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Reference named group: (?P=<i>groupname</i>)</b>\n"
"<p>Select to insert a reference to named group previously declared.</p>"))
        self.namedReferenceButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Reference named group: (?P=<i>groupname</i>)</b>\n"
"<p>Select to insert a reference to named group previously declared. Each reference group refers to the match\n"
" found by the corresponding named group. In the following example, (?P=foo) may refer to the charaters \'a\',\'b\' or \'c\'.</p>\n"
"<p>E.g. (?P<foo>[abc])x(?P=foo)x(?P=foo)x matches \'axaxax\',\'bxbxbx\' or \'cxcxcx\'.</p>"))
        self.altnButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. </p>"))
        self.altnButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Alternatives: \'|\'</b>\n"
"<p>Select to insert the alternation symbol \'|\'. The alternation is used to match a single regular expression out of \n"
"several possible regular expressions. E.g. \'cat|dog|mouse|fish\' matches words containing the word \'cat\', \'dog\',\'mouse\' or \'fish\'.\n"
"Be aware that in the above example, the alternatives refer to whole or part of words. If you want to match exactly the\n"
" words \'cat\', \'dog\', ... you should express the fact that you only want to match complete words: \'\\b(cat|dog|mouse|fish)\\b\'</p>"))
        self.beglineButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^).</p>"))
        self.beglineButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Begin of line: \'^\'</b>\n"
"<p>Select to insert the start line character (^). It is used to find some expressions at the begining of lines.\n"
"E.g. \'^[A-Z]\' match lines starting with a capitalized character. </p>"))
        self.endlineButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($).</p>"))
        self.endlineButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>End of line: \'$\'</b>\n"
"<p>Select to insert the end of line character ($). It is used to find some expressions at the end of lines.</p>"))
        self.wordboundButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b).</p>"))
        self.wordboundButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Word boundary</b>\n"
"<p>Select to insert the word boudary character (\\b). This character is used to express the fact that word \n"
"must begin or end at this position. E.g. \'\\bcat\\b\' matches exactly the word \'cat\' while \'concatenation\' is ignored.</p>"))
        self.nonwordboundButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b.</p>"))
        self.nonwordboundButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Non word boundary</b>\n"
"<p>Select to insert the word boudary character (\\B). \\B is the negated version of \\b. \\B matches at every position where \\b \n"
"does not. Effectively, \\B matches at any position between two word characters as well as at any position between two non-word characters.</p>"))
        self.poslookaheadButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets.</p>"))
        self.poslookaheadButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Positive lookahead: (?=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookhead brackets. Basically, positive lookhead is used to match a character only if followed by another one.\n"
"Writting \'q(?=u)\' means that you want to match the \'q\' character only if it is followed by \'u\'. In this statement \'u\' is a trivial \n"
"regexp which may be replaced by a more complex expression; q(?=[abc])\' will match a \'q\' if followed by either \'a\', \'b\' or \'c\'.</p>"))
        self.neglookaheadButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets.</p>"))
        self.neglookaheadButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Negative lookahead: (?!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookhead brackets. Basically, negative lookhead is used to match a character only if it is not\n"
"followed by a another one. Writting \'q(?!u)\' means that you want to match \'q\' only if it is not followed by \'u\'. In this statement, \'u\' is a\n"
"trivial regexp which may be replaced by a more complex expression; \'q(?![abc])\' will match a \'q\' if it is followed by anything else than \'a\', \'b\' or \'c\'.</p>"))
        self.poslookbehindButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Positive lookbehind: (?&lt;=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookbehind brackets.</p>"))
        self.poslookbehindButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Positive lookbehind: (?&lt;=<i>regexpr</i>)</b>\n"
"<p>Select to insert the positive lookbehind brackets. Lookbehind has the same effect as lookahead, but works backwards. \n"
"It is used to match a character only if preceded by another one. Writting \'(?&lt;=u)q\' means that you want to match the \'q\' character \n"
"only if it is preceded by \'u\'. As with lookhead, \'u\' may be replaced by a more complex expression; \'(?&lt;=[abc])q\' will match a \'q\' if preceded by either \'a\', \'b\' or \'c\'.</p>"))
        self.neglookbehindButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Negative lookbehind (?&lt;!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookbehind brackets.</p>"))
        self.neglookbehindButton.setWhatsThis(_translate("QRegularExpressionWizardDialog", "<b>Negative lookbehind (?&lt;!<i>regexpr</i>)</b>\n"
"<p>Select to insert the negative lookbehind brackets. Lookbehind has the same effect as lookahead, \n"
"but works backwards. It is used to match a character only if not preceded by another one. Writting \'(?&lt;!u)q\' means that you want to match the \'q\' \n"
"character only if it is not preceded by \'u\'. As other lookaround, \'u\' may be replaced by a more complex \n"
"expression; \'(?&lt;![abc])q\' will match a \'q\' only if not preceded by either \'a\', \'b\' nor \'c\'.</p>"))
        self.undoButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Undo last edit</b>"))
        self.redoButton.setToolTip(_translate("QRegularExpressionWizardDialog", "<b>Redo last edit</b>"))
        self.textLabel1.setText(_translate("QRegularExpressionWizardDialog", "Regexp:"))
        self.textLabel2.setText(_translate("QRegularExpressionWizardDialog", "Text:"))
        self.caseInsensitiveCheckBox.setText(_translate("QRegularExpressionWizardDialog", "Case Insensitive"))
        self.multilineCheckBox.setToolTip(_translate("QRegularExpressionWizardDialog", "\"^\" matches beginning of line, \"$\" matches end of line"))
        self.multilineCheckBox.setText(_translate("QRegularExpressionWizardDialog", "Match Linebreaks"))
        self.dotallCheckBox.setToolTip(_translate("QRegularExpressionWizardDialog", "\".\" matches everything including linebreaks"))
        self.dotallCheckBox.setText(_translate("QRegularExpressionWizardDialog", "Dot matches everything"))
        self.extendedCheckBox.setText(_translate("QRegularExpressionWizardDialog", "Extended Pattern Syntax"))
        self.greedinessCheckBox.setText(_translate("QRegularExpressionWizardDialog", "Inverted Greediness"))
        self.unicodeCheckBox.setText(_translate("QRegularExpressionWizardDialog", "Unicode"))
        self.captureCheckBox.setToolTip(_translate("QRegularExpressionWizardDialog", "Non-named capturing groups do not capture substrings"))
        self.captureCheckBox.setText(_translate("QRegularExpressionWizardDialog", "Don\'t Capture"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QRegularExpressionWizardDialog = QtWidgets.QWidget()
    ui = Ui_QRegularExpressionWizardDialog()
    ui.setupUi(QRegularExpressionWizardDialog)
    QRegularExpressionWizardDialog.show()
    sys.exit(app.exec_())

