# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Templates\TemplateSingleVariableDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TemplateSingleVariableDialog(object):
    def setupUi(self, TemplateSingleVariableDialog):
        TemplateSingleVariableDialog.setObjectName("TemplateSingleVariableDialog")
        TemplateSingleVariableDialog.resize(403, 218)
        TemplateSingleVariableDialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(TemplateSingleVariableDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.variableEdit = QtWidgets.QTextEdit(TemplateSingleVariableDialog)
        self.variableEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.variableEdit.setAcceptRichText(False)
        self.variableEdit.setObjectName("variableEdit")
        self.gridlayout.addWidget(self.variableEdit, 0, 1, 1, 1)
        self.variableLabel = QtWidgets.QLabel(TemplateSingleVariableDialog)
        self.variableLabel.setAlignment(QtCore.Qt.AlignTop)
        self.variableLabel.setObjectName("variableLabel")
        self.gridlayout.addWidget(self.variableLabel, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(TemplateSingleVariableDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(TemplateSingleVariableDialog)
        self.buttonBox.accepted.connect(TemplateSingleVariableDialog.accept)
        self.buttonBox.rejected.connect(TemplateSingleVariableDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TemplateSingleVariableDialog)

    def retranslateUi(self, TemplateSingleVariableDialog):
        _translate = QtCore.QCoreApplication.translate
        TemplateSingleVariableDialog.setWindowTitle(_translate("TemplateSingleVariableDialog", "Enter Template Variable"))
        self.variableEdit.setToolTip(_translate("TemplateSingleVariableDialog", "Enter the value for the variable."))
        self.variableLabel.setText(_translate("TemplateSingleVariableDialog", "Variable:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TemplateSingleVariableDialog = QtWidgets.QDialog()
    ui = Ui_TemplateSingleVariableDialog()
    ui.setupUi(TemplateSingleVariableDialog)
    TemplateSingleVariableDialog.show()
    sys.exit(app.exec_())

