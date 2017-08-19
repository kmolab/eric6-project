# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\QueuesExtension\HgQueuesRenamePatchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesRenamePatchDialog(object):
    def setupUi(self, HgQueuesRenamePatchDialog):
        HgQueuesRenamePatchDialog.setObjectName("HgQueuesRenamePatchDialog")
        HgQueuesRenamePatchDialog.resize(400, 174)
        HgQueuesRenamePatchDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(HgQueuesRenamePatchDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(HgQueuesRenamePatchDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(HgQueuesRenamePatchDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(HgQueuesRenamePatchDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.currentButton = QtWidgets.QRadioButton(self.groupBox)
        self.currentButton.setText("Current Patch")
        self.currentButton.setChecked(True)
        self.currentButton.setObjectName("currentButton")
        self.verticalLayout.addWidget(self.currentButton)
        self.namedButton = QtWidgets.QRadioButton(self.groupBox)
        self.namedButton.setObjectName("namedButton")
        self.verticalLayout.addWidget(self.namedButton)
        self.nameCombo = QtWidgets.QComboBox(self.groupBox)
        self.nameCombo.setEnabled(False)
        self.nameCombo.setObjectName("nameCombo")
        self.verticalLayout.addWidget(self.nameCombo)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesRenamePatchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(HgQueuesRenamePatchDialog)
        self.buttonBox.accepted.connect(HgQueuesRenamePatchDialog.accept)
        self.buttonBox.rejected.connect(HgQueuesRenamePatchDialog.reject)
        self.namedButton.toggled['bool'].connect(self.nameCombo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesRenamePatchDialog)
        HgQueuesRenamePatchDialog.setTabOrder(self.nameEdit, self.currentButton)
        HgQueuesRenamePatchDialog.setTabOrder(self.currentButton, self.namedButton)
        HgQueuesRenamePatchDialog.setTabOrder(self.namedButton, self.nameCombo)
        HgQueuesRenamePatchDialog.setTabOrder(self.nameCombo, self.buttonBox)

    def retranslateUi(self, HgQueuesRenamePatchDialog):
        _translate = QtCore.QCoreApplication.translate
        HgQueuesRenamePatchDialog.setWindowTitle(_translate("HgQueuesRenamePatchDialog", "Rename Patch"))
        self.label.setText(_translate("HgQueuesRenamePatchDialog", "New Name:"))
        self.nameEdit.setToolTip(_translate("HgQueuesRenamePatchDialog", "Enter the new name for the selected patch"))
        self.groupBox.setTitle(_translate("HgQueuesRenamePatchDialog", "Patch"))
        self.currentButton.setToolTip(_translate("HgQueuesRenamePatchDialog", "Select to rename the current patch"))
        self.namedButton.setToolTip(_translate("HgQueuesRenamePatchDialog", "Select to rename the selected named patch"))
        self.namedButton.setText(_translate("HgQueuesRenamePatchDialog", "Named Patch"))
        self.nameCombo.setToolTip(_translate("HgQueuesRenamePatchDialog", "Select the patch to be renamed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgQueuesRenamePatchDialog = QtWidgets.QDialog()
    ui = Ui_HgQueuesRenamePatchDialog()
    ui.setupUi(HgQueuesRenamePatchDialog)
    HgQueuesRenamePatchDialog.show()
    sys.exit(app.exec_())

