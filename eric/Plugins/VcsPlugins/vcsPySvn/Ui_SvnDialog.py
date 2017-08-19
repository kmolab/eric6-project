# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnDialog(object):
    def setupUi(self, SvnDialog):
        SvnDialog.setObjectName("SvnDialog")
        SvnDialog.resize(593, 499)
        SvnDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.outputGroup = QtWidgets.QGroupBox(SvnDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.outputGroup.sizePolicy().hasHeightForWidth())
        self.outputGroup.setSizePolicy(sizePolicy)
        self.outputGroup.setObjectName("outputGroup")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.outputGroup)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.resultbox = QtWidgets.QTextEdit(self.outputGroup)
        self.resultbox.setReadOnly(True)
        self.resultbox.setAcceptRichText(False)
        self.resultbox.setObjectName("resultbox")
        self.vboxlayout1.addWidget(self.resultbox)
        self.vboxlayout.addWidget(self.outputGroup)
        self.errorGroup = QtWidgets.QGroupBox(SvnDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout2.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnDialog)
        SvnDialog.setTabOrder(self.resultbox, self.errors)
        SvnDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnDialog.setWindowTitle(_translate("SvnDialog", "Subversion"))
        self.outputGroup.setTitle(_translate("SvnDialog", "Output"))
        self.errorGroup.setTitle(_translate("SvnDialog", "Errors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnDialog = QtWidgets.QDialog()
    ui = Ui_SvnDialog()
    ui.setupUi(SvnDialog)
    SvnDialog.show()
    sys.exit(app.exec_())

