# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnPropSetDialog.ui'
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SvnPropSetDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel1 = QtWidgets.QLabel(SvnPropSetDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.hboxlayout.addWidget(self.textLabel1)
        self.propNameEdit = QtWidgets.QLineEdit(SvnPropSetDialog)
        self.propNameEdit.setObjectName("propNameEdit")
        self.hboxlayout.addWidget(self.propNameEdit)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        self.groupBox = QtWidgets.QGroupBox(SvnPropSetDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.textRadioButton.setChecked(True)
        self.textRadioButton.setObjectName("textRadioButton")
        self.verticalLayout.addWidget(self.textRadioButton)
        self.propTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.propTextEdit.setTabChangesFocus(True)
        self.propTextEdit.setAcceptRichText(False)
        self.propTextEdit.setObjectName("propTextEdit")
        self.verticalLayout.addWidget(self.propTextEdit)
        self.fileRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.fileRadioButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fileRadioButton.setObjectName("fileRadioButton")
        self.verticalLayout.addWidget(self.fileRadioButton)
        self.propFilePicker = E5PathPicker(self.groupBox)
        self.propFilePicker.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propFilePicker.sizePolicy().hasHeightForWidth())
        self.propFilePicker.setSizePolicy(sizePolicy)
        self.propFilePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.propFilePicker.setObjectName("propFilePicker")
        self.verticalLayout.addWidget(self.propFilePicker)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnPropSetDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SvnPropSetDialog)
        self.textRadioButton.toggled['bool'].connect(self.propTextEdit.setEnabled)
        self.buttonBox.accepted.connect(SvnPropSetDialog.accept)
        self.buttonBox.rejected.connect(SvnPropSetDialog.reject)
        self.fileRadioButton.toggled['bool'].connect(self.propFilePicker.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(SvnPropSetDialog)
        SvnPropSetDialog.setTabOrder(self.propNameEdit, self.textRadioButton)
        SvnPropSetDialog.setTabOrder(self.textRadioButton, self.propTextEdit)
        SvnPropSetDialog.setTabOrder(self.propTextEdit, self.propFilePicker)

    def retranslateUi(self, SvnPropSetDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnPropSetDialog.setWindowTitle(_translate("SvnPropSetDialog", "Set Subversion Property"))
        self.textLabel1.setText(_translate("SvnPropSetDialog", "Property Name:"))
        self.propNameEdit.setToolTip(_translate("SvnPropSetDialog", "Enter the name of the property to be set"))
        self.groupBox.setTitle(_translate("SvnPropSetDialog", "Select property source"))
        self.textRadioButton.setText(_translate("SvnPropSetDialog", "Text"))
        self.propTextEdit.setToolTip(_translate("SvnPropSetDialog", "Enter text of the property"))
        self.fileRadioButton.setText(_translate("SvnPropSetDialog", "File"))
        self.propFilePicker.setToolTip(_translate("SvnPropSetDialog", "Enter the name of a file for the property"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnPropSetDialog = QtWidgets.QDialog()
    ui = Ui_SvnPropSetDialog()
    ui.setupUi(SvnPropSetDialog)
    SvnPropSetDialog.show()
    sys.exit(app.exec_())

