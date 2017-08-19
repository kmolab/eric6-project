# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\PageScreenDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PageScreenDialog(object):
    def setupUi(self, PageScreenDialog):
        PageScreenDialog.setObjectName("PageScreenDialog")
        PageScreenDialog.resize(500, 450)
        PageScreenDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PageScreenDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(PageScreenDialog)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 482, 403))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pageScreenLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pageScreenLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pageScreenLabel.setObjectName("pageScreenLabel")
        self.horizontalLayout.addWidget(self.pageScreenLabel)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(PageScreenDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PageScreenDialog)
        QtCore.QMetaObject.connectSlotsByName(PageScreenDialog)
        PageScreenDialog.setTabOrder(self.scrollArea, self.buttonBox)

    def retranslateUi(self, PageScreenDialog):
        _translate = QtCore.QCoreApplication.translate
        PageScreenDialog.setWindowTitle(_translate("PageScreenDialog", "Page Screen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PageScreenDialog = QtWidgets.QDialog()
    ui = Ui_PageScreenDialog()
    ui.setupUi(PageScreenDialog)
    PageScreenDialog.show()
    sys.exit(app.exec_())

