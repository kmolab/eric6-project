# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ViewProfileToolboxesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewProfileToolboxesDialog(object):
    def setupUi(self, ViewProfileToolboxesDialog):
        ViewProfileToolboxesDialog.setObjectName("ViewProfileToolboxesDialog")
        ViewProfileToolboxesDialog.resize(608, 177)
        ViewProfileToolboxesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(ViewProfileToolboxesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(ViewProfileToolboxesDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 2)
        self.editGroup = QtWidgets.QGroupBox(ViewProfileToolboxesDialog)
        self.editGroup.setObjectName("editGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.editGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.epltCheckBox = QtWidgets.QCheckBox(self.editGroup)
        self.epltCheckBox.setChecked(True)
        self.epltCheckBox.setObjectName("epltCheckBox")
        self.verticalLayout_2.addWidget(self.epltCheckBox)
        self.eprtCheckBox = QtWidgets.QCheckBox(self.editGroup)
        self.eprtCheckBox.setChecked(True)
        self.eprtCheckBox.setObjectName("eprtCheckBox")
        self.verticalLayout_2.addWidget(self.eprtCheckBox)
        self.ephtCheckBox = QtWidgets.QCheckBox(self.editGroup)
        self.ephtCheckBox.setChecked(True)
        self.ephtCheckBox.setObjectName("ephtCheckBox")
        self.verticalLayout_2.addWidget(self.ephtCheckBox)
        self.gridLayout.addWidget(self.editGroup, 1, 0, 1, 1)
        self.debugGroup = QtWidgets.QGroupBox(ViewProfileToolboxesDialog)
        self.debugGroup.setObjectName("debugGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.debugGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dpltCheckBox = QtWidgets.QCheckBox(self.debugGroup)
        self.dpltCheckBox.setObjectName("dpltCheckBox")
        self.verticalLayout.addWidget(self.dpltCheckBox)
        self.dprtCheckBox = QtWidgets.QCheckBox(self.debugGroup)
        self.dprtCheckBox.setChecked(True)
        self.dprtCheckBox.setObjectName("dprtCheckBox")
        self.verticalLayout.addWidget(self.dprtCheckBox)
        self.dphtCheckBox = QtWidgets.QCheckBox(self.debugGroup)
        self.dphtCheckBox.setChecked(True)
        self.dphtCheckBox.setObjectName("dphtCheckBox")
        self.verticalLayout.addWidget(self.dphtCheckBox)
        self.gridLayout.addWidget(self.debugGroup, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ViewProfileToolboxesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(ViewProfileToolboxesDialog)
        self.buttonBox.accepted.connect(ViewProfileToolboxesDialog.accept)
        self.buttonBox.rejected.connect(ViewProfileToolboxesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ViewProfileToolboxesDialog)
        ViewProfileToolboxesDialog.setTabOrder(self.epltCheckBox, self.eprtCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.eprtCheckBox, self.ephtCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.ephtCheckBox, self.dpltCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.dpltCheckBox, self.dprtCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.dprtCheckBox, self.dphtCheckBox)
        ViewProfileToolboxesDialog.setTabOrder(self.dphtCheckBox, self.buttonBox)

    def retranslateUi(self, ViewProfileToolboxesDialog):
        _translate = QtCore.QCoreApplication.translate
        ViewProfileToolboxesDialog.setWindowTitle(_translate("ViewProfileToolboxesDialog", "Configure View Profiles"))
        self.textLabel1.setText(_translate("ViewProfileToolboxesDialog", "Select the windows, that should be visible, when the different profiles are active."))
        self.editGroup.setTitle(_translate("ViewProfileToolboxesDialog", "&Edit Profile"))
        self.epltCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Left Toolbox"))
        self.eprtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Right Toolbox"))
        self.ephtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Horizontal Toolbox"))
        self.debugGroup.setTitle(_translate("ViewProfileToolboxesDialog", "&Debug Profile"))
        self.dpltCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Left Toolbox"))
        self.dprtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Right Toolbox"))
        self.dphtCheckBox.setText(_translate("ViewProfileToolboxesDialog", "Horizontal Toolbox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewProfileToolboxesDialog = QtWidgets.QDialog()
    ui = Ui_ViewProfileToolboxesDialog()
    ui.setupUi(ViewProfileToolboxesDialog)
    ViewProfileToolboxesDialog.show()
    sys.exit(app.exec_())

