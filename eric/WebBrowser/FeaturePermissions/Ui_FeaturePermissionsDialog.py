# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\FeaturePermissions\FeaturePermissionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FeaturePermissionsDialog(object):
    def setupUi(self, FeaturePermissionsDialog):
        FeaturePermissionsDialog.setObjectName("FeaturePermissionsDialog")
        FeaturePermissionsDialog.resize(650, 400)
        FeaturePermissionsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(FeaturePermissionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(FeaturePermissionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.removeButton = QtWidgets.QPushButton(FeaturePermissionsDialog)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtWidgets.QPushButton(FeaturePermissionsDialog)
        self.removeAllButton.setObjectName("removeAllButton")
        self.verticalLayout_3.addWidget(self.removeAllButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(FeaturePermissionsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(FeaturePermissionsDialog)
        self.tabWidget.setCurrentIndex(-1)
        self.buttonBox.accepted.connect(FeaturePermissionsDialog.accept)
        self.buttonBox.rejected.connect(FeaturePermissionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FeaturePermissionsDialog)
        FeaturePermissionsDialog.setTabOrder(self.tabWidget, self.removeButton)
        FeaturePermissionsDialog.setTabOrder(self.removeButton, self.removeAllButton)

    def retranslateUi(self, FeaturePermissionsDialog):
        _translate = QtCore.QCoreApplication.translate
        FeaturePermissionsDialog.setWindowTitle(_translate("FeaturePermissionsDialog", "HTML5 Feature Permissions"))
        self.removeButton.setText(_translate("FeaturePermissionsDialog", "&Remove"))
        self.removeAllButton.setText(_translate("FeaturePermissionsDialog", "Remove &All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FeaturePermissionsDialog = QtWidgets.QDialog()
    ui = Ui_FeaturePermissionsDialog()
    ui.setupUi(FeaturePermissionsDialog)
    FeaturePermissionsDialog.show()
    sys.exit(app.exec_())

