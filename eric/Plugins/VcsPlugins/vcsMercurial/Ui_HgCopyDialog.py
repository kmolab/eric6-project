# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgCopyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgCopyDialog(object):
    def setupUi(self, HgCopyDialog):
        HgCopyDialog.setObjectName("HgCopyDialog")
        HgCopyDialog.resize(409, 120)
        HgCopyDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgCopyDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(HgCopyDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.sourceEdit = QtWidgets.QLineEdit(HgCopyDialog)
        self.sourceEdit.setReadOnly(True)
        self.sourceEdit.setObjectName("sourceEdit")
        self.gridLayout.addWidget(self.sourceEdit, 0, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(HgCopyDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridLayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.targetPicker = E5PathPicker(HgCopyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetPicker.sizePolicy().hasHeightForWidth())
        self.targetPicker.setSizePolicy(sizePolicy)
        self.targetPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.targetPicker.setObjectName("targetPicker")
        self.gridLayout.addWidget(self.targetPicker, 1, 1, 1, 1)
        self.forceCheckBox = QtWidgets.QCheckBox(HgCopyDialog)
        self.forceCheckBox.setObjectName("forceCheckBox")
        self.gridLayout.addWidget(self.forceCheckBox, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgCopyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(HgCopyDialog)
        self.buttonBox.accepted.connect(HgCopyDialog.accept)
        self.buttonBox.rejected.connect(HgCopyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgCopyDialog)
        HgCopyDialog.setTabOrder(self.sourceEdit, self.targetPicker)
        HgCopyDialog.setTabOrder(self.targetPicker, self.forceCheckBox)

    def retranslateUi(self, HgCopyDialog):
        _translate = QtCore.QCoreApplication.translate
        HgCopyDialog.setWindowTitle(_translate("HgCopyDialog", "Mercurial Copy"))
        self.textLabel1.setText(_translate("HgCopyDialog", "Source:"))
        self.sourceEdit.setToolTip(_translate("HgCopyDialog", "Shows the name of the source"))
        self.sourceEdit.setWhatsThis(_translate("HgCopyDialog", "<b>Source name</b>\n"
"<p>This field shows the name of the source.</p>"))
        self.textLabel2.setText(_translate("HgCopyDialog", "Target:"))
        self.targetPicker.setToolTip(_translate("HgCopyDialog", "Enter the target name"))
        self.targetPicker.setWhatsThis(_translate("HgCopyDialog", "<b>Target name</b>\n"
"<p>Enter the new name in this field. The target must be the new name or an absolute path.</p>"))
        self.forceCheckBox.setToolTip(_translate("HgCopyDialog", "Select to force the operation"))
        self.forceCheckBox.setText(_translate("HgCopyDialog", "Enforce operation"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgCopyDialog = QtWidgets.QDialog()
    ui = Ui_HgCopyDialog()
    ui.setupUi(HgCopyDialog)
    HgCopyDialog.show()
    sys.exit(app.exec_())

