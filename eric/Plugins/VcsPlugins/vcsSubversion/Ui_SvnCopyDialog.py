# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnCopyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnCopyDialog(object):
    def setupUi(self, SvnCopyDialog):
        SvnCopyDialog.setObjectName("SvnCopyDialog")
        SvnCopyDialog.resize(409, 138)
        SvnCopyDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(SvnCopyDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(SvnCopyDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.sourceEdit = QtWidgets.QLineEdit(SvnCopyDialog)
        self.sourceEdit.setReadOnly(True)
        self.sourceEdit.setObjectName("sourceEdit")
        self.gridLayout.addWidget(self.sourceEdit, 0, 1, 1, 1)
        self.textLabel2 = QtWidgets.QLabel(SvnCopyDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.gridLayout.addWidget(self.textLabel2, 1, 0, 1, 1)
        self.targetPicker = E5PathPicker(SvnCopyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetPicker.sizePolicy().hasHeightForWidth())
        self.targetPicker.setSizePolicy(sizePolicy)
        self.targetPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.targetPicker.setObjectName("targetPicker")
        self.gridLayout.addWidget(self.targetPicker, 1, 1, 1, 1)
        self.forceCheckBox = QtWidgets.QCheckBox(SvnCopyDialog)
        self.forceCheckBox.setObjectName("forceCheckBox")
        self.gridLayout.addWidget(self.forceCheckBox, 2, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnCopyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(SvnCopyDialog)
        self.buttonBox.accepted.connect(SvnCopyDialog.accept)
        self.buttonBox.rejected.connect(SvnCopyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnCopyDialog)
        SvnCopyDialog.setTabOrder(self.sourceEdit, self.targetPicker)
        SvnCopyDialog.setTabOrder(self.targetPicker, self.forceCheckBox)

    def retranslateUi(self, SvnCopyDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnCopyDialog.setWindowTitle(_translate("SvnCopyDialog", "Subversion Copy"))
        self.textLabel1.setText(_translate("SvnCopyDialog", "Source:"))
        self.sourceEdit.setToolTip(_translate("SvnCopyDialog", "Shows the name of the source"))
        self.sourceEdit.setWhatsThis(_translate("SvnCopyDialog", "<b>Source name</b>\n"
"<p>This field shows the name of the source.</p>"))
        self.textLabel2.setText(_translate("SvnCopyDialog", "Target:"))
        self.targetPicker.setToolTip(_translate("SvnCopyDialog", "Enter the target name"))
        self.targetPicker.setWhatsThis(_translate("SvnCopyDialog", "<b>Target name</b>\n"
"<p>Enter the new name in this field. The target must be the new name or an absolute path.</p>"))
        self.forceCheckBox.setToolTip(_translate("SvnCopyDialog", "Select to force the operation"))
        self.forceCheckBox.setText(_translate("SvnCopyDialog", "Enforce operation"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnCopyDialog = QtWidgets.QDialog()
    ui = Ui_SvnCopyDialog()
    ui.setupUi(SvnCopyDialog)
    SvnCopyDialog.show()
    sys.exit(app.exec_())

