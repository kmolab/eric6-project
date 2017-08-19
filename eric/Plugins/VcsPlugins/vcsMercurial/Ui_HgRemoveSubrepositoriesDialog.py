# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgRemoveSubrepositoriesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgRemoveSubrepositoriesDialog(object):
    def setupUi(self, HgRemoveSubrepositoriesDialog):
        HgRemoveSubrepositoriesDialog.setObjectName("HgRemoveSubrepositoriesDialog")
        HgRemoveSubrepositoriesDialog.resize(500, 300)
        HgRemoveSubrepositoriesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgRemoveSubrepositoriesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subrepositories = QtWidgets.QListWidget(HgRemoveSubrepositoriesDialog)
        self.subrepositories.setAlternatingRowColors(True)
        self.subrepositories.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.subrepositories.setObjectName("subrepositories")
        self.verticalLayout.addWidget(self.subrepositories)
        self.removeButton = QtWidgets.QPushButton(HgRemoveSubrepositoriesDialog)
        self.removeButton.setEnabled(False)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        self.deleteCheckBox = QtWidgets.QCheckBox(HgRemoveSubrepositoriesDialog)
        self.deleteCheckBox.setObjectName("deleteCheckBox")
        self.verticalLayout.addWidget(self.deleteCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgRemoveSubrepositoriesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgRemoveSubrepositoriesDialog)
        self.buttonBox.accepted.connect(HgRemoveSubrepositoriesDialog.accept)
        self.buttonBox.rejected.connect(HgRemoveSubrepositoriesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgRemoveSubrepositoriesDialog)
        HgRemoveSubrepositoriesDialog.setTabOrder(self.subrepositories, self.removeButton)
        HgRemoveSubrepositoriesDialog.setTabOrder(self.removeButton, self.deleteCheckBox)
        HgRemoveSubrepositoriesDialog.setTabOrder(self.deleteCheckBox, self.buttonBox)

    def retranslateUi(self, HgRemoveSubrepositoriesDialog):
        _translate = QtCore.QCoreApplication.translate
        HgRemoveSubrepositoriesDialog.setWindowTitle(_translate("HgRemoveSubrepositoriesDialog", "Remove Sub-repositories"))
        self.removeButton.setToolTip(_translate("HgRemoveSubrepositoriesDialog", "Press to remove the selected entries"))
        self.removeButton.setText(_translate("HgRemoveSubrepositoriesDialog", "&Remove"))
        self.deleteCheckBox.setToolTip(_translate("HgRemoveSubrepositoriesDialog", "Select to delete the removed entries from disc"))
        self.deleteCheckBox.setText(_translate("HgRemoveSubrepositoriesDialog", "Delete removed entries from disc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgRemoveSubrepositoriesDialog = QtWidgets.QDialog()
    ui = Ui_HgRemoveSubrepositoriesDialog()
    ui.setupUi(HgRemoveSubrepositoriesDialog)
    HgRemoveSubrepositoriesDialog.show()
    sys.exit(app.exec_())

