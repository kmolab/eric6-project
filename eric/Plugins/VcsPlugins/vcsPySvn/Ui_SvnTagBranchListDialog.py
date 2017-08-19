# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnTagBranchListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnTagBranchListDialog(object):
    def setupUi(self, SvnTagBranchListDialog):
        SvnTagBranchListDialog.setObjectName("SvnTagBranchListDialog")
        SvnTagBranchListDialog.resize(634, 494)
        SvnTagBranchListDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnTagBranchListDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.tagList = QtWidgets.QTreeWidget(SvnTagBranchListDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.tagList.sizePolicy().hasHeightForWidth())
        self.tagList.setSizePolicy(sizePolicy)
        self.tagList.setAlternatingRowColors(True)
        self.tagList.setRootIsDecorated(False)
        self.tagList.setItemsExpandable(False)
        self.tagList.setObjectName("tagList")
        self.vboxlayout.addWidget(self.tagList)
        self.errorGroup = QtWidgets.QGroupBox(SvnTagBranchListDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnTagBranchListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnTagBranchListDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnTagBranchListDialog)
        SvnTagBranchListDialog.setTabOrder(self.tagList, self.errors)
        SvnTagBranchListDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, SvnTagBranchListDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnTagBranchListDialog.setWindowTitle(_translate("SvnTagBranchListDialog", "Subversion Tag List"))
        SvnTagBranchListDialog.setWhatsThis(_translate("SvnTagBranchListDialog", "<b>Subversion Tag/Branch List</b>\n"
"<p>This dialog shows a list of the projects tags or branches.</p>"))
        self.tagList.setWhatsThis(_translate("SvnTagBranchListDialog", "<b>Tag/Branches List</b>\n"
"<p>This shows a list of the projects tags or branches.</p>"))
        self.tagList.setSortingEnabled(True)
        self.tagList.headerItem().setText(0, _translate("SvnTagBranchListDialog", "Revision"))
        self.tagList.headerItem().setText(1, _translate("SvnTagBranchListDialog", "Author"))
        self.tagList.headerItem().setText(2, _translate("SvnTagBranchListDialog", "Date"))
        self.tagList.headerItem().setText(3, _translate("SvnTagBranchListDialog", "Name"))
        self.errorGroup.setTitle(_translate("SvnTagBranchListDialog", "Errors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnTagBranchListDialog = QtWidgets.QDialog()
    ui = Ui_SvnTagBranchListDialog()
    ui.setupUi(SvnTagBranchListDialog)
    SvnTagBranchListDialog.show()
    sys.exit(app.exec_())

