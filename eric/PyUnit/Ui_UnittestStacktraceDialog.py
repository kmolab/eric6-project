# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\PyUnit\UnittestStacktraceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UnittestStacktraceDialog(object):
    def setupUi(self, UnittestStacktraceDialog):
        UnittestStacktraceDialog.setObjectName("UnittestStacktraceDialog")
        UnittestStacktraceDialog.resize(600, 250)
        self.vboxlayout = QtWidgets.QVBoxLayout(UnittestStacktraceDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.testLabel = QtWidgets.QLabel(UnittestStacktraceDialog)
        self.testLabel.setObjectName("testLabel")
        self.vboxlayout.addWidget(self.testLabel)
        self.traceback = QtWidgets.QTextEdit(UnittestStacktraceDialog)
        self.traceback.setReadOnly(True)
        self.traceback.setAcceptRichText(False)
        self.traceback.setObjectName("traceback")
        self.vboxlayout.addWidget(self.traceback)
        self.buttonBox = QtWidgets.QDialogButtonBox(UnittestStacktraceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(UnittestStacktraceDialog)
        self.buttonBox.accepted.connect(UnittestStacktraceDialog.accept)
        self.buttonBox.rejected.connect(UnittestStacktraceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UnittestStacktraceDialog)

    def retranslateUi(self, UnittestStacktraceDialog):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UnittestStacktraceDialog = QtWidgets.QDialog()
    ui = Ui_UnittestStacktraceDialog()
    ui.setupUi(UnittestStacktraceDialog)
    UnittestStacktraceDialog.show()
    sys.exit(app.exec_())

