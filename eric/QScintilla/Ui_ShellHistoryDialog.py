# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\QScintilla\ShellHistoryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShellHistoryDialog(object):
    def setupUi(self, ShellHistoryDialog):
        ShellHistoryDialog.setObjectName("ShellHistoryDialog")
        ShellHistoryDialog.resize(540, 506)
        ShellHistoryDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(ShellHistoryDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.historyList = QtWidgets.QListWidget(ShellHistoryDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.historyList.setFont(font)
        self.historyList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.historyList.setAlternatingRowColors(True)
        self.historyList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.historyList.setWordWrap(True)
        self.historyList.setObjectName("historyList")
        self.gridLayout.addWidget(self.historyList, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.deleteButton = QtWidgets.QPushButton(ShellHistoryDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.copyButton = QtWidgets.QPushButton(ShellHistoryDialog)
        self.copyButton.setEnabled(False)
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout.addWidget(self.copyButton)
        self.executeButton = QtWidgets.QPushButton(ShellHistoryDialog)
        self.executeButton.setEnabled(False)
        self.executeButton.setObjectName("executeButton")
        self.verticalLayout.addWidget(self.executeButton)
        self.reloadButton = QtWidgets.QPushButton(ShellHistoryDialog)
        self.reloadButton.setObjectName("reloadButton")
        self.verticalLayout.addWidget(self.reloadButton)
        spacerItem = QtWidgets.QSpacerItem(72, 208, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ShellHistoryDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(ShellHistoryDialog)
        self.buttonBox.accepted.connect(ShellHistoryDialog.accept)
        self.buttonBox.rejected.connect(ShellHistoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShellHistoryDialog)
        ShellHistoryDialog.setTabOrder(self.historyList, self.deleteButton)
        ShellHistoryDialog.setTabOrder(self.deleteButton, self.copyButton)
        ShellHistoryDialog.setTabOrder(self.copyButton, self.executeButton)
        ShellHistoryDialog.setTabOrder(self.executeButton, self.reloadButton)
        ShellHistoryDialog.setTabOrder(self.reloadButton, self.buttonBox)

    def retranslateUi(self, ShellHistoryDialog):
        _translate = QtCore.QCoreApplication.translate
        ShellHistoryDialog.setWindowTitle(_translate("ShellHistoryDialog", "Shell History"))
        self.deleteButton.setToolTip(_translate("ShellHistoryDialog", "Delete the selected entries"))
        self.deleteButton.setText(_translate("ShellHistoryDialog", "&Delete"))
        self.copyButton.setToolTip(_translate("ShellHistoryDialog", "Copy the selected entries to the current editor"))
        self.copyButton.setText(_translate("ShellHistoryDialog", "C&opy"))
        self.executeButton.setToolTip(_translate("ShellHistoryDialog", "Execute the selected entries"))
        self.executeButton.setText(_translate("ShellHistoryDialog", "&Execute"))
        self.reloadButton.setToolTip(_translate("ShellHistoryDialog", "Reload the history"))
        self.reloadButton.setText(_translate("ShellHistoryDialog", "&Reload"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShellHistoryDialog = QtWidgets.QDialog()
    ui = Ui_ShellHistoryDialog()
    ui.setupUi(ShellHistoryDialog)
    ShellHistoryDialog.show()
    sys.exit(app.exec_())

