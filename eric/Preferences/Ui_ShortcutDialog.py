# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ShortcutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShortcutDialog(object):
    def setupUi(self, ShortcutDialog):
        ShortcutDialog.setObjectName("ShortcutDialog")
        ShortcutDialog.resize(539, 134)
        self.vboxlayout = QtWidgets.QVBoxLayout(ShortcutDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.shortcutsGroup = QtWidgets.QGroupBox(ShortcutDialog)
        self.shortcutsGroup.setTitle("")
        self.shortcutsGroup.setObjectName("shortcutsGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.shortcutsGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.primaryButton = QtWidgets.QRadioButton(self.shortcutsGroup)
        self.primaryButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.primaryButton.setChecked(True)
        self.primaryButton.setObjectName("primaryButton")
        self.gridLayout.addWidget(self.primaryButton, 0, 0, 1, 1)
        self.primaryClearButton = QtWidgets.QPushButton(self.shortcutsGroup)
        self.primaryClearButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.primaryClearButton.setObjectName("primaryClearButton")
        self.gridLayout.addWidget(self.primaryClearButton, 0, 1, 1, 1)
        self.keyEdit = QtWidgets.QLineEdit(self.shortcutsGroup)
        self.keyEdit.setReadOnly(True)
        self.keyEdit.setObjectName("keyEdit")
        self.gridLayout.addWidget(self.keyEdit, 0, 2, 1, 1)
        self.alternateButton = QtWidgets.QRadioButton(self.shortcutsGroup)
        self.alternateButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alternateButton.setObjectName("alternateButton")
        self.gridLayout.addWidget(self.alternateButton, 1, 0, 1, 1)
        self.alternateClearButton = QtWidgets.QPushButton(self.shortcutsGroup)
        self.alternateClearButton.setEnabled(False)
        self.alternateClearButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alternateClearButton.setObjectName("alternateClearButton")
        self.gridLayout.addWidget(self.alternateClearButton, 1, 1, 1, 1)
        self.alternateKeyEdit = QtWidgets.QLineEdit(self.shortcutsGroup)
        self.alternateKeyEdit.setReadOnly(True)
        self.alternateKeyEdit.setObjectName("alternateKeyEdit")
        self.gridLayout.addWidget(self.alternateKeyEdit, 1, 2, 1, 1)
        self.vboxlayout.addWidget(self.shortcutsGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(ShortcutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ShortcutDialog)
        self.primaryButton.toggled['bool'].connect(self.primaryClearButton.setEnabled)
        self.alternateButton.toggled['bool'].connect(self.alternateClearButton.setEnabled)
        self.buttonBox.rejected.connect(ShortcutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShortcutDialog)
        ShortcutDialog.setTabOrder(self.keyEdit, self.alternateKeyEdit)
        ShortcutDialog.setTabOrder(self.alternateKeyEdit, self.buttonBox)

    def retranslateUi(self, ShortcutDialog):
        _translate = QtCore.QCoreApplication.translate
        ShortcutDialog.setWindowTitle(_translate("ShortcutDialog", "Edit Shortcut"))
        ShortcutDialog.setWhatsThis(_translate("ShortcutDialog", "Press your shortcut keys and select OK"))
        self.primaryButton.setToolTip(_translate("ShortcutDialog", "Select to change the primary keyboard shortcut"))
        self.primaryButton.setText(_translate("ShortcutDialog", "Primary Shortcut:"))
        self.primaryClearButton.setToolTip(_translate("ShortcutDialog", "Press to clear the key sequence buffer."))
        self.primaryClearButton.setText(_translate("ShortcutDialog", "Clear"))
        self.alternateButton.setToolTip(_translate("ShortcutDialog", "Select to change the alternative keyboard shortcut"))
        self.alternateButton.setText(_translate("ShortcutDialog", "Alternative Shortcut:"))
        self.alternateClearButton.setToolTip(_translate("ShortcutDialog", "Press to clear the key sequence buffer."))
        self.alternateClearButton.setText(_translate("ShortcutDialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShortcutDialog = QtWidgets.QDialog()
    ui = Ui_ShortcutDialog()
    ui.setupUi(ShortcutDialog)
    ShortcutDialog.show()
    sys.exit(app.exec_())

