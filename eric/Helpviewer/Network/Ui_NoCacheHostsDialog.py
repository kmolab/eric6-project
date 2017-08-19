# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\Network\NoCacheHostsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NoCacheHostsDialog(object):
    def setupUi(self, NoCacheHostsDialog):
        NoCacheHostsDialog.setObjectName("NoCacheHostsDialog")
        NoCacheHostsDialog.resize(500, 350)
        NoCacheHostsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(NoCacheHostsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.searchEdit = E5ClearableLineEdit(NoCacheHostsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout_2.addWidget(self.searchEdit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(NoCacheHostsDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(NoCacheHostsDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(NoCacheHostsDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(NoCacheHostsDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 3, 1, 1, 1)
        self.noCacheList = E5ListView(NoCacheHostsDialog)
        self.noCacheList.setAlternatingRowColors(True)
        self.noCacheList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.noCacheList.setObjectName("noCacheList")
        self.gridLayout.addWidget(self.noCacheList, 0, 0, 5, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NoCacheHostsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NoCacheHostsDialog)
        self.buttonBox.accepted.connect(NoCacheHostsDialog.accept)
        self.buttonBox.rejected.connect(NoCacheHostsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NoCacheHostsDialog)
        NoCacheHostsDialog.setTabOrder(self.searchEdit, self.noCacheList)
        NoCacheHostsDialog.setTabOrder(self.noCacheList, self.addButton)
        NoCacheHostsDialog.setTabOrder(self.addButton, self.removeButton)
        NoCacheHostsDialog.setTabOrder(self.removeButton, self.removeAllButton)
        NoCacheHostsDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, NoCacheHostsDialog):
        _translate = QtCore.QCoreApplication.translate
        NoCacheHostsDialog.setWindowTitle(_translate("NoCacheHostsDialog", "Not Cached Hosts"))
        self.searchEdit.setToolTip(_translate("NoCacheHostsDialog", "Enter search term for hosts"))
        self.addButton.setToolTip(_translate("NoCacheHostsDialog", "Press to add site to the list"))
        self.addButton.setText(_translate("NoCacheHostsDialog", "&Add..."))
        self.removeButton.setToolTip(_translate("NoCacheHostsDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("NoCacheHostsDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("NoCacheHostsDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("NoCacheHostsDialog", "R&emove All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5ListView import E5ListView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoCacheHostsDialog = QtWidgets.QDialog()
    ui = Ui_NoCacheHostsDialog()
    ui.setupUi(NoCacheHostsDialog)
    NoCacheHostsDialog.show()
    sys.exit(app.exec_())

