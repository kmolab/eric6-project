# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\WizardPlugins\PyRegExpWizard\PyRegExpWizardCharactersDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyRegExpWizardCharactersDialog(object):
    def setupUi(self, PyRegExpWizardCharactersDialog):
        PyRegExpWizardCharactersDialog.setObjectName("PyRegExpWizardCharactersDialog")
        PyRegExpWizardCharactersDialog.resize(800, 500)
        PyRegExpWizardCharactersDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(PyRegExpWizardCharactersDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.negativeCheckBox = QtWidgets.QCheckBox(PyRegExpWizardCharactersDialog)
        self.negativeCheckBox.setObjectName("negativeCheckBox")
        self.vboxlayout.addWidget(self.negativeCheckBox)
        self.groupBox = QtWidgets.QGroupBox(PyRegExpWizardCharactersDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.nonWhitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonWhitespaceCheckBox.setObjectName("nonWhitespaceCheckBox")
        self.gridlayout.addWidget(self.nonWhitespaceCheckBox, 1, 2, 1, 1)
        self.nonDigitsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonDigitsCheckBox.setObjectName("nonDigitsCheckBox")
        self.gridlayout.addWidget(self.nonDigitsCheckBox, 1, 1, 1, 1)
        self.whitespaceCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.whitespaceCheckBox.setObjectName("whitespaceCheckBox")
        self.gridlayout.addWidget(self.whitespaceCheckBox, 0, 2, 1, 1)
        self.digitsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.digitsCheckBox.setObjectName("digitsCheckBox")
        self.gridlayout.addWidget(self.digitsCheckBox, 0, 1, 1, 1)
        self.nonWordCharCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.nonWordCharCheckBox.setObjectName("nonWordCharCheckBox")
        self.gridlayout.addWidget(self.nonWordCharCheckBox, 1, 0, 1, 1)
        self.wordCharCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.wordCharCheckBox.setObjectName("wordCharCheckBox")
        self.gridlayout.addWidget(self.wordCharCheckBox, 0, 0, 1, 1)
        self.vboxlayout.addWidget(self.groupBox)
        self.singlesBox = QtWidgets.QGroupBox(PyRegExpWizardCharactersDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.singlesBox.sizePolicy().hasHeightForWidth())
        self.singlesBox.setSizePolicy(sizePolicy)
        self.singlesBox.setObjectName("singlesBox")
        self.vboxlayout.addWidget(self.singlesBox)
        self.rangesBox = QtWidgets.QGroupBox(PyRegExpWizardCharactersDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangesBox.sizePolicy().hasHeightForWidth())
        self.rangesBox.setSizePolicy(sizePolicy)
        self.rangesBox.setObjectName("rangesBox")
        self.vboxlayout.addWidget(self.rangesBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(PyRegExpWizardCharactersDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PyRegExpWizardCharactersDialog)
        self.buttonBox.accepted.connect(PyRegExpWizardCharactersDialog.accept)
        self.buttonBox.rejected.connect(PyRegExpWizardCharactersDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PyRegExpWizardCharactersDialog)
        PyRegExpWizardCharactersDialog.setTabOrder(self.negativeCheckBox, self.wordCharCheckBox)
        PyRegExpWizardCharactersDialog.setTabOrder(self.wordCharCheckBox, self.nonWordCharCheckBox)
        PyRegExpWizardCharactersDialog.setTabOrder(self.nonWordCharCheckBox, self.digitsCheckBox)
        PyRegExpWizardCharactersDialog.setTabOrder(self.digitsCheckBox, self.nonDigitsCheckBox)
        PyRegExpWizardCharactersDialog.setTabOrder(self.nonDigitsCheckBox, self.whitespaceCheckBox)
        PyRegExpWizardCharactersDialog.setTabOrder(self.whitespaceCheckBox, self.nonWhitespaceCheckBox)

    def retranslateUi(self, PyRegExpWizardCharactersDialog):
        _translate = QtCore.QCoreApplication.translate
        PyRegExpWizardCharactersDialog.setWindowTitle(_translate("PyRegExpWizardCharactersDialog", "Editor for character sets"))
        self.negativeCheckBox.setText(_translate("PyRegExpWizardCharactersDialog", "The defined characters should not match"))
        self.groupBox.setTitle(_translate("PyRegExpWizardCharactersDialog", "Predefined character ranges"))
        self.nonWhitespaceCheckBox.setText(_translate("PyRegExpWizardCharactersDialog", "Non-whitespace characters"))
        self.nonDigitsCheckBox.setText(_translate("PyRegExpWizardCharactersDialog", "Non-digits"))
        self.whitespaceCheckBox.setText(_translate("PyRegExpWizardCharactersDialog", "Whitespace characters"))
        self.digitsCheckBox.setText(_translate("PyRegExpWizardCharactersDialog", "Digits"))
        self.nonWordCharCheckBox.setText(_translate("PyRegExpWizardCharactersDialog", "Non-word characters"))
        self.wordCharCheckBox.setText(_translate("PyRegExpWizardCharactersDialog", "Word character"))
        self.singlesBox.setTitle(_translate("PyRegExpWizardCharactersDialog", "Single character"))
        self.rangesBox.setTitle(_translate("PyRegExpWizardCharactersDialog", "Character ranges"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyRegExpWizardCharactersDialog = QtWidgets.QDialog()
    ui = Ui_PyRegExpWizardCharactersDialog()
    ui.setupUi(PyRegExpWizardCharactersDialog)
    PyRegExpWizardCharactersDialog.show()
    sys.exit(app.exec_())

