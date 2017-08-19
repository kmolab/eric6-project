# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\DebuggerPythonPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DebuggerPythonPage(object):
    def setupUi(self, DebuggerPythonPage):
        DebuggerPythonPage.setObjectName("DebuggerPythonPage")
        DebuggerPythonPage.resize(455, 449)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DebuggerPythonPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(DebuggerPythonPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line11_2 = QtWidgets.QFrame(DebuggerPythonPage)
        self.line11_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11_2.setObjectName("line11_2")
        self.verticalLayout_2.addWidget(self.line11_2)
        self.groupBox = QtWidgets.QGroupBox(DebuggerPythonPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.interpreterPicker = E5PathPicker(self.groupBox)
        self.interpreterPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.interpreterPicker.setObjectName("interpreterPicker")
        self.verticalLayout_3.addWidget(self.interpreterPicker)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(DebuggerPythonPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.debugClientPicker = E5PathPicker(self.groupBox_2)
        self.debugClientPicker.setEnabled(False)
        self.debugClientPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.debugClientPicker.setObjectName("debugClientPicker")
        self.gridLayout.addWidget(self.debugClientPicker, 1, 0, 1, 2)
        self.standardButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.standardButton.setObjectName("standardButton")
        self.gridLayout.addWidget(self.standardButton, 0, 0, 1, 1)
        self.customButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.customButton.setObjectName("customButton")
        self.gridLayout.addWidget(self.customButton, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(DebuggerPythonPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.sourceExtensionsEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.sourceExtensionsEdit.setObjectName("sourceExtensionsEdit")
        self.verticalLayout.addWidget(self.sourceExtensionsEdit)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.pyRedirectCheckBox = QtWidgets.QCheckBox(DebuggerPythonPage)
        self.pyRedirectCheckBox.setObjectName("pyRedirectCheckBox")
        self.verticalLayout_2.addWidget(self.pyRedirectCheckBox)
        self.pyNoEncodingCheckBox = QtWidgets.QCheckBox(DebuggerPythonPage)
        self.pyNoEncodingCheckBox.setObjectName("pyNoEncodingCheckBox")
        self.verticalLayout_2.addWidget(self.pyNoEncodingCheckBox)
        spacerItem = QtWidgets.QSpacerItem(435, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(DebuggerPythonPage)
        self.customButton.toggled['bool'].connect(self.debugClientPicker.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DebuggerPythonPage)
        DebuggerPythonPage.setTabOrder(self.interpreterPicker, self.standardButton)
        DebuggerPythonPage.setTabOrder(self.standardButton, self.customButton)
        DebuggerPythonPage.setTabOrder(self.customButton, self.debugClientPicker)
        DebuggerPythonPage.setTabOrder(self.debugClientPicker, self.sourceExtensionsEdit)
        DebuggerPythonPage.setTabOrder(self.sourceExtensionsEdit, self.pyRedirectCheckBox)
        DebuggerPythonPage.setTabOrder(self.pyRedirectCheckBox, self.pyNoEncodingCheckBox)

    def retranslateUi(self, DebuggerPythonPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("DebuggerPythonPage", "<b>Configure Python Debugger</b>"))
        self.groupBox.setTitle(_translate("DebuggerPythonPage", "Python Interpreter for Debug Client"))
        self.interpreterPicker.setToolTip(_translate("DebuggerPythonPage", "Enter the path of the Python interpreter to be used by the debug client."))
        self.groupBox_2.setTitle(_translate("DebuggerPythonPage", "Debug Client Type"))
        self.debugClientPicker.setToolTip(_translate("DebuggerPythonPage", "Enter the path of the Debug Client to be used.  Leave empty to use the default."))
        self.standardButton.setToolTip(_translate("DebuggerPythonPage", "Select the standard debug client"))
        self.standardButton.setText(_translate("DebuggerPythonPage", "Standard"))
        self.customButton.setToolTip(_translate("DebuggerPythonPage", "Select the custom selected debug client"))
        self.customButton.setText(_translate("DebuggerPythonPage", "Custom"))
        self.groupBox_3.setTitle(_translate("DebuggerPythonPage", "Source association"))
        self.label.setText(_translate("DebuggerPythonPage", "Enter the file extensions to be associated with the Python2 debugger separated by a space. They must not overlap with the ones for Python3."))
        self.pyRedirectCheckBox.setToolTip(_translate("DebuggerPythonPage", "Select, to redirect stdin, stdout and stderr of the program being debugged to the eric6 IDE"))
        self.pyRedirectCheckBox.setText(_translate("DebuggerPythonPage", "Redirect stdin/stdout/stderr"))
        self.pyNoEncodingCheckBox.setToolTip(_translate("DebuggerPythonPage", "Select to not set the debug client encoding"))
        self.pyNoEncodingCheckBox.setText(_translate("DebuggerPythonPage", "Don\'t set the encoding of the debug client"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DebuggerPythonPage = QtWidgets.QWidget()
    ui = Ui_DebuggerPythonPage()
    ui.setupUi(DebuggerPythonPage)
    DebuggerPythonPage.show()
    sys.exit(app.exec_())

