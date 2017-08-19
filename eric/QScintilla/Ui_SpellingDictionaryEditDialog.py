# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\QScintilla\SpellingDictionaryEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpellingDictionaryEditDialog(object):
    def setupUi(self, SpellingDictionaryEditDialog):
        SpellingDictionaryEditDialog.setObjectName("SpellingDictionaryEditDialog")
        SpellingDictionaryEditDialog.resize(500, 400)
        SpellingDictionaryEditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SpellingDictionaryEditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoLabel = QtWidgets.QLabel(SpellingDictionaryEditDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.infoLabel.setFont(font)
        self.infoLabel.setText("")
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        self.line_2 = QtWidgets.QFrame(SpellingDictionaryEditDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.searchEdit = E5ClearableLineEdit(SpellingDictionaryEditDialog)
        self.searchEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.searchEdit.setToolTip("")
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout.addWidget(self.searchEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(SpellingDictionaryEditDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.addButton = QtWidgets.QPushButton(SpellingDictionaryEditDialog)
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 0, 1, 1, 1)
        self.removeButton = QtWidgets.QPushButton(SpellingDictionaryEditDialog)
        self.removeButton.setAutoDefault(False)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 1, 1, 1)
        self.removeAllButton = QtWidgets.QPushButton(SpellingDictionaryEditDialog)
        self.removeAllButton.setAutoDefault(False)
        self.removeAllButton.setObjectName("removeAllButton")
        self.gridLayout.addWidget(self.removeAllButton, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.wordList = E5ListView(SpellingDictionaryEditDialog)
        self.wordList.setAlternatingRowColors(True)
        self.wordList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.wordList.setObjectName("wordList")
        self.gridLayout.addWidget(self.wordList, 0, 0, 5, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SpellingDictionaryEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SpellingDictionaryEditDialog)
        self.buttonBox.accepted.connect(SpellingDictionaryEditDialog.accept)
        self.buttonBox.rejected.connect(SpellingDictionaryEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SpellingDictionaryEditDialog)
        SpellingDictionaryEditDialog.setTabOrder(self.searchEdit, self.wordList)
        SpellingDictionaryEditDialog.setTabOrder(self.wordList, self.removeButton)
        SpellingDictionaryEditDialog.setTabOrder(self.removeButton, self.removeAllButton)
        SpellingDictionaryEditDialog.setTabOrder(self.removeAllButton, self.buttonBox)

    def retranslateUi(self, SpellingDictionaryEditDialog):
        _translate = QtCore.QCoreApplication.translate
        SpellingDictionaryEditDialog.setWindowTitle(_translate("SpellingDictionaryEditDialog", "Edit Spelling Dictionary"))
        self.searchEdit.setPlaceholderText(_translate("SpellingDictionaryEditDialog", "Enter search term"))
        self.addButton.setToolTip(_translate("SpellingDictionaryEditDialog", "Press to add an entry"))
        self.addButton.setText(_translate("SpellingDictionaryEditDialog", "&Add"))
        self.removeButton.setToolTip(_translate("SpellingDictionaryEditDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("SpellingDictionaryEditDialog", "&Remove"))
        self.removeAllButton.setToolTip(_translate("SpellingDictionaryEditDialog", "Press to remove all entries"))
        self.removeAllButton.setText(_translate("SpellingDictionaryEditDialog", "R&emove All"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5ListView import E5ListView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpellingDictionaryEditDialog = QtWidgets.QDialog()
    ui = Ui_SpellingDictionaryEditDialog()
    ui.setupUi(SpellingDictionaryEditDialog)
    SpellingDictionaryEditDialog.show()
    sys.exit(app.exec_())

