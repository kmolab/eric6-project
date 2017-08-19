# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\LargefilesExtension\LfConvertDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LfConvertDataDialog(object):
    def setupUi(self, LfConvertDataDialog):
        LfConvertDataDialog.setObjectName("LfConvertDataDialog")
        LfConvertDataDialog.resize(500, 144)
        LfConvertDataDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(LfConvertDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.currentProjectLabel = E5SqueezeLabelPath(LfConvertDataDialog)
        self.currentProjectLabel.setObjectName("currentProjectLabel")
        self.gridLayout.addWidget(self.currentProjectLabel, 0, 0, 1, 3)
        self.label = QtWidgets.QLabel(LfConvertDataDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.newProjectPicker = E5PathPicker(LfConvertDataDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newProjectPicker.sizePolicy().hasHeightForWidth())
        self.newProjectPicker.setSizePolicy(sizePolicy)
        self.newProjectPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.newProjectPicker.setObjectName("newProjectPicker")
        self.gridLayout.addWidget(self.newProjectPicker, 1, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(LfConvertDataDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lfFileSizeSpinBox = QtWidgets.QSpinBox(LfConvertDataDialog)
        self.lfFileSizeSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lfFileSizeSpinBox.setMinimum(1)
        self.lfFileSizeSpinBox.setProperty("value", 10)
        self.lfFileSizeSpinBox.setObjectName("lfFileSizeSpinBox")
        self.gridLayout.addWidget(self.lfFileSizeSpinBox, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(297, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(LfConvertDataDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lfFilePatternsEdit = QtWidgets.QLineEdit(LfConvertDataDialog)
        self.lfFilePatternsEdit.setObjectName("lfFilePatternsEdit")
        self.gridLayout.addWidget(self.lfFilePatternsEdit, 3, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(LfConvertDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)

        self.retranslateUi(LfConvertDataDialog)
        self.buttonBox.accepted.connect(LfConvertDataDialog.accept)
        self.buttonBox.rejected.connect(LfConvertDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LfConvertDataDialog)
        LfConvertDataDialog.setTabOrder(self.newProjectPicker, self.lfFileSizeSpinBox)
        LfConvertDataDialog.setTabOrder(self.lfFileSizeSpinBox, self.lfFilePatternsEdit)

    def retranslateUi(self, LfConvertDataDialog):
        _translate = QtCore.QCoreApplication.translate
        LfConvertDataDialog.setWindowTitle(_translate("LfConvertDataDialog", "Convert Repository Format"))
        self.label.setText(_translate("LfConvertDataDialog", "New project directory:"))
        self.newProjectPicker.setToolTip(_translate("LfConvertDataDialog", "Enter the directory name of the new project directory"))
        self.label_4.setText(_translate("LfConvertDataDialog", "Minimum file size:"))
        self.lfFileSizeSpinBox.setToolTip(_translate("LfConvertDataDialog", "Enter the minimum file size in MB for files to be treated as Large Files"))
        self.lfFileSizeSpinBox.setSuffix(_translate("LfConvertDataDialog", " MB"))
        self.label_5.setText(_translate("LfConvertDataDialog", "Patterns:"))
        self.lfFilePatternsEdit.setToolTip(_translate("LfConvertDataDialog", "Enter file patterns (space separated) for files to be treated as Large Files"))

from E5Gui.E5PathPicker import E5PathPicker
from E5Gui.E5SqueezeLabels import E5SqueezeLabelPath

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LfConvertDataDialog = QtWidgets.QDialog()
    ui = Ui_LfConvertDataDialog()
    ui.setupUi(LfConvertDataDialog)
    LfConvertDataDialog.show()
    sys.exit(app.exec_())

