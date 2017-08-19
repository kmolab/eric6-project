# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnBlameDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnBlameDialog(object):
    def setupUi(self, SvnBlameDialog):
        SvnBlameDialog.setObjectName("SvnBlameDialog")
        SvnBlameDialog.resize(690, 750)
        SvnBlameDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnBlameDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.blameList = QtWidgets.QTreeWidget(SvnBlameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.blameList.sizePolicy().hasHeightForWidth())
        self.blameList.setSizePolicy(sizePolicy)
        self.blameList.setAlternatingRowColors(True)
        self.blameList.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.blameList.setRootIsDecorated(False)
        self.blameList.setItemsExpandable(False)
        self.blameList.setObjectName("blameList")
        self.blameList.header().setStretchLastSection(False)
        self.vboxlayout.addWidget(self.blameList)
        self.errorGroup = QtWidgets.QGroupBox(SvnBlameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout1.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnBlameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnBlameDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnBlameDialog)
        SvnBlameDialog.setTabOrder(self.blameList, self.errors)
        SvnBlameDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnBlameDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnBlameDialog.setWindowTitle(_translate("SvnBlameDialog", "Subversion Blame"))
        self.blameList.headerItem().setText(0, _translate("SvnBlameDialog", "Revision"))
        self.blameList.headerItem().setText(1, _translate("SvnBlameDialog", "Author"))
        self.blameList.headerItem().setText(2, _translate("SvnBlameDialog", "Line"))
        self.errorGroup.setTitle(_translate("SvnBlameDialog", "Errors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnBlameDialog = QtWidgets.QDialog()
    ui = Ui_SvnBlameDialog()
    ui.setupUi(SvnBlameDialog)
    SvnBlameDialog.show()
    sys.exit(app.exec_())

