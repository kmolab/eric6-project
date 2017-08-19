# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgBranchInputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgBranchInputDialog(object):
    def setupUi(self, HgBranchInputDialog):
        HgBranchInputDialog.setObjectName("HgBranchInputDialog")
        HgBranchInputDialog.resize(400, 128)
        HgBranchInputDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgBranchInputDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(HgBranchInputDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.branchComboBox = QtWidgets.QComboBox(HgBranchInputDialog)
        self.branchComboBox.setEditable(True)
        self.branchComboBox.setObjectName("branchComboBox")
        self.verticalLayout.addWidget(self.branchComboBox)
        self.commitCheckBox = QtWidgets.QCheckBox(HgBranchInputDialog)
        self.commitCheckBox.setObjectName("commitCheckBox")
        self.verticalLayout.addWidget(self.commitCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgBranchInputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgBranchInputDialog)
        self.buttonBox.accepted.connect(HgBranchInputDialog.accept)
        self.buttonBox.rejected.connect(HgBranchInputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgBranchInputDialog)
        HgBranchInputDialog.setTabOrder(self.branchComboBox, self.commitCheckBox)
        HgBranchInputDialog.setTabOrder(self.commitCheckBox, self.buttonBox)

    def retranslateUi(self, HgBranchInputDialog):
        _translate = QtCore.QCoreApplication.translate
        HgBranchInputDialog.setWindowTitle(_translate("HgBranchInputDialog", "Create Branch"))
        self.label.setText(_translate("HgBranchInputDialog", "Enter branch name:"))
        self.branchComboBox.setToolTip(_translate("HgBranchInputDialog", "Enter the new branch name (spaces will be converted to _)"))
        self.commitCheckBox.setToolTip(_translate("HgBranchInputDialog", "Select to commit the branch"))
        self.commitCheckBox.setText(_translate("HgBranchInputDialog", "Commit Branch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgBranchInputDialog = QtWidgets.QDialog()
    ui = Ui_HgBranchInputDialog()
    ui.setupUi(HgBranchInputDialog)
    HgBranchInputDialog.show()
    sys.exit(app.exec_())

