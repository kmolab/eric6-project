# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\HexEdit\HexEditGotoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HexEditGotoWidget(object):
    def setupUi(self, HexEditGotoWidget):
        HexEditGotoWidget.setObjectName("HexEditGotoWidget")
        HexEditGotoWidget.resize(600, 54)
        self.gridLayout = QtWidgets.QGridLayout(HexEditGotoWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.closeButton = QtWidgets.QToolButton(HexEditGotoWidget)
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(HexEditGotoWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.formatCombo = QtWidgets.QComboBox(HexEditGotoWidget)
        self.formatCombo.setObjectName("formatCombo")
        self.gridLayout.addWidget(self.formatCombo, 0, 2, 1, 1)
        self.offsetEdit = QtWidgets.QLineEdit(HexEditGotoWidget)
        self.offsetEdit.setObjectName("offsetEdit")
        self.gridLayout.addWidget(self.offsetEdit, 0, 3, 1, 1)
        self.cursorCheckBox = QtWidgets.QCheckBox(HexEditGotoWidget)
        self.cursorCheckBox.setObjectName("cursorCheckBox")
        self.gridLayout.addWidget(self.cursorCheckBox, 0, 4, 1, 1)
        self.backCheckBox = QtWidgets.QCheckBox(HexEditGotoWidget)
        self.backCheckBox.setObjectName("backCheckBox")
        self.gridLayout.addWidget(self.backCheckBox, 0, 5, 1, 1)
        self.gotoButton = QtWidgets.QPushButton(HexEditGotoWidget)
        self.gotoButton.setEnabled(False)
        self.gotoButton.setObjectName("gotoButton")
        self.gridLayout.addWidget(self.gotoButton, 0, 6, 1, 1)
        self.selectionCheckBox = QtWidgets.QCheckBox(HexEditGotoWidget)
        self.selectionCheckBox.setObjectName("selectionCheckBox")
        self.gridLayout.addWidget(self.selectionCheckBox, 1, 4, 1, 2)

        self.retranslateUi(HexEditGotoWidget)
        self.offsetEdit.returnPressed.connect(self.gotoButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(HexEditGotoWidget)
        HexEditGotoWidget.setTabOrder(self.formatCombo, self.offsetEdit)
        HexEditGotoWidget.setTabOrder(self.offsetEdit, self.cursorCheckBox)
        HexEditGotoWidget.setTabOrder(self.cursorCheckBox, self.backCheckBox)
        HexEditGotoWidget.setTabOrder(self.backCheckBox, self.selectionCheckBox)
        HexEditGotoWidget.setTabOrder(self.selectionCheckBox, self.gotoButton)
        HexEditGotoWidget.setTabOrder(self.gotoButton, self.closeButton)

    def retranslateUi(self, HexEditGotoWidget):
        _translate = QtCore.QCoreApplication.translate
        HexEditGotoWidget.setWindowTitle(_translate("HexEditGotoWidget", "Go to"))
        self.closeButton.setToolTip(_translate("HexEditGotoWidget", "Press to close the window"))
        self.label.setText(_translate("HexEditGotoWidget", "Offset:"))
        self.formatCombo.setToolTip(_translate("HexEditGotoWidget", "Select the data format of the offset field"))
        self.offsetEdit.setToolTip(_translate("HexEditGotoWidget", "Enter the address to move to or the offset from the cursor position"))
        self.cursorCheckBox.setToolTip(_translate("HexEditGotoWidget", "Select to move relative to the cursor"))
        self.cursorCheckBox.setText(_translate("HexEditGotoWidget", "From Cursor"))
        self.backCheckBox.setToolTip(_translate("HexEditGotoWidget", "Select to move backwards"))
        self.backCheckBox.setText(_translate("HexEditGotoWidget", "Backwards"))
        self.gotoButton.setToolTip(_translate("HexEditGotoWidget", "Press to move the cursor"))
        self.gotoButton.setText(_translate("HexEditGotoWidget", "> Goto"))
        self.selectionCheckBox.setToolTip(_translate("HexEditGotoWidget", "Select to also extend the selection"))
        self.selectionCheckBox.setText(_translate("HexEditGotoWidget", "Extend Selection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HexEditGotoWidget = QtWidgets.QWidget()
    ui = Ui_HexEditGotoWidget()
    ui.setupUi(HexEditGotoWidget)
    HexEditGotoWidget.show()
    sys.exit(app.exec_())

