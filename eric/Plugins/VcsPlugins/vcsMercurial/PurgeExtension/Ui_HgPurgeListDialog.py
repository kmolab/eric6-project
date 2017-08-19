# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\PurgeExtension\HgPurgeListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgPurgeListDialog(object):
    def setupUi(self, HgPurgeListDialog):
        HgPurgeListDialog.setObjectName("HgPurgeListDialog")
        HgPurgeListDialog.resize(500, 400)
        HgPurgeListDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgPurgeListDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.purgeList = QtWidgets.QListWidget(HgPurgeListDialog)
        self.purgeList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.purgeList.setAlternatingRowColors(True)
        self.purgeList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.purgeList.setTextElideMode(QtCore.Qt.ElideLeft)
        self.purgeList.setObjectName("purgeList")
        self.verticalLayout.addWidget(self.purgeList)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgPurgeListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgPurgeListDialog)
        self.buttonBox.accepted.connect(HgPurgeListDialog.accept)
        self.buttonBox.rejected.connect(HgPurgeListDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgPurgeListDialog)
        HgPurgeListDialog.setTabOrder(self.purgeList, self.buttonBox)

    def retranslateUi(self, HgPurgeListDialog):
        _translate = QtCore.QCoreApplication.translate
        HgPurgeListDialog.setWindowTitle(_translate("HgPurgeListDialog", "Purge List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgPurgeListDialog = QtWidgets.QDialog()
    ui = Ui_HgPurgeListDialog()
    ui.setupUi(HgPurgeListDialog)
    HgPurgeListDialog.show()
    sys.exit(app.exec_())

