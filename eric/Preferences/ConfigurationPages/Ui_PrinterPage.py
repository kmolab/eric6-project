# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\PrinterPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrinterPage(object):
    def setupUi(self, PrinterPage):
        PrinterPage.setObjectName("PrinterPage")
        PrinterPage.resize(448, 568)
        self.verticalLayout = QtWidgets.QVBoxLayout(PrinterPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(PrinterPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line7 = QtWidgets.QFrame(PrinterPage)
        self.line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line7.setObjectName("line7")
        self.verticalLayout.addWidget(self.line7)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.TextLabel1 = QtWidgets.QLabel(PrinterPage)
        self.TextLabel1.setObjectName("TextLabel1")
        self.gridLayout.addWidget(self.TextLabel1, 0, 0, 1, 1)
        self.printerNameEdit = QtWidgets.QLineEdit(PrinterPage)
        self.printerNameEdit.setObjectName("printerNameEdit")
        self.gridLayout.addWidget(self.printerNameEdit, 0, 1, 1, 3)
        self.TextLabel2 = QtWidgets.QLabel(PrinterPage)
        self.TextLabel2.setAlignment(QtCore.Qt.AlignTop)
        self.TextLabel2.setObjectName("TextLabel2")
        self.gridLayout.addWidget(self.TextLabel2, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(PrinterPage)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setObjectName("frame_2")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.printerColorButton = QtWidgets.QRadioButton(self.frame_2)
        self.printerColorButton.setObjectName("printerColorButton")
        self.vboxlayout.addWidget(self.printerColorButton)
        self.printerGrayscaleButton = QtWidgets.QRadioButton(self.frame_2)
        self.printerGrayscaleButton.setObjectName("printerGrayscaleButton")
        self.vboxlayout.addWidget(self.printerGrayscaleButton)
        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 3)
        self.TextLabel4 = QtWidgets.QLabel(PrinterPage)
        self.TextLabel4.setAlignment(QtCore.Qt.AlignTop)
        self.TextLabel4.setObjectName("TextLabel4")
        self.gridLayout.addWidget(self.TextLabel4, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(PrinterPage)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setObjectName("frame")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.frame)
        self.vboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.printFirstPageFirstButton = QtWidgets.QRadioButton(self.frame)
        self.printFirstPageFirstButton.setObjectName("printFirstPageFirstButton")
        self.vboxlayout1.addWidget(self.printFirstPageFirstButton)
        self.printFirstPageLastButton = QtWidgets.QRadioButton(self.frame)
        self.printFirstPageLastButton.setObjectName("printFirstPageLastButton")
        self.vboxlayout1.addWidget(self.printFirstPageLastButton)
        self.gridLayout.addWidget(self.frame, 2, 1, 1, 3)
        self.TextLabel3 = QtWidgets.QLabel(PrinterPage)
        self.TextLabel3.setObjectName("TextLabel3")
        self.gridLayout.addWidget(self.TextLabel3, 3, 0, 1, 1)
        self.printMagnificationSpinBox = QtWidgets.QSpinBox(PrinterPage)
        self.printMagnificationSpinBox.setMinimum(-10)
        self.printMagnificationSpinBox.setMaximum(10)
        self.printMagnificationSpinBox.setProperty("value", -3)
        self.printMagnificationSpinBox.setObjectName("printMagnificationSpinBox")
        self.gridLayout.addWidget(self.printMagnificationSpinBox, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(251, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 2)
        self.label = QtWidgets.QLabel(PrinterPage)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.resolutionSpinBox = QtWidgets.QSpinBox(PrinterPage)
        self.resolutionSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resolutionSpinBox.setMaximum(6000)
        self.resolutionSpinBox.setSingleStep(50)
        self.resolutionSpinBox.setObjectName("resolutionSpinBox")
        self.gridLayout.addWidget(self.resolutionSpinBox, 4, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.printheaderFontButton = QtWidgets.QPushButton(PrinterPage)
        self.printheaderFontButton.setObjectName("printheaderFontButton")
        self.gridLayout.addWidget(self.printheaderFontButton, 5, 0, 1, 1)
        self.printheaderFontSample = QtWidgets.QLineEdit(PrinterPage)
        self.printheaderFontSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.printheaderFontSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.printheaderFontSample.setReadOnly(True)
        self.printheaderFontSample.setObjectName("printheaderFontSample")
        self.gridLayout.addWidget(self.printheaderFontSample, 5, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.groupBox = QtWidgets.QGroupBox(PrinterPage)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.topMarginSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.topMarginSpinBox.setDecimals(1)
        self.topMarginSpinBox.setMaximum(9.9)
        self.topMarginSpinBox.setSingleStep(0.5)
        self.topMarginSpinBox.setObjectName("topMarginSpinBox")
        self.gridlayout.addWidget(self.topMarginSpinBox, 0, 1, 1, 1)
        self.leftMarginSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.leftMarginSpinBox.setDecimals(1)
        self.leftMarginSpinBox.setMaximum(9.9)
        self.leftMarginSpinBox.setSingleStep(0.5)
        self.leftMarginSpinBox.setObjectName("leftMarginSpinBox")
        self.gridlayout.addWidget(self.leftMarginSpinBox, 1, 0, 1, 1)
        self.rightMarginSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.rightMarginSpinBox.setDecimals(1)
        self.rightMarginSpinBox.setMaximum(9.9)
        self.rightMarginSpinBox.setSingleStep(0.5)
        self.rightMarginSpinBox.setObjectName("rightMarginSpinBox")
        self.gridlayout.addWidget(self.rightMarginSpinBox, 1, 2, 1, 1)
        self.bottomMarginSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.bottomMarginSpinBox.setDecimals(1)
        self.bottomMarginSpinBox.setMaximum(9.9)
        self.bottomMarginSpinBox.setSingleStep(0.5)
        self.bottomMarginSpinBox.setObjectName("bottomMarginSpinBox")
        self.gridlayout.addWidget(self.bottomMarginSpinBox, 2, 1, 1, 1)
        self.hboxlayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.hboxlayout)
        spacerItem3 = QtWidgets.QSpacerItem(428, 61, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(PrinterPage)
        QtCore.QMetaObject.connectSlotsByName(PrinterPage)
        PrinterPage.setTabOrder(self.printerNameEdit, self.printerColorButton)
        PrinterPage.setTabOrder(self.printerColorButton, self.printerGrayscaleButton)
        PrinterPage.setTabOrder(self.printerGrayscaleButton, self.printFirstPageFirstButton)
        PrinterPage.setTabOrder(self.printFirstPageFirstButton, self.printFirstPageLastButton)
        PrinterPage.setTabOrder(self.printFirstPageLastButton, self.printMagnificationSpinBox)
        PrinterPage.setTabOrder(self.printMagnificationSpinBox, self.resolutionSpinBox)
        PrinterPage.setTabOrder(self.resolutionSpinBox, self.printheaderFontButton)
        PrinterPage.setTabOrder(self.printheaderFontButton, self.topMarginSpinBox)
        PrinterPage.setTabOrder(self.topMarginSpinBox, self.leftMarginSpinBox)
        PrinterPage.setTabOrder(self.leftMarginSpinBox, self.rightMarginSpinBox)
        PrinterPage.setTabOrder(self.rightMarginSpinBox, self.bottomMarginSpinBox)

    def retranslateUi(self, PrinterPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("PrinterPage", "<b>Configure printer settings</b>"))
        self.TextLabel1.setText(_translate("PrinterPage", "Printername:"))
        self.TextLabel2.setText(_translate("PrinterPage", "Colour Mode:"))
        self.printerColorButton.setText(_translate("PrinterPage", "Colour"))
        self.printerGrayscaleButton.setText(_translate("PrinterPage", "Gray Scale"))
        self.TextLabel4.setText(_translate("PrinterPage", "Page Order:"))
        self.printFirstPageFirstButton.setText(_translate("PrinterPage", "First Page First"))
        self.printFirstPageLastButton.setText(_translate("PrinterPage", "Last Page First"))
        self.TextLabel3.setText(_translate("PrinterPage", "Magnification:"))
        self.label.setText(_translate("PrinterPage", "Resolution:"))
        self.resolutionSpinBox.setToolTip(_translate("PrinterPage", "Select the printer resolution "))
        self.resolutionSpinBox.setSuffix(_translate("PrinterPage", " DPI"))
        self.printheaderFontButton.setToolTip(_translate("PrinterPage", "Press to select the font for the page headers"))
        self.printheaderFontButton.setText(_translate("PrinterPage", "Header Font"))
        self.printheaderFontSample.setText(_translate("PrinterPage", "Header Font"))
        self.groupBox.setTitle(_translate("PrinterPage", "Margins"))
        self.topMarginSpinBox.setToolTip(_translate("PrinterPage", "Enter the top margin in cm."))
        self.topMarginSpinBox.setSuffix(_translate("PrinterPage", " cm"))
        self.leftMarginSpinBox.setToolTip(_translate("PrinterPage", "Enter the left margin in cm."))
        self.leftMarginSpinBox.setSuffix(_translate("PrinterPage", " cm"))
        self.rightMarginSpinBox.setToolTip(_translate("PrinterPage", "Enter the right margin in cm."))
        self.rightMarginSpinBox.setSuffix(_translate("PrinterPage", " cm"))
        self.bottomMarginSpinBox.setToolTip(_translate("PrinterPage", "Enter the bottom margin in cm."))
        self.bottomMarginSpinBox.setSuffix(_translate("PrinterPage", " cm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrinterPage = QtWidgets.QWidget()
    ui = Ui_PrinterPage()
    ui.setupUi(PrinterPage)
    PrinterPage.show()
    sys.exit(app.exec_())

