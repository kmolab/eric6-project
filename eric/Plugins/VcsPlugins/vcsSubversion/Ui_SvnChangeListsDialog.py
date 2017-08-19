# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnChangeListsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnChangeListsDialog(object):
    def setupUi(self, SvnChangeListsDialog):
        SvnChangeListsDialog.setObjectName("SvnChangeListsDialog")
        SvnChangeListsDialog.resize(519, 494)
        SvnChangeListsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SvnChangeListsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SvnChangeListsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.changeLists = QtWidgets.QListWidget(SvnChangeListsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.changeLists.sizePolicy().hasHeightForWidth())
        self.changeLists.setSizePolicy(sizePolicy)
        self.changeLists.setAlternatingRowColors(True)
        self.changeLists.setObjectName("changeLists")
        self.verticalLayout.addWidget(self.changeLists)
        self.filesLabel = QtWidgets.QLabel(SvnChangeListsDialog)
        self.filesLabel.setText("")
        self.filesLabel.setWordWrap(True)
        self.filesLabel.setObjectName("filesLabel")
        self.verticalLayout.addWidget(self.filesLabel)
        self.filesList = QtWidgets.QListWidget(SvnChangeListsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.filesList.sizePolicy().hasHeightForWidth())
        self.filesList.setSizePolicy(sizePolicy)
        self.filesList.setAlternatingRowColors(True)
        self.filesList.setObjectName("filesList")
        self.verticalLayout.addWidget(self.filesList)
        self.errorGroup = QtWidgets.QGroupBox(SvnChangeListsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout.addWidget(self.errors)
        self.verticalLayout.addWidget(self.errorGroup)
        self.inputGroup = QtWidgets.QGroupBox(SvnChangeListsDialog)
        self.inputGroup.setObjectName("inputGroup")
        self._2 = QtWidgets.QGridLayout(self.inputGroup)
        self._2.setObjectName("_2")
        spacerItem = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._2.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self._2.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self._2.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self._2.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.inputGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnChangeListsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnChangeListsDialog)
        self.buttonBox.accepted.connect(SvnChangeListsDialog.accept)
        self.buttonBox.rejected.connect(SvnChangeListsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnChangeListsDialog)
        SvnChangeListsDialog.setTabOrder(self.changeLists, self.filesList)
        SvnChangeListsDialog.setTabOrder(self.filesList, self.errors)
        SvnChangeListsDialog.setTabOrder(self.errors, self.input)
        SvnChangeListsDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnChangeListsDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        SvnChangeListsDialog.setTabOrder(self.sendButton, self.buttonBox)

    def retranslateUi(self, SvnChangeListsDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnChangeListsDialog.setWindowTitle(_translate("SvnChangeListsDialog", "Subversion Change Lists"))
        self.label.setText(_translate("SvnChangeListsDialog", "Change Lists:"))
        self.changeLists.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Change Lists</b>\n"
"<p>Select a change list here to see the associated files in the list below.</p>"))
        self.filesList.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Files</b>\n"
"<p>This shows a list of files associated with the change list selected above.</p>"))
        self.errorGroup.setTitle(_translate("SvnChangeListsDialog", "Errors"))
        self.inputGroup.setTitle(_translate("SvnChangeListsDialog", "Input"))
        self.sendButton.setToolTip(_translate("SvnChangeListsDialog", "Press to send the input to the subversion process"))
        self.sendButton.setText(_translate("SvnChangeListsDialog", "&Send"))
        self.sendButton.setShortcut(_translate("SvnChangeListsDialog", "Alt+S"))
        self.input.setToolTip(_translate("SvnChangeListsDialog", "Enter data to be sent to the subversion process"))
        self.passwordCheckBox.setToolTip(_translate("SvnChangeListsDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("SvnChangeListsDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("SvnChangeListsDialog", "Alt+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnChangeListsDialog = QtWidgets.QDialog()
    ui = Ui_SvnChangeListsDialog()
    ui.setupUi(SvnChangeListsDialog)
    SvnChangeListsDialog.show()
    sys.exit(app.exec_())

