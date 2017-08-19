# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\NotificationWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NotificationWidget(object):
    def setupUi(self, NotificationWidget):
        NotificationWidget.setObjectName("NotificationWidget")
        NotificationWidget.resize(400, 80)
        NotificationWidget.setWindowTitle("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NotificationWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(NotificationWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QLabel(self.frame)
        self.icon.setMaximumSize(QtCore.QSize(48, 48))
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.heading = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heading.sizePolicy().hasHeightForWidth())
        self.heading.setSizePolicy(sizePolicy)
        self.heading.setMinimumSize(QtCore.QSize(335, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setText("")
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)
        self.text = QtWidgets.QLabel(self.frame)
        self.text.setMinimumSize(QtCore.QSize(335, 0))
        self.text.setText("")
        self.text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(NotificationWidget)
        QtCore.QMetaObject.connectSlotsByName(NotificationWidget)

    def retranslateUi(self, NotificationWidget):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NotificationWidget = QtWidgets.QWidget()
    ui = Ui_NotificationWidget()
    ui.setupUi(NotificationWidget)
    NotificationWidget.show()
    sys.exit(app.exec_())

