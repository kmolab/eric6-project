# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\RebaseExtension\HgRebaseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgRebaseDialog(object):
    def setupUi(self, HgRebaseDialog):
        HgRebaseDialog.setObjectName("HgRebaseDialog")
        HgRebaseDialog.resize(650, 394)
        HgRebaseDialog.setSizeGripEnabled(True)
        self.gridLayout_3 = QtWidgets.QGridLayout(HgRebaseDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(HgRebaseDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.parentButton = QtWidgets.QRadioButton(self.groupBox)
        self.parentButton.setChecked(True)
        self.parentButton.setObjectName("parentButton")
        self.verticalLayout.addWidget(self.parentButton)
        self.sourceButton = QtWidgets.QRadioButton(self.groupBox)
        self.sourceButton.setObjectName("sourceButton")
        self.verticalLayout.addWidget(self.sourceButton)
        self.baseButton = QtWidgets.QRadioButton(self.groupBox)
        self.baseButton.setObjectName("baseButton")
        self.verticalLayout.addWidget(self.baseButton)
        self.rev1GroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.rev1GroupBox.setEnabled(False)
        self.rev1GroupBox.setObjectName("rev1GroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.rev1GroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.number1Button = QtWidgets.QRadioButton(self.rev1GroupBox)
        self.number1Button.setChecked(True)
        self.number1Button.setObjectName("number1Button")
        self.gridLayout.addWidget(self.number1Button, 0, 0, 1, 1)
        self.number1SpinBox = QtWidgets.QSpinBox(self.rev1GroupBox)
        self.number1SpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.number1SpinBox.setMaximum(999999999)
        self.number1SpinBox.setObjectName("number1SpinBox")
        self.gridLayout.addWidget(self.number1SpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.id1Button = QtWidgets.QRadioButton(self.rev1GroupBox)
        self.id1Button.setObjectName("id1Button")
        self.gridLayout.addWidget(self.id1Button, 1, 0, 1, 1)
        self.id1Edit = QtWidgets.QLineEdit(self.rev1GroupBox)
        self.id1Edit.setEnabled(False)
        self.id1Edit.setObjectName("id1Edit")
        self.gridLayout.addWidget(self.id1Edit, 1, 1, 1, 2)
        self.tag1Button = QtWidgets.QRadioButton(self.rev1GroupBox)
        self.tag1Button.setObjectName("tag1Button")
        self.gridLayout.addWidget(self.tag1Button, 2, 0, 1, 1)
        self.tag1Combo = QtWidgets.QComboBox(self.rev1GroupBox)
        self.tag1Combo.setEnabled(False)
        self.tag1Combo.setEditable(True)
        self.tag1Combo.setObjectName("tag1Combo")
        self.gridLayout.addWidget(self.tag1Combo, 2, 1, 1, 2)
        self.branch1Button = QtWidgets.QRadioButton(self.rev1GroupBox)
        self.branch1Button.setObjectName("branch1Button")
        self.gridLayout.addWidget(self.branch1Button, 3, 0, 1, 1)
        self.branch1Combo = QtWidgets.QComboBox(self.rev1GroupBox)
        self.branch1Combo.setEnabled(False)
        self.branch1Combo.setEditable(True)
        self.branch1Combo.setObjectName("branch1Combo")
        self.gridLayout.addWidget(self.branch1Combo, 3, 1, 1, 2)
        self.bookmark1Button = QtWidgets.QRadioButton(self.rev1GroupBox)
        self.bookmark1Button.setObjectName("bookmark1Button")
        self.gridLayout.addWidget(self.bookmark1Button, 4, 0, 1, 1)
        self.bookmark1Combo = QtWidgets.QComboBox(self.rev1GroupBox)
        self.bookmark1Combo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmark1Combo.sizePolicy().hasHeightForWidth())
        self.bookmark1Combo.setSizePolicy(sizePolicy)
        self.bookmark1Combo.setEditable(True)
        self.bookmark1Combo.setObjectName("bookmark1Combo")
        self.gridLayout.addWidget(self.bookmark1Combo, 4, 1, 1, 2)
        self.verticalLayout.addWidget(self.rev1GroupBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rev2GroupBox = QtWidgets.QGroupBox(HgRebaseDialog)
        self.rev2GroupBox.setObjectName("rev2GroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.rev2GroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.number2Button = QtWidgets.QRadioButton(self.rev2GroupBox)
        self.number2Button.setObjectName("number2Button")
        self.gridLayout_2.addWidget(self.number2Button, 0, 0, 1, 1)
        self.number2SpinBox = QtWidgets.QSpinBox(self.rev2GroupBox)
        self.number2SpinBox.setEnabled(False)
        self.number2SpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.number2SpinBox.setMaximum(999999999)
        self.number2SpinBox.setObjectName("number2SpinBox")
        self.gridLayout_2.addWidget(self.number2SpinBox, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.id2Button = QtWidgets.QRadioButton(self.rev2GroupBox)
        self.id2Button.setObjectName("id2Button")
        self.gridLayout_2.addWidget(self.id2Button, 1, 0, 1, 1)
        self.id2Edit = QtWidgets.QLineEdit(self.rev2GroupBox)
        self.id2Edit.setEnabled(False)
        self.id2Edit.setObjectName("id2Edit")
        self.gridLayout_2.addWidget(self.id2Edit, 1, 1, 1, 2)
        self.tag2Button = QtWidgets.QRadioButton(self.rev2GroupBox)
        self.tag2Button.setObjectName("tag2Button")
        self.gridLayout_2.addWidget(self.tag2Button, 2, 0, 1, 1)
        self.tag2Combo = QtWidgets.QComboBox(self.rev2GroupBox)
        self.tag2Combo.setEnabled(False)
        self.tag2Combo.setEditable(True)
        self.tag2Combo.setObjectName("tag2Combo")
        self.gridLayout_2.addWidget(self.tag2Combo, 2, 1, 1, 2)
        self.branch2Button = QtWidgets.QRadioButton(self.rev2GroupBox)
        self.branch2Button.setObjectName("branch2Button")
        self.gridLayout_2.addWidget(self.branch2Button, 3, 0, 1, 1)
        self.branch2Combo = QtWidgets.QComboBox(self.rev2GroupBox)
        self.branch2Combo.setEnabled(False)
        self.branch2Combo.setEditable(True)
        self.branch2Combo.setObjectName("branch2Combo")
        self.gridLayout_2.addWidget(self.branch2Combo, 3, 1, 1, 2)
        self.bookmark2Button = QtWidgets.QRadioButton(self.rev2GroupBox)
        self.bookmark2Button.setObjectName("bookmark2Button")
        self.gridLayout_2.addWidget(self.bookmark2Button, 4, 0, 1, 1)
        self.bookmark2Combo = QtWidgets.QComboBox(self.rev2GroupBox)
        self.bookmark2Combo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmark2Combo.sizePolicy().hasHeightForWidth())
        self.bookmark2Combo.setSizePolicy(sizePolicy)
        self.bookmark2Combo.setEditable(True)
        self.bookmark2Combo.setObjectName("bookmark2Combo")
        self.gridLayout_2.addWidget(self.bookmark2Combo, 4, 1, 1, 2)
        self.tip2Button = QtWidgets.QRadioButton(self.rev2GroupBox)
        self.tip2Button.setChecked(True)
        self.tip2Button.setObjectName("tip2Button")
        self.gridLayout_2.addWidget(self.tip2Button, 5, 0, 1, 3)
        self.verticalLayout_2.addWidget(self.rev2GroupBox)
        self.collapseCheckBox = QtWidgets.QCheckBox(HgRebaseDialog)
        self.collapseCheckBox.setObjectName("collapseCheckBox")
        self.verticalLayout_2.addWidget(self.collapseCheckBox)
        self.keepChangesetsCheckBox = QtWidgets.QCheckBox(HgRebaseDialog)
        self.keepChangesetsCheckBox.setObjectName("keepChangesetsCheckBox")
        self.verticalLayout_2.addWidget(self.keepChangesetsCheckBox)
        self.keepBranchCheckBox = QtWidgets.QCheckBox(HgRebaseDialog)
        self.keepBranchCheckBox.setObjectName("keepBranchCheckBox")
        self.verticalLayout_2.addWidget(self.keepBranchCheckBox)
        self.detachCheckBox = QtWidgets.QCheckBox(HgRebaseDialog)
        self.detachCheckBox.setObjectName("detachCheckBox")
        self.verticalLayout_2.addWidget(self.detachCheckBox)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgRebaseDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(HgRebaseDialog)
        self.buttonBox.accepted.connect(HgRebaseDialog.accept)
        self.buttonBox.rejected.connect(HgRebaseDialog.reject)
        self.number1Button.toggled['bool'].connect(self.number1SpinBox.setEnabled)
        self.number2Button.toggled['bool'].connect(self.number2SpinBox.setEnabled)
        self.id1Button.toggled['bool'].connect(self.id1Edit.setEnabled)
        self.id2Button.toggled['bool'].connect(self.id2Edit.setEnabled)
        self.tag1Button.toggled['bool'].connect(self.tag1Combo.setEnabled)
        self.branch1Button.toggled['bool'].connect(self.branch1Combo.setEnabled)
        self.tag2Button.toggled['bool'].connect(self.tag2Combo.setEnabled)
        self.branch2Button.toggled['bool'].connect(self.branch2Combo.setEnabled)
        self.bookmark1Button.toggled['bool'].connect(self.bookmark1Combo.setEnabled)
        self.bookmark2Button.toggled['bool'].connect(self.bookmark2Combo.setEnabled)
        self.parentButton.toggled['bool'].connect(self.rev1GroupBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(HgRebaseDialog)
        HgRebaseDialog.setTabOrder(self.parentButton, self.sourceButton)
        HgRebaseDialog.setTabOrder(self.sourceButton, self.baseButton)
        HgRebaseDialog.setTabOrder(self.baseButton, self.number1Button)
        HgRebaseDialog.setTabOrder(self.number1Button, self.number1SpinBox)
        HgRebaseDialog.setTabOrder(self.number1SpinBox, self.id1Button)
        HgRebaseDialog.setTabOrder(self.id1Button, self.id1Edit)
        HgRebaseDialog.setTabOrder(self.id1Edit, self.tag1Button)
        HgRebaseDialog.setTabOrder(self.tag1Button, self.tag1Combo)
        HgRebaseDialog.setTabOrder(self.tag1Combo, self.branch1Button)
        HgRebaseDialog.setTabOrder(self.branch1Button, self.branch1Combo)
        HgRebaseDialog.setTabOrder(self.branch1Combo, self.bookmark1Button)
        HgRebaseDialog.setTabOrder(self.bookmark1Button, self.bookmark1Combo)
        HgRebaseDialog.setTabOrder(self.bookmark1Combo, self.number2Button)
        HgRebaseDialog.setTabOrder(self.number2Button, self.number2SpinBox)
        HgRebaseDialog.setTabOrder(self.number2SpinBox, self.id2Button)
        HgRebaseDialog.setTabOrder(self.id2Button, self.id2Edit)
        HgRebaseDialog.setTabOrder(self.id2Edit, self.tag2Button)
        HgRebaseDialog.setTabOrder(self.tag2Button, self.tag2Combo)
        HgRebaseDialog.setTabOrder(self.tag2Combo, self.branch2Button)
        HgRebaseDialog.setTabOrder(self.branch2Button, self.branch2Combo)
        HgRebaseDialog.setTabOrder(self.branch2Combo, self.bookmark2Button)
        HgRebaseDialog.setTabOrder(self.bookmark2Button, self.bookmark2Combo)
        HgRebaseDialog.setTabOrder(self.bookmark2Combo, self.tip2Button)
        HgRebaseDialog.setTabOrder(self.tip2Button, self.collapseCheckBox)
        HgRebaseDialog.setTabOrder(self.collapseCheckBox, self.keepChangesetsCheckBox)
        HgRebaseDialog.setTabOrder(self.keepChangesetsCheckBox, self.keepBranchCheckBox)
        HgRebaseDialog.setTabOrder(self.keepBranchCheckBox, self.detachCheckBox)
        HgRebaseDialog.setTabOrder(self.detachCheckBox, self.buttonBox)

    def retranslateUi(self, HgRebaseDialog):
        _translate = QtCore.QCoreApplication.translate
        HgRebaseDialog.setWindowTitle(_translate("HgRebaseDialog", "Rebase Changesets"))
        self.groupBox.setTitle(_translate("HgRebaseDialog", "Source / Base Revision"))
        self.parentButton.setToolTip(_translate("HgRebaseDialog", "Select to use the parent of the working directory as the base"))
        self.parentButton.setText(_translate("HgRebaseDialog", "Use &Parent as Base"))
        self.sourceButton.setToolTip(_translate("HgRebaseDialog", "Select to use a revision as the source"))
        self.sourceButton.setText(_translate("HgRebaseDialog", "&Source Revision"))
        self.baseButton.setToolTip(_translate("HgRebaseDialog", "Select to use a revision as the base"))
        self.baseButton.setText(_translate("HgRebaseDialog", "&Base Revision"))
        self.rev1GroupBox.setTitle(_translate("HgRebaseDialog", "&Revision"))
        self.number1Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by number"))
        self.number1Button.setText(_translate("HgRebaseDialog", "Number"))
        self.number1SpinBox.setToolTip(_translate("HgRebaseDialog", "Enter a revision number"))
        self.id1Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by changeset id"))
        self.id1Button.setText(_translate("HgRebaseDialog", "Id:"))
        self.id1Edit.setToolTip(_translate("HgRebaseDialog", "Enter a changeset id"))
        self.tag1Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by a tag"))
        self.tag1Button.setText(_translate("HgRebaseDialog", "Tag:"))
        self.tag1Combo.setToolTip(_translate("HgRebaseDialog", "Enter a tag name"))
        self.branch1Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by a branch"))
        self.branch1Button.setText(_translate("HgRebaseDialog", "Branch:"))
        self.branch1Combo.setToolTip(_translate("HgRebaseDialog", "Enter a branch name"))
        self.bookmark1Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by a bookmark"))
        self.bookmark1Button.setText(_translate("HgRebaseDialog", "Bookmark:"))
        self.bookmark1Combo.setToolTip(_translate("HgRebaseDialog", "Enter a bookmark name"))
        self.rev2GroupBox.setTitle(_translate("HgRebaseDialog", "&Destination Revision"))
        self.number2Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by number"))
        self.number2Button.setText(_translate("HgRebaseDialog", "Number"))
        self.number2SpinBox.setToolTip(_translate("HgRebaseDialog", "Enter a revision number"))
        self.id2Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by changeset id"))
        self.id2Button.setText(_translate("HgRebaseDialog", "Id:"))
        self.id2Edit.setToolTip(_translate("HgRebaseDialog", "Enter a changeset id"))
        self.tag2Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by a tag"))
        self.tag2Button.setText(_translate("HgRebaseDialog", "Tag:"))
        self.tag2Combo.setToolTip(_translate("HgRebaseDialog", "Enter a tag name"))
        self.branch2Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by a branch"))
        self.branch2Button.setText(_translate("HgRebaseDialog", "Branch:"))
        self.branch2Combo.setToolTip(_translate("HgRebaseDialog", "Enter a branch name"))
        self.bookmark2Button.setToolTip(_translate("HgRebaseDialog", "Select to specify a revision by a bookmark"))
        self.bookmark2Button.setText(_translate("HgRebaseDialog", "Bookmark:"))
        self.bookmark2Combo.setToolTip(_translate("HgRebaseDialog", "Enter a bookmark name"))
        self.tip2Button.setToolTip(_translate("HgRebaseDialog", "Select tip revision of repository"))
        self.tip2Button.setText(_translate("HgRebaseDialog", "Current branch tip"))
        self.collapseCheckBox.setToolTip(_translate("HgRebaseDialog", "Select to collapse the rebased changesets"))
        self.collapseCheckBox.setText(_translate("HgRebaseDialog", "Collapse Changesets"))
        self.keepChangesetsCheckBox.setToolTip(_translate("HgRebaseDialog", "Select to keep the original changesets"))
        self.keepChangesetsCheckBox.setText(_translate("HgRebaseDialog", "Keep Original Changesets"))
        self.keepBranchCheckBox.setToolTip(_translate("HgRebaseDialog", "Select to keep the original branch names"))
        self.keepBranchCheckBox.setText(_translate("HgRebaseDialog", "Keep Original Branch Name"))
        self.detachCheckBox.setToolTip(_translate("HgRebaseDialog", "Select to detach the source from its original branch"))
        self.detachCheckBox.setText(_translate("HgRebaseDialog", "Detach Source"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgRebaseDialog = QtWidgets.QDialog()
    ui = Ui_HgRebaseDialog()
    ui.setupUi(HgRebaseDialog)
    HgRebaseDialog.show()
    sys.exit(app.exec_())

