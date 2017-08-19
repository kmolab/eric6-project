# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\NewDialogClassDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewDialogClassDialog(object):
    def setupUi(self, NewDialogClassDialog):
        NewDialogClassDialog.setObjectName("NewDialogClassDialog")
        NewDialogClassDialog.resize(600, 124)
        NewDialogClassDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewDialogClassDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(NewDialogClassDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.classnameEdit = QtWidgets.QLineEdit(NewDialogClassDialog)
        self.classnameEdit.setObjectName("classnameEdit")
        self.gridLayout.addWidget(self.classnameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(NewDialogClassDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.filenameEdit = QtWidgets.QLineEdit(NewDialogClassDialog)
        self.filenameEdit.setObjectName("filenameEdit")
        self.gridLayout.addWidget(self.filenameEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(NewDialogClassDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pathnamePicker = E5PathPicker(NewDialogClassDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathnamePicker.sizePolicy().hasHeightForWidth())
        self.pathnamePicker.setSizePolicy(sizePolicy)
        self.pathnamePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pathnamePicker.setObjectName("pathnamePicker")
        self.gridLayout.addWidget(self.pathnamePicker, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewDialogClassDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.classnameEdit)
        self.label_2.setBuddy(self.filenameEdit)
        self.label_3.setBuddy(self.pathnamePicker)

        self.retranslateUi(NewDialogClassDialog)
        self.buttonBox.accepted.connect(NewDialogClassDialog.accept)
        self.buttonBox.rejected.connect(NewDialogClassDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewDialogClassDialog)
        NewDialogClassDialog.setTabOrder(self.classnameEdit, self.filenameEdit)
        NewDialogClassDialog.setTabOrder(self.filenameEdit, self.buttonBox)

    def retranslateUi(self, NewDialogClassDialog):
        _translate = QtCore.QCoreApplication.translate
        NewDialogClassDialog.setWindowTitle(_translate("NewDialogClassDialog", "New Dialog Class"))
        self.label.setText(_translate("NewDialogClassDialog", "&Classname:"))
        self.classnameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the name of the new class"))
        self.label_2.setText(_translate("NewDialogClassDialog", "&Filename:"))
        self.filenameEdit.setToolTip(_translate("NewDialogClassDialog", "Enter the name of the file for the forms code"))
        self.label_3.setText(_translate("NewDialogClassDialog", "&Path:"))
        self.pathnamePicker.setToolTip(_translate("NewDialogClassDialog", "Enter the path of the file for the forms code"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDialogClassDialog = QtWidgets.QDialog()
    ui = Ui_NewDialogClassDialog()
    ui.setupUi(NewDialogClassDialog)
    NewDialogClassDialog.show()
    sys.exit(app.exec_())

