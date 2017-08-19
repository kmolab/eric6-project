# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgPhaseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgPhaseDialog(object):
    def setupUi(self, HgPhaseDialog):
        HgPhaseDialog.setObjectName("HgPhaseDialog")
        HgPhaseDialog.resize(400, 186)
        HgPhaseDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgPhaseDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(HgPhaseDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.revisionsEdit = QtWidgets.QPlainTextEdit(HgPhaseDialog)
        self.revisionsEdit.setTabChangesFocus(True)
        self.revisionsEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.revisionsEdit.setObjectName("revisionsEdit")
        self.gridLayout.addWidget(self.revisionsEdit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(HgPhaseDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.phaseCombo = QtWidgets.QComboBox(HgPhaseDialog)
        self.phaseCombo.setObjectName("phaseCombo")
        self.gridLayout.addWidget(self.phaseCombo, 1, 1, 1, 1)
        self.forceCheckBox = QtWidgets.QCheckBox(HgPhaseDialog)
        self.forceCheckBox.setObjectName("forceCheckBox")
        self.gridLayout.addWidget(self.forceCheckBox, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgPhaseDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.label_5.setBuddy(self.revisionsEdit)

        self.retranslateUi(HgPhaseDialog)
        self.buttonBox.accepted.connect(HgPhaseDialog.accept)
        self.buttonBox.rejected.connect(HgPhaseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgPhaseDialog)
        HgPhaseDialog.setTabOrder(self.revisionsEdit, self.phaseCombo)
        HgPhaseDialog.setTabOrder(self.phaseCombo, self.forceCheckBox)
        HgPhaseDialog.setTabOrder(self.forceCheckBox, self.buttonBox)

    def retranslateUi(self, HgPhaseDialog):
        _translate = QtCore.QCoreApplication.translate
        HgPhaseDialog.setWindowTitle(_translate("HgPhaseDialog", "Mercurial Phases"))
        self.label_5.setText(_translate("HgPhaseDialog", "&Revisions:"))
        self.revisionsEdit.setToolTip(_translate("HgPhaseDialog", "Enter revisions by number, id, range or revset expression one per line"))
        self.label.setText(_translate("HgPhaseDialog", "Phase:"))
        self.phaseCombo.setToolTip(_translate("HgPhaseDialog", "Select the phase to be set for the specified revisions"))
        self.forceCheckBox.setToolTip(_translate("HgPhaseDialog", "Select to force the phase change"))
        self.forceCheckBox.setText(_translate("HgPhaseDialog", "Force Phase Change"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgPhaseDialog = QtWidgets.QDialog()
    ui = Ui_HgPhaseDialog()
    ui.setupUi(HgPhaseDialog)
    HgPhaseDialog.show()
    sys.exit(app.exec_())

