# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgCommandDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgCommandDialog(object):
    def setupUi(self, HgCommandDialog):
        HgCommandDialog.setObjectName("HgCommandDialog")
        HgCommandDialog.resize(628, 99)
        HgCommandDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgCommandDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(HgCommandDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.commandCombo = QtWidgets.QComboBox(HgCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandCombo.sizePolicy().hasHeightForWidth())
        self.commandCombo.setSizePolicy(sizePolicy)
        self.commandCombo.setEditable(True)
        self.commandCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.commandCombo.setDuplicatesEnabled(False)
        self.commandCombo.setObjectName("commandCombo")
        self.gridLayout.addWidget(self.commandCombo, 0, 1, 1, 1)
        self.textLabel3 = QtWidgets.QLabel(HgCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textLabel3.sizePolicy().hasHeightForWidth())
        self.textLabel3.setSizePolicy(sizePolicy)
        self.textLabel3.setObjectName("textLabel3")
        self.gridLayout.addWidget(self.textLabel3, 1, 0, 1, 1)
        self.projectDirLabel = QtWidgets.QLabel(HgCommandDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectDirLabel.sizePolicy().hasHeightForWidth())
        self.projectDirLabel.setSizePolicy(sizePolicy)
        self.projectDirLabel.setObjectName("projectDirLabel")
        self.gridLayout.addWidget(self.projectDirLabel, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgCommandDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(HgCommandDialog)
        self.buttonBox.accepted.connect(HgCommandDialog.accept)
        self.buttonBox.rejected.connect(HgCommandDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgCommandDialog)
        HgCommandDialog.setTabOrder(self.commandCombo, self.buttonBox)

    def retranslateUi(self, HgCommandDialog):
        _translate = QtCore.QCoreApplication.translate
        HgCommandDialog.setWindowTitle(_translate("HgCommandDialog", "Mercurial Command"))
        self.textLabel1.setText(_translate("HgCommandDialog", "Mercurial Command:"))
        self.commandCombo.setToolTip(_translate("HgCommandDialog", "Enter the Mercurial command to be executed with all necessary parameters"))
        self.commandCombo.setWhatsThis(_translate("HgCommandDialog", "<b>Mercurial Command</b>\n"
"<p>Enter the Mercurial command to be executed including all necessary \n"
"parameters. If a parameter of the commandline includes a space you have to \n"
"surround this parameter by single or double quotes. Do not include the name \n"
"of the Mercurial client executable (i.e. hg).</p>"))
        self.textLabel3.setText(_translate("HgCommandDialog", "Project Directory:"))
        self.projectDirLabel.setToolTip(_translate("HgCommandDialog", "This shows the root directory of the current project."))
        self.projectDirLabel.setText(_translate("HgCommandDialog", "project directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgCommandDialog = QtWidgets.QDialog()
    ui = Ui_HgCommandDialog()
    ui.setupUi(HgCommandDialog)
    HgCommandDialog.show()
    sys.exit(app.exec_())

