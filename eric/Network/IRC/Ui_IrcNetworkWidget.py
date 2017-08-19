# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Network\IRC\IrcNetworkWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IrcNetworkWidget(object):
    def setupUi(self, IrcNetworkWidget):
        IrcNetworkWidget.setObjectName("IrcNetworkWidget")
        IrcNetworkWidget.resize(400, 322)
        IrcNetworkWidget.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(IrcNetworkWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messages = QtWidgets.QTextBrowser(IrcNetworkWidget)
        self.messages.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.messages.setTabChangesFocus(True)
        self.messages.setOpenLinks(False)
        self.messages.setObjectName("messages")
        self.verticalLayout.addWidget(self.messages)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.networkCombo = QtWidgets.QComboBox(IrcNetworkWidget)
        self.networkCombo.setObjectName("networkCombo")
        self.horizontalLayout_2.addWidget(self.networkCombo)
        self.connectButton = QtWidgets.QToolButton(IrcNetworkWidget)
        self.connectButton.setToolTip("")
        self.connectButton.setText("")
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_2.addWidget(self.connectButton)
        self.awayButton = QtWidgets.QToolButton(IrcNetworkWidget)
        self.awayButton.setText("")
        self.awayButton.setObjectName("awayButton")
        self.horizontalLayout_2.addWidget(self.awayButton)
        self.editButton = QtWidgets.QToolButton(IrcNetworkWidget)
        self.editButton.setText("")
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_2.addWidget(self.editButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nickCombo = QtWidgets.QComboBox(IrcNetworkWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nickCombo.sizePolicy().hasHeightForWidth())
        self.nickCombo.setSizePolicy(sizePolicy)
        self.nickCombo.setEditable(True)
        self.nickCombo.setObjectName("nickCombo")
        self.horizontalLayout.addWidget(self.nickCombo)
        self.line = QtWidgets.QFrame(IrcNetworkWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.channelCombo = QtWidgets.QComboBox(IrcNetworkWidget)
        self.channelCombo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.channelCombo.sizePolicy().hasHeightForWidth())
        self.channelCombo.setSizePolicy(sizePolicy)
        self.channelCombo.setEditable(True)
        self.channelCombo.setObjectName("channelCombo")
        self.horizontalLayout.addWidget(self.channelCombo)
        self.joinButton = QtWidgets.QToolButton(IrcNetworkWidget)
        self.joinButton.setEnabled(False)
        self.joinButton.setText("")
        self.joinButton.setObjectName("joinButton")
        self.horizontalLayout.addWidget(self.joinButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(IrcNetworkWidget)
        QtCore.QMetaObject.connectSlotsByName(IrcNetworkWidget)
        IrcNetworkWidget.setTabOrder(self.networkCombo, self.connectButton)
        IrcNetworkWidget.setTabOrder(self.connectButton, self.awayButton)
        IrcNetworkWidget.setTabOrder(self.awayButton, self.editButton)
        IrcNetworkWidget.setTabOrder(self.editButton, self.nickCombo)
        IrcNetworkWidget.setTabOrder(self.nickCombo, self.channelCombo)
        IrcNetworkWidget.setTabOrder(self.channelCombo, self.joinButton)
        IrcNetworkWidget.setTabOrder(self.joinButton, self.messages)

    def retranslateUi(self, IrcNetworkWidget):
        _translate = QtCore.QCoreApplication.translate
        self.messages.setToolTip(_translate("IrcNetworkWidget", "Shows the network messages"))
        self.networkCombo.setToolTip(_translate("IrcNetworkWidget", "Select a network to connect to"))
        self.awayButton.setToolTip(_translate("IrcNetworkWidget", "Press to set the user status to AWAY"))
        self.editButton.setToolTip(_translate("IrcNetworkWidget", "Press to edit the networks"))
        self.nickCombo.setToolTip(_translate("IrcNetworkWidget", "Select a nick name for the channel"))
        self.channelCombo.setToolTip(_translate("IrcNetworkWidget", "Enter the channel to join"))
        self.joinButton.setToolTip(_translate("IrcNetworkWidget", "Press to join the channel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IrcNetworkWidget = QtWidgets.QWidget()
    ui = Ui_IrcNetworkWidget()
    ui.setupUi(IrcNetworkWidget)
    IrcNetworkWidget.show()
    sys.exit(app.exec_())

