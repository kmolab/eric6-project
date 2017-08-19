# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\QueuesExtension\HgQueuesListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesListDialog(object):
    def setupUi(self, HgQueuesListDialog):
        HgQueuesListDialog.setObjectName("HgQueuesListDialog")
        HgQueuesListDialog.resize(634, 494)
        HgQueuesListDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(HgQueuesListDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.patchesList = QtWidgets.QTreeWidget(HgQueuesListDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.patchesList.sizePolicy().hasHeightForWidth())
        self.patchesList.setSizePolicy(sizePolicy)
        self.patchesList.setAlternatingRowColors(True)
        self.patchesList.setRootIsDecorated(False)
        self.patchesList.setItemsExpandable(False)
        self.patchesList.setObjectName("patchesList")
        self.patchesList.headerItem().setText(0, "#")
        self.patchesList.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.vboxlayout.addWidget(self.patchesList)
        self.errorGroup = QtWidgets.QGroupBox(HgQueuesListDialog)
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
        self.inputGroup = QtWidgets.QGroupBox(HgQueuesListDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(HgQueuesListDialog)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesListDialog)
        HgQueuesListDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgQueuesListDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        HgQueuesListDialog.setTabOrder(self.sendButton, self.patchesList)
        HgQueuesListDialog.setTabOrder(self.patchesList, self.errors)
        HgQueuesListDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, HgQueuesListDialog):
        _translate = QtCore.QCoreApplication.translate
        HgQueuesListDialog.setWindowTitle(_translate("HgQueuesListDialog", "List of Patches"))
        HgQueuesListDialog.setWhatsThis(_translate("HgQueuesListDialog", "<b>List of Patches</b>\n"
"<p>This dialog shows a list of applied and unapplied patches.</p>"))
        self.patchesList.setWhatsThis(_translate("HgQueuesListDialog", "<b>Patches List</b>\n"
"<p>This shows a list of applied and unapplied patches.</p>"))
        self.patchesList.headerItem().setText(1, _translate("HgQueuesListDialog", "Name"))
        self.patchesList.headerItem().setText(2, _translate("HgQueuesListDialog", "Status"))
        self.patchesList.headerItem().setText(3, _translate("HgQueuesListDialog", "Summary"))
        self.errorGroup.setTitle(_translate("HgQueuesListDialog", "Errors"))
        self.inputGroup.setTitle(_translate("HgQueuesListDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgQueuesListDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgQueuesListDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgQueuesListDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgQueuesListDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgQueuesListDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgQueuesListDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgQueuesListDialog", "Alt+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgQueuesListDialog = QtWidgets.QDialog()
    ui = Ui_HgQueuesListDialog()
    ui.setupUi(HgQueuesListDialog)
    HgQueuesListDialog.show()
    sys.exit(app.exec_())

