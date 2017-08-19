# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgNewProjectOptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgNewProjectOptionsDialog(object):
    def setupUi(self, HgNewProjectOptionsDialog):
        HgNewProjectOptionsDialog.setObjectName("HgNewProjectOptionsDialog")
        HgNewProjectOptionsDialog.resize(562, 187)
        HgNewProjectOptionsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(HgNewProjectOptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lfNoteLabel = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.lfNoteLabel.setWordWrap(True)
        self.lfNoteLabel.setObjectName("lfNoteLabel")
        self.gridLayout.addWidget(self.lfNoteLabel, 4, 0, 1, 3)
        self.vcsUrlPicker = E5ComboPathPicker(HgNewProjectOptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcsUrlPicker.sizePolicy().hasHeightForWidth())
        self.vcsUrlPicker.setSizePolicy(sizePolicy)
        self.vcsUrlPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.vcsUrlPicker.setObjectName("vcsUrlPicker")
        self.gridLayout.addWidget(self.vcsUrlPicker, 0, 1, 1, 1)
        self.vcsRevisionLabel = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.vcsRevisionLabel.setObjectName("vcsRevisionLabel")
        self.gridLayout.addWidget(self.vcsRevisionLabel, 1, 0, 1, 1)
        self.vcsRevisionEdit = QtWidgets.QLineEdit(HgNewProjectOptionsDialog)
        self.vcsRevisionEdit.setWhatsThis("")
        self.vcsRevisionEdit.setObjectName("vcsRevisionEdit")
        self.gridLayout.addWidget(self.vcsRevisionEdit, 1, 1, 1, 2)
        self.vcsProjectDirPicker = E5PathPicker(HgNewProjectOptionsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcsProjectDirPicker.sizePolicy().hasHeightForWidth())
        self.vcsProjectDirPicker.setSizePolicy(sizePolicy)
        self.vcsProjectDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.vcsProjectDirPicker.setObjectName("vcsProjectDirPicker")
        self.gridLayout.addWidget(self.vcsProjectDirPicker, 2, 1, 1, 2)
        self.largeCheckBox = QtWidgets.QCheckBox(HgNewProjectOptionsDialog)
        self.largeCheckBox.setObjectName("largeCheckBox")
        self.gridLayout.addWidget(self.largeCheckBox, 3, 0, 1, 3)
        self.TextLabel4 = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.TextLabel4.setObjectName("TextLabel4")
        self.gridLayout.addWidget(self.TextLabel4, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgNewProjectOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 3)
        self.TextLabel2 = QtWidgets.QLabel(HgNewProjectOptionsDialog)
        self.TextLabel2.setObjectName("TextLabel2")
        self.gridLayout.addWidget(self.TextLabel2, 0, 0, 1, 1)
        self.vcsUrlClearHistoryButton = QtWidgets.QToolButton(HgNewProjectOptionsDialog)
        self.vcsUrlClearHistoryButton.setObjectName("vcsUrlClearHistoryButton")
        self.gridLayout.addWidget(self.vcsUrlClearHistoryButton, 0, 2, 1, 1)
        self.vcsRevisionLabel.setBuddy(self.vcsRevisionEdit)
        self.TextLabel4.setBuddy(self.vcsProjectDirPicker)
        self.TextLabel2.setBuddy(self.vcsUrlPicker)

        self.retranslateUi(HgNewProjectOptionsDialog)
        self.buttonBox.accepted.connect(HgNewProjectOptionsDialog.accept)
        self.buttonBox.rejected.connect(HgNewProjectOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgNewProjectOptionsDialog)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsUrlPicker, self.vcsUrlClearHistoryButton)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsUrlClearHistoryButton, self.vcsRevisionEdit)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsRevisionEdit, self.vcsProjectDirPicker)
        HgNewProjectOptionsDialog.setTabOrder(self.vcsProjectDirPicker, self.largeCheckBox)

    def retranslateUi(self, HgNewProjectOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        HgNewProjectOptionsDialog.setWindowTitle(_translate("HgNewProjectOptionsDialog", "New Project from Repository"))
        HgNewProjectOptionsDialog.setWhatsThis(_translate("HgNewProjectOptionsDialog", "<b>New Project from Repository Dialog</b>\n"
"<p>Enter the various repository infos into the entry fields. These values are used, when the new project is retrieved from the repository. If the checkbox is selected, the URL must end in the project name. A repository layout with project/tags, project/branches and project/trunk will be assumed. In this case, you may enter a tag or branch, which must look like tags/tagname or branches/branchname. If the checkbox is not selected, the URL must contain the complete path in the repository.</p>\n"
"<p>For remote repositories the URL must contain the hostname.</p>"))
        self.lfNoteLabel.setText(_translate("HgNewProjectOptionsDialog", "<b>Note:</b> This option increases the download time and volume."))
        self.vcsUrlPicker.setToolTip(_translate("HgNewProjectOptionsDialog", "Enter the URL of the repository"))
        self.vcsRevisionLabel.setText(_translate("HgNewProjectOptionsDialog", "&Revision:"))
        self.vcsRevisionEdit.setToolTip(_translate("HgNewProjectOptionsDialog", "Enter the revision the new project should be generated from"))
        self.vcsProjectDirPicker.setToolTip(_translate("HgNewProjectOptionsDialog", "Enter the directory of the new project."))
        self.vcsProjectDirPicker.setWhatsThis(_translate("HgNewProjectOptionsDialog", "<b>Project Directory</b>\n"
"<p>Enter the directory of the new project. It will be retrieved from \n"
"the repository and be placed in this directory.</p>"))
        self.largeCheckBox.setText(_translate("HgNewProjectOptionsDialog", "Download all versions of all large files"))
        self.TextLabel4.setText(_translate("HgNewProjectOptionsDialog", "Project &Directory:"))
        self.TextLabel2.setText(_translate("HgNewProjectOptionsDialog", "&URL:"))
        self.vcsUrlClearHistoryButton.setToolTip(_translate("HgNewProjectOptionsDialog", "Press to clear the history of entered repository URLs"))

from E5Gui.E5PathPicker import E5ComboPathPicker, E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgNewProjectOptionsDialog = QtWidgets.QDialog()
    ui = Ui_HgNewProjectOptionsDialog()
    ui.setupUi(HgNewProjectOptionsDialog)
    HgNewProjectOptionsDialog.show()
    sys.exit(app.exec_())

