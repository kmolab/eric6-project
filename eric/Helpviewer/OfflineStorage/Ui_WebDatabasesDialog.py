# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\OfflineStorage\WebDatabasesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebDatabasesDialog(object):
    def setupUi(self, WebDatabasesDialog):
        WebDatabasesDialog.setObjectName("WebDatabasesDialog")
        WebDatabasesDialog.resize(500, 357)
        WebDatabasesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(WebDatabasesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(WebDatabasesDialog)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.databasesTree = E5TreeView(WebDatabasesDialog)
        self.databasesTree.setAlternatingRowColors(True)
        self.databasesTree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.databasesTree.setObjectName("databasesTree")
        self.gridLayout.addWidget(self.databasesTree, 1, 0, 1, 3)
        self.removeButton = QtWidgets.QPushButton(WebDatabasesDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 0, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(WebDatabasesDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(309, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(WebDatabasesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)

        self.retranslateUi(WebDatabasesDialog)
        self.buttonBox.accepted.connect(WebDatabasesDialog.accept)
        self.buttonBox.rejected.connect(WebDatabasesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WebDatabasesDialog)
        WebDatabasesDialog.setTabOrder(self.searchEdit, self.databasesTree)
        WebDatabasesDialog.setTabOrder(self.databasesTree, self.removeButton)
        WebDatabasesDialog.setTabOrder(self.removeButton, self.removeAllButton)
        WebDatabasesDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, WebDatabasesDialog):
        _translate = QtCore.QCoreApplication.translate
        WebDatabasesDialog.setWindowTitle(_translate("WebDatabasesDialog", "Web SQL Databases"))
        self.searchEdit.setToolTip(_translate("WebDatabasesDialog", "Enter search term for databases"))
        self.removeButton.setToolTip(_translate("WebDatabasesDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("WebDatabasesDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("WebDatabasesDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("WebDatabasesDialog", "Remove &All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TreeView import E5TreeView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WebDatabasesDialog = QtWidgets.QDialog()
    ui = Ui_WebDatabasesDialog()
    ui.setupUi(WebDatabasesDialog)
    WebDatabasesDialog.show()
    sys.exit(app.exec_())

