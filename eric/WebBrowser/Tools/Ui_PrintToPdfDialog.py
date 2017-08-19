# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\Tools\PrintToPdfDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrintToPdfDialog(object):
    def setupUi(self, PrintToPdfDialog):
        PrintToPdfDialog.setObjectName("PrintToPdfDialog")
        PrintToPdfDialog.resize(600, 105)
        PrintToPdfDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PrintToPdfDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(PrintToPdfDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pdfFilePicker = E5PathPicker(PrintToPdfDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfFilePicker.sizePolicy().hasHeightForWidth())
        self.pdfFilePicker.setSizePolicy(sizePolicy)
        self.pdfFilePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pdfFilePicker.setObjectName("pdfFilePicker")
        self.gridLayout.addWidget(self.pdfFilePicker, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(PrintToPdfDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pageLayoutLabel = QtWidgets.QLabel(PrintToPdfDialog)
        self.pageLayoutLabel.setText("")
        self.pageLayoutLabel.setObjectName("pageLayoutLabel")
        self.horizontalLayout.addWidget(self.pageLayoutLabel)
        self.pageLayoutButton = QtWidgets.QToolButton(PrintToPdfDialog)
        self.pageLayoutButton.setObjectName("pageLayoutButton")
        self.horizontalLayout.addWidget(self.pageLayoutButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(PrintToPdfDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PrintToPdfDialog)
        self.buttonBox.accepted.connect(PrintToPdfDialog.accept)
        self.buttonBox.rejected.connect(PrintToPdfDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PrintToPdfDialog)

    def retranslateUi(self, PrintToPdfDialog):
        _translate = QtCore.QCoreApplication.translate
        PrintToPdfDialog.setWindowTitle(_translate("PrintToPdfDialog", "Print to PDF"))
        self.label.setText(_translate("PrintToPdfDialog", "Save as:"))
        self.pdfFilePicker.setToolTip(_translate("PrintToPdfDialog", "Enter the file name of the PDF document"))
        self.label_2.setText(_translate("PrintToPdfDialog", "Page Layout:"))
        self.pageLayoutButton.setToolTip(_translate("PrintToPdfDialog", "Select the page layout via a dialog"))
        self.pageLayoutButton.setText(_translate("PrintToPdfDialog", "..."))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrintToPdfDialog = QtWidgets.QDialog()
    ui = Ui_PrintToPdfDialog()
    ui.setupUi(PrintToPdfDialog)
    PrintToPdfDialog.show()
    sys.exit(app.exec_())

