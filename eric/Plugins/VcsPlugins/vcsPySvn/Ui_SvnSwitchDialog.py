# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnSwitchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnSwitchDialog(object):
    def setupUi(self, SvnSwitchDialog):
        SvnSwitchDialog.setObjectName("SvnSwitchDialog")
        SvnSwitchDialog.resize(391, 146)
        SvnSwitchDialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(SvnSwitchDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnSwitchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.TextLabel1 = QtWidgets.QLabel(SvnSwitchDialog)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.tagCombo = QtWidgets.QComboBox(SvnSwitchDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagCombo.sizePolicy().hasHeightForWidth())
        self.tagCombo.setSizePolicy(sizePolicy)
        self.tagCombo.setEditable(True)
        self.tagCombo.setDuplicatesEnabled(False)
        self.tagCombo.setObjectName("tagCombo")
        self.gridlayout.addWidget(self.tagCombo, 0, 1, 1, 1)
        self.TagTypeGroup = QtWidgets.QGroupBox(SvnSwitchDialog)
        self.TagTypeGroup.setObjectName("TagTypeGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.TagTypeGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.regularButton = QtWidgets.QRadioButton(self.TagTypeGroup)
        self.regularButton.setChecked(True)
        self.regularButton.setObjectName("regularButton")
        self.vboxlayout.addWidget(self.regularButton)
        self.branchButton = QtWidgets.QRadioButton(self.TagTypeGroup)
        self.branchButton.setObjectName("branchButton")
        self.vboxlayout.addWidget(self.branchButton)
        self.gridlayout.addWidget(self.TagTypeGroup, 1, 1, 1, 1)

        self.retranslateUi(SvnSwitchDialog)
        self.buttonBox.accepted.connect(SvnSwitchDialog.accept)
        self.buttonBox.rejected.connect(SvnSwitchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnSwitchDialog)
        SvnSwitchDialog.setTabOrder(self.tagCombo, self.regularButton)
        SvnSwitchDialog.setTabOrder(self.regularButton, self.branchButton)

    def retranslateUi(self, SvnSwitchDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnSwitchDialog.setWindowTitle(_translate("SvnSwitchDialog", "Subversion Switch"))
        self.TextLabel1.setText(_translate("SvnSwitchDialog", "Tag Name:"))
        self.tagCombo.setToolTip(_translate("SvnSwitchDialog", "Enter the name of the tag"))
        self.tagCombo.setWhatsThis(_translate("SvnSwitchDialog", "<b>Tag Name</b>\n"
"<p>Enter the name of the tag to be switched to.\n"
"In order to switch to the trunk version leave it empty.</p>"))
        self.TagTypeGroup.setTitle(_translate("SvnSwitchDialog", "Tag Type"))
        self.regularButton.setToolTip(_translate("SvnSwitchDialog", "Select for a regular tag"))
        self.regularButton.setWhatsThis(_translate("SvnSwitchDialog", "<b>Regular Tag</b>\n"
"<p>Select this entry for a regular tag.</p>"))
        self.regularButton.setText(_translate("SvnSwitchDialog", "Regular Tag"))
        self.branchButton.setToolTip(_translate("SvnSwitchDialog", "Select for a branch tag"))
        self.branchButton.setWhatsThis(_translate("SvnSwitchDialog", "<b>Branch Tag</b>\n"
"<p>Select this entry for a branch tag.</p>"))
        self.branchButton.setText(_translate("SvnSwitchDialog", "Branch Tag"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnSwitchDialog = QtWidgets.QDialog()
    ui = Ui_SvnSwitchDialog()
    ui.setupUi(SvnSwitchDialog)
    SvnSwitchDialog.show()
    sys.exit(app.exec_())

