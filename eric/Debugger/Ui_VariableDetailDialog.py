# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Debugger\VariableDetailDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VariableDetailDialog(object):
    def setupUi(self, VariableDetailDialog):
        VariableDetailDialog.setObjectName("VariableDetailDialog")
        VariableDetailDialog.resize(800, 350)
        VariableDetailDialog.setSizeGripEnabled(True)
        VariableDetailDialog.setModal(True)
        self.gridlayout = QtWidgets.QGridLayout(VariableDetailDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(VariableDetailDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.TextLabel1 = QtWidgets.QLabel(VariableDetailDialog)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.eType = QtWidgets.QLineEdit(VariableDetailDialog)
        self.eType.setReadOnly(True)
        self.eType.setObjectName("eType")
        self.gridlayout.addWidget(self.eType, 1, 1, 1, 1)
        self.eName = QtWidgets.QLineEdit(VariableDetailDialog)
        self.eName.setReadOnly(True)
        self.eName.setObjectName("eName")
        self.gridlayout.addWidget(self.eName, 0, 1, 1, 1)
        self.TextLabel2 = QtWidgets.QLabel(VariableDetailDialog)
        self.TextLabel2.setObjectName("TextLabel2")
        self.gridlayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.TextLabel3 = QtWidgets.QLabel(VariableDetailDialog)
        self.TextLabel3.setAlignment(QtCore.Qt.AlignTop)
        self.TextLabel3.setObjectName("TextLabel3")
        self.gridlayout.addWidget(self.TextLabel3, 2, 0, 1, 1)
        self.eValue = QtWidgets.QTextEdit(VariableDetailDialog)
        self.eValue.setReadOnly(True)
        self.eValue.setAcceptRichText(False)
        self.eValue.setObjectName("eValue")
        self.gridlayout.addWidget(self.eValue, 2, 1, 1, 1)

        self.retranslateUi(VariableDetailDialog)
        self.buttonBox.accepted.connect(VariableDetailDialog.accept)
        self.buttonBox.rejected.connect(VariableDetailDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VariableDetailDialog)
        VariableDetailDialog.setTabOrder(self.eName, self.eType)
        VariableDetailDialog.setTabOrder(self.eType, self.eValue)

    def retranslateUi(self, VariableDetailDialog):
        _translate = QtCore.QCoreApplication.translate
        VariableDetailDialog.setWindowTitle(_translate("VariableDetailDialog", "Variable Details"))
        self.TextLabel1.setText(_translate("VariableDetailDialog", "Name:"))
        self.TextLabel2.setText(_translate("VariableDetailDialog", "Type:"))
        self.TextLabel3.setText(_translate("VariableDetailDialog", "Value:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VariableDetailDialog = QtWidgets.QDialog()
    ui = Ui_VariableDetailDialog()
    ui.setupUi(VariableDetailDialog)
    VariableDetailDialog.show()
    sys.exit(app.exec_())

