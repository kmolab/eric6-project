# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgAddSubrepositoryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgAddSubrepositoryDialog(object):
    def setupUi(self, HgAddSubrepositoryDialog):
        HgAddSubrepositoryDialog.setObjectName("HgAddSubrepositoryDialog")
        HgAddSubrepositoryDialog.resize(550, 124)
        HgAddSubrepositoryDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgAddSubrepositoryDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgAddSubrepositoryDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pathPicker = E5PathPicker(HgAddSubrepositoryDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathPicker.sizePolicy().hasHeightForWidth())
        self.pathPicker.setSizePolicy(sizePolicy)
        self.pathPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pathPicker.setObjectName("pathPicker")
        self.gridLayout.addWidget(self.pathPicker, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(HgAddSubrepositoryDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.typeCombo = QtWidgets.QComboBox(HgAddSubrepositoryDialog)
        self.typeCombo.setObjectName("typeCombo")
        self.horizontalLayout_2.addWidget(self.typeCombo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HgAddSubrepositoryDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.urlEdit = QtWidgets.QLineEdit(HgAddSubrepositoryDialog)
        self.urlEdit.setObjectName("urlEdit")
        self.gridLayout.addWidget(self.urlEdit, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgAddSubrepositoryDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.label.setBuddy(self.pathPicker)
        self.label_2.setBuddy(self.typeCombo)
        self.label_3.setBuddy(self.urlEdit)

        self.retranslateUi(HgAddSubrepositoryDialog)
        self.buttonBox.accepted.connect(HgAddSubrepositoryDialog.accept)
        self.buttonBox.rejected.connect(HgAddSubrepositoryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgAddSubrepositoryDialog)
        HgAddSubrepositoryDialog.setTabOrder(self.pathPicker, self.typeCombo)
        HgAddSubrepositoryDialog.setTabOrder(self.typeCombo, self.urlEdit)

    def retranslateUi(self, HgAddSubrepositoryDialog):
        _translate = QtCore.QCoreApplication.translate
        HgAddSubrepositoryDialog.setWindowTitle(_translate("HgAddSubrepositoryDialog", "Add Sub-repository"))
        self.label.setText(_translate("HgAddSubrepositoryDialog", "&Path within Project:"))
        self.pathPicker.setToolTip(_translate("HgAddSubrepositoryDialog", "Enter the path of the sub-repository relative to the project"))
        self.label_2.setText(_translate("HgAddSubrepositoryDialog", "&Type:"))
        self.typeCombo.setToolTip(_translate("HgAddSubrepositoryDialog", "Select the type of the sub-repository"))
        self.label_3.setText(_translate("HgAddSubrepositoryDialog", "&URL:"))
        self.urlEdit.setToolTip(_translate("HgAddSubrepositoryDialog", "Enter the URL of the sub-repository"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgAddSubrepositoryDialog = QtWidgets.QDialog()
    ui = Ui_HgAddSubrepositoryDialog()
    ui.setupUi(HgAddSubrepositoryDialog)
    HgAddSubrepositoryDialog.show()
    sys.exit(app.exec_())

