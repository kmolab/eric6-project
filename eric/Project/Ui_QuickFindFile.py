# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\QuickFindFile.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuickFindFile(object):
    def setupUi(self, QuickFindFile):
        QuickFindFile.setObjectName("QuickFindFile")
        QuickFindFile.resize(599, 478)
        self.verticalLayout = QtWidgets.QVBoxLayout(QuickFindFile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textLabel1 = QtWidgets.QLabel(QuickFindFile)
        self.textLabel1.setObjectName("textLabel1")
        self.verticalLayout.addWidget(self.textLabel1)
        self.fileNameEdit = QtWidgets.QLineEdit(QuickFindFile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileNameEdit.sizePolicy().hasHeightForWidth())
        self.fileNameEdit.setSizePolicy(sizePolicy)
        self.fileNameEdit.setObjectName("fileNameEdit")
        self.verticalLayout.addWidget(self.fileNameEdit)
        self.fileList = QtWidgets.QTreeWidget(QuickFindFile)
        self.fileList.setRootIsDecorated(False)
        self.fileList.setObjectName("fileList")
        self.verticalLayout.addWidget(self.fileList)
        self.buttonBox = QtWidgets.QDialogButtonBox(QuickFindFile)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QuickFindFile)
        self.buttonBox.rejected.connect(QuickFindFile.close)
        QtCore.QMetaObject.connectSlotsByName(QuickFindFile)
        QuickFindFile.setTabOrder(self.fileNameEdit, self.fileList)

    def retranslateUi(self, QuickFindFile):
        _translate = QtCore.QCoreApplication.translate
        QuickFindFile.setWindowTitle(_translate("QuickFindFile", "Search Project File"))
        self.textLabel1.setText(_translate("QuickFindFile", "Type text to match in filenames (up/down to select shown files)"))
        self.fileNameEdit.setToolTip(_translate("QuickFindFile", "Enter search strings separated by a blank"))
        self.fileList.setSortingEnabled(True)
        self.fileList.headerItem().setText(0, _translate("QuickFindFile", "Path"))
        self.fileList.headerItem().setText(1, _translate("QuickFindFile", "Filename"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QuickFindFile = QtWidgets.QWidget()
    ui = Ui_QuickFindFile()
    ui.setupUi(QuickFindFile)
    QuickFindFile.show()
    sys.exit(app.exec_())

