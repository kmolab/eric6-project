# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsPySvn\SvnRepoBrowserDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnRepoBrowserDialog(object):
    def setupUi(self, SvnRepoBrowserDialog):
        SvnRepoBrowserDialog.setObjectName("SvnRepoBrowserDialog")
        SvnRepoBrowserDialog.resize(650, 500)
        self.gridlayout = QtWidgets.QGridLayout(SvnRepoBrowserDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(SvnRepoBrowserDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.urlCombo = QtWidgets.QComboBox(SvnRepoBrowserDialog)
        self.urlCombo.setEditable(True)
        self.urlCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.urlCombo.setObjectName("urlCombo")
        self.gridlayout.addWidget(self.urlCombo, 0, 1, 1, 1)
        self.repoTree = QtWidgets.QTreeWidget(SvnRepoBrowserDialog)
        self.repoTree.setAlternatingRowColors(True)
        self.repoTree.setAllColumnsShowFocus(True)
        self.repoTree.setColumnCount(5)
        self.repoTree.setObjectName("repoTree")
        self.gridlayout.addWidget(self.repoTree, 1, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnRepoBrowserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(SvnRepoBrowserDialog)
        self.buttonBox.rejected.connect(SvnRepoBrowserDialog.reject)
        self.buttonBox.accepted.connect(SvnRepoBrowserDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(SvnRepoBrowserDialog)
        SvnRepoBrowserDialog.setTabOrder(self.urlCombo, self.repoTree)
        SvnRepoBrowserDialog.setTabOrder(self.repoTree, self.buttonBox)

    def retranslateUi(self, SvnRepoBrowserDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnRepoBrowserDialog.setWindowTitle(_translate("SvnRepoBrowserDialog", "Subversion Repository Browser"))
        self.label.setText(_translate("SvnRepoBrowserDialog", "URL:"))
        self.urlCombo.setToolTip(_translate("SvnRepoBrowserDialog", "Enter the URL of the repository"))
        self.repoTree.setSortingEnabled(True)
        self.repoTree.headerItem().setText(0, _translate("SvnRepoBrowserDialog", "File"))
        self.repoTree.headerItem().setText(1, _translate("SvnRepoBrowserDialog", "Revision"))
        self.repoTree.headerItem().setText(2, _translate("SvnRepoBrowserDialog", "Author"))
        self.repoTree.headerItem().setText(3, _translate("SvnRepoBrowserDialog", "Size"))
        self.repoTree.headerItem().setText(4, _translate("SvnRepoBrowserDialog", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnRepoBrowserDialog = QtWidgets.QDialog()
    ui = Ui_SvnRepoBrowserDialog()
    ui.setupUi(SvnRepoBrowserDialog)
    SvnRepoBrowserDialog.show()
    sys.exit(app.exec_())

