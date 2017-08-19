# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\FetchExtension\HgFetchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgFetchDialog(object):
    def setupUi(self, HgFetchDialog):
        HgFetchDialog.setObjectName("HgFetchDialog")
        HgFetchDialog.resize(400, 300)
        HgFetchDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(HgFetchDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(HgFetchDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.messageEdit.setTabChangesFocus(True)
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout.addWidget(self.messageEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.recentComboBox = QtWidgets.QComboBox(self.groupBox)
        self.recentComboBox.setObjectName("recentComboBox")
        self.verticalLayout.addWidget(self.recentComboBox)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.switchCheckBox = QtWidgets.QCheckBox(HgFetchDialog)
        self.switchCheckBox.setObjectName("switchCheckBox")
        self.verticalLayout_2.addWidget(self.switchCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgFetchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(HgFetchDialog)
        self.buttonBox.accepted.connect(HgFetchDialog.accept)
        self.buttonBox.rejected.connect(HgFetchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgFetchDialog)
        HgFetchDialog.setTabOrder(self.messageEdit, self.recentComboBox)
        HgFetchDialog.setTabOrder(self.recentComboBox, self.switchCheckBox)
        HgFetchDialog.setTabOrder(self.switchCheckBox, self.buttonBox)

    def retranslateUi(self, HgFetchDialog):
        _translate = QtCore.QCoreApplication.translate
        HgFetchDialog.setWindowTitle(_translate("HgFetchDialog", "Fetch Changes"))
        self.groupBox.setTitle(_translate("HgFetchDialog", "Commit Message"))
        self.messageEdit.setToolTip(_translate("HgFetchDialog", "Enter commit message or leave empty to use the default message"))
        self.label_2.setText(_translate("HgFetchDialog", "Recent commit messages"))
        self.recentComboBox.setToolTip(_translate("HgFetchDialog", "Select a recent commit message to use"))
        self.switchCheckBox.setToolTip(_translate("HgFetchDialog", "Select to switch the merge order"))
        self.switchCheckBox.setText(_translate("HgFetchDialog", "Switch Parents when Merging"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgFetchDialog = QtWidgets.QDialog()
    ui = Ui_HgFetchDialog()
    ui.setupUi(HgFetchDialog)
    HgFetchDialog.show()
    sys.exit(app.exec_())

