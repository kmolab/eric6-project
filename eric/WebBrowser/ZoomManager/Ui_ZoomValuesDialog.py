# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\ZoomManager\ZoomValuesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZoomValuesDialog(object):
    def setupUi(self, ZoomValuesDialog):
        ZoomValuesDialog.setObjectName("ZoomValuesDialog")
        ZoomValuesDialog.resize(500, 350)
        ZoomValuesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ZoomValuesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(ZoomValuesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.zoomValuesTable = E5TableView(ZoomValuesDialog)
        self.zoomValuesTable.setAlternatingRowColors(True)
        self.zoomValuesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.zoomValuesTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.zoomValuesTable.setShowGrid(False)
        self.zoomValuesTable.setSortingEnabled(True)
        self.zoomValuesTable.setObjectName("zoomValuesTable")
        self.verticalLayout.addWidget(self.zoomValuesTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.removeButton = QtWidgets.QPushButton(ZoomValuesDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.removeAllButton = QtWidgets.QPushButton(ZoomValuesDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.horizontalLayout_3.addWidget(self.removeAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(ZoomValuesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ZoomValuesDialog)
        self.buttonBox.accepted.connect(ZoomValuesDialog.accept)
        self.buttonBox.rejected.connect(ZoomValuesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ZoomValuesDialog)
        ZoomValuesDialog.setTabOrder(self.searchEdit, self.zoomValuesTable)
        ZoomValuesDialog.setTabOrder(self.zoomValuesTable, self.removeButton)
        ZoomValuesDialog.setTabOrder(self.removeButton, self.removeAllButton)
        ZoomValuesDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, ZoomValuesDialog):
        _translate = QtCore.QCoreApplication.translate
        ZoomValuesDialog.setWindowTitle(_translate("ZoomValuesDialog", "Saved Zoom Values"))
        self.searchEdit.setToolTip(_translate("ZoomValuesDialog", "Enter search term"))
        self.removeButton.setToolTip(_translate("ZoomValuesDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("ZoomValuesDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("ZoomValuesDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("ZoomValuesDialog", "Remove &All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TableView import E5TableView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ZoomValuesDialog = QtWidgets.QDialog()
    ui = Ui_ZoomValuesDialog()
    ui.setupUi(ZoomValuesDialog)
    ZoomValuesDialog.show()
    sys.exit(app.exec_())

