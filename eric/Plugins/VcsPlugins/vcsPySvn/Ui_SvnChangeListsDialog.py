# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnChangeListsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnChangeListsDialog(object):
    def setupUi(self, SvnChangeListsDialog):
        SvnChangeListsDialog.setObjectName("SvnChangeListsDialog")
        SvnChangeListsDialog.resize(519, 494)
        SvnChangeListsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(SvnChangeListsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SvnChangeListsDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.changeLists = QtWidgets.QListWidget(SvnChangeListsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.changeLists.sizePolicy().hasHeightForWidth())
        self.changeLists.setSizePolicy(sizePolicy)
        self.changeLists.setAlternatingRowColors(True)
        self.changeLists.setObjectName("changeLists")
        self.verticalLayout.addWidget(self.changeLists)
        self.filesLabel = QtWidgets.QLabel(SvnChangeListsDialog)
        self.filesLabel.setText("")
        self.filesLabel.setWordWrap(True)
        self.filesLabel.setObjectName("filesLabel")
        self.verticalLayout.addWidget(self.filesLabel)
        self.filesList = QtWidgets.QListWidget(SvnChangeListsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.filesList.sizePolicy().hasHeightForWidth())
        self.filesList.setSizePolicy(sizePolicy)
        self.filesList.setAlternatingRowColors(True)
        self.filesList.setObjectName("filesList")
        self.verticalLayout.addWidget(self.filesList)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnChangeListsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnChangeListsDialog)
        self.buttonBox.accepted.connect(SvnChangeListsDialog.accept)
        self.buttonBox.rejected.connect(SvnChangeListsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SvnChangeListsDialog)
        SvnChangeListsDialog.setTabOrder(self.changeLists, self.filesList)
        SvnChangeListsDialog.setTabOrder(self.filesList, self.buttonBox)

    def retranslateUi(self, SvnChangeListsDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnChangeListsDialog.setWindowTitle(_translate("SvnChangeListsDialog", "Subversion Change Lists"))
        self.label.setText(_translate("SvnChangeListsDialog", "Change Lists:"))
        self.changeLists.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Change Lists</b>\n"
"<p>Select a change list here to see the associated files in the list below.</p>"))
        self.filesList.setWhatsThis(_translate("SvnChangeListsDialog", "<b>Files</b>\n"
"<p>This shows a list of files associated with the change list selected above.</p>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnChangeListsDialog = QtWidgets.QDialog()
    ui = Ui_SvnChangeListsDialog()
    ui.setupUi(SvnChangeListsDialog)
    SvnChangeListsDialog.show()
    sys.exit(app.exec_())

