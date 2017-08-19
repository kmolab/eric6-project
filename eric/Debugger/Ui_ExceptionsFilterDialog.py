# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Debugger\ExceptionsFilterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExceptionsFilterDialog(object):
    def setupUi(self, ExceptionsFilterDialog):
        ExceptionsFilterDialog.setObjectName("ExceptionsFilterDialog")
        ExceptionsFilterDialog.resize(450, 400)
        ExceptionsFilterDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(ExceptionsFilterDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.exceptionList = QtWidgets.QListWidget(ExceptionsFilterDialog)
        self.exceptionList.setAlternatingRowColors(True)
        self.exceptionList.setObjectName("exceptionList")
        self.gridLayout.addWidget(self.exceptionList, 0, 0, 1, 3)
        self.addButton = QtWidgets.QPushButton(ExceptionsFilterDialog)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 1, 0, 1, 1)
        self.exceptionEdit = QtWidgets.QLineEdit(ExceptionsFilterDialog)
        self.exceptionEdit.setObjectName("exceptionEdit")
        self.gridLayout.addWidget(self.exceptionEdit, 1, 1, 1, 2)
        self.deleteButton = QtWidgets.QPushButton(ExceptionsFilterDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 2, 0, 1, 1)
        self.deleteAllButton = QtWidgets.QPushButton(ExceptionsFilterDialog)
        self.deleteAllButton.setObjectName("deleteAllButton")
        self.gridLayout.addWidget(self.deleteAllButton, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(261, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ExceptionsFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)

        self.retranslateUi(ExceptionsFilterDialog)
        self.buttonBox.accepted.connect(ExceptionsFilterDialog.accept)
        self.buttonBox.rejected.connect(ExceptionsFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExceptionsFilterDialog)
        ExceptionsFilterDialog.setTabOrder(self.exceptionList, self.exceptionEdit)
        ExceptionsFilterDialog.setTabOrder(self.exceptionEdit, self.addButton)
        ExceptionsFilterDialog.setTabOrder(self.addButton, self.deleteButton)
        ExceptionsFilterDialog.setTabOrder(self.deleteButton, self.deleteAllButton)
        ExceptionsFilterDialog.setTabOrder(self.deleteAllButton, self.buttonBox)

    def retranslateUi(self, ExceptionsFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        ExceptionsFilterDialog.setWindowTitle(_translate("ExceptionsFilterDialog", "Exceptions Filter"))
        ExceptionsFilterDialog.setWhatsThis(_translate("ExceptionsFilterDialog", "<b>Exception Filter</b>\n"
"<p>This dialog is used to enter the exception types, that shall be highlighted during a debugging session. If this list is empty, all exception types will be highlighted. If the exception reporting flag in the \"Start Debugging\" dialog is unchecked, no exception will be reported at all.</p>\n"
"<p>Please note, that unhandled exceptions are always highlighted independent of these settings.</p>"))
        self.exceptionList.setToolTip(_translate("ExceptionsFilterDialog", "List of exceptions that shall be highlighted"))
        self.addButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to add the entered exception to the list"))
        self.addButton.setText(_translate("ExceptionsFilterDialog", "Add"))
        self.exceptionEdit.setToolTip(_translate("ExceptionsFilterDialog", "Enter an exception type that shall be highlighted"))
        self.deleteButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to delete the selected exception from the list"))
        self.deleteButton.setText(_translate("ExceptionsFilterDialog", "Delete"))
        self.deleteAllButton.setToolTip(_translate("ExceptionsFilterDialog", "Press to delete all exceptions from the list"))
        self.deleteAllButton.setText(_translate("ExceptionsFilterDialog", "Delete All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExceptionsFilterDialog = QtWidgets.QDialog()
    ui = Ui_ExceptionsFilterDialog()
    ui.setupUi(ExceptionsFilterDialog)
    ExceptionsFilterDialog.show()
    sys.exit(app.exec_())

