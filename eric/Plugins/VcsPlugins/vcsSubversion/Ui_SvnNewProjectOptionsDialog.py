# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnNewProjectOptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnNewProjectOptionsDialog(object):
    def setupUi(self, SvnNewProjectOptionsDialog):
        SvnNewProjectOptionsDialog.setObjectName("SvnNewProjectOptionsDialog")
        SvnNewProjectOptionsDialog.resize(562, 170)
        SvnNewProjectOptionsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(SvnNewProjectOptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.protocolCombo = QtWidgets.QComboBox(SvnNewProjectOptionsDialog)
        self.protocolCombo.setObjectName("protocolCombo")
        self.gridLayout.addWidget(self.protocolCombo, 0, 1, 1, 1)
        self.vcsUrlLabel = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.vcsUrlLabel.setObjectName("vcsUrlLabel")
        self.gridLayout.addWidget(self.vcsUrlLabel, 1, 0, 1, 1)
        self.vcsUrlPicker = E5PathPicker(SvnNewProjectOptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcsUrlPicker.sizePolicy().hasHeightForWidth())
        self.vcsUrlPicker.setSizePolicy(sizePolicy)
        self.vcsUrlPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.vcsUrlPicker.setObjectName("vcsUrlPicker")
        self.gridLayout.addWidget(self.vcsUrlPicker, 1, 1, 1, 1)
        self.vcsTagLabel = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.vcsTagLabel.setObjectName("vcsTagLabel")
        self.gridLayout.addWidget(self.vcsTagLabel, 2, 0, 1, 1)
        self.vcsTagEdit = QtWidgets.QLineEdit(SvnNewProjectOptionsDialog)
        self.vcsTagEdit.setObjectName("vcsTagEdit")
        self.gridLayout.addWidget(self.vcsTagEdit, 2, 1, 1, 1)
        self.TextLabel4 = QtWidgets.QLabel(SvnNewProjectOptionsDialog)
        self.TextLabel4.setObjectName("TextLabel4")
        self.gridLayout.addWidget(self.TextLabel4, 3, 0, 1, 1)
        self.vcsProjectDirPicker = E5PathPicker(SvnNewProjectOptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcsProjectDirPicker.sizePolicy().hasHeightForWidth())
        self.vcsProjectDirPicker.setSizePolicy(sizePolicy)
        self.vcsProjectDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.vcsProjectDirPicker.setObjectName("vcsProjectDirPicker")
        self.gridLayout.addWidget(self.vcsProjectDirPicker, 3, 1, 1, 1)
        self.layoutCheckBox = QtWidgets.QCheckBox(SvnNewProjectOptionsDialog)
        self.layoutCheckBox.setChecked(True)
        self.layoutCheckBox.setObjectName("layoutCheckBox")
        self.gridLayout.addWidget(self.layoutCheckBox, 4, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnNewProjectOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.textLabel1.setBuddy(self.protocolCombo)
        self.vcsUrlLabel.setBuddy(self.vcsUrlPicker)
        self.vcsTagLabel.setBuddy(self.vcsTagEdit)
        self.TextLabel4.setBuddy(self.vcsProjectDirPicker)

        self.retranslateUi(SvnNewProjectOptionsDialog)
        self.buttonBox.accepted.connect(SvnNewProjectOptionsDialog.accept)
        self.buttonBox.rejected.connect(SvnNewProjectOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnNewProjectOptionsDialog)
        SvnNewProjectOptionsDialog.setTabOrder(self.protocolCombo, self.vcsUrlPicker)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsUrlPicker, self.vcsTagEdit)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsTagEdit, self.vcsProjectDirPicker)
        SvnNewProjectOptionsDialog.setTabOrder(self.vcsProjectDirPicker, self.layoutCheckBox)

    def retranslateUi(self, SvnNewProjectOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnNewProjectOptionsDialog.setWindowTitle(_translate("SvnNewProjectOptionsDialog", "New Project from Repository"))
        SvnNewProjectOptionsDialog.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>New Project from Repository Dialog</b>\n"
"<p>Enter the various repository infos into the entry fields. These values are used, when the new project is retrieved from the repository. If the checkbox is selected, the URL must end in the project name. A repository layout with project/tags, project/branches and project/trunk will be assumed. In this case, you may enter a tag or branch, which must look like tags/tagname or branches/branchname. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>"))
        self.textLabel1.setText(_translate("SvnNewProjectOptionsDialog", "&Protocol:"))
        self.protocolCombo.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select the protocol to access the repository"))
        self.vcsUrlLabel.setText(_translate("SvnNewProjectOptionsDialog", "&URL:"))
        self.vcsUrlPicker.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the url path of the module in the repository (without protocol part)"))
        self.vcsUrlPicker.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>URL</b><p>Enter the URL to the module. For a repository with standard layout, this must not contain the trunk, tags or branches part.</p>"))
        self.vcsTagLabel.setText(_translate("SvnNewProjectOptionsDialog", "&Tag:"))
        self.vcsTagEdit.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the tag the new project should be generated from"))
        self.vcsTagEdit.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>Tag in VCS</b>\n"
"<p>Enter the tag name the new project shall be generated from. Leave empty to retrieve the latest data from the repository.</p>"))
        self.TextLabel4.setText(_translate("SvnNewProjectOptionsDialog", "Project &Directory:"))
        self.vcsProjectDirPicker.setToolTip(_translate("SvnNewProjectOptionsDialog", "Enter the directory of the new project."))
        self.vcsProjectDirPicker.setWhatsThis(_translate("SvnNewProjectOptionsDialog", "<b>Project Directory</b>\n"
"<p>Enter the directory of the new project. It will be retrieved from \n"
"the repository and be placed in this directory.</p>"))
        self.layoutCheckBox.setToolTip(_translate("SvnNewProjectOptionsDialog", "Select to indicate, that the repository has a standard layout (projectdir/trunk, projectdir/tags, projectdir/branches)"))
        self.layoutCheckBox.setText(_translate("SvnNewProjectOptionsDialog", "Repository has standard &layout"))
        self.layoutCheckBox.setShortcut(_translate("SvnNewProjectOptionsDialog", "Alt+L"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnNewProjectOptionsDialog = QtWidgets.QDialog()
    ui = Ui_SvnNewProjectOptionsDialog()
    ui.setupUi(SvnNewProjectOptionsDialog)
    SvnNewProjectOptionsDialog.show()
    sys.exit(app.exec_())

