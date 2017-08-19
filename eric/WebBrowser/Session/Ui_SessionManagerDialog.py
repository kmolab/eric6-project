# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Session\SessionManagerDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SessionManagerDialog(object):
    def setupUi(self, SessionManagerDialog):
        SessionManagerDialog.setObjectName("SessionManagerDialog")
        SessionManagerDialog.resize(500, 400)
        SessionManagerDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(SessionManagerDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.sessionsList = QtWidgets.QTreeWidget(SessionManagerDialog)
        self.sessionsList.setAlternatingRowColors(True)
        self.sessionsList.setRootIsDecorated(False)
        self.sessionsList.setObjectName("sessionsList")
        self.gridLayout.addWidget(self.sessionsList, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.newButton = QtWidgets.QPushButton(SessionManagerDialog)
        self.newButton.setObjectName("newButton")
        self.verticalLayout.addWidget(self.newButton)
        self.renameButton = QtWidgets.QPushButton(SessionManagerDialog)
        self.renameButton.setObjectName("renameButton")
        self.verticalLayout.addWidget(self.renameButton)
        self.cloneButton = QtWidgets.QPushButton(SessionManagerDialog)
        self.cloneButton.setObjectName("cloneButton")
        self.verticalLayout.addWidget(self.cloneButton)
        self.deleteButton = QtWidgets.QPushButton(SessionManagerDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        self.switchButton = QtWidgets.QPushButton(SessionManagerDialog)
        self.switchButton.setObjectName("switchButton")
        self.verticalLayout.addWidget(self.switchButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SessionManagerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(SessionManagerDialog)
        self.buttonBox.accepted.connect(SessionManagerDialog.accept)
        self.buttonBox.rejected.connect(SessionManagerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SessionManagerDialog)

    def retranslateUi(self, SessionManagerDialog):
        _translate = QtCore.QCoreApplication.translate
        SessionManagerDialog.setWindowTitle(_translate("SessionManagerDialog", "Session Manager"))
        self.sessionsList.setToolTip(_translate("SessionManagerDialog", "Shows a list of available sessions"))
        self.sessionsList.headerItem().setText(0, _translate("SessionManagerDialog", "Session"))
        self.sessionsList.headerItem().setText(1, _translate("SessionManagerDialog", "Last Modified"))
        self.newButton.setToolTip(_translate("SessionManagerDialog", "Press to create a new session"))
        self.newButton.setText(_translate("SessionManagerDialog", "New"))
        self.renameButton.setToolTip(_translate("SessionManagerDialog", "Press to rename the selected session"))
        self.renameButton.setText(_translate("SessionManagerDialog", "Rename"))
        self.cloneButton.setToolTip(_translate("SessionManagerDialog", "Press to clone the selected session"))
        self.cloneButton.setText(_translate("SessionManagerDialog", "Clone"))
        self.deleteButton.setToolTip(_translate("SessionManagerDialog", "Press to delete the selected session"))
        self.deleteButton.setText(_translate("SessionManagerDialog", "Delete"))
        self.switchButton.setToolTip(_translate("SessionManagerDialog", "Press to switch to the selected session"))
        self.switchButton.setText(_translate("SessionManagerDialog", "Switch To"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SessionManagerDialog = QtWidgets.QDialog()
    ui = Ui_SessionManagerDialog()
    ui.setupUi(SessionManagerDialog)
    SessionManagerDialog.show()
    sys.exit(app.exec_())

