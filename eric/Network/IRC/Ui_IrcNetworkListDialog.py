# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Network\IRC\IrcNetworkListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IrcNetworkListDialog(object):
    def setupUi(self, IrcNetworkListDialog):
        IrcNetworkListDialog.setObjectName("IrcNetworkListDialog")
        IrcNetworkListDialog.resize(500, 350)
        IrcNetworkListDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(IrcNetworkListDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.networksList = QtWidgets.QTreeWidget(IrcNetworkListDialog)
        self.networksList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.networksList.setAlternatingRowColors(True)
        self.networksList.setColumnCount(2)
        self.networksList.setObjectName("networksList")
        self.networksList.headerItem().setText(0, "1")
        self.networksList.headerItem().setText(1, "2")
        self.networksList.header().setVisible(False)
        self.gridLayout.addWidget(self.networksList, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.newButton = QtWidgets.QPushButton(IrcNetworkListDialog)
        self.newButton.setObjectName("newButton")
        self.verticalLayout.addWidget(self.newButton)
        self.editButton = QtWidgets.QPushButton(IrcNetworkListDialog)
        self.editButton.setObjectName("editButton")
        self.verticalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(IrcNetworkListDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.autoConnectButton = QtWidgets.QPushButton(IrcNetworkListDialog)
        self.autoConnectButton.setCheckable(True)
        self.autoConnectButton.setObjectName("autoConnectButton")
        self.verticalLayout.addWidget(self.autoConnectButton)
        self.line = QtWidgets.QFrame(IrcNetworkListDialog)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.editIdentitiesButton = QtWidgets.QPushButton(IrcNetworkListDialog)
        self.editIdentitiesButton.setObjectName("editIdentitiesButton")
        self.verticalLayout.addWidget(self.editIdentitiesButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(IrcNetworkListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(IrcNetworkListDialog)
        self.buttonBox.accepted.connect(IrcNetworkListDialog.accept)
        self.buttonBox.rejected.connect(IrcNetworkListDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IrcNetworkListDialog)
        IrcNetworkListDialog.setTabOrder(self.networksList, self.newButton)
        IrcNetworkListDialog.setTabOrder(self.newButton, self.editButton)
        IrcNetworkListDialog.setTabOrder(self.editButton, self.deleteButton)
        IrcNetworkListDialog.setTabOrder(self.deleteButton, self.autoConnectButton)
        IrcNetworkListDialog.setTabOrder(self.autoConnectButton, self.editIdentitiesButton)
        IrcNetworkListDialog.setTabOrder(self.editIdentitiesButton, self.buttonBox)

    def retranslateUi(self, IrcNetworkListDialog):
        _translate = QtCore.QCoreApplication.translate
        IrcNetworkListDialog.setWindowTitle(_translate("IrcNetworkListDialog", "IRC Networks"))
        self.newButton.setToolTip(_translate("IrcNetworkListDialog", "Press to define a new network"))
        self.newButton.setText(_translate("IrcNetworkListDialog", "&New..."))
        self.editButton.setToolTip(_translate("IrcNetworkListDialog", "Press to edit the selected network"))
        self.editButton.setText(_translate("IrcNetworkListDialog", "&Edit..."))
        self.deleteButton.setToolTip(_translate("IrcNetworkListDialog", "Press to delete the selected network"))
        self.deleteButton.setText(_translate("IrcNetworkListDialog", "&Delete"))
        self.autoConnectButton.setToolTip(_translate("IrcNetworkListDialog", "Press to  toggle the auto-connect flag of the selected network"))
        self.autoConnectButton.setText(_translate("IrcNetworkListDialog", "&Auto-Connect"))
        self.editIdentitiesButton.setToolTip(_translate("IrcNetworkListDialog", "Press to edit the identities"))
        self.editIdentitiesButton.setText(_translate("IrcNetworkListDialog", "Edit &Identities..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IrcNetworkListDialog = QtWidgets.QDialog()
    ui = Ui_IrcNetworkListDialog()
    ui.setupUi(IrcNetworkListDialog)
    IrcNetworkListDialog.show()
    sys.exit(app.exec_())

