# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgAnnotateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgAnnotateDialog(object):
    def setupUi(self, HgAnnotateDialog):
        HgAnnotateDialog.setObjectName("HgAnnotateDialog")
        HgAnnotateDialog.resize(690, 750)
        HgAnnotateDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(HgAnnotateDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.annotateList = QtWidgets.QTreeWidget(HgAnnotateDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.annotateList.sizePolicy().hasHeightForWidth())
        self.annotateList.setSizePolicy(sizePolicy)
        self.annotateList.setAlternatingRowColors(True)
        self.annotateList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.annotateList.setRootIsDecorated(False)
        self.annotateList.setItemsExpandable(False)
        self.annotateList.setObjectName("annotateList")
        self.annotateList.header().setStretchLastSection(False)
        self.vboxlayout.addWidget(self.annotateList)
        self.errorGroup = QtWidgets.QGroupBox(HgAnnotateDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout1.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.inputGroup = QtWidgets.QGroupBox(HgAnnotateDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(HgAnnotateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(HgAnnotateDialog)
        QtCore.QMetaObject.connectSlotsByName(HgAnnotateDialog)
        HgAnnotateDialog.setTabOrder(self.annotateList, self.errors)
        HgAnnotateDialog.setTabOrder(self.errors, self.input)
        HgAnnotateDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgAnnotateDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        HgAnnotateDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, HgAnnotateDialog):
        _translate = QtCore.QCoreApplication.translate
        HgAnnotateDialog.setWindowTitle(_translate("HgAnnotateDialog", "Mercurial Annotate"))
        self.annotateList.headerItem().setText(0, _translate("HgAnnotateDialog", "Revision"))
        self.annotateList.headerItem().setText(1, _translate("HgAnnotateDialog", "Changeset"))
        self.annotateList.headerItem().setText(2, _translate("HgAnnotateDialog", "Author"))
        self.annotateList.headerItem().setText(3, _translate("HgAnnotateDialog", "Date"))
        self.annotateList.headerItem().setText(4, _translate("HgAnnotateDialog", "Line"))
        self.errorGroup.setTitle(_translate("HgAnnotateDialog", "Errors"))
        self.inputGroup.setTitle(_translate("HgAnnotateDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgAnnotateDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgAnnotateDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgAnnotateDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgAnnotateDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgAnnotateDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgAnnotateDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgAnnotateDialog", "Alt+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgAnnotateDialog = QtWidgets.QDialog()
    ui = Ui_HgAnnotateDialog()
    ui.setupUi(HgAnnotateDialog)
    HgAnnotateDialog.show()
    sys.exit(app.exec_())

