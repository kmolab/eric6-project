# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\FiletypeAssociationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FiletypeAssociationDialog(object):
    def setupUi(self, FiletypeAssociationDialog):
        FiletypeAssociationDialog.setObjectName("FiletypeAssociationDialog")
        FiletypeAssociationDialog.resize(600, 573)
        FiletypeAssociationDialog.setSizeGripEnabled(True)
        self._2 = QtWidgets.QVBoxLayout(FiletypeAssociationDialog)
        self._2.setObjectName("_2")
        self.filetypeAssociationList = QtWidgets.QTreeWidget(FiletypeAssociationDialog)
        self.filetypeAssociationList.setAlternatingRowColors(True)
        self.filetypeAssociationList.setRootIsDecorated(False)
        self.filetypeAssociationList.setItemsExpandable(False)
        self.filetypeAssociationList.setObjectName("filetypeAssociationList")
        self._2.addWidget(self.filetypeAssociationList)
        self._3 = QtWidgets.QGridLayout()
        self._3.setObjectName("_3")
        self.deleteAssociationButton = QtWidgets.QPushButton(FiletypeAssociationDialog)
        self.deleteAssociationButton.setEnabled(False)
        self.deleteAssociationButton.setObjectName("deleteAssociationButton")
        self._3.addWidget(self.deleteAssociationButton, 1, 2, 1, 1)
        self.filetypeCombo = QtWidgets.QComboBox(FiletypeAssociationDialog)
        self.filetypeCombo.setObjectName("filetypeCombo")
        self._3.addWidget(self.filetypeCombo, 1, 1, 1, 1)
        self.textLabel3_3 = QtWidgets.QLabel(FiletypeAssociationDialog)
        self.textLabel3_3.setObjectName("textLabel3_3")
        self._3.addWidget(self.textLabel3_3, 1, 0, 1, 1)
        self.filePatternEdit = QtWidgets.QLineEdit(FiletypeAssociationDialog)
        self.filePatternEdit.setObjectName("filePatternEdit")
        self._3.addWidget(self.filePatternEdit, 0, 1, 1, 1)
        self.textLabel2_6 = QtWidgets.QLabel(FiletypeAssociationDialog)
        self.textLabel2_6.setObjectName("textLabel2_6")
        self._3.addWidget(self.textLabel2_6, 0, 0, 1, 1)
        self.addAssociationButton = QtWidgets.QPushButton(FiletypeAssociationDialog)
        self.addAssociationButton.setEnabled(False)
        self.addAssociationButton.setObjectName("addAssociationButton")
        self._3.addWidget(self.addAssociationButton, 0, 2, 1, 1)
        self._2.addLayout(self._3)
        self.buttonBox = QtWidgets.QDialogButtonBox(FiletypeAssociationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self._2.addWidget(self.buttonBox)

        self.retranslateUi(FiletypeAssociationDialog)
        self.buttonBox.accepted.connect(FiletypeAssociationDialog.accept)
        self.buttonBox.rejected.connect(FiletypeAssociationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FiletypeAssociationDialog)
        FiletypeAssociationDialog.setTabOrder(self.filetypeAssociationList, self.filePatternEdit)
        FiletypeAssociationDialog.setTabOrder(self.filePatternEdit, self.filetypeCombo)
        FiletypeAssociationDialog.setTabOrder(self.filetypeCombo, self.addAssociationButton)
        FiletypeAssociationDialog.setTabOrder(self.addAssociationButton, self.deleteAssociationButton)

    def retranslateUi(self, FiletypeAssociationDialog):
        _translate = QtCore.QCoreApplication.translate
        FiletypeAssociationDialog.setWindowTitle(_translate("FiletypeAssociationDialog", "Filetype Associations"))
        self.filetypeAssociationList.setSortingEnabled(True)
        self.filetypeAssociationList.headerItem().setText(0, _translate("FiletypeAssociationDialog", "Filename Pattern"))
        self.filetypeAssociationList.headerItem().setText(1, _translate("FiletypeAssociationDialog", "Filetype"))
        self.deleteAssociationButton.setToolTip(_translate("FiletypeAssociationDialog", "Press to delete the selected association"))
        self.deleteAssociationButton.setText(_translate("FiletypeAssociationDialog", "Delete"))
        self.filetypeCombo.setToolTip(_translate("FiletypeAssociationDialog", "Select the filetype to associate"))
        self.textLabel3_3.setText(_translate("FiletypeAssociationDialog", "Filetype:"))
        self.filePatternEdit.setToolTip(_translate("FiletypeAssociationDialog", "Enter the filename pattern to be associated"))
        self.textLabel2_6.setText(_translate("FiletypeAssociationDialog", "Filename Pattern:"))
        self.addAssociationButton.setToolTip(_translate("FiletypeAssociationDialog", "Press to add or change the entered association"))
        self.addAssociationButton.setText(_translate("FiletypeAssociationDialog", "Add/Change"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FiletypeAssociationDialog = QtWidgets.QDialog()
    ui = Ui_FiletypeAssociationDialog()
    ui.setupUi(FiletypeAssociationDialog)
    FiletypeAssociationDialog.show()
    sys.exit(app.exec_())

