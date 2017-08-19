# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\AddDirectoryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddDirectoryDialog(object):
    def setupUi(self, AddDirectoryDialog):
        AddDirectoryDialog.setObjectName("AddDirectoryDialog")
        AddDirectoryDialog.resize(391, 141)
        AddDirectoryDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(AddDirectoryDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(AddDirectoryDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.filterComboBox = QtWidgets.QComboBox(AddDirectoryDialog)
        self.filterComboBox.setObjectName("filterComboBox")
        self.gridLayout.addWidget(self.filterComboBox, 0, 1, 1, 1)
        self.sourceDirLabel = QtWidgets.QLabel(AddDirectoryDialog)
        self.sourceDirLabel.setObjectName("sourceDirLabel")
        self.gridLayout.addWidget(self.sourceDirLabel, 1, 0, 1, 1)
        self.sourceDirPicker = E5PathPicker(AddDirectoryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceDirPicker.sizePolicy().hasHeightForWidth())
        self.sourceDirPicker.setSizePolicy(sizePolicy)
        self.sourceDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sourceDirPicker.setObjectName("sourceDirPicker")
        self.gridLayout.addWidget(self.sourceDirPicker, 1, 1, 1, 1)
        self.targetDirLabel = QtWidgets.QLabel(AddDirectoryDialog)
        self.targetDirLabel.setObjectName("targetDirLabel")
        self.gridLayout.addWidget(self.targetDirLabel, 2, 0, 1, 1)
        self.targetDirPicker = E5PathPicker(AddDirectoryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetDirPicker.sizePolicy().hasHeightForWidth())
        self.targetDirPicker.setSizePolicy(sizePolicy)
        self.targetDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.targetDirPicker.setObjectName("targetDirPicker")
        self.gridLayout.addWidget(self.targetDirPicker, 2, 1, 1, 1)
        self.recursiveCheckBox = QtWidgets.QCheckBox(AddDirectoryDialog)
        self.recursiveCheckBox.setObjectName("recursiveCheckBox")
        self.gridLayout.addWidget(self.recursiveCheckBox, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddDirectoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.textLabel1.setBuddy(self.filterComboBox)
        self.sourceDirLabel.setBuddy(self.sourceDirPicker)
        self.targetDirLabel.setBuddy(self.targetDirPicker)

        self.retranslateUi(AddDirectoryDialog)
        self.buttonBox.accepted.connect(AddDirectoryDialog.accept)
        self.buttonBox.rejected.connect(AddDirectoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddDirectoryDialog)
        AddDirectoryDialog.setTabOrder(self.filterComboBox, self.sourceDirPicker)
        AddDirectoryDialog.setTabOrder(self.sourceDirPicker, self.targetDirPicker)
        AddDirectoryDialog.setTabOrder(self.targetDirPicker, self.recursiveCheckBox)

    def retranslateUi(self, AddDirectoryDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDirectoryDialog.setWindowTitle(_translate("AddDirectoryDialog", "Add Directory"))
        AddDirectoryDialog.setToolTip(_translate("AddDirectoryDialog", "Add a directory to the current project"))
        AddDirectoryDialog.setWhatsThis(_translate("AddDirectoryDialog", "<b>Add Directory Dialog</b>\n"
"<p>This dialog is used to add a directory to the current project.</p>"))
        self.textLabel1.setText(_translate("AddDirectoryDialog", "&File Type:"))
        self.sourceDirLabel.setText(_translate("AddDirectoryDialog", "&Source Directory:"))
        self.sourceDirPicker.setToolTip(_translate("AddDirectoryDialog", "Enter the name of the directory to add"))
        self.sourceDirPicker.setWhatsThis(_translate("AddDirectoryDialog", "<b>Source Directory</b>\n"
"<p>Enter the name of the directory to add to the current project.\n"
" You may select it with a dialog by pressing the button to the right.</p>"))
        self.targetDirLabel.setText(_translate("AddDirectoryDialog", "&Target Directory:"))
        self.targetDirPicker.setToolTip(_translate("AddDirectoryDialog", "Enter the target directory for the file"))
        self.targetDirPicker.setWhatsThis(_translate("AddDirectoryDialog", "<b>Target Directory</b>\n"
"<p>Enter the target directory. You may select it\n"
" with a dialog by pressing the button to the right.</p>"))
        self.recursiveCheckBox.setToolTip(_translate("AddDirectoryDialog", "Select, whether a recursive add should be performed"))
        self.recursiveCheckBox.setText(_translate("AddDirectoryDialog", "&Recurse into subdirectories"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddDirectoryDialog = QtWidgets.QDialog()
    ui = Ui_AddDirectoryDialog()
    ui.setupUi(AddDirectoryDialog)
    AddDirectoryDialog.show()
    sys.exit(app.exec_())

