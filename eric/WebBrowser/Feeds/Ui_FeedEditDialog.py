# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Feeds\FeedEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FeedEditDialog(object):
    def setupUi(self, FeedEditDialog):
        FeedEditDialog.setObjectName("FeedEditDialog")
        FeedEditDialog.resize(475, 114)
        FeedEditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FeedEditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(FeedEditDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(FeedEditDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.titleEdit = QtWidgets.QLineEdit(FeedEditDialog)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(FeedEditDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.urlEdit = QtWidgets.QLineEdit(FeedEditDialog)
        self.urlEdit.setObjectName("urlEdit")
        self.gridLayout.addWidget(self.urlEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(FeedEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FeedEditDialog)
        self.buttonBox.accepted.connect(FeedEditDialog.accept)
        self.buttonBox.rejected.connect(FeedEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FeedEditDialog)
        FeedEditDialog.setTabOrder(self.titleEdit, self.urlEdit)
        FeedEditDialog.setTabOrder(self.urlEdit, self.buttonBox)

    def retranslateUi(self, FeedEditDialog):
        _translate = QtCore.QCoreApplication.translate
        FeedEditDialog.setWindowTitle(_translate("FeedEditDialog", "Edit Feed Data"))
        self.label.setText(_translate("FeedEditDialog", "Fill title and URL of a feed:"))
        self.label_2.setText(_translate("FeedEditDialog", "Feed title:"))
        self.titleEdit.setToolTip(_translate("FeedEditDialog", "Enter the title of the feed"))
        self.label_3.setText(_translate("FeedEditDialog", "Feed URL:"))
        self.urlEdit.setToolTip(_translate("FeedEditDialog", "Enter the URL of the feed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FeedEditDialog = QtWidgets.QDialog()
    ui = Ui_FeedEditDialog()
    ui.setupUi(FeedEditDialog)
    FeedEditDialog.show()
    sys.exit(app.exec_())

