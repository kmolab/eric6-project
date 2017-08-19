# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\QueuesExtension\HgQueuesListGuardsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgQueuesListGuardsDialog(object):
    def setupUi(self, HgQueuesListGuardsDialog):
        HgQueuesListGuardsDialog.setObjectName("HgQueuesListGuardsDialog")
        HgQueuesListGuardsDialog.resize(400, 400)
        HgQueuesListGuardsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgQueuesListGuardsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(HgQueuesListGuardsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.patchSelector = QtWidgets.QComboBox(HgQueuesListGuardsDialog)
        self.patchSelector.setObjectName("patchSelector")
        self.verticalLayout.addWidget(self.patchSelector)
        self.line = QtWidgets.QFrame(HgQueuesListGuardsDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(HgQueuesListGuardsDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.patchNameLabel = QtWidgets.QLabel(HgQueuesListGuardsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patchNameLabel.sizePolicy().hasHeightForWidth())
        self.patchNameLabel.setSizePolicy(sizePolicy)
        self.patchNameLabel.setText("")
        self.patchNameLabel.setObjectName("patchNameLabel")
        self.horizontalLayout.addWidget(self.patchNameLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.guardsList = QtWidgets.QListWidget(HgQueuesListGuardsDialog)
        self.guardsList.setAlternatingRowColors(True)
        self.guardsList.setObjectName("guardsList")
        self.verticalLayout.addWidget(self.guardsList)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgQueuesListGuardsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgQueuesListGuardsDialog)
        self.buttonBox.accepted.connect(HgQueuesListGuardsDialog.accept)
        self.buttonBox.rejected.connect(HgQueuesListGuardsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgQueuesListGuardsDialog)
        HgQueuesListGuardsDialog.setTabOrder(self.patchSelector, self.guardsList)
        HgQueuesListGuardsDialog.setTabOrder(self.guardsList, self.buttonBox)

    def retranslateUi(self, HgQueuesListGuardsDialog):
        _translate = QtCore.QCoreApplication.translate
        HgQueuesListGuardsDialog.setWindowTitle(_translate("HgQueuesListGuardsDialog", "List Guards"))
        self.label.setText(_translate("HgQueuesListGuardsDialog", "Select patch (leave empty for current patch):"))
        self.patchSelector.setToolTip(_translate("HgQueuesListGuardsDialog", "Select the patch to show the guards of"))
        self.label_2.setText(_translate("HgQueuesListGuardsDialog", "Patch:"))
        self.patchNameLabel.setToolTip(_translate("HgQueuesListGuardsDialog", "Shows the name of the patch"))
        self.guardsList.setToolTip(_translate("HgQueuesListGuardsDialog", "This shows the list of guards defined for the selected patch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgQueuesListGuardsDialog = QtWidgets.QDialog()
    ui = Ui_HgQueuesListGuardsDialog()
    ui.setupUi(HgQueuesListGuardsDialog)
    HgQueuesListGuardsDialog.show()
    sys.exit(app.exec_())

