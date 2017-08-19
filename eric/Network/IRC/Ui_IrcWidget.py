# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Network\IRC\IrcWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IrcWidget(object):
    def setupUi(self, IrcWidget):
        IrcWidget.setObjectName("IrcWidget")
        IrcWidget.resize(400, 941)
        IrcWidget.setWindowTitle("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(IrcWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(IrcWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.channelsWidget = QtWidgets.QTabWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.channelsWidget.sizePolicy().hasHeightForWidth())
        self.channelsWidget.setSizePolicy(sizePolicy)
        self.channelsWidget.setDocumentMode(True)
        self.channelsWidget.setTabsClosable(True)
        self.channelsWidget.setMovable(True)
        self.channelsWidget.setObjectName("channelsWidget")
        self.verticalLayout.addWidget(self.channelsWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.networkWidget = IrcNetworkWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.networkWidget.sizePolicy().hasHeightForWidth())
        self.networkWidget.setSizePolicy(sizePolicy)
        self.networkWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.networkWidget.setObjectName("networkWidget")
        self.verticalLayout_2.addWidget(self.networkWidget)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(IrcWidget)
        QtCore.QMetaObject.connectSlotsByName(IrcWidget)
        IrcWidget.setTabOrder(self.networkWidget, self.channelsWidget)

    def retranslateUi(self, IrcWidget):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox.setTitle(_translate("IrcWidget", "Channels"))
        self.groupBox_2.setTitle(_translate("IrcWidget", "Network"))

from Network.IRC.IrcNetworkWidget import IrcNetworkWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IrcWidget = QtWidgets.QWidget()
    ui = Ui_IrcWidget()
    ui.setupUi(IrcWidget)
    IrcWidget.show()
    sys.exit(app.exec_())

