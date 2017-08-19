# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\CorbaPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CorbaPage(object):
    def setupUi(self, CorbaPage):
        CorbaPage.setObjectName("CorbaPage")
        CorbaPage.resize(589, 490)
        self.vboxlayout = QtWidgets.QVBoxLayout(CorbaPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(CorbaPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line13 = QtWidgets.QFrame(CorbaPage)
        self.line13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line13.setObjectName("line13")
        self.vboxlayout.addWidget(self.line13)
        self.groupBox = QtWidgets.QGroupBox(CorbaPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.idlPicker = E5PathPicker(self.groupBox)
        self.idlPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.idlPicker.setObjectName("idlPicker")
        self.verticalLayout.addWidget(self.idlPicker)
        self.textLabel1_4 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_4.setObjectName("textLabel1_4")
        self.verticalLayout.addWidget(self.textLabel1_4)
        self.vboxlayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 81, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(CorbaPage)
        QtCore.QMetaObject.connectSlotsByName(CorbaPage)

    def retranslateUi(self, CorbaPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("CorbaPage", "<b>Configure CORBA support</b>"))
        self.groupBox.setTitle(_translate("CorbaPage", "IDL Compiler"))
        self.idlPicker.setToolTip(_translate("CorbaPage", "Enter the path to the IDL compiler."))
        self.textLabel1_4.setText(_translate("CorbaPage", "<b>Note:</b> Leave this entry empty to use the default value (omniidl or omniidl.exe)."))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CorbaPage = QtWidgets.QWidget()
    ui = Ui_CorbaPage()
    ui.setupUi(CorbaPage)
    CorbaPage.show()
    sys.exit(app.exec_())

