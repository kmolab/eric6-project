# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnUrlSelectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnUrlSelectionDialog(object):
    def setupUi(self, SvnUrlSelectionDialog):
        SvnUrlSelectionDialog.setObjectName("SvnUrlSelectionDialog")
        SvnUrlSelectionDialog.resize(542, 195)
        SvnUrlSelectionDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnUrlSelectionDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.urlGroup1 = QtWidgets.QGroupBox(SvnUrlSelectionDialog)
        self.urlGroup1.setObjectName("urlGroup1")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.urlGroup1)
        self.hboxlayout.setObjectName("hboxlayout")
        self.repoRootLabel1 = QtWidgets.QLabel(self.urlGroup1)
        self.repoRootLabel1.setObjectName("repoRootLabel1")
        self.hboxlayout.addWidget(self.repoRootLabel1)
        self.typeCombo1 = QtWidgets.QComboBox(self.urlGroup1)
        self.typeCombo1.setObjectName("typeCombo1")
        self.hboxlayout.addWidget(self.typeCombo1)
        self.labelCombo1 = QtWidgets.QComboBox(self.urlGroup1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCombo1.sizePolicy().hasHeightForWidth())
        self.labelCombo1.setSizePolicy(sizePolicy)
        self.labelCombo1.setEditable(True)
        self.labelCombo1.setObjectName("labelCombo1")
        self.hboxlayout.addWidget(self.labelCombo1)
        self.vboxlayout.addWidget(self.urlGroup1)
        self.urlGroup2 = QtWidgets.QGroupBox(SvnUrlSelectionDialog)
        self.urlGroup2.setObjectName("urlGroup2")
        self.hboxlayout1 = QtWidgets.QHBoxLayout(self.urlGroup2)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.repoRootLabel2 = QtWidgets.QLabel(self.urlGroup2)
        self.repoRootLabel2.setObjectName("repoRootLabel2")
        self.hboxlayout1.addWidget(self.repoRootLabel2)
        self.typeCombo2 = QtWidgets.QComboBox(self.urlGroup2)
        self.typeCombo2.setObjectName("typeCombo2")
        self.hboxlayout1.addWidget(self.typeCombo2)
        self.labelCombo2 = QtWidgets.QComboBox(self.urlGroup2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCombo2.sizePolicy().hasHeightForWidth())
        self.labelCombo2.setSizePolicy(sizePolicy)
        self.labelCombo2.setEditable(True)
        self.labelCombo2.setObjectName("labelCombo2")
        self.hboxlayout1.addWidget(self.labelCombo2)
        self.vboxlayout.addWidget(self.urlGroup2)
        self.summaryCheckBox = QtWidgets.QCheckBox(SvnUrlSelectionDialog)
        self.summaryCheckBox.setObjectName("summaryCheckBox")
        self.vboxlayout.addWidget(self.summaryCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnUrlSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnUrlSelectionDialog)
        self.buttonBox.accepted.connect(SvnUrlSelectionDialog.accept)
        self.buttonBox.rejected.connect(SvnUrlSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnUrlSelectionDialog)
        SvnUrlSelectionDialog.setTabOrder(self.typeCombo1, self.labelCombo1)
        SvnUrlSelectionDialog.setTabOrder(self.labelCombo1, self.typeCombo2)
        SvnUrlSelectionDialog.setTabOrder(self.typeCombo2, self.labelCombo2)
        SvnUrlSelectionDialog.setTabOrder(self.labelCombo2, self.summaryCheckBox)
        SvnUrlSelectionDialog.setTabOrder(self.summaryCheckBox, self.buttonBox)

    def retranslateUi(self, SvnUrlSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnUrlSelectionDialog.setWindowTitle(_translate("SvnUrlSelectionDialog", "Subversion Diff"))
        self.urlGroup1.setTitle(_translate("SvnUrlSelectionDialog", "Repository URL 1"))
        self.typeCombo1.setToolTip(_translate("SvnUrlSelectionDialog", "Select the URL type"))
        self.labelCombo1.setToolTip(_translate("SvnUrlSelectionDialog", "Enter the label name or path"))
        self.urlGroup2.setTitle(_translate("SvnUrlSelectionDialog", "Repository URL 2"))
        self.typeCombo2.setToolTip(_translate("SvnUrlSelectionDialog", "Select the URL type"))
        self.labelCombo2.setToolTip(_translate("SvnUrlSelectionDialog", "Enter the label name or path"))
        self.summaryCheckBox.setToolTip(_translate("SvnUrlSelectionDialog", "Select to just show a summary of differences"))
        self.summaryCheckBox.setText(_translate("SvnUrlSelectionDialog", "Summary only"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnUrlSelectionDialog = QtWidgets.QDialog()
    ui = Ui_SvnUrlSelectionDialog()
    ui.setupUi(SvnUrlSelectionDialog)
    SvnUrlSelectionDialog.show()
    sys.exit(app.exec_())

