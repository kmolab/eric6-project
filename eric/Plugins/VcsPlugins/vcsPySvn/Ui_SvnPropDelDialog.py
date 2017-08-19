# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnPropDelDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnPropDelDialog(object):
    def setupUi(self, SvnPropDelDialog):
        SvnPropDelDialog.setObjectName("SvnPropDelDialog")
        SvnPropDelDialog.resize(494, 98)
        SvnPropDelDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnPropDelDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.propNameEdit = QtWidgets.QLineEdit(SvnPropDelDialog)
        self.propNameEdit.setObjectName("propNameEdit")
        self.gridlayout.addWidget(self.propNameEdit, 0, 1, 1, 1)
        self.recurseCheckBox = QtWidgets.QCheckBox(SvnPropDelDialog)
        self.recurseCheckBox.setObjectName("recurseCheckBox")
        self.gridlayout.addWidget(self.recurseCheckBox, 1, 0, 1, 2)
        self.textLabel1 = QtWidgets.QLabel(SvnPropDelDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnPropDelDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.propNameEdit)

        self.retranslateUi(SvnPropDelDialog)
        self.buttonBox.accepted.connect(SvnPropDelDialog.accept)
        self.buttonBox.rejected.connect(SvnPropDelDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnPropDelDialog)
        SvnPropDelDialog.setTabOrder(self.propNameEdit, self.recurseCheckBox)

    def retranslateUi(self, SvnPropDelDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnPropDelDialog.setWindowTitle(_translate("SvnPropDelDialog", "Delete Subversion Property"))
        self.propNameEdit.setToolTip(_translate("SvnPropDelDialog", "Enter the name of the property to be deleted"))
        self.recurseCheckBox.setToolTip(_translate("SvnPropDelDialog", "Select to apply the property recursively"))
        self.recurseCheckBox.setText(_translate("SvnPropDelDialog", "Apply &recursively"))
        self.textLabel1.setText(_translate("SvnPropDelDialog", "Property &Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnPropDelDialog = QtWidgets.QDialog()
    ui = Ui_SvnPropDelDialog()
    ui.setupUi(SvnPropDelDialog)
    SvnPropDelDialog.show()
    sys.exit(app.exec_())

