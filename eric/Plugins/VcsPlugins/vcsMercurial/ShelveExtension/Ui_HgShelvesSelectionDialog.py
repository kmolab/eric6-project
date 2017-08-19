# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\ShelveExtension\HgShelvesSelectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgShelvesSelectionDialog(object):
    def setupUi(self, HgShelvesSelectionDialog):
        HgShelvesSelectionDialog.setObjectName("HgShelvesSelectionDialog")
        HgShelvesSelectionDialog.resize(400, 300)
        HgShelvesSelectionDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgShelvesSelectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message = QtWidgets.QLabel(HgShelvesSelectionDialog)
        self.message.setText("")
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.shelvesList = QtWidgets.QListWidget(HgShelvesSelectionDialog)
        self.shelvesList.setAlternatingRowColors(True)
        self.shelvesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.shelvesList.setObjectName("shelvesList")
        self.verticalLayout.addWidget(self.shelvesList)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgShelvesSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgShelvesSelectionDialog)
        self.buttonBox.accepted.connect(HgShelvesSelectionDialog.accept)
        self.buttonBox.rejected.connect(HgShelvesSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgShelvesSelectionDialog)
        HgShelvesSelectionDialog.setTabOrder(self.shelvesList, self.buttonBox)

    def retranslateUi(self, HgShelvesSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        HgShelvesSelectionDialog.setWindowTitle(_translate("HgShelvesSelectionDialog", "Mercurial Shelve Selection"))
        self.shelvesList.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgShelvesSelectionDialog = QtWidgets.QDialog()
    ui = Ui_HgShelvesSelectionDialog()
    ui.setupUi(HgShelvesSelectionDialog)
    HgShelvesSelectionDialog.show()
    sys.exit(app.exec_())

