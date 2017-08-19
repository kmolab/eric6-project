# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\Sync\SyncHostTypePage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SyncHostTypePage(object):
    def setupUi(self, SyncHostTypePage):
        SyncHostTypePage.setObjectName("SyncHostTypePage")
        SyncHostTypePage.resize(650, 400)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SyncHostTypePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(SyncHostTypePage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ftpRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.ftpRadioButton.setObjectName("ftpRadioButton")
        self.verticalLayout.addWidget(self.ftpRadioButton)
        self.directoryRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.directoryRadioButton.setObjectName("directoryRadioButton")
        self.verticalLayout.addWidget(self.directoryRadioButton)
        self.noneRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.noneRadioButton.setObjectName("noneRadioButton")
        self.verticalLayout.addWidget(self.noneRadioButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(SyncHostTypePage)
        QtCore.QMetaObject.connectSlotsByName(SyncHostTypePage)
        SyncHostTypePage.setTabOrder(self.ftpRadioButton, self.directoryRadioButton)
        SyncHostTypePage.setTabOrder(self.directoryRadioButton, self.noneRadioButton)

    def retranslateUi(self, SyncHostTypePage):
        _translate = QtCore.QCoreApplication.translate
        SyncHostTypePage.setTitle(_translate("SyncHostTypePage", "Host Type Selection"))
        SyncHostTypePage.setSubTitle(_translate("SyncHostTypePage", "Please select the type of the host to be used for synchronization."))
        self.groupBox.setTitle(_translate("SyncHostTypePage", "Synchronization Host Type"))
        self.ftpRadioButton.setToolTip(_translate("SyncHostTypePage", "Select to use a FTP host"))
        self.ftpRadioButton.setText(_translate("SyncHostTypePage", "FTP"))
        self.directoryRadioButton.setToolTip(_translate("SyncHostTypePage", "Select to use a shared directory"))
        self.directoryRadioButton.setText(_translate("SyncHostTypePage", "Shared Directory"))
        self.noneRadioButton.setToolTip(_translate("SyncHostTypePage", "Select to use no particular host type"))
        self.noneRadioButton.setText(_translate("SyncHostTypePage", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SyncHostTypePage = QtWidgets.QWizardPage()
    ui = Ui_SyncHostTypePage()
    ui.setupUi(SyncHostTypePage)
    SyncHostTypePage.show()
    sys.exit(app.exec_())

