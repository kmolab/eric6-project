# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\VirusTotal\VirusTotalWhoisDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VirusTotalWhoisDialog(object):
    def setupUi(self, VirusTotalWhoisDialog):
        VirusTotalWhoisDialog.setObjectName("VirusTotalWhoisDialog")
        VirusTotalWhoisDialog.resize(500, 400)
        VirusTotalWhoisDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(VirusTotalWhoisDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.headerPixmap = QtWidgets.QLabel(VirusTotalWhoisDialog)
        self.headerPixmap.setObjectName("headerPixmap")
        self.horizontalLayout_4.addWidget(self.headerPixmap)
        self.headerLabel = QtWidgets.QLabel(VirusTotalWhoisDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerLabel.sizePolicy().hasHeightForWidth())
        self.headerLabel.setSizePolicy(sizePolicy)
        self.headerLabel.setObjectName("headerLabel")
        self.horizontalLayout_4.addWidget(self.headerLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line9_3 = QtWidgets.QFrame(VirusTotalWhoisDialog)
        self.line9_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line9_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9_3.setObjectName("line9_3")
        self.verticalLayout.addWidget(self.line9_3)
        self.whoisEdit = QtWidgets.QPlainTextEdit(VirusTotalWhoisDialog)
        self.whoisEdit.setTabChangesFocus(True)
        self.whoisEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.whoisEdit.setReadOnly(True)
        self.whoisEdit.setObjectName("whoisEdit")
        self.verticalLayout.addWidget(self.whoisEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(VirusTotalWhoisDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(VirusTotalWhoisDialog)
        self.buttonBox.accepted.connect(VirusTotalWhoisDialog.accept)
        self.buttonBox.rejected.connect(VirusTotalWhoisDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VirusTotalWhoisDialog)

    def retranslateUi(self, VirusTotalWhoisDialog):
        _translate = QtCore.QCoreApplication.translate
        VirusTotalWhoisDialog.setWindowTitle(_translate("VirusTotalWhoisDialog", "Whois Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VirusTotalWhoisDialog = QtWidgets.QDialog()
    ui = Ui_VirusTotalWhoisDialog()
    ui.setupUi(VirusTotalWhoisDialog)
    VirusTotalWhoisDialog.show()
    sys.exit(app.exec_())

