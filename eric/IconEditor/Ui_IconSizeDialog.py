# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\IconEditor\IconSizeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IconSizeDialog(object):
    def setupUi(self, IconSizeDialog):
        IconSizeDialog.setObjectName("IconSizeDialog")
        IconSizeDialog.resize(232, 78)
        IconSizeDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(IconSizeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(IconSizeDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.widthSpin = QtWidgets.QSpinBox(IconSizeDialog)
        self.widthSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthSpin.setMinimum(1)
        self.widthSpin.setMaximum(256)
        self.widthSpin.setProperty("value", 32)
        self.widthSpin.setObjectName("widthSpin")
        self.gridLayout.addWidget(self.widthSpin, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(IconSizeDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.heightSpin = QtWidgets.QSpinBox(IconSizeDialog)
        self.heightSpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightSpin.setMinimum(1)
        self.heightSpin.setMaximum(256)
        self.heightSpin.setProperty("value", 32)
        self.heightSpin.setObjectName("heightSpin")
        self.gridLayout.addWidget(self.heightSpin, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(42, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(IconSizeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 5)

        self.retranslateUi(IconSizeDialog)
        self.buttonBox.accepted.connect(IconSizeDialog.accept)
        self.buttonBox.rejected.connect(IconSizeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IconSizeDialog)
        IconSizeDialog.setTabOrder(self.widthSpin, self.heightSpin)
        IconSizeDialog.setTabOrder(self.heightSpin, self.buttonBox)

    def retranslateUi(self, IconSizeDialog):
        _translate = QtCore.QCoreApplication.translate
        IconSizeDialog.setWindowTitle(_translate("IconSizeDialog", "Icon Size"))
        self.label.setText(_translate("IconSizeDialog", "Size:"))
        self.widthSpin.setToolTip(_translate("IconSizeDialog", "Enter the width of the icon"))
        self.label_2.setText(_translate("IconSizeDialog", "X"))
        self.heightSpin.setToolTip(_translate("IconSizeDialog", "Enter the height of the icon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IconSizeDialog = QtWidgets.QDialog()
    ui = Ui_IconSizeDialog()
    ui.setupUi(IconSizeDialog)
    IconSizeDialog.show()
    sys.exit(app.exec_())

