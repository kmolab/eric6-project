# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgRevisionSelectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgRevisionSelectionDialog(object):
    def setupUi(self, HgRevisionSelectionDialog):
        HgRevisionSelectionDialog.setObjectName("HgRevisionSelectionDialog")
        HgRevisionSelectionDialog.resize(372, 250)
        HgRevisionSelectionDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgRevisionSelectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(HgRevisionSelectionDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.numberButton = QtWidgets.QRadioButton(self.groupBox)
        self.numberButton.setObjectName("numberButton")
        self.gridLayout.addWidget(self.numberButton, 0, 0, 1, 1)
        self.numberSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.numberSpinBox.setEnabled(False)
        self.numberSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.numberSpinBox.setMaximum(999999999)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.gridLayout.addWidget(self.numberSpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.idButton = QtWidgets.QRadioButton(self.groupBox)
        self.idButton.setObjectName("idButton")
        self.gridLayout.addWidget(self.idButton, 1, 0, 1, 1)
        self.idEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idEdit.setEnabled(False)
        self.idEdit.setObjectName("idEdit")
        self.gridLayout.addWidget(self.idEdit, 1, 1, 1, 2)
        self.tagButton = QtWidgets.QRadioButton(self.groupBox)
        self.tagButton.setObjectName("tagButton")
        self.gridLayout.addWidget(self.tagButton, 2, 0, 1, 1)
        self.tagCombo = QtWidgets.QComboBox(self.groupBox)
        self.tagCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagCombo.sizePolicy().hasHeightForWidth())
        self.tagCombo.setSizePolicy(sizePolicy)
        self.tagCombo.setEditable(True)
        self.tagCombo.setObjectName("tagCombo")
        self.gridLayout.addWidget(self.tagCombo, 2, 1, 1, 2)
        self.branchButton = QtWidgets.QRadioButton(self.groupBox)
        self.branchButton.setObjectName("branchButton")
        self.gridLayout.addWidget(self.branchButton, 3, 0, 1, 1)
        self.branchCombo = QtWidgets.QComboBox(self.groupBox)
        self.branchCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.branchCombo.sizePolicy().hasHeightForWidth())
        self.branchCombo.setSizePolicy(sizePolicy)
        self.branchCombo.setEditable(True)
        self.branchCombo.setObjectName("branchCombo")
        self.gridLayout.addWidget(self.branchCombo, 3, 1, 1, 2)
        self.bookmarkButton = QtWidgets.QRadioButton(self.groupBox)
        self.bookmarkButton.setObjectName("bookmarkButton")
        self.gridLayout.addWidget(self.bookmarkButton, 4, 0, 1, 1)
        self.bookmarkCombo = QtWidgets.QComboBox(self.groupBox)
        self.bookmarkCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmarkCombo.sizePolicy().hasHeightForWidth())
        self.bookmarkCombo.setSizePolicy(sizePolicy)
        self.bookmarkCombo.setEditable(True)
        self.bookmarkCombo.setObjectName("bookmarkCombo")
        self.gridLayout.addWidget(self.bookmarkCombo, 4, 1, 1, 2)
        self.tipButton = QtWidgets.QRadioButton(self.groupBox)
        self.tipButton.setObjectName("tipButton")
        self.gridLayout.addWidget(self.tipButton, 5, 0, 1, 3)
        self.noneButton = QtWidgets.QRadioButton(self.groupBox)
        self.noneButton.setChecked(True)
        self.noneButton.setObjectName("noneButton")
        self.gridLayout.addWidget(self.noneButton, 6, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgRevisionSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgRevisionSelectionDialog)
        self.buttonBox.accepted.connect(HgRevisionSelectionDialog.accept)
        self.buttonBox.rejected.connect(HgRevisionSelectionDialog.reject)
        self.numberButton.toggled['bool'].connect(self.numberSpinBox.setEnabled)
        self.idButton.toggled['bool'].connect(self.idEdit.setEnabled)
        self.tagButton.toggled['bool'].connect(self.tagCombo.setEnabled)
        self.branchButton.toggled['bool'].connect(self.branchCombo.setEnabled)
        self.bookmarkButton.toggled['bool'].connect(self.bookmarkCombo.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(HgRevisionSelectionDialog)
        HgRevisionSelectionDialog.setTabOrder(self.numberButton, self.numberSpinBox)
        HgRevisionSelectionDialog.setTabOrder(self.numberSpinBox, self.idButton)
        HgRevisionSelectionDialog.setTabOrder(self.idButton, self.idEdit)
        HgRevisionSelectionDialog.setTabOrder(self.idEdit, self.tagButton)
        HgRevisionSelectionDialog.setTabOrder(self.tagButton, self.tagCombo)
        HgRevisionSelectionDialog.setTabOrder(self.tagCombo, self.branchButton)
        HgRevisionSelectionDialog.setTabOrder(self.branchButton, self.branchCombo)
        HgRevisionSelectionDialog.setTabOrder(self.branchCombo, self.bookmarkButton)
        HgRevisionSelectionDialog.setTabOrder(self.bookmarkButton, self.bookmarkCombo)
        HgRevisionSelectionDialog.setTabOrder(self.bookmarkCombo, self.tipButton)
        HgRevisionSelectionDialog.setTabOrder(self.tipButton, self.noneButton)
        HgRevisionSelectionDialog.setTabOrder(self.noneButton, self.buttonBox)

    def retranslateUi(self, HgRevisionSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        HgRevisionSelectionDialog.setWindowTitle(_translate("HgRevisionSelectionDialog", "Mercurial Revision"))
        self.groupBox.setTitle(_translate("HgRevisionSelectionDialog", "Revision"))
        self.numberButton.setToolTip(_translate("HgRevisionSelectionDialog", "Select to specify a revision by number"))
        self.numberButton.setText(_translate("HgRevisionSelectionDialog", "Number"))
        self.numberSpinBox.setToolTip(_translate("HgRevisionSelectionDialog", "Enter a revision number"))
        self.idButton.setToolTip(_translate("HgRevisionSelectionDialog", "Select to specify a revision by changeset id"))
        self.idButton.setText(_translate("HgRevisionSelectionDialog", "Id:"))
        self.idEdit.setToolTip(_translate("HgRevisionSelectionDialog", "Enter a changeset id"))
        self.tagButton.setToolTip(_translate("HgRevisionSelectionDialog", "Select to specify a revision by a tag"))
        self.tagButton.setText(_translate("HgRevisionSelectionDialog", "Tag:"))
        self.tagCombo.setToolTip(_translate("HgRevisionSelectionDialog", "Enter a tag name"))
        self.branchButton.setToolTip(_translate("HgRevisionSelectionDialog", "Select to specify a revision by a branch"))
        self.branchButton.setText(_translate("HgRevisionSelectionDialog", "Branch:"))
        self.branchCombo.setToolTip(_translate("HgRevisionSelectionDialog", "Enter a branch name"))
        self.bookmarkButton.setToolTip(_translate("HgRevisionSelectionDialog", "Select to specify a revision by a bookmark"))
        self.bookmarkButton.setText(_translate("HgRevisionSelectionDialog", "Bookmark:"))
        self.bookmarkCombo.setToolTip(_translate("HgRevisionSelectionDialog", "Enter a bookmark name"))
        self.tipButton.setToolTip(_translate("HgRevisionSelectionDialog", "Select tip revision of repository"))
        self.tipButton.setText(_translate("HgRevisionSelectionDialog", "TIP"))
        self.noneButton.setText(_translate("HgRevisionSelectionDialog", "No revision selected"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgRevisionSelectionDialog = QtWidgets.QDialog()
    ui = Ui_HgRevisionSelectionDialog()
    ui.setupUi(HgRevisionSelectionDialog)
    HgRevisionSelectionDialog.show()
    sys.exit(app.exec_())

