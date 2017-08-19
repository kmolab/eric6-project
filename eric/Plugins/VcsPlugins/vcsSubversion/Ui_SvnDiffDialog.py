# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsSubversion\SvnDiffDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SvnDiffDialog(object):
    def setupUi(self, SvnDiffDialog):
        SvnDiffDialog.setObjectName("SvnDiffDialog")
        SvnDiffDialog.resize(749, 646)
        self.vboxlayout = QtWidgets.QVBoxLayout(SvnDiffDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.contentsGroup = QtWidgets.QGroupBox(SvnDiffDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.contentsGroup.sizePolicy().hasHeightForWidth())
        self.contentsGroup.setSizePolicy(sizePolicy)
        self.contentsGroup.setObjectName("contentsGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.contentsGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filesCombo = QtWidgets.QComboBox(self.contentsGroup)
        self.filesCombo.setObjectName("filesCombo")
        self.verticalLayout.addWidget(self.filesCombo)
        self.searchWidget = E5TextEditSearchWidget(self.contentsGroup)
        self.searchWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.searchWidget.setObjectName("searchWidget")
        self.verticalLayout.addWidget(self.searchWidget)
        self.contents = QtWidgets.QTextEdit(self.contentsGroup)
        self.contents.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.contents.setReadOnly(True)
        self.contents.setTabStopWidth(8)
        self.contents.setAcceptRichText(False)
        self.contents.setObjectName("contents")
        self.verticalLayout.addWidget(self.contents)
        self.vboxlayout.addWidget(self.contentsGroup)
        self.errorGroup = QtWidgets.QGroupBox(SvnDiffDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout1.addWidget(self.errors)
        self.vboxlayout.addWidget(self.errorGroup)
        self.inputGroup = QtWidgets.QGroupBox(SvnDiffDialog)
        self.inputGroup.setObjectName("inputGroup")
        self.gridlayout = QtWidgets.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.vboxlayout.addWidget(self.inputGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(SvnDiffDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(SvnDiffDialog)
        self.buttonBox.rejected.connect(SvnDiffDialog.close)
        QtCore.QMetaObject.connectSlotsByName(SvnDiffDialog)
        SvnDiffDialog.setTabOrder(self.filesCombo, self.searchWidget)
        SvnDiffDialog.setTabOrder(self.searchWidget, self.contents)
        SvnDiffDialog.setTabOrder(self.contents, self.errors)
        SvnDiffDialog.setTabOrder(self.errors, self.input)
        SvnDiffDialog.setTabOrder(self.input, self.passwordCheckBox)
        SvnDiffDialog.setTabOrder(self.passwordCheckBox, self.sendButton)

    def retranslateUi(self, SvnDiffDialog):
        _translate = QtCore.QCoreApplication.translate
        SvnDiffDialog.setWindowTitle(_translate("SvnDiffDialog", "Subversion Diff"))
        self.contentsGroup.setTitle(_translate("SvnDiffDialog", "Difference"))
        self.contents.setWhatsThis(_translate("SvnDiffDialog", "<b>Subversion Diff</b><p>This shows the output of the svn diff command.</p>"))
        self.errorGroup.setTitle(_translate("SvnDiffDialog", "Errors"))
        self.inputGroup.setTitle(_translate("SvnDiffDialog", "Input"))
        self.sendButton.setToolTip(_translate("SvnDiffDialog", "Press to send the input to the subversion process"))
        self.sendButton.setText(_translate("SvnDiffDialog", "&Send"))
        self.sendButton.setShortcut(_translate("SvnDiffDialog", "Alt+S"))
        self.input.setToolTip(_translate("SvnDiffDialog", "Enter data to be sent to the subversion process"))
        self.passwordCheckBox.setToolTip(_translate("SvnDiffDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("SvnDiffDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("SvnDiffDialog", "Alt+P"))

from E5Gui.E5TextEditSearchWidget import E5TextEditSearchWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SvnDiffDialog = QtWidgets.QWidget()
    ui = Ui_SvnDiffDialog()
    ui.setupUi(SvnDiffDialog)
    SvnDiffDialog.show()
    sys.exit(app.exec_())

