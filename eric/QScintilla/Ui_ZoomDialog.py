# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\QScintilla\ZoomDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZoomDialog(object):
    def setupUi(self, ZoomDialog):
        ZoomDialog.setObjectName("ZoomDialog")
        ZoomDialog.resize(206, 77)
        self.vboxlayout = QtWidgets.QVBoxLayout(ZoomDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.zoomLabel = QtWidgets.QLabel(ZoomDialog)
        self.zoomLabel.setObjectName("zoomLabel")
        self.hboxlayout.addWidget(self.zoomLabel)
        self.zoomSpinBox = QtWidgets.QSpinBox(ZoomDialog)
        self.zoomSpinBox.setAlignment(QtCore.Qt.AlignRight)
        self.zoomSpinBox.setMinimum(-10)
        self.zoomSpinBox.setMaximum(20)
        self.zoomSpinBox.setProperty("value", 0)
        self.zoomSpinBox.setObjectName("zoomSpinBox")
        self.hboxlayout.addWidget(self.zoomSpinBox)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ZoomDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.zoomLabel.setBuddy(self.zoomSpinBox)

        self.retranslateUi(ZoomDialog)
        self.buttonBox.accepted.connect(ZoomDialog.accept)
        self.buttonBox.rejected.connect(ZoomDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ZoomDialog)

    def retranslateUi(self, ZoomDialog):
        _translate = QtCore.QCoreApplication.translate
        ZoomDialog.setWindowTitle(_translate("ZoomDialog", "Zoom"))
        self.zoomLabel.setText(_translate("ZoomDialog", "Zoom &Factor:"))
        self.zoomSpinBox.setToolTip(_translate("ZoomDialog", "Enter zoom factor"))
        self.zoomSpinBox.setWhatsThis(_translate("ZoomDialog", "<b>Zoom Factor</b>\n"
"<p>Enter the desired zoom factor here. The zoom factor\n"
"may be between -10 and +20 and is the increment that is \n"
"added to the size of the fonts used in the editor windows.</p>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ZoomDialog = QtWidgets.QDialog()
    ui = Ui_ZoomDialog()
    ui.setupUi(ZoomDialog)
    ZoomDialog.show()
    sys.exit(app.exec_())

