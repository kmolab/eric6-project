# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\LogViewerPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LogViewerPage(object):
    def setupUi(self, LogViewerPage):
        LogViewerPage.setObjectName("LogViewerPage")
        LogViewerPage.resize(480, 515)
        self.verticalLayout = QtWidgets.QVBoxLayout(LogViewerPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(LogViewerPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line9 = QtWidgets.QFrame(LogViewerPage)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setObjectName("line9")
        self.verticalLayout.addWidget(self.line9)
        self.lvAutoRaiseCheckBox = QtWidgets.QCheckBox(LogViewerPage)
        self.lvAutoRaiseCheckBox.setObjectName("lvAutoRaiseCheckBox")
        self.verticalLayout.addWidget(self.lvAutoRaiseCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TextLabel3_2_2 = QtWidgets.QLabel(LogViewerPage)
        self.TextLabel3_2_2.setObjectName("TextLabel3_2_2")
        self.horizontalLayout.addWidget(self.TextLabel3_2_2)
        self.stderrTextColourButton = QtWidgets.QPushButton(LogViewerPage)
        self.stderrTextColourButton.setMinimumSize(QtCore.QSize(100, 0))
        self.stderrTextColourButton.setText("")
        self.stderrTextColourButton.setObjectName("stderrTextColourButton")
        self.horizontalLayout.addWidget(self.stderrTextColourButton)
        spacerItem = QtWidgets.QSpacerItem(316, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(LogViewerPage)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.filtersTabWidget = QtWidgets.QTabWidget(LogViewerPage)
        self.filtersTabWidget.setObjectName("filtersTabWidget")
        self.stdout = QtWidgets.QWidget()
        self.stdout.setObjectName("stdout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stdout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stdoutFilterEdit = E5StringListEditWidget(self.stdout)
        self.stdoutFilterEdit.setObjectName("stdoutFilterEdit")
        self.verticalLayout_2.addWidget(self.stdoutFilterEdit)
        self.filtersTabWidget.addTab(self.stdout, "")
        self.stderr = QtWidgets.QWidget()
        self.stderr.setObjectName("stderr")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.stderr)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stderrFilterEdit = E5StringListEditWidget(self.stderr)
        self.stderrFilterEdit.setObjectName("stderrFilterEdit")
        self.verticalLayout_3.addWidget(self.stderrFilterEdit)
        self.filtersTabWidget.addTab(self.stderr, "")
        self.stdxxx = QtWidgets.QWidget()
        self.stdxxx.setObjectName("stdxxx")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.stdxxx)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stdxxxFilterEdit = E5StringListEditWidget(self.stdxxx)
        self.stdxxxFilterEdit.setObjectName("stdxxxFilterEdit")
        self.verticalLayout_4.addWidget(self.stdxxxFilterEdit)
        self.filtersTabWidget.addTab(self.stdxxx, "")
        self.verticalLayout.addWidget(self.filtersTabWidget)

        self.retranslateUi(LogViewerPage)
        self.filtersTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LogViewerPage)
        LogViewerPage.setTabOrder(self.lvAutoRaiseCheckBox, self.stderrTextColourButton)
        LogViewerPage.setTabOrder(self.stderrTextColourButton, self.filtersTabWidget)

    def retranslateUi(self, LogViewerPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("LogViewerPage", "<b>Configure Log Viewer</b>"))
        self.lvAutoRaiseCheckBox.setToolTip(_translate("LogViewerPage", "Select to show the log-viewer upon new output"))
        self.lvAutoRaiseCheckBox.setText(_translate("LogViewerPage", "Show upon new output"))
        self.TextLabel3_2_2.setText(_translate("LogViewerPage", "Error Colour:"))
        self.stderrTextColourButton.setToolTip(_translate("LogViewerPage", "Select the colour for text sent to stderr"))
        self.label.setText(_translate("LogViewerPage", "Message Filters:"))
        self.filtersTabWidget.setTabText(self.filtersTabWidget.indexOf(self.stdout), _translate("LogViewerPage", "Standard Output"))
        self.filtersTabWidget.setTabText(self.filtersTabWidget.indexOf(self.stderr), _translate("LogViewerPage", "Standard Error"))
        self.filtersTabWidget.setTabText(self.filtersTabWidget.indexOf(self.stdxxx), _translate("LogViewerPage", "Both"))

from E5Gui.E5StringListEditWidget import E5StringListEditWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogViewerPage = QtWidgets.QWidget()
    ui = Ui_LogViewerPage()
    ui.setupUi(LogViewerPage)
    LogViewerPage.show()
    sys.exit(app.exec_())

