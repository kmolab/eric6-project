# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\DataViews\CodeMetricsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CodeMetricsDialog(object):
    def setupUi(self, CodeMetricsDialog):
        CodeMetricsDialog.setObjectName("CodeMetricsDialog")
        CodeMetricsDialog.resize(832, 587)
        CodeMetricsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(CodeMetricsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterFrame = QtWidgets.QFrame(CodeMetricsDialog)
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
        self.resultList = QtWidgets.QTreeWidget(CodeMetricsDialog)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setObjectName("resultList")
        self.verticalLayout.addWidget(self.resultList)
        self.summaryList = QtWidgets.QTreeWidget(CodeMetricsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summaryList.sizePolicy().hasHeightForWidth())
        self.summaryList.setSizePolicy(sizePolicy)
        self.summaryList.setAlternatingRowColors(True)
        self.summaryList.setObjectName("summaryList")
        self.verticalLayout.addWidget(self.summaryList)
        self.checkProgress = QtWidgets.QProgressBar(CodeMetricsDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName("checkProgress")
        self.verticalLayout.addWidget(self.checkProgress)
        self.buttonBox = QtWidgets.QDialogButtonBox(CodeMetricsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CodeMetricsDialog)
        QtCore.QMetaObject.connectSlotsByName(CodeMetricsDialog)
        CodeMetricsDialog.setTabOrder(self.startButton, self.excludeFilesEdit)
        CodeMetricsDialog.setTabOrder(self.excludeFilesEdit, self.resultList)
        CodeMetricsDialog.setTabOrder(self.resultList, self.summaryList)
        CodeMetricsDialog.setTabOrder(self.summaryList, self.buttonBox)

    def retranslateUi(self, CodeMetricsDialog):
        _translate = QtCore.QCoreApplication.translate
        CodeMetricsDialog.setWindowTitle(_translate("CodeMetricsDialog", "Code Metrics"))
        CodeMetricsDialog.setWhatsThis(_translate("CodeMetricsDialog", "<b>Code Metrics</b>\n"
"<p>This dialog shows some code metrics.</p>"))
        self.label_2.setText(_translate("CodeMetricsDialog", "Exclude Files:"))
        self.excludeFilesEdit.setToolTip(_translate("CodeMetricsDialog", "Enter filename patterns of files to be excluded separated by a comma"))
        self.startButton.setToolTip(_translate("CodeMetricsDialog", "Press to start the code metrics run"))
        self.startButton.setText(_translate("CodeMetricsDialog", "Start"))
        self.resultList.setWhatsThis(_translate("CodeMetricsDialog", "<b>Code metrics</b>\n"
"<p>This list shows some code metrics.</p>"))
        self.resultList.headerItem().setText(0, _translate("CodeMetricsDialog", "Name"))
        self.resultList.headerItem().setText(1, _translate("CodeMetricsDialog", "Start"))
        self.resultList.headerItem().setText(2, _translate("CodeMetricsDialog", "End"))
        self.resultList.headerItem().setText(3, _translate("CodeMetricsDialog", "Lines"))
        self.resultList.headerItem().setText(4, _translate("CodeMetricsDialog", "Lines of code"))
        self.resultList.headerItem().setText(5, _translate("CodeMetricsDialog", "Comments"))
        self.resultList.headerItem().setText(6, _translate("CodeMetricsDialog", "Empty"))
        self.summaryList.setWhatsThis(_translate("CodeMetricsDialog", "<b>Summary</b>\n"
"<p>This shows some overall code metrics.</p>"))
        self.summaryList.headerItem().setText(0, _translate("CodeMetricsDialog", "Summary"))
        self.summaryList.headerItem().setText(1, _translate("CodeMetricsDialog", "#"))
        self.checkProgress.setToolTip(_translate("CodeMetricsDialog", "Shows the progress of the code metrics action"))
        self.checkProgress.setFormat(_translate("CodeMetricsDialog", "%v/%m Files"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CodeMetricsDialog = QtWidgets.QDialog()
    ui = Ui_CodeMetricsDialog()
    ui.setupUi(CodeMetricsDialog)
    CodeMetricsDialog.show()
    sys.exit(app.exec_())

