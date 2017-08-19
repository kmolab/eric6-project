# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Network\IRC\IrcChannelEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IrcChannelEditDialog(object):
    def setupUi(self, IrcChannelEditDialog):
        IrcChannelEditDialog.setObjectName("IrcChannelEditDialog")
        IrcChannelEditDialog.resize(303, 128)
        IrcChannelEditDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(IrcChannelEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(IrcChannelEditDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(IrcChannelEditDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(IrcChannelEditDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.keyEdit = QtWidgets.QLineEdit(IrcChannelEditDialog)
        self.keyEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.keyEdit.setObjectName("keyEdit")
        self.gridLayout.addWidget(self.keyEdit, 1, 1, 1, 1)
        self.autoJoinCheckBox = QtWidgets.QCheckBox(IrcChannelEditDialog)
        self.autoJoinCheckBox.setObjectName("autoJoinCheckBox")
        self.gridLayout.addWidget(self.autoJoinCheckBox, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(IrcChannelEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(IrcChannelEditDialog)
        self.buttonBox.accepted.connect(IrcChannelEditDialog.accept)
        self.buttonBox.rejected.connect(IrcChannelEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IrcChannelEditDialog)
        IrcChannelEditDialog.setTabOrder(self.nameEdit, self.keyEdit)
        IrcChannelEditDialog.setTabOrder(self.keyEdit, self.autoJoinCheckBox)
        IrcChannelEditDialog.setTabOrder(self.autoJoinCheckBox, self.buttonBox)

    def retranslateUi(self, IrcChannelEditDialog):
        _translate = QtCore.QCoreApplication.translate
        IrcChannelEditDialog.setWindowTitle(_translate("IrcChannelEditDialog", "IRC Channel"))
        self.label.setText(_translate("IrcChannelEditDialog", "Name:"))
        self.nameEdit.setToolTip(_translate("IrcChannelEditDialog", "Enter the channel name"))
        self.label_2.setText(_translate("IrcChannelEditDialog", "Key:"))
        self.keyEdit.setToolTip(_translate("IrcChannelEditDialog", "Enter the channel key/password"))
        self.autoJoinCheckBox.setToolTip(_translate("IrcChannelEditDialog", "Select to join this channel automatically"))
        self.autoJoinCheckBox.setText(_translate("IrcChannelEditDialog", "Join channel automatically"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IrcChannelEditDialog = QtWidgets.QDialog()
    ui = Ui_IrcChannelEditDialog()
    ui.setupUi(IrcChannelEditDialog)
    IrcChannelEditDialog.show()
    sys.exit(app.exec_())

