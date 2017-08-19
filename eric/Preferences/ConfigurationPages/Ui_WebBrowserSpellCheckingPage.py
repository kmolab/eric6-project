# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\WebBrowserSpellCheckingPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WebBrowserSpellCheckingPage(object):
    def setupUi(self, WebBrowserSpellCheckingPage):
        WebBrowserSpellCheckingPage.setObjectName("WebBrowserSpellCheckingPage")
        WebBrowserSpellCheckingPage.resize(499, 550)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(WebBrowserSpellCheckingPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headerLabel = QtWidgets.QLabel(WebBrowserSpellCheckingPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_3.addWidget(self.headerLabel)
        self.line17 = QtWidgets.QFrame(WebBrowserSpellCheckingPage)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setObjectName("line17")
        self.verticalLayout_3.addWidget(self.line17)
        self.groupBox = QtWidgets.QGroupBox(WebBrowserSpellCheckingPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spellCheckEnabledCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.spellCheckEnabledCheckBox.setObjectName("spellCheckEnabledCheckBox")
        self.verticalLayout.addWidget(self.spellCheckEnabledCheckBox)
        self.noLanguagesLabel = QtWidgets.QLabel(self.groupBox)
        self.noLanguagesLabel.setObjectName("noLanguagesLabel")
        self.verticalLayout.addWidget(self.noLanguagesLabel)
        self.spellCheckLanguagesList = QtWidgets.QListWidget(self.groupBox)
        self.spellCheckLanguagesList.setDragEnabled(True)
        self.spellCheckLanguagesList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.spellCheckLanguagesList.setAlternatingRowColors(True)
        self.spellCheckLanguagesList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.spellCheckLanguagesList.setObjectName("spellCheckLanguagesList")
        self.verticalLayout.addWidget(self.spellCheckLanguagesList)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(WebBrowserSpellCheckingPage)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spellCheckDictionaryDirectoriesEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.spellCheckDictionaryDirectoriesEdit.setTabChangesFocus(True)
        self.spellCheckDictionaryDirectoriesEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.spellCheckDictionaryDirectoriesEdit.setReadOnly(True)
        self.spellCheckDictionaryDirectoriesEdit.setObjectName("spellCheckDictionaryDirectoriesEdit")
        self.verticalLayout_2.addWidget(self.spellCheckDictionaryDirectoriesEdit)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(WebBrowserSpellCheckingPage)
        QtCore.QMetaObject.connectSlotsByName(WebBrowserSpellCheckingPage)
        WebBrowserSpellCheckingPage.setTabOrder(self.spellCheckEnabledCheckBox, self.spellCheckLanguagesList)
        WebBrowserSpellCheckingPage.setTabOrder(self.spellCheckLanguagesList, self.spellCheckDictionaryDirectoriesEdit)

    def retranslateUi(self, WebBrowserSpellCheckingPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("WebBrowserSpellCheckingPage", "<b>Configure Web Browser Spell Checking</b>"))
        self.groupBox.setTitle(_translate("WebBrowserSpellCheckingPage", "Spell Check Options"))
        self.spellCheckEnabledCheckBox.setToolTip(_translate("WebBrowserSpellCheckingPage", "Select to enable spell checking for editable parts"))
        self.spellCheckEnabledCheckBox.setText(_translate("WebBrowserSpellCheckingPage", "Enable Spell Checking"))
        self.noLanguagesLabel.setText(_translate("WebBrowserSpellCheckingPage", "No languages found"))
        self.groupBox_2.setTitle(_translate("WebBrowserSpellCheckingPage", "Dictionary Directories"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WebBrowserSpellCheckingPage = QtWidgets.QWidget()
    ui = Ui_WebBrowserSpellCheckingPage()
    ui.setupUi(WebBrowserSpellCheckingPage)
    WebBrowserSpellCheckingPage.show()
    sys.exit(app.exec_())

