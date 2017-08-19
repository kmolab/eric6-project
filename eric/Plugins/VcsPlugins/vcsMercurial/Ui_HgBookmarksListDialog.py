# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgBookmarksListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgBookmarksListDialog(object):
    def setupUi(self, HgBookmarksListDialog):
        HgBookmarksListDialog.setObjectName("HgBookmarksListDialog")
        HgBookmarksListDialog.resize(634, 494)
        HgBookmarksListDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(HgBookmarksListDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.bookmarksList = QtWidgets.QTreeWidget(HgBookmarksListDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.bookmarksList.sizePolicy().hasHeightForWidth())
        self.bookmarksList.setSizePolicy(sizePolicy)
        self.bookmarksList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.bookmarksList.setAlternatingRowColors(True)
        self.bookmarksList.setRootIsDecorated(False)
        self.bookmarksList.setItemsExpandable(False)
        self.bookmarksList.setObjectName("bookmarksList")
        self.vboxlayout.addWidget(self.bookmarksList)
        self.errorGroup = QtWidgets.QGroupBox(HgBookmarksListDialog)
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
        self.inputGroup = QtWidgets.QGroupBox(HgBookmarksListDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(HgBookmarksListDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(HgBookmarksListDialog)
        QtCore.QMetaObject.connectSlotsByName(HgBookmarksListDialog)
        HgBookmarksListDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgBookmarksListDialog.setTabOrder(self.passwordCheckBox, self.sendButton)
        HgBookmarksListDialog.setTabOrder(self.sendButton, self.bookmarksList)
        HgBookmarksListDialog.setTabOrder(self.bookmarksList, self.errors)
        HgBookmarksListDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, HgBookmarksListDialog):
        _translate = QtCore.QCoreApplication.translate
        HgBookmarksListDialog.setWindowTitle(_translate("HgBookmarksListDialog", "Mercurial Bookmarks"))
        HgBookmarksListDialog.setWhatsThis(_translate("HgBookmarksListDialog", "<b>Mercurial Bookmarks</b>\n"
"<p>This dialog shows a list of the projects bookmarks.</p>"))
        self.bookmarksList.setWhatsThis(_translate("HgBookmarksListDialog", "<b>Bookmarks List</b>\n"
"<p>This shows a list of the projects bookmarks.</p>"))
        self.bookmarksList.setSortingEnabled(True)
        self.bookmarksList.headerItem().setText(0, _translate("HgBookmarksListDialog", "Revision"))
        self.bookmarksList.headerItem().setText(1, _translate("HgBookmarksListDialog", "Changeset"))
        self.bookmarksList.headerItem().setText(2, _translate("HgBookmarksListDialog", "Status"))
        self.bookmarksList.headerItem().setText(3, _translate("HgBookmarksListDialog", "Name"))
        self.errorGroup.setTitle(_translate("HgBookmarksListDialog", "Errors"))
        self.inputGroup.setTitle(_translate("HgBookmarksListDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgBookmarksListDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgBookmarksListDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgBookmarksListDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgBookmarksListDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgBookmarksListDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgBookmarksListDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgBookmarksListDialog", "Alt+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgBookmarksListDialog = QtWidgets.QDialog()
    ui = Ui_HgBookmarksListDialog()
    ui.setupUi(HgBookmarksListDialog)
    HgBookmarksListDialog.show()
    sys.exit(app.exec_())

