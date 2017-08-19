# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\MultiProject\PropertiesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PropertiesDialog(object):
    def setupUi(self, PropertiesDialog):
        PropertiesDialog.setObjectName("PropertiesDialog")
        PropertiesDialog.resize(530, 227)
        PropertiesDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(PropertiesDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.descriptionLabel = QtWidgets.QLabel(PropertiesDialog)
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignTop)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridlayout.addWidget(self.descriptionLabel, 0, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QTextEdit(PropertiesDialog)
        self.descriptionEdit.setTabChangesFocus(True)
        self.descriptionEdit.setAcceptRichText(False)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridlayout.addWidget(self.descriptionEdit, 0, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(PropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.descriptionLabel.setBuddy(self.descriptionEdit)

        self.retranslateUi(PropertiesDialog)
        self.buttonBox.accepted.connect(PropertiesDialog.accept)
        self.buttonBox.rejected.connect(PropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PropertiesDialog)
        PropertiesDialog.setTabOrder(self.descriptionEdit, self.buttonBox)

    def retranslateUi(self, PropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        PropertiesDialog.setWindowTitle(_translate("PropertiesDialog", "Multiproject Properties"))
        self.descriptionLabel.setText(_translate("PropertiesDialog", "&Description:"))
        self.descriptionEdit.setToolTip(_translate("PropertiesDialog", "Enter description"))
        self.descriptionEdit.setWhatsThis(_translate("PropertiesDialog", "<b>Description</b>\n"
"<p>Enter a short description for the multiproject.</p>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PropertiesDialog = QtWidgets.QDialog()
    ui = Ui_PropertiesDialog()
    ui.setupUi(PropertiesDialog)
    PropertiesDialog.show()
    sys.exit(app.exec_())

