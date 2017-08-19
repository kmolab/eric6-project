# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\Download\DownloadItem.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadItem(object):
    def setupUi(self, DownloadItem):
        DownloadItem.setObjectName("DownloadItem")
        DownloadItem.resize(400, 82)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DownloadItem.sizePolicy().hasHeightForWidth())
        DownloadItem.setSizePolicy(sizePolicy)
        DownloadItem.setWindowTitle("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(DownloadItem)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileIcon = QtWidgets.QLabel(DownloadItem)
        self.fileIcon.setObjectName("fileIcon")
        self.horizontalLayout.addWidget(self.fileIcon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.filenameLabel = QtWidgets.QLabel(DownloadItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameLabel.sizePolicy().hasHeightForWidth())
        self.filenameLabel.setSizePolicy(sizePolicy)
        self.filenameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filenameLabel.setWordWrap(True)
        self.filenameLabel.setObjectName("filenameLabel")
        self.verticalLayout.addWidget(self.filenameLabel)
        self.progressBar = QtWidgets.QProgressBar(DownloadItem)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.infoLabel = QtWidgets.QLabel(DownloadItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setText("Info")
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tryAgainButton = QtWidgets.QToolButton(DownloadItem)
        self.tryAgainButton.setText("")
        self.tryAgainButton.setObjectName("tryAgainButton")
        self.horizontalLayout.addWidget(self.tryAgainButton)
        self.pauseButton = QtWidgets.QToolButton(DownloadItem)
        self.pauseButton.setText("")
        self.pauseButton.setCheckable(True)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QToolButton(DownloadItem)
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.openButton = QtWidgets.QToolButton(DownloadItem)
        self.openButton.setText("")
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)

        self.retranslateUi(DownloadItem)
        QtCore.QMetaObject.connectSlotsByName(DownloadItem)
        DownloadItem.setTabOrder(self.tryAgainButton, self.pauseButton)
        DownloadItem.setTabOrder(self.pauseButton, self.stopButton)
        DownloadItem.setTabOrder(self.stopButton, self.openButton)

    def retranslateUi(self, DownloadItem):
        _translate = QtCore.QCoreApplication.translate
        self.fileIcon.setText(_translate("DownloadItem", "Icon"))
        self.filenameLabel.setText(_translate("DownloadItem", "Filename"))
        self.tryAgainButton.setToolTip(_translate("DownloadItem", "Press to repeat the download"))
        self.pauseButton.setToolTip(_translate("DownloadItem", "Press to pause the download"))
        self.stopButton.setToolTip(_translate("DownloadItem", "Press to cancel the download"))
        self.openButton.setToolTip(_translate("DownloadItem", "Press to open the downloaded file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DownloadItem = QtWidgets.QWidget()
    ui = Ui_DownloadItem()
    ui.setupUi(DownloadItem)
    DownloadItem.show()
    sys.exit(app.exec_())

