# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Sync\SyncEncryptionPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SyncEncryptionPage(object):
    def setupUi(self, SyncEncryptionPage):
        SyncEncryptionPage.setObjectName("SyncEncryptionPage")
        SyncEncryptionPage.resize(650, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(SyncEncryptionPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.encryptionGroupBox = QtWidgets.QGroupBox(SyncEncryptionPage)
        self.encryptionGroupBox.setCheckable(True)
        self.encryptionGroupBox.setObjectName("encryptionGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.encryptionGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.encryptionGroupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.reencryptCheckBox = QtWidgets.QCheckBox(self.encryptionGroupBox)
        self.reencryptCheckBox.setObjectName("reencryptCheckBox")
        self.gridLayout.addWidget(self.reencryptCheckBox, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.encryptionGroupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.encryptionKeyEdit = QtWidgets.QLineEdit(self.encryptionGroupBox)
        self.encryptionKeyEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.encryptionKeyEdit.setObjectName("encryptionKeyEdit")
        self.gridLayout.addWidget(self.encryptionKeyEdit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.encryptionGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.encryptionKeyAgainEdit = QtWidgets.QLineEdit(self.encryptionGroupBox)
        self.encryptionKeyAgainEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.encryptionKeyAgainEdit.setObjectName("encryptionKeyAgainEdit")
        self.gridLayout.addWidget(self.encryptionKeyAgainEdit, 3, 1, 1, 1)
        self.passwordMeter = E5PasswordMeter(self.encryptionGroupBox)
        self.passwordMeter.setObjectName("passwordMeter")
        self.gridLayout.addWidget(self.passwordMeter, 4, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.encryptionGroupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.keySizeComboBox = QtWidgets.QComboBox(self.encryptionGroupBox)
        self.keySizeComboBox.setObjectName("keySizeComboBox")
        self.horizontalLayout.addWidget(self.keySizeComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.errorLabel = QtWidgets.QLabel(self.encryptionGroupBox)
        self.errorLabel.setStyleSheet("color : red;")
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 6, 0, 1, 2)
        self.loginsOnlyCheckBox = QtWidgets.QCheckBox(self.encryptionGroupBox)
        self.loginsOnlyCheckBox.setObjectName("loginsOnlyCheckBox")
        self.gridLayout.addWidget(self.loginsOnlyCheckBox, 7, 0, 1, 2)
        self.verticalLayout.addWidget(self.encryptionGroupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(SyncEncryptionPage)
        QtCore.QMetaObject.connectSlotsByName(SyncEncryptionPage)
        SyncEncryptionPage.setTabOrder(self.encryptionGroupBox, self.reencryptCheckBox)
        SyncEncryptionPage.setTabOrder(self.reencryptCheckBox, self.encryptionKeyEdit)
        SyncEncryptionPage.setTabOrder(self.encryptionKeyEdit, self.encryptionKeyAgainEdit)
        SyncEncryptionPage.setTabOrder(self.encryptionKeyAgainEdit, self.keySizeComboBox)
        SyncEncryptionPage.setTabOrder(self.keySizeComboBox, self.loginsOnlyCheckBox)

    def retranslateUi(self, SyncEncryptionPage):
        _translate = QtCore.QCoreApplication.translate
        SyncEncryptionPage.setTitle(_translate("SyncEncryptionPage", "Encryption Settings"))
        SyncEncryptionPage.setSubTitle(_translate("SyncEncryptionPage", "Please select, if the synchronized data should be encrypted and enter the encryption key"))
        self.encryptionGroupBox.setToolTip(_translate("SyncEncryptionPage", "Select to encrypt the synchronzed data"))
        self.encryptionGroupBox.setTitle(_translate("SyncEncryptionPage", "Encrypt Data"))
        self.label_3.setText(_translate("SyncEncryptionPage", "<p>The encryption key will be used to encrypt and decrypt the synchronizde data. If the data should be re-encrypted, the respective selection should be done. The key must only be repeated, if a re-encryption is requested.<br/><br/><b>Note: If you forget the encryption key, the encrypted data cannot be recovered!</b><br/></p>"))
        self.reencryptCheckBox.setToolTip(_translate("SyncEncryptionPage", "Select to re-encrypt the synchronized data"))
        self.reencryptCheckBox.setText(_translate("SyncEncryptionPage", "Re-encrypt synchronized data"))
        self.label.setText(_translate("SyncEncryptionPage", "Encryption Key:"))
        self.encryptionKeyEdit.setToolTip(_translate("SyncEncryptionPage", "Enter the encryption key"))
        self.label_2.setText(_translate("SyncEncryptionPage", "Encryption Key (again):"))
        self.encryptionKeyAgainEdit.setToolTip(_translate("SyncEncryptionPage", "Repeat the encryption key"))
        self.passwordMeter.setToolTip(_translate("SyncEncryptionPage", "Shows an indication for the encryption key strength"))
        self.label_4.setText(_translate("SyncEncryptionPage", "Size of generated encryption key:"))
        self.keySizeComboBox.setToolTip(_translate("SyncEncryptionPage", "Select the size of the generated encryption key"))
        self.loginsOnlyCheckBox.setToolTip(_translate("SyncEncryptionPage", "Select to encrypt only the passwords"))
        self.loginsOnlyCheckBox.setText(_translate("SyncEncryptionPage", "Encrypt Passwords Only"))

from E5Gui.E5PasswordMeter import E5PasswordMeter

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SyncEncryptionPage = QtWidgets.QWizardPage()
    ui = Ui_SyncEncryptionPage()
    ui.setupUi(SyncEncryptionPage)
    SyncEncryptionPage.show()
    sys.exit(app.exec_())

