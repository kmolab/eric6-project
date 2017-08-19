# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Debugger\EditWatchpointDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditWatchpointDialog(object):
    def setupUi(self, EditWatchpointDialog):
        EditWatchpointDialog.setObjectName("EditWatchpointDialog")
        EditWatchpointDialog.resize(402, 234)
        EditWatchpointDialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(EditWatchpointDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(EditWatchpointDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 4, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(211, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 2, 1, 1)
        self.ignoreSpinBox = QtWidgets.QSpinBox(EditWatchpointDialog)
        self.ignoreSpinBox.setMaximum(9999)
        self.ignoreSpinBox.setObjectName("ignoreSpinBox")
        self.gridlayout.addWidget(self.ignoreSpinBox, 1, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(EditWatchpointDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.enabledCheckBox = QtWidgets.QCheckBox(EditWatchpointDialog)
        self.enabledCheckBox.setObjectName("enabledCheckBox")
        self.gridlayout.addWidget(self.enabledCheckBox, 3, 0, 1, 3)
        self.temporaryCheckBox = QtWidgets.QCheckBox(EditWatchpointDialog)
        self.temporaryCheckBox.setObjectName("temporaryCheckBox")
        self.gridlayout.addWidget(self.temporaryCheckBox, 2, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(EditWatchpointDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridlayout1 = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout1.setObjectName("gridlayout1")
        self.specialButton = QtWidgets.QRadioButton(self.groupBox)
        self.specialButton.setObjectName("specialButton")
        self.gridlayout1.addWidget(self.specialButton, 1, 0, 1, 1)
        self.conditionButton = QtWidgets.QRadioButton(self.groupBox)
        self.conditionButton.setChecked(True)
        self.conditionButton.setObjectName("conditionButton")
        self.gridlayout1.addWidget(self.conditionButton, 0, 0, 1, 1)
        self.specialEdit = QtWidgets.QLineEdit(self.groupBox)
        self.specialEdit.setEnabled(False)
        self.specialEdit.setObjectName("specialEdit")
        self.gridlayout1.addWidget(self.specialEdit, 1, 1, 1, 1)
        self.specialCombo = QtWidgets.QComboBox(self.groupBox)
        self.specialCombo.setEnabled(False)
        self.specialCombo.setObjectName("specialCombo")
        self.specialCombo.addItem("")
        self.specialCombo.addItem("")
        self.gridlayout1.addWidget(self.specialCombo, 2, 1, 1, 1)
        self.conditionEdit = QtWidgets.QLineEdit(self.groupBox)
        self.conditionEdit.setObjectName("conditionEdit")
        self.gridlayout1.addWidget(self.conditionEdit, 0, 1, 1, 1)
        self.gridlayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.retranslateUi(EditWatchpointDialog)
        self.conditionButton.toggled['bool'].connect(self.conditionEdit.setEnabled)
        self.specialButton.toggled['bool'].connect(self.specialCombo.setEnabled)
        self.specialButton.toggled['bool'].connect(self.specialEdit.setEnabled)
        self.buttonBox.accepted.connect(EditWatchpointDialog.accept)
        self.buttonBox.rejected.connect(EditWatchpointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditWatchpointDialog)
        EditWatchpointDialog.setTabOrder(self.conditionButton, self.conditionEdit)
        EditWatchpointDialog.setTabOrder(self.conditionEdit, self.specialButton)
        EditWatchpointDialog.setTabOrder(self.specialButton, self.specialEdit)
        EditWatchpointDialog.setTabOrder(self.specialEdit, self.specialCombo)
        EditWatchpointDialog.setTabOrder(self.specialCombo, self.ignoreSpinBox)
        EditWatchpointDialog.setTabOrder(self.ignoreSpinBox, self.temporaryCheckBox)
        EditWatchpointDialog.setTabOrder(self.temporaryCheckBox, self.enabledCheckBox)

    def retranslateUi(self, EditWatchpointDialog):
        _translate = QtCore.QCoreApplication.translate
        EditWatchpointDialog.setWindowTitle(_translate("EditWatchpointDialog", "Edit Watch Expression"))
        self.ignoreSpinBox.setToolTip(_translate("EditWatchpointDialog", "Enter an ignore count for the watch expression"))
        self.textLabel2.setText(_translate("EditWatchpointDialog", "Ignore Count:"))
        self.enabledCheckBox.setToolTip(_translate("EditWatchpointDialog", "Select, whether the watch expression is enabled"))
        self.enabledCheckBox.setText(_translate("EditWatchpointDialog", "Enabled"))
        self.temporaryCheckBox.setToolTip(_translate("EditWatchpointDialog", "Select whether this is a temporary watch expression"))
        self.temporaryCheckBox.setText(_translate("EditWatchpointDialog", "Temporary Watch Expression"))
        self.specialButton.setText(_translate("EditWatchpointDialog", "Variable:"))
        self.conditionButton.setText(_translate("EditWatchpointDialog", "Expression:"))
        self.specialEdit.setToolTip(_translate("EditWatchpointDialog", "Enter a variable and select the special condition below"))
        self.specialCombo.setToolTip(_translate("EditWatchpointDialog", "Select a special condition"))
        self.specialCombo.setItemText(0, _translate("EditWatchpointDialog", "created"))
        self.specialCombo.setItemText(1, _translate("EditWatchpointDialog", "changed"))
        self.conditionEdit.setToolTip(_translate("EditWatchpointDialog", "Enter the expression for the watch expression"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditWatchpointDialog = QtWidgets.QDialog()
    ui = Ui_EditWatchpointDialog()
    ui.setupUi(EditWatchpointDialog)
    EditWatchpointDialog.show()
    sys.exit(app.exec_())

