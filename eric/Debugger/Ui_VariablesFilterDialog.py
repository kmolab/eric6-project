# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Debugger\VariablesFilterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VariablesFilterDialog(object):
    def setupUi(self, VariablesFilterDialog):
        VariablesFilterDialog.setObjectName("VariablesFilterDialog")
        VariablesFilterDialog.resize(400, 400)
        VariablesFilterDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(VariablesFilterDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(VariablesFilterDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.localsLabel = QtWidgets.QLabel(VariablesFilterDialog)
        self.localsLabel.setObjectName("localsLabel")
        self.gridLayout.addWidget(self.localsLabel, 1, 0, 1, 1)
        self.globalsLabel = QtWidgets.QLabel(VariablesFilterDialog)
        self.globalsLabel.setObjectName("globalsLabel")
        self.gridLayout.addWidget(self.globalsLabel, 1, 1, 1, 1)
        self.localsList = QtWidgets.QListWidget(VariablesFilterDialog)
        self.localsList.setAlternatingRowColors(True)
        self.localsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.localsList.setObjectName("localsList")
        self.gridLayout.addWidget(self.localsList, 2, 0, 1, 1)
        self.globalsList = QtWidgets.QListWidget(VariablesFilterDialog)
        self.globalsList.setAlternatingRowColors(True)
        self.globalsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.globalsList.setObjectName("globalsList")
        self.gridLayout.addWidget(self.globalsList, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(VariablesFilterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.localsLabel.setBuddy(self.localsList)
        self.globalsLabel.setBuddy(self.globalsList)

        self.retranslateUi(VariablesFilterDialog)
        self.buttonBox.accepted.connect(VariablesFilterDialog.accept)
        self.buttonBox.rejected.connect(VariablesFilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VariablesFilterDialog)
        VariablesFilterDialog.setTabOrder(self.localsList, self.globalsList)

    def retranslateUi(self, VariablesFilterDialog):
        _translate = QtCore.QCoreApplication.translate
        VariablesFilterDialog.setWindowTitle(_translate("VariablesFilterDialog", "Variables Type Filter"))
        VariablesFilterDialog.setWhatsThis(_translate("VariablesFilterDialog", "<b>Filter Dialog</b>\n"
"<p> This dialog gives the user the possibility to select what kind of variables should <b>not</b> be shown during a debugging session.</p>"))
        self.label.setText(_translate("VariablesFilterDialog", "Select the variable types to be shown in the variables viewers:"))
        self.localsLabel.setText(_translate("VariablesFilterDialog", "&Locals Viewer"))
        self.globalsLabel.setText(_translate("VariablesFilterDialog", "&Globals Viewer"))
        self.localsList.setToolTip(_translate("VariablesFilterDialog", "Locals Filter List"))
        self.localsList.setWhatsThis(_translate("VariablesFilterDialog", "<b>Locals Filter List</b>\n"
"<p>Select the variable types you want to be shown in the local variables viewer.</p<"))
        self.localsList.setSortingEnabled(True)
        self.globalsList.setToolTip(_translate("VariablesFilterDialog", "Globals Filter List"))
        self.globalsList.setWhatsThis(_translate("VariablesFilterDialog", "<b>Globals Filter List</b>\n"
"<p>Select the variable types you want to be shown in the global variables viewer.</p<"))
        self.globalsList.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VariablesFilterDialog = QtWidgets.QDialog()
    ui = Ui_VariablesFilterDialog()
    ui.setupUi(VariablesFilterDialog)
    VariablesFilterDialog.show()
    sys.exit(app.exec_())

