# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\CookieJar\CookiesExceptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CookiesExceptionsDialog(object):
    def setupUi(self, CookiesExceptionsDialog):
        CookiesExceptionsDialog.setObjectName("CookiesExceptionsDialog")
        CookiesExceptionsDialog.resize(500, 450)
        CookiesExceptionsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(CookiesExceptionsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newExceptionGroupBox = QtWidgets.QGroupBox(CookiesExceptionsDialog)
        self.newExceptionGroupBox.setObjectName("newExceptionGroupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.newExceptionGroupBox)
        self.gridlayout.setObjectName("gridlayout")
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setObjectName("_2")
        self.label = QtWidgets.QLabel(self.newExceptionGroupBox)
        self.label.setObjectName("label")
        self._2.addWidget(self.label)
        self.domainEdit = QtWidgets.QLineEdit(self.newExceptionGroupBox)
        self.domainEdit.setObjectName("domainEdit")
        self._2.addWidget(self.domainEdit)
        self.gridlayout.addLayout(self._2, 0, 0, 1, 1)
        self._3 = QtWidgets.QHBoxLayout()
        self._3.setObjectName("_3")
        spacerItem = QtWidgets.QSpacerItem(81, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._3.addItem(spacerItem)
        self.blockButton = QtWidgets.QPushButton(self.newExceptionGroupBox)
        self.blockButton.setEnabled(False)
        self.blockButton.setAutoDefault(False)
        self.blockButton.setObjectName("blockButton")
        self._3.addWidget(self.blockButton)
        self.allowForSessionButton = QtWidgets.QPushButton(self.newExceptionGroupBox)
        self.allowForSessionButton.setEnabled(False)
        self.allowForSessionButton.setAutoDefault(False)
        self.allowForSessionButton.setObjectName("allowForSessionButton")
        self._3.addWidget(self.allowForSessionButton)
        self.allowButton = QtWidgets.QPushButton(self.newExceptionGroupBox)
        self.allowButton.setEnabled(False)
        self.allowButton.setAutoDefault(False)
        self.allowButton.setObjectName("allowButton")
        self._3.addWidget(self.allowButton)
        self.gridlayout.addLayout(self._3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.newExceptionGroupBox)
        self.exceptionsGroup = QtWidgets.QGroupBox(CookiesExceptionsDialog)
        self.exceptionsGroup.setObjectName("exceptionsGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.exceptionsGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(self.exceptionsGroup)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.exceptionsTable = E5TableView(self.exceptionsGroup)
        self.exceptionsTable.setAlternatingRowColors(True)
        self.exceptionsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.exceptionsTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.exceptionsTable.setShowGrid(False)
        self.exceptionsTable.setSortingEnabled(True)
        self.exceptionsTable.setObjectName("exceptionsTable")
        self.exceptionsTable.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.exceptionsTable, 1, 0, 1, 3)
        self.removeButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 0, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(286, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.exceptionsGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(CookiesExceptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.domainEdit)

        self.retranslateUi(CookiesExceptionsDialog)
        self.buttonBox.accepted.connect(CookiesExceptionsDialog.accept)
        self.buttonBox.rejected.connect(CookiesExceptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CookiesExceptionsDialog)
        CookiesExceptionsDialog.setTabOrder(self.domainEdit, self.blockButton)
        CookiesExceptionsDialog.setTabOrder(self.blockButton, self.allowForSessionButton)
        CookiesExceptionsDialog.setTabOrder(self.allowForSessionButton, self.allowButton)
        CookiesExceptionsDialog.setTabOrder(self.allowButton, self.searchEdit)
        CookiesExceptionsDialog.setTabOrder(self.searchEdit, self.exceptionsTable)
        CookiesExceptionsDialog.setTabOrder(self.exceptionsTable, self.removeButton)
        CookiesExceptionsDialog.setTabOrder(self.removeButton, self.removeAllButton)
        CookiesExceptionsDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, CookiesExceptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        CookiesExceptionsDialog.setWindowTitle(_translate("CookiesExceptionsDialog", "Cookie Exceptions"))
        self.newExceptionGroupBox.setTitle(_translate("CookiesExceptionsDialog", "New Exception"))
        self.label.setText(_translate("CookiesExceptionsDialog", "&Domain:"))
        self.domainEdit.setToolTip(_translate("CookiesExceptionsDialog", "Enter the domain name"))
        self.blockButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to always reject cookies for the domain"))
        self.blockButton.setText(_translate("CookiesExceptionsDialog", "&Block"))
        self.allowForSessionButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to accept cookies for the domain for the current session"))
        self.allowForSessionButton.setText(_translate("CookiesExceptionsDialog", "Allow For &Session"))
        self.allowButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to always accept cookies for the domain"))
        self.allowButton.setText(_translate("CookiesExceptionsDialog", "Allo&w"))
        self.exceptionsGroup.setTitle(_translate("CookiesExceptionsDialog", "Exceptions"))
        self.searchEdit.setToolTip(_translate("CookiesExceptionsDialog", "Enter search term for exceptions"))
        self.removeButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("CookiesExceptionsDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("CookiesExceptionsDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("CookiesExceptionsDialog", "Remove &All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TableView import E5TableView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CookiesExceptionsDialog = QtWidgets.QDialog()
    ui = Ui_CookiesExceptionsDialog()
    ui.setupUi(CookiesExceptionsDialog)
    CookiesExceptionsDialog.show()
    sys.exit(app.exec_())
