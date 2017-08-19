# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\AdBlock\AdBlockDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdBlockDialog(object):
    def setupUi(self, AdBlockDialog):
        AdBlockDialog.setObjectName("AdBlockDialog")
        AdBlockDialog.resize(650, 600)
        AdBlockDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(AdBlockDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.adBlockGroup = QtWidgets.QGroupBox(AdBlockDialog)
        self.adBlockGroup.setCheckable(True)
        self.adBlockGroup.setObjectName("adBlockGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.adBlockGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.iconLabel = QtWidgets.QLabel(self.adBlockGroup)
        self.iconLabel.setMinimumSize(QtCore.QSize(48, 48))
        self.iconLabel.setText("Icon")
        self.iconLabel.setObjectName("iconLabel")
        self.gridLayout.addWidget(self.iconLabel, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.searchEdit = E5ClearableLineEdit(self.adBlockGroup)
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout.addWidget(self.searchEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.subscriptionsTabWidget = QtWidgets.QTabWidget(self.adBlockGroup)
        self.subscriptionsTabWidget.setDocumentMode(True)
        self.subscriptionsTabWidget.setObjectName("subscriptionsTabWidget")
        self.verticalLayout.addWidget(self.subscriptionsTabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.actionButton = QtWidgets.QToolButton(self.adBlockGroup)
        self.actionButton.setObjectName("actionButton")
        self.horizontalLayout.addWidget(self.actionButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.adBlockGroup)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.updateSpinBox = QtWidgets.QSpinBox(self.adBlockGroup)
        self.updateSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.updateSpinBox.setSuffix("")
        self.updateSpinBox.setMinimum(1)
        self.updateSpinBox.setMaximum(14)
        self.updateSpinBox.setProperty("value", 7)
        self.updateSpinBox.setObjectName("updateSpinBox")
        self.horizontalLayout.addWidget(self.updateSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.adBlockGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(AdBlockDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(AdBlockDialog)
        self.buttonBox.accepted.connect(AdBlockDialog.accept)
        self.buttonBox.rejected.connect(AdBlockDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AdBlockDialog)
        AdBlockDialog.setTabOrder(self.adBlockGroup, self.searchEdit)
        AdBlockDialog.setTabOrder(self.searchEdit, self.subscriptionsTabWidget)
        AdBlockDialog.setTabOrder(self.subscriptionsTabWidget, self.actionButton)
        AdBlockDialog.setTabOrder(self.actionButton, self.updateSpinBox)
        AdBlockDialog.setTabOrder(self.updateSpinBox, self.buttonBox)

    def retranslateUi(self, AdBlockDialog):
        _translate = QtCore.QCoreApplication.translate
        AdBlockDialog.setWindowTitle(_translate("AdBlockDialog", "AdBlock Configuration"))
        self.adBlockGroup.setTitle(_translate("AdBlockDialog", "Enable AdBlock"))
        self.searchEdit.setToolTip(_translate("AdBlockDialog", "Enter search term for subscriptions and rules"))
        self.actionButton.setText(_translate("AdBlockDialog", "Actions"))
        self.label.setText(_translate("AdBlockDialog", "Default Update Period (days):"))
        self.updateSpinBox.setToolTip(_translate("AdBlockDialog", "Enter the update period (1 to 14 days)"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdBlockDialog = QtWidgets.QDialog()
    ui = Ui_AdBlockDialog()
    ui.setupUi(AdBlockDialog)
    AdBlockDialog.show()
    sys.exit(app.exec_())

