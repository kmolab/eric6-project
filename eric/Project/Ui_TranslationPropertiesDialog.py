# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\TranslationPropertiesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TranslationPropertiesDialog(object):
    def setupUi(self, TranslationPropertiesDialog):
        TranslationPropertiesDialog.setObjectName("TranslationPropertiesDialog")
        TranslationPropertiesDialog.resize(592, 543)
        TranslationPropertiesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(TranslationPropertiesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textLabel1_3 = QtWidgets.QLabel(TranslationPropertiesDialog)
        self.textLabel1_3.setWordWrap(True)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.verticalLayout.addWidget(self.textLabel1_3)
        self.transPatternPicker = E5PathPicker(TranslationPropertiesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transPatternPicker.sizePolicy().hasHeightForWidth())
        self.transPatternPicker.setSizePolicy(sizePolicy)
        self.transPatternPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.transPatternPicker.setObjectName("transPatternPicker")
        self.verticalLayout.addWidget(self.transPatternPicker)
        self.label = QtWidgets.QLabel(TranslationPropertiesDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.transBinPathPicker = E5PathPicker(TranslationPropertiesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transBinPathPicker.sizePolicy().hasHeightForWidth())
        self.transBinPathPicker.setSizePolicy(sizePolicy)
        self.transBinPathPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.transBinPathPicker.setObjectName("transBinPathPicker")
        self.verticalLayout.addWidget(self.transBinPathPicker)
        self.exceptionsGroup = QtWidgets.QGroupBox(TranslationPropertiesDialog)
        self.exceptionsGroup.setObjectName("exceptionsGroup")
        self._4 = QtWidgets.QGridLayout(self.exceptionsGroup)
        self._4.setObjectName("_4")
        self.exceptDirButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.exceptDirButton.setObjectName("exceptDirButton")
        self._4.addWidget(self.exceptDirButton, 2, 3, 1, 1)
        self.exceptFileButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.exceptFileButton.setObjectName("exceptFileButton")
        self._4.addWidget(self.exceptFileButton, 2, 2, 1, 1)
        self.addExceptionButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.addExceptionButton.setEnabled(False)
        self.addExceptionButton.setObjectName("addExceptionButton")
        self._4.addWidget(self.addExceptionButton, 2, 1, 1, 1)
        self.deleteExceptionButton = QtWidgets.QPushButton(self.exceptionsGroup)
        self.deleteExceptionButton.setEnabled(False)
        self.deleteExceptionButton.setObjectName("deleteExceptionButton")
        self._4.addWidget(self.deleteExceptionButton, 2, 0, 1, 1)
        self.exceptionEdit = QtWidgets.QLineEdit(self.exceptionsGroup)
        self.exceptionEdit.setObjectName("exceptionEdit")
        self._4.addWidget(self.exceptionEdit, 1, 0, 1, 4)
        self.exceptionsList = QtWidgets.QListWidget(self.exceptionsGroup)
        self.exceptionsList.setAlternatingRowColors(True)
        self.exceptionsList.setObjectName("exceptionsList")
        self._4.addWidget(self.exceptionsList, 0, 0, 1, 4)
        self.verticalLayout.addWidget(self.exceptionsGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(TranslationPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.textLabel1_3.setBuddy(self.transPatternPicker)
        self.label.setBuddy(self.transBinPathPicker)

        self.retranslateUi(TranslationPropertiesDialog)
        self.buttonBox.accepted.connect(TranslationPropertiesDialog.accept)
        self.buttonBox.rejected.connect(TranslationPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TranslationPropertiesDialog)
        TranslationPropertiesDialog.setTabOrder(self.transPatternPicker, self.transBinPathPicker)
        TranslationPropertiesDialog.setTabOrder(self.transBinPathPicker, self.exceptionsList)
        TranslationPropertiesDialog.setTabOrder(self.exceptionsList, self.exceptionEdit)
        TranslationPropertiesDialog.setTabOrder(self.exceptionEdit, self.deleteExceptionButton)
        TranslationPropertiesDialog.setTabOrder(self.deleteExceptionButton, self.addExceptionButton)
        TranslationPropertiesDialog.setTabOrder(self.addExceptionButton, self.exceptFileButton)
        TranslationPropertiesDialog.setTabOrder(self.exceptFileButton, self.exceptDirButton)

    def retranslateUi(self, TranslationPropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        TranslationPropertiesDialog.setWindowTitle(_translate("TranslationPropertiesDialog", "Translation Properties"))
        self.textLabel1_3.setText(_translate("TranslationPropertiesDialog", "&Translation Path Pattern:\n"
"(Use \'%language%\' where the language code should be inserted, e.g. i18n/eric6_%language%.ts)"))
        self.transPatternPicker.setToolTip(_translate("TranslationPropertiesDialog", "Enter the path pattern for the translation files"))
        self.transPatternPicker.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Translation Pattern</b>\n"
"<p>Enter the path pattern for the translation files using %language% at the place of the language code (e.g. /path_to_eric/i18n/eric6_%language%.ts). This will result in translation files like /path_to_eric/i18n/eric6_de.ts.</p>"))
        self.label.setText(_translate("TranslationPropertiesDialog", "&Binary Translations Path:"))
        self.transBinPathPicker.setToolTip(_translate("TranslationPropertiesDialog", "Enter the path for the binary translation files (*.qm)"))
        self.transBinPathPicker.setWhatsThis(_translate("TranslationPropertiesDialog", "<b>Binary Translations Path</b>\n"
"<p>Enter the directory for the binary translation files (*.qm). Leave it empty to store them together with the *.ts files.</p>"))
        self.exceptionsGroup.setTitle(_translate("TranslationPropertiesDialog", "Exclude from translation"))
        self.exceptDirButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to select a directory via a selection dialog"))
        self.exceptDirButton.setText(_translate("TranslationPropertiesDialog", "Select d&irectory..."))
        self.exceptFileButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to select a file via a selection dialog"))
        self.exceptFileButton.setText(_translate("TranslationPropertiesDialog", "Select &file..."))
        self.addExceptionButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to add the entered path or file to the list"))
        self.addExceptionButton.setText(_translate("TranslationPropertiesDialog", "&Add"))
        self.deleteExceptionButton.setToolTip(_translate("TranslationPropertiesDialog", "Press to delete the selected entry from the list"))
        self.deleteExceptionButton.setText(_translate("TranslationPropertiesDialog", "&Delete"))
        self.exceptionEdit.setToolTip(_translate("TranslationPropertiesDialog", "Enter a path or file to be added"))
        self.exceptionsList.setToolTip(_translate("TranslationPropertiesDialog", "List of paths or files to excude from translation"))
        self.exceptionsList.setSortingEnabled(True)

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TranslationPropertiesDialog = QtWidgets.QDialog()
    ui = Ui_TranslationPropertiesDialog()
    ui.setupUi(TranslationPropertiesDialog)
    TranslationPropertiesDialog.show()
    sys.exit(app.exec_())

