# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\UserAgent\UserAgentsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserAgentsDialog(object):
    def setupUi(self, UserAgentsDialog):
        UserAgentsDialog.setObjectName("UserAgentsDialog")
        UserAgentsDialog.resize(700, 400)
        UserAgentsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(UserAgentsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(UserAgentsDialog)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.userAgentsTable = E5TableView(UserAgentsDialog)
        self.userAgentsTable.setAlternatingRowColors(True)
        self.userAgentsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.userAgentsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.userAgentsTable.setShowGrid(False)
        self.userAgentsTable.setSortingEnabled(True)
        self.userAgentsTable.setObjectName("userAgentsTable")
        self.verticalLayout.addWidget(self.userAgentsTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.removeButton = QtWidgets.QPushButton(UserAgentsDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtWidgets.QPushButton(UserAgentsDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.horizontalLayout_3.addWidget(self.removeAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(UserAgentsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(UserAgentsDialog)
        self.buttonBox.accepted.connect(UserAgentsDialog.accept)
        self.buttonBox.rejected.connect(UserAgentsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UserAgentsDialog)
        UserAgentsDialog.setTabOrder(self.searchEdit, self.userAgentsTable)
        UserAgentsDialog.setTabOrder(self.userAgentsTable, self.removeButton)
        UserAgentsDialog.setTabOrder(self.removeButton, self.removeAllButton)
        UserAgentsDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, UserAgentsDialog):
        _translate = QtCore.QCoreApplication.translate
        UserAgentsDialog.setWindowTitle(_translate("UserAgentsDialog", "User Agent Settings"))
        self.searchEdit.setToolTip(_translate("UserAgentsDialog", "Enter search term"))
        self.removeButton.setToolTip(_translate("UserAgentsDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("UserAgentsDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("UserAgentsDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("UserAgentsDialog", "Remove &All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TableView import E5TableView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserAgentsDialog = QtWidgets.QDialog()
    ui = Ui_UserAgentsDialog()
    ui.setupUi(UserAgentsDialog)
    UserAgentsDialog.show()
    sys.exit(app.exec_())

