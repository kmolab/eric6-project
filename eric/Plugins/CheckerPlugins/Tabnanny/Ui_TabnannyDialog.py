# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\CheckerPlugins\Tabnanny\TabnannyDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabnannyDialog(object):
    def setupUi(self, TabnannyDialog):
        TabnannyDialog.setObjectName("TabnannyDialog")
        TabnannyDialog.resize(650, 400)
        TabnannyDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(TabnannyDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterFrame = QtWidgets.QFrame(TabnannyDialog)
        self.filterFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.filterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filterFrame.setObjectName("filterFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.filterFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.filterFrame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.excludeFilesEdit = E5ClearableLineEdit(self.filterFrame)
        self.excludeFilesEdit.setObjectName("excludeFilesEdit")
        self.horizontalLayout.addWidget(self.excludeFilesEdit)
        self.line = QtWidgets.QFrame(self.filterFrame)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.startButton = QtWidgets.QPushButton(self.filterFrame)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.verticalLayout.addWidget(self.filterFrame)
        self.resultList = QtWidgets.QTreeWidget(TabnannyDialog)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setRootIsDecorated(False)
        self.resultList.setItemsExpandable(False)
        self.resultList.setObjectName("resultList")
        self.verticalLayout.addWidget(self.resultList)
        self.checkProgressLabel = E5SqueezeLabelPath(TabnannyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkProgressLabel.sizePolicy().hasHeightForWidth())
        self.checkProgressLabel.setSizePolicy(sizePolicy)
        self.checkProgressLabel.setText("")
        self.checkProgressLabel.setObjectName("checkProgressLabel")
        self.verticalLayout.addWidget(self.checkProgressLabel)
        self.checkProgress = QtWidgets.QProgressBar(TabnannyDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName("checkProgress")
        self.verticalLayout.addWidget(self.checkProgress)
        self.buttonBox = QtWidgets.QDialogButtonBox(TabnannyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TabnannyDialog)
        QtCore.QMetaObject.connectSlotsByName(TabnannyDialog)
        TabnannyDialog.setTabOrder(self.startButton, self.excludeFilesEdit)
        TabnannyDialog.setTabOrder(self.excludeFilesEdit, self.resultList)
        TabnannyDialog.setTabOrder(self.resultList, self.buttonBox)

    def retranslateUi(self, TabnannyDialog):
        _translate = QtCore.QCoreApplication.translate
        TabnannyDialog.setWindowTitle(_translate("TabnannyDialog", "Tabnanny Result"))
        TabnannyDialog.setWhatsThis(_translate("TabnannyDialog", "<b>Tabnanny Results</b>\n"
"<p>This dialog shows the results of the tabnanny command. Double clicking an\n"
"entry will open an editor window and position the cursor at the respective line.</p>"))
        self.label_2.setText(_translate("TabnannyDialog", "Exclude Files:"))
        self.excludeFilesEdit.setToolTip(_translate("TabnannyDialog", "Enter filename patterns of files to be excluded separated by a comma"))
        self.startButton.setToolTip(_translate("TabnannyDialog", "Press to start the tabnanny run"))
        self.startButton.setText(_translate("TabnannyDialog", "Start"))
        self.resultList.setWhatsThis(_translate("TabnannyDialog", "<b>Result List</b>\n"
"<p>This list shows the results of the tabnanny command. Double clicking\n"
"an entry will open this entry in an editor window and position the cursor at\n"
"the respective line.</p>"))
        self.resultList.setSortingEnabled(True)
        self.resultList.headerItem().setText(0, _translate("TabnannyDialog", "Filename"))
        self.resultList.headerItem().setText(1, _translate("TabnannyDialog", "#"))
        self.resultList.headerItem().setText(2, _translate("TabnannyDialog", "Source"))
        self.checkProgress.setToolTip(_translate("TabnannyDialog", "Shows the progress of the tabnanny action"))
        self.checkProgress.setFormat(_translate("TabnannyDialog", "%v/%m Files"))

from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5SqueezeLabels import E5SqueezeLabelPath

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabnannyDialog = QtWidgets.QDialog()
    ui = Ui_TabnannyDialog()
    ui.setupUi(TabnannyDialog)
    TabnannyDialog.show()
    sys.exit(app.exec_())

