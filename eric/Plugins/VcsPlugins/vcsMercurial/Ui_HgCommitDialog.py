# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgCommitDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgCommitDialog(object):
    def setupUi(self, HgCommitDialog):
        HgCommitDialog.setObjectName("HgCommitDialog")
        HgCommitDialog.resize(450, 500)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(HgCommitDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logGroup = QtWidgets.QGroupBox(HgCommitDialog)
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
        self.amendCheckBox = QtWidgets.QCheckBox(HgCommitDialog)
        self.amendCheckBox.setObjectName("amendCheckBox")
        self.verticalLayout_3.addWidget(self.amendCheckBox)
        self.subrepoCheckBox = QtWidgets.QCheckBox(HgCommitDialog)
        self.subrepoCheckBox.setObjectName("subrepoCheckBox")
        self.verticalLayout_3.addWidget(self.subrepoCheckBox)
        self.groupBox = QtWidgets.QGroupBox(HgCommitDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.authorComboBox = QtWidgets.QComboBox(self.groupBox)
        self.authorComboBox.setEditable(True)
        self.authorComboBox.setObjectName("authorComboBox")
        self.verticalLayout_2.addWidget(self.authorComboBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.dateTimeGroup = QtWidgets.QGroupBox(HgCommitDialog)
        self.dateTimeGroup.setCheckable(True)
        self.dateTimeGroup.setChecked(False)
        self.dateTimeGroup.setObjectName("dateTimeGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dateTimeGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(241, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.dateTimeGroup)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.dateTimeGroup)
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.dateTimeGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgCommitDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(HgCommitDialog)
        QtCore.QMetaObject.connectSlotsByName(HgCommitDialog)
        HgCommitDialog.setTabOrder(self.logEdit, self.recentComboBox)
        HgCommitDialog.setTabOrder(self.recentComboBox, self.amendCheckBox)
        HgCommitDialog.setTabOrder(self.amendCheckBox, self.subrepoCheckBox)
        HgCommitDialog.setTabOrder(self.subrepoCheckBox, self.authorComboBox)
        HgCommitDialog.setTabOrder(self.authorComboBox, self.dateTimeGroup)
        HgCommitDialog.setTabOrder(self.dateTimeGroup, self.dateTimeEdit)

    def retranslateUi(self, HgCommitDialog):
        _translate = QtCore.QCoreApplication.translate
        HgCommitDialog.setWindowTitle(_translate("HgCommitDialog", "Mercurial"))
        self.logGroup.setTitle(_translate("HgCommitDialog", "Commit Message"))
        self.logEdit.setToolTip(_translate("HgCommitDialog", "Enter the log message."))
        self.logEdit.setWhatsThis(_translate("HgCommitDialog", "<b>Log Message</b>\n"
"<p>Enter the log message for the commit action.</p>"))
        self.label.setText(_translate("HgCommitDialog", "Recent commit messages"))
        self.recentComboBox.setToolTip(_translate("HgCommitDialog", "Select a recent commit message to use"))
        self.amendCheckBox.setToolTip(_translate("HgCommitDialog", "Select to amend the last commit (leave message empty to keep it)"))
        self.amendCheckBox.setText(_translate("HgCommitDialog", "Amend the last commit"))
        self.subrepoCheckBox.setToolTip(_translate("HgCommitDialog", "Select to commit sub-repositories as well"))
        self.subrepoCheckBox.setText(_translate("HgCommitDialog", "Commit sub-repositories"))
        self.groupBox.setTitle(_translate("HgCommitDialog", "Author"))
        self.label_3.setText(_translate("HgCommitDialog", "Enter author name to override the configured user:"))
        self.authorComboBox.setToolTip(_translate("HgCommitDialog", "Enter an author name in order to override the configured one"))
        self.dateTimeGroup.setToolTip(_translate("HgCommitDialog", "Select to give date and time information"))
        self.dateTimeGroup.setTitle(_translate("HgCommitDialog", "Date and Time"))
        self.label_4.setText(_translate("HgCommitDialog", "Date/Time:"))
        self.dateTimeEdit.setToolTip(_translate("HgCommitDialog", "Enter the date and time to be used"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgCommitDialog = QtWidgets.QWidget()
    ui = Ui_HgCommitDialog()
    ui.setupUi(HgCommitDialog)
    HgCommitDialog.show()
    sys.exit(app.exec_())

