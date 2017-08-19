# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\HelpViewersPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpViewersPage(object):
    def setupUi(self, HelpViewersPage):
        HelpViewersPage.setObjectName("HelpViewersPage")
        HelpViewersPage.resize(613, 634)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(HelpViewersPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headerLabel = QtWidgets.QLabel(HelpViewersPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_3.addWidget(self.headerLabel)
        self.line17 = QtWidgets.QFrame(HelpViewersPage)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setObjectName("line17")
        self.verticalLayout_3.addWidget(self.line17)
        self.groupBox = QtWidgets.QGroupBox(HelpViewersPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.helpBrowserButton = QtWidgets.QRadioButton(self.groupBox)
        self.helpBrowserButton.setChecked(True)
        self.helpBrowserButton.setObjectName("helpBrowserButton")
        self.gridLayout.addWidget(self.helpBrowserButton, 0, 0, 1, 1)
        self.qtAssistantButton = QtWidgets.QRadioButton(self.groupBox)
        self.qtAssistantButton.setObjectName("qtAssistantButton")
        self.gridLayout.addWidget(self.qtAssistantButton, 0, 1, 1, 1)
        self.webBrowserButton = QtWidgets.QRadioButton(self.groupBox)
        self.webBrowserButton.setObjectName("webBrowserButton")
        self.gridLayout.addWidget(self.webBrowserButton, 0, 2, 1, 1)
        self.customViewerButton = QtWidgets.QRadioButton(self.groupBox)
        self.customViewerButton.setObjectName("customViewerButton")
        self.gridLayout.addWidget(self.customViewerButton, 0, 3, 1, 1)
        self.customViewerPicker = E5PathPicker(self.groupBox)
        self.customViewerPicker.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customViewerPicker.sizePolicy().hasHeightForWidth())
        self.customViewerPicker.setSizePolicy(sizePolicy)
        self.customViewerPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.customViewerPicker.setObjectName("customViewerPicker")
        self.gridLayout.addWidget(self.customViewerPicker, 1, 0, 1, 4)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(479, 121, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(HelpViewersPage)
        self.customViewerButton.toggled['bool'].connect(self.customViewerPicker.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(HelpViewersPage)
        HelpViewersPage.setTabOrder(self.helpBrowserButton, self.qtAssistantButton)
        HelpViewersPage.setTabOrder(self.qtAssistantButton, self.webBrowserButton)
        HelpViewersPage.setTabOrder(self.webBrowserButton, self.customViewerButton)

    def retranslateUi(self, HelpViewersPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("HelpViewersPage", "<b>Configure help viewers</b>"))
        self.groupBox.setTitle(_translate("HelpViewersPage", "Help Viewer"))
        self.helpBrowserButton.setToolTip(_translate("HelpViewersPage", "Select to use the Eric Web Browser"))
        self.helpBrowserButton.setText(_translate("HelpViewersPage", "Eric Web Browser"))
        self.qtAssistantButton.setToolTip(_translate("HelpViewersPage", "Select to use Qt Assistant"))
        self.qtAssistantButton.setText(_translate("HelpViewersPage", "Qt Assistant"))
        self.webBrowserButton.setToolTip(_translate("HelpViewersPage", "Select to use the configured web browser of the system"))
        self.webBrowserButton.setText(_translate("HelpViewersPage", "System Web Browser"))
        self.customViewerButton.setToolTip(_translate("HelpViewersPage", "Select to use a custom viewer"))
        self.customViewerButton.setText(_translate("HelpViewersPage", "Custom"))
        self.customViewerPicker.setToolTip(_translate("HelpViewersPage", "Enter the custom viewer to be used"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpViewersPage = QtWidgets.QWidget()
    ui = Ui_HelpViewersPage()
    ui.setupUi(HelpViewersPage)
    HelpViewersPage.show()
    sys.exit(app.exec_())

