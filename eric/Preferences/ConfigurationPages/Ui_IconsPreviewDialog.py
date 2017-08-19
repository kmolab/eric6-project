# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\IconsPreviewDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IconsPreviewDialog(object):
    def setupUi(self, IconsPreviewDialog):
        IconsPreviewDialog.setObjectName("IconsPreviewDialog")
        IconsPreviewDialog.resize(596, 541)
        IconsPreviewDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(IconsPreviewDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.iconView = QtWidgets.QListWidget(IconsPreviewDialog)
        self.iconView.setMovement(QtWidgets.QListView.Free)
        self.iconView.setFlow(QtWidgets.QListView.LeftToRight)
        self.iconView.setGridSize(QtCore.QSize(100, 50))
        self.iconView.setViewMode(QtWidgets.QListView.IconMode)
        self.iconView.setObjectName("iconView")
        self.vboxlayout.addWidget(self.iconView)
        self.buttonBox = QtWidgets.QDialogButtonBox(IconsPreviewDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(IconsPreviewDialog)
        self.buttonBox.accepted.connect(IconsPreviewDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(IconsPreviewDialog)

    def retranslateUi(self, IconsPreviewDialog):
        _translate = QtCore.QCoreApplication.translate
        IconsPreviewDialog.setWindowTitle(_translate("IconsPreviewDialog", "Icons Preview"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IconsPreviewDialog = QtWidgets.QDialog()
    ui = Ui_IconsPreviewDialog()
    ui.setupUi(IconsPreviewDialog)
    IconsPreviewDialog.show()
    sys.exit(app.exec_())

