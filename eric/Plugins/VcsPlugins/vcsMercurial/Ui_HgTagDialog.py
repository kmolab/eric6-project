# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgTagDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgTagDialog(object):
    def setupUi(self, HgTagDialog):
        HgTagDialog.setObjectName("HgTagDialog")
        HgTagDialog.resize(391, 294)
        HgTagDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgTagDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.TextLabel1 = QtWidgets.QLabel(HgTagDialog)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridLayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.tagCombo = QtWidgets.QComboBox(HgTagDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagCombo.sizePolicy().hasHeightForWidth())
        self.tagCombo.setSizePolicy(sizePolicy)
        self.tagCombo.setEditable(True)
        self.tagCombo.setDuplicatesEnabled(False)
        self.tagCombo.setObjectName("tagCombo")
        self.gridLayout.addWidget(self.tagCombo, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(HgTagDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.revisionEdit = QtWidgets.QLineEdit(HgTagDialog)
        self.revisionEdit.setObjectName("revisionEdit")
        self.gridLayout.addWidget(self.revisionEdit, 1, 1, 1, 1)
        self.tagActionGroup = QtWidgets.QGroupBox(HgTagDialog)
        self.tagActionGroup.setObjectName("tagActionGroup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tagActionGroup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.createTagButton = QtWidgets.QRadioButton(self.tagActionGroup)
        self.createTagButton.setChecked(True)
        self.createTagButton.setObjectName("createTagButton")
        self.horizontalLayout_2.addWidget(self.createTagButton)
        self.deleteTagButton = QtWidgets.QRadioButton(self.tagActionGroup)
        self.deleteTagButton.setObjectName("deleteTagButton")
        self.horizontalLayout_2.addWidget(self.deleteTagButton)
        self.gridLayout.addWidget(self.tagActionGroup, 2, 0, 1, 2)
        self.forceCheckBox = QtWidgets.QCheckBox(HgTagDialog)
        self.forceCheckBox.setObjectName("forceCheckBox")
        self.gridLayout.addWidget(self.forceCheckBox, 3, 0, 1, 2)
        self.tagTypeGroup = QtWidgets.QGroupBox(HgTagDialog)
        self.tagTypeGroup.setObjectName("tagTypeGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tagTypeGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.globalTagButton = QtWidgets.QRadioButton(self.tagTypeGroup)
        self.globalTagButton.setChecked(True)
        self.globalTagButton.setObjectName("globalTagButton")
        self.horizontalLayout.addWidget(self.globalTagButton)
        self.localTagButton = QtWidgets.QRadioButton(self.tagTypeGroup)
        self.localTagButton.setObjectName("localTagButton")
        self.horizontalLayout.addWidget(self.localTagButton)
        self.gridLayout.addWidget(self.tagTypeGroup, 4, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgTagDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)

        self.retranslateUi(HgTagDialog)
        self.buttonBox.accepted.connect(HgTagDialog.accept)
        self.buttonBox.rejected.connect(HgTagDialog.reject)
        self.deleteTagButton.toggled['bool'].connect(self.revisionEdit.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(HgTagDialog)
        HgTagDialog.setTabOrder(self.tagCombo, self.revisionEdit)
        HgTagDialog.setTabOrder(self.revisionEdit, self.createTagButton)
        HgTagDialog.setTabOrder(self.createTagButton, self.deleteTagButton)
        HgTagDialog.setTabOrder(self.deleteTagButton, self.forceCheckBox)
        HgTagDialog.setTabOrder(self.forceCheckBox, self.globalTagButton)
        HgTagDialog.setTabOrder(self.globalTagButton, self.localTagButton)

    def retranslateUi(self, HgTagDialog):
        _translate = QtCore.QCoreApplication.translate
        HgTagDialog.setWindowTitle(_translate("HgTagDialog", "Mercurial Tag"))
        self.TextLabel1.setText(_translate("HgTagDialog", "Name:"))
        self.tagCombo.setToolTip(_translate("HgTagDialog", "Enter the name of the tag"))
        self.tagCombo.setWhatsThis(_translate("HgTagDialog", "<b>Tag Name</b>\n"
"<p>Enter the name of the tag to be created, moved or deleted.</p>"))
        self.label.setText(_translate("HgTagDialog", "Revision:"))
        self.revisionEdit.setToolTip(_translate("HgTagDialog", "Enter a revision to set a tag for"))
        self.tagActionGroup.setTitle(_translate("HgTagDialog", "Tag Action"))
        self.createTagButton.setToolTip(_translate("HgTagDialog", "Select to create a tag"))
        self.createTagButton.setWhatsThis(_translate("HgTagDialog", "<b>Create Tag</b>\n"
"<p>Select this entry in order to create a tag.</p>"))
        self.createTagButton.setText(_translate("HgTagDialog", "Create Tag"))
        self.deleteTagButton.setToolTip(_translate("HgTagDialog", "Select to delete a tag"))
        self.deleteTagButton.setWhatsThis(_translate("HgTagDialog", "<b>Delete Tag</b>\n"
"<p>Select this entry in order to delete the selected tag.</p>"))
        self.deleteTagButton.setText(_translate("HgTagDialog", "Delete Tag"))
        self.forceCheckBox.setToolTip(_translate("HgTagDialog", "Select to enforce the selected action"))
        self.forceCheckBox.setText(_translate("HgTagDialog", "Force Action"))
        self.tagTypeGroup.setTitle(_translate("HgTagDialog", "Tag Type"))
        self.globalTagButton.setToolTip(_translate("HgTagDialog", "Select to create/delete a global tag"))
        self.globalTagButton.setText(_translate("HgTagDialog", "Global Tag"))
        self.localTagButton.setToolTip(_translate("HgTagDialog", "Select to create/delete a local tag"))
        self.localTagButton.setText(_translate("HgTagDialog", "Local Tag"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgTagDialog = QtWidgets.QDialog()
    ui = Ui_HgTagDialog()
    ui.setupUi(HgTagDialog)
    HgTagDialog.show()
    sys.exit(app.exec_())

