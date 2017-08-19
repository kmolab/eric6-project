# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\CookieJar\CookiesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CookiesDialog(object):
    def setupUi(self, CookiesDialog):
        CookiesDialog.setObjectName("CookiesDialog")
        CookiesDialog.resize(500, 350)
        CookiesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(CookiesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(CookiesDialog)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 4)
        self.cookiesTable = E5TableView(CookiesDialog)
        self.cookiesTable.setAlternatingRowColors(True)
        self.cookiesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cookiesTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.cookiesTable.setShowGrid(False)
        self.cookiesTable.setSortingEnabled(True)
        self.cookiesTable.setObjectName("cookiesTable")
        self.gridLayout.addWidget(self.cookiesTable, 1, 0, 1, 4)
        self.removeButton = QtWidgets.QPushButton(CookiesDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 0, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(CookiesDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 2, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(CookiesDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CookiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 4)

        self.retranslateUi(CookiesDialog)
        self.buttonBox.accepted.connect(CookiesDialog.accept)
        self.buttonBox.rejected.connect(CookiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CookiesDialog)
        CookiesDialog.setTabOrder(self.searchEdit, self.cookiesTable)
        CookiesDialog.setTabOrder(self.cookiesTable, self.removeButton)
        CookiesDialog.setTabOrder(self.removeButton, self.removeAllButton)
        CookiesDialog.setTabOrder(self.removeAllButton, self.addButton)
        CookiesDialog.setTabOrder(self.addButton, self.buttonBox)

    def retranslateUi(self, CookiesDialog):
        _translate = QtCore.QCoreApplication.translate
        CookiesDialog.setWindowTitle(_translate("CookiesDialog", "Cookies"))
        self.searchEdit.setToolTip(_translate("CookiesDialog", "Enter search term for cookies"))
        self.removeButton.setToolTip(_translate("CookiesDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("CookiesDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("CookiesDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("CookiesDialog", "Remove &All"))
        self.addButton.setToolTip(_translate("CookiesDialog", "Press to open the cookies exceptions dialog to add a new rule"))
        self.addButton.setText(_translate("CookiesDialog", "Add R&ule..."))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TableView import E5TableView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CookiesDialog = QtWidgets.QDialog()
    ui = Ui_CookiesDialog()
    ui.setupUi(CookiesDialog)
    CookiesDialog.show()
    sys.exit(app.exec_())

