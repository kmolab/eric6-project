# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\WebPlugins\ClickToFlash\ClickToFlash.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClickToFlash(object):
    def setupUi(self, ClickToFlash):
        ClickToFlash.setObjectName("ClickToFlash")
        ClickToFlash.resize(200, 200)
        self.gridLayout = QtWidgets.QGridLayout(ClickToFlash)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.loadFlashButton = QtWidgets.QToolButton(ClickToFlash)
        self.loadFlashButton.setIconSize(QtCore.QSize(128, 128))
        self.loadFlashButton.setObjectName("loadFlashButton")
        self.gridLayout.addWidget(self.loadFlashButton, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)

        self.retranslateUi(ClickToFlash)
        QtCore.QMetaObject.connectSlotsByName(ClickToFlash)

    def retranslateUi(self, ClickToFlash):
        _translate = QtCore.QCoreApplication.translate
        self.loadFlashButton.setToolTip(_translate("ClickToFlash", "Press to activate the content; context menu for more options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClickToFlash = QtWidgets.QWidget()
    ui = Ui_ClickToFlash()
    ui.setupUi(ClickToFlash)
    ClickToFlash.show()
    sys.exit(app.exec_())

