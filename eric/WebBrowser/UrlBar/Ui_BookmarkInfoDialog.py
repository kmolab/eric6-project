# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\UrlBar\BookmarkInfoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookmarkInfoDialog(object):
    def setupUi(self, BookmarkInfoDialog):
        BookmarkInfoDialog.setObjectName("BookmarkInfoDialog")
        BookmarkInfoDialog.resize(350, 135)
        BookmarkInfoDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(BookmarkInfoDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QLabel(BookmarkInfoDialog)
        self.icon.setText("")
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(BookmarkInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.removeButton = QtWidgets.QPushButton(BookmarkInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
        self.removeButton.setSizePolicy(sizePolicy)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(BookmarkInfoDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.titleEdit = QtWidgets.QLineEdit(BookmarkInfoDialog)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(BookmarkInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(BookmarkInfoDialog)
        self.buttonBox.accepted.connect(BookmarkInfoDialog.accept)
        self.buttonBox.rejected.connect(BookmarkInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarkInfoDialog)
        BookmarkInfoDialog.setTabOrder(self.removeButton, self.titleEdit)
        BookmarkInfoDialog.setTabOrder(self.titleEdit, self.buttonBox)

    def retranslateUi(self, BookmarkInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        BookmarkInfoDialog.setWindowTitle(_translate("BookmarkInfoDialog", "Edit Bookmark"))
        self.title.setText(_translate("BookmarkInfoDialog", "Edit this Bookmark"))
        self.removeButton.setToolTip(_translate("BookmarkInfoDialog", "Press to remove this bookmark"))
        self.removeButton.setText(_translate("BookmarkInfoDialog", "Remove this Bookmark"))
        self.label.setText(_translate("BookmarkInfoDialog", "Title:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookmarkInfoDialog = QtWidgets.QDialog()
    ui = Ui_BookmarkInfoDialog()
    ui.setupUi(BookmarkInfoDialog)
    BookmarkInfoDialog.show()
    sys.exit(app.exec_())

