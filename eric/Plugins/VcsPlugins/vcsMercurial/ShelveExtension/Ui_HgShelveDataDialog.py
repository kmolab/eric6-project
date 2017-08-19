# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\ShelveExtension\HgShelveDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgShelveDataDialog(object):
    def setupUi(self, HgShelveDataDialog):
        HgShelveDataDialog.setObjectName("HgShelveDataDialog")
        HgShelveDataDialog.resize(500, 170)
        HgShelveDataDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgShelveDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgShelveDataDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(HgShelveDataDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(HgShelveDataDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(HgShelveDataDialog)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        spacerItem = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HgShelveDataDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.messageEdit = QtWidgets.QLineEdit(HgShelveDataDialog)
        self.messageEdit.setObjectName("messageEdit")
        self.gridLayout.addWidget(self.messageEdit, 2, 1, 1, 1)
        self.addRemoveCheckBox = QtWidgets.QCheckBox(HgShelveDataDialog)
        self.addRemoveCheckBox.setObjectName("addRemoveCheckBox")
        self.gridLayout.addWidget(self.addRemoveCheckBox, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgShelveDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(HgShelveDataDialog)
        self.buttonBox.accepted.connect(HgShelveDataDialog.accept)
        self.buttonBox.rejected.connect(HgShelveDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgShelveDataDialog)
        HgShelveDataDialog.setTabOrder(self.nameEdit, self.dateTimeEdit)
        HgShelveDataDialog.setTabOrder(self.dateTimeEdit, self.messageEdit)
        HgShelveDataDialog.setTabOrder(self.messageEdit, self.addRemoveCheckBox)
        HgShelveDataDialog.setTabOrder(self.addRemoveCheckBox, self.buttonBox)

    def retranslateUi(self, HgShelveDataDialog):
        _translate = QtCore.QCoreApplication.translate
        HgShelveDataDialog.setWindowTitle(_translate("HgShelveDataDialog", "Shelve"))
        self.label.setText(_translate("HgShelveDataDialog", "Name:"))
        self.nameEdit.setToolTip(_translate("HgShelveDataDialog", "Enter a name for the shelve"))
        self.label_2.setText(_translate("HgShelveDataDialog", "Date, Time:"))
        self.dateTimeEdit.setStatusTip(_translate("HgShelveDataDialog", "Enter the commit date and time for the shelve"))
        self.dateTimeEdit.setDisplayFormat(_translate("HgShelveDataDialog", "yyyy-MM-dd HH:mm"))
        self.label_3.setText(_translate("HgShelveDataDialog", "Message:"))
        self.messageEdit.setToolTip(_translate("HgShelveDataDialog", "Enter a message for the shelve"))
        self.addRemoveCheckBox.setText(_translate("HgShelveDataDialog", "Mark new/missing files as added/removed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgShelveDataDialog = QtWidgets.QDialog()
    ui = Ui_HgShelveDataDialog()
    ui.setupUi(HgShelveDataDialog)
    HgShelveDataDialog.show()
    sys.exit(app.exec_())

