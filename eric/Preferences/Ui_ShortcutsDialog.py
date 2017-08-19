# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ShortcutsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShortcutsDialog(object):
    def setupUi(self, ShortcutsDialog):
        ShortcutsDialog.setObjectName("ShortcutsDialog")
        ShortcutsDialog.resize(800, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShortcutsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(ShortcutsDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.searchEdit = E5ClearableLineEdit(ShortcutsDialog)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(ShortcutsDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.actionButton = QtWidgets.QRadioButton(ShortcutsDialog)
        self.actionButton.setChecked(True)
        self.actionButton.setObjectName("actionButton")
        self.horizontalLayout_2.addWidget(self.actionButton)
        self.shortcutButton = QtWidgets.QRadioButton(ShortcutsDialog)
        self.shortcutButton.setObjectName("shortcutButton")
        self.horizontalLayout_2.addWidget(self.shortcutButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.shortcutsList = QtWidgets.QTreeWidget(ShortcutsDialog)
        self.shortcutsList.setAlternatingRowColors(True)
        self.shortcutsList.setObjectName("shortcutsList")
        self.verticalLayout.addWidget(self.shortcutsList)
        self.buttonBox = QtWidgets.QDialogButtonBox(ShortcutsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.searchEdit)

        self.retranslateUi(ShortcutsDialog)
        self.buttonBox.rejected.connect(ShortcutsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShortcutsDialog)
        ShortcutsDialog.setTabOrder(self.searchEdit, self.actionButton)
        ShortcutsDialog.setTabOrder(self.actionButton, self.shortcutButton)
        ShortcutsDialog.setTabOrder(self.shortcutButton, self.shortcutsList)
        ShortcutsDialog.setTabOrder(self.shortcutsList, self.buttonBox)

    def retranslateUi(self, ShortcutsDialog):
        _translate = QtCore.QCoreApplication.translate
        ShortcutsDialog.setWindowTitle(_translate("ShortcutsDialog", "Keyboard Shortcuts"))
        self.label.setText(_translate("ShortcutsDialog", "&Filter:"))
        self.searchEdit.setToolTip(_translate("ShortcutsDialog", "Enter the regular expression that should be contained in the shortcut action"))
        self.label_2.setText(_translate("ShortcutsDialog", "Filter on"))
        self.actionButton.setToolTip(_translate("ShortcutsDialog", "Select to filter based on the actions"))
        self.actionButton.setText(_translate("ShortcutsDialog", "&Action"))
        self.shortcutButton.setToolTip(_translate("ShortcutsDialog", "Select to filter based on shortcut or alternative shortcut"))
        self.shortcutButton.setText(_translate("ShortcutsDialog", "&Shortcut or Alternative"))
        self.shortcutsList.setToolTip(_translate("ShortcutsDialog", "This list shows all keyboard shortcuts."))
        self.shortcutsList.setWhatsThis(_translate("ShortcutsDialog", "<b>Keyboard Shortcuts List</b>\n"
"<p>This list shows all keyboard shortcuts defined in the application. Double click an entry in order to change the respective shortcut. Alternatively, the shortcut might be changed by editing the key sequence in the respective column.</p>"))
        self.shortcutsList.headerItem().setText(0, _translate("ShortcutsDialog", "Action"))
        self.shortcutsList.headerItem().setText(1, _translate("ShortcutsDialog", "Shortcut"))
        self.shortcutsList.headerItem().setText(2, _translate("ShortcutsDialog", "Alternativ"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShortcutsDialog = QtWidgets.QDialog()
    ui = Ui_ShortcutsDialog()
    ui.setupUi(ShortcutsDialog)
    ShortcutsDialog.show()
    sys.exit(app.exec_())

