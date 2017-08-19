# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\DataViews\PyCoverageDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyCoverageDialog(object):
    def setupUi(self, PyCoverageDialog):
        PyCoverageDialog.setObjectName("PyCoverageDialog")
        PyCoverageDialog.resize(832, 585)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(PyCoverageDialog.sizePolicy().hasHeightForWidth())
        PyCoverageDialog.setSizePolicy(sizePolicy)
        PyCoverageDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PyCoverageDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel1_2 = QtWidgets.QLabel(PyCoverageDialog)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self.hboxlayout.addWidget(self.textLabel1_2)
        self.excludeCombo = QtWidgets.QComboBox(PyCoverageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excludeCombo.sizePolicy().hasHeightForWidth())
        self.excludeCombo.setSizePolicy(sizePolicy)
        self.excludeCombo.setEditable(True)
        self.excludeCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.excludeCombo.setDuplicatesEnabled(False)
        self.excludeCombo.setObjectName("excludeCombo")
        self.hboxlayout.addWidget(self.excludeCombo)
        self.reloadButton = QtWidgets.QPushButton(PyCoverageDialog)
        self.reloadButton.setObjectName("reloadButton")
        self.hboxlayout.addWidget(self.reloadButton)
        self.verticalLayout_2.addLayout(self.hboxlayout)
        self.resultList = QtWidgets.QTreeWidget(PyCoverageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.resultList.sizePolicy().hasHeightForWidth())
        self.resultList.setSizePolicy(sizePolicy)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setRootIsDecorated(False)
        self.resultList.setItemsExpandable(False)
        self.resultList.setObjectName("resultList")
        self.verticalLayout_2.addWidget(self.resultList)
        self.summaryGroup = QtWidgets.QGroupBox(PyCoverageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.summaryGroup.sizePolicy().hasHeightForWidth())
        self.summaryGroup.setSizePolicy(sizePolicy)
        self.summaryGroup.setObjectName("summaryGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.summaryGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summaryList = QtWidgets.QTreeWidget(self.summaryGroup)
        self.summaryList.setAlternatingRowColors(True)
        self.summaryList.setRootIsDecorated(False)
        self.summaryList.setItemsExpandable(False)
        self.summaryList.setObjectName("summaryList")
        self.verticalLayout.addWidget(self.summaryList)
        self.verticalLayout_2.addWidget(self.summaryGroup)
        self.checkProgress = QtWidgets.QProgressBar(PyCoverageDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName("checkProgress")
        self.verticalLayout_2.addWidget(self.checkProgress)
        self.buttonBox = QtWidgets.QDialogButtonBox(PyCoverageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.textLabel1_2.setBuddy(self.excludeCombo)

        self.retranslateUi(PyCoverageDialog)
        QtCore.QMetaObject.connectSlotsByName(PyCoverageDialog)
        PyCoverageDialog.setTabOrder(self.excludeCombo, self.reloadButton)
        PyCoverageDialog.setTabOrder(self.reloadButton, self.resultList)
        PyCoverageDialog.setTabOrder(self.resultList, self.summaryList)

    def retranslateUi(self, PyCoverageDialog):
        _translate = QtCore.QCoreApplication.translate
        PyCoverageDialog.setWindowTitle(_translate("PyCoverageDialog", "Python Code Coverage"))
        PyCoverageDialog.setWhatsThis(_translate("PyCoverageDialog", "<b>Python Code Coverage</b>\n"
"<p>This dialog shows the collected code coverage data.</p>"))
        self.textLabel1_2.setText(_translate("PyCoverageDialog", "E&xclude pattern:"))
        self.excludeCombo.setToolTip(_translate("PyCoverageDialog", "Enter a regexp pattern marking lines to exclude from coverage"))
        self.excludeCombo.setWhatsThis(_translate("PyCoverageDialog", "<b>Exclude pattern</b>\n"
"<p>Enter a regular expression pattern. Lines matching this pattern are excluded from the coverage analysis. The default pattern is \'#pragma[: ]+[nN][oO] [cC][oO][vV][eE][rR]\'. If the pattern is found on a line containing the colon that introduces a suite of statements, the entire suite is excluded.</p>"))
        self.reloadButton.setText(_translate("PyCoverageDialog", "&Reload"))
        self.reloadButton.setShortcut(_translate("PyCoverageDialog", "Alt+R"))
        self.resultList.setWhatsThis(_translate("PyCoverageDialog", "<b>Python Code Coverage</b>\n"
"<p>This list shows the collected code coverage data. There are several actions available via the context menu.</p>"))
        self.resultList.headerItem().setText(0, _translate("PyCoverageDialog", "Name"))
        self.resultList.headerItem().setText(1, _translate("PyCoverageDialog", "Statements"))
        self.resultList.headerItem().setText(2, _translate("PyCoverageDialog", "Executed"))
        self.resultList.headerItem().setText(3, _translate("PyCoverageDialog", "Coverage"))
        self.resultList.headerItem().setText(4, _translate("PyCoverageDialog", "Excluded"))
        self.resultList.headerItem().setText(5, _translate("PyCoverageDialog", "Missing"))
        self.summaryGroup.setTitle(_translate("PyCoverageDialog", "Summary"))
        self.summaryList.setWhatsThis(_translate("PyCoverageDialog", "<b>Summary</b>\n"
"<p>This shows some overall code coverage information.</p>"))
        self.summaryList.headerItem().setText(0, _translate("PyCoverageDialog", "Statements"))
        self.summaryList.headerItem().setText(1, _translate("PyCoverageDialog", "Executed"))
        self.summaryList.headerItem().setText(2, _translate("PyCoverageDialog", "Coverage"))
        self.checkProgress.setToolTip(_translate("PyCoverageDialog", "Shows the progress of the code coverage action"))
        self.checkProgress.setFormat(_translate("PyCoverageDialog", "%v/%m Files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyCoverageDialog = QtWidgets.QDialog()
    ui = Ui_PyCoverageDialog()
    ui.setupUi(PyCoverageDialog)
    PyCoverageDialog.show()
    sys.exit(app.exec_())

