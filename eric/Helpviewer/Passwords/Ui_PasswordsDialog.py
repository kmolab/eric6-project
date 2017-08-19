# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\Passwords\PasswordsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PasswordsDialog(object):
    def setupUi(self, PasswordsDialog):
        PasswordsDialog.setObjectName("PasswordsDialog")
        PasswordsDialog.resize(500, 350)
        PasswordsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PasswordsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(PasswordsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.passwordsTable = E5TableView(PasswordsDialog)
        self.passwordsTable.setAlternatingRowColors(True)
        self.passwordsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.passwordsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.passwordsTable.setShowGrid(False)
        self.passwordsTable.setSortingEnabled(True)
        self.passwordsTable.setObjectName("passwordsTable")
        self.verticalLayout.addWidget(self.passwordsTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.removeButton = QtWidgets.QPushButton(PasswordsDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtWidgets.QPushButton(PasswordsDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.horizontalLayout_3.addWidget(self.removeAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.passwordsButton = QtWidgets.QPushButton(PasswordsDialog)
        self.passwordsButton.setText("")
        self.passwordsButton.setObjectName("passwordsButton")
        self.horizontalLayout_3.addWidget(self.passwordsButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(PasswordsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PasswordsDialog)
        self.buttonBox.accepted.connect(PasswordsDialog.accept)
        self.buttonBox.rejected.connect(PasswordsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PasswordsDialog)
        PasswordsDialog.setTabOrder(self.searchEdit, self.passwordsTable)
        PasswordsDialog.setTabOrder(self.passwordsTable, self.removeButton)
        PasswordsDialog.setTabOrder(self.removeButton, self.removeAllButton)
        PasswordsDialog.setTabOrder(self.removeAllButton, self.passwordsButton)
        PasswordsDialog.setTabOrder(self.passwordsButton, self.buttonBox)

    def retranslateUi(self, PasswordsDialog):
        _translate = QtCore.QCoreApplication.translate
        PasswordsDialog.setWindowTitle(_translate("PasswordsDialog", "Saved Passwords"))
        self.searchEdit.setToolTip(_translate("PasswordsDialog", "Enter search term"))
        self.removeButton.setToolTip(_translate("PasswordsDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("PasswordsDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("PasswordsDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("PasswordsDialog", "Remove &All"))
        self.passwordsButton.setToolTip(_translate("PasswordsDialog", "Press to toggle the display of passwords"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TableView import E5TableView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordsDialog = QtWidgets.QDialog()
    ui = Ui_PasswordsDialog()
    ui.setupUi(PasswordsDialog)
    PasswordsDialog.show()
    sys.exit(app.exec_())

