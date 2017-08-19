# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\ConfigurationPage\SubversionPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SubversionPage(object):
    def setupUi(self, SubversionPage):
        SubversionPage.setObjectName("SubversionPage")
        SubversionPage.resize(402, 384)
        self.vboxlayout = QtWidgets.QVBoxLayout(SubversionPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(SubversionPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line15 = QtWidgets.QFrame(SubversionPage)
        self.line15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line15.setObjectName("line15")
        self.vboxlayout.addWidget(self.line15)
        self.groupBox = QtWidgets.QGroupBox(SubversionPage)
        self.groupBox.setObjectName("groupBox")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.logSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.logSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.logSpinBox.setMaximum(999999)
        self.logSpinBox.setObjectName("logSpinBox")
        self.hboxlayout.addWidget(self.logSpinBox)
        spacerItem = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(SubversionPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.hboxlayout1 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.hboxlayout1.addWidget(self.label_2)
        self.commitSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.commitSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.commitSpinBox.setMinimum(1)
        self.commitSpinBox.setMaximum(100)
        self.commitSpinBox.setObjectName("commitSpinBox")
        self.hboxlayout1.addWidget(self.commitSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout.addWidget(self.groupBox_2)
        self.configButton = QtWidgets.QPushButton(SubversionPage)
        self.configButton.setObjectName("configButton")
        self.vboxlayout.addWidget(self.configButton)
        self.serversButton = QtWidgets.QPushButton(SubversionPage)
        self.serversButton.setObjectName("serversButton")
        self.vboxlayout.addWidget(self.serversButton)
        spacerItem2 = QtWidgets.QSpacerItem(388, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.retranslateUi(SubversionPage)
        QtCore.QMetaObject.connectSlotsByName(SubversionPage)

    def retranslateUi(self, SubversionPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("SubversionPage", "<b>Configure Subversion Interface</b>"))
        self.groupBox.setTitle(_translate("SubversionPage", "Log"))
        self.label.setText(_translate("SubversionPage", "No. of log messages shown:"))
        self.logSpinBox.setToolTip(_translate("SubversionPage", "Enter the number of log messages to be shown"))
        self.groupBox_2.setTitle(_translate("SubversionPage", "Commit"))
        self.label_2.setText(_translate("SubversionPage", "No. of commit messages to remember:"))
        self.commitSpinBox.setToolTip(_translate("SubversionPage", "Enter the number of commit messages to remember"))
        self.configButton.setToolTip(_translate("SubversionPage", "Edit the subversion config file"))
        self.configButton.setText(_translate("SubversionPage", "Edit config file"))
        self.serversButton.setToolTip(_translate("SubversionPage", "Edit the subversion servers file"))
        self.serversButton.setText(_translate("SubversionPage", "Edit servers file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubversionPage = QtWidgets.QWidget()
    ui = Ui_SubversionPage()
    ui.setupUi(SubversionPage)
    SubversionPage.show()
    sys.exit(app.exec_())

