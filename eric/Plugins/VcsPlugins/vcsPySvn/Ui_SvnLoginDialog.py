# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnLoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnLoginDialog(object):
    def setupUi(self, SvnLoginDialog):
        SvnLoginDialog.setObjectName("SvnLoginDialog")
        SvnLoginDialog.resize(400, 145)
        SvnLoginDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnLoginDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.saveCheckBox = QtWidgets.QCheckBox(SvnLoginDialog)
        self.saveCheckBox.setObjectName("saveCheckBox")
        self.gridlayout.addWidget(self.saveCheckBox, 3, 0, 1, 2)
        self.passwordEdit = QtWidgets.QLineEdit(SvnLoginDialog)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridlayout.addWidget(self.passwordEdit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(SvnLoginDialog)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(SvnLoginDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.realmLabel = QtWidgets.QLabel(SvnLoginDialog)
        self.realmLabel.setText("")
        self.realmLabel.setObjectName("realmLabel")
        self.gridlayout.addWidget(self.realmLabel, 0, 0, 1, 2)
        self.usernameEdit = QtWidgets.QLineEdit(SvnLoginDialog)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridlayout.addWidget(self.usernameEdit, 1, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnLoginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnLoginDialog)
        self.buttonBox.accepted.connect(SvnLoginDialog.accept)
        self.buttonBox.rejected.connect(SvnLoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnLoginDialog)
        SvnLoginDialog.setTabOrder(self.usernameEdit, self.passwordEdit)
        SvnLoginDialog.setTabOrder(self.passwordEdit, self.saveCheckBox)

    def retranslateUi(self, SvnLoginDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnLoginDialog.setWindowTitle(_translate("SvnLoginDialog", "Subversion Login"))
        self.saveCheckBox.setToolTip(_translate("SvnLoginDialog", "Select, if the login data should be saved."))
        self.saveCheckBox.setText(_translate("SvnLoginDialog", "Save login data"))
        self.passwordEdit.setToolTip(_translate("SvnLoginDialog", "Enter password"))
        self.label_2.setText(_translate("SvnLoginDialog", "Password:"))
        self.label.setText(_translate("SvnLoginDialog", "Username:"))
        self.usernameEdit.setToolTip(_translate("SvnLoginDialog", "Enter username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnLoginDialog = QtWidgets.QDialog()
    ui = Ui_SvnLoginDialog()
    ui.setupUi(SvnLoginDialog)
    SvnLoginDialog.show()
    sys.exit(app.exec_())

