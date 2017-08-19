# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HisteditExtension\HgHisteditCommitEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgHisteditCommitEditor(object):
    def setupUi(self, HgHisteditCommitEditor):
        HgHisteditCommitEditor.setObjectName("HgHisteditCommitEditor")
        HgHisteditCommitEditor.resize(500, 600)
        HgHisteditCommitEditor.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(HgHisteditCommitEditor)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(HgHisteditCommitEditor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messageEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.messageEdit.setTabChangesFocus(True)
        self.messageEdit.setObjectName("messageEdit")
        self.verticalLayout_3.addWidget(self.messageEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.recentComboBox = QtWidgets.QComboBox(self.groupBox)
        self.recentComboBox.setObjectName("recentComboBox")
        self.verticalLayout_3.addWidget(self.recentComboBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.infoEdit.setReadOnly(True)
        self.infoEdit.setObjectName("infoEdit")
        self.verticalLayout.addWidget(self.infoEdit)
        self.verticalLayout_2.addWidget(self.splitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgHisteditCommitEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(HgHisteditCommitEditor)
        QtCore.QMetaObject.connectSlotsByName(HgHisteditCommitEditor)

    def retranslateUi(self, HgHisteditCommitEditor):
        _translate = QtCore.QCoreApplication.translate
        HgHisteditCommitEditor.setWindowTitle(_translate("HgHisteditCommitEditor", "Commit Message"))
        self.groupBox.setTitle(_translate("HgHisteditCommitEditor", "Commit Message"))
        self.messageEdit.setToolTip(_translate("HgHisteditCommitEditor", "Edit the commit message"))
        self.label_2.setText(_translate("HgHisteditCommitEditor", "Recent commit messages"))
        self.recentComboBox.setToolTip(_translate("HgHisteditCommitEditor", "Select a recent commit message to use"))
        self.groupBox_2.setTitle(_translate("HgHisteditCommitEditor", "Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgHisteditCommitEditor = QtWidgets.QDialog()
    ui = Ui_HgHisteditCommitEditor()
    ui.setupUi(HgHisteditCommitEditor)
    HgHisteditCommitEditor.show()
    sys.exit(app.exec_())

