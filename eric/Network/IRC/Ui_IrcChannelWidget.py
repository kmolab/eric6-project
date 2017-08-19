# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Network\IRC\IrcChannelWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IrcChannelWidget(object):
    def setupUi(self, IrcChannelWidget):
        IrcChannelWidget.setObjectName("IrcChannelWidget")
        IrcChannelWidget.resize(400, 685)
        IrcChannelWidget.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(IrcChannelWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.topicLabel = QtWidgets.QLabel(IrcChannelWidget)
        self.topicLabel.setText("")
        self.topicLabel.setWordWrap(True)
        self.topicLabel.setOpenExternalLinks(True)
        self.topicLabel.setObjectName("topicLabel")
        self.horizontalLayout.addWidget(self.topicLabel)
        self.editTopicButton = QtWidgets.QToolButton(IrcChannelWidget)
        self.editTopicButton.setText("")
        self.editTopicButton.setObjectName("editTopicButton")
        self.horizontalLayout.addWidget(self.editTopicButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(IrcChannelWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.usersList = QtWidgets.QListWidget(self.splitter)
        self.usersList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.usersList.setAlternatingRowColors(True)
        self.usersList.setObjectName("usersList")
        self.messages = QtWidgets.QTextBrowser(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.messages.sizePolicy().hasHeightForWidth())
        self.messages.setSizePolicy(sizePolicy)
        self.messages.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.messages.setTabChangesFocus(True)
        self.messages.setOpenLinks(False)
        self.messages.setObjectName("messages")
        self.verticalLayout.addWidget(self.splitter)
        self.messageEdit = IrcMessageEdit(IrcChannelWidget)
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout.addWidget(self.messageEdit)

        self.retranslateUi(IrcChannelWidget)
        QtCore.QMetaObject.connectSlotsByName(IrcChannelWidget)
        IrcChannelWidget.setTabOrder(self.messageEdit, self.messages)
        IrcChannelWidget.setTabOrder(self.messages, self.usersList)
        IrcChannelWidget.setTabOrder(self.usersList, self.editTopicButton)

    def retranslateUi(self, IrcChannelWidget):
        _translate = QtCore.QCoreApplication.translate
        self.editTopicButton.setToolTip(_translate("IrcChannelWidget", "Press to change the topic"))
        self.usersList.setToolTip(_translate("IrcChannelWidget", "Shows the list of users"))
        self.usersList.setSortingEnabled(True)
        self.messages.setToolTip(_translate("IrcChannelWidget", "Shows the channel messages"))
        self.messageEdit.setToolTip(_translate("IrcChannelWidget", "Enter a message, send by pressing Return or Enter"))
        self.messageEdit.setPlaceholderText(_translate("IrcChannelWidget", "Enter a message, send by pressing Return or Enter"))

from Network.IRC.IrcMessageEdit import IrcMessageEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IrcChannelWidget = QtWidgets.QWidget()
    ui = Ui_IrcChannelWidget()
    ui.setupUi(IrcChannelWidget)
    IrcChannelWidget.show()
    sys.exit(app.exec_())

