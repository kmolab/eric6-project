# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Bookmarks\BookmarksDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookmarksDialog(object):
    def setupUi(self, BookmarksDialog):
        BookmarksDialog.setObjectName("BookmarksDialog")
        BookmarksDialog.resize(750, 450)
        BookmarksDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(BookmarksDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchEdit = E5ClearableLineEdit(BookmarksDialog)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.bookmarksTree = E5TreeView(BookmarksDialog)
        self.bookmarksTree.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.bookmarksTree.setAlternatingRowColors(True)
        self.bookmarksTree.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.bookmarksTree.setUniformRowHeights(True)
        self.bookmarksTree.setObjectName("bookmarksTree")
        self.verticalLayout.addWidget(self.bookmarksTree)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.removeButton = QtWidgets.QPushButton(BookmarksDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.horizontalLayout_3.addWidget(self.removeButton)
        self.addFolderButton = QtWidgets.QPushButton(BookmarksDialog)
        self.addFolderButton.setAutoDefault(False)
        self.addFolderButton.setObjectName("addFolderButton")
        self.horizontalLayout_3.addWidget(self.addFolderButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(BookmarksDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(BookmarksDialog)
        self.buttonBox.accepted.connect(BookmarksDialog.accept)
        self.buttonBox.rejected.connect(BookmarksDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarksDialog)
        BookmarksDialog.setTabOrder(self.searchEdit, self.bookmarksTree)
        BookmarksDialog.setTabOrder(self.bookmarksTree, self.removeButton)
        BookmarksDialog.setTabOrder(self.removeButton, self.addFolderButton)
        BookmarksDialog.setTabOrder(self.addFolderButton, self.buttonBox)

    def retranslateUi(self, BookmarksDialog):
        _translate = QtCore.QCoreApplication.translate
        BookmarksDialog.setWindowTitle(_translate("BookmarksDialog", "Manage Bookmarks"))
        self.searchEdit.setToolTip(_translate("BookmarksDialog", "Enter search term for bookmarks"))
        self.removeButton.setToolTip(_translate("BookmarksDialog", "Press to delete the selected entries"))
        self.removeButton.setText(_translate("BookmarksDialog", "&Delete"))
        self.addFolderButton.setToolTip(_translate("BookmarksDialog", "Press to add a new bookmarks folder"))
        self.addFolderButton.setText(_translate("BookmarksDialog", "Add &Folder"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5TreeView import E5TreeView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookmarksDialog = QtWidgets.QDialog()
    ui = Ui_BookmarksDialog()
    ui.setupUi(BookmarksDialog)
    BookmarksDialog.show()
    sys.exit(app.exec_())

