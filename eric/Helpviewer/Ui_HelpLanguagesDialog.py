# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\HelpLanguagesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpLanguagesDialog(object):
    def setupUi(self, HelpLanguagesDialog):
        HelpLanguagesDialog.setObjectName("HelpLanguagesDialog")
        HelpLanguagesDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(HelpLanguagesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HelpLanguagesDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.languagesList = QtWidgets.QListView(HelpLanguagesDialog)
        self.languagesList.setObjectName("languagesList")
        self.gridLayout.addWidget(self.languagesList, 1, 0, 4, 1)
        self.upButton = QtWidgets.QPushButton(HelpLanguagesDialog)
        self.upButton.setObjectName("upButton")
        self.gridLayout.addWidget(self.upButton, 1, 1, 1, 1)
        self.downButton = QtWidgets.QPushButton(HelpLanguagesDialog)
        self.downButton.setObjectName("downButton")
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(HelpLanguagesDialog)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 77, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.addCombo = QtWidgets.QComboBox(HelpLanguagesDialog)
        self.addCombo.setObjectName("addCombo")
        self.gridLayout.addWidget(self.addCombo, 5, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(HelpLanguagesDialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HelpLanguagesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)

        self.retranslateUi(HelpLanguagesDialog)
        self.buttonBox.accepted.connect(HelpLanguagesDialog.accept)
        self.buttonBox.rejected.connect(HelpLanguagesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HelpLanguagesDialog)
        HelpLanguagesDialog.setTabOrder(self.languagesList, self.upButton)
        HelpLanguagesDialog.setTabOrder(self.upButton, self.downButton)
        HelpLanguagesDialog.setTabOrder(self.downButton, self.removeButton)
        HelpLanguagesDialog.setTabOrder(self.removeButton, self.addCombo)
        HelpLanguagesDialog.setTabOrder(self.addCombo, self.addButton)
        HelpLanguagesDialog.setTabOrder(self.addButton, self.buttonBox)

    def retranslateUi(self, HelpLanguagesDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpLanguagesDialog.setWindowTitle(_translate("HelpLanguagesDialog", "Languages"))
        self.label.setText(_translate("HelpLanguagesDialog", "Languages in order of preference:"))
        self.upButton.setText(_translate("HelpLanguagesDialog", "&Up"))
        self.downButton.setText(_translate("HelpLanguagesDialog", "&Down"))
        self.removeButton.setText(_translate("HelpLanguagesDialog", "&Remove"))
        self.addButton.setText(_translate("HelpLanguagesDialog", "&Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpLanguagesDialog = QtWidgets.QDialog()
    ui = Ui_HelpLanguagesDialog()
    ui.setupUi(HelpLanguagesDialog)
    HelpLanguagesDialog.show()
    sys.exit(app.exec_())

