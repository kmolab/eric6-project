# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Debugger\EditBreakpointDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditBreakpointDialog(object):
    def setupUi(self, EditBreakpointDialog):
        EditBreakpointDialog.setObjectName("EditBreakpointDialog")
        EditBreakpointDialog.resize(428, 207)
        EditBreakpointDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(EditBreakpointDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1_2 = QtWidgets.QLabel(EditBreakpointDialog)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.gridLayout.addWidget(self.textLabel1_2, 0, 0, 1, 1)
        self.filenamePicker = E5ComboPathPicker(EditBreakpointDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenamePicker.sizePolicy().hasHeightForWidth())
        self.filenamePicker.setSizePolicy(sizePolicy)
        self.filenamePicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.filenamePicker.setObjectName("filenamePicker")
        self.gridLayout.addWidget(self.filenamePicker, 0, 1, 1, 2)
        self.textLabel2_2 = QtWidgets.QLabel(EditBreakpointDialog)
        self.textLabel2_2.setObjectName("textLabel2_2")
        self.gridLayout.addWidget(self.textLabel2_2, 1, 0, 1, 1)
        self.linenoSpinBox = QtWidgets.QSpinBox(EditBreakpointDialog)
        self.linenoSpinBox.setMinimum(1)
        self.linenoSpinBox.setMaximum(99999)
        self.linenoSpinBox.setObjectName("linenoSpinBox")
        self.gridLayout.addWidget(self.linenoSpinBox, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(EditBreakpointDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.conditionCombo = QtWidgets.QComboBox(EditBreakpointDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditionCombo.sizePolicy().hasHeightForWidth())
        self.conditionCombo.setSizePolicy(sizePolicy)
        self.conditionCombo.setEditable(True)
        self.conditionCombo.setObjectName("conditionCombo")
        self.gridLayout.addWidget(self.conditionCombo, 2, 1, 1, 2)
        self.textLabel2 = QtWidgets.QLabel(EditBreakpointDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridLayout.addWidget(self.textLabel2, 3, 0, 1, 1)
        self.ignoreSpinBox = QtWidgets.QSpinBox(EditBreakpointDialog)
        self.ignoreSpinBox.setMaximum(9999)
        self.ignoreSpinBox.setObjectName("ignoreSpinBox")
        self.gridLayout.addWidget(self.ignoreSpinBox, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.temporaryCheckBox = QtWidgets.QCheckBox(EditBreakpointDialog)
        self.temporaryCheckBox.setObjectName("temporaryCheckBox")
        self.gridLayout.addWidget(self.temporaryCheckBox, 4, 0, 1, 3)
        self.enabledCheckBox = QtWidgets.QCheckBox(EditBreakpointDialog)
        self.enabledCheckBox.setChecked(True)
        self.enabledCheckBox.setObjectName("enabledCheckBox")
        self.gridLayout.addWidget(self.enabledCheckBox, 5, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditBreakpointDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 3)

        self.retranslateUi(EditBreakpointDialog)
        self.buttonBox.accepted.connect(EditBreakpointDialog.accept)
        self.buttonBox.rejected.connect(EditBreakpointDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditBreakpointDialog)
        EditBreakpointDialog.setTabOrder(self.filenamePicker, self.linenoSpinBox)
        EditBreakpointDialog.setTabOrder(self.linenoSpinBox, self.conditionCombo)
        EditBreakpointDialog.setTabOrder(self.conditionCombo, self.ignoreSpinBox)
        EditBreakpointDialog.setTabOrder(self.ignoreSpinBox, self.temporaryCheckBox)
        EditBreakpointDialog.setTabOrder(self.temporaryCheckBox, self.enabledCheckBox)

    def retranslateUi(self, EditBreakpointDialog):
        _translate = QtCore.QCoreApplication.translate
        EditBreakpointDialog.setWindowTitle(_translate("EditBreakpointDialog", "Edit Breakpoint"))
        self.textLabel1_2.setText(_translate("EditBreakpointDialog", "Filename:"))
        self.filenamePicker.setToolTip(_translate("EditBreakpointDialog", "Enter the filename of the breakpoint"))
        self.textLabel2_2.setText(_translate("EditBreakpointDialog", "Linenumber:"))
        self.linenoSpinBox.setToolTip(_translate("EditBreakpointDialog", "Enter the linenumber of the breakpoint"))
        self.textLabel1.setText(_translate("EditBreakpointDialog", "Condition:"))
        self.conditionCombo.setToolTip(_translate("EditBreakpointDialog", "Enter or select a condition for the breakpoint"))
        self.textLabel2.setText(_translate("EditBreakpointDialog", "Ignore Count:"))
        self.ignoreSpinBox.setToolTip(_translate("EditBreakpointDialog", "Enter an ignore count for the breakpoint"))
        self.temporaryCheckBox.setToolTip(_translate("EditBreakpointDialog", "Select whether this is a temporary breakpoint"))
        self.temporaryCheckBox.setText(_translate("EditBreakpointDialog", "Temporary Breakpoint"))
        self.enabledCheckBox.setToolTip(_translate("EditBreakpointDialog", "Select, whether the breakpoint is enabled"))
        self.enabledCheckBox.setText(_translate("EditBreakpointDialog", "Enabled"))

from E5Gui.E5PathPicker import E5ComboPathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditBreakpointDialog = QtWidgets.QDialog()
    ui = Ui_EditBreakpointDialog()
    ui.setupUi(EditBreakpointDialog)
    EditBreakpointDialog.show()
    sys.exit(app.exec_())

