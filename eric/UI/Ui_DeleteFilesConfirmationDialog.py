# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\DeleteFilesConfirmationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteFilesConfirmationDialog(object):
    def setupUi(self, DeleteFilesConfirmationDialog):
        DeleteFilesConfirmationDialog.setObjectName("DeleteFilesConfirmationDialog")
        DeleteFilesConfirmationDialog.resize(458, 288)
        DeleteFilesConfirmationDialog.setWindowTitle("")
        DeleteFilesConfirmationDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(DeleteFilesConfirmationDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.message = QtWidgets.QLabel(DeleteFilesConfirmationDialog)
        self.message.setAlignment(QtCore.Qt.AlignVCenter)
        self.message.setObjectName("message")
        self.vboxlayout.addWidget(self.message)
        self.filesList = QtWidgets.QListWidget(DeleteFilesConfirmationDialog)
        self.filesList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.filesList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.filesList.setObjectName("filesList")
        self.vboxlayout.addWidget(self.filesList)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleteFilesConfirmationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(DeleteFilesConfirmationDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteFilesConfirmationDialog)

    def retranslateUi(self, DeleteFilesConfirmationDialog):
        _translate = QtCore.QCoreApplication.translate
        self.message.setText(_translate("DeleteFilesConfirmationDialog", "Dummy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteFilesConfirmationDialog = QtWidgets.QDialog()
    ui = Ui_DeleteFilesConfirmationDialog()
    ui.setupUi(DeleteFilesConfirmationDialog)
    DeleteFilesConfirmationDialog.show()
    sys.exit(app.exec_())

