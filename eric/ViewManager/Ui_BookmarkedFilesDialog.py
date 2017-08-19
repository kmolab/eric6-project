# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\ViewManager\BookmarkedFilesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookmarkedFilesDialog(object):
    def setupUi(self, BookmarkedFilesDialog):
        BookmarkedFilesDialog.setObjectName("BookmarkedFilesDialog")
        BookmarkedFilesDialog.resize(475, 391)
        BookmarkedFilesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(BookmarkedFilesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.filesList = QtWidgets.QListWidget(BookmarkedFilesDialog)
        self.filesList.setAlternatingRowColors(True)
        self.filesList.setObjectName("filesList")
        self.gridLayout.addWidget(self.filesList, 0, 0, 6, 2)
        self.addButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.addButton.setEnabled(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 2, 1, 1)
        self.changeButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.changeButton.setEnabled(False)
        self.changeButton.setObjectName("changeButton")
        self.gridLayout.addWidget(self.changeButton, 1, 2, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.deleteButton.setEnabled(False)
        self.deleteButton.setObjectName("deleteButton")
        self.gridLayout.addWidget(self.deleteButton, 2, 2, 1, 1)
        self.upButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.upButton.setEnabled(False)
        self.upButton.setObjectName("upButton")
        self.gridLayout.addWidget(self.upButton, 3, 2, 1, 1)
        self.downButton = QtWidgets.QPushButton(BookmarkedFilesDialog)
        self.downButton.setEnabled(False)
        self.downButton.setObjectName("downButton")
        self.gridLayout.addWidget(self.downButton, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(87, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.TextLabel1 = QtWidgets.QLabel(BookmarkedFilesDialog)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridLayout.addWidget(self.TextLabel1, 6, 0, 1, 1)
        self.filePicker = E5PathPicker(BookmarkedFilesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePicker.sizePolicy().hasHeightForWidth())
        self.filePicker.setSizePolicy(sizePolicy)
        self.filePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.filePicker.setObjectName("filePicker")
        self.gridLayout.addWidget(self.filePicker, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(BookmarkedFilesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.TextLabel1.setBuddy(self.filePicker)

        self.retranslateUi(BookmarkedFilesDialog)
        self.buttonBox.accepted.connect(BookmarkedFilesDialog.accept)
        self.buttonBox.rejected.connect(BookmarkedFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarkedFilesDialog)
        BookmarkedFilesDialog.setTabOrder(self.filesList, self.addButton)
        BookmarkedFilesDialog.setTabOrder(self.addButton, self.changeButton)
        BookmarkedFilesDialog.setTabOrder(self.changeButton, self.deleteButton)
        BookmarkedFilesDialog.setTabOrder(self.deleteButton, self.upButton)
        BookmarkedFilesDialog.setTabOrder(self.upButton, self.downButton)

    def retranslateUi(self, BookmarkedFilesDialog):
        _translate = QtCore.QCoreApplication.translate
        BookmarkedFilesDialog.setWindowTitle(_translate("BookmarkedFilesDialog", "Configure Bookmarked Files Menu"))
        self.addButton.setToolTip(_translate("BookmarkedFilesDialog", "Add a new bookmarked file"))
        self.addButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Add</b>\n"
"<p>Add a new bookmarked file with the value entered below.</p>"))
        self.addButton.setText(_translate("BookmarkedFilesDialog", "&Add"))
        self.addButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+A"))
        self.changeButton.setToolTip(_translate("BookmarkedFilesDialog", "Change the value of the selected entry"))
        self.changeButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Change</b>\n"
"<p>Change the value of the selected entry.</p>"))
        self.changeButton.setText(_translate("BookmarkedFilesDialog", "C&hange"))
        self.changeButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+H"))
        self.deleteButton.setToolTip(_translate("BookmarkedFilesDialog", "Delete the selected entry"))
        self.deleteButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Delete</b>\n"
"<p>Delete the selected entry.</p>"))
        self.deleteButton.setText(_translate("BookmarkedFilesDialog", "&Delete"))
        self.deleteButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+D"))
        self.upButton.setToolTip(_translate("BookmarkedFilesDialog", "Move up"))
        self.upButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Move Up</b>\n"
"<p>Move the selected entry up.</p>"))
        self.upButton.setText(_translate("BookmarkedFilesDialog", "&Up"))
        self.upButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+U"))
        self.downButton.setToolTip(_translate("BookmarkedFilesDialog", "Move down"))
        self.downButton.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>Move Down</b>\n"
"<p>Move the selected entry down.</p>"))
        self.downButton.setText(_translate("BookmarkedFilesDialog", "&Down"))
        self.downButton.setShortcut(_translate("BookmarkedFilesDialog", "Alt+D"))
        self.TextLabel1.setText(_translate("BookmarkedFilesDialog", "&File:"))
        self.filePicker.setToolTip(_translate("BookmarkedFilesDialog", "Enter the filename of the file"))
        self.filePicker.setWhatsThis(_translate("BookmarkedFilesDialog", "<b>File</b>\n"
"<p>Enter the filename of the bookmarked file.</p>"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BookmarkedFilesDialog = QtWidgets.QDialog()
    ui = Ui_BookmarkedFilesDialog()
    ui.setupUi(BookmarkedFilesDialog)
    BookmarkedFilesDialog.show()
    sys.exit(app.exec_())

