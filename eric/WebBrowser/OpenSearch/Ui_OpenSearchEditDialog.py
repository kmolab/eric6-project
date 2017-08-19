# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\OpenSearch\OpenSearchEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenSearchEditDialog(object):
    def setupUi(self, OpenSearchEditDialog):
        OpenSearchEditDialog.setObjectName("OpenSearchEditDialog")
        OpenSearchEditDialog.resize(690, 218)
        OpenSearchEditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenSearchEditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(OpenSearchEditDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(OpenSearchEditDialog)
        self.nameEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(OpenSearchEditDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QLineEdit(OpenSearchEditDialog)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(OpenSearchEditDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.imageEdit = QtWidgets.QLineEdit(OpenSearchEditDialog)
        self.imageEdit.setObjectName("imageEdit")
        self.gridLayout.addWidget(self.imageEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label_4 = QtWidgets.QLabel(OpenSearchEditDialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.searchEdit = QtWidgets.QLineEdit(OpenSearchEditDialog)
        self.searchEdit.setObjectName("searchEdit")
        self.verticalLayout.addWidget(self.searchEdit)
        self.label_6 = QtWidgets.QLabel(OpenSearchEditDialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.suggestionsEdit = QtWidgets.QLineEdit(OpenSearchEditDialog)
        self.suggestionsEdit.setObjectName("suggestionsEdit")
        self.verticalLayout.addWidget(self.suggestionsEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpenSearchEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.nameEdit)
        self.label_3.setBuddy(self.descriptionEdit)
        self.label_5.setBuddy(self.imageEdit)
        self.label_4.setBuddy(self.searchEdit)
        self.label_6.setBuddy(self.suggestionsEdit)

        self.retranslateUi(OpenSearchEditDialog)
        self.buttonBox.accepted.connect(OpenSearchEditDialog.accept)
        self.buttonBox.rejected.connect(OpenSearchEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenSearchEditDialog)
        OpenSearchEditDialog.setTabOrder(self.nameEdit, self.descriptionEdit)
        OpenSearchEditDialog.setTabOrder(self.descriptionEdit, self.imageEdit)
        OpenSearchEditDialog.setTabOrder(self.imageEdit, self.searchEdit)
        OpenSearchEditDialog.setTabOrder(self.searchEdit, self.suggestionsEdit)
        OpenSearchEditDialog.setTabOrder(self.suggestionsEdit, self.buttonBox)

    def retranslateUi(self, OpenSearchEditDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenSearchEditDialog.setWindowTitle(_translate("OpenSearchEditDialog", "Edit search engine data"))
        self.label_2.setText(_translate("OpenSearchEditDialog", "&Name:"))
        self.nameEdit.setToolTip(_translate("OpenSearchEditDialog", "Shows the name of the search engine"))
        self.label_3.setText(_translate("OpenSearchEditDialog", "&Description:"))
        self.descriptionEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter a description"))
        self.label_5.setText(_translate("OpenSearchEditDialog", "&Image URL:"))
        self.imageEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter the URL of the image"))
        self.label_4.setText(_translate("OpenSearchEditDialog", "&Search URL Template:"))
        self.searchEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter the template of the search URL"))
        self.label_6.setText(_translate("OpenSearchEditDialog", "Su&ggestions URL Template:"))
        self.suggestionsEdit.setToolTip(_translate("OpenSearchEditDialog", "Enter the template of the suggestions URL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenSearchEditDialog = QtWidgets.QDialog()
    ui = Ui_OpenSearchEditDialog()
    ui.setupUi(OpenSearchEditDialog)
    OpenSearchEditDialog.show()
    sys.exit(app.exec_())

