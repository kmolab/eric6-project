# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\VCS\RepositoryInfoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VcsRepositoryInfoDialog(object):
    def setupUi(self, VcsRepositoryInfoDialog):
        VcsRepositoryInfoDialog.setObjectName("VcsRepositoryInfoDialog")
        VcsRepositoryInfoDialog.resize(590, 437)
        VcsRepositoryInfoDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(VcsRepositoryInfoDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.infoBrowser = QtWidgets.QTextEdit(VcsRepositoryInfoDialog)
        self.infoBrowser.setReadOnly(True)
        self.infoBrowser.setObjectName("infoBrowser")
        self.vboxlayout.addWidget(self.infoBrowser)
        self.buttonBox = QtWidgets.QDialogButtonBox(VcsRepositoryInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(VcsRepositoryInfoDialog)
        self.buttonBox.accepted.connect(VcsRepositoryInfoDialog.accept)
        self.buttonBox.rejected.connect(VcsRepositoryInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VcsRepositoryInfoDialog)

    def retranslateUi(self, VcsRepositoryInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        VcsRepositoryInfoDialog.setWindowTitle(_translate("VcsRepositoryInfoDialog", "Repository Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VcsRepositoryInfoDialog = QtWidgets.QDialog()
    ui = Ui_VcsRepositoryInfoDialog()
    ui.setupUi(VcsRepositoryInfoDialog)
    VcsRepositoryInfoDialog.show()
    sys.exit(app.exec_())

