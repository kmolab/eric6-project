# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\AddFileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddFileDialog(object):
    def setupUi(self, AddFileDialog):
        AddFileDialog.setObjectName("AddFileDialog")
        AddFileDialog.resize(391, 114)
        AddFileDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddFileDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sourceFileLabel = QtWidgets.QLabel(AddFileDialog)
        self.sourceFileLabel.setObjectName("sourceFileLabel")
        self.gridLayout.addWidget(self.sourceFileLabel, 0, 0, 1, 1)
        self.sourceFilesPicker = E5PathPicker(AddFileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceFilesPicker.sizePolicy().hasHeightForWidth())
        self.sourceFilesPicker.setSizePolicy(sizePolicy)
        self.sourceFilesPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sourceFilesPicker.setObjectName("sourceFilesPicker")
        self.gridLayout.addWidget(self.sourceFilesPicker, 0, 1, 1, 1)
        self.targetDirLabel = QtWidgets.QLabel(AddFileDialog)
        self.targetDirLabel.setObjectName("targetDirLabel")
        self.gridLayout.addWidget(self.targetDirLabel, 1, 0, 1, 1)
        self.targetDirPicker = E5PathPicker(AddFileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetDirPicker.sizePolicy().hasHeightForWidth())
        self.targetDirPicker.setSizePolicy(sizePolicy)
        self.targetDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.targetDirPicker.setObjectName("targetDirPicker")
        self.gridLayout.addWidget(self.targetDirPicker, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.sourcecodeCheckBox = QtWidgets.QCheckBox(AddFileDialog)
        self.sourcecodeCheckBox.setObjectName("sourcecodeCheckBox")
        self.verticalLayout.addWidget(self.sourcecodeCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.sourceFileLabel.setBuddy(self.sourceFilesPicker)
        self.targetDirLabel.setBuddy(self.targetDirPicker)

        self.retranslateUi(AddFileDialog)
        self.buttonBox.accepted.connect(AddFileDialog.accept)
        self.buttonBox.rejected.connect(AddFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddFileDialog)
        AddFileDialog.setTabOrder(self.sourceFilesPicker, self.targetDirPicker)
        AddFileDialog.setTabOrder(self.targetDirPicker, self.sourcecodeCheckBox)

    def retranslateUi(self, AddFileDialog):
        _translate = QtCore.QCoreApplication.translate
        AddFileDialog.setWindowTitle(_translate("AddFileDialog", "Add Files"))
        AddFileDialog.setWhatsThis(_translate("AddFileDialog", "<b>Add Files Dialog</b>\n"
"<p>This dialog is used to add files to the current project.</p>"))
        self.sourceFileLabel.setText(_translate("AddFileDialog", "&Source Files:"))
        self.sourceFilesPicker.setToolTip(_translate("AddFileDialog", "Enter the name of files to add separated by \";\""))
        self.sourceFilesPicker.setWhatsThis(_translate("AddFileDialog", "<b>Source Files</b>\n"
"<p>Enter the name of files to add to the current project separated\n"
"by \";\". You may select them with a dialog by pressing \n"
"the button to the right.</p>"))
        self.targetDirLabel.setText(_translate("AddFileDialog", "&Target Directory:"))
        self.targetDirPicker.setToolTip(_translate("AddFileDialog", "Enter the target directory for the file"))
        self.targetDirPicker.setWhatsThis(_translate("AddFileDialog", "<b>Target Directory</b>\n"
"<p>Enter the target directory. You may select it\n"
" with a dialog by pressing the button to the right.</p>"))
        self.sourcecodeCheckBox.setToolTip(_translate("AddFileDialog", "Select, if the files should be added as sourcecode (overriding automatic detection)"))
        self.sourcecodeCheckBox.setText(_translate("AddFileDialog", "Is source&code files"))
        self.sourcecodeCheckBox.setShortcut(_translate("AddFileDialog", "Alt+C"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddFileDialog = QtWidgets.QDialog()
    ui = Ui_AddFileDialog()
    ui.setupUi(AddFileDialog)
    AddFileDialog.show()
    sys.exit(app.exec_())

