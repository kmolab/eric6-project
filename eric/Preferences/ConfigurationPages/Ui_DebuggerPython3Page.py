# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\DebuggerPython3Page.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DebuggerPython3Page(object):
    def setupUi(self, DebuggerPython3Page):
        DebuggerPython3Page.setObjectName("DebuggerPython3Page")
        DebuggerPython3Page.resize(455, 449)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DebuggerPython3Page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(DebuggerPython3Page)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line11_2 = QtWidgets.QFrame(DebuggerPython3Page)
        self.line11_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line11_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line11_2.setObjectName("line11_2")
        self.verticalLayout_2.addWidget(self.line11_2)
        self.groupBox = QtWidgets.QGroupBox(DebuggerPython3Page)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.interpreterPicker = E5PathPicker(self.groupBox)
        self.interpreterPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.interpreterPicker.setObjectName("interpreterPicker")
        self.verticalLayout_3.addWidget(self.interpreterPicker)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(DebuggerPython3Page)
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
        self.groupBox_3 = QtWidgets.QGroupBox(DebuggerPython3Page)
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
        self.pyRedirectCheckBox = QtWidgets.QCheckBox(DebuggerPython3Page)
        self.pyRedirectCheckBox.setObjectName("pyRedirectCheckBox")
        self.verticalLayout_2.addWidget(self.pyRedirectCheckBox)
        self.pyNoEncodingCheckBox = QtWidgets.QCheckBox(DebuggerPython3Page)
        self.pyNoEncodingCheckBox.setObjectName("pyNoEncodingCheckBox")
        self.verticalLayout_2.addWidget(self.pyNoEncodingCheckBox)
        spacerItem = QtWidgets.QSpacerItem(435, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(DebuggerPython3Page)
        self.customButton.toggled['bool'].connect(self.debugClientPicker.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(DebuggerPython3Page)
        DebuggerPython3Page.setTabOrder(self.interpreterPicker, self.standardButton)
        DebuggerPython3Page.setTabOrder(self.standardButton, self.customButton)
        DebuggerPython3Page.setTabOrder(self.customButton, self.debugClientPicker)
        DebuggerPython3Page.setTabOrder(self.debugClientPicker, self.sourceExtensionsEdit)
        DebuggerPython3Page.setTabOrder(self.sourceExtensionsEdit, self.pyRedirectCheckBox)
        DebuggerPython3Page.setTabOrder(self.pyRedirectCheckBox, self.pyNoEncodingCheckBox)

    def retranslateUi(self, DebuggerPython3Page):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("DebuggerPython3Page", "<b>Configure Python3 Debugger</b>"))
        self.groupBox.setTitle(_translate("DebuggerPython3Page", "Python3 Interpreter for Debug Client"))
        self.interpreterPicker.setToolTip(_translate("DebuggerPython3Page", "Enter the path of the Python3 interpreter to be used by the debug client. Leave empty to use the default."))
        self.groupBox_2.setTitle(_translate("DebuggerPython3Page", "Debug Client Type"))
        self.debugClientPicker.setToolTip(_translate("DebuggerPython3Page", "Enter the path of the Debug Client to be used.  Leave empty to use the default."))
        self.standardButton.setToolTip(_translate("DebuggerPython3Page", "Select the standard debug client"))
        self.standardButton.setText(_translate("DebuggerPython3Page", "Standard"))
        self.customButton.setToolTip(_translate("DebuggerPython3Page", "Select the custom selected debug client"))
        self.customButton.setText(_translate("DebuggerPython3Page", "Custom"))
        self.groupBox_3.setTitle(_translate("DebuggerPython3Page", "Source association"))
        self.label.setText(_translate("DebuggerPython3Page", "Enter the file extensions to be associated with the Python3 debugger separated by a space. They must not overlap with the ones for Python2."))
        self.pyRedirectCheckBox.setToolTip(_translate("DebuggerPython3Page", "Select, to redirect stdin, stdout and stderr of the program being debugged to the eric6 IDE"))
        self.pyRedirectCheckBox.setText(_translate("DebuggerPython3Page", "Redirect stdin/stdout/stderr"))
        self.pyNoEncodingCheckBox.setToolTip(_translate("DebuggerPython3Page", "Select to not set the debug client encoding"))
        self.pyNoEncodingCheckBox.setText(_translate("DebuggerPython3Page", "Don\'t set the encoding of the debug client"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DebuggerPython3Page = QtWidgets.QWidget()
    ui = Ui_DebuggerPython3Page()
    ui.setupUi(DebuggerPython3Page)
    DebuggerPython3Page.show()
    sys.exit(app.exec_())

