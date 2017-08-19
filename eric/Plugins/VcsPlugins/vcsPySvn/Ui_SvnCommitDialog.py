# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnCommitDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnCommitDialog(object):
    def setupUi(self, SvnCommitDialog):
        SvnCommitDialog.setObjectName("SvnCommitDialog")
        SvnCommitDialog.resize(450, 396)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SvnCommitDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logGroup = QtWidgets.QGroupBox(SvnCommitDialog)
        self.logGroup.setObjectName("logGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.logGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logEdit = QtWidgets.QTextEdit(self.logGroup)
        self.logEdit.setTabChangesFocus(True)
        self.logEdit.setAcceptRichText(False)
        self.logEdit.setObjectName("logEdit")
        self.verticalLayout.addWidget(self.logEdit)
        self.label = QtWidgets.QLabel(self.logGroup)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.recentComboBox = QtWidgets.QComboBox(self.logGroup)
        self.recentComboBox.setObjectName("recentComboBox")
        self.verticalLayout.addWidget(self.recentComboBox)
        self.verticalLayout_3.addWidget(self.logGroup)
        self.changeListsGroup = QtWidgets.QGroupBox(SvnCommitDialog)
        self.changeListsGroup.setObjectName("changeListsGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.changeListsGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.changeLists = QtWidgets.QListWidget(self.changeListsGroup)
        self.changeLists.setObjectName("changeLists")
        self.verticalLayout_2.addWidget(self.changeLists)
        self.keepChangeListsCheckBox = QtWidgets.QCheckBox(self.changeListsGroup)
        self.keepChangeListsCheckBox.setObjectName("keepChangeListsCheckBox")
        self.verticalLayout_2.addWidget(self.keepChangeListsCheckBox)
        self.verticalLayout_3.addWidget(self.changeListsGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnCommitDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(SvnCommitDialog)
        QtCore.QMetaObject.connectSlotsByName(SvnCommitDialog)
        SvnCommitDialog.setTabOrder(self.logEdit, self.recentComboBox)
        SvnCommitDialog.setTabOrder(self.recentComboBox, self.changeLists)
        SvnCommitDialog.setTabOrder(self.changeLists, self.keepChangeListsCheckBox)
        SvnCommitDialog.setTabOrder(self.keepChangeListsCheckBox, self.buttonBox)

    def retranslateUi(self, SvnCommitDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnCommitDialog.setWindowTitle(_translate("SvnCommitDialog", "Subversion"))
        self.logGroup.setTitle(_translate("SvnCommitDialog", "Commit Message"))
        self.logEdit.setToolTip(_translate("SvnCommitDialog", "Enter the log message."))
        self.logEdit.setWhatsThis(_translate("SvnCommitDialog", "<b>Log Message</b>\n"
"<p>Enter the log message for the commit action.</p>"))
        self.label.setText(_translate("SvnCommitDialog", "Recent commit messages"))
        self.recentComboBox.setToolTip(_translate("SvnCommitDialog", "Select a recent commit message to use"))
        self.changeListsGroup.setTitle(_translate("SvnCommitDialog", "Changelists"))
        self.changeLists.setToolTip(_translate("SvnCommitDialog", "Select the change lists to limit the commit"))
        self.keepChangeListsCheckBox.setToolTip(_translate("SvnCommitDialog", "Select to keep the changelists"))
        self.keepChangeListsCheckBox.setText(_translate("SvnCommitDialog", "Keep changelists"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnCommitDialog = QtWidgets.QWidget()
    ui = Ui_SvnCommitDialog()
    ui.setupUi(SvnCommitDialog)
    SvnCommitDialog.show()
    sys.exit(app.exec_())

