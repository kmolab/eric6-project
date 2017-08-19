# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\StatusBar\JavaScriptSettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JavaScriptSettingsDialog(object):
    def setupUi(self, JavaScriptSettingsDialog):
        JavaScriptSettingsDialog.setObjectName("JavaScriptSettingsDialog")
        JavaScriptSettingsDialog.resize(400, 87)
        JavaScriptSettingsDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(JavaScriptSettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.jsOpenWindowsCheckBox = QtWidgets.QCheckBox(JavaScriptSettingsDialog)
        self.jsOpenWindowsCheckBox.setObjectName("jsOpenWindowsCheckBox")
        self.verticalLayout.addWidget(self.jsOpenWindowsCheckBox)
        self.jsClipboardCheckBox = QtWidgets.QCheckBox(JavaScriptSettingsDialog)
        self.jsClipboardCheckBox.setObjectName("jsClipboardCheckBox")
        self.verticalLayout.addWidget(self.jsClipboardCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(JavaScriptSettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(JavaScriptSettingsDialog)
        self.buttonBox.accepted.connect(JavaScriptSettingsDialog.accept)
        self.buttonBox.rejected.connect(JavaScriptSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(JavaScriptSettingsDialog)

    def retranslateUi(self, JavaScriptSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        JavaScriptSettingsDialog.setWindowTitle(_translate("JavaScriptSettingsDialog", "JavaScript Settings"))
        self.jsOpenWindowsCheckBox.setToolTip(_translate("JavaScriptSettingsDialog", "Select to allow JavaScript to open windows"))
        self.jsOpenWindowsCheckBox.setText(_translate("JavaScriptSettingsDialog", "JavaScript can open windows"))
        self.jsClipboardCheckBox.setToolTip(_translate("JavaScriptSettingsDialog", "Select to allow JavaScript to access the clipboard"))
        self.jsClipboardCheckBox.setText(_translate("JavaScriptSettingsDialog", "JavaScript can access clipboard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JavaScriptSettingsDialog = QtWidgets.QDialog()
    ui = Ui_JavaScriptSettingsDialog()
    ui.setupUi(JavaScriptSettingsDialog)
    JavaScriptSettingsDialog.show()
    sys.exit(app.exec_())

