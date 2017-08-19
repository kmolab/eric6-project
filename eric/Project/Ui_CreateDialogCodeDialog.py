# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\CreateDialogCodeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateDialogCodeDialog(object):
    def setupUi(self, CreateDialogCodeDialog):
        CreateDialogCodeDialog.setObjectName("CreateDialogCodeDialog")
        CreateDialogCodeDialog.resize(584, 466)
        CreateDialogCodeDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateDialogCodeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(CreateDialogCodeDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.classNameCombo = QtWidgets.QComboBox(CreateDialogCodeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.classNameCombo.sizePolicy().hasHeightForWidth())
        self.classNameCombo.setSizePolicy(sizePolicy)
        self.classNameCombo.setObjectName("classNameCombo")
        self.gridLayout.addWidget(self.classNameCombo, 0, 1, 1, 1)
        self.newButton = QtWidgets.QPushButton(CreateDialogCodeDialog)
        self.newButton.setObjectName("newButton")
        self.gridLayout.addWidget(self.newButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(CreateDialogCodeDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.filenameEdit = QtWidgets.QLineEdit(CreateDialogCodeDialog)
        self.filenameEdit.setReadOnly(True)
        self.filenameEdit.setObjectName("filenameEdit")
        self.gridLayout.addWidget(self.filenameEdit, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(CreateDialogCodeDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.filterEdit = E5ClearableLineEdit(CreateDialogCodeDialog)
        self.filterEdit.setObjectName("filterEdit")
        self.gridLayout.addWidget(self.filterEdit, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.slotsView = QtWidgets.QTreeView(CreateDialogCodeDialog)
        self.slotsView.setSortingEnabled(True)
        self.slotsView.setObjectName("slotsView")
        self.verticalLayout.addWidget(self.slotsView)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateDialogCodeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.classNameCombo)
        self.label_2.setBuddy(self.filenameEdit)
        self.label_3.setBuddy(self.filterEdit)

        self.retranslateUi(CreateDialogCodeDialog)
        self.buttonBox.rejected.connect(CreateDialogCodeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CreateDialogCodeDialog)
        CreateDialogCodeDialog.setTabOrder(self.classNameCombo, self.newButton)
        CreateDialogCodeDialog.setTabOrder(self.newButton, self.filenameEdit)
        CreateDialogCodeDialog.setTabOrder(self.filenameEdit, self.filterEdit)
        CreateDialogCodeDialog.setTabOrder(self.filterEdit, self.slotsView)
        CreateDialogCodeDialog.setTabOrder(self.slotsView, self.buttonBox)

    def retranslateUi(self, CreateDialogCodeDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateDialogCodeDialog.setWindowTitle(_translate("CreateDialogCodeDialog", "Forms code generator"))
        self.label.setText(_translate("CreateDialogCodeDialog", "&Classname:"))
        self.classNameCombo.setToolTip(_translate("CreateDialogCodeDialog", "Select the class that should get the forms code"))
        self.newButton.setToolTip(_translate("CreateDialogCodeDialog", "Press to generate a new forms class"))
        self.newButton.setText(_translate("CreateDialogCodeDialog", "&New..."))
        self.label_2.setText(_translate("CreateDialogCodeDialog", "&Filename:"))
        self.filenameEdit.setToolTip(_translate("CreateDialogCodeDialog", "Displays the name of the file containing the code"))
        self.label_3.setText(_translate("CreateDialogCodeDialog", "Filter &with:"))
        self.filterEdit.setToolTip(_translate("CreateDialogCodeDialog", "Enter a regular expression to filter the list below"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateDialogCodeDialog = QtWidgets.QDialog()
    ui = Ui_CreateDialogCodeDialog()
    ui.setupUi(CreateDialogCodeDialog)
    CreateDialogCodeDialog.show()
    sys.exit(app.exec_())

