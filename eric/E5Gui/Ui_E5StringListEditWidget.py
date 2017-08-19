# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\E5Gui\E5StringListEditWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_E5StringListEditWidget(object):
    def setupUi(self, E5StringListEditWidget):
        E5StringListEditWidget.setObjectName("E5StringListEditWidget")
        E5StringListEditWidget.resize(500, 300)
        E5StringListEditWidget.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(E5StringListEditWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.searchEdit = E5ClearableLineEdit(E5StringListEditWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchEdit.sizePolicy().hasHeightForWidth())
        self.searchEdit.setSizePolicy(sizePolicy)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setObjectName("searchEdit")
        self.gridLayout_4.addWidget(self.searchEdit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 4, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(E5StringListEditWidget)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout_5.addWidget(self.addButton, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(E5StringListEditWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_5.addWidget(self.line_3, 1, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(E5StringListEditWidget)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout_5.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(E5StringListEditWidget)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout_5.addWidget(self.removeAllButton, 3, 1, 1, 1)
        self.stringList = E5ListView(E5StringListEditWidget)
        self.stringList.setAlternatingRowColors(True)
        self.stringList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.stringList.setObjectName("stringList")
        self.gridLayout_5.addWidget(self.stringList, 0, 0, 5, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)

        self.retranslateUi(E5StringListEditWidget)
        QtCore.QMetaObject.connectSlotsByName(E5StringListEditWidget)

    def retranslateUi(self, E5StringListEditWidget):
        _translate = QtCore.QCoreApplication.translate
        self.searchEdit.setToolTip(_translate("E5StringListEditWidget", "Enter search term for strings"))
        self.addButton.setToolTip(_translate("E5StringListEditWidget", "Press to add an entry"))
        self.addButton.setText(_translate("E5StringListEditWidget", "&Add..."))
        self.removeButton.setToolTip(_translate("E5StringListEditWidget", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("E5StringListEditWidget", "&Remove"))
        self.removeAllButton.setToolTip(_translate("E5StringListEditWidget", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("E5StringListEditWidget", "R&emove All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5ListView import E5ListView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    E5StringListEditWidget = QtWidgets.QWidget()
    ui = Ui_E5StringListEditWidget()
    ui.setupUi(E5StringListEditWidget)
    E5StringListEditWidget.show()
    sys.exit(app.exec_())

