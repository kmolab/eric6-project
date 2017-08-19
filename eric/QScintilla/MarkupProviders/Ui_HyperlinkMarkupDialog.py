# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\QScintilla\MarkupProviders\HyperlinkMarkupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HyperlinkMarkupDialog(object):
    def setupUi(self, HyperlinkMarkupDialog):
        HyperlinkMarkupDialog.setObjectName("HyperlinkMarkupDialog")
        HyperlinkMarkupDialog.resize(400, 142)
        HyperlinkMarkupDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HyperlinkMarkupDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HyperlinkMarkupDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QLineEdit(HyperlinkMarkupDialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(HyperlinkMarkupDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.targetEdit = QtWidgets.QLineEdit(HyperlinkMarkupDialog)
        self.targetEdit.setObjectName("targetEdit")
        self.gridLayout.addWidget(self.targetEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HyperlinkMarkupDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.titelEdit = QtWidgets.QLineEdit(HyperlinkMarkupDialog)
        self.titelEdit.setObjectName("titelEdit")
        self.gridLayout.addWidget(self.titelEdit, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HyperlinkMarkupDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(HyperlinkMarkupDialog)
        self.buttonBox.accepted.connect(HyperlinkMarkupDialog.accept)
        self.buttonBox.rejected.connect(HyperlinkMarkupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HyperlinkMarkupDialog)

    def retranslateUi(self, HyperlinkMarkupDialog):
        _translate = QtCore.QCoreApplication.translate
        HyperlinkMarkupDialog.setWindowTitle(_translate("HyperlinkMarkupDialog", "Insert Hyperlink"))
        self.label.setText(_translate("HyperlinkMarkupDialog", "Link Text:"))
        self.label_2.setText(_translate("HyperlinkMarkupDialog", "Link Target:"))
        self.label_3.setText(_translate("HyperlinkMarkupDialog", "Link Title:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HyperlinkMarkupDialog = QtWidgets.QDialog()
    ui = Ui_HyperlinkMarkupDialog()
    ui.setupUi(HyperlinkMarkupDialog)
    HyperlinkMarkupDialog.show()
    sys.exit(app.exec_())

