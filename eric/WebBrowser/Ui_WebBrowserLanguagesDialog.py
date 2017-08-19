# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\WebBrowserLanguagesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebBrowserLanguagesDialog(object):
    def setupUi(self, WebBrowserLanguagesDialog):
        WebBrowserLanguagesDialog.setObjectName("WebBrowserLanguagesDialog")
        WebBrowserLanguagesDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(WebBrowserLanguagesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(WebBrowserLanguagesDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.languagesList = QtWidgets.QListView(WebBrowserLanguagesDialog)
        self.languagesList.setObjectName("languagesList")
        self.gridLayout.addWidget(self.languagesList, 1, 0, 4, 1)
        self.upButton = QtWidgets.QPushButton(WebBrowserLanguagesDialog)
        self.upButton.setObjectName("upButton")
        self.gridLayout.addWidget(self.upButton, 1, 1, 1, 1)
        self.downButton = QtWidgets.QPushButton(WebBrowserLanguagesDialog)
        self.downButton.setObjectName("downButton")
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(WebBrowserLanguagesDialog)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 77, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.addCombo = QtWidgets.QComboBox(WebBrowserLanguagesDialog)
        self.addCombo.setObjectName("addCombo")
        self.gridLayout.addWidget(self.addCombo, 5, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(WebBrowserLanguagesDialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(WebBrowserLanguagesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)

        self.retranslateUi(WebBrowserLanguagesDialog)
        self.buttonBox.accepted.connect(WebBrowserLanguagesDialog.accept)
        self.buttonBox.rejected.connect(WebBrowserLanguagesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WebBrowserLanguagesDialog)
        WebBrowserLanguagesDialog.setTabOrder(self.languagesList, self.upButton)
        WebBrowserLanguagesDialog.setTabOrder(self.upButton, self.downButton)
        WebBrowserLanguagesDialog.setTabOrder(self.downButton, self.removeButton)
        WebBrowserLanguagesDialog.setTabOrder(self.removeButton, self.addCombo)
        WebBrowserLanguagesDialog.setTabOrder(self.addCombo, self.addButton)
        WebBrowserLanguagesDialog.setTabOrder(self.addButton, self.buttonBox)

    def retranslateUi(self, WebBrowserLanguagesDialog):
        _translate = QtCore.QCoreApplication.translate
        WebBrowserLanguagesDialog.setWindowTitle(_translate("WebBrowserLanguagesDialog", "Languages"))
        self.label.setText(_translate("WebBrowserLanguagesDialog", "Languages in order of preference:"))
        self.upButton.setText(_translate("WebBrowserLanguagesDialog", "&Up"))
        self.downButton.setText(_translate("WebBrowserLanguagesDialog", "&Down"))
        self.removeButton.setText(_translate("WebBrowserLanguagesDialog", "&Remove"))
        self.addButton.setText(_translate("WebBrowserLanguagesDialog", "&Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WebBrowserLanguagesDialog = QtWidgets.QDialog()
    ui = Ui_WebBrowserLanguagesDialog()
    ui.setupUi(WebBrowserLanguagesDialog)
    WebBrowserLanguagesDialog.show()
    sys.exit(app.exec_())

