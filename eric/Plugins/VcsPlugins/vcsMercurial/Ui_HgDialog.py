# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgDialog(object):
    def setupUi(self, HgDialog):
        HgDialog.setObjectName("HgDialog")
        HgDialog.resize(593, 499)
        HgDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(HgDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.outputGroup = QtWidgets.QGroupBox(HgDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.outputGroup.sizePolicy().hasHeightForWidth())
        self.outputGroup.setSizePolicy(sizePolicy)
        self.outputGroup.setObjectName("outputGroup")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.outputGroup)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.resultbox = QtWidgets.QTextEdit(self.outputGroup)
        self.resultbox.setReadOnly(True)
        self.resultbox.setAcceptRichText(False)
        self.resultbox.setObjectName("resultbox")
        self.vboxlayout1.addWidget(self.resultbox)
        self.vboxlayout.addWidget(self.outputGroup)
        self.errorGroup = QtWidgets.QGroupBox(HgDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout2.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.inputGroup = QtWidgets.QGroupBox(HgDialog)
        self.inputGroup.setObjectName("inputGroup")
        self.gridlayout = QtWidgets.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.vboxlayout.addWidget(self.inputGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(HgDialog)
        QtCore.QMetaObject.connectSlotsByName(HgDialog)
        HgDialog.setTabOrder(self.resultbox, self.errors)
        HgDialog.setTabOrder(self.errors, self.input)
        HgDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        HgDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, HgDialog):
        _translate = QtCore.QCoreApplication.translate
        HgDialog.setWindowTitle(_translate("HgDialog", "Mercurial"))
        self.outputGroup.setTitle(_translate("HgDialog", "Output"))
        self.errorGroup.setTitle(_translate("HgDialog", "Errors"))
        self.inputGroup.setTitle(_translate("HgDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgDialog", "Alt+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgDialog = QtWidgets.QDialog()
    ui = Ui_HgDialog()
    ui.setupUi(HgDialog)
    HgDialog.show()
    sys.exit(app.exec_())

