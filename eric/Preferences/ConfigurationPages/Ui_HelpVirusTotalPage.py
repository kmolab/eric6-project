# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\HelpVirusTotalPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelpVirusTotalPage(object):
    def setupUi(self, HelpVirusTotalPage):
        HelpVirusTotalPage.setObjectName("HelpVirusTotalPage")
        HelpVirusTotalPage.resize(485, 409)
        HelpVirusTotalPage.setWindowTitle("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(HelpVirusTotalPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(HelpVirusTotalPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line17 = QtWidgets.QFrame(HelpVirusTotalPage)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setObjectName("line17")
        self.verticalLayout_2.addWidget(self.line17)
        self.vtEnabledCheckBox = QtWidgets.QCheckBox(HelpVirusTotalPage)
        self.vtEnabledCheckBox.setObjectName("vtEnabledCheckBox")
        self.verticalLayout_2.addWidget(self.vtEnabledCheckBox)
        self.groupBox = QtWidgets.QGroupBox(HelpVirusTotalPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.vtServiceKeyEdit = QtWidgets.QLineEdit(self.groupBox)
        self.vtServiceKeyEdit.setToolTip("")
        self.vtServiceKeyEdit.setObjectName("vtServiceKeyEdit")
        self.verticalLayout.addWidget(self.vtServiceKeyEdit)
        self.testResultLabel = QtWidgets.QLabel(self.groupBox)
        self.testResultLabel.setText("")
        self.testResultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.testResultLabel.setWordWrap(True)
        self.testResultLabel.setObjectName("testResultLabel")
        self.verticalLayout.addWidget(self.testResultLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.testButton = QtWidgets.QPushButton(self.groupBox)
        self.testButton.setEnabled(False)
        self.testButton.setObjectName("testButton")
        self.horizontalLayout.addWidget(self.testButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.vtSecureCheckBox = QtWidgets.QCheckBox(HelpVirusTotalPage)
        self.vtSecureCheckBox.setObjectName("vtSecureCheckBox")
        self.verticalLayout_2.addWidget(self.vtSecureCheckBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)

        self.retranslateUi(HelpVirusTotalPage)
        QtCore.QMetaObject.connectSlotsByName(HelpVirusTotalPage)
        HelpVirusTotalPage.setTabOrder(self.vtEnabledCheckBox, self.vtServiceKeyEdit)
        HelpVirusTotalPage.setTabOrder(self.vtServiceKeyEdit, self.testButton)
        HelpVirusTotalPage.setTabOrder(self.testButton, self.vtSecureCheckBox)

    def retranslateUi(self, HelpVirusTotalPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("HelpVirusTotalPage", "<b>Configure VirusTotal Interface</b>"))
        self.vtEnabledCheckBox.setToolTip(_translate("HelpVirusTotalPage", "Select to enable the VirusTotal interface"))
        self.vtEnabledCheckBox.setText(_translate("HelpVirusTotalPage", "Enable VirusTotal"))
        self.groupBox.setTitle(_translate("HelpVirusTotalPage", "Service Key"))
        self.label.setText(_translate("HelpVirusTotalPage", "Enter your personal VirusTotal service key (s. <a href=\"http://virustotal.com\">VirusTotal &copy;</a> for details):"))
        self.testButton.setText(_translate("HelpVirusTotalPage", "Test Service Key"))
        self.vtSecureCheckBox.setToolTip(_translate("HelpVirusTotalPage", "Select to use secure (https) connections"))
        self.vtSecureCheckBox.setText(_translate("HelpVirusTotalPage", "Use secure (https) connections"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpVirusTotalPage = QtWidgets.QWidget()
    ui = Ui_HelpVirusTotalPage()
    ui.setupUi(HelpVirusTotalPage)
    HelpVirusTotalPage.show()
    sys.exit(app.exec_())

