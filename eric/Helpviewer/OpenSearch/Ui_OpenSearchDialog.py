# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\OpenSearch\OpenSearchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenSearchDialog(object):
    def setupUi(self, OpenSearchDialog):
        OpenSearchDialog.setObjectName("OpenSearchDialog")
        OpenSearchDialog.resize(650, 350)
        OpenSearchDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenSearchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.enginesTable = E5TableView(OpenSearchDialog)
        self.enginesTable.setAlternatingRowColors(True)
        self.enginesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.enginesTable.setShowGrid(False)
        self.enginesTable.setObjectName("enginesTable")
        self.gridLayout.addWidget(self.enginesTable, 0, 0, 5, 1)
        self.addButton = QtWidgets.QPushButton(OpenSearchDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(OpenSearchDialog)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 1, 1, 1, 1)
        self.editButton = QtWidgets.QPushButton(OpenSearchDialog)
        self.editButton.setAutoDefault(False)
        self.editButton.setObjectName("editButton")
        self.gridLayout.addWidget(self.editButton, 2, 1, 1, 1)
        self.restoreButton = QtWidgets.QPushButton(OpenSearchDialog)
        self.restoreButton.setAutoDefault(False)
        self.restoreButton.setObjectName("restoreButton")
        self.gridLayout.addWidget(self.restoreButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 38, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpenSearchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OpenSearchDialog)
        self.buttonBox.accepted.connect(OpenSearchDialog.accept)
        self.buttonBox.rejected.connect(OpenSearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenSearchDialog)
        OpenSearchDialog.setTabOrder(self.enginesTable, self.addButton)
        OpenSearchDialog.setTabOrder(self.addButton, self.deleteButton)
        OpenSearchDialog.setTabOrder(self.deleteButton, self.editButton)
        OpenSearchDialog.setTabOrder(self.editButton, self.restoreButton)
        OpenSearchDialog.setTabOrder(self.restoreButton, self.buttonBox)

    def retranslateUi(self, OpenSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenSearchDialog.setWindowTitle(_translate("OpenSearchDialog", "Open Search Engines Configuration"))
        self.addButton.setToolTip(_translate("OpenSearchDialog", "Press to add a new search engine from file"))
        self.addButton.setText(_translate("OpenSearchDialog", "&Add..."))
        self.deleteButton.setToolTip(_translate("OpenSearchDialog", "Press to delete the selected engines"))
        self.deleteButton.setText(_translate("OpenSearchDialog", "&Delete"))
        self.editButton.setToolTip(_translate("OpenSearchDialog", "Press to edit the data of the current engine"))
        self.editButton.setText(_translate("OpenSearchDialog", "Edit..."))
        self.restoreButton.setToolTip(_translate("OpenSearchDialog", "Press to restore the default engines"))
        self.restoreButton.setText(_translate("OpenSearchDialog", "&Restore Defaults"))

from E5Gui.E5TableView import E5TableView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenSearchDialog = QtWidgets.QDialog()
    ui = Ui_OpenSearchDialog()
    ui.setupUi(OpenSearchDialog)
    OpenSearchDialog.show()
    sys.exit(app.exec_())

