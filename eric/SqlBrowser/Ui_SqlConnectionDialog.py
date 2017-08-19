# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\SqlBrowser\SqlConnectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SqlConnectionDialog(object):
    def setupUi(self, SqlConnectionDialog):
        SqlConnectionDialog.setObjectName("SqlConnectionDialog")
        SqlConnectionDialog.resize(500, 210)
        self.gridLayout = QtWidgets.QGridLayout(SqlConnectionDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel2 = QtWidgets.QLabel(SqlConnectionDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridLayout.addWidget(self.textLabel2, 0, 0, 1, 1)
        self.driverCombo = QtWidgets.QComboBox(SqlConnectionDialog)
        self.driverCombo.setObjectName("driverCombo")
        self.gridLayout.addWidget(self.driverCombo, 0, 1, 1, 1)
        self.textLabel3 = QtWidgets.QLabel(SqlConnectionDialog)
        self.textLabel3.setObjectName("textLabel3")
        self.gridLayout.addWidget(self.textLabel3, 1, 0, 1, 1)
        self.databasePicker = E5PathPicker(SqlConnectionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databasePicker.sizePolicy().hasHeightForWidth())
        self.databasePicker.setSizePolicy(sizePolicy)
        self.databasePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.databasePicker.setObjectName("databasePicker")
        self.gridLayout.addWidget(self.databasePicker, 1, 1, 1, 1)
        self.textLabel4 = QtWidgets.QLabel(SqlConnectionDialog)
        self.textLabel4.setObjectName("textLabel4")
        self.gridLayout.addWidget(self.textLabel4, 2, 0, 1, 1)
        self.usernameEdit = QtWidgets.QLineEdit(SqlConnectionDialog)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridLayout.addWidget(self.usernameEdit, 2, 1, 1, 1)
        self.textLabel4_2 = QtWidgets.QLabel(SqlConnectionDialog)
        self.textLabel4_2.setObjectName("textLabel4_2")
        self.gridLayout.addWidget(self.textLabel4_2, 3, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(SqlConnectionDialog)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 3, 1, 1, 1)
        self.textLabel5 = QtWidgets.QLabel(SqlConnectionDialog)
        self.textLabel5.setObjectName("textLabel5")
        self.gridLayout.addWidget(self.textLabel5, 4, 0, 1, 1)
        self.hostnameEdit = QtWidgets.QLineEdit(SqlConnectionDialog)
        self.hostnameEdit.setObjectName("hostnameEdit")
        self.gridLayout.addWidget(self.hostnameEdit, 4, 1, 1, 1)
        self.textLabel5_2 = QtWidgets.QLabel(SqlConnectionDialog)
        self.textLabel5_2.setObjectName("textLabel5_2")
        self.gridLayout.addWidget(self.textLabel5_2, 5, 0, 1, 1)
        self.portSpinBox = QtWidgets.QSpinBox(SqlConnectionDialog)
        self.portSpinBox.setMinimum(-1)
        self.portSpinBox.setMaximum(65535)
        self.portSpinBox.setProperty("value", -1)
        self.portSpinBox.setObjectName("portSpinBox")
        self.gridLayout.addWidget(self.portSpinBox, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SqlConnectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.textLabel2.setBuddy(self.driverCombo)
        self.textLabel3.setBuddy(self.databasePicker)
        self.textLabel4.setBuddy(self.usernameEdit)
        self.textLabel4_2.setBuddy(self.passwordEdit)
        self.textLabel5.setBuddy(self.hostnameEdit)
        self.textLabel5_2.setBuddy(self.portSpinBox)

        self.retranslateUi(SqlConnectionDialog)
        self.buttonBox.accepted.connect(SqlConnectionDialog.accept)
        self.buttonBox.rejected.connect(SqlConnectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SqlConnectionDialog)
        SqlConnectionDialog.setTabOrder(self.driverCombo, self.databasePicker)
        SqlConnectionDialog.setTabOrder(self.databasePicker, self.usernameEdit)
        SqlConnectionDialog.setTabOrder(self.usernameEdit, self.passwordEdit)
        SqlConnectionDialog.setTabOrder(self.passwordEdit, self.hostnameEdit)
        SqlConnectionDialog.setTabOrder(self.hostnameEdit, self.portSpinBox)

    def retranslateUi(self, SqlConnectionDialog):
        _translate = QtCore.QCoreApplication.translate
        SqlConnectionDialog.setWindowTitle(_translate("SqlConnectionDialog", "Connect..."))
        self.textLabel2.setText(_translate("SqlConnectionDialog", "D&river:"))
        self.driverCombo.setToolTip(_translate("SqlConnectionDialog", "Select the database driver"))
        self.textLabel3.setText(_translate("SqlConnectionDialog", "&Database Name:"))
        self.databasePicker.setToolTip(_translate("SqlConnectionDialog", "Enter the database name"))
        self.textLabel4.setText(_translate("SqlConnectionDialog", "&Username:"))
        self.usernameEdit.setToolTip(_translate("SqlConnectionDialog", "Enter the user name"))
        self.textLabel4_2.setText(_translate("SqlConnectionDialog", "&Password:"))
        self.textLabel5.setText(_translate("SqlConnectionDialog", "&Hostname:"))
        self.hostnameEdit.setToolTip(_translate("SqlConnectionDialog", "Enter the hostname"))
        self.textLabel5_2.setText(_translate("SqlConnectionDialog", "P&ort:"))
        self.portSpinBox.setToolTip(_translate("SqlConnectionDialog", "Enter the port number"))
        self.portSpinBox.setSpecialValueText(_translate("SqlConnectionDialog", "Default"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SqlConnectionDialog = QtWidgets.QDialog()
    ui = Ui_SqlConnectionDialog()
    ui.setupUi(SqlConnectionDialog)
    SqlConnectionDialog.show()
    sys.exit(app.exec_())

