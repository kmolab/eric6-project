# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\History\HistoryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistoryDialog(object):
    def setupUi(self, HistoryDialog):
        HistoryDialog.setObjectName("HistoryDialog")
        HistoryDialog.resize(750, 450)
        HistoryDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HistoryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(HistoryDialog)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.historyTree = E5TreeView(HistoryDialog)
        self.historyTree.setAlternatingRowColors(True)
        self.historyTree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.historyTree.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.historyTree.setUniformRowHeights(True)
        self.historyTree.setObjectName("historyTree")
        self.verticalLayout.addWidget(self.historyTree)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.removeButton = QtWidgets.QPushButton(HistoryDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtWidgets.QPushButton(HistoryDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.horizontalLayout_3.addWidget(self.removeAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(HistoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HistoryDialog)
        self.buttonBox.accepted.connect(HistoryDialog.accept)
        self.buttonBox.rejected.connect(HistoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HistoryDialog)
        HistoryDialog.setTabOrder(self.searchEdit, self.historyTree)
        HistoryDialog.setTabOrder(self.historyTree, self.removeButton)
        HistoryDialog.setTabOrder(self.removeButton, self.removeAllButton)
        HistoryDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, HistoryDialog):
        _translate = QtCore.QCoreApplication.translate
        HistoryDialog.setWindowTitle(_translate("HistoryDialog", "Manage History"))
        self.searchEdit.setToolTip(_translate("HistoryDialog", "Enter search term for history entries"))
        self.removeButton.setToolTip(_translate("HistoryDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("HistoryDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("HistoryDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("HistoryDialog", "Remove &All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TreeView import E5TreeView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HistoryDialog = QtWidgets.QDialog()
    ui = Ui_HistoryDialog()
    ui.setupUi(HistoryDialog)
    HistoryDialog.show()
    sys.exit(app.exec_())

