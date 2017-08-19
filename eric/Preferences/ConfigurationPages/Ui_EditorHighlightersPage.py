# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorHighlightersPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorHighlightersPage(object):
    def setupUi(self, EditorHighlightersPage):
        EditorHighlightersPage.setObjectName("EditorHighlightersPage")
        EditorHighlightersPage.resize(400, 361)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditorHighlightersPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(EditorHighlightersPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line19 = QtWidgets.QFrame(EditorHighlightersPage)
        self.line19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line19.setObjectName("line19")
        self.verticalLayout.addWidget(self.line19)
        self.editorLexerList = QtWidgets.QTreeWidget(EditorHighlightersPage)
        self.editorLexerList.setAlternatingRowColors(True)
        self.editorLexerList.setRootIsDecorated(False)
        self.editorLexerList.setObjectName("editorLexerList")
        self.verticalLayout.addWidget(self.editorLexerList)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel2_6 = QtWidgets.QLabel(EditorHighlightersPage)
        self.textLabel2_6.setObjectName("textLabel2_6")
        self.gridLayout.addWidget(self.textLabel2_6, 0, 0, 1, 1)
        self.editorFileExtEdit = QtWidgets.QLineEdit(EditorHighlightersPage)
        self.editorFileExtEdit.setObjectName("editorFileExtEdit")
        self.gridLayout.addWidget(self.editorFileExtEdit, 0, 1, 1, 1)
        self.addLexerButton = QtWidgets.QPushButton(EditorHighlightersPage)
        self.addLexerButton.setObjectName("addLexerButton")
        self.gridLayout.addWidget(self.addLexerButton, 0, 2, 1, 1)
        self.textLabel3_3 = QtWidgets.QLabel(EditorHighlightersPage)
        self.textLabel3_3.setObjectName("textLabel3_3")
        self.gridLayout.addWidget(self.textLabel3_3, 1, 0, 1, 1)
        self.editorLexerCombo = QtWidgets.QComboBox(EditorHighlightersPage)
        self.editorLexerCombo.setObjectName("editorLexerCombo")
        self.gridLayout.addWidget(self.editorLexerCombo, 1, 1, 1, 1)
        self.deleteLexerButton = QtWidgets.QPushButton(EditorHighlightersPage)
        self.deleteLexerButton.setObjectName("deleteLexerButton")
        self.gridLayout.addWidget(self.deleteLexerButton, 1, 2, 1, 1)
        self.pygmentsLabel = QtWidgets.QLabel(EditorHighlightersPage)
        self.pygmentsLabel.setObjectName("pygmentsLabel")
        self.gridLayout.addWidget(self.pygmentsLabel, 2, 0, 1, 1)
        self.pygmentsLexerCombo = QtWidgets.QComboBox(EditorHighlightersPage)
        self.pygmentsLexerCombo.setObjectName("pygmentsLexerCombo")
        self.gridLayout.addWidget(self.pygmentsLexerCombo, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(EditorHighlightersPage)
        QtCore.QMetaObject.connectSlotsByName(EditorHighlightersPage)
        EditorHighlightersPage.setTabOrder(self.editorLexerList, self.editorFileExtEdit)
        EditorHighlightersPage.setTabOrder(self.editorFileExtEdit, self.editorLexerCombo)
        EditorHighlightersPage.setTabOrder(self.editorLexerCombo, self.pygmentsLexerCombo)
        EditorHighlightersPage.setTabOrder(self.pygmentsLexerCombo, self.addLexerButton)
        EditorHighlightersPage.setTabOrder(self.addLexerButton, self.deleteLexerButton)

    def retranslateUi(self, EditorHighlightersPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorHighlightersPage", "<b>Configure syntax highlighters</b>"))
        self.editorLexerList.setSortingEnabled(True)
        self.editorLexerList.headerItem().setText(0, _translate("EditorHighlightersPage", "Filename Pattern"))
        self.editorLexerList.headerItem().setText(1, _translate("EditorHighlightersPage", "Lexer Language"))
        self.textLabel2_6.setText(_translate("EditorHighlightersPage", "Filename Pattern:"))
        self.editorFileExtEdit.setToolTip(_translate("EditorHighlightersPage", "Enter the filename pattern to be associated"))
        self.addLexerButton.setToolTip(_translate("EditorHighlightersPage", "Press to add or change the entered association"))
        self.addLexerButton.setText(_translate("EditorHighlightersPage", "Add/Change"))
        self.textLabel3_3.setText(_translate("EditorHighlightersPage", "Lexer Language:"))
        self.editorLexerCombo.setToolTip(_translate("EditorHighlightersPage", "Select the lexer language to associate"))
        self.deleteLexerButton.setToolTip(_translate("EditorHighlightersPage", "Press to delete the selected association"))
        self.deleteLexerButton.setText(_translate("EditorHighlightersPage", "Delete"))
        self.pygmentsLabel.setText(_translate("EditorHighlightersPage", "Alternative Lexer:"))
        self.pygmentsLexerCombo.setToolTip(_translate("EditorHighlightersPage", "Select the alternative lexer to associate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorHighlightersPage = QtWidgets.QWidget()
    ui = Ui_EditorHighlightersPage()
    ui.setupUi(EditorHighlightersPage)
    EditorHighlightersPage.show()
    sys.exit(app.exec_())

