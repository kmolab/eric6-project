# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\WizardPlugins\MessageBoxWizard\MessageBoxWizardDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessageBoxWizardDialog(object):
    def setupUi(self, MessageBoxWizardDialog):
        MessageBoxWizardDialog.setObjectName("MessageBoxWizardDialog")
        MessageBoxWizardDialog.resize(535, 522)
        MessageBoxWizardDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(MessageBoxWizardDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(MessageBoxWizardDialog)
        self.groupBox.setObjectName("groupBox")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName("hboxlayout")
        self.rInformation = QtWidgets.QRadioButton(self.groupBox)
        self.rInformation.setChecked(True)
        self.rInformation.setObjectName("rInformation")
        self.hboxlayout.addWidget(self.rInformation)
        self.rQuestion = QtWidgets.QRadioButton(self.groupBox)
        self.rQuestion.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rQuestion.setObjectName("rQuestion")
        self.hboxlayout.addWidget(self.rQuestion)
        self.rWarning = QtWidgets.QRadioButton(self.groupBox)
        self.rWarning.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rWarning.setObjectName("rWarning")
        self.hboxlayout.addWidget(self.rWarning)
        self.rCritical = QtWidgets.QRadioButton(self.groupBox)
        self.rCritical.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rCritical.setObjectName("rCritical")
        self.hboxlayout.addWidget(self.rCritical)
        self.rAbout = QtWidgets.QRadioButton(self.groupBox)
        self.rAbout.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rAbout.setObjectName("rAbout")
        self.hboxlayout.addWidget(self.rAbout)
        self.rAboutQt = QtWidgets.QRadioButton(self.groupBox)
        self.rAboutQt.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rAboutQt.setObjectName("rAboutQt")
        self.hboxlayout.addWidget(self.rAboutQt)
        self.verticalLayout.addWidget(self.groupBox)
        self.lResultVar = QtWidgets.QLabel(MessageBoxWizardDialog)
        self.lResultVar.setObjectName("lResultVar")
        self.verticalLayout.addWidget(self.lResultVar)
        self.eResultVar = QtWidgets.QLineEdit(MessageBoxWizardDialog)
        self.eResultVar.setObjectName("eResultVar")
        self.verticalLayout.addWidget(self.eResultVar)
        self.textLabel1 = QtWidgets.QLabel(MessageBoxWizardDialog)
        self.textLabel1.setObjectName("textLabel1")
        self.verticalLayout.addWidget(self.textLabel1)
        self.eCaption = QtWidgets.QLineEdit(MessageBoxWizardDialog)
        self.eCaption.setObjectName("eCaption")
        self.verticalLayout.addWidget(self.eCaption)
        self.textLabel2 = QtWidgets.QLabel(MessageBoxWizardDialog)
        self.textLabel2.setObjectName("textLabel2")
        self.verticalLayout.addWidget(self.textLabel2)
        self.eMessage = QtWidgets.QTextEdit(MessageBoxWizardDialog)
        self.eMessage.setTabChangesFocus(True)
        self.eMessage.setObjectName("eMessage")
        self.verticalLayout.addWidget(self.eMessage)
        self.parentGroup = QtWidgets.QGroupBox(MessageBoxWizardDialog)
        self.parentGroup.setObjectName("parentGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.parentGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.parentSelf = QtWidgets.QRadioButton(self.parentGroup)
        self.parentSelf.setChecked(True)
        self.parentSelf.setObjectName("parentSelf")
        self.gridLayout_3.addWidget(self.parentSelf, 0, 0, 1, 1)
        self.parentNone = QtWidgets.QRadioButton(self.parentGroup)
        self.parentNone.setObjectName("parentNone")
        self.gridLayout_3.addWidget(self.parentNone, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.parentOther = QtWidgets.QRadioButton(self.parentGroup)
        self.parentOther.setObjectName("parentOther")
        self.horizontalLayout_2.addWidget(self.parentOther)
        self.parentEdit = QtWidgets.QLineEdit(self.parentGroup)
        self.parentEdit.setEnabled(False)
        self.parentEdit.setObjectName("parentEdit")
        self.horizontalLayout_2.addWidget(self.parentEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.parentGroup)
        self.standardButtons = QtWidgets.QGroupBox(MessageBoxWizardDialog)
        self.standardButtons.setObjectName("standardButtons")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.standardButtons)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.applyCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.applyCheck.setObjectName("applyCheck")
        self.gridlayout.addWidget(self.applyCheck, 0, 1, 1, 1)
        self.abortCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.abortCheck.setObjectName("abortCheck")
        self.gridlayout.addWidget(self.abortCheck, 0, 0, 1, 1)
        self.cancelCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.cancelCheck.setObjectName("cancelCheck")
        self.gridlayout.addWidget(self.cancelCheck, 0, 2, 1, 1)
        self.ignoreCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.ignoreCheck.setObjectName("ignoreCheck")
        self.gridlayout.addWidget(self.ignoreCheck, 1, 1, 1, 1)
        self.saveallCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.saveallCheck.setObjectName("saveallCheck")
        self.gridlayout.addWidget(self.saveallCheck, 3, 0, 1, 1)
        self.saveCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.saveCheck.setObjectName("saveCheck")
        self.gridlayout.addWidget(self.saveCheck, 2, 4, 1, 1)
        self.discardCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.discardCheck.setObjectName("discardCheck")
        self.gridlayout.addWidget(self.discardCheck, 0, 4, 1, 1)
        self.yestoallCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.yestoallCheck.setObjectName("yestoallCheck")
        self.gridlayout.addWidget(self.yestoallCheck, 3, 2, 1, 1)
        self.openCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.openCheck.setObjectName("openCheck")
        self.gridlayout.addWidget(self.openCheck, 2, 0, 1, 1)
        self.resetCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.resetCheck.setObjectName("resetCheck")
        self.gridlayout.addWidget(self.resetCheck, 2, 1, 1, 1)
        self.okCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.okCheck.setObjectName("okCheck")
        self.gridlayout.addWidget(self.okCheck, 1, 4, 1, 1)
        self.noCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.noCheck.setObjectName("noCheck")
        self.gridlayout.addWidget(self.noCheck, 1, 2, 1, 1)
        self.helpCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.helpCheck.setObjectName("helpCheck")
        self.gridlayout.addWidget(self.helpCheck, 1, 0, 1, 1)
        self.notoallCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.notoallCheck.setObjectName("notoallCheck")
        self.gridlayout.addWidget(self.notoallCheck, 1, 3, 1, 1)
        self.retryCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.retryCheck.setObjectName("retryCheck")
        self.gridlayout.addWidget(self.retryCheck, 2, 3, 1, 1)
        self.restoreCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.restoreCheck.setObjectName("restoreCheck")
        self.gridlayout.addWidget(self.restoreCheck, 2, 2, 1, 1)
        self.yesCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.yesCheck.setObjectName("yesCheck")
        self.gridlayout.addWidget(self.yesCheck, 3, 1, 1, 1)
        self.closeCheck = QtWidgets.QCheckBox(self.standardButtons)
        self.closeCheck.setObjectName("closeCheck")
        self.gridlayout.addWidget(self.closeCheck, 0, 3, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.TextLabel1_2 = QtWidgets.QLabel(self.standardButtons)
        self.TextLabel1_2.setObjectName("TextLabel1_2")
        self.hboxlayout1.addWidget(self.TextLabel1_2)
        self.defaultCombo = QtWidgets.QComboBox(self.standardButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.defaultCombo.sizePolicy().hasHeightForWidth())
        self.defaultCombo.setSizePolicy(sizePolicy)
        self.defaultCombo.setObjectName("defaultCombo")
        self.hboxlayout1.addWidget(self.defaultCombo)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.verticalLayout.addWidget(self.standardButtons)
        self.buttonBox = QtWidgets.QDialogButtonBox(MessageBoxWizardDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MessageBoxWizardDialog)
        self.buttonBox.accepted.connect(MessageBoxWizardDialog.accept)
        self.buttonBox.rejected.connect(MessageBoxWizardDialog.reject)
        self.parentOther.toggled['bool'].connect(self.parentEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MessageBoxWizardDialog)
        MessageBoxWizardDialog.setTabOrder(self.rInformation, self.rQuestion)
        MessageBoxWizardDialog.setTabOrder(self.rQuestion, self.rWarning)
        MessageBoxWizardDialog.setTabOrder(self.rWarning, self.rCritical)
        MessageBoxWizardDialog.setTabOrder(self.rCritical, self.rAbout)
        MessageBoxWizardDialog.setTabOrder(self.rAbout, self.rAboutQt)
        MessageBoxWizardDialog.setTabOrder(self.rAboutQt, self.eResultVar)
        MessageBoxWizardDialog.setTabOrder(self.eResultVar, self.eCaption)
        MessageBoxWizardDialog.setTabOrder(self.eCaption, self.eMessage)
        MessageBoxWizardDialog.setTabOrder(self.eMessage, self.parentSelf)
        MessageBoxWizardDialog.setTabOrder(self.parentSelf, self.parentNone)
        MessageBoxWizardDialog.setTabOrder(self.parentNone, self.parentOther)
        MessageBoxWizardDialog.setTabOrder(self.parentOther, self.parentEdit)
        MessageBoxWizardDialog.setTabOrder(self.parentEdit, self.abortCheck)
        MessageBoxWizardDialog.setTabOrder(self.abortCheck, self.applyCheck)
        MessageBoxWizardDialog.setTabOrder(self.applyCheck, self.cancelCheck)
        MessageBoxWizardDialog.setTabOrder(self.cancelCheck, self.closeCheck)
        MessageBoxWizardDialog.setTabOrder(self.closeCheck, self.discardCheck)
        MessageBoxWizardDialog.setTabOrder(self.discardCheck, self.helpCheck)
        MessageBoxWizardDialog.setTabOrder(self.helpCheck, self.ignoreCheck)
        MessageBoxWizardDialog.setTabOrder(self.ignoreCheck, self.noCheck)
        MessageBoxWizardDialog.setTabOrder(self.noCheck, self.notoallCheck)
        MessageBoxWizardDialog.setTabOrder(self.notoallCheck, self.okCheck)
        MessageBoxWizardDialog.setTabOrder(self.okCheck, self.openCheck)
        MessageBoxWizardDialog.setTabOrder(self.openCheck, self.resetCheck)
        MessageBoxWizardDialog.setTabOrder(self.resetCheck, self.restoreCheck)
        MessageBoxWizardDialog.setTabOrder(self.restoreCheck, self.retryCheck)
        MessageBoxWizardDialog.setTabOrder(self.retryCheck, self.saveCheck)
        MessageBoxWizardDialog.setTabOrder(self.saveCheck, self.saveallCheck)
        MessageBoxWizardDialog.setTabOrder(self.saveallCheck, self.yesCheck)
        MessageBoxWizardDialog.setTabOrder(self.yesCheck, self.yestoallCheck)
        MessageBoxWizardDialog.setTabOrder(self.yestoallCheck, self.defaultCombo)
        MessageBoxWizardDialog.setTabOrder(self.defaultCombo, self.buttonBox)

    def retranslateUi(self, MessageBoxWizardDialog):
        _translate = QtCore.QCoreApplication.translate
        MessageBoxWizardDialog.setWindowTitle(_translate("MessageBoxWizardDialog", "QMessageBox Wizard"))
        self.groupBox.setTitle(_translate("MessageBoxWizardDialog", "Type"))
        self.rInformation.setToolTip(_translate("MessageBoxWizardDialog", "Generate an Information QMessageBox"))
        self.rInformation.setText(_translate("MessageBoxWizardDialog", "Information"))
        self.rQuestion.setToolTip(_translate("MessageBoxWizardDialog", "Generate a Question QMessageBox"))
        self.rQuestion.setText(_translate("MessageBoxWizardDialog", "Question"))
        self.rWarning.setToolTip(_translate("MessageBoxWizardDialog", "Generate a Warning QMessageBox"))
        self.rWarning.setText(_translate("MessageBoxWizardDialog", "Warning"))
        self.rCritical.setToolTip(_translate("MessageBoxWizardDialog", "Generate a Critical QMessageBox"))
        self.rCritical.setText(_translate("MessageBoxWizardDialog", "Critical"))
        self.rAbout.setToolTip(_translate("MessageBoxWizardDialog", "Generate an About QMessageBox"))
        self.rAbout.setText(_translate("MessageBoxWizardDialog", "About"))
        self.rAboutQt.setToolTip(_translate("MessageBoxWizardDialog", "Generate an AboutQt QMessageBox"))
        self.rAboutQt.setText(_translate("MessageBoxWizardDialog", "About Qt"))
        self.lResultVar.setText(_translate("MessageBoxWizardDialog", "Result:"))
        self.eResultVar.setToolTip(_translate("MessageBoxWizardDialog", "Enter the result variable name"))
        self.textLabel1.setText(_translate("MessageBoxWizardDialog", "Title"))
        self.eCaption.setToolTip(_translate("MessageBoxWizardDialog", "Enter the title for the QMessageBox"))
        self.textLabel2.setText(_translate("MessageBoxWizardDialog", "Message"))
        self.eMessage.setToolTip(_translate("MessageBoxWizardDialog", "Enter the message to be shown in the QMessageBox"))
        self.parentGroup.setTitle(_translate("MessageBoxWizardDialog", "Parent"))
        self.parentSelf.setToolTip(_translate("MessageBoxWizardDialog", "Select \"self\" as parent"))
        self.parentSelf.setText(_translate("MessageBoxWizardDialog", "self"))
        self.parentNone.setToolTip(_translate("MessageBoxWizardDialog", "Select \"None\" as parent"))
        self.parentNone.setText(_translate("MessageBoxWizardDialog", "None"))
        self.parentOther.setToolTip(_translate("MessageBoxWizardDialog", "Select to enter a parent expression"))
        self.parentOther.setText(_translate("MessageBoxWizardDialog", "Expression:"))
        self.parentEdit.setToolTip(_translate("MessageBoxWizardDialog", "Enter the parent expression"))
        self.standardButtons.setTitle(_translate("MessageBoxWizardDialog", "Standard Buttons"))
        self.applyCheck.setText(_translate("MessageBoxWizardDialog", "Apply"))
        self.abortCheck.setText(_translate("MessageBoxWizardDialog", "Abort"))
        self.cancelCheck.setText(_translate("MessageBoxWizardDialog", "Cancel"))
        self.ignoreCheck.setText(_translate("MessageBoxWizardDialog", "Ignore"))
        self.saveallCheck.setText(_translate("MessageBoxWizardDialog", "Save all"))
        self.saveCheck.setText(_translate("MessageBoxWizardDialog", "Save"))
        self.discardCheck.setText(_translate("MessageBoxWizardDialog", "Discard"))
        self.yestoallCheck.setText(_translate("MessageBoxWizardDialog", "Yes to all"))
        self.openCheck.setText(_translate("MessageBoxWizardDialog", "Open"))
        self.resetCheck.setText(_translate("MessageBoxWizardDialog", "Reset"))
        self.okCheck.setText(_translate("MessageBoxWizardDialog", "Ok"))
        self.noCheck.setText(_translate("MessageBoxWizardDialog", "No"))
        self.helpCheck.setText(_translate("MessageBoxWizardDialog", "Help"))
        self.notoallCheck.setText(_translate("MessageBoxWizardDialog", "No to all"))
        self.retryCheck.setText(_translate("MessageBoxWizardDialog", "Retry"))
        self.restoreCheck.setText(_translate("MessageBoxWizardDialog", "Restore defaults"))
        self.yesCheck.setText(_translate("MessageBoxWizardDialog", "Yes"))
        self.closeCheck.setText(_translate("MessageBoxWizardDialog", "Close"))
        self.TextLabel1_2.setText(_translate("MessageBoxWizardDialog", "Default Button:"))
        self.defaultCombo.setToolTip(_translate("MessageBoxWizardDialog", "Select the default button"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageBoxWizardDialog = QtWidgets.QDialog()
    ui = Ui_MessageBoxWizardDialog()
    ui.setupUi(MessageBoxWizardDialog)
    MessageBoxWizardDialog.show()
    sys.exit(app.exec_())

