# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\QueuesExtension\HgQueuesQueueManagementDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesQueueManagementDialog(object):
    def setupUi(self, HgQueuesQueueManagementDialog):
        HgQueuesQueueManagementDialog.setObjectName("HgQueuesQueueManagementDialog")
        HgQueuesQueueManagementDialog.resize(400, 300)
        HgQueuesQueueManagementDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgQueuesQueueManagementDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputFrame = QtWidgets.QFrame(HgQueuesQueueManagementDialog)
        self.inputFrame.setObjectName("inputFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.inputFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.inputFrame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameEdit = QtWidgets.QLineEdit(self.inputFrame)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout.addWidget(self.nameEdit)
        self.verticalLayout.addWidget(self.inputFrame)
        self.selectLabel = QtWidgets.QLabel(HgQueuesQueueManagementDialog)
        self.selectLabel.setObjectName("selectLabel")
        self.verticalLayout.addWidget(self.selectLabel)
        self.queuesList = QtWidgets.QListWidget(HgQueuesQueueManagementDialog)
        self.queuesList.setAlternatingRowColors(True)
        self.queuesList.setObjectName("queuesList")
        self.verticalLayout.addWidget(self.queuesList)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesQueueManagementDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgQueuesQueueManagementDialog)
        self.buttonBox.accepted.connect(HgQueuesQueueManagementDialog.accept)
        self.buttonBox.rejected.connect(HgQueuesQueueManagementDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesQueueManagementDialog)
        HgQueuesQueueManagementDialog.setTabOrder(self.nameEdit, self.queuesList)
        HgQueuesQueueManagementDialog.setTabOrder(self.queuesList, self.buttonBox)

    def retranslateUi(self, HgQueuesQueueManagementDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("HgQueuesQueueManagementDialog", "Queue Name:"))
        self.nameEdit.setToolTip(_translate("HgQueuesQueueManagementDialog", "Enter the queue name"))
        self.selectLabel.setText(_translate("HgQueuesQueueManagementDialog", "Select queue name:"))
        self.queuesList.setToolTip(_translate("HgQueuesQueueManagementDialog", "This shows a list of available queues (active queue in bold)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgQueuesQueueManagementDialog = QtWidgets.QDialog()
    ui = Ui_HgQueuesQueueManagementDialog()
    ui.setupUi(HgQueuesQueueManagementDialog)
    HgQueuesQueueManagementDialog.show()
    sys.exit(app.exec_())

