# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Templates\TemplatePropertiesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TemplatePropertiesDialog(object):
    def setupUi(self, TemplatePropertiesDialog):
        TemplatePropertiesDialog.setObjectName("TemplatePropertiesDialog")
        TemplatePropertiesDialog.resize(448, 323)
        TemplatePropertiesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(TemplatePropertiesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textLabel1 = QtWidgets.QLabel(TemplatePropertiesDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.gridLayout.addWidget(self.textLabel1, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(TemplatePropertiesDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.descriptionLabel = QtWidgets.QLabel(TemplatePropertiesDialog)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 1, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QLineEdit(TemplatePropertiesDialog)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.groupLabel = QtWidgets.QLabel(TemplatePropertiesDialog)
        self.groupLabel.setObjectName("groupLabel")
        self.gridLayout.addWidget(self.groupLabel, 2, 0, 1, 1)
        self.groupCombo = QtWidgets.QComboBox(TemplatePropertiesDialog)
        self.groupCombo.setToolTip("")
        self.groupCombo.setObjectName("groupCombo")
        self.gridLayout.addWidget(self.groupCombo, 2, 1, 1, 1)
        self.templateLabel = QtWidgets.QLabel(TemplatePropertiesDialog)
        self.templateLabel.setAlignment(QtCore.Qt.AlignTop)
        self.templateLabel.setObjectName("templateLabel")
        self.gridLayout.addWidget(self.templateLabel, 3, 0, 1, 1)
        self.templateEdit = QtWidgets.QTextEdit(TemplatePropertiesDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.templateEdit.setFont(font)
        self.templateEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.templateEdit.setAcceptRichText(False)
        self.templateEdit.setObjectName("templateEdit")
        self.gridLayout.addWidget(self.templateEdit, 3, 1, 3, 1)
        self.helpButton = QtWidgets.QPushButton(TemplatePropertiesDialog)
        self.helpButton.setObjectName("helpButton")
        self.gridLayout.addWidget(self.helpButton, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(84, 98, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(TemplatePropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(TemplatePropertiesDialog)
        self.buttonBox.rejected.connect(TemplatePropertiesDialog.reject)
        self.buttonBox.accepted.connect(TemplatePropertiesDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(TemplatePropertiesDialog)
        TemplatePropertiesDialog.setTabOrder(self.nameEdit, self.descriptionEdit)
        TemplatePropertiesDialog.setTabOrder(self.descriptionEdit, self.groupCombo)
        TemplatePropertiesDialog.setTabOrder(self.groupCombo, self.templateEdit)
        TemplatePropertiesDialog.setTabOrder(self.templateEdit, self.helpButton)
        TemplatePropertiesDialog.setTabOrder(self.helpButton, self.buttonBox)

    def retranslateUi(self, TemplatePropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        TemplatePropertiesDialog.setWindowTitle(_translate("TemplatePropertiesDialog", "Template Properties"))
        self.textLabel1.setText(_translate("TemplatePropertiesDialog", "Name:"))
        self.nameEdit.setToolTip(_translate("TemplatePropertiesDialog", "Enter the name of the template/group. Templates are autocompleted upon this name."))
        self.descriptionLabel.setText(_translate("TemplatePropertiesDialog", "Description:"))
        self.descriptionEdit.setToolTip(_translate("TemplatePropertiesDialog", "Enter a description for the template"))
        self.groupLabel.setText(_translate("TemplatePropertiesDialog", "Group:"))
        self.templateLabel.setText(_translate("TemplatePropertiesDialog", "Template:"))
        self.templateEdit.setToolTip(_translate("TemplatePropertiesDialog", "Enter the text of the template"))
        self.templateEdit.setWhatsThis(_translate("TemplatePropertiesDialog", "<b>Template Text</b>\n"
"<p>Enter the template text in this area. Every occurrence of $VAR$ will be replaced\n"
"by the associated text when the template is applied.  Predefined variables may be used in the template. The separator character might\n"
"be changed via the preferences dialog.</p>\n"
"<p>Press the help button for more information.</p>"))
        self.helpButton.setText(_translate("TemplatePropertiesDialog", "&Help"))
        self.helpButton.setShortcut(_translate("TemplatePropertiesDialog", "Alt+H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TemplatePropertiesDialog = QtWidgets.QDialog()
    ui = Ui_TemplatePropertiesDialog()
    ui.setupUi(TemplatePropertiesDialog)
    TemplatePropertiesDialog.show()
    sys.exit(app.exec_())

