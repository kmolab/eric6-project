# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\WebPlugins\ClickToFlash\ClickToFlashWhitelistDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClickToFlashWhitelistDialog(object):
    def setupUi(self, ClickToFlashWhitelistDialog):
        ClickToFlashWhitelistDialog.setObjectName("ClickToFlashWhitelistDialog")
        ClickToFlashWhitelistDialog.resize(500, 350)
        ClickToFlashWhitelistDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ClickToFlashWhitelistDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.iconLabel = QtWidgets.QLabel(ClickToFlashWhitelistDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setText("Icon")
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout_2.addWidget(self.iconLabel, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.searchEdit = E5ClearableLineEdit(ClickToFlashWhitelistDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout_2.addWidget(self.searchEdit, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(ClickToFlashWhitelistDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(ClickToFlashWhitelistDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(ClickToFlashWhitelistDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(ClickToFlashWhitelistDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 3, 1, 1, 1)
        self.whitelist = E5ListView(ClickToFlashWhitelistDialog)
        self.whitelist.setAlternatingRowColors(True)
        self.whitelist.setObjectName("whitelist")
        self.gridLayout.addWidget(self.whitelist, 0, 0, 5, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ClickToFlashWhitelistDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ClickToFlashWhitelistDialog)
        self.buttonBox.accepted.connect(ClickToFlashWhitelistDialog.accept)
        self.buttonBox.rejected.connect(ClickToFlashWhitelistDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ClickToFlashWhitelistDialog)
        ClickToFlashWhitelistDialog.setTabOrder(self.searchEdit, self.whitelist)
        ClickToFlashWhitelistDialog.setTabOrder(self.whitelist, self.addButton)
        ClickToFlashWhitelistDialog.setTabOrder(self.addButton, self.removeButton)
        ClickToFlashWhitelistDialog.setTabOrder(self.removeButton, self.removeAllButton)
        ClickToFlashWhitelistDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, ClickToFlashWhitelistDialog):
        _translate = QtCore.QCoreApplication.translate
        ClickToFlashWhitelistDialog.setWindowTitle(_translate("ClickToFlashWhitelistDialog", "ClickToFlash Whitelist"))
        self.searchEdit.setToolTip(_translate("ClickToFlashWhitelistDialog", "Enter search term for hosts"))
        self.addButton.setToolTip(_translate("ClickToFlashWhitelistDialog", "Press to add site to the whitelist"))
        self.addButton.setText(_translate("ClickToFlashWhitelistDialog", "&Add..."))
        self.removeButton.setToolTip(_translate("ClickToFlashWhitelistDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("ClickToFlashWhitelistDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("ClickToFlashWhitelistDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("ClickToFlashWhitelistDialog", "R&emove All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5ListView import E5ListView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClickToFlashWhitelistDialog = QtWidgets.QDialog()
    ui = Ui_ClickToFlashWhitelistDialog()
    ui.setupUi(ClickToFlashWhitelistDialog)
    ClickToFlashWhitelistDialog.show()
    sys.exit(app.exec_())

