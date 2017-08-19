# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorMouseClickHandlerPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorMouseClickHandlerPage(object):
    def setupUi(self, EditorMouseClickHandlerPage):
        EditorMouseClickHandlerPage.setObjectName("EditorMouseClickHandlerPage")
        EditorMouseClickHandlerPage.resize(506, 398)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditorMouseClickHandlerPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(EditorMouseClickHandlerPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line6 = QtWidgets.QFrame(EditorMouseClickHandlerPage)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setObjectName("line6")
        self.verticalLayout.addWidget(self.line6)
        self.mcEnabledCheckBox = QtWidgets.QCheckBox(EditorMouseClickHandlerPage)
        self.mcEnabledCheckBox.setObjectName("mcEnabledCheckBox")
        self.verticalLayout.addWidget(self.mcEnabledCheckBox)
        spacerItem = QtWidgets.QSpacerItem(456, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(EditorMouseClickHandlerPage)
        QtCore.QMetaObject.connectSlotsByName(EditorMouseClickHandlerPage)

    def retranslateUi(self, EditorMouseClickHandlerPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorMouseClickHandlerPage", "<b>Configure Mouse Click Handler Support</b>"))
        self.mcEnabledCheckBox.setToolTip(_translate("EditorMouseClickHandlerPage", "Select this to enable support for mouse click handlers"))
        self.mcEnabledCheckBox.setWhatsThis(_translate("EditorMouseClickHandlerPage", "<b>Mouse Click Handlers Enabled</b><p>Select to enable support for mouse click handlers. Individual mouse click handlers may be configured on subordinate pages, if such have been installed and registered. This is usually done by plug-ins.</p>"))
        self.mcEnabledCheckBox.setText(_translate("EditorMouseClickHandlerPage", "Mouse Click Handlers Enabled"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorMouseClickHandlerPage = QtWidgets.QWidget()
    ui = Ui_EditorMouseClickHandlerPage()
    ui.setupUi(EditorMouseClickHandlerPage)
    EditorMouseClickHandlerPage.show()
    sys.exit(app.exec_())

