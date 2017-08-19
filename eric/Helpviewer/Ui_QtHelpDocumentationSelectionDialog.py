# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\QtHelpDocumentationSelectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QtHelpDocumentationSelectionDialog(object):
    def setupUi(self, QtHelpDocumentationSelectionDialog):
        QtHelpDocumentationSelectionDialog.setObjectName("QtHelpDocumentationSelectionDialog")
        QtHelpDocumentationSelectionDialog.resize(450, 500)
        QtHelpDocumentationSelectionDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QtHelpDocumentationSelectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(QtHelpDocumentationSelectionDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.documentationList = QtWidgets.QTreeWidget(QtHelpDocumentationSelectionDialog)
        self.documentationList.setAlternatingRowColors(True)
        self.documentationList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.documentationList.setAllColumnsShowFocus(True)
        self.documentationList.setObjectName("documentationList")
        self.documentationList.headerItem().setText(0, "1")
        self.documentationList.header().setVisible(False)
        self.verticalLayout.addWidget(self.documentationList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteButton = QtWidgets.QPushButton(QtHelpDocumentationSelectionDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.deleteCategoryButton = QtWidgets.QPushButton(QtHelpDocumentationSelectionDialog)
        self.deleteCategoryButton.setObjectName("deleteCategoryButton")
        self.horizontalLayout.addWidget(self.deleteCategoryButton)
        self.deleteAllButton = QtWidgets.QPushButton(QtHelpDocumentationSelectionDialog)
        self.deleteAllButton.setObjectName("deleteAllButton")
        self.horizontalLayout.addWidget(self.deleteAllButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(QtHelpDocumentationSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QtHelpDocumentationSelectionDialog)
        self.buttonBox.accepted.connect(QtHelpDocumentationSelectionDialog.accept)
        self.buttonBox.rejected.connect(QtHelpDocumentationSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QtHelpDocumentationSelectionDialog)
        QtHelpDocumentationSelectionDialog.setTabOrder(self.documentationList, self.deleteButton)
        QtHelpDocumentationSelectionDialog.setTabOrder(self.deleteButton, self.deleteCategoryButton)
        QtHelpDocumentationSelectionDialog.setTabOrder(self.deleteCategoryButton, self.deleteAllButton)

    def retranslateUi(self, QtHelpDocumentationSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        QtHelpDocumentationSelectionDialog.setWindowTitle(_translate("QtHelpDocumentationSelectionDialog", "QtHelp Documentations"))
        self.label.setText(_translate("QtHelpDocumentationSelectionDialog", "Select the documentation files to be installed:"))
        self.documentationList.setSortingEnabled(True)
        self.deleteButton.setToolTip(_translate("QtHelpDocumentationSelectionDialog", "Press to delete the selected documentation sets"))
        self.deleteButton.setText(_translate("QtHelpDocumentationSelectionDialog", "Delete"))
        self.deleteCategoryButton.setToolTip(_translate("QtHelpDocumentationSelectionDialog", "Press to delete the selected category"))
        self.deleteCategoryButton.setText(_translate("QtHelpDocumentationSelectionDialog", "Delete Categories"))
        self.deleteAllButton.setToolTip(_translate("QtHelpDocumentationSelectionDialog", "Press to delete all entries"))
        self.deleteAllButton.setText(_translate("QtHelpDocumentationSelectionDialog", "Delete All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtHelpDocumentationSelectionDialog = QtWidgets.QDialog()
    ui = Ui_QtHelpDocumentationSelectionDialog()
    ui.setupUi(QtHelpDocumentationSelectionDialog)
    QtHelpDocumentationSelectionDialog.show()
    sys.exit(app.exec_())

