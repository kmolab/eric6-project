# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\GreaseMonkey\GreaseMonkeyAddScriptDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GreaseMonkeyAddScriptDialog(object):
    def setupUi(self, GreaseMonkeyAddScriptDialog):
        GreaseMonkeyAddScriptDialog.setObjectName("GreaseMonkeyAddScriptDialog")
        GreaseMonkeyAddScriptDialog.resize(550, 400)
        GreaseMonkeyAddScriptDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(GreaseMonkeyAddScriptDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.iconLabel = QtWidgets.QLabel(GreaseMonkeyAddScriptDialog)
        self.iconLabel.setMinimumSize(QtCore.QSize(48, 48))
        self.iconLabel.setText("Icon")
        self.iconLabel.setObjectName("iconLabel")
        self.horizontalLayout.addWidget(self.iconLabel)
        self.label_2 = QtWidgets.QLabel(GreaseMonkeyAddScriptDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(GreaseMonkeyAddScriptDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.scriptInfo = QtWidgets.QTextBrowser(GreaseMonkeyAddScriptDialog)
        self.scriptInfo.setObjectName("scriptInfo")
        self.verticalLayout.addWidget(self.scriptInfo)
        self.label_5 = QtWidgets.QLabel(GreaseMonkeyAddScriptDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(GreaseMonkeyAddScriptDialog)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.showScriptSourceButton = QtWidgets.QPushButton(GreaseMonkeyAddScriptDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showScriptSourceButton.sizePolicy().hasHeightForWidth())
        self.showScriptSourceButton.setSizePolicy(sizePolicy)
        self.showScriptSourceButton.setObjectName("showScriptSourceButton")
        self.horizontalLayout_2.addWidget(self.showScriptSourceButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(GreaseMonkeyAddScriptDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(GreaseMonkeyAddScriptDialog)
        self.buttonBox.accepted.connect(GreaseMonkeyAddScriptDialog.accept)
        self.buttonBox.rejected.connect(GreaseMonkeyAddScriptDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GreaseMonkeyAddScriptDialog)

    def retranslateUi(self, GreaseMonkeyAddScriptDialog):
        _translate = QtCore.QCoreApplication.translate
        GreaseMonkeyAddScriptDialog.setWindowTitle(_translate("GreaseMonkeyAddScriptDialog", "GreaseMonkey Script Installation"))
        self.label_2.setText(_translate("GreaseMonkeyAddScriptDialog", "<h2>GreaseMonkey Script Installation</h2>"))
        self.label_3.setText(_translate("GreaseMonkeyAddScriptDialog", "You are about to install this userscript into GreaseMonkey:"))
        self.label_5.setText(_translate("GreaseMonkeyAddScriptDialog", "<b>You should only install scripts from sources you trust!</b>"))
        self.label_4.setText(_translate("GreaseMonkeyAddScriptDialog", "Are you sure you want to install it?"))
        self.showScriptSourceButton.setToolTip(_translate("GreaseMonkeyAddScriptDialog", "Press to open an editor with the script\'s source"))
        self.showScriptSourceButton.setText(_translate("GreaseMonkeyAddScriptDialog", "Show source code of script"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GreaseMonkeyAddScriptDialog = QtWidgets.QDialog()
    ui = Ui_GreaseMonkeyAddScriptDialog()
    ui.setupUi(GreaseMonkeyAddScriptDialog)
    GreaseMonkeyAddScriptDialog.show()
    sys.exit(app.exec_())

