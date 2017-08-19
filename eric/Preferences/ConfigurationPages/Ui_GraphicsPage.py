# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\GraphicsPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GraphicsPage(object):
    def setupUi(self, GraphicsPage):
        GraphicsPage.setObjectName("GraphicsPage")
        GraphicsPage.resize(440, 334)
        self.vboxlayout = QtWidgets.QVBoxLayout(GraphicsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(GraphicsPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line7 = QtWidgets.QFrame(GraphicsPage)
        self.line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line7.setObjectName("line7")
        self.vboxlayout.addWidget(self.line7)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.graphicsFontButton = QtWidgets.QPushButton(GraphicsPage)
        self.graphicsFontButton.setObjectName("graphicsFontButton")
        self.hboxlayout.addWidget(self.graphicsFontButton)
        self.graphicsFontSample = QtWidgets.QLineEdit(GraphicsPage)
        self.graphicsFontSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.graphicsFontSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.graphicsFontSample.setReadOnly(True)
        self.graphicsFontSample.setObjectName("graphicsFontSample")
        self.hboxlayout.addWidget(self.graphicsFontSample)
        self.vboxlayout.addLayout(self.hboxlayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(GraphicsPage)
        QtCore.QMetaObject.connectSlotsByName(GraphicsPage)

    def retranslateUi(self, GraphicsPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("GraphicsPage", "<b>Configure graphics settings</b>"))
        self.graphicsFontButton.setToolTip(_translate("GraphicsPage", "Press to select the font for the graphic items"))
        self.graphicsFontButton.setText(_translate("GraphicsPage", "Graphics Font"))
        self.graphicsFontSample.setText(_translate("GraphicsPage", "Graphics Font"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphicsPage = QtWidgets.QWidget()
    ui = Ui_GraphicsPage()
    ui.setupUi(GraphicsPage)
    GraphicsPage.show()
    sys.exit(app.exec_())

