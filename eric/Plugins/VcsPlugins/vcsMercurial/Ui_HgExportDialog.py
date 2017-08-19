# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgExportDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgExportDialog(object):
    def setupUi(self, HgExportDialog):
        HgExportDialog.setObjectName("HgExportDialog")
        HgExportDialog.resize(450, 350)
        HgExportDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HgExportDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(HgExportDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.directoryPicker = E5PathPicker(HgExportDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directoryPicker.sizePolicy().hasHeightForWidth())
        self.directoryPicker.setSizePolicy(sizePolicy)
        self.directoryPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.directoryPicker.setObjectName("directoryPicker")
        self.gridLayout.addWidget(self.directoryPicker, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(HgExportDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.patternEdit = QtWidgets.QLineEdit(HgExportDialog)
        self.patternEdit.setObjectName("patternEdit")
        self.gridLayout.addWidget(self.patternEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(HgExportDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.changesetsEdit = QtWidgets.QPlainTextEdit(HgExportDialog)
        self.changesetsEdit.setTabChangesFocus(True)
        self.changesetsEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.changesetsEdit.setObjectName("changesetsEdit")
        self.gridLayout.addWidget(self.changesetsEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.switchParentCheckBox = QtWidgets.QCheckBox(HgExportDialog)
        self.switchParentCheckBox.setToolTip("")
        self.switchParentCheckBox.setObjectName("switchParentCheckBox")
        self.verticalLayout.addWidget(self.switchParentCheckBox)
        self.textCheckBox = QtWidgets.QCheckBox(HgExportDialog)
        self.textCheckBox.setToolTip("")
        self.textCheckBox.setObjectName("textCheckBox")
        self.verticalLayout.addWidget(self.textCheckBox)
        self.datesCheckBox = QtWidgets.QCheckBox(HgExportDialog)
        self.datesCheckBox.setObjectName("datesCheckBox")
        self.verticalLayout.addWidget(self.datesCheckBox)
        self.gitCheckBox = QtWidgets.QCheckBox(HgExportDialog)
        self.gitCheckBox.setObjectName("gitCheckBox")
        self.verticalLayout.addWidget(self.gitCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgExportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(HgExportDialog)
        self.buttonBox.accepted.connect(HgExportDialog.accept)
        self.buttonBox.rejected.connect(HgExportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HgExportDialog)
        HgExportDialog.setTabOrder(self.directoryPicker, self.patternEdit)
        HgExportDialog.setTabOrder(self.patternEdit, self.changesetsEdit)
        HgExportDialog.setTabOrder(self.changesetsEdit, self.switchParentCheckBox)
        HgExportDialog.setTabOrder(self.switchParentCheckBox, self.textCheckBox)
        HgExportDialog.setTabOrder(self.textCheckBox, self.datesCheckBox)
        HgExportDialog.setTabOrder(self.datesCheckBox, self.gitCheckBox)

    def retranslateUi(self, HgExportDialog):
        _translate = QtCore.QCoreApplication.translate
        HgExportDialog.setWindowTitle(_translate("HgExportDialog", "Export Patches"))
        self.label.setText(_translate("HgExportDialog", "Export Directory:"))
        self.directoryPicker.setToolTip(_translate("HgExportDialog", "Enter the target name"))
        self.directoryPicker.setWhatsThis(_translate("HgExportDialog", "<b>Target name</b>\n"
"<p>Enter the new name in this field. The target must be the new name or an absolute path.</p>"))
        self.label_2.setText(_translate("HgExportDialog", "File Name Pattern:"))
        self.patternEdit.setToolTip(_translate("HgExportDialog", "Enter the file name pattern for the export files"))
        self.patternEdit.setWhatsThis(_translate("HgExportDialog", "<b>File Name Pattern</b>\n"
"<p>Enter the file name pattern to be used to generate the export files\n"
"here. Valid recognized patterns are:</p>\n"
"<table>\n"
"<tr><td>%%</td><td>literal \"%\" character</td></tr>\n"
"<tr><td>%H</td><td>changeset hash (40 hexadecimal digits)</td></tr>\n"
"<tr><td>%N</td><td>number of patches being generated</td></tr>\n"
"<tr><td>%R</td><td>changeset revision number</td></tr>\n"
"<tr><td>%b</td><td>basename of the exporting repository</td></tr>\n"
"<tr><td>%h</td><td>short-form changeset hash (12 hexadecimal digits)</td></tr>\n"
"<tr><td>%n</td><td>zero-padded sequence number, starting at 1</td></tr>\n"
"<tr><td>%r</td><td>zero-padded changeset revision number</td></tr>\n"
"</table>    \n"
""))
        self.label_3.setText(_translate("HgExportDialog", "Changesets:"))
        self.changesetsEdit.setToolTip(_translate("HgExportDialog", "Enter changesets by number, id, range or revset expression one per line"))
        self.switchParentCheckBox.setText(_translate("HgExportDialog", "Compare Against Second Parent"))
        self.textCheckBox.setText(_translate("HgExportDialog", "Treat all Files as Text"))
        self.datesCheckBox.setText(_translate("HgExportDialog", "Omit Dates"))
        self.gitCheckBox.setText(_translate("HgExportDialog", "Use Git extended Diff-Format"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgExportDialog = QtWidgets.QDialog()
    ui = Ui_HgExportDialog()
    ui.setupUi(HgExportDialog)
    HgExportDialog.show()
    sys.exit(app.exec_())

