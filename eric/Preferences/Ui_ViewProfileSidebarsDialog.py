# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ViewProfileSidebarsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewProfileSidebarsDialog(object):
    def setupUi(self, ViewProfileSidebarsDialog):
        ViewProfileSidebarsDialog.setObjectName("ViewProfileSidebarsDialog")
        ViewProfileSidebarsDialog.resize(608, 177)
        ViewProfileSidebarsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(ViewProfileSidebarsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(ViewProfileSidebarsDialog)
        self.textLabel1.setAlignment(QtCore.Qt.AlignVCenter)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 2)
        self.editGroup = QtWidgets.QGroupBox(ViewProfileSidebarsDialog)
        self.editGroup.setObjectName("editGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.editGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.epltCheckBox = QtWidgets.QCheckBox(self.editGroup)
        self.epltCheckBox.setChecked(True)
        self.epltCheckBox.setObjectName("epltCheckBox")
        self.verticalLayout.addWidget(self.epltCheckBox)
        self.eprtCheckBox = QtWidgets.QCheckBox(self.editGroup)
        self.eprtCheckBox.setChecked(True)
        self.eprtCheckBox.setObjectName("eprtCheckBox")
        self.verticalLayout.addWidget(self.eprtCheckBox)
        self.ephtCheckBox = QtWidgets.QCheckBox(self.editGroup)
        self.ephtCheckBox.setChecked(True)
        self.ephtCheckBox.setObjectName("ephtCheckBox")
        self.verticalLayout.addWidget(self.ephtCheckBox)
        self.gridLayout.addWidget(self.editGroup, 1, 0, 1, 1)
        self.debugGroup = QtWidgets.QGroupBox(ViewProfileSidebarsDialog)
        self.debugGroup.setObjectName("debugGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.debugGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dpltCheckBox = QtWidgets.QCheckBox(self.debugGroup)
        self.dpltCheckBox.setObjectName("dpltCheckBox")
        self.verticalLayout_2.addWidget(self.dpltCheckBox)
        self.dprtCheckBox = QtWidgets.QCheckBox(self.debugGroup)
        self.dprtCheckBox.setChecked(True)
        self.dprtCheckBox.setObjectName("dprtCheckBox")
        self.verticalLayout_2.addWidget(self.dprtCheckBox)
        self.dphtCheckBox = QtWidgets.QCheckBox(self.debugGroup)
        self.dphtCheckBox.setChecked(True)
        self.dphtCheckBox.setObjectName("dphtCheckBox")
        self.verticalLayout_2.addWidget(self.dphtCheckBox)
        self.gridLayout.addWidget(self.debugGroup, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ViewProfileSidebarsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(ViewProfileSidebarsDialog)
        self.buttonBox.accepted.connect(ViewProfileSidebarsDialog.accept)
        self.buttonBox.rejected.connect(ViewProfileSidebarsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ViewProfileSidebarsDialog)
        ViewProfileSidebarsDialog.setTabOrder(self.eprtCheckBox, self.epltCheckBox)
        ViewProfileSidebarsDialog.setTabOrder(self.epltCheckBox, self.ephtCheckBox)
        ViewProfileSidebarsDialog.setTabOrder(self.ephtCheckBox, self.dpltCheckBox)
        ViewProfileSidebarsDialog.setTabOrder(self.dpltCheckBox, self.dprtCheckBox)
        ViewProfileSidebarsDialog.setTabOrder(self.dprtCheckBox, self.dphtCheckBox)
        ViewProfileSidebarsDialog.setTabOrder(self.dphtCheckBox, self.buttonBox)

    def retranslateUi(self, ViewProfileSidebarsDialog):
        _translate = QtCore.QCoreApplication.translate
        ViewProfileSidebarsDialog.setWindowTitle(_translate("ViewProfileSidebarsDialog", "Configure View Profiles"))
        self.textLabel1.setText(_translate("ViewProfileSidebarsDialog", "Select the windows, that should be visible, when the different profiles are active."))
        self.editGroup.setTitle(_translate("ViewProfileSidebarsDialog", "&Edit Profile"))
        self.epltCheckBox.setText(_translate("ViewProfileSidebarsDialog", "Left Sidebar"))
        self.eprtCheckBox.setText(_translate("ViewProfileSidebarsDialog", "Right Sidebar"))
        self.ephtCheckBox.setText(_translate("ViewProfileSidebarsDialog", "Bottom Sidebar"))
        self.debugGroup.setTitle(_translate("ViewProfileSidebarsDialog", "&Debug Profile"))
        self.dpltCheckBox.setText(_translate("ViewProfileSidebarsDialog", "Left Sidebar"))
        self.dprtCheckBox.setText(_translate("ViewProfileSidebarsDialog", "Right Sidebar"))
        self.dphtCheckBox.setText(_translate("ViewProfileSidebarsDialog", "Bottom Sidebar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewProfileSidebarsDialog = QtWidgets.QDialog()
    ui = Ui_ViewProfileSidebarsDialog()
    ui.setupUi(ViewProfileSidebarsDialog)
    ViewProfileSidebarsDialog.show()
    sys.exit(app.exec_())

