# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\CheckerPlugins\CodeStyleChecker\CodeStyleAddBuiltinIgnoreDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CodeStyleAddBuiltinIgnoreDialog(object):
    def setupUi(self, CodeStyleAddBuiltinIgnoreDialog):
        CodeStyleAddBuiltinIgnoreDialog.setObjectName("CodeStyleAddBuiltinIgnoreDialog")
        CodeStyleAddBuiltinIgnoreDialog.resize(400, 112)
        CodeStyleAddBuiltinIgnoreDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(CodeStyleAddBuiltinIgnoreDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CodeStyleAddBuiltinIgnoreDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(CodeStyleAddBuiltinIgnoreDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.leftEdit = E5ClearableLineEdit(CodeStyleAddBuiltinIgnoreDialog)
        self.leftEdit.setObjectName("leftEdit")
        self.gridLayout.addWidget(self.leftEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(CodeStyleAddBuiltinIgnoreDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.rightEdit = E5ClearableLineEdit(CodeStyleAddBuiltinIgnoreDialog)
        self.rightEdit.setObjectName("rightEdit")
        self.gridLayout.addWidget(self.rightEdit, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CodeStyleAddBuiltinIgnoreDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(CodeStyleAddBuiltinIgnoreDialog)
        self.buttonBox.accepted.connect(CodeStyleAddBuiltinIgnoreDialog.accept)
        self.buttonBox.rejected.connect(CodeStyleAddBuiltinIgnoreDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CodeStyleAddBuiltinIgnoreDialog)

    def retranslateUi(self, CodeStyleAddBuiltinIgnoreDialog):
        _translate = QtCore.QCoreApplication.translate
        CodeStyleAddBuiltinIgnoreDialog.setWindowTitle(_translate("CodeStyleAddBuiltinIgnoreDialog", "Add Built-in Assignment"))
        self.label.setText(_translate("CodeStyleAddBuiltinIgnoreDialog", "Enter the data for a built-in assignment to be ignored:"))
        self.label_2.setText(_translate("CodeStyleAddBuiltinIgnoreDialog", "Left Side:"))
        self.leftEdit.setPlaceholderText(_translate("CodeStyleAddBuiltinIgnoreDialog", "Enter left hand side of assignment"))
        self.label_3.setText(_translate("CodeStyleAddBuiltinIgnoreDialog", "Right Side:"))
        self.rightEdit.setPlaceholderText(_translate("CodeStyleAddBuiltinIgnoreDialog", "Enter right hand side of assignment"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CodeStyleAddBuiltinIgnoreDialog = QtWidgets.QDialog()
    ui = Ui_CodeStyleAddBuiltinIgnoreDialog()
    ui.setupUi(CodeStyleAddBuiltinIgnoreDialog)
    CodeStyleAddBuiltinIgnoreDialog.show()
    sys.exit(app.exec_())

