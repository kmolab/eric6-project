# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgUserConfigHostMinimumProtocolDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgUserConfigHostMinimumProtocolDialog(object):
    def setupUi(self, HgUserConfigHostMinimumProtocolDialog):
        HgUserConfigHostMinimumProtocolDialog.setObjectName("HgUserConfigHostMinimumProtocolDialog")
        HgUserConfigHostMinimumProtocolDialog.resize(450, 95)
        HgUserConfigHostMinimumProtocolDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgUserConfigHostMinimumProtocolDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgUserConfigHostMinimumProtocolDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.hostEdit = E5ClearableLineEdit(HgUserConfigHostMinimumProtocolDialog)
        self.hostEdit.setObjectName("hostEdit")
        self.gridLayout.addWidget(self.hostEdit, 0, 1, 1, 1)
        self.hashLabel = QtWidgets.QLabel(HgUserConfigHostMinimumProtocolDialog)
        self.hashLabel.setObjectName("hashLabel")
        self.gridLayout.addWidget(self.hashLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimumProtocolComboBox = QtWidgets.QComboBox(HgUserConfigHostMinimumProtocolDialog)
        self.minimumProtocolComboBox.setCurrentText("")
        self.minimumProtocolComboBox.setObjectName("minimumProtocolComboBox")
        self.horizontalLayout.addWidget(self.minimumProtocolComboBox)
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgUserConfigHostMinimumProtocolDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(HgUserConfigHostMinimumProtocolDialog)
        self.buttonBox.accepted.connect(HgUserConfigHostMinimumProtocolDialog.accept)
        self.buttonBox.rejected.connect(HgUserConfigHostMinimumProtocolDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgUserConfigHostMinimumProtocolDialog)
        HgUserConfigHostMinimumProtocolDialog.setTabOrder(self.hostEdit, self.minimumProtocolComboBox)

    def retranslateUi(self, HgUserConfigHostMinimumProtocolDialog):
        _translate = QtCore.QCoreApplication.translate
        HgUserConfigHostMinimumProtocolDialog.setWindowTitle(_translate("HgUserConfigHostMinimumProtocolDialog", "Minimum Protocol"))
        self.label.setText(_translate("HgUserConfigHostMinimumProtocolDialog", "Host:"))
        self.hostEdit.setToolTip(_translate("HgUserConfigHostMinimumProtocolDialog", "Enter the host name"))
        self.hostEdit.setPlaceholderText(_translate("HgUserConfigHostMinimumProtocolDialog", "Enter Hostname"))
        self.hashLabel.setText(_translate("HgUserConfigHostMinimumProtocolDialog", "Minimum Protocol:"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgUserConfigHostMinimumProtocolDialog = QtWidgets.QDialog()
    ui = Ui_HgUserConfigHostMinimumProtocolDialog()
    ui.setupUi(HgUserConfigHostMinimumProtocolDialog)
    HgUserConfigHostMinimumProtocolDialog.show()
    sys.exit(app.exec_())

