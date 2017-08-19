# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\CheckerPlugins\CodeStyleChecker\CodeStyleStatisticsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CodeStyleStatisticsDialog(object):
    def setupUi(self, CodeStyleStatisticsDialog):
        CodeStyleStatisticsDialog.setObjectName("CodeStyleStatisticsDialog")
        CodeStyleStatisticsDialog.resize(531, 372)
        self.verticalLayout = QtWidgets.QVBoxLayout(CodeStyleStatisticsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statisticsList = QtWidgets.QTreeWidget(CodeStyleStatisticsDialog)
        self.statisticsList.setAlternatingRowColors(True)
        self.statisticsList.setRootIsDecorated(False)
        self.statisticsList.setWordWrap(True)
        self.statisticsList.setObjectName("statisticsList")
        self.verticalLayout.addWidget(self.statisticsList)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.filesChecked = QtWidgets.QLabel(CodeStyleStatisticsDialog)
        self.filesChecked.setObjectName("filesChecked")
        self.gridLayout.addWidget(self.filesChecked, 0, 0, 1, 1)
        self.filesIssues = QtWidgets.QLabel(CodeStyleStatisticsDialog)
        self.filesIssues.setObjectName("filesIssues")
        self.gridLayout.addWidget(self.filesIssues, 0, 1, 1, 1)
        self.totalIssues = QtWidgets.QLabel(CodeStyleStatisticsDialog)
        self.totalIssues.setObjectName("totalIssues")
        self.gridLayout.addWidget(self.totalIssues, 1, 0, 1, 1)
        self.ignoredIssues = QtWidgets.QLabel(CodeStyleStatisticsDialog)
        self.ignoredIssues.setObjectName("ignoredIssues")
        self.gridLayout.addWidget(self.ignoredIssues, 1, 1, 1, 1)
        self.fixedIssues = QtWidgets.QLabel(CodeStyleStatisticsDialog)
        self.fixedIssues.setObjectName("fixedIssues")
        self.gridLayout.addWidget(self.fixedIssues, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(CodeStyleStatisticsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CodeStyleStatisticsDialog)
        self.buttonBox.accepted.connect(CodeStyleStatisticsDialog.accept)
        self.buttonBox.rejected.connect(CodeStyleStatisticsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CodeStyleStatisticsDialog)
        CodeStyleStatisticsDialog.setTabOrder(self.statisticsList, self.buttonBox)

    def retranslateUi(self, CodeStyleStatisticsDialog):
        _translate = QtCore.QCoreApplication.translate
        CodeStyleStatisticsDialog.setWindowTitle(_translate("CodeStyleStatisticsDialog", "Code Style Checker Statistics"))
        self.statisticsList.headerItem().setText(0, _translate("CodeStyleStatisticsDialog", "Count"))
        self.statisticsList.headerItem().setText(1, _translate("CodeStyleStatisticsDialog", "Code"))
        self.statisticsList.headerItem().setText(2, _translate("CodeStyleStatisticsDialog", "Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CodeStyleStatisticsDialog = QtWidgets.QDialog()
    ui = Ui_CodeStyleStatisticsDialog()
    ui.setupUi(CodeStyleStatisticsDialog)
    CodeStyleStatisticsDialog.show()
    sys.exit(app.exec_())

