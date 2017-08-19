# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnTagDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnTagDialog(object):
    def setupUi(self, SvnTagDialog):
        SvnTagDialog.setObjectName("SvnTagDialog")
        SvnTagDialog.resize(391, 197)
        SvnTagDialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(SvnTagDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnTagDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.tagCombo = QtWidgets.QComboBox(SvnTagDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagCombo.sizePolicy().hasHeightForWidth())
        self.tagCombo.setSizePolicy(sizePolicy)
        self.tagCombo.setEditable(True)
        self.tagCombo.setDuplicatesEnabled(False)
        self.tagCombo.setObjectName("tagCombo")
        self.gridlayout.addWidget(self.tagCombo, 0, 1, 1, 1)
        self.TextLabel1 = QtWidgets.QLabel(SvnTagDialog)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridlayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.TagActionGroup = QtWidgets.QGroupBox(SvnTagDialog)
        self.TagActionGroup.setObjectName("TagActionGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.TagActionGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.createRegularButton = QtWidgets.QRadioButton(self.TagActionGroup)
        self.createRegularButton.setChecked(True)
        self.createRegularButton.setObjectName("createRegularButton")
        self.vboxlayout.addWidget(self.createRegularButton)
        self.createBranchButton = QtWidgets.QRadioButton(self.TagActionGroup)
        self.createBranchButton.setObjectName("createBranchButton")
        self.vboxlayout.addWidget(self.createBranchButton)
        self.deleteRegularButton = QtWidgets.QRadioButton(self.TagActionGroup)
        self.deleteRegularButton.setObjectName("deleteRegularButton")
        self.vboxlayout.addWidget(self.deleteRegularButton)
        self.deleteBranchButton = QtWidgets.QRadioButton(self.TagActionGroup)
        self.deleteBranchButton.setObjectName("deleteBranchButton")
        self.vboxlayout.addWidget(self.deleteBranchButton)
        self.gridlayout.addWidget(self.TagActionGroup, 1, 1, 1, 1)

        self.retranslateUi(SvnTagDialog)
        self.buttonBox.accepted.connect(SvnTagDialog.accept)
        self.buttonBox.rejected.connect(SvnTagDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnTagDialog)
        SvnTagDialog.setTabOrder(self.tagCombo, self.createRegularButton)
        SvnTagDialog.setTabOrder(self.createRegularButton, self.createBranchButton)
        SvnTagDialog.setTabOrder(self.createBranchButton, self.deleteRegularButton)
        SvnTagDialog.setTabOrder(self.deleteRegularButton, self.deleteBranchButton)

    def retranslateUi(self, SvnTagDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnTagDialog.setWindowTitle(_translate("SvnTagDialog", "Subversion Tag"))
        self.tagCombo.setToolTip(_translate("SvnTagDialog", "Enter the name of the tag"))
        self.tagCombo.setWhatsThis(_translate("SvnTagDialog", "<b>Tag Name</b>\n"
"<p>Enter the name of the tag to be created, moved or deleted.</p>"))
        self.TextLabel1.setText(_translate("SvnTagDialog", "Name:"))
        self.TagActionGroup.setTitle(_translate("SvnTagDialog", "Tag Action"))
        self.createRegularButton.setToolTip(_translate("SvnTagDialog", "Select to create a regular tag"))
        self.createRegularButton.setWhatsThis(_translate("SvnTagDialog", "<b>Create Regular Tag</b>\n"
"<p>Select this entry in order to create a regular tag in the repository.</p>"))
        self.createRegularButton.setText(_translate("SvnTagDialog", "Create Regular Tag"))
        self.createBranchButton.setToolTip(_translate("SvnTagDialog", "Select to create a branch tag"))
        self.createBranchButton.setWhatsThis(_translate("SvnTagDialog", "<b>Create Branch Tag</b>\n"
"<p>Select this entry in order to create a branch in the repository.</p>"))
        self.createBranchButton.setText(_translate("SvnTagDialog", "Create Branch Tag"))
        self.deleteRegularButton.setToolTip(_translate("SvnTagDialog", "Select to delete a regular tag"))
        self.deleteRegularButton.setWhatsThis(_translate("SvnTagDialog", "<b>Delete Regular Tag</b>\n"
"<p>Select this entry in order to delete the selected regular tag.</p>"))
        self.deleteRegularButton.setText(_translate("SvnTagDialog", "Delete Regular Tag"))
        self.deleteBranchButton.setToolTip(_translate("SvnTagDialog", "Select to delete a branch tag"))
        self.deleteBranchButton.setWhatsThis(_translate("SvnTagDialog", "<b>Delete Branch Tag</b>\n"
"<p>Select this entry in order to delete the selected branch tag.</p>"))
        self.deleteBranchButton.setText(_translate("SvnTagDialog", "Delete Branch Tag"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnTagDialog = QtWidgets.QDialog()
    ui = Ui_SvnTagDialog()
    ui.setupUi(SvnTagDialog)
    SvnTagDialog.show()
    sys.exit(app.exec_())

