# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\LexerAssociationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LexerAssociationDialog(object):
    def setupUi(self, LexerAssociationDialog):
        LexerAssociationDialog.setObjectName("LexerAssociationDialog")
        LexerAssociationDialog.resize(460, 418)
        LexerAssociationDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(LexerAssociationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editorLexerList = QtWidgets.QTreeWidget(LexerAssociationDialog)
        self.editorLexerList.setAlternatingRowColors(True)
        self.editorLexerList.setRootIsDecorated(False)
        self.editorLexerList.setObjectName("editorLexerList")
        self.verticalLayout.addWidget(self.editorLexerList)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel2_6 = QtWidgets.QLabel(LexerAssociationDialog)
        self.textLabel2_6.setObjectName("textLabel2_6")
        self.gridLayout.addWidget(self.textLabel2_6, 0, 0, 1, 1)
        self.editorFileExtEdit = QtWidgets.QLineEdit(LexerAssociationDialog)
        self.editorFileExtEdit.setObjectName("editorFileExtEdit")
        self.gridLayout.addWidget(self.editorFileExtEdit, 0, 1, 1, 1)
        self.addLexerButton = QtWidgets.QPushButton(LexerAssociationDialog)
        self.addLexerButton.setObjectName("addLexerButton")
        self.gridLayout.addWidget(self.addLexerButton, 0, 2, 1, 1)
        self.textLabel3_3 = QtWidgets.QLabel(LexerAssociationDialog)
        self.textLabel3_3.setObjectName("textLabel3_3")
        self.gridLayout.addWidget(self.textLabel3_3, 1, 0, 1, 1)
        self.editorLexerCombo = QtWidgets.QComboBox(LexerAssociationDialog)
        self.editorLexerCombo.setObjectName("editorLexerCombo")
        self.gridLayout.addWidget(self.editorLexerCombo, 1, 1, 1, 1)
        self.deleteLexerButton = QtWidgets.QPushButton(LexerAssociationDialog)
        self.deleteLexerButton.setObjectName("deleteLexerButton")
        self.gridLayout.addWidget(self.deleteLexerButton, 1, 2, 1, 1)
        self.pygmentsLabel = QtWidgets.QLabel(LexerAssociationDialog)
        self.pygmentsLabel.setObjectName("pygmentsLabel")
        self.gridLayout.addWidget(self.pygmentsLabel, 2, 0, 1, 1)
        self.pygmentsLexerCombo = QtWidgets.QComboBox(LexerAssociationDialog)
        self.pygmentsLexerCombo.setObjectName("pygmentsLexerCombo")
        self.gridLayout.addWidget(self.pygmentsLexerCombo, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(LexerAssociationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.textLabel2_6.setBuddy(self.editorFileExtEdit)
        self.textLabel3_3.setBuddy(self.editorLexerCombo)
        self.pygmentsLabel.setBuddy(self.pygmentsLexerCombo)

        self.retranslateUi(LexerAssociationDialog)
        self.buttonBox.accepted.connect(LexerAssociationDialog.accept)
        self.buttonBox.rejected.connect(LexerAssociationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LexerAssociationDialog)
        LexerAssociationDialog.setTabOrder(self.editorLexerList, self.editorFileExtEdit)
        LexerAssociationDialog.setTabOrder(self.editorFileExtEdit, self.editorLexerCombo)
        LexerAssociationDialog.setTabOrder(self.editorLexerCombo, self.pygmentsLexerCombo)
        LexerAssociationDialog.setTabOrder(self.pygmentsLexerCombo, self.addLexerButton)
        LexerAssociationDialog.setTabOrder(self.addLexerButton, self.deleteLexerButton)
        LexerAssociationDialog.setTabOrder(self.deleteLexerButton, self.buttonBox)

    def retranslateUi(self, LexerAssociationDialog):
        _translate = QtCore.QCoreApplication.translate
        LexerAssociationDialog.setWindowTitle(_translate("LexerAssociationDialog", "Project Lexer Associations"))
        self.editorLexerList.setSortingEnabled(True)
        self.editorLexerList.headerItem().setText(0, _translate("LexerAssociationDialog", "Filename Pattern"))
        self.editorLexerList.headerItem().setText(1, _translate("LexerAssociationDialog", "Lexer Language"))
        self.textLabel2_6.setText(_translate("LexerAssociationDialog", "Filename &Pattern:"))
        self.editorFileExtEdit.setToolTip(_translate("LexerAssociationDialog", "Enter the filename pattern to be associated"))
        self.addLexerButton.setToolTip(_translate("LexerAssociationDialog", "Press to add or change the entered association"))
        self.addLexerButton.setText(_translate("LexerAssociationDialog", "Add/&Change"))
        self.textLabel3_3.setText(_translate("LexerAssociationDialog", "&Lexer Language:"))
        self.editorLexerCombo.setToolTip(_translate("LexerAssociationDialog", "Select the lexer language to associate"))
        self.deleteLexerButton.setToolTip(_translate("LexerAssociationDialog", "Press to delete the selected association"))
        self.deleteLexerButton.setText(_translate("LexerAssociationDialog", "&Delete"))
        self.pygmentsLabel.setText(_translate("LexerAssociationDialog", "Alternative Le&xer:"))
        self.pygmentsLexerCombo.setToolTip(_translate("LexerAssociationDialog", "Select the alternative lexer to associate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LexerAssociationDialog = QtWidgets.QDialog()
    ui = Ui_LexerAssociationDialog()
    ui.setupUi(LexerAssociationDialog)
    LexerAssociationDialog.show()
    sys.exit(app.exec_())

