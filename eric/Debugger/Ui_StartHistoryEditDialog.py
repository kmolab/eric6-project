# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Debugger\StartHistoryEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartHistoryEditDialog(object):
    def setupUi(self, StartHistoryEditDialog):
        StartHistoryEditDialog.setObjectName("StartHistoryEditDialog")
        StartHistoryEditDialog.resize(600, 400)
        StartHistoryEditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(StartHistoryEditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.historyList = QtWidgets.QListWidget(StartHistoryEditDialog)
        self.historyList.setAlternatingRowColors(True)
        self.historyList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.historyList.setObjectName("historyList")
        self.gridLayout.addWidget(self.historyList, 0, 0, 5, 1)
        self.editButton = QtWidgets.QPushButton(StartHistoryEditDialog)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(StartHistoryEditDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(StartHistoryEditDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 2, 1, 1, 1)
        self.deleteAllButton = QtWidgets.QPushButton(StartHistoryEditDialog)
        self.deleteAllButton.setObjectName("deleteAllButton")
        self.gridLayout.addWidget(self.deleteAllButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(StartHistoryEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(StartHistoryEditDialog)
        self.buttonBox.accepted.connect(StartHistoryEditDialog.accept)
        self.buttonBox.rejected.connect(StartHistoryEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(StartHistoryEditDialog)

    def retranslateUi(self, StartHistoryEditDialog):
        _translate = QtCore.QCoreApplication.translate
        StartHistoryEditDialog.setWindowTitle(_translate("StartHistoryEditDialog", "Edit History"))
        self.editButton.setToolTip(_translate("StartHistoryEditDialog", "Press to edit the selected entry"))
        self.editButton.setText(_translate("StartHistoryEditDialog", "Edit..."))
        self.deleteButton.setToolTip(_translate("StartHistoryEditDialog", "Press to delete the selected entries"))
        self.deleteButton.setText(_translate("StartHistoryEditDialog", "Delete Selected"))
        self.deleteAllButton.setToolTip(_translate("StartHistoryEditDialog", "Press to delete all entries"))
        self.deleteAllButton.setText(_translate("StartHistoryEditDialog", "Delete All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartHistoryEditDialog = QtWidgets.QDialog()
    ui = Ui_StartHistoryEditDialog()
    ui.setupUi(StartHistoryEditDialog)
    StartHistoryEditDialog.show()
    sys.exit(app.exec_())

