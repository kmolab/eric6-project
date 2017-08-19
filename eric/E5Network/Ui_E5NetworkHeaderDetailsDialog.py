# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\E5Network\E5NetworkHeaderDetailsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_E5NetworkHeaderDetailsDialog(object):
    def setupUi(self, E5NetworkHeaderDetailsDialog):
        E5NetworkHeaderDetailsDialog.setObjectName("E5NetworkHeaderDetailsDialog")
        E5NetworkHeaderDetailsDialog.resize(500, 350)
        E5NetworkHeaderDetailsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(E5NetworkHeaderDetailsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(E5NetworkHeaderDetailsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(E5NetworkHeaderDetailsDialog)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.label_2 = QtWidgets.QLabel(E5NetworkHeaderDetailsDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.valueEdit = QtWidgets.QPlainTextEdit(E5NetworkHeaderDetailsDialog)
        self.valueEdit.setTabChangesFocus(True)
        self.valueEdit.setReadOnly(True)
        self.valueEdit.setObjectName("valueEdit")
        self.verticalLayout.addWidget(self.valueEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(E5NetworkHeaderDetailsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(E5NetworkHeaderDetailsDialog)
        self.buttonBox.accepted.connect(E5NetworkHeaderDetailsDialog.accept)
        self.buttonBox.rejected.connect(E5NetworkHeaderDetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(E5NetworkHeaderDetailsDialog)

    def retranslateUi(self, E5NetworkHeaderDetailsDialog):
        _translate = QtCore.QCoreApplication.translate
        E5NetworkHeaderDetailsDialog.setWindowTitle(_translate("E5NetworkHeaderDetailsDialog", "Header Details"))
        self.label.setText(_translate("E5NetworkHeaderDetailsDialog", "Name:"))
        self.label_2.setText(_translate("E5NetworkHeaderDetailsDialog", "Value:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    E5NetworkHeaderDetailsDialog = QtWidgets.QDialog()
    ui = Ui_E5NetworkHeaderDetailsDialog()
    ui.setupUi(E5NetworkHeaderDetailsDialog)
    E5NetworkHeaderDetailsDialog.show()
    sys.exit(app.exec_())

