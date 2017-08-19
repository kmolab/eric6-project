# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnPropSetDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnPropSetDialog(object):
    def setupUi(self, SvnPropSetDialog):
        SvnPropSetDialog.setObjectName("SvnPropSetDialog")
        SvnPropSetDialog.resize(494, 385)
        SvnPropSetDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnPropSetDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.propTextEdit = QtWidgets.QTextEdit(SvnPropSetDialog)
        self.propTextEdit.setTabChangesFocus(True)
        self.propTextEdit.setAcceptRichText(False)
        self.propTextEdit.setObjectName("propTextEdit")
        self.gridlayout.addWidget(self.propTextEdit, 1, 1, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(SvnPropSetDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridlayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.propNameEdit = QtWidgets.QLineEdit(SvnPropSetDialog)
        self.propNameEdit.setObjectName("propNameEdit")
        self.gridlayout.addWidget(self.propNameEdit, 0, 1, 1, 1)
        self.recurseCheckBox = QtWidgets.QCheckBox(SvnPropSetDialog)
        self.recurseCheckBox.setObjectName("recurseCheckBox")
        self.gridlayout.addWidget(self.recurseCheckBox, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(SvnPropSetDialog)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnPropSetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.propNameEdit)
        self.label.setBuddy(self.propTextEdit)

        self.retranslateUi(SvnPropSetDialog)
        self.buttonBox.accepted.connect(SvnPropSetDialog.accept)
        self.buttonBox.rejected.connect(SvnPropSetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnPropSetDialog)
        SvnPropSetDialog.setTabOrder(self.propNameEdit, self.propTextEdit)
        SvnPropSetDialog.setTabOrder(self.propTextEdit, self.recurseCheckBox)

    def retranslateUi(self, SvnPropSetDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnPropSetDialog.setWindowTitle(_translate("SvnPropSetDialog", "Set Subversion Property"))
        self.propTextEdit.setToolTip(_translate("SvnPropSetDialog", "Enter text of the property"))
        self.textLabel1.setText(_translate("SvnPropSetDialog", "Property &Name:"))
        self.propNameEdit.setToolTip(_translate("SvnPropSetDialog", "Enter the name of the property to be set"))
        self.recurseCheckBox.setToolTip(_translate("SvnPropSetDialog", "Select to apply the property recursively"))
        self.recurseCheckBox.setText(_translate("SvnPropSetDialog", "Apply &recursively"))
        self.label.setText(_translate("SvnPropSetDialog", "Property &Value:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnPropSetDialog = QtWidgets.QDialog()
    ui = Ui_SvnPropSetDialog()
    ui.setupUi(SvnPropSetDialog)
    SvnPropSetDialog.show()
    sys.exit(app.exec_())

