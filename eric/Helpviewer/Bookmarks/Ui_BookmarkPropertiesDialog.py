# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Helpviewer\Bookmarks\BookmarkPropertiesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookmarkPropertiesDialog(object):
    def setupUi(self, BookmarkPropertiesDialog):
        BookmarkPropertiesDialog.setObjectName("BookmarkPropertiesDialog")
        BookmarkPropertiesDialog.resize(500, 221)
        BookmarkPropertiesDialog.setMinimumSize(QtCore.QSize(500, 0))
        BookmarkPropertiesDialog.setMaximumSize(QtCore.QSize(500, 250))
        BookmarkPropertiesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(BookmarkPropertiesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(BookmarkPropertiesDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.nameEdit = E5LineEdit(BookmarkPropertiesDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.addressLabel = QtWidgets.QLabel(BookmarkPropertiesDialog)
        self.addressLabel.setObjectName("addressLabel")
        self.gridLayout.addWidget(self.addressLabel, 1, 0, 1, 1)
        self.addressEdit = E5LineEdit(BookmarkPropertiesDialog)
        self.addressEdit.setObjectName("addressEdit")
        self.gridLayout.addWidget(self.addressEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(BookmarkPropertiesDialog)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QPlainTextEdit(BookmarkPropertiesDialog)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(BookmarkPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(BookmarkPropertiesDialog)
        self.buttonBox.accepted.connect(BookmarkPropertiesDialog.accept)
        self.buttonBox.rejected.connect(BookmarkPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarkPropertiesDialog)
        BookmarkPropertiesDialog.setTabOrder(self.nameEdit, self.addressEdit)
        BookmarkPropertiesDialog.setTabOrder(self.addressEdit, self.descriptionEdit)
        BookmarkPropertiesDialog.setTabOrder(self.descriptionEdit, self.buttonBox)

    def retranslateUi(self, BookmarkPropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        BookmarkPropertiesDialog.setWindowTitle(_translate("BookmarkPropertiesDialog", "Bookmark Properties"))
        self.label_2.setText(_translate("BookmarkPropertiesDialog", "Name:"))
        self.nameEdit.setToolTip(_translate("BookmarkPropertiesDialog", "Enter the name"))
        self.addressLabel.setText(_translate("BookmarkPropertiesDialog", "Address:"))
        self.addressEdit.setToolTip(_translate("BookmarkPropertiesDialog", "Enter the address"))
        self.label.setText(_translate("BookmarkPropertiesDialog", "Description:"))
        self.descriptionEdit.setToolTip(_translate("BookmarkPropertiesDialog", "Enter a description"))

from E5Gui.E5LineEdit import E5LineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookmarkPropertiesDialog = QtWidgets.QDialog()
    ui = Ui_BookmarkPropertiesDialog()
    ui.setupUi(BookmarkPropertiesDialog)
    BookmarkPropertiesDialog.show()
    sys.exit(app.exec_())

