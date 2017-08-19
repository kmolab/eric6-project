# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\SpellingPropertiesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpellingPropertiesDialog(object):
    def setupUi(self, SpellingPropertiesDialog):
        SpellingPropertiesDialog.setObjectName("SpellingPropertiesDialog")
        SpellingPropertiesDialog.resize(600, 114)
        SpellingPropertiesDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(SpellingPropertiesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1_3 = QtWidgets.QLabel(SpellingPropertiesDialog)
        self.textLabel1_3.setObjectName("textLabel1_3")
        self.gridLayout.addWidget(self.textLabel1_3, 0, 0, 1, 1)
        self.spellingComboBox = QtWidgets.QComboBox(SpellingPropertiesDialog)
        self.spellingComboBox.setObjectName("spellingComboBox")
        self.gridLayout.addWidget(self.spellingComboBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(SpellingPropertiesDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pwlPicker = E5PathPicker(SpellingPropertiesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwlPicker.sizePolicy().hasHeightForWidth())
        self.pwlPicker.setSizePolicy(sizePolicy)
        self.pwlPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pwlPicker.setObjectName("pwlPicker")
        self.gridLayout.addWidget(self.pwlPicker, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(SpellingPropertiesDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pelPicker = E5PathPicker(SpellingPropertiesDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pelPicker.sizePolicy().hasHeightForWidth())
        self.pelPicker.setSizePolicy(sizePolicy)
        self.pelPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pelPicker.setObjectName("pelPicker")
        self.gridLayout.addWidget(self.pelPicker, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(SpellingPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.textLabel1_3.setBuddy(self.spellingComboBox)
        self.label.setBuddy(self.pwlPicker)
        self.label_2.setBuddy(self.pelPicker)

        self.retranslateUi(SpellingPropertiesDialog)
        self.buttonBox.accepted.connect(SpellingPropertiesDialog.accept)
        self.buttonBox.rejected.connect(SpellingPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SpellingPropertiesDialog)
        SpellingPropertiesDialog.setTabOrder(self.spellingComboBox, self.buttonBox)

    def retranslateUi(self, SpellingPropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        SpellingPropertiesDialog.setWindowTitle(_translate("SpellingPropertiesDialog", "Spelling Properties"))
        self.textLabel1_3.setText(_translate("SpellingPropertiesDialog", "Project &Language:"))
        self.spellingComboBox.setToolTip(_translate("SpellingPropertiesDialog", "Select the project\'s language"))
        self.label.setText(_translate("SpellingPropertiesDialog", "Project &Word List:"))
        self.pwlPicker.setToolTip(_translate("SpellingPropertiesDialog", "Enter the filename of the project word list"))
        self.label_2.setText(_translate("SpellingPropertiesDialog", "Project E&xclude List:"))
        self.pelPicker.setToolTip(_translate("SpellingPropertiesDialog", "Enter the filename of the project exclude list"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpellingPropertiesDialog = QtWidgets.QDialog()
    ui = Ui_SpellingPropertiesDialog()
    ui.setupUi(SpellingPropertiesDialog)
    SpellingPropertiesDialog.show()
    sys.exit(app.exec_())

