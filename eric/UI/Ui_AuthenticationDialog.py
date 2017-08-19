# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\AuthenticationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AuthenticationDialog(object):
    def setupUi(self, AuthenticationDialog):
        AuthenticationDialog.setObjectName("AuthenticationDialog")
        AuthenticationDialog.resize(400, 154)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AuthenticationDialog.sizePolicy().hasHeightForWidth())
        AuthenticationDialog.setSizePolicy(sizePolicy)
        AuthenticationDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(AuthenticationDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iconLabel = QtWidgets.QLabel(AuthenticationDialog)
        self.iconLabel.setObjectName("iconLabel")
        self.horizontalLayout.addWidget(self.iconLabel)
        self.infoLabel = QtWidgets.QLabel(AuthenticationDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout.addWidget(self.infoLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(AuthenticationDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.usernameEdit = QtWidgets.QLineEdit(AuthenticationDialog)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridLayout.addWidget(self.usernameEdit, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(AuthenticationDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(AuthenticationDialog)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 2, 1, 1, 1)
        self.saveCheckBox = QtWidgets.QCheckBox(AuthenticationDialog)
        self.saveCheckBox.setObjectName("saveCheckBox")
        self.gridLayout.addWidget(self.saveCheckBox, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(AuthenticationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(AuthenticationDialog)
        self.buttonBox.accepted.connect(AuthenticationDialog.accept)
        self.buttonBox.rejected.connect(AuthenticationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AuthenticationDialog)
        AuthenticationDialog.setTabOrder(self.usernameEdit, self.passwordEdit)
        AuthenticationDialog.setTabOrder(self.passwordEdit, self.saveCheckBox)
        AuthenticationDialog.setTabOrder(self.saveCheckBox, self.buttonBox)

    def retranslateUi(self, AuthenticationDialog):
        _translate = QtCore.QCoreApplication.translate
        AuthenticationDialog.setWindowTitle(_translate("AuthenticationDialog", "Authentication Required"))
        self.iconLabel.setText(_translate("AuthenticationDialog", "Icon"))
        self.infoLabel.setText(_translate("AuthenticationDialog", "Info"))
        self.label.setText(_translate("AuthenticationDialog", "Username:"))
        self.usernameEdit.setToolTip(_translate("AuthenticationDialog", "Enter username"))
        self.label_2.setText(_translate("AuthenticationDialog", "Password:"))
        self.passwordEdit.setToolTip(_translate("AuthenticationDialog", "Enter password"))
        self.saveCheckBox.setToolTip(_translate("AuthenticationDialog", "Select to save the login data"))
        self.saveCheckBox.setText(_translate("AuthenticationDialog", "Save login data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthenticationDialog = QtWidgets.QDialog()
    ui = Ui_AuthenticationDialog()
    ui.setupUi(AuthenticationDialog)
    AuthenticationDialog.show()
    sys.exit(app.exec_())

