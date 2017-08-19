# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Tools\WebIconDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebIconDialog(object):
    def setupUi(self, WebIconDialog):
        WebIconDialog.setObjectName("WebIconDialog")
        WebIconDialog.resize(550, 600)
        WebIconDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(WebIconDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.iconsList = QtWidgets.QListWidget(WebIconDialog)
        self.iconsList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.iconsList.setAlternatingRowColors(True)
        self.iconsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.iconsList.setIconSize(QtCore.QSize(22, 22))
        self.iconsList.setObjectName("iconsList")
        self.gridLayout.addWidget(self.iconsList, 0, 0, 3, 1)
        self.removeButton = QtWidgets.QPushButton(WebIconDialog)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 0, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(WebIconDialog)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(WebIconDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(WebIconDialog)
        self.buttonBox.accepted.connect(WebIconDialog.accept)
        self.buttonBox.rejected.connect(WebIconDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WebIconDialog)

    def retranslateUi(self, WebIconDialog):
        _translate = QtCore.QCoreApplication.translate
        WebIconDialog.setWindowTitle(_translate("WebIconDialog", "Favicons"))
        self.iconsList.setSortingEnabled(True)
        self.removeButton.setToolTip(_translate("WebIconDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("WebIconDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("WebIconDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("WebIconDialog", "Remove &All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WebIconDialog = QtWidgets.QDialog()
    ui = Ui_WebIconDialog()
    ui.setupUi(WebIconDialog)
    WebIconDialog.show()
    sys.exit(app.exec_())

