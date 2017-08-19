# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\ClearPrivateDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClearPrivateDataDialog(object):
    def setupUi(self, ClearPrivateDataDialog):
        ClearPrivateDataDialog.setObjectName("ClearPrivateDataDialog")
        ClearPrivateDataDialog.resize(400, 211)
        ClearPrivateDataDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ClearPrivateDataDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filesCheckBox = QtWidgets.QCheckBox(ClearPrivateDataDialog)
        self.filesCheckBox.setChecked(True)
        self.filesCheckBox.setObjectName("filesCheckBox")
        self.verticalLayout.addWidget(self.filesCheckBox)
        self.projectsCheckBox = QtWidgets.QCheckBox(ClearPrivateDataDialog)
        self.projectsCheckBox.setChecked(True)
        self.projectsCheckBox.setObjectName("projectsCheckBox")
        self.verticalLayout.addWidget(self.projectsCheckBox)
        self.multiProjectsCheckBox = QtWidgets.QCheckBox(ClearPrivateDataDialog)
        self.multiProjectsCheckBox.setChecked(True)
        self.multiProjectsCheckBox.setObjectName("multiProjectsCheckBox")
        self.verticalLayout.addWidget(self.multiProjectsCheckBox)
        self.debugCheckBox = QtWidgets.QCheckBox(ClearPrivateDataDialog)
        self.debugCheckBox.setChecked(True)
        self.debugCheckBox.setObjectName("debugCheckBox")
        self.verticalLayout.addWidget(self.debugCheckBox)
        self.shellCheckBox = QtWidgets.QCheckBox(ClearPrivateDataDialog)
        self.shellCheckBox.setChecked(True)
        self.shellCheckBox.setObjectName("shellCheckBox")
        self.verticalLayout.addWidget(self.shellCheckBox)
        self.vcsCheckBox = QtWidgets.QCheckBox(ClearPrivateDataDialog)
        self.vcsCheckBox.setChecked(True)
        self.vcsCheckBox.setObjectName("vcsCheckBox")
        self.verticalLayout.addWidget(self.vcsCheckBox)
        self.line = QtWidgets.QFrame(ClearPrivateDataDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pluginsCheckBox = QtWidgets.QCheckBox(ClearPrivateDataDialog)
        self.pluginsCheckBox.setChecked(True)
        self.pluginsCheckBox.setObjectName("pluginsCheckBox")
        self.verticalLayout.addWidget(self.pluginsCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(ClearPrivateDataDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ClearPrivateDataDialog)
        self.buttonBox.accepted.connect(ClearPrivateDataDialog.accept)
        self.buttonBox.rejected.connect(ClearPrivateDataDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ClearPrivateDataDialog)

    def retranslateUi(self, ClearPrivateDataDialog):
        _translate = QtCore.QCoreApplication.translate
        ClearPrivateDataDialog.setWindowTitle(_translate("ClearPrivateDataDialog", "Clear Private Data"))
        self.filesCheckBox.setToolTip(_translate("ClearPrivateDataDialog", "Select to clear the list of recently opened files"))
        self.filesCheckBox.setText(_translate("ClearPrivateDataDialog", "Recently opened files"))
        self.projectsCheckBox.setToolTip(_translate("ClearPrivateDataDialog", "Select to clear the list of recently opened projects and project related histories"))
        self.projectsCheckBox.setText(_translate("ClearPrivateDataDialog", "Recently opened projects and project histories"))
        self.multiProjectsCheckBox.setToolTip(_translate("ClearPrivateDataDialog", "Select to clear the list of recently opened multi projects"))
        self.multiProjectsCheckBox.setText(_translate("ClearPrivateDataDialog", "Recently opened multi projects"))
        self.debugCheckBox.setToolTip(_translate("ClearPrivateDataDialog", "Select to clear the debug histories"))
        self.debugCheckBox.setText(_translate("ClearPrivateDataDialog", "Debug histories"))
        self.shellCheckBox.setToolTip(_translate("ClearPrivateDataDialog", "Select to clear the shell histories"))
        self.shellCheckBox.setText(_translate("ClearPrivateDataDialog", "Shell histories"))
        self.vcsCheckBox.setToolTip(_translate("ClearPrivateDataDialog", "Select to clear the VCS related histories"))
        self.vcsCheckBox.setText(_translate("ClearPrivateDataDialog", "Version Control System histories"))
        self.pluginsCheckBox.setToolTip(_translate("ClearPrivateDataDialog", "Select to clear the private data of plug-ins not covered above"))
        self.pluginsCheckBox.setText(_translate("ClearPrivateDataDialog", "Plug-in private data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClearPrivateDataDialog = QtWidgets.QDialog()
    ui = Ui_ClearPrivateDataDialog()
    ui.setupUi(ClearPrivateDataDialog)
    ClearPrivateDataDialog.show()
    sys.exit(app.exec_())

