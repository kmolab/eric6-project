# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\QScintilla\GotoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GotoDialog(object):
    def setupUi(self, GotoDialog):
        GotoDialog.setObjectName("GotoDialog")
        GotoDialog.resize(206, 77)
        self._3 = QtWidgets.QVBoxLayout(GotoDialog)
        self._3.setObjectName("_3")
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setObjectName("_2")
        self.linenumberLabel = QtWidgets.QLabel(GotoDialog)
        self.linenumberLabel.setObjectName("linenumberLabel")
        self._2.addWidget(self.linenumberLabel)
        self.linenumberSpinBox = QtWidgets.QSpinBox(GotoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linenumberSpinBox.sizePolicy().hasHeightForWidth())
        self.linenumberSpinBox.setSizePolicy(sizePolicy)
        self.linenumberSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.linenumberSpinBox.setMinimum(1)
        self.linenumberSpinBox.setMaximum(99999)
        self.linenumberSpinBox.setObjectName("linenumberSpinBox")
        self._2.addWidget(self.linenumberSpinBox)
        self._3.addLayout(self._2)
        self.buttonBox = QtWidgets.QDialogButtonBox(GotoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self._3.addWidget(self.buttonBox)
        self.linenumberLabel.setBuddy(self.linenumberSpinBox)

        self.retranslateUi(GotoDialog)
        self.buttonBox.accepted.connect(GotoDialog.accept)
        self.buttonBox.rejected.connect(GotoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GotoDialog)

    def retranslateUi(self, GotoDialog):
        _translate = QtCore.QCoreApplication.translate
        GotoDialog.setWindowTitle(_translate("GotoDialog", "Goto"))
        self.linenumberLabel.setText(_translate("GotoDialog", "&Line Number:"))
        self.linenumberSpinBox.setToolTip(_translate("GotoDialog", "Enter linenumber to go to"))
        self.linenumberSpinBox.setWhatsThis(_translate("GotoDialog", "<b>Linenumber</b>\n"
"<p>Enter the linenumber to go to in this entry field.</p>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GotoDialog = QtWidgets.QDialog()
    ui = Ui_GotoDialog()
    ui.setupUi(GotoDialog)
    GotoDialog.show()
    sys.exit(app.exec_())

