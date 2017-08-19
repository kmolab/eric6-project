# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Download\DownloadManager.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadManager(object):
    def setupUi(self, DownloadManager):
        DownloadManager.setObjectName("DownloadManager")
        DownloadManager.resize(400, 300)
        DownloadManager.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(DownloadManager)
        self.gridLayout.setObjectName("gridLayout")
        self.downloadsView = E5TableView(DownloadManager)
        self.downloadsView.setObjectName("downloadsView")
        self.gridLayout.addWidget(self.downloadsView, 0, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cleanupButton = QtWidgets.QPushButton(DownloadManager)
        self.cleanupButton.setEnabled(False)
        self.cleanupButton.setAutoDefault(False)
        self.cleanupButton.setObjectName("cleanupButton")
        self.horizontalLayout_2.addWidget(self.cleanupButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.countLabel = QtWidgets.QLabel(DownloadManager)
        self.countLabel.setObjectName("countLabel")
        self.gridLayout.addWidget(self.countLabel, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(DownloadManager)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)

        self.retranslateUi(DownloadManager)
        self.buttonBox.rejected.connect(DownloadManager.close)
        QtCore.QMetaObject.connectSlotsByName(DownloadManager)
        DownloadManager.setTabOrder(self.downloadsView, self.cleanupButton)
        DownloadManager.setTabOrder(self.cleanupButton, self.buttonBox)

    def retranslateUi(self, DownloadManager):
        _translate = QtCore.QCoreApplication.translate
        DownloadManager.setWindowTitle(_translate("DownloadManager", "Downloads"))
        self.cleanupButton.setToolTip(_translate("DownloadManager", "Press to clean up the list of downloads"))
        self.cleanupButton.setText(_translate("DownloadManager", "Clear List"))
        self.countLabel.setText(_translate("DownloadManager", "0 Items"))

from E5Gui.E5TableView import E5TableView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DownloadManager = QtWidgets.QDialog()
    ui = Ui_DownloadManager()
    ui.setupUi(DownloadManager)
    DownloadManager.show()
    sys.exit(app.exec_())

