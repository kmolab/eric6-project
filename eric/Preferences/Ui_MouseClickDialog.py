# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\MouseClickDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MouseClickDialog(object):
    def setupUi(self, MouseClickDialog):
        MouseClickDialog.setObjectName("MouseClickDialog")
        MouseClickDialog.resize(550, 137)
        MouseClickDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(MouseClickDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clickGroup = QtWidgets.QGroupBox(MouseClickDialog)
        self.clickGroup.setTitle("")
        self.clickGroup.setObjectName("clickGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.clickGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.clearButton = QtWidgets.QPushButton(self.clickGroup)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 0, 1, 1)
        self.clickEdit = QtWidgets.QLineEdit(self.clickGroup)
        self.clickEdit.setReadOnly(True)
        self.clickEdit.setObjectName("clickEdit")
        self.gridLayout.addWidget(self.clickEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.clickGroup)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.clickGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(MouseClickDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MouseClickDialog)
        self.buttonBox.accepted.connect(MouseClickDialog.accept)
        self.buttonBox.rejected.connect(MouseClickDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MouseClickDialog)

    def retranslateUi(self, MouseClickDialog):
        _translate = QtCore.QCoreApplication.translate
        MouseClickDialog.setWindowTitle(_translate("MouseClickDialog", "Edit Mouse Click"))
        self.clearButton.setToolTip(_translate("MouseClickDialog", "Press to clear the mouse click sequence."))
        self.clearButton.setText(_translate("MouseClickDialog", "Clear"))
        self.label.setText(_translate("MouseClickDialog", "Press the desired modifier keys and then click the desired mouse button."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MouseClickDialog = QtWidgets.QDialog()
    ui = Ui_MouseClickDialog()
    ui.setupUi(MouseClickDialog)
    MouseClickDialog.show()
    sys.exit(app.exec_())

