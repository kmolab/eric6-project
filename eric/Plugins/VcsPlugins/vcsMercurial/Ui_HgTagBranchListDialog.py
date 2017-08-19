# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgTagBranchListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgTagBranchListDialog(object):
    def setupUi(self, HgTagBranchListDialog):
        HgTagBranchListDialog.setObjectName("HgTagBranchListDialog")
        HgTagBranchListDialog.resize(634, 494)
        HgTagBranchListDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(HgTagBranchListDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.tagList = QtWidgets.QTreeWidget(HgTagBranchListDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tagList.sizePolicy().hasHeightForWidth())
        self.tagList.setSizePolicy(sizePolicy)
        self.tagList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tagList.setAlternatingRowColors(True)
        self.tagList.setRootIsDecorated(False)
        self.tagList.setItemsExpandable(False)
        self.tagList.setObjectName("tagList")
        self.vboxlayout.addWidget(self.tagList)
        self.errorGroup = QtWidgets.QGroupBox(HgTagBranchListDialog)
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
        self.inputGroup = QtWidgets.QGroupBox(HgTagBranchListDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(HgTagBranchListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(HgTagBranchListDialog)
        QtCore.QMetaObject.connectSlotsByName(HgTagBranchListDialog)
        HgTagBranchListDialog.setTabOrder(self.tagList, self.errors)
        HgTagBranchListDialog.setTabOrder(self.errors, self.input)
        HgTagBranchListDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgTagBranchListDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        HgTagBranchListDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, HgTagBranchListDialog):
        _translate = QtCore.QCoreApplication.translate
        HgTagBranchListDialog.setWindowTitle(_translate("HgTagBranchListDialog", "Mercurial Tag List"))
        HgTagBranchListDialog.setWhatsThis(_translate("HgTagBranchListDialog", "<b>Mercurial Tag/Branch List</b>\n"
"<p>This dialog shows a list of the projects tags or branches.</p>"))
        self.tagList.setWhatsThis(_translate("HgTagBranchListDialog", "<b>Tag/Branches List</b>\n"
"<p>This shows a list of the projects tags or branches.</p>"))
        self.tagList.setSortingEnabled(True)
        self.tagList.headerItem().setText(0, _translate("HgTagBranchListDialog", "Revision"))
        self.tagList.headerItem().setText(1, _translate("HgTagBranchListDialog", "Changeset"))
        self.tagList.headerItem().setText(2, _translate("HgTagBranchListDialog", "Local"))
        self.tagList.headerItem().setText(3, _translate("HgTagBranchListDialog", "Name"))
        self.errorGroup.setTitle(_translate("HgTagBranchListDialog", "Errors"))
        self.inputGroup.setTitle(_translate("HgTagBranchListDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgTagBranchListDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgTagBranchListDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgTagBranchListDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgTagBranchListDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgTagBranchListDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgTagBranchListDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgTagBranchListDialog", "Alt+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgTagBranchListDialog = QtWidgets.QDialog()
    ui = Ui_HgTagBranchListDialog()
    ui.setupUi(HgTagBranchListDialog)
    HgTagBranchListDialog.show()
    sys.exit(app.exec_())

