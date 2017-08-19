# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\AdBlock\AdBlockExceptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdBlockExceptionsDialog(object):
    def setupUi(self, AdBlockExceptionsDialog):
        AdBlockExceptionsDialog.setObjectName("AdBlockExceptionsDialog")
        AdBlockExceptionsDialog.resize(550, 450)
        AdBlockExceptionsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(AdBlockExceptionsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.iconLabel = QtWidgets.QLabel(AdBlockExceptionsDialog)
        self.iconLabel.setMinimumSize(QtCore.QSize(48, 48))
        self.iconLabel.setText("Icon")
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout.addWidget(self.iconLabel, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.hostEdit = E5ClearableLineEdit(AdBlockExceptionsDialog)
        self.hostEdit.setObjectName("hostEdit")
        self.gridLayout.addWidget(self.hostEdit, 1, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(AdBlockExceptionsDialog)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 1, 2, 1, 1)
        self.hostList = QtWidgets.QListWidget(AdBlockExceptionsDialog)
        self.hostList.setAlternatingRowColors(True)
        self.hostList.setObjectName("hostList")
        self.gridLayout.addWidget(self.hostList, 2, 0, 2, 2)
        self.deleteButton = QtWidgets.QPushButton(AdBlockExceptionsDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AdBlockExceptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AdBlockExceptionsDialog)
        self.buttonBox.accepted.connect(AdBlockExceptionsDialog.accept)
        self.buttonBox.rejected.connect(AdBlockExceptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AdBlockExceptionsDialog)
        AdBlockExceptionsDialog.setTabOrder(self.hostEdit, self.addButton)
        AdBlockExceptionsDialog.setTabOrder(self.addButton, self.hostList)
        AdBlockExceptionsDialog.setTabOrder(self.hostList, self.deleteButton)
        AdBlockExceptionsDialog.setTabOrder(self.deleteButton, self.buttonBox)

    def retranslateUi(self, AdBlockExceptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        AdBlockExceptionsDialog.setWindowTitle(_translate("AdBlockExceptionsDialog", "AdBlock Exceptions"))
        self.hostEdit.setToolTip(_translate("AdBlockExceptionsDialog", "Enter a host to block AdBlock for"))
        self.addButton.setToolTip(_translate("AdBlockExceptionsDialog", "Press to add the host"))
        self.addButton.setText(_translate("AdBlockExceptionsDialog", "&Add"))
        self.hostList.setSortingEnabled(True)
        self.deleteButton.setToolTip(_translate("AdBlockExceptionsDialog", "Press to delete the selected hosts"))
        self.deleteButton.setText(_translate("AdBlockExceptionsDialog", "&Delete"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdBlockExceptionsDialog = QtWidgets.QDialog()
    ui = Ui_AdBlockExceptionsDialog()
    ui.setupUi(AdBlockExceptionsDialog)
    AdBlockExceptionsDialog.show()
    sys.exit(app.exec_())

