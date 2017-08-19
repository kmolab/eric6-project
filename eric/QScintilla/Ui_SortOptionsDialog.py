# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\QScintilla\SortOptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SortOptionsDialog(object):
    def setupUi(self, SortOptionsDialog):
        SortOptionsDialog.setObjectName("SortOptionsDialog")
        SortOptionsDialog.resize(400, 209)
        SortOptionsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SortOptionsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.directionGroupBox = QtWidgets.QGroupBox(SortOptionsDialog)
        self.directionGroupBox.setObjectName("directionGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.directionGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ascendingButton = QtWidgets.QRadioButton(self.directionGroupBox)
        self.ascendingButton.setChecked(True)
        self.ascendingButton.setObjectName("ascendingButton")
        self.horizontalLayout.addWidget(self.ascendingButton)
        self.descendingButton = QtWidgets.QRadioButton(self.directionGroupBox)
        self.descendingButton.setChecked(False)
        self.descendingButton.setObjectName("descendingButton")
        self.horizontalLayout.addWidget(self.descendingButton)
        self.verticalLayout.addWidget(self.directionGroupBox)
        self.typeGroupBox = QtWidgets.QGroupBox(SortOptionsDialog)
        self.typeGroupBox.setObjectName("typeGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.typeGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.alnumButton = QtWidgets.QRadioButton(self.typeGroupBox)
        self.alnumButton.setChecked(True)
        self.alnumButton.setObjectName("alnumButton")
        self.horizontalLayout_2.addWidget(self.alnumButton)
        self.numButton = QtWidgets.QRadioButton(self.typeGroupBox)
        self.numButton.setObjectName("numButton")
        self.horizontalLayout_2.addWidget(self.numButton)
        self.verticalLayout.addWidget(self.typeGroupBox)
        self.caseGroupBox = QtWidgets.QGroupBox(SortOptionsDialog)
        self.caseGroupBox.setObjectName("caseGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.caseGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.respectCaseButton = QtWidgets.QRadioButton(self.caseGroupBox)
        self.respectCaseButton.setChecked(True)
        self.respectCaseButton.setObjectName("respectCaseButton")
        self.horizontalLayout_3.addWidget(self.respectCaseButton)
        self.ignoreCaseButton = QtWidgets.QRadioButton(self.caseGroupBox)
        self.ignoreCaseButton.setObjectName("ignoreCaseButton")
        self.horizontalLayout_3.addWidget(self.ignoreCaseButton)
        self.verticalLayout.addWidget(self.caseGroupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SortOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SortOptionsDialog)
        self.buttonBox.accepted.connect(SortOptionsDialog.accept)
        self.buttonBox.rejected.connect(SortOptionsDialog.reject)
        self.alnumButton.toggled['bool'].connect(self.caseGroupBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(SortOptionsDialog)
        SortOptionsDialog.setTabOrder(self.ascendingButton, self.descendingButton)
        SortOptionsDialog.setTabOrder(self.descendingButton, self.alnumButton)
        SortOptionsDialog.setTabOrder(self.alnumButton, self.numButton)
        SortOptionsDialog.setTabOrder(self.numButton, self.respectCaseButton)
        SortOptionsDialog.setTabOrder(self.respectCaseButton, self.ignoreCaseButton)
        SortOptionsDialog.setTabOrder(self.ignoreCaseButton, self.buttonBox)

    def retranslateUi(self, SortOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        SortOptionsDialog.setWindowTitle(_translate("SortOptionsDialog", "Sort Options"))
        self.directionGroupBox.setTitle(_translate("SortOptionsDialog", "Direction"))
        self.ascendingButton.setToolTip(_translate("SortOptionsDialog", "Select to sort in ascending order"))
        self.ascendingButton.setText(_translate("SortOptionsDialog", "Ascending"))
        self.descendingButton.setToolTip(_translate("SortOptionsDialog", "Select to sort in descending order"))
        self.descendingButton.setText(_translate("SortOptionsDialog", "Descending"))
        self.typeGroupBox.setTitle(_translate("SortOptionsDialog", "Type"))
        self.alnumButton.setToolTip(_translate("SortOptionsDialog", "Select to sort alphanumerically"))
        self.alnumButton.setText(_translate("SortOptionsDialog", "Alphanumerical"))
        self.numButton.setToolTip(_translate("SortOptionsDialog", "Select to sort numerically"))
        self.numButton.setText(_translate("SortOptionsDialog", "Numerical"))
        self.caseGroupBox.setTitle(_translate("SortOptionsDialog", "Case Sensitivity"))
        self.respectCaseButton.setToolTip(_translate("SortOptionsDialog", "Select to respect the case while sorting"))
        self.respectCaseButton.setText(_translate("SortOptionsDialog", "Respect Case"))
        self.ignoreCaseButton.setToolTip(_translate("SortOptionsDialog", "Select to ignore the case while sorting"))
        self.ignoreCaseButton.setText(_translate("SortOptionsDialog", "Ignore Case"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SortOptionsDialog = QtWidgets.QDialog()
    ui = Ui_SortOptionsDialog()
    ui.setupUi(SortOptionsDialog)
    SortOptionsDialog.show()
    sys.exit(app.exec_())

