# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Download\DownloadAskActionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadAskActionDialog(object):
    def setupUi(self, DownloadAskActionDialog):
        DownloadAskActionDialog.setObjectName("DownloadAskActionDialog")
        DownloadAskActionDialog.resize(500, 209)
        DownloadAskActionDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DownloadAskActionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(DownloadAskActionDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(DownloadAskActionDialog)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.infoLabel = QtWidgets.QLabel(DownloadAskActionDialog)
        self.infoLabel.setText("")
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout_2.addWidget(self.infoLabel, 0, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(DownloadAskActionDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
        self.typeLabel = QtWidgets.QLabel(DownloadAskActionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLabel.sizePolicy().hasHeightForWidth())
        self.typeLabel.setSizePolicy(sizePolicy)
        self.typeLabel.setText("")
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout_2.addWidget(self.typeLabel, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(DownloadAskActionDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)
        self.siteLabel = QtWidgets.QLabel(DownloadAskActionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.siteLabel.sizePolicy().hasHeightForWidth())
        self.siteLabel.setSizePolicy(sizePolicy)
        self.siteLabel.setText("")
        self.siteLabel.setObjectName("siteLabel")
        self.gridLayout_2.addWidget(self.siteLabel, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(DownloadAskActionDialog)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.openButton = QtWidgets.QRadioButton(DownloadAskActionDialog)
        self.openButton.setObjectName("openButton")
        self.gridLayout.addWidget(self.openButton, 1, 1, 1, 1)
        self.scanButton = QtWidgets.QRadioButton(DownloadAskActionDialog)
        self.scanButton.setObjectName("scanButton")
        self.gridLayout.addWidget(self.scanButton, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 2, 1)
        self.saveButton = QtWidgets.QRadioButton(DownloadAskActionDialog)
        self.saveButton.setChecked(True)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(DownloadAskActionDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(DownloadAskActionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DownloadAskActionDialog)
        self.buttonBox.accepted.connect(DownloadAskActionDialog.accept)
        self.buttonBox.rejected.connect(DownloadAskActionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DownloadAskActionDialog)
        DownloadAskActionDialog.setTabOrder(self.openButton, self.scanButton)
        DownloadAskActionDialog.setTabOrder(self.scanButton, self.saveButton)
        DownloadAskActionDialog.setTabOrder(self.saveButton, self.buttonBox)

    def retranslateUi(self, DownloadAskActionDialog):
        _translate = QtCore.QCoreApplication.translate
        DownloadAskActionDialog.setWindowTitle(_translate("DownloadAskActionDialog", "What to do?"))
        self.label_3.setText(_translate("DownloadAskActionDialog", "You are about to download this file:"))
        self.label_5.setText(_translate("DownloadAskActionDialog", "Type:"))
        self.label_6.setText(_translate("DownloadAskActionDialog", "From:"))
        self.openButton.setToolTip(_translate("DownloadAskActionDialog", "Select to open the downloaded file"))
        self.openButton.setText(_translate("DownloadAskActionDialog", "&Open File"))
        self.scanButton.setStatusTip(_translate("DownloadAskActionDialog", "Select to scan the file with VirusTotal"))
        self.scanButton.setText(_translate("DownloadAskActionDialog", "Scan with &VirusTotal"))
        self.saveButton.setToolTip(_translate("DownloadAskActionDialog", "Select to save the file"))
        self.saveButton.setText(_translate("DownloadAskActionDialog", "&Save File"))
        self.label.setText(_translate("DownloadAskActionDialog", "<b>What do you want to do?</b>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DownloadAskActionDialog = QtWidgets.QDialog()
    ui = Ui_DownloadAskActionDialog()
    ui.setupUi(DownloadAskActionDialog)
    DownloadAskActionDialog.show()
    sys.exit(app.exec_())
