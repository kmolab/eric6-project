# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Cooperation\ChatWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatWidget(object):
    def setupUi(self, ChatWidget):
        ChatWidget.setObjectName("ChatWidget")
        ChatWidget.resize(300, 600)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ChatWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.usersGroup = QtWidgets.QGroupBox(ChatWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.usersGroup.sizePolicy().hasHeightForWidth())
        self.usersGroup.setSizePolicy(sizePolicy)
        self.usersGroup.setObjectName("usersGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.usersGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.usersList = QtWidgets.QListWidget(self.usersGroup)
        self.usersList.setFocusPolicy(QtCore.Qt.NoFocus)
        self.usersList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.usersList.setObjectName("usersList")
        self.verticalLayout.addWidget(self.usersList)
        self.verticalLayout_2.addWidget(self.usersGroup)
        self.chatGroup = QtWidgets.QGroupBox(ChatWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.chatGroup.sizePolicy().hasHeightForWidth())
        self.chatGroup.setSizePolicy(sizePolicy)
        self.chatGroup.setObjectName("chatGroup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.chatGroup)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.chatEdit = QtWidgets.QTextEdit(self.chatGroup)
        self.chatEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.chatEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.chatEdit.setReadOnly(True)
        self.chatEdit.setObjectName("chatEdit")
        self.verticalLayout_4.addWidget(self.chatEdit)
        self.messageEdit = E5ClearableLineEdit(self.chatGroup)
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout_4.addWidget(self.messageEdit)
        self.sendButton = QtWidgets.QPushButton(self.chatGroup)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout_4.addWidget(self.sendButton)
        self.verticalLayout_2.addWidget(self.chatGroup)
        self.sharingGroup = QtWidgets.QGroupBox(ChatWidget)
        self.sharingGroup.setEnabled(False)
        self.sharingGroup.setObjectName("sharingGroup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.sharingGroup)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.shareButton = QtWidgets.QToolButton(self.sharingGroup)
        self.shareButton.setEnabled(False)
        self.shareButton.setCheckable(True)
        self.shareButton.setObjectName("shareButton")
        self.horizontalLayout.addWidget(self.shareButton)
        self.startEditButton = QtWidgets.QToolButton(self.sharingGroup)
        self.startEditButton.setEnabled(False)
        self.startEditButton.setCheckable(True)
        self.startEditButton.setObjectName("startEditButton")
        self.horizontalLayout.addWidget(self.startEditButton)
        self.sendEditButton = QtWidgets.QToolButton(self.sharingGroup)
        self.sendEditButton.setEnabled(False)
        self.sendEditButton.setObjectName("sendEditButton")
        self.horizontalLayout.addWidget(self.sendEditButton)
        self.cancelEditButton = QtWidgets.QToolButton(self.sharingGroup)
        self.cancelEditButton.setEnabled(False)
        self.cancelEditButton.setObjectName("cancelEditButton")
        self.horizontalLayout.addWidget(self.cancelEditButton)
        spacerItem1 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.sharingGroup)
        self.connectGroup = QtWidgets.QGroupBox(ChatWidget)
        self.connectGroup.setObjectName("connectGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.connectGroup)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.connectGroup)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.hostEdit = E5ClearableComboBox(self.connectGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hostEdit.sizePolicy().hasHeightForWidth())
        self.hostEdit.setSizePolicy(sizePolicy)
        self.hostEdit.setEditable(True)
        self.hostEdit.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.hostEdit.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.hostEdit.setObjectName("hostEdit")
        self.horizontalLayout_3.addWidget(self.hostEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.clearHostsButton = QtWidgets.QPushButton(self.connectGroup)
        self.clearHostsButton.setObjectName("clearHostsButton")
        self.horizontalLayout_4.addWidget(self.clearHostsButton)
        self.connectButton = QtWidgets.QPushButton(self.connectGroup)
        self.connectButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setText("")
        self.connectButton.setAutoDefault(False)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout_4.addWidget(self.connectButton)
        self.connectionLed = E5Led(self.connectGroup)
        self.connectionLed.setObjectName("connectionLed")
        self.horizontalLayout_4.addWidget(self.connectionLed)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.connectGroup)
        self.serverGroup = QtWidgets.QGroupBox(ChatWidget)
        self.serverGroup.setObjectName("serverGroup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.serverGroup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.serverGroup)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.serverPortSpin = QtWidgets.QSpinBox(self.serverGroup)
        self.serverPortSpin.setMinimum(1025)
        self.serverPortSpin.setMaximum(65535)
        self.serverPortSpin.setSingleStep(1)
        self.serverPortSpin.setProperty("value", 42000)
        self.serverPortSpin.setObjectName("serverPortSpin")
        self.horizontalLayout_2.addWidget(self.serverPortSpin)
        self.serverButton = QtWidgets.QPushButton(self.serverGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverButton.sizePolicy().hasHeightForWidth())
        self.serverButton.setSizePolicy(sizePolicy)
        self.serverButton.setText("")
        self.serverButton.setAutoDefault(False)
        self.serverButton.setObjectName("serverButton")
        self.horizontalLayout_2.addWidget(self.serverButton)
        self.serverLed = E5Led(self.serverGroup)
        self.serverLed.setObjectName("serverLed")
        self.horizontalLayout_2.addWidget(self.serverLed)
        self.verticalLayout_2.addWidget(self.serverGroup)

        self.retranslateUi(ChatWidget)
        QtCore.QMetaObject.connectSlotsByName(ChatWidget)
        ChatWidget.setTabOrder(self.serverButton, self.serverPortSpin)
        ChatWidget.setTabOrder(self.serverPortSpin, self.hostEdit)
        ChatWidget.setTabOrder(self.hostEdit, self.connectButton)
        ChatWidget.setTabOrder(self.connectButton, self.clearHostsButton)
        ChatWidget.setTabOrder(self.clearHostsButton, self.shareButton)
        ChatWidget.setTabOrder(self.shareButton, self.startEditButton)
        ChatWidget.setTabOrder(self.startEditButton, self.sendEditButton)
        ChatWidget.setTabOrder(self.sendEditButton, self.cancelEditButton)
        ChatWidget.setTabOrder(self.cancelEditButton, self.messageEdit)
        ChatWidget.setTabOrder(self.messageEdit, self.sendButton)

    def retranslateUi(self, ChatWidget):
        _translate = QtCore.QCoreApplication.translate
        ChatWidget.setWindowTitle(_translate("ChatWidget", "Chat"))
        self.usersGroup.setTitle(_translate("ChatWidget", "Users"))
        self.chatGroup.setTitle(_translate("ChatWidget", "Chat"))
        self.messageEdit.setToolTip(_translate("ChatWidget", "Enter the text to send"))
        self.sendButton.setToolTip(_translate("ChatWidget", "Press to send the text above"))
        self.sendButton.setText(_translate("ChatWidget", "Send"))
        self.sharingGroup.setTitle(_translate("ChatWidget", "Share Editor"))
        self.shareButton.setToolTip(_translate("ChatWidget", "Press to toggle the shared status of the current editor"))
        self.startEditButton.setToolTip(_translate("ChatWidget", "Press to start a shared edit"))
        self.sendEditButton.setToolTip(_translate("ChatWidget", "Press to end the edit and send the changes"))
        self.cancelEditButton.setToolTip(_translate("ChatWidget", "Press to cancel the shared edit"))
        self.connectGroup.setTitle(_translate("ChatWidget", "Connection"))
        self.label_2.setText(_translate("ChatWidget", "Host:"))
        self.hostEdit.setToolTip(_translate("ChatWidget", "Enter the host and port to connect to in the form \"host@port\""))
        self.clearHostsButton.setToolTip(_translate("ChatWidget", "Press to clear the hosts list"))
        self.clearHostsButton.setText(_translate("ChatWidget", "Clear"))
        self.connectionLed.setToolTip(_translate("ChatWidget", "Shows the connection status"))
        self.serverGroup.setTitle(_translate("ChatWidget", "Server"))
        self.label_4.setText(_translate("ChatWidget", "Port:"))
        self.serverPortSpin.setToolTip(_translate("ChatWidget", "Enter the server port"))
        self.serverLed.setToolTip(_translate("ChatWidget", "Shows the status of the server"))

from E5Gui.E5ComboBox import E5ClearableComboBox
from E5Gui.E5Led import E5Led
from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatWidget = QtWidgets.QWidget()
    ui = Ui_ChatWidget()
    ui.setupUi(ChatWidget)
    ChatWidget.show()
    sys.exit(app.exec_())

