# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Network\IRC\IrcServerEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IrcServerEditDialog(object):
    def setupUi(self, IrcServerEditDialog):
        IrcServerEditDialog.setObjectName("IrcServerEditDialog")
        IrcServerEditDialog.resize(400, 158)
        IrcServerEditDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(IrcServerEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(IrcServerEditDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.serverEdit = QtWidgets.QLineEdit(IrcServerEditDialog)
        self.serverEdit.setObjectName("serverEdit")
        self.gridLayout.addWidget(self.serverEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(IrcServerEditDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.portSpinBox = QtWidgets.QSpinBox(IrcServerEditDialog)
        self.portSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.portSpinBox.setMinimum(1)
        self.portSpinBox.setMaximum(65535)
        self.portSpinBox.setProperty("value", 6667)
        self.portSpinBox.setObjectName("portSpinBox")
        self.gridLayout.addWidget(self.portSpinBox, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(IrcServerEditDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(IrcServerEditDialog)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 2, 1, 1, 2)
        self.sslCheckBox = QtWidgets.QCheckBox(IrcServerEditDialog)
        self.sslCheckBox.setObjectName("sslCheckBox")
        self.gridLayout.addWidget(self.sslCheckBox, 3, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(IrcServerEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        self.retranslateUi(IrcServerEditDialog)
        self.buttonBox.accepted.connect(IrcServerEditDialog.accept)
        self.buttonBox.rejected.connect(IrcServerEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IrcServerEditDialog)
        IrcServerEditDialog.setTabOrder(self.serverEdit, self.portSpinBox)
        IrcServerEditDialog.setTabOrder(self.portSpinBox, self.passwordEdit)
        IrcServerEditDialog.setTabOrder(self.passwordEdit, self.sslCheckBox)
        IrcServerEditDialog.setTabOrder(self.sslCheckBox, self.buttonBox)

    def retranslateUi(self, IrcServerEditDialog):
        _translate = QtCore.QCoreApplication.translate
        IrcServerEditDialog.setWindowTitle(_translate("IrcServerEditDialog", "IRC Server"))
        self.label.setText(_translate("IrcServerEditDialog", "Server:"))
        self.serverEdit.setToolTip(_translate("IrcServerEditDialog", "Enter the host name of the IRC server"))
        self.label_2.setText(_translate("IrcServerEditDialog", "Port:"))
        self.portSpinBox.setToolTip(_translate("IrcServerEditDialog", "Enter the port number"))
        self.label_3.setText(_translate("IrcServerEditDialog", "Password:"))
        self.passwordEdit.setToolTip(_translate("IrcServerEditDialog", "Enter the server password"))
        self.sslCheckBox.setToolTip(_translate("IrcServerEditDialog", "Select to use an SSL encrypted connection"))
        self.sslCheckBox.setText(_translate("IrcServerEditDialog", "Use Encrypted Connection (SSL)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IrcServerEditDialog = QtWidgets.QDialog()
    ui = Ui_IrcServerEditDialog()
    ui.setupUi(IrcServerEditDialog)
    IrcServerEditDialog.show()
    sys.exit(app.exec_())

