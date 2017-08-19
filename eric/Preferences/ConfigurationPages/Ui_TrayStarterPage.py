# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\TrayStarterPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TrayStarterPage(object):
    def setupUi(self, TrayStarterPage):
        TrayStarterPage.setObjectName("TrayStarterPage")
        TrayStarterPage.resize(482, 473)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TrayStarterPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(TrayStarterPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line1 = QtWidgets.QFrame(TrayStarterPage)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setObjectName("line1")
        self.verticalLayout_2.addWidget(self.line1)
        self.groupBox = QtWidgets.QGroupBox(TrayStarterPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.standardButton = QtWidgets.QRadioButton(self.groupBox)
        self.standardButton.setObjectName("standardButton")
        self.verticalLayout.addWidget(self.standardButton)
        self.highContrastButton = QtWidgets.QRadioButton(self.groupBox)
        self.highContrastButton.setObjectName("highContrastButton")
        self.verticalLayout.addWidget(self.highContrastButton)
        self.blackWhiteButton = QtWidgets.QRadioButton(self.groupBox)
        self.blackWhiteButton.setObjectName("blackWhiteButton")
        self.verticalLayout.addWidget(self.blackWhiteButton)
        self.blackWhiteInverseButton = QtWidgets.QRadioButton(self.groupBox)
        self.blackWhiteInverseButton.setObjectName("blackWhiteInverseButton")
        self.verticalLayout.addWidget(self.blackWhiteInverseButton)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(464, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(TrayStarterPage)
        QtCore.QMetaObject.connectSlotsByName(TrayStarterPage)

    def retranslateUi(self, TrayStarterPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("TrayStarterPage", "<b>Configure Tray Starter</b>"))
        self.groupBox.setTitle(_translate("TrayStarterPage", "Icon"))
        self.standardButton.setToolTip(_translate("TrayStarterPage", "Select to use the standard icon"))
        self.standardButton.setText(_translate("TrayStarterPage", "Standard Icon"))
        self.highContrastButton.setToolTip(_translate("TrayStarterPage", "Select to use the high contrast icon"))
        self.highContrastButton.setText(_translate("TrayStarterPage", "High Contrast Icon"))
        self.blackWhiteButton.setToolTip(_translate("TrayStarterPage", "Select to use a black and white icon"))
        self.blackWhiteButton.setText(_translate("TrayStarterPage", "Black and White Icon"))
        self.blackWhiteInverseButton.setToolTip(_translate("TrayStarterPage", "Select to use an inverse black and white icon"))
        self.blackWhiteInverseButton.setText(_translate("TrayStarterPage", "Inverse Black and White Icon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrayStarterPage = QtWidgets.QWidget()
    ui = Ui_TrayStarterPage()
    ui.setupUi(TrayStarterPage)
    TrayStarterPage.show()
    sys.exit(app.exec_())

