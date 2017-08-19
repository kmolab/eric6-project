# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgSummaryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgSummaryDialog(object):
    def setupUi(self, HgSummaryDialog):
        HgSummaryDialog.setObjectName("HgSummaryDialog")
        HgSummaryDialog.resize(600, 500)
        HgSummaryDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgSummaryDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summary = QtWidgets.QTextEdit(HgSummaryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.summary.sizePolicy().hasHeightForWidth())
        self.summary.setSizePolicy(sizePolicy)
        self.summary.setReadOnly(True)
        self.summary.setObjectName("summary")
        self.verticalLayout.addWidget(self.summary)
        self.errorGroup = QtWidgets.QGroupBox(HgSummaryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errors.sizePolicy().hasHeightForWidth())
        self.errors.setSizePolicy(sizePolicy)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout.addWidget(self.errors)
        self.verticalLayout.addWidget(self.errorGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgSummaryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgSummaryDialog)
        self.buttonBox.accepted.connect(HgSummaryDialog.accept)
        self.buttonBox.rejected.connect(HgSummaryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgSummaryDialog)
        HgSummaryDialog.setTabOrder(self.summary, self.errors)
        HgSummaryDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, HgSummaryDialog):
        _translate = QtCore.QCoreApplication.translate
        HgSummaryDialog.setWindowTitle(_translate("HgSummaryDialog", "Summary Information"))
        self.errorGroup.setTitle(_translate("HgSummaryDialog", "Errors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgSummaryDialog = QtWidgets.QDialog()
    ui = Ui_HgSummaryDialog()
    ui.setupUi(HgSummaryDialog)
    HgSummaryDialog.show()
    sys.exit(app.exec_())

