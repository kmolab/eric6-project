# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ToolGroupConfigurationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ToolGroupConfigurationDialog(object):
    def setupUi(self, ToolGroupConfigurationDialog):
        ToolGroupConfigurationDialog.setObjectName("ToolGroupConfigurationDialog")
        ToolGroupConfigurationDialog.resize(475, 391)
        ToolGroupConfigurationDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(ToolGroupConfigurationDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.deleteButton = QtWidgets.QPushButton(ToolGroupConfigurationDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.gridlayout.addWidget(self.deleteButton, 3, 2, 1, 1)
        self.addButton = QtWidgets.QPushButton(ToolGroupConfigurationDialog)
        self.addButton.setObjectName("addButton")
        self.gridlayout.addWidget(self.addButton, 1, 2, 1, 1)
        self.TextLabel2 = QtWidgets.QLabel(ToolGroupConfigurationDialog)
        self.TextLabel2.setObjectName("TextLabel2")
        self.gridlayout.addWidget(self.TextLabel2, 7, 0, 1, 1)
        self.changeButton = QtWidgets.QPushButton(ToolGroupConfigurationDialog)
        self.changeButton.setEnabled(False)
        self.changeButton.setObjectName("changeButton")
        self.gridlayout.addWidget(self.changeButton, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(87, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 6, 2, 1, 1)
        self.newButton = QtWidgets.QPushButton(ToolGroupConfigurationDialog)
        self.newButton.setObjectName("newButton")
        self.gridlayout.addWidget(self.newButton, 0, 2, 1, 1)
        self.upButton = QtWidgets.QPushButton(ToolGroupConfigurationDialog)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName("upButton")
        self.gridlayout.addWidget(self.upButton, 4, 2, 1, 1)
        self.downButton = QtWidgets.QPushButton(ToolGroupConfigurationDialog)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName("downButton")
        self.gridlayout.addWidget(self.downButton, 5, 2, 1, 1)
        self.groupsList = QtWidgets.QListWidget(ToolGroupConfigurationDialog)
        self.groupsList.setObjectName("groupsList")
        self.gridlayout.addWidget(self.groupsList, 0, 0, 7, 2)
        self.nameEdit = QtWidgets.QLineEdit(ToolGroupConfigurationDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridlayout.addWidget(self.nameEdit, 7, 1, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ToolGroupConfigurationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.TextLabel2.setBuddy(self.nameEdit)

        self.retranslateUi(ToolGroupConfigurationDialog)
        self.buttonBox.accepted.connect(ToolGroupConfigurationDialog.accept)
        self.buttonBox.rejected.connect(ToolGroupConfigurationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ToolGroupConfigurationDialog)
        ToolGroupConfigurationDialog.setTabOrder(self.groupsList, self.nameEdit)
        ToolGroupConfigurationDialog.setTabOrder(self.nameEdit, self.newButton)
        ToolGroupConfigurationDialog.setTabOrder(self.newButton, self.addButton)
        ToolGroupConfigurationDialog.setTabOrder(self.addButton, self.changeButton)
        ToolGroupConfigurationDialog.setTabOrder(self.changeButton, self.deleteButton)
        ToolGroupConfigurationDialog.setTabOrder(self.deleteButton, self.upButton)
        ToolGroupConfigurationDialog.setTabOrder(self.upButton, self.downButton)

    def retranslateUi(self, ToolGroupConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        ToolGroupConfigurationDialog.setWindowTitle(_translate("ToolGroupConfigurationDialog", "Configure Tool Groups"))
        self.deleteButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Delete the selected entry"))
        self.deleteButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Delete</b>\n"
"<p>Delete the selected entry.</p>"))
        self.deleteButton.setText(_translate("ToolGroupConfigurationDialog", "&Delete"))
        self.deleteButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+D"))
        self.addButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Add a new tools entry"))
        self.addButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Add</b>\n"
"<p>Add a new tool groups entry with the name entered below.</p>"))
        self.addButton.setText(_translate("ToolGroupConfigurationDialog", "&Add"))
        self.addButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+A"))
        self.TextLabel2.setText(_translate("ToolGroupConfigurationDialog", "&Group name:"))
        self.changeButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Change the values of the selected entry"))
        self.changeButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Change</b>\n"
"<p>Change the values of the selected entry.</p>"))
        self.changeButton.setText(_translate("ToolGroupConfigurationDialog", "C&hange"))
        self.changeButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+H"))
        self.newButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Clear all entry fields"))
        self.newButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>New</b>\n"
"<p>Clear all entry fields for entering a new tool groups entry.</p>"))
        self.newButton.setText(_translate("ToolGroupConfigurationDialog", "&New"))
        self.newButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+N"))
        self.upButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Move up"))
        self.upButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Move Up</b>\n"
"<p>Move the selected entry up.</p>"))
        self.upButton.setText(_translate("ToolGroupConfigurationDialog", "&Up"))
        self.upButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+U"))
        self.downButton.setToolTip(_translate("ToolGroupConfigurationDialog", "Move down"))
        self.downButton.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Move Down</b>\n"
"<p>Move the selected entry down.</p>"))
        self.downButton.setText(_translate("ToolGroupConfigurationDialog", "Do&wn"))
        self.downButton.setShortcut(_translate("ToolGroupConfigurationDialog", "Alt+W"))
        self.nameEdit.setToolTip(_translate("ToolGroupConfigurationDialog", "Enter the menu text"))
        self.nameEdit.setWhatsThis(_translate("ToolGroupConfigurationDialog", "<b>Menu text</b>\n"
"<p>Enter the menu text. Precede the accelerator key with an & character.</p>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToolGroupConfigurationDialog = QtWidgets.QDialog()
    ui = Ui_ToolGroupConfigurationDialog()
    ui.setupUi(ToolGroupConfigurationDialog)
    ToolGroupConfigurationDialog.show()
    sys.exit(app.exec_())

