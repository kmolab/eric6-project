# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorSyntaxPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorSyntaxPage(object):
    def setupUi(self, EditorSyntaxPage):
        EditorSyntaxPage.setObjectName("EditorSyntaxPage")
        EditorSyntaxPage.resize(400, 412)
        EditorSyntaxPage.setWindowTitle("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EditorSyntaxPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(EditorSyntaxPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line2 = QtWidgets.QFrame(EditorSyntaxPage)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setObjectName("line2")
        self.verticalLayout_2.addWidget(self.line2)
        self.automaticSyntaxCheckCheckBox = QtWidgets.QGroupBox(EditorSyntaxPage)
        self.automaticSyntaxCheckCheckBox.setCheckable(True)
        self.automaticSyntaxCheckCheckBox.setObjectName("automaticSyntaxCheckCheckBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.automaticSyntaxCheckCheckBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.onlineCheckBox = QtWidgets.QGroupBox(self.automaticSyntaxCheckCheckBox)
        self.onlineCheckBox.setCheckable(True)
        self.onlineCheckBox.setObjectName("onlineCheckBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.onlineCheckBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.onlineCheckBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.onlineTimeoutSpinBox = QtWidgets.QSpinBox(self.onlineCheckBox)
        self.onlineTimeoutSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.onlineTimeoutSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.onlineTimeoutSpinBox.setProperty("value", 5)
        self.onlineTimeoutSpinBox.setObjectName("onlineTimeoutSpinBox")
        self.horizontalLayout.addWidget(self.onlineTimeoutSpinBox)
        spacerItem = QtWidgets.QSpacerItem(205, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.onlineCheckBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.automaticSyntaxCheckCheckBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.includeCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.includeCheckBox.setObjectName("includeCheckBox")
        self.verticalLayout.addWidget(self.includeCheckBox)
        self.ignoreStarImportCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.ignoreStarImportCheckBox.setObjectName("ignoreStarImportCheckBox")
        self.verticalLayout.addWidget(self.ignoreStarImportCheckBox)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_2.addWidget(self.automaticSyntaxCheckCheckBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(EditorSyntaxPage)
        QtCore.QMetaObject.connectSlotsByName(EditorSyntaxPage)

    def retranslateUi(self, EditorSyntaxPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorSyntaxPage", "<b>Configure Code Checker settings</b>"))
        self.automaticSyntaxCheckCheckBox.setToolTip(_translate("EditorSyntaxPage", "Select, whether source files should be checked automatically for syntax errors"))
        self.automaticSyntaxCheckCheckBox.setWhatsThis(_translate("EditorSyntaxPage", "<b>Automatic Syntax Check</b><p>Select to enable the automatic syntax checker. The syntax is checked, when a file is loaded or saved or the programming language of the editor is selected.</p>"))
        self.automaticSyntaxCheckCheckBox.setTitle(_translate("EditorSyntaxPage", "Automatic Syntax Check"))
        self.onlineCheckBox.setToolTip(_translate("EditorSyntaxPage", "Select to enable the online syntax checker"))
        self.onlineCheckBox.setWhatsThis(_translate("EditorSyntaxPage", "<b>Online Syntax Check</b><p>Select this to enable syntax checks while typing. The check is performed, if typing is interrupted for the configured timeout period.</p>"))
        self.onlineCheckBox.setTitle(_translate("EditorSyntaxPage", "Online Syntax Check"))
        self.label.setText(_translate("EditorSyntaxPage", "Timeout Interval:"))
        self.onlineTimeoutSpinBox.setToolTip(_translate("EditorSyntaxPage", "Enter the timeout for the online syntax checker"))
        self.onlineTimeoutSpinBox.setWhatsThis(_translate("EditorSyntaxPage", "<b>Timeout Interval</b><p>Enter the timeout interval for the online syntax check. The check is performed, if typing is interrupted for the configured timeout period.</p>"))
        self.onlineTimeoutSpinBox.setSuffix(_translate("EditorSyntaxPage", " s"))
        self.groupBox_2.setTitle(_translate("EditorSyntaxPage", "PyFlakes"))
        self.includeCheckBox.setToolTip(_translate("EditorSyntaxPage", "Select to include a PyFlakes check after the syntax check"))
        self.includeCheckBox.setText(_translate("EditorSyntaxPage", "Include PyFlakes Checks after syntax check"))
        self.ignoreStarImportCheckBox.setToolTip(_translate("EditorSyntaxPage", "Select to suppress star import warnings"))
        self.ignoreStarImportCheckBox.setText(_translate("EditorSyntaxPage", "Suppress star import warnings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorSyntaxPage = QtWidgets.QWidget()
    ui = Ui_EditorSyntaxPage()
    ui.setupUi(EditorSyntaxPage)
    EditorSyntaxPage.show()
    sys.exit(app.exec_())

