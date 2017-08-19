# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\DiffDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DiffDialog(object):
    def setupUi(self, DiffDialog):
        DiffDialog.setObjectName("DiffDialog")
        DiffDialog.resize(750, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(DiffDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textLabel1 = QtWidgets.QLabel(DiffDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.horizontalLayout_2.addWidget(self.textLabel1)
        self.file1Picker = E5PathPicker(DiffDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file1Picker.sizePolicy().hasHeightForWidth())
        self.file1Picker.setSizePolicy(sizePolicy)
        self.file1Picker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.file1Picker.setObjectName("file1Picker")
        self.horizontalLayout_2.addWidget(self.file1Picker)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textLabel2 = QtWidgets.QLabel(DiffDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.horizontalLayout.addWidget(self.textLabel2)
        self.file2Picker = E5PathPicker(DiffDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file2Picker.sizePolicy().hasHeightForWidth())
        self.file2Picker.setSizePolicy(sizePolicy)
        self.file2Picker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.file2Picker.setObjectName("file2Picker")
        self.horizontalLayout.addWidget(self.file2Picker)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.diffFormatGroup = QtWidgets.QGroupBox(DiffDialog)
        self.diffFormatGroup.setObjectName("diffFormatGroup")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.diffFormatGroup)
        self.hboxlayout.setObjectName("hboxlayout")
        self.unifiedRadioButton = QtWidgets.QRadioButton(self.diffFormatGroup)
        self.unifiedRadioButton.setChecked(True)
        self.unifiedRadioButton.setObjectName("unifiedRadioButton")
        self.hboxlayout.addWidget(self.unifiedRadioButton)
        self.contextRadioButton = QtWidgets.QRadioButton(self.diffFormatGroup)
        self.contextRadioButton.setObjectName("contextRadioButton")
        self.hboxlayout.addWidget(self.contextRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.diffFormatGroup)
        self.searchWidget = E5TextEditSearchWidget(DiffDialog)
        self.searchWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.searchWidget.setObjectName("searchWidget")
        self.verticalLayout.addWidget(self.searchWidget)
        self.contents = QtWidgets.QTextEdit(DiffDialog)
        self.contents.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.contents.setReadOnly(True)
        self.contents.setTabStopWidth(8)
        self.contents.setAcceptRichText(False)
        self.contents.setObjectName("contents")
        self.verticalLayout.addWidget(self.contents)
        self.buttonBox = QtWidgets.QDialogButtonBox(DiffDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.file1Picker)
        self.textLabel2.setBuddy(self.file2Picker)

        self.retranslateUi(DiffDialog)
        self.buttonBox.rejected.connect(DiffDialog.close)
        QtCore.QMetaObject.connectSlotsByName(DiffDialog)
        DiffDialog.setTabOrder(self.file1Picker, self.file2Picker)
        DiffDialog.setTabOrder(self.file2Picker, self.unifiedRadioButton)
        DiffDialog.setTabOrder(self.unifiedRadioButton, self.contextRadioButton)
        DiffDialog.setTabOrder(self.contextRadioButton, self.searchWidget)
        DiffDialog.setTabOrder(self.searchWidget, self.contents)

    def retranslateUi(self, DiffDialog):
        _translate = QtCore.QCoreApplication.translate
        DiffDialog.setWindowTitle(_translate("DiffDialog", "File Differences"))
        self.textLabel1.setText(_translate("DiffDialog", "File &1:"))
        self.file1Picker.setToolTip(_translate("DiffDialog", "Enter the name of the first file"))
        self.textLabel2.setText(_translate("DiffDialog", "File &2:"))
        self.file2Picker.setToolTip(_translate("DiffDialog", "Enter the name of the second file"))
        self.diffFormatGroup.setTitle(_translate("DiffDialog", "Select Diff Kind"))
        self.unifiedRadioButton.setToolTip(_translate("DiffDialog", "Select to generate a unified diff"))
        self.unifiedRadioButton.setText(_translate("DiffDialog", "&Unified Diff"))
        self.unifiedRadioButton.setShortcut(_translate("DiffDialog", "Alt+U"))
        self.contextRadioButton.setToolTip(_translate("DiffDialog", "Select to generate a context diff"))
        self.contextRadioButton.setText(_translate("DiffDialog", "Co&ntext Diff"))
        self.contextRadioButton.setShortcut(_translate("DiffDialog", "Alt+N"))

from E5Gui.E5PathPicker import E5PathPicker
from E5Gui.E5TextEditSearchWidget import E5TextEditSearchWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiffDialog = QtWidgets.QWidget()
    ui = Ui_DiffDialog()
    ui.setupUi(DiffDialog)
    DiffDialog.show()
    sys.exit(app.exec_())

