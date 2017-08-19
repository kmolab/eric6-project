# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgBookmarkRenameDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgBookmarkRenameDialog(object):
    def setupUi(self, HgBookmarkRenameDialog):
        HgBookmarkRenameDialog.setObjectName("HgBookmarkRenameDialog")
        HgBookmarkRenameDialog.resize(400, 102)
        HgBookmarkRenameDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgBookmarkRenameDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgBookmarkRenameDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(HgBookmarkRenameDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(HgBookmarkRenameDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.bookmarkCombo = QtWidgets.QComboBox(HgBookmarkRenameDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookmarkCombo.sizePolicy().hasHeightForWidth())
        self.bookmarkCombo.setSizePolicy(sizePolicy)
        self.bookmarkCombo.setEditable(True)
        self.bookmarkCombo.setObjectName("bookmarkCombo")
        self.gridLayout.addWidget(self.bookmarkCombo, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgBookmarkRenameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(HgBookmarkRenameDialog)
        self.buttonBox.accepted.connect(HgBookmarkRenameDialog.accept)
        self.buttonBox.rejected.connect(HgBookmarkRenameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgBookmarkRenameDialog)
        HgBookmarkRenameDialog.setTabOrder(self.nameEdit, self.bookmarkCombo)
        HgBookmarkRenameDialog.setTabOrder(self.bookmarkCombo, self.buttonBox)

    def retranslateUi(self, HgBookmarkRenameDialog):
        _translate = QtCore.QCoreApplication.translate
        HgBookmarkRenameDialog.setWindowTitle(_translate("HgBookmarkRenameDialog", "Rename Bookmark"))
        self.label.setText(_translate("HgBookmarkRenameDialog", "New Name:"))
        self.nameEdit.setToolTip(_translate("HgBookmarkRenameDialog", "Enter the bookmark name"))
        self.label_2.setText(_translate("HgBookmarkRenameDialog", "Bookmark:"))
        self.bookmarkCombo.setToolTip(_translate("HgBookmarkRenameDialog", "Enter the bookmark name to be renamed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgBookmarkRenameDialog = QtWidgets.QDialog()
    ui = Ui_HgBookmarkRenameDialog()
    ui.setupUi(HgBookmarkRenameDialog)
    HgBookmarkRenameDialog.show()
    sys.exit(app.exec_())

