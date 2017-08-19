# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Sync\SyncFtpSettingsPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SyncFtpSettingsPage(object):
    def setupUi(self, SyncFtpSettingsPage):
        SyncFtpSettingsPage.setObjectName("SyncFtpSettingsPage")
        SyncFtpSettingsPage.resize(650, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(SyncFtpSettingsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SyncFtpSettingsPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.serverEdit = QtWidgets.QLineEdit(self.groupBox)
        self.serverEdit.setObjectName("serverEdit")
        self.gridLayout.addWidget(self.serverEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.userNameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userNameEdit.setObjectName("userNameEdit")
        self.gridLayout.addWidget(self.userNameEdit, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.groupBox)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pathEdit = QtWidgets.QLineEdit(self.groupBox)
        self.pathEdit.setObjectName("pathEdit")
        self.gridLayout.addWidget(self.pathEdit, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.portSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.portSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.portSpinBox.setMinimum(1)
        self.portSpinBox.setMaximum(65635)
        self.portSpinBox.setProperty("value", 21)
        self.portSpinBox.setObjectName("portSpinBox")
        self.gridLayout.addWidget(self.portSpinBox, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.idleSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.idleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idleSpinBox.setMinimum(10)
        self.idleSpinBox.setMaximum(3600)
        self.idleSpinBox.setObjectName("idleSpinBox")
        self.gridLayout.addWidget(self.idleSpinBox, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(419, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(SyncFtpSettingsPage)
        QtCore.QMetaObject.connectSlotsByName(SyncFtpSettingsPage)

    def retranslateUi(self, SyncFtpSettingsPage):
        _translate = QtCore.QCoreApplication.translate
        SyncFtpSettingsPage.setTitle(_translate("SyncFtpSettingsPage", "Synchronize to an FTP host"))
        SyncFtpSettingsPage.setSubTitle(_translate("SyncFtpSettingsPage", "Please enter the data for synchronization via FTP. All fields must be filled."))
        self.groupBox.setTitle(_translate("SyncFtpSettingsPage", "Remote FTP Host Settings"))
        self.label.setText(_translate("SyncFtpSettingsPage", "Server:"))
        self.serverEdit.setToolTip(_translate("SyncFtpSettingsPage", "Enter the FTP server name"))
        self.label_2.setText(_translate("SyncFtpSettingsPage", "User Name:"))
        self.userNameEdit.setToolTip(_translate("SyncFtpSettingsPage", "Enter the user name"))
        self.label_3.setText(_translate("SyncFtpSettingsPage", "Password:"))
        self.passwordEdit.setToolTip(_translate("SyncFtpSettingsPage", "Enter the password"))
        self.label_4.setText(_translate("SyncFtpSettingsPage", "Path:"))
        self.pathEdit.setToolTip(_translate("SyncFtpSettingsPage", "Enter the remote path"))
        self.label_5.setText(_translate("SyncFtpSettingsPage", "Port:"))
        self.portSpinBox.setToolTip(_translate("SyncFtpSettingsPage", "Enter the remote port"))
        self.label_6.setText(_translate("SyncFtpSettingsPage", "Idle Timeout:"))
        self.idleSpinBox.setToolTip(_translate("SyncFtpSettingsPage", "Enter the idle timeout interval to prevent a server disconnect"))
        self.idleSpinBox.setSuffix(_translate("SyncFtpSettingsPage", " s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SyncFtpSettingsPage = QtWidgets.QWizardPage()
    ui = Ui_SyncFtpSettingsPage()
    ui.setupUi(SyncFtpSettingsPage)
    SyncFtpSettingsPage.show()
    sys.exit(app.exec_())

