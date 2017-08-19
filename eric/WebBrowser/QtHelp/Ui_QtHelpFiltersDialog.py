# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\QtHelp\QtHelpFiltersDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QtHelpFiltersDialog(object):
    def setupUi(self, QtHelpFiltersDialog):
        QtHelpFiltersDialog.setObjectName("QtHelpFiltersDialog")
        QtHelpFiltersDialog.resize(570, 391)
        QtHelpFiltersDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QtHelpFiltersDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(QtHelpFiltersDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(QtHelpFiltersDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)
        self.filtersList = QtWidgets.QListWidget(QtHelpFiltersDialog)
        self.filtersList.setAlternatingRowColors(True)
        self.filtersList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.filtersList.setObjectName("filtersList")
        self.gridLayout.addWidget(self.filtersList, 1, 0, 1, 2)
        self.attributesList = QtWidgets.QTreeWidget(QtHelpFiltersDialog)
        self.attributesList.setAlternatingRowColors(True)
        self.attributesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.attributesList.setRootIsDecorated(False)
        self.attributesList.setHeaderHidden(True)
        self.attributesList.setObjectName("attributesList")
        self.gridLayout.addWidget(self.attributesList, 1, 2, 1, 2)
        self.addButton = QtWidgets.QPushButton(QtHelpFiltersDialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 0, 1, 1)
        self.removeButton = QtWidgets.QPushButton(QtHelpFiltersDialog)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAttributeButton = QtWidgets.QPushButton(QtHelpFiltersDialog)
        self.removeAttributeButton.setObjectName("removeAttributeButton")
        self.gridLayout.addWidget(self.removeAttributeButton, 2, 2, 1, 1)
        self.unusedAttributesButton = QtWidgets.QPushButton(QtHelpFiltersDialog)
        self.unusedAttributesButton.setObjectName("unusedAttributesButton")
        self.gridLayout.addWidget(self.unusedAttributesButton, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(QtHelpFiltersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QtHelpFiltersDialog)
        self.buttonBox.rejected.connect(QtHelpFiltersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QtHelpFiltersDialog)
        QtHelpFiltersDialog.setTabOrder(self.filtersList, self.addButton)
        QtHelpFiltersDialog.setTabOrder(self.addButton, self.removeButton)
        QtHelpFiltersDialog.setTabOrder(self.removeButton, self.attributesList)
        QtHelpFiltersDialog.setTabOrder(self.attributesList, self.removeAttributeButton)
        QtHelpFiltersDialog.setTabOrder(self.removeAttributeButton, self.unusedAttributesButton)
        QtHelpFiltersDialog.setTabOrder(self.unusedAttributesButton, self.buttonBox)

    def retranslateUi(self, QtHelpFiltersDialog):
        _translate = QtCore.QCoreApplication.translate
        QtHelpFiltersDialog.setWindowTitle(_translate("QtHelpFiltersDialog", "Manage QtHelp Filters"))
        self.label.setText(_translate("QtHelpFiltersDialog", "Filters:"))
        self.label_2.setText(_translate("QtHelpFiltersDialog", "Attributes:"))
        self.filtersList.setSortingEnabled(True)
        self.attributesList.setSortingEnabled(True)
        self.attributesList.headerItem().setText(0, _translate("QtHelpFiltersDialog", "1"))
        self.addButton.setToolTip(_translate("QtHelpFiltersDialog", "Press to add a new filter"))
        self.addButton.setText(_translate("QtHelpFiltersDialog", "Add Filter ..."))
        self.removeButton.setToolTip(_translate("QtHelpFiltersDialog", "Press to remove the selected filters"))
        self.removeButton.setText(_translate("QtHelpFiltersDialog", "Remove Filters"))
        self.removeAttributeButton.setToolTip(_translate("QtHelpFiltersDialog", "Press to remove the selected attributes"))
        self.removeAttributeButton.setText(_translate("QtHelpFiltersDialog", "Remove Attributes"))
        self.unusedAttributesButton.setStatusTip(_translate("QtHelpFiltersDialog", "Press to select all unused attributes"))
        self.unusedAttributesButton.setText(_translate("QtHelpFiltersDialog", "Select Unused"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtHelpFiltersDialog = QtWidgets.QDialog()
    ui = Ui_QtHelpFiltersDialog()
    ui.setupUi(QtHelpFiltersDialog)
    QtHelpFiltersDialog.show()
    sys.exit(app.exec_())

