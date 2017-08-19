# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnRelocateDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnRelocateDialog(object):
    def setupUi(self, SvnRelocateDialog):
        SvnRelocateDialog.setObjectName("SvnRelocateDialog")
        SvnRelocateDialog.resize(531, 119)
        SvnRelocateDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SvnRelocateDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.currUrlLabel = QtWidgets.QLabel(SvnRelocateDialog)
        self.currUrlLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currUrlLabel.setText("")
        self.currUrlLabel.setObjectName("currUrlLabel")
        self.gridlayout.addWidget(self.currUrlLabel, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(SvnRelocateDialog)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.newUrlEdit = QtWidgets.QLineEdit(SvnRelocateDialog)
        self.newUrlEdit.setObjectName("newUrlEdit")
        self.gridlayout.addWidget(self.newUrlEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(SvnRelocateDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.insideCheckBox = QtWidgets.QCheckBox(SvnRelocateDialog)
        self.insideCheckBox.setObjectName("insideCheckBox")
        self.verticalLayout.addWidget(self.insideCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnRelocateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnRelocateDialog)
        self.buttonBox.accepted.connect(SvnRelocateDialog.accept)
        self.buttonBox.rejected.connect(SvnRelocateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnRelocateDialog)
        SvnRelocateDialog.setTabOrder(self.newUrlEdit, self.insideCheckBox)
        SvnRelocateDialog.setTabOrder(self.insideCheckBox, self.buttonBox)

    def retranslateUi(self, SvnRelocateDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnRelocateDialog.setWindowTitle(_translate("SvnRelocateDialog", "Subversion Relocate"))
        self.label_2.setText(_translate("SvnRelocateDialog", "New repository URL:"))
        self.newUrlEdit.setToolTip(_translate("SvnRelocateDialog", "Enter the URL of the repository the working space should be relocated to"))
        self.label.setText(_translate("SvnRelocateDialog", "Current repository URL:"))
        self.insideCheckBox.setToolTip(_translate("SvnRelocateDialog", "Select, if the relocate should happen inside the repository"))
        self.insideCheckBox.setText(_translate("SvnRelocateDialog", "Relocate inside repository (used, if the repository layout has changed)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnRelocateDialog = QtWidgets.QDialog()
    ui = Ui_SvnRelocateDialog()
    ui.setupUi(SvnRelocateDialog)
    SvnRelocateDialog.show()
    sys.exit(app.exec_())

