# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\PersonalInformationManager\PersonalDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PersonalDataDialog(object):
    def setupUi(self, PersonalDataDialog):
        PersonalDataDialog.setObjectName("PersonalDataDialog")
        PersonalDataDialog.resize(600, 400)
        PersonalDataDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PersonalDataDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.iconLabel = QtWidgets.QLabel(PersonalDataDialog)
        self.iconLabel.setMinimumSize(QtCore.QSize(48, 48))
        self.iconLabel.setText("Icon")
        self.iconLabel.setObjectName("iconLabel")
        self.horizontalLayout.addWidget(self.iconLabel)
        self.label = QtWidgets.QLabel(PersonalDataDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_01 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_01.setAlignment(QtCore.Qt.AlignCenter)
        self.label_01.setWordWrap(True)
        self.label_01.setObjectName("label_01")
        self.verticalLayout.addWidget(self.label_01)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_02 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_02.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_02.setObjectName("label_02")
        self.gridLayout.addWidget(self.label_02, 0, 0, 1, 1)
        self.firstnameEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.firstnameEdit.setObjectName("firstnameEdit")
        self.gridLayout.addWidget(self.firstnameEdit, 0, 1, 1, 1)
        self.label_08 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_08.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_08.setObjectName("label_08")
        self.gridLayout.addWidget(self.label_08, 0, 2, 1, 1)
        self.zipEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.zipEdit.setObjectName("zipEdit")
        self.gridLayout.addWidget(self.zipEdit, 0, 3, 1, 1)
        self.label_03 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_03.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_03.setObjectName("label_03")
        self.gridLayout.addWidget(self.label_03, 1, 0, 1, 1)
        self.lastnameEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.lastnameEdit.setObjectName("lastnameEdit")
        self.gridLayout.addWidget(self.lastnameEdit, 1, 1, 1, 1)
        self.label_09 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_09.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_09.setObjectName("label_09")
        self.gridLayout.addWidget(self.label_09, 1, 2, 1, 1)
        self.stateEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.stateEdit.setObjectName("stateEdit")
        self.gridLayout.addWidget(self.stateEdit, 1, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)
        self.fullnameEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.fullnameEdit.setObjectName("fullnameEdit")
        self.gridLayout.addWidget(self.fullnameEdit, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)
        self.countryEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.countryEdit.setObjectName("countryEdit")
        self.gridLayout.addWidget(self.countryEdit, 2, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        self.emailEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.emailEdit.setObjectName("emailEdit")
        self.gridLayout.addWidget(self.emailEdit, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 2, 1, 1)
        self.homepageEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.homepageEdit.setObjectName("homepageEdit")
        self.gridLayout.addWidget(self.homepageEdit, 3, 3, 1, 1)
        self.label_04 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_04.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_04.setObjectName("label_04")
        self.gridLayout.addWidget(self.label_04, 4, 0, 1, 1)
        self.phoneEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.phoneEdit.setObjectName("phoneEdit")
        self.gridLayout.addWidget(self.phoneEdit, 4, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 2, 1, 1)
        self.special1Edit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.special1Edit.setObjectName("special1Edit")
        self.gridLayout.addWidget(self.special1Edit, 4, 3, 1, 1)
        self.label_05 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_05.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_05.setObjectName("label_05")
        self.gridLayout.addWidget(self.label_05, 5, 0, 1, 1)
        self.mobileEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.mobileEdit.setObjectName("mobileEdit")
        self.gridLayout.addWidget(self.mobileEdit, 5, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 2, 1, 1)
        self.special2Edit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.special2Edit.setObjectName("special2Edit")
        self.gridLayout.addWidget(self.special2Edit, 5, 3, 1, 1)
        self.label_06 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_06.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_06.setObjectName("label_06")
        self.gridLayout.addWidget(self.label_06, 6, 0, 1, 1)
        self.addressEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.addressEdit.setObjectName("addressEdit")
        self.gridLayout.addWidget(self.addressEdit, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 6, 2, 1, 1)
        self.special3Edit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.special3Edit.setObjectName("special3Edit")
        self.gridLayout.addWidget(self.special3Edit, 6, 3, 1, 1)
        self.label_07 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_07.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_07.setObjectName("label_07")
        self.gridLayout.addWidget(self.label_07, 7, 0, 1, 1)
        self.cityEdit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.cityEdit.setObjectName("cityEdit")
        self.gridLayout.addWidget(self.cityEdit, 7, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 2, 1, 1)
        self.special4Edit = QtWidgets.QLineEdit(PersonalDataDialog)
        self.special4Edit.setObjectName("special4Edit")
        self.gridLayout.addWidget(self.special4Edit, 7, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_16 = QtWidgets.QLabel(PersonalDataDialog)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        spacerItem2 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PersonalDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PersonalDataDialog)
        self.buttonBox.accepted.connect(PersonalDataDialog.accept)
        self.buttonBox.rejected.connect(PersonalDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PersonalDataDialog)
        PersonalDataDialog.setTabOrder(self.firstnameEdit, self.lastnameEdit)
        PersonalDataDialog.setTabOrder(self.lastnameEdit, self.fullnameEdit)
        PersonalDataDialog.setTabOrder(self.fullnameEdit, self.emailEdit)
        PersonalDataDialog.setTabOrder(self.emailEdit, self.phoneEdit)
        PersonalDataDialog.setTabOrder(self.phoneEdit, self.mobileEdit)
        PersonalDataDialog.setTabOrder(self.mobileEdit, self.addressEdit)
        PersonalDataDialog.setTabOrder(self.addressEdit, self.cityEdit)
        PersonalDataDialog.setTabOrder(self.cityEdit, self.zipEdit)
        PersonalDataDialog.setTabOrder(self.zipEdit, self.stateEdit)
        PersonalDataDialog.setTabOrder(self.stateEdit, self.countryEdit)
        PersonalDataDialog.setTabOrder(self.countryEdit, self.homepageEdit)
        PersonalDataDialog.setTabOrder(self.homepageEdit, self.special1Edit)
        PersonalDataDialog.setTabOrder(self.special1Edit, self.special2Edit)
        PersonalDataDialog.setTabOrder(self.special2Edit, self.special3Edit)
        PersonalDataDialog.setTabOrder(self.special3Edit, self.special4Edit)
        PersonalDataDialog.setTabOrder(self.special4Edit, self.buttonBox)

    def retranslateUi(self, PersonalDataDialog):
        _translate = QtCore.QCoreApplication.translate
        PersonalDataDialog.setWindowTitle(_translate("PersonalDataDialog", "Personal Information"))
        self.label.setText(_translate("PersonalDataDialog", "<h2>Personal Information</h2>"))
        self.label_01.setText(_translate("PersonalDataDialog", "Your personal information that will be used on webpages."))
        self.label_02.setText(_translate("PersonalDataDialog", "First Name:"))
        self.label_08.setText(_translate("PersonalDataDialog", "ZIP Code:"))
        self.label_03.setText(_translate("PersonalDataDialog", "Last Name:"))
        self.label_09.setText(_translate("PersonalDataDialog", "State/Region:"))
        self.label_18.setText(_translate("PersonalDataDialog", "Full Name:"))
        self.label_10.setText(_translate("PersonalDataDialog", "Country:"))
        self.label_12.setText(_translate("PersonalDataDialog", "E-mail:"))
        self.label_11.setText(_translate("PersonalDataDialog", "Home Page:"))
        self.label_04.setText(_translate("PersonalDataDialog", "Phone:"))
        self.label_13.setText(_translate("PersonalDataDialog", "Custom 1:"))
        self.label_05.setText(_translate("PersonalDataDialog", "Mobile Phone:"))
        self.label_14.setText(_translate("PersonalDataDialog", "Custom 2:"))
        self.label_06.setText(_translate("PersonalDataDialog", "Address:"))
        self.label_15.setText(_translate("PersonalDataDialog", "Custom 3:"))
        self.label_07.setText(_translate("PersonalDataDialog", "City:"))
        self.label_17.setText(_translate("PersonalDataDialog", "Custom 4:"))
        self.label_16.setText(_translate("PersonalDataDialog", "<b>Note:</b> Press Ctrl+ENTER to autofill form fields for which personal entries were found."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PersonalDataDialog = QtWidgets.QDialog()
    ui = Ui_PersonalDataDialog()
    ui.setupUi(PersonalDataDialog)
    PersonalDataDialog.show()
    sys.exit(app.exec_())

