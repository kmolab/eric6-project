# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\SiteInfo\SiteInfoNoSslDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SiteInfoDialog(object):
    def setupUi(self, SiteInfoDialog):
        SiteInfoDialog.setObjectName("SiteInfoDialog")
        SiteInfoDialog.resize(700, 550)
        SiteInfoDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SiteInfoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.heading = QtWidgets.QLabel(SiteInfoDialog)
        self.heading.setText("")
        self.heading.setWordWrap(True)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)
        self.tabWidget = QtWidgets.QTabWidget(SiteInfoDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.generalTab = QtWidgets.QWidget()
        self.generalTab.setObjectName("generalTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.generalTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.generalTab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.siteAddressLabel = QtWidgets.QLabel(self.generalTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.siteAddressLabel.sizePolicy().hasHeightForWidth())
        self.siteAddressLabel.setSizePolicy(sizePolicy)
        self.siteAddressLabel.setObjectName("siteAddressLabel")
        self.gridLayout.addWidget(self.siteAddressLabel, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.generalTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.encodingLabel = QtWidgets.QLabel(self.generalTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encodingLabel.sizePolicy().hasHeightForWidth())
        self.encodingLabel.setSizePolicy(sizePolicy)
        self.encodingLabel.setObjectName("encodingLabel")
        self.gridLayout.addWidget(self.encodingLabel, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.generalTab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(self.generalTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeLabel.sizePolicy().hasHeightForWidth())
        self.sizeLabel.setSizePolicy(sizePolicy)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_9 = QtWidgets.QLabel(self.generalTab)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.tagsTree = QtWidgets.QTreeWidget(self.generalTab)
        self.tagsTree.setAlternatingRowColors(True)
        self.tagsTree.setRootIsDecorated(False)
        self.tagsTree.setItemsExpandable(False)
        self.tagsTree.setWordWrap(False)
        self.tagsTree.setObjectName("tagsTree")
        self.verticalLayout_2.addWidget(self.tagsTree)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.generalTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.securityLabel = QtWidgets.QLabel(self.generalTab)
        self.securityLabel.setText("")
        self.securityLabel.setObjectName("securityLabel")
        self.gridLayout_2.addWidget(self.securityLabel, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.securityDetailsButton = QtWidgets.QPushButton(self.generalTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.securityDetailsButton.sizePolicy().hasHeightForWidth())
        self.securityDetailsButton.setSizePolicy(sizePolicy)
        self.securityDetailsButton.setAutoDefault(False)
        self.securityDetailsButton.setObjectName("securityDetailsButton")
        self.gridLayout_2.addWidget(self.securityDetailsButton, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.generalTab, "")
        self.mediaTab = QtWidgets.QWidget()
        self.mediaTab.setObjectName("mediaTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mediaTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.imagesTree = QtWidgets.QTreeWidget(self.mediaTab)
        self.imagesTree.setAlternatingRowColors(True)
        self.imagesTree.setRootIsDecorated(False)
        self.imagesTree.setItemsExpandable(False)
        self.imagesTree.setObjectName("imagesTree")
        self.verticalLayout_4.addWidget(self.imagesTree)
        self.label_5 = QtWidgets.QLabel(self.mediaTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.imagePreview = QtWidgets.QGraphicsView(self.mediaTab)
        self.imagePreview.setObjectName("imagePreview")
        self.verticalLayout_4.addWidget(self.imagePreview)
        self.tabWidget.addTab(self.mediaTab, "")
        self.databasesTab = QtWidgets.QWidget()
        self.databasesTab.setObjectName("databasesTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.databasesTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.databasesList = QtWidgets.QListWidget(self.databasesTab)
        self.databasesList.setObjectName("databasesList")
        self.verticalLayout_5.addWidget(self.databasesList)
        self.label_10 = QtWidgets.QLabel(self.databasesTab)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.databasesTab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.databaseName = QtWidgets.QLabel(self.databasesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databaseName.sizePolicy().hasHeightForWidth())
        self.databaseName.setSizePolicy(sizePolicy)
        self.databaseName.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.databaseName.setObjectName("databaseName")
        self.gridLayout_3.addWidget(self.databaseName, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.databasesTab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.databasePath = QtWidgets.QLabel(self.databasesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databasePath.sizePolicy().hasHeightForWidth())
        self.databasePath.setSizePolicy(sizePolicy)
        self.databasePath.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.databasePath.setObjectName("databasePath")
        self.gridLayout_3.addWidget(self.databasePath, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.databasesTab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.databaseSize = QtWidgets.QLabel(self.databasesTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databaseSize.sizePolicy().hasHeightForWidth())
        self.databaseSize.setSizePolicy(sizePolicy)
        self.databaseSize.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.databaseSize.setObjectName("databaseSize")
        self.gridLayout_3.addWidget(self.databaseSize, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 161, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.tabWidget.addTab(self.databasesTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(SiteInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SiteInfoDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(SiteInfoDialog.accept)
        self.buttonBox.rejected.connect(SiteInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SiteInfoDialog)
        SiteInfoDialog.setTabOrder(self.tabWidget, self.tagsTree)
        SiteInfoDialog.setTabOrder(self.tagsTree, self.securityDetailsButton)
        SiteInfoDialog.setTabOrder(self.securityDetailsButton, self.imagesTree)
        SiteInfoDialog.setTabOrder(self.imagesTree, self.imagePreview)
        SiteInfoDialog.setTabOrder(self.imagePreview, self.databasesList)
        SiteInfoDialog.setTabOrder(self.databasesList, self.buttonBox)

    def retranslateUi(self, SiteInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        SiteInfoDialog.setWindowTitle(_translate("SiteInfoDialog", "Site Information"))
        self.label.setText(_translate("SiteInfoDialog", "Site Address:"))
        self.label_2.setText(_translate("SiteInfoDialog", "Encoding:"))
        self.label_3.setText(_translate("SiteInfoDialog", "Size:"))
        self.label_9.setText(_translate("SiteInfoDialog", "Meta tags of site:"))
        self.tagsTree.headerItem().setText(0, _translate("SiteInfoDialog", "Tag"))
        self.tagsTree.headerItem().setText(1, _translate("SiteInfoDialog", "Value"))
        self.label_4.setText(_translate("SiteInfoDialog", "<b>Security information</b>"))
        self.securityDetailsButton.setText(_translate("SiteInfoDialog", "Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generalTab), _translate("SiteInfoDialog", "General"))
        self.imagesTree.headerItem().setText(0, _translate("SiteInfoDialog", "Image"))
        self.imagesTree.headerItem().setText(1, _translate("SiteInfoDialog", "Image Address"))
        self.label_5.setText(_translate("SiteInfoDialog", "<b>Preview</b>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mediaTab), _translate("SiteInfoDialog", "Media"))
        self.databasesList.setToolTip(_translate("SiteInfoDialog", "Shows a list of databases used by the site"))
        self.label_10.setText(_translate("SiteInfoDialog", "<b>Database details</b>"))
        self.label_6.setText(_translate("SiteInfoDialog", "Name:"))
        self.databaseName.setText(_translate("SiteInfoDialog", "<database not selected>"))
        self.label_7.setText(_translate("SiteInfoDialog", "Path:"))
        self.databasePath.setText(_translate("SiteInfoDialog", "<database not selected>"))
        self.label_8.setText(_translate("SiteInfoDialog", "Size:"))
        self.databaseSize.setText(_translate("SiteInfoDialog", "<database not selected>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.databasesTab), _translate("SiteInfoDialog", "Databases"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SiteInfoDialog = QtWidgets.QDialog()
    ui = Ui_SiteInfoDialog()
    ui.setupUi(SiteInfoDialog)
    SiteInfoDialog.show()
    sys.exit(app.exec_())

