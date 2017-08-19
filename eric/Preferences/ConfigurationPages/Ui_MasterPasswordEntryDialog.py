# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\MasterPasswordEntryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MasterPasswordEntryDialog(object):
    def setupUi(self, MasterPasswordEntryDialog):
        MasterPasswordEntryDialog.setObjectName("MasterPasswordEntryDialog")
        MasterPasswordEntryDialog.resize(450, 300)
        MasterPasswordEntryDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(MasterPasswordEntryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MasterPasswordEntryDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(MasterPasswordEntryDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.currentPasswordEdit = QtWidgets.QLineEdit(MasterPasswordEntryDialog)
        self.currentPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.currentPasswordEdit.setObjectName("currentPasswordEdit")
        self.gridLayout.addWidget(self.currentPasswordEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(MasterPasswordEntryDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.newPasswordEdit = QtWidgets.QLineEdit(MasterPasswordEntryDialog)
        self.newPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordEdit.setObjectName("newPasswordEdit")
        self.gridLayout.addWidget(self.newPasswordEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(MasterPasswordEntryDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.newPasswordAgainEdit = QtWidgets.QLineEdit(MasterPasswordEntryDialog)
        self.newPasswordAgainEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordAgainEdit.setObjectName("newPasswordAgainEdit")
        self.gridLayout.addWidget(self.newPasswordAgainEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.passwordMeter = E5PasswordMeter(MasterPasswordEntryDialog)
        self.passwordMeter.setObjectName("passwordMeter")
        self.verticalLayout.addWidget(self.passwordMeter)
        self.errorLabel = QtWidgets.QLabel(MasterPasswordEntryDialog)
        self.errorLabel.setStyleSheet("color : red;")
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout.addWidget(self.errorLabel)
        self.buttonBox = QtWidgets.QDialogButtonBox(MasterPasswordEntryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MasterPasswordEntryDialog)
        self.buttonBox.accepted.connect(MasterPasswordEntryDialog.accept)
        self.buttonBox.rejected.connect(MasterPasswordEntryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MasterPasswordEntryDialog)
        MasterPasswordEntryDialog.setTabOrder(self.currentPasswordEdit, self.newPasswordEdit)
        MasterPasswordEntryDialog.setTabOrder(self.newPasswordEdit, self.newPasswordAgainEdit)
        MasterPasswordEntryDialog.setTabOrder(self.newPasswordAgainEdit, self.buttonBox)

    def retranslateUi(self, MasterPasswordEntryDialog):
        _translate = QtCore.QCoreApplication.translate
        MasterPasswordEntryDialog.setWindowTitle(_translate("MasterPasswordEntryDialog", "Master Password"))
        self.label.setText(_translate("MasterPasswordEntryDialog", "<p>Enter your master password below. This password will be used to encrypt sensitive data. You will be asked once per session for this password when the data needs to be accessed for the first time.<br/><br/><b>Note: If you forget the master password, the encrypted data cannot be recovered!</b></p>"))
        self.label_2.setText(_translate("MasterPasswordEntryDialog", "Current Password:"))
        self.currentPasswordEdit.setToolTip(_translate("MasterPasswordEntryDialog", "Enter the current password"))
        self.label_3.setText(_translate("MasterPasswordEntryDialog", "New Password:"))
        self.newPasswordEdit.setToolTip(_translate("MasterPasswordEntryDialog", "Enter the new password"))
        self.label_4.setText(_translate("MasterPasswordEntryDialog", "New Password (again):"))
        self.newPasswordAgainEdit.setToolTip(_translate("MasterPasswordEntryDialog", "Repeat the new password"))
        self.passwordMeter.setToolTip(_translate("MasterPasswordEntryDialog", "Shows an indication for the password strength"))

from E5Gui.E5PasswordMeter import E5PasswordMeter

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MasterPasswordEntryDialog = QtWidgets.QDialog()
    ui = Ui_MasterPasswordEntryDialog()
    ui.setupUi(MasterPasswordEntryDialog)
    MasterPasswordEntryDialog.show()
    sys.exit(app.exec_())

