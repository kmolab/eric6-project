# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgBookmarksInOutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgBookmarksInOutDialog(object):
    def setupUi(self, HgBookmarksInOutDialog):
        HgBookmarksInOutDialog.setObjectName("HgBookmarksInOutDialog")
        HgBookmarksInOutDialog.resize(520, 494)
        HgBookmarksInOutDialog.setWindowTitle("")
        HgBookmarksInOutDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(HgBookmarksInOutDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.bookmarksList = QtWidgets.QTreeWidget(HgBookmarksInOutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.bookmarksList.sizePolicy().hasHeightForWidth())
        self.bookmarksList.setSizePolicy(sizePolicy)
        self.bookmarksList.setAlternatingRowColors(True)
        self.bookmarksList.setRootIsDecorated(False)
        self.bookmarksList.setItemsExpandable(False)
        self.bookmarksList.setObjectName("bookmarksList")
        self.vboxlayout.addWidget(self.bookmarksList)
        self.errorGroup = QtWidgets.QGroupBox(HgBookmarksInOutDialog)
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
        self.inputGroup = QtWidgets.QGroupBox(HgBookmarksInOutDialog)
        self.inputGroup.setObjectName("inputGroup")
        self.gridlayout = QtWidgets.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.vboxlayout.addWidget(self.inputGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgBookmarksInOutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(HgBookmarksInOutDialog)
        QtCore.QMetaObject.connectSlotsByName(HgBookmarksInOutDialog)
        HgBookmarksInOutDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgBookmarksInOutDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        HgBookmarksInOutDialog.setTabOrder(self.sendButton, self.bookmarksList)
        HgBookmarksInOutDialog.setTabOrder(self.bookmarksList, self.errors)
        HgBookmarksInOutDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, HgBookmarksInOutDialog):
        _translate = QtCore.QCoreApplication.translate
        self.bookmarksList.setWhatsThis(_translate("HgBookmarksInOutDialog", "<b>Bookmarks List</b>\n"
"<p>This shows a list of the bookmarks.</p>"))
        self.bookmarksList.setSortingEnabled(True)
        self.bookmarksList.headerItem().setText(0, _translate("HgBookmarksInOutDialog", "Name"))
        self.bookmarksList.headerItem().setText(1, _translate("HgBookmarksInOutDialog", "Changeset"))
        self.errorGroup.setTitle(_translate("HgBookmarksInOutDialog", "Errors"))
        self.inputGroup.setTitle(_translate("HgBookmarksInOutDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgBookmarksInOutDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgBookmarksInOutDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgBookmarksInOutDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgBookmarksInOutDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgBookmarksInOutDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgBookmarksInOutDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgBookmarksInOutDialog", "Alt+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgBookmarksInOutDialog = QtWidgets.QDialog()
    ui = Ui_HgBookmarksInOutDialog()
    ui.setupUi(HgBookmarksInOutDialog)
    HgBookmarksInOutDialog.show()
    sys.exit(app.exec_())

