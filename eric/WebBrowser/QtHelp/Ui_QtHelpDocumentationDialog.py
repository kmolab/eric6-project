# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\QtHelp\QtHelpDocumentationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QtHelpDocumentationDialog(object):
    def setupUi(self, QtHelpDocumentationDialog):
        QtHelpDocumentationDialog.setObjectName("QtHelpDocumentationDialog")
        QtHelpDocumentationDialog.resize(500, 450)
        QtHelpDocumentationDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QtHelpDocumentationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(QtHelpDocumentationDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.documentsList = QtWidgets.QListWidget(QtHelpDocumentationDialog)
        self.documentsList.setAlternatingRowColors(True)
        self.documentsList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.documentsList.setObjectName("documentsList")
        self.gridLayout.addWidget(self.documentsList, 0, 0, 6, 1)
        self.addButton = QtWidgets.QPushButton(QtHelpDocumentationDialog)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.addPluginButton = QtWidgets.QPushButton(QtHelpDocumentationDialog)
        self.addPluginButton.setObjectName("addPluginButton")
        self.gridLayout.addWidget(self.addPluginButton, 1, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(QtHelpDocumentationDialog)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(QtHelpDocumentationDialog)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)
        self.managePluginButton = QtWidgets.QPushButton(QtHelpDocumentationDialog)
        self.managePluginButton.setObjectName("managePluginButton")
        self.gridLayout.addWidget(self.managePluginButton, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(QtHelpDocumentationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QtHelpDocumentationDialog)
        self.buttonBox.accepted.connect(QtHelpDocumentationDialog.accept)
        self.buttonBox.rejected.connect(QtHelpDocumentationDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QtHelpDocumentationDialog)
        QtHelpDocumentationDialog.setTabOrder(self.documentsList, self.addButton)
        QtHelpDocumentationDialog.setTabOrder(self.addButton, self.addPluginButton)
        QtHelpDocumentationDialog.setTabOrder(self.addPluginButton, self.removeButton)

    def retranslateUi(self, QtHelpDocumentationDialog):
        _translate = QtCore.QCoreApplication.translate
        QtHelpDocumentationDialog.setWindowTitle(_translate("QtHelpDocumentationDialog", "Manage QtHelp Documentation Database"))
        self.label.setText(_translate("QtHelpDocumentationDialog", "Registered Documents"))
        self.documentsList.setSortingEnabled(True)
        self.addButton.setToolTip(_translate("QtHelpDocumentationDialog", "Press to select QtHelp documents to add to the database"))
        self.addButton.setText(_translate("QtHelpDocumentationDialog", "Add..."))
        self.addPluginButton.setToolTip(_translate("QtHelpDocumentationDialog", "Press to select QtHelp documents provided by a plug-in to add to the database"))
        self.addPluginButton.setText(_translate("QtHelpDocumentationDialog", "Add from Plug-ins..."))
        self.removeButton.setToolTip(_translate("QtHelpDocumentationDialog", "Press to remove the selected documents from the database"))
        self.removeButton.setText(_translate("QtHelpDocumentationDialog", "Remove"))
        self.managePluginButton.setToolTip(_translate("QtHelpDocumentationDialog", "Select to manage the plug-in provided documentation sets"))
        self.managePluginButton.setText(_translate("QtHelpDocumentationDialog", "Manage Plug-ins..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtHelpDocumentationDialog = QtWidgets.QDialog()
    ui = Ui_QtHelpDocumentationDialog()
    ui.setupUi(QtHelpDocumentationDialog)
    QtHelpDocumentationDialog.show()
    sys.exit(app.exec_())

