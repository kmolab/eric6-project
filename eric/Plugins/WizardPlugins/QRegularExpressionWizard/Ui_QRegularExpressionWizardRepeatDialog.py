# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\WizardPlugins\QRegularExpressionWizard\QRegularExpressionWizardRepeatDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QRegularExpressionWizardRepeatDialog(object):
    def setupUi(self, QRegularExpressionWizardRepeatDialog):
        QRegularExpressionWizardRepeatDialog.setObjectName("QRegularExpressionWizardRepeatDialog")
        QRegularExpressionWizardRepeatDialog.resize(331, 370)
        QRegularExpressionWizardRepeatDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(QRegularExpressionWizardRepeatDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(QRegularExpressionWizardRepeatDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.textLabel1_6 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_6.setObjectName("textLabel1_6")
        self.gridlayout.addWidget(self.textLabel1_6, 2, 2, 1, 1)
        self.textLabel1_7 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_7.setObjectName("textLabel1_7")
        self.gridlayout.addWidget(self.textLabel1_7, 3, 2, 1, 1)
        self.textLabel1_5 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_5.setObjectName("textLabel1_5")
        self.gridlayout.addWidget(self.textLabel1_5, 1, 2, 1, 1)
        self.lowerSpin = QtWidgets.QSpinBox(self.groupBox)
        self.lowerSpin.setEnabled(False)
        self.lowerSpin.setAlignment(QtCore.Qt.AlignRight)
        self.lowerSpin.setProperty("value", 1)
        self.lowerSpin.setObjectName("lowerSpin")
        self.gridlayout.addWidget(self.lowerSpin, 4, 1, 1, 1)
        self.upperSpin = QtWidgets.QSpinBox(self.groupBox)
        self.upperSpin.setEnabled(False)
        self.upperSpin.setAlignment(QtCore.Qt.AlignRight)
        self.upperSpin.setProperty("value", 1)
        self.upperSpin.setObjectName("upperSpin")
        self.gridlayout.addWidget(self.upperSpin, 4, 3, 1, 1)
        self.textLabel6 = QtWidgets.QLabel(self.groupBox)
        self.textLabel6.setObjectName("textLabel6")
        self.gridlayout.addWidget(self.textLabel6, 4, 2, 1, 1)
        self.betweenButton = QtWidgets.QRadioButton(self.groupBox)
        self.betweenButton.setObjectName("betweenButton")
        self.gridlayout.addWidget(self.betweenButton, 4, 0, 1, 1)
        self.exactSpin = QtWidgets.QSpinBox(self.groupBox)
        self.exactSpin.setEnabled(False)
        self.exactSpin.setAlignment(QtCore.Qt.AlignRight)
        self.exactSpin.setProperty("value", 1)
        self.exactSpin.setObjectName("exactSpin")
        self.gridlayout.addWidget(self.exactSpin, 3, 1, 1, 1)
        self.exactButton = QtWidgets.QRadioButton(self.groupBox)
        self.exactButton.setObjectName("exactButton")
        self.gridlayout.addWidget(self.exactButton, 3, 0, 1, 1)
        self.maxSpin = QtWidgets.QSpinBox(self.groupBox)
        self.maxSpin.setEnabled(False)
        self.maxSpin.setAlignment(QtCore.Qt.AlignRight)
        self.maxSpin.setProperty("value", 1)
        self.maxSpin.setObjectName("maxSpin")
        self.gridlayout.addWidget(self.maxSpin, 2, 1, 1, 1)
        self.maxButton = QtWidgets.QRadioButton(self.groupBox)
        self.maxButton.setObjectName("maxButton")
        self.gridlayout.addWidget(self.maxButton, 2, 0, 1, 1)
        self.minButton = QtWidgets.QRadioButton(self.groupBox)
        self.minButton.setObjectName("minButton")
        self.gridlayout.addWidget(self.minButton, 1, 0, 1, 1)
        self.minSpin = QtWidgets.QSpinBox(self.groupBox)
        self.minSpin.setEnabled(False)
        self.minSpin.setAlignment(QtCore.Qt.AlignRight)
        self.minSpin.setProperty("value", 1)
        self.minSpin.setObjectName("minSpin")
        self.gridlayout.addWidget(self.minSpin, 1, 1, 1, 1)
        self.unlimitedButton = QtWidgets.QRadioButton(self.groupBox)
        self.unlimitedButton.setObjectName("unlimitedButton")
        self.gridlayout.addWidget(self.unlimitedButton, 0, 0, 1, 4)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(QRegularExpressionWizardRepeatDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.greedyButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.greedyButton.setObjectName("greedyButton")
        self.verticalLayout_2.addWidget(self.greedyButton)
        self.possessiveButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.possessiveButton.setObjectName("possessiveButton")
        self.verticalLayout_2.addWidget(self.possessiveButton)
        self.lazyButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.lazyButton.setObjectName("lazyButton")
        self.verticalLayout_2.addWidget(self.lazyButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(QRegularExpressionWizardRepeatDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(QRegularExpressionWizardRepeatDialog)
        self.minButton.toggled['bool'].connect(self.minSpin.setEnabled)
        self.maxButton.toggled['bool'].connect(self.maxSpin.setEnabled)
        self.exactButton.toggled['bool'].connect(self.exactSpin.setEnabled)
        self.betweenButton.toggled['bool'].connect(self.lowerSpin.setEnabled)
        self.betweenButton.toggled['bool'].connect(self.upperSpin.setEnabled)
        self.buttonBox.accepted.connect(QRegularExpressionWizardRepeatDialog.accept)
        self.buttonBox.rejected.connect(QRegularExpressionWizardRepeatDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QRegularExpressionWizardRepeatDialog)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.unlimitedButton, self.minButton)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.minButton, self.minSpin)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.minSpin, self.maxButton)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.maxButton, self.maxSpin)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.maxSpin, self.exactButton)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.exactButton, self.exactSpin)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.exactSpin, self.betweenButton)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.betweenButton, self.lowerSpin)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.lowerSpin, self.upperSpin)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.upperSpin, self.greedyButton)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.greedyButton, self.possessiveButton)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.possessiveButton, self.lazyButton)
        QRegularExpressionWizardRepeatDialog.setTabOrder(self.lazyButton, self.buttonBox)

    def retranslateUi(self, QRegularExpressionWizardRepeatDialog):
        _translate = QtCore.QCoreApplication.translate
        QRegularExpressionWizardRepeatDialog.setWindowTitle(_translate("QRegularExpressionWizardRepeatDialog", "Number of repetitions"))
        self.groupBox.setTitle(_translate("QRegularExpressionWizardRepeatDialog", "Quantifier"))
        self.textLabel1_6.setText(_translate("QRegularExpressionWizardRepeatDialog", "times"))
        self.textLabel1_7.setText(_translate("QRegularExpressionWizardRepeatDialog", "times"))
        self.textLabel1_5.setText(_translate("QRegularExpressionWizardRepeatDialog", "times"))
        self.textLabel6.setText(_translate("QRegularExpressionWizardRepeatDialog", "and"))
        self.betweenButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Between"))
        self.exactButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Exactly"))
        self.maxButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Maximum"))
        self.minButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Minimum"))
        self.unlimitedButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Unlimited (incl. zero times)"))
        self.groupBox_2.setTitle(_translate("QRegularExpressionWizardRepeatDialog", "Greediness"))
        self.greedyButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Greedy"))
        self.possessiveButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Possessive"))
        self.lazyButton.setText(_translate("QRegularExpressionWizardRepeatDialog", "Lazy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QRegularExpressionWizardRepeatDialog = QtWidgets.QDialog()
    ui = Ui_QRegularExpressionWizardRepeatDialog()
    ui.setupUi(QRegularExpressionWizardRepeatDialog)
    QRegularExpressionWizardRepeatDialog.show()
    sys.exit(app.exec_())

