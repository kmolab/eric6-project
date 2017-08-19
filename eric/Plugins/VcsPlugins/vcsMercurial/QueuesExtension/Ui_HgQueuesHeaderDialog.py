# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\QueuesExtension\HgQueuesHeaderDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesHeaderDialog(object):
    def setupUi(self, HgQueuesHeaderDialog):
        HgQueuesHeaderDialog.setObjectName("HgQueuesHeaderDialog")
        HgQueuesHeaderDialog.resize(400, 300)
        HgQueuesHeaderDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgQueuesHeaderDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messageEdit = QtWidgets.QPlainTextEdit(HgQueuesHeaderDialog)
        self.messageEdit.setReadOnly(True)
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout.addWidget(self.messageEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesHeaderDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgQueuesHeaderDialog)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesHeaderDialog)
        HgQueuesHeaderDialog.setTabOrder(self.messageEdit, self.buttonBox)

    def retranslateUi(self, HgQueuesHeaderDialog):
        _translate = QtCore.QCoreApplication.translate
        HgQueuesHeaderDialog.setWindowTitle(_translate("HgQueuesHeaderDialog", "Commit Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgQueuesHeaderDialog = QtWidgets.QDialog()
    ui = Ui_HgQueuesHeaderDialog()
    ui.setupUi(HgQueuesHeaderDialog)
    HgQueuesHeaderDialog.show()
    sys.exit(app.exec_())

