# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Debugger\StartDebugDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartDebugDialog(object):
    def setupUi(self, StartDebugDialog):
        StartDebugDialog.setObjectName("StartDebugDialog")
        StartDebugDialog.resize(488, 284)
        StartDebugDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(StartDebugDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.TextLabel1 = QtWidgets.QLabel(StartDebugDialog)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridLayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.cmdlineCombo = QtWidgets.QComboBox(StartDebugDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdlineCombo.sizePolicy().hasHeightForWidth())
        self.cmdlineCombo.setSizePolicy(sizePolicy)
        self.cmdlineCombo.setEditable(True)
        self.cmdlineCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.cmdlineCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmdlineCombo.setDuplicatesEnabled(False)
        self.cmdlineCombo.setObjectName("cmdlineCombo")
        self.gridLayout.addWidget(self.cmdlineCombo, 0, 1, 1, 1)
        self.TextLabel2 = QtWidgets.QLabel(StartDebugDialog)
        self.TextLabel2.setObjectName("TextLabel2")
        self.gridLayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.workdirPicker = E5ComboPathPicker(StartDebugDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workdirPicker.sizePolicy().hasHeightForWidth())
        self.workdirPicker.setSizePolicy(sizePolicy)
        self.workdirPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.workdirPicker.setObjectName("workdirPicker")
        self.gridLayout.addWidget(self.workdirPicker, 1, 1, 1, 1)
        self.textLabel1 = QtWidgets.QLabel(StartDebugDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 2, 0, 1, 1)
        self.environmentCombo = QtWidgets.QComboBox(StartDebugDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.environmentCombo.sizePolicy().hasHeightForWidth())
        self.environmentCombo.setSizePolicy(sizePolicy)
        self.environmentCombo.setEditable(True)
        self.environmentCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.environmentCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.environmentCombo.setDuplicatesEnabled(False)
        self.environmentCombo.setObjectName("environmentCombo")
        self.gridLayout.addWidget(self.environmentCombo, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.exceptionCheckBox = QtWidgets.QCheckBox(StartDebugDialog)
        self.exceptionCheckBox.setChecked(True)
        self.exceptionCheckBox.setObjectName("exceptionCheckBox")
        self.gridLayout_2.addWidget(self.exceptionCheckBox, 0, 0, 1, 1)
        self.clearShellCheckBox = QtWidgets.QCheckBox(StartDebugDialog)
        self.clearShellCheckBox.setChecked(True)
        self.clearShellCheckBox.setObjectName("clearShellCheckBox")
        self.gridLayout_2.addWidget(self.clearShellCheckBox, 0, 1, 1, 1)
        self.consoleCheckBox = QtWidgets.QCheckBox(StartDebugDialog)
        self.consoleCheckBox.setObjectName("consoleCheckBox")
        self.gridLayout_2.addWidget(self.consoleCheckBox, 1, 0, 1, 1)
        self.tracePythonCheckBox = QtWidgets.QCheckBox(StartDebugDialog)
        self.tracePythonCheckBox.setObjectName("tracePythonCheckBox")
        self.gridLayout_2.addWidget(self.tracePythonCheckBox, 2, 0, 1, 1)
        self.autoContinueCheckBox = QtWidgets.QCheckBox(StartDebugDialog)
        self.autoContinueCheckBox.setChecked(True)
        self.autoContinueCheckBox.setObjectName("autoContinueCheckBox")
        self.gridLayout_2.addWidget(self.autoContinueCheckBox, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.groupBox = QtWidgets.QGroupBox(StartDebugDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.forkModeCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.forkModeCheckBox.setObjectName("forkModeCheckBox")
        self.horizontalLayout.addWidget(self.forkModeCheckBox)
        self.forkChildCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.forkChildCheckBox.setEnabled(False)
        self.forkChildCheckBox.setObjectName("forkChildCheckBox")
        self.horizontalLayout.addWidget(self.forkChildCheckBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(StartDebugDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.TextLabel1.setBuddy(self.cmdlineCombo)
        self.TextLabel2.setBuddy(self.workdirPicker)
        self.textLabel1.setBuddy(self.environmentCombo)

        self.retranslateUi(StartDebugDialog)
        self.buttonBox.accepted.connect(StartDebugDialog.accept)
        self.buttonBox.rejected.connect(StartDebugDialog.reject)
        self.forkModeCheckBox.toggled['bool'].connect(self.forkChildCheckBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(StartDebugDialog)
        StartDebugDialog.setTabOrder(self.cmdlineCombo, self.workdirPicker)
        StartDebugDialog.setTabOrder(self.workdirPicker, self.environmentCombo)
        StartDebugDialog.setTabOrder(self.environmentCombo, self.exceptionCheckBox)
        StartDebugDialog.setTabOrder(self.exceptionCheckBox, self.clearShellCheckBox)
        StartDebugDialog.setTabOrder(self.clearShellCheckBox, self.consoleCheckBox)
        StartDebugDialog.setTabOrder(self.consoleCheckBox, self.tracePythonCheckBox)
        StartDebugDialog.setTabOrder(self.tracePythonCheckBox, self.autoContinueCheckBox)
        StartDebugDialog.setTabOrder(self.autoContinueCheckBox, self.forkModeCheckBox)
        StartDebugDialog.setTabOrder(self.forkModeCheckBox, self.forkChildCheckBox)

    def retranslateUi(self, StartDebugDialog):
        _translate = QtCore.QCoreApplication.translate
        StartDebugDialog.setWindowTitle(_translate("StartDebugDialog", "Start debugging"))
        self.TextLabel1.setText(_translate("StartDebugDialog", "Command&line:"))
        self.cmdlineCombo.setToolTip(_translate("StartDebugDialog", "Enter the commandline parameters"))
        self.cmdlineCombo.setWhatsThis(_translate("StartDebugDialog", "<b>Commandline</b>\n"
"<p>Enter the commandline parameters in this field.</p>"))
        self.TextLabel2.setText(_translate("StartDebugDialog", "&Working directory:"))
        self.workdirPicker.setToolTip(_translate("StartDebugDialog", "Enter the working directory"))
        self.workdirPicker.setWhatsThis(_translate("StartDebugDialog", "<b>Working directory</b>\n"
"<p>Enter the working directory of the application to be debugged. Leave it empty to set the working directory to the executable directory.</p>"))
        self.textLabel1.setText(_translate("StartDebugDialog", "&Environment:"))
        self.environmentCombo.setToolTip(_translate("StartDebugDialog", "Enter the environment variables to be set."))
        self.environmentCombo.setWhatsThis(_translate("StartDebugDialog", "<b>Environment</b>\n"
"<p>Enter the environment variables to be set for the program. The individual settings must be separated by whitespace and be given in the form \'var=value\'. In order to add to an environment variable, enter it in the form \'var+=value\'.</p>\n"
"<p>Example: var1=1 var2=\"hello world\" var3+=\":/tmp\"</p>"))
        self.exceptionCheckBox.setToolTip(_translate("StartDebugDialog", "Uncheck to disable exception reporting"))
        self.exceptionCheckBox.setWhatsThis(_translate("StartDebugDialog", "<b>Report exceptions</b>\n"
"<p>Uncheck this in order to disable exception reporting.</p>"))
        self.exceptionCheckBox.setText(_translate("StartDebugDialog", "Report &exceptions"))
        self.exceptionCheckBox.setShortcut(_translate("StartDebugDialog", "Alt+E"))
        self.clearShellCheckBox.setToolTip(_translate("StartDebugDialog", "Select to clear the display of the interpreter window"))
        self.clearShellCheckBox.setWhatsThis(_translate("StartDebugDialog", "<b>Clear interpreter window</b><p>This clears the display of the interpreter window before starting the debug client.</p>"))
        self.clearShellCheckBox.setText(_translate("StartDebugDialog", "Clear &interpreter window"))
        self.consoleCheckBox.setToolTip(_translate("StartDebugDialog", "Select to start the debugger in a console window"))
        self.consoleCheckBox.setWhatsThis(_translate("StartDebugDialog", "<b>Start in console</b>\n"
"<p>Select to start the debugger in a console window. The console command has to be configured on the Debugger-&gt;General page</p>"))
        self.consoleCheckBox.setText(_translate("StartDebugDialog", "Start in console"))
        self.tracePythonCheckBox.setToolTip(_translate("StartDebugDialog", "Select to trace into the Python library"))
        self.tracePythonCheckBox.setText(_translate("StartDebugDialog", "&Trace into interpreter libraries"))
        self.tracePythonCheckBox.setShortcut(_translate("StartDebugDialog", "Alt+T"))
        self.autoContinueCheckBox.setToolTip(_translate("StartDebugDialog", "Select to not stop the debugger at the first executable line."))
        self.autoContinueCheckBox.setWhatsThis(_translate("StartDebugDialog", "<b>Don\'t stop at first line</b><p>This prevents the debugger from stopping at the first executable line.</p>"))
        self.autoContinueCheckBox.setText(_translate("StartDebugDialog", "Don\'t stop at first line"))
        self.groupBox.setTitle(_translate("StartDebugDialog", "Forking"))
        self.forkModeCheckBox.setToolTip(_translate("StartDebugDialog", "Select to go through the fork without asking"))
        self.forkModeCheckBox.setWhatsThis(_translate("StartDebugDialog", "<b>Fork without pausing</b>\n"
"<p>Select to go through the fork without asking making the forking decision based on the Parent/Child selection.</p>"))
        self.forkModeCheckBox.setText(_translate("StartDebugDialog", "Fork without pausing"))
        self.forkChildCheckBox.setToolTip(_translate("StartDebugDialog", "Select to debug the child process after forking"))
        self.forkChildCheckBox.setWhatsThis(_translate("StartDebugDialog", "<b>Debug Child Process</b>\n"
"<p>Select to debug the child process after forking. If it is not selected, the parent process will be debugged. This has no effect, if forking without pausing is not selected.</p>"))
        self.forkChildCheckBox.setText(_translate("StartDebugDialog", "Follow Child Process"))

from E5Gui.E5PathPicker import E5ComboPathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartDebugDialog = QtWidgets.QDialog()
    ui = Ui_StartDebugDialog()
    ui.setupUi(StartDebugDialog)
    StartDebugDialog.show()
    sys.exit(app.exec_())
