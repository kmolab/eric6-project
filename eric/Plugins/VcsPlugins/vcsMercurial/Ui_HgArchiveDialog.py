# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgArchiveDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgArchiveDialog(object):
    def setupUi(self, HgArchiveDialog):
        HgArchiveDialog.setObjectName("HgArchiveDialog")
        HgArchiveDialog.resize(400, 149)
        HgArchiveDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgArchiveDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgArchiveDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.archivePicker = E5PathPicker(HgArchiveDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.archivePicker.sizePolicy().hasHeightForWidth())
        self.archivePicker.setSizePolicy(sizePolicy)
        self.archivePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.archivePicker.setObjectName("archivePicker")
        self.gridLayout.addWidget(self.archivePicker, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HgArchiveDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.typeComboBox = QtWidgets.QComboBox(HgArchiveDialog)
        self.typeComboBox.setObjectName("typeComboBox")
        self.gridLayout.addWidget(self.typeComboBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(HgArchiveDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.prefixEdit = QtWidgets.QLineEdit(HgArchiveDialog)
        self.prefixEdit.setObjectName("prefixEdit")
        self.gridLayout.addWidget(self.prefixEdit, 2, 1, 1, 1)
        self.subReposCheckBox = QtWidgets.QCheckBox(HgArchiveDialog)
        self.subReposCheckBox.setObjectName("subReposCheckBox")
        self.gridLayout.addWidget(self.subReposCheckBox, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgArchiveDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)

        self.retranslateUi(HgArchiveDialog)
        self.buttonBox.accepted.connect(HgArchiveDialog.accept)
        self.buttonBox.rejected.connect(HgArchiveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgArchiveDialog)
        HgArchiveDialog.setTabOrder(self.archivePicker, self.typeComboBox)
        HgArchiveDialog.setTabOrder(self.typeComboBox, self.prefixEdit)
        HgArchiveDialog.setTabOrder(self.prefixEdit, self.subReposCheckBox)

    def retranslateUi(self, HgArchiveDialog):
        _translate = QtCore.QCoreApplication.translate
        HgArchiveDialog.setWindowTitle(_translate("HgArchiveDialog", "Mercurial Archive"))
        self.label.setText(_translate("HgArchiveDialog", "Archive:"))
        self.archivePicker.setToolTip(_translate("HgArchiveDialog", "Enter the file name of the archive"))
        self.label_3.setText(_translate("HgArchiveDialog", "Type:"))
        self.typeComboBox.setToolTip(_translate("HgArchiveDialog", "Select the archive type"))
        self.label_2.setText(_translate("HgArchiveDialog", "Prefix:"))
        self.prefixEdit.setToolTip(_translate("HgArchiveDialog", "Enter the directory prefix for the files in the archive"))
        self.subReposCheckBox.setToolTip(_translate("HgArchiveDialog", "Select to recurse into subrepositories"))
        self.subReposCheckBox.setText(_translate("HgArchiveDialog", "Include Subrepositories"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgArchiveDialog = QtWidgets.QDialog()
    ui = Ui_HgArchiveDialog()
    ui.setupUi(HgArchiveDialog)
    HgArchiveDialog.show()
    sys.exit(app.exec_())

