# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnOptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnOptionsDialog(object):
    def setupUi(self, SvnOptionsDialog):
        SvnOptionsDialog.setObjectName("SvnOptionsDialog")
        SvnOptionsDialog.resize(565, 149)
        SvnOptionsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(SvnOptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(SvnOptionsDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.protocolCombo = QtWidgets.QComboBox(SvnOptionsDialog)
        self.protocolCombo.setObjectName("protocolCombo")
        self.gridLayout.addWidget(self.protocolCombo, 0, 1, 1, 1)
        self.vcsUrlLabel = QtWidgets.QLabel(SvnOptionsDialog)
        self.vcsUrlLabel.setObjectName("vcsUrlLabel")
        self.gridLayout.addWidget(self.vcsUrlLabel, 1, 0, 1, 1)
        self.vcsUrlPicker = E5PathPicker(SvnOptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcsUrlPicker.sizePolicy().hasHeightForWidth())
        self.vcsUrlPicker.setSizePolicy(sizePolicy)
        self.vcsUrlPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.vcsUrlPicker.setObjectName("vcsUrlPicker")
        self.gridLayout.addWidget(self.vcsUrlPicker, 1, 1, 1, 1)
        self.TextLabel5 = QtWidgets.QLabel(SvnOptionsDialog)
        self.TextLabel5.setObjectName("TextLabel5")
        self.gridLayout.addWidget(self.TextLabel5, 2, 0, 1, 1)
        self.vcsLogEdit = QtWidgets.QLineEdit(SvnOptionsDialog)
        self.vcsLogEdit.setObjectName("vcsLogEdit")
        self.gridLayout.addWidget(self.vcsLogEdit, 2, 1, 1, 1)
        self.layoutCheckBox = QtWidgets.QCheckBox(SvnOptionsDialog)
        self.layoutCheckBox.setChecked(True)
        self.layoutCheckBox.setObjectName("layoutCheckBox")
        self.gridLayout.addWidget(self.layoutCheckBox, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 2)
        self.textLabel1.setBuddy(self.protocolCombo)
        self.vcsUrlLabel.setBuddy(self.vcsUrlPicker)
        self.TextLabel5.setBuddy(self.vcsLogEdit)

        self.retranslateUi(SvnOptionsDialog)
        self.buttonBox.accepted.connect(SvnOptionsDialog.accept)
        self.buttonBox.rejected.connect(SvnOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnOptionsDialog)
        SvnOptionsDialog.setTabOrder(self.protocolCombo, self.vcsUrlPicker)
        SvnOptionsDialog.setTabOrder(self.vcsUrlPicker, self.vcsLogEdit)
        SvnOptionsDialog.setTabOrder(self.vcsLogEdit, self.layoutCheckBox)

    def retranslateUi(self, SvnOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnOptionsDialog.setWindowTitle(_translate("SvnOptionsDialog", "Repository Infos"))
        SvnOptionsDialog.setWhatsThis(_translate("SvnOptionsDialog", "<b>Repository Infos Dialog</b>\n"
"<p>Enter the various infos into the entry fields. These values are used to generate a new project in the repository. If the checkbox is selected, the URL must end in the project name. A directory tree with project/tags, project/branches and project/trunk will be generated in the repository. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>"))
        self.textLabel1.setText(_translate("SvnOptionsDialog", "&Protocol:"))
        self.protocolCombo.setToolTip(_translate("SvnOptionsDialog", "Select the protocol to access the repository"))
        self.vcsUrlLabel.setText(_translate("SvnOptionsDialog", "&URL:"))
        self.vcsUrlPicker.setToolTip(_translate("SvnOptionsDialog", "Enter the url path of the module in the repository (without protocol part)"))
        self.vcsUrlPicker.setWhatsThis(_translate("SvnOptionsDialog", "<b>URL</b><p>Enter the URL to the module. For a repository with standard layout, this must not contain the trunk, tags or branches part.</p>"))
        self.TextLabel5.setText(_translate("SvnOptionsDialog", "Log &Message:"))
        self.vcsLogEdit.setToolTip(_translate("SvnOptionsDialog", "Enter the log message for the new project."))
        self.vcsLogEdit.setWhatsThis(_translate("SvnOptionsDialog", "<b>Log Message</b>\n"
"<p>Enter the log message to be used for the new project.</p>"))
        self.vcsLogEdit.setText(_translate("SvnOptionsDialog", "new project started"))
        self.layoutCheckBox.setToolTip(_translate("SvnOptionsDialog", "Select, if the standard repository layout (projectdir/trunk, projectdir/tags, projectdir/branches) should be generated"))
        self.layoutCheckBox.setText(_translate("SvnOptionsDialog", "Create standard repository &layout"))
        self.layoutCheckBox.setShortcut(_translate("SvnOptionsDialog", "Alt+L"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnOptionsDialog = QtWidgets.QDialog()
    ui = Ui_SvnOptionsDialog()
    ui.setupUi(SvnOptionsDialog)
    SvnOptionsDialog.show()
    sys.exit(app.exec_())

