# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\DiffColoursPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DiffColoursPage(object):
    def setupUi(self, DiffColoursPage):
        DiffColoursPage.setObjectName("DiffColoursPage")
        DiffColoursPage.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DiffColoursPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(DiffColoursPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line1 = QtWidgets.QFrame(DiffColoursPage)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setObjectName("line1")
        self.verticalLayout.addWidget(self.line1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.headerButton = QtWidgets.QPushButton(DiffColoursPage)
        self.headerButton.setObjectName("headerButton")
        self.gridLayout.addWidget(self.headerButton, 5, 0, 1, 1)
        self.headerSample = QtWidgets.QLineEdit(DiffColoursPage)
        self.headerSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.headerSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.headerSample.setReadOnly(True)
        self.headerSample.setObjectName("headerSample")
        self.gridLayout.addWidget(self.headerSample, 5, 1, 1, 1)
        self.whitespaceButton = QtWidgets.QPushButton(DiffColoursPage)
        self.whitespaceButton.setObjectName("whitespaceButton")
        self.gridLayout.addWidget(self.whitespaceButton, 6, 0, 1, 1)
        self.whitespaceSample = QtWidgets.QLineEdit(DiffColoursPage)
        self.whitespaceSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.whitespaceSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.whitespaceSample.setReadOnly(True)
        self.whitespaceSample.setObjectName("whitespaceSample")
        self.gridLayout.addWidget(self.whitespaceSample, 6, 1, 1, 1)
        self.textButton = QtWidgets.QPushButton(DiffColoursPage)
        self.textButton.setObjectName("textButton")
        self.gridLayout.addWidget(self.textButton, 0, 0, 1, 1)
        self.textSample = QtWidgets.QLineEdit(DiffColoursPage)
        self.textSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.textSample.setReadOnly(True)
        self.textSample.setObjectName("textSample")
        self.gridLayout.addWidget(self.textSample, 0, 1, 1, 1)
        self.addedButton = QtWidgets.QPushButton(DiffColoursPage)
        self.addedButton.setObjectName("addedButton")
        self.gridLayout.addWidget(self.addedButton, 1, 0, 1, 1)
        self.addedSample = QtWidgets.QLineEdit(DiffColoursPage)
        self.addedSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addedSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.addedSample.setReadOnly(True)
        self.addedSample.setObjectName("addedSample")
        self.gridLayout.addWidget(self.addedSample, 1, 1, 1, 1)
        self.removedButton = QtWidgets.QPushButton(DiffColoursPage)
        self.removedButton.setObjectName("removedButton")
        self.gridLayout.addWidget(self.removedButton, 2, 0, 1, 1)
        self.removedSample = QtWidgets.QLineEdit(DiffColoursPage)
        self.removedSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.removedSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.removedSample.setReadOnly(True)
        self.removedSample.setObjectName("removedSample")
        self.gridLayout.addWidget(self.removedSample, 2, 1, 1, 1)
        self.replacedButton = QtWidgets.QPushButton(DiffColoursPage)
        self.replacedButton.setObjectName("replacedButton")
        self.gridLayout.addWidget(self.replacedButton, 3, 0, 1, 1)
        self.replacedSample = QtWidgets.QLineEdit(DiffColoursPage)
        self.replacedSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.replacedSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.replacedSample.setReadOnly(True)
        self.replacedSample.setObjectName("replacedSample")
        self.gridLayout.addWidget(self.replacedSample, 3, 1, 1, 1)
        self.contextButton = QtWidgets.QPushButton(DiffColoursPage)
        self.contextButton.setObjectName("contextButton")
        self.gridLayout.addWidget(self.contextButton, 4, 0, 1, 1)
        self.contextSample = QtWidgets.QLineEdit(DiffColoursPage)
        self.contextSample.setFocusPolicy(QtCore.Qt.NoFocus)
        self.contextSample.setAlignment(QtCore.Qt.AlignHCenter)
        self.contextSample.setReadOnly(True)
        self.contextSample.setObjectName("contextSample")
        self.gridLayout.addWidget(self.contextSample, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 46, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(DiffColoursPage)
        QtCore.QMetaObject.connectSlotsByName(DiffColoursPage)

    def retranslateUi(self, DiffColoursPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("DiffColoursPage", "<b>Configure Diff colours</b>"))
        self.headerButton.setToolTip(_translate("DiffColoursPage", "Select the background colour for header lines"))
        self.headerButton.setText(_translate("DiffColoursPage", "Header Colour"))
        self.headerSample.setText(_translate("DiffColoursPage", "Header Line"))
        self.whitespaceButton.setToolTip(_translate("DiffColoursPage", "Select the background colour for bad whitespace"))
        self.whitespaceButton.setText(_translate("DiffColoursPage", "Whitespace Colour"))
        self.textButton.setToolTip(_translate("DiffColoursPage", "Select the text foreground colour"))
        self.textButton.setText(_translate("DiffColoursPage", "Text Colour"))
        self.textSample.setText(_translate("DiffColoursPage", "Normal Text"))
        self.addedButton.setToolTip(_translate("DiffColoursPage", "Select the background colour for additions"))
        self.addedButton.setText(_translate("DiffColoursPage", "Added Colour"))
        self.addedSample.setText(_translate("DiffColoursPage", "Added Text"))
        self.removedButton.setToolTip(_translate("DiffColoursPage", "Select the background colour for removed text"))
        self.removedButton.setText(_translate("DiffColoursPage", "Removed Colour"))
        self.removedSample.setText(_translate("DiffColoursPage", "Removed Text"))
        self.replacedButton.setToolTip(_translate("DiffColoursPage", "Select the background colour for replaced text"))
        self.replacedButton.setText(_translate("DiffColoursPage", "Replaced Colour"))
        self.replacedSample.setText(_translate("DiffColoursPage", "Replaced Text"))
        self.contextButton.setToolTip(_translate("DiffColoursPage", "Select the background colour for context lines"))
        self.contextButton.setText(_translate("DiffColoursPage", "Context Colour"))
        self.contextSample.setText(_translate("DiffColoursPage", "Context Line"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiffColoursPage = QtWidgets.QWidget()
    ui = Ui_DiffColoursPage()
    ui.setupUi(DiffColoursPage)
    DiffColoursPage.show()
    sys.exit(app.exec_())

