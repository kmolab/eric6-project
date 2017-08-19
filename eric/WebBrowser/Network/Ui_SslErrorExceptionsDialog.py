# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Network\SslErrorExceptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SslErrorExceptionsDialog(object):
    def setupUi(self, SslErrorExceptionsDialog):
        SslErrorExceptionsDialog.setObjectName("SslErrorExceptionsDialog")
        SslErrorExceptionsDialog.resize(751, 513)
        SslErrorExceptionsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SslErrorExceptionsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.errorsTree = QtWidgets.QTreeWidget(SslErrorExceptionsDialog)
        self.errorsTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.errorsTree.setAlternatingRowColors(True)
        self.errorsTree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.errorsTree.setAllColumnsShowFocus(True)
        self.errorsTree.setObjectName("errorsTree")
        self.gridLayout.addWidget(self.errorsTree, 0, 0, 3, 1)
        self.removeButton = QtWidgets.QPushButton(SslErrorExceptionsDialog)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 0, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(SslErrorExceptionsDialog)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 128, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SslErrorExceptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SslErrorExceptionsDialog)
        self.buttonBox.accepted.connect(SslErrorExceptionsDialog.accept)
        self.buttonBox.rejected.connect(SslErrorExceptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SslErrorExceptionsDialog)

    def retranslateUi(self, SslErrorExceptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        SslErrorExceptionsDialog.setWindowTitle(_translate("SslErrorExceptionsDialog", "SSL Error Exceptions"))
        self.errorsTree.setSortingEnabled(True)
        self.errorsTree.headerItem().setText(0, _translate("SslErrorExceptionsDialog", "Code"))
        self.errorsTree.headerItem().setText(1, _translate("SslErrorExceptionsDialog", "Error Description"))
        self.removeButton.setToolTip(_translate("SslErrorExceptionsDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("SslErrorExceptionsDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("SslErrorExceptionsDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("SslErrorExceptionsDialog", "Remove &All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SslErrorExceptionsDialog = QtWidgets.QDialog()
    ui = Ui_SslErrorExceptionsDialog()
    ui.setupUi(SslErrorExceptionsDialog)
    SslErrorExceptionsDialog.show()
    sys.exit(app.exec_())

