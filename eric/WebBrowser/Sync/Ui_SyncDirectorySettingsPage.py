# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Sync\SyncDirectorySettingsPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SyncDirectorySettingsPage(object):
    def setupUi(self, SyncDirectorySettingsPage):
        SyncDirectorySettingsPage.setObjectName("SyncDirectorySettingsPage")
        SyncDirectorySettingsPage.resize(650, 400)
        SyncDirectorySettingsPage.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SyncDirectorySettingsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(SyncDirectorySettingsPage)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.directoryPicker = E5PathPicker(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directoryPicker.sizePolicy().hasHeightForWidth())
        self.directoryPicker.setSizePolicy(sizePolicy)
        self.directoryPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.directoryPicker.setObjectName("directoryPicker")
        self.horizontalLayout.addWidget(self.directoryPicker)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 317, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(SyncDirectorySettingsPage)
        QtCore.QMetaObject.connectSlotsByName(SyncDirectorySettingsPage)

    def retranslateUi(self, SyncDirectorySettingsPage):
        _translate = QtCore.QCoreApplication.translate
        SyncDirectorySettingsPage.setTitle(_translate("SyncDirectorySettingsPage", "Synchronize to a shared directory"))
        SyncDirectorySettingsPage.setSubTitle(_translate("SyncDirectorySettingsPage", "Please enter the data for synchronization via a shared directory. All fields must be filled."))
        self.groupBox.setTitle(_translate("SyncDirectorySettingsPage", "Shared Directory Settings"))
        self.label.setText(_translate("SyncDirectorySettingsPage", "Directory Name:"))
        self.directoryPicker.setToolTip(_translate("SyncDirectorySettingsPage", "Enter the full path of the shared directory"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SyncDirectorySettingsPage = QtWidgets.QWizardPage()
    ui = Ui_SyncDirectorySettingsPage()
    ui.setupUi(SyncDirectorySettingsPage)
    SyncDirectorySettingsPage.show()
    sys.exit(app.exec_())

