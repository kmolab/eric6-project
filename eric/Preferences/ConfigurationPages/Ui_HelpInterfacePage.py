# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\HelpInterfacePage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpInterfacePage(object):
    def setupUi(self, HelpInterfacePage):
        HelpInterfacePage.setObjectName("HelpInterfacePage")
        HelpInterfacePage.resize(557, 152)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpInterfacePage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(HelpInterfacePage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line9 = QtWidgets.QFrame(HelpInterfacePage)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setObjectName("line9")
        self.verticalLayout.addWidget(self.line9)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(HelpInterfacePage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.styleComboBox = QtWidgets.QComboBox(HelpInterfacePage)
        self.styleComboBox.setObjectName("styleComboBox")
        self.gridLayout.addWidget(self.styleComboBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HelpInterfacePage)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.styleSheetPicker = E5PathPicker(HelpInterfacePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.styleSheetPicker.sizePolicy().hasHeightForWidth())
        self.styleSheetPicker.setSizePolicy(sizePolicy)
        self.styleSheetPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.styleSheetPicker.setObjectName("styleSheetPicker")
        self.gridLayout.addWidget(self.styleSheetPicker, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(537, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(HelpInterfacePage)
        QtCore.QMetaObject.connectSlotsByName(HelpInterfacePage)

    def retranslateUi(self, HelpInterfacePage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("HelpInterfacePage", "<b>Configure User Interface</b>"))
        self.label_2.setText(_translate("HelpInterfacePage", "Style:"))
        self.styleComboBox.setToolTip(_translate("HelpInterfacePage", "Select the interface style"))
        self.label_3.setText(_translate("HelpInterfacePage", "Style Sheet:"))
        self.styleSheetPicker.setToolTip(_translate("HelpInterfacePage", "Enter the name of the style sheet file"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpInterfacePage = QtWidgets.QWidget()
    ui = Ui_HelpInterfacePage()
    ui.setupUi(HelpInterfacePage)
    HelpInterfacePage.show()
    sys.exit(app.exec_())

