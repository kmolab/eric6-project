# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ProgramsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProgramsDialog(object):
    def setupUi(self, ProgramsDialog):
        ProgramsDialog.setObjectName("ProgramsDialog")
        ProgramsDialog.resize(700, 570)
        self.vboxlayout = QtWidgets.QVBoxLayout(ProgramsDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.programsList = QtWidgets.QTreeWidget(ProgramsDialog)
        self.programsList.setRootIsDecorated(False)
        self.programsList.setObjectName("programsList")
        self.vboxlayout.addWidget(self.programsList)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProgramsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ProgramsDialog)
        self.buttonBox.accepted.connect(ProgramsDialog.close)
        self.buttonBox.rejected.connect(ProgramsDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ProgramsDialog)

    def retranslateUi(self, ProgramsDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgramsDialog.setWindowTitle(_translate("ProgramsDialog", "External Programs"))
        self.programsList.setSortingEnabled(True)
        self.programsList.headerItem().setText(0, _translate("ProgramsDialog", "Path"))
        self.programsList.headerItem().setText(1, _translate("ProgramsDialog", "Version"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProgramsDialog = QtWidgets.QDialog()
    ui = Ui_ProgramsDialog()
    ui.setupUi(ProgramsDialog)
    ProgramsDialog.show()
    sys.exit(app.exec_())

