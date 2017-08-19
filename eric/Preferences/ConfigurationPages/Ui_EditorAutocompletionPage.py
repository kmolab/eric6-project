# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorAutocompletionPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorAutocompletionPage(object):
    def setupUi(self, EditorAutocompletionPage):
        EditorAutocompletionPage.setObjectName("EditorAutocompletionPage")
        EditorAutocompletionPage.resize(506, 398)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EditorAutocompletionPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.headerLabel = QtWidgets.QLabel(EditorAutocompletionPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_2.addWidget(self.headerLabel)
        self.line6 = QtWidgets.QFrame(EditorAutocompletionPage)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setObjectName("line6")
        self.verticalLayout_2.addWidget(self.line6)
        self.acEnabledCheckBox = QtWidgets.QCheckBox(EditorAutocompletionPage)
        self.acEnabledCheckBox.setObjectName("acEnabledCheckBox")
        self.verticalLayout_2.addWidget(self.acEnabledCheckBox)
        self.groupBox = QtWidgets.QGroupBox(EditorAutocompletionPage)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.acCaseSensitivityCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.acCaseSensitivityCheckBox.setObjectName("acCaseSensitivityCheckBox")
        self.gridLayout.addWidget(self.acCaseSensitivityCheckBox, 0, 0, 1, 1)
        self.acReplaceWordCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.acReplaceWordCheckBox.setObjectName("acReplaceWordCheckBox")
        self.gridLayout.addWidget(self.acReplaceWordCheckBox, 0, 1, 1, 1)
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setObjectName("_2")
        self.textLabel1_2 = QtWidgets.QLabel(self.groupBox)
        self.textLabel1_2.setObjectName("textLabel1_2")
        self._2.addWidget(self.textLabel1_2)
        self.acThresholdSlider = QtWidgets.QSlider(self.groupBox)
        self.acThresholdSlider.setMaximum(10)
        self.acThresholdSlider.setProperty("value", 2)
        self.acThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.acThresholdSlider.setTickInterval(1)
        self.acThresholdSlider.setObjectName("acThresholdSlider")
        self._2.addWidget(self.acThresholdSlider)
        self.lCDNumber4 = QtWidgets.QLCDNumber(self.groupBox)
        self.lCDNumber4.setDigitCount(2)
        self.lCDNumber4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lCDNumber4.setProperty("value", 2.0)
        self.lCDNumber4.setObjectName("lCDNumber4")
        self._2.addWidget(self.lCDNumber4)
        self.gridLayout.addLayout(self._2, 1, 0, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(EditorAutocompletionPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.acScintillaCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.acScintillaCheckBox.setObjectName("acScintillaCheckBox")
        self.verticalLayout.addWidget(self.acScintillaCheckBox)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(456, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(EditorAutocompletionPage)
        self.acThresholdSlider.valueChanged['int'].connect(self.lCDNumber4.display)
        self.acEnabledCheckBox.toggled['bool'].connect(self.groupBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(EditorAutocompletionPage)
        EditorAutocompletionPage.setTabOrder(self.acEnabledCheckBox, self.acCaseSensitivityCheckBox)
        EditorAutocompletionPage.setTabOrder(self.acCaseSensitivityCheckBox, self.acReplaceWordCheckBox)
        EditorAutocompletionPage.setTabOrder(self.acReplaceWordCheckBox, self.acThresholdSlider)
        EditorAutocompletionPage.setTabOrder(self.acThresholdSlider, self.acScintillaCheckBox)

    def retranslateUi(self, EditorAutocompletionPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorAutocompletionPage", "<b>Configure Completion Support</b>"))
        self.acEnabledCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this to enable autocompletion"))
        self.acEnabledCheckBox.setWhatsThis(_translate("EditorAutocompletionPage", "<b>Autocompletion Enabled</b><p>Select to enable autocompletion. In order to get autocompletion from alternative autocompletion providers (if installed), these have to be enabled on their respective configuration page. Only one alternative provider might be enabled.</p>"))
        self.acEnabledCheckBox.setText(_translate("EditorAutocompletionPage", "Automatic Completion Enabled"))
        self.groupBox.setTitle(_translate("EditorAutocompletionPage", "General"))
        self.acCaseSensitivityCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this to have case sensitive auto-completion lists"))
        self.acCaseSensitivityCheckBox.setText(_translate("EditorAutocompletionPage", "Case sensitive"))
        self.acReplaceWordCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select this, if the word to the right should be replaced by the selected entry"))
        self.acReplaceWordCheckBox.setText(_translate("EditorAutocompletionPage", "Replace word"))
        self.textLabel1_2.setText(_translate("EditorAutocompletionPage", "Threshold:"))
        self.acThresholdSlider.setToolTip(_translate("EditorAutocompletionPage", "Move to set the threshold for display of an autocompletion list"))
        self.lCDNumber4.setToolTip(_translate("EditorAutocompletionPage", "Displays the selected autocompletion threshold"))
        self.groupBox_2.setTitle(_translate("EditorAutocompletionPage", "Plug-In Behavior"))
        self.acScintillaCheckBox.setToolTip(_translate("EditorAutocompletionPage", "Select to show QScintilla provided completions, if the selected plug-ins fail"))
        self.acScintillaCheckBox.setWhatsThis(_translate("EditorAutocompletionPage", "Qscintilla provided completions are shown, if this option is enabled and completions shall be provided by plug-ins (see completions sub-page of the plug-in) and the plugin-ins don\'t deliver any completions."))
        self.acScintillaCheckBox.setText(_translate("EditorAutocompletionPage", "Show QScintilla completions, if plug-ins fail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorAutocompletionPage = QtWidgets.QWidget()
    ui = Ui_EditorAutocompletionPage()
    ui.setupUi(EditorAutocompletionPage)
    EditorAutocompletionPage.show()
    sys.exit(app.exec_())

