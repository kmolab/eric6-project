# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\NotificationsPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NotificationsPage(object):
    def setupUi(self, NotificationsPage):
        NotificationsPage.setObjectName("NotificationsPage")
        NotificationsPage.resize(507, 300)
        NotificationsPage.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(NotificationsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(NotificationsPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line11 = QtWidgets.QFrame(NotificationsPage)
        self.line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11.setObjectName("line11")
        self.verticalLayout.addWidget(self.line11)
        self.enableCheckBox = QtWidgets.QCheckBox(NotificationsPage)
        self.enableCheckBox.setObjectName("enableCheckBox")
        self.verticalLayout.addWidget(self.enableCheckBox)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(NotificationsPage)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.timeoutSpinBox = QtWidgets.QSpinBox(NotificationsPage)
        self.timeoutSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeoutSpinBox.setMinimum(1)
        self.timeoutSpinBox.setMaximum(10)
        self.timeoutSpinBox.setObjectName("timeoutSpinBox")
        self.gridLayout_2.addWidget(self.timeoutSpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(NotificationsPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.xSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.xSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.xSpinBox.setMinimum(-10000)
        self.xSpinBox.setMaximum(10000)
        self.xSpinBox.setObjectName("xSpinBox")
        self.gridLayout.addWidget(self.xSpinBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.ySpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.ySpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ySpinBox.setMinimum(-10000)
        self.ySpinBox.setMaximum(10000)
        self.ySpinBox.setObjectName("ySpinBox")
        self.gridLayout.addWidget(self.ySpinBox, 0, 3, 1, 1)
        self.visualButton = QtWidgets.QPushButton(self.groupBox)
        self.visualButton.setCheckable(True)
        self.visualButton.setObjectName("visualButton")
        self.gridLayout.addWidget(self.visualButton, 1, 0, 1, 4)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 142, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(NotificationsPage)
        QtCore.QMetaObject.connectSlotsByName(NotificationsPage)
        NotificationsPage.setTabOrder(self.enableCheckBox, self.timeoutSpinBox)
        NotificationsPage.setTabOrder(self.timeoutSpinBox, self.xSpinBox)
        NotificationsPage.setTabOrder(self.xSpinBox, self.ySpinBox)
        NotificationsPage.setTabOrder(self.ySpinBox, self.visualButton)

    def retranslateUi(self, NotificationsPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("NotificationsPage", "<b>Configure notification settings</b>"))
        self.enableCheckBox.setToolTip(_translate("NotificationsPage", "Select to enable notifications"))
        self.enableCheckBox.setText(_translate("NotificationsPage", "Enable Notifications"))
        self.label.setText(_translate("NotificationsPage", "Auto Close Timeout:"))
        self.timeoutSpinBox.setToolTip(_translate("NotificationsPage", "Enter the timeout for closing the notification"))
        self.timeoutSpinBox.setSuffix(_translate("NotificationsPage", " s"))
        self.groupBox.setTitle(_translate("NotificationsPage", "Position"))
        self.label_2.setText(_translate("NotificationsPage", "X:"))
        self.xSpinBox.setToolTip(_translate("NotificationsPage", "Enter the X-position the notification should be shown at"))
        self.label_3.setText(_translate("NotificationsPage", "Y:"))
        self.ySpinBox.setToolTip(_translate("NotificationsPage", "Enter the Y-position the notification should be shown at"))
        self.visualButton.setToolTip(_translate("NotificationsPage", "Press to select the position visually, release to get it"))
        self.visualButton.setText(_translate("NotificationsPage", "Visual Selection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NotificationsPage = QtWidgets.QWidget()
    ui = Ui_NotificationsPage()
    ui.setupUi(NotificationsPage)
    NotificationsPage.show()
    sys.exit(app.exec_())

