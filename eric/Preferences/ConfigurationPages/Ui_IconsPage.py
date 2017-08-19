# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\IconsPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IconsPage(object):
    def setupUi(self, IconsPage):
        IconsPage.setObjectName("IconsPage")
        IconsPage.resize(539, 371)
        self.gridLayout = QtWidgets.QGridLayout(IconsPage)
        self.gridLayout.setObjectName("gridLayout")
        self.headerLabel = QtWidgets.QLabel(IconsPage)
        self.headerLabel.setObjectName("headerLabel")
        self.gridLayout.addWidget(self.headerLabel, 0, 0, 1, 2)
        self.line10 = QtWidgets.QFrame(IconsPage)
        self.line10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line10.setObjectName("line10")
        self.gridLayout.addWidget(self.line10, 1, 0, 1, 2)
        self.TextLabel1_2_2_2_2 = QtWidgets.QLabel(IconsPage)
        self.TextLabel1_2_2_2_2.setObjectName("TextLabel1_2_2_2_2")
        self.gridLayout.addWidget(self.TextLabel1_2_2_2_2, 2, 0, 1, 2)
        self.iconDirectoryList = QtWidgets.QListWidget(IconsPage)
        self.iconDirectoryList.setAlternatingRowColors(True)
        self.iconDirectoryList.setObjectName("iconDirectoryList")
        self.gridLayout.addWidget(self.iconDirectoryList, 3, 0, 1, 1)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 209, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.upButton = QtWidgets.QPushButton(IconsPage)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName("upButton")
        self.vboxlayout.addWidget(self.upButton)
        self.downButton = QtWidgets.QPushButton(IconsPage)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName("downButton")
        self.vboxlayout.addWidget(self.downButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.vboxlayout, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteIconDirectoryButton = QtWidgets.QPushButton(IconsPage)
        self.deleteIconDirectoryButton.setEnabled(False)
        self.deleteIconDirectoryButton.setObjectName("deleteIconDirectoryButton")
        self.horizontalLayout.addWidget(self.deleteIconDirectoryButton)
        self.addIconDirectoryButton = QtWidgets.QPushButton(IconsPage)
        self.addIconDirectoryButton.setEnabled(False)
        self.addIconDirectoryButton.setObjectName("addIconDirectoryButton")
        self.horizontalLayout.addWidget(self.addIconDirectoryButton)
        self.iconDirectoryPicker = E5PathPicker(IconsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconDirectoryPicker.sizePolicy().hasHeightForWidth())
        self.iconDirectoryPicker.setSizePolicy(sizePolicy)
        self.iconDirectoryPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.iconDirectoryPicker.setObjectName("iconDirectoryPicker")
        self.horizontalLayout.addWidget(self.iconDirectoryPicker)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.showIconsButton = QtWidgets.QPushButton(IconsPage)
        self.showIconsButton.setEnabled(False)
        self.showIconsButton.setObjectName("showIconsButton")
        self.gridLayout.addWidget(self.showIconsButton, 4, 1, 1, 1)

        self.retranslateUi(IconsPage)
        QtCore.QMetaObject.connectSlotsByName(IconsPage)
        IconsPage.setTabOrder(self.iconDirectoryList, self.upButton)
        IconsPage.setTabOrder(self.upButton, self.downButton)
        IconsPage.setTabOrder(self.downButton, self.deleteIconDirectoryButton)
        IconsPage.setTabOrder(self.deleteIconDirectoryButton, self.addIconDirectoryButton)
        IconsPage.setTabOrder(self.addIconDirectoryButton, self.iconDirectoryPicker)
        IconsPage.setTabOrder(self.iconDirectoryPicker, self.showIconsButton)

    def retranslateUi(self, IconsPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("IconsPage", "<b>Configure icon directories</b>"))
        self.TextLabel1_2_2_2_2.setText(_translate("IconsPage", "<font color=\"#FF0000\"><b>Note:</b> These settings are activated at the next startup of the application.</font>"))
        self.iconDirectoryList.setToolTip(_translate("IconsPage", "List of icon directories"))
        self.upButton.setText(_translate("IconsPage", "Up"))
        self.downButton.setText(_translate("IconsPage", "Down"))
        self.deleteIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to delete the selected directory from the list"))
        self.deleteIconDirectoryButton.setText(_translate("IconsPage", "Delete"))
        self.addIconDirectoryButton.setToolTip(_translate("IconsPage", "Press to add the entered directory to the list"))
        self.addIconDirectoryButton.setText(_translate("IconsPage", "Add"))
        self.showIconsButton.setText(_translate("IconsPage", "Show"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IconsPage = QtWidgets.QWidget()
    ui = Ui_IconsPage()
    ui.setupUi(IconsPage)
    IconsPage.show()
    sys.exit(app.exec_())

