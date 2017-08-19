# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\ShelveExtension\HgUnshelveDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgUnshelveDataDialog(object):
    def setupUi(self, HgUnshelveDataDialog):
        HgUnshelveDataDialog.setObjectName("HgUnshelveDataDialog")
        HgUnshelveDataDialog.resize(400, 108)
        HgUnshelveDataDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgUnshelveDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgUnshelveDataDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameComboBox = QtWidgets.QComboBox(HgUnshelveDataDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameComboBox.sizePolicy().hasHeightForWidth())
        self.nameComboBox.setSizePolicy(sizePolicy)
        self.nameComboBox.setEditable(True)
        self.nameComboBox.setObjectName("nameComboBox")
        self.gridLayout.addWidget(self.nameComboBox, 0, 1, 1, 1)
        self.keepCheckBox = QtWidgets.QCheckBox(HgUnshelveDataDialog)
        self.keepCheckBox.setObjectName("keepCheckBox")
        self.gridLayout.addWidget(self.keepCheckBox, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgUnshelveDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(HgUnshelveDataDialog)
        self.buttonBox.accepted.connect(HgUnshelveDataDialog.accept)
        self.buttonBox.rejected.connect(HgUnshelveDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgUnshelveDataDialog)
        HgUnshelveDataDialog.setTabOrder(self.nameComboBox, self.keepCheckBox)
        HgUnshelveDataDialog.setTabOrder(self.keepCheckBox, self.buttonBox)

    def retranslateUi(self, HgUnshelveDataDialog):
        _translate = QtCore.QCoreApplication.translate
        HgUnshelveDataDialog.setWindowTitle(_translate("HgUnshelveDataDialog", "Mercurial Unshelve"))
        self.label.setText(_translate("HgUnshelveDataDialog", "Name:"))
        self.nameComboBox.setToolTip(_translate("HgUnshelveDataDialog", "Enter the name of the shelve"))
        self.keepCheckBox.setToolTip(_translate("HgUnshelveDataDialog", "Select to keep the shelved change"))
        self.keepCheckBox.setText(_translate("HgUnshelveDataDialog", "Keep shelved change"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgUnshelveDataDialog = QtWidgets.QDialog()
    ui = Ui_HgUnshelveDataDialog()
    ui.setupUi(HgUnshelveDataDialog)
    HgUnshelveDataDialog.show()
    sys.exit(app.exec_())

