# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Graphics\UMLSceneSizeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UMLSceneSizeDialog(object):
    def setupUi(self, UMLSceneSizeDialog):
        UMLSceneSizeDialog.setObjectName("UMLSceneSizeDialog")
        UMLSceneSizeDialog.resize(314, 103)
        UMLSceneSizeDialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(UMLSceneSizeDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(UMLSceneSizeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.textLabel2 = QtWidgets.QLabel(UMLSceneSizeDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridlayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(UMLSceneSizeDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.heightSpinBox = QtWidgets.QSpinBox(UMLSceneSizeDialog)
        self.heightSpinBox.setMinimum(100)
        self.heightSpinBox.setMaximum(100000)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.gridlayout.addWidget(self.heightSpinBox, 1, 1, 1, 1)
        self.widthSpinBox = QtWidgets.QSpinBox(UMLSceneSizeDialog)
        self.widthSpinBox.setMinimum(100)
        self.widthSpinBox.setMaximum(100000)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.gridlayout.addWidget(self.widthSpinBox, 0, 1, 1, 1)

        self.retranslateUi(UMLSceneSizeDialog)
        self.buttonBox.accepted.connect(UMLSceneSizeDialog.accept)
        self.buttonBox.rejected.connect(UMLSceneSizeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UMLSceneSizeDialog)

    def retranslateUi(self, UMLSceneSizeDialog):
        _translate = QtCore.QCoreApplication.translate
        UMLSceneSizeDialog.setWindowTitle(_translate("UMLSceneSizeDialog", "Set Size"))
        self.textLabel2.setText(_translate("UMLSceneSizeDialog", "Height (in pixels):"))
        self.textLabel1.setText(_translate("UMLSceneSizeDialog", "Width (in pixels):"))
        self.heightSpinBox.setToolTip(_translate("UMLSceneSizeDialog", "Select the height of the diagram"))
        self.widthSpinBox.setToolTip(_translate("UMLSceneSizeDialog", "Select the width of the diagram"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UMLSceneSizeDialog = QtWidgets.QDialog()
    ui = Ui_UMLSceneSizeDialog()
    ui.setupUi(UMLSceneSizeDialog)
    UMLSceneSizeDialog.show()
    sys.exit(app.exec_())

