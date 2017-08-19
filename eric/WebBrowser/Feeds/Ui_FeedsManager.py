# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Feeds\FeedsManager.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FeedsManager(object):
    def setupUi(self, FeedsManager):
        FeedsManager.setObjectName("FeedsManager")
        FeedsManager.resize(750, 500)
        FeedsManager.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(FeedsManager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.feedsTree = QtWidgets.QTreeWidget(FeedsManager)
        self.feedsTree.setAlternatingRowColors(True)
        self.feedsTree.setAllColumnsShowFocus(True)
        self.feedsTree.setWordWrap(True)
        self.feedsTree.setObjectName("feedsTree")
        self.feedsTree.header().setVisible(False)
        self.verticalLayout.addWidget(self.feedsTree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reloadAllButton = QtWidgets.QPushButton(FeedsManager)
        self.reloadAllButton.setAutoDefault(False)
        self.reloadAllButton.setObjectName("reloadAllButton")
        self.horizontalLayout.addWidget(self.reloadAllButton)
        self.reloadButton = QtWidgets.QPushButton(FeedsManager)
        self.reloadButton.setAutoDefault(False)
        self.reloadButton.setObjectName("reloadButton")
        self.horizontalLayout.addWidget(self.reloadButton)
        self.editButton = QtWidgets.QPushButton(FeedsManager)
        self.editButton.setAutoDefault(False)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(FeedsManager)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(FeedsManager)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FeedsManager)
        self.buttonBox.accepted.connect(FeedsManager.accept)
        self.buttonBox.rejected.connect(FeedsManager.reject)
        QtCore.QMetaObject.connectSlotsByName(FeedsManager)
        FeedsManager.setTabOrder(self.feedsTree, self.reloadAllButton)
        FeedsManager.setTabOrder(self.reloadAllButton, self.reloadButton)
        FeedsManager.setTabOrder(self.reloadButton, self.editButton)
        FeedsManager.setTabOrder(self.editButton, self.deleteButton)
        FeedsManager.setTabOrder(self.deleteButton, self.buttonBox)

    def retranslateUi(self, FeedsManager):
        _translate = QtCore.QCoreApplication.translate
        FeedsManager.setWindowTitle(_translate("FeedsManager", "Feeds Manager"))
        self.feedsTree.headerItem().setText(0, _translate("FeedsManager", "News"))
        self.reloadAllButton.setToolTip(_translate("FeedsManager", "Press to reload all feeds"))
        self.reloadAllButton.setText(_translate("FeedsManager", "Reload &All"))
        self.reloadButton.setToolTip(_translate("FeedsManager", "Press to reload the selected feed"))
        self.reloadButton.setText(_translate("FeedsManager", "&Reload"))
        self.editButton.setToolTip(_translate("FeedsManager", "Press to edit the selected feed"))
        self.editButton.setText(_translate("FeedsManager", "&Edit Feed"))
        self.deleteButton.setToolTip(_translate("FeedsManager", "Press to delete the selected feed"))
        self.deleteButton.setText(_translate("FeedsManager", "&Delete Feed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FeedsManager = QtWidgets.QDialog()
    ui = Ui_FeedsManager()
    ui.setupUi(FeedsManager)
    FeedsManager.show()
    sys.exit(app.exec_())

