# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorSpellCheckingPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorSpellCheckingPage(object):
    def setupUi(self, EditorSpellCheckingPage):
        EditorSpellCheckingPage.setObjectName("EditorSpellCheckingPage")
        EditorSpellCheckingPage.resize(578, 666)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(EditorSpellCheckingPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.headerLabel = QtWidgets.QLabel(EditorSpellCheckingPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_4.addWidget(self.headerLabel)
        self.line3 = QtWidgets.QFrame(EditorSpellCheckingPage)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setObjectName("line3")
        self.verticalLayout_4.addWidget(self.line3)
        self.errorLabel = QtWidgets.QLabel(EditorSpellCheckingPage)
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout_4.addWidget(self.errorLabel)
        self.spellingFrame = QtWidgets.QFrame(EditorSpellCheckingPage)
        self.spellingFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.spellingFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.spellingFrame.setObjectName("spellingFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.spellingFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkingEnabledCheckBox = QtWidgets.QCheckBox(self.spellingFrame)
        self.checkingEnabledCheckBox.setObjectName("checkingEnabledCheckBox")
        self.verticalLayout_3.addWidget(self.checkingEnabledCheckBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.spellingFrame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.defaultLanguageCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.defaultLanguageCombo.setObjectName("defaultLanguageCombo")
        self.gridLayout_3.addWidget(self.defaultLanguageCombo, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(353, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.spellingFrame)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stringsOnlyCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.stringsOnlyCheckBox.setObjectName("stringsOnlyCheckBox")
        self.verticalLayout.addWidget(self.stringsOnlyCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.minimumWordSizeSlider = QtWidgets.QSlider(self.groupBox_4)
        self.minimumWordSizeSlider.setMinimum(1)
        self.minimumWordSizeSlider.setMaximum(10)
        self.minimumWordSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minimumWordSizeSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.minimumWordSizeSlider.setTickInterval(1)
        self.minimumWordSizeSlider.setObjectName("minimumWordSizeSlider")
        self.horizontalLayout.addWidget(self.minimumWordSizeSlider)
        self.lCDNumber = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lCDNumber.setDigitCount(2)
        self.lCDNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lCDNumber.setProperty("intValue", 1)
        self.lCDNumber.setObjectName("lCDNumber")
        self.horizontalLayout.addWidget(self.lCDNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.spellingFrame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TextLabel2_2_2_2_2_2 = QtWidgets.QLabel(self.groupBox_2)
        self.TextLabel2_2_2_2_2_2.setObjectName("TextLabel2_2_2_2_2_2")
        self.gridLayout_2.addWidget(self.TextLabel2_2_2_2_2_2, 0, 0, 1, 1)
        self.spellingMarkerButton = QtWidgets.QPushButton(self.groupBox_2)
        self.spellingMarkerButton.setMinimumSize(QtCore.QSize(100, 0))
        self.spellingMarkerButton.setText("")
        self.spellingMarkerButton.setObjectName("spellingMarkerButton")
        self.gridLayout_2.addWidget(self.spellingMarkerButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.spellingFrame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.pwlPicker = E5PathPicker(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwlPicker.sizePolicy().hasHeightForWidth())
        self.pwlPicker.setSizePolicy(sizePolicy)
        self.pwlPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pwlPicker.setObjectName("pwlPicker")
        self.gridLayout.addWidget(self.pwlPicker, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.pelPicker = E5PathPicker(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pelPicker.sizePolicy().hasHeightForWidth())
        self.pelPicker.setSizePolicy(sizePolicy)
        self.pelPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pelPicker.setObjectName("pelPicker")
        self.gridLayout.addWidget(self.pelPicker, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.spellingFrame)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.enabledCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.enabledCheckBox.setObjectName("enabledCheckBox")
        self.verticalLayout_2.addWidget(self.enabledCheckBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.chunkSizeSpinBox = QtWidgets.QSpinBox(self.groupBox_5)
        self.chunkSizeSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chunkSizeSpinBox.setMinimum(10)
        self.chunkSizeSpinBox.setMaximum(999)
        self.chunkSizeSpinBox.setObjectName("chunkSizeSpinBox")
        self.horizontalLayout_3.addWidget(self.chunkSizeSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.verticalLayout_4.addWidget(self.spellingFrame)
        spacerItem3 = QtWidgets.QSpacerItem(558, 231, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)

        self.retranslateUi(EditorSpellCheckingPage)
        self.minimumWordSizeSlider.valueChanged['int'].connect(self.lCDNumber.display)
        QtCore.QMetaObject.connectSlotsByName(EditorSpellCheckingPage)
        EditorSpellCheckingPage.setTabOrder(self.checkingEnabledCheckBox, self.defaultLanguageCombo)
        EditorSpellCheckingPage.setTabOrder(self.defaultLanguageCombo, self.stringsOnlyCheckBox)
        EditorSpellCheckingPage.setTabOrder(self.stringsOnlyCheckBox, self.minimumWordSizeSlider)
        EditorSpellCheckingPage.setTabOrder(self.minimumWordSizeSlider, self.spellingMarkerButton)
        EditorSpellCheckingPage.setTabOrder(self.spellingMarkerButton, self.pwlPicker)
        EditorSpellCheckingPage.setTabOrder(self.pwlPicker, self.pelPicker)
        EditorSpellCheckingPage.setTabOrder(self.pelPicker, self.enabledCheckBox)
        EditorSpellCheckingPage.setTabOrder(self.enabledCheckBox, self.chunkSizeSpinBox)

    def retranslateUi(self, EditorSpellCheckingPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorSpellCheckingPage", "<b>Configure editor spell checking options</b>"))
        self.errorLabel.setText(_translate("EditorSpellCheckingPage", "<font color=\"#FF0000\">Spell checking with PyEnchant is not available.</font>"))
        self.checkingEnabledCheckBox.setToolTip(_translate("EditorSpellCheckingPage", "Select to enable spell checking"))
        self.checkingEnabledCheckBox.setText(_translate("EditorSpellCheckingPage", "Spell checking enabled"))
        self.groupBox_3.setTitle(_translate("EditorSpellCheckingPage", "Defaults"))
        self.label_2.setText(_translate("EditorSpellCheckingPage", "Default language:"))
        self.defaultLanguageCombo.setToolTip(_translate("EditorSpellCheckingPage", "Select the default language"))
        self.groupBox_4.setTitle(_translate("EditorSpellCheckingPage", "Spell checking options"))
        self.stringsOnlyCheckBox.setToolTip(_translate("EditorSpellCheckingPage", "Select to check strings only"))
        self.stringsOnlyCheckBox.setText(_translate("EditorSpellCheckingPage", "Spell check strings only"))
        self.label.setText(_translate("EditorSpellCheckingPage", "Minimum word size:"))
        self.minimumWordSizeSlider.setToolTip(_translate("EditorSpellCheckingPage", "Move to set the minimum size of words to be checked"))
        self.lCDNumber.setToolTip(_translate("EditorSpellCheckingPage", "Displays the minimum size of words to be checked"))
        self.groupBox_2.setTitle(_translate("EditorSpellCheckingPage", "Colours"))
        self.TextLabel2_2_2_2_2_2.setText(_translate("EditorSpellCheckingPage", "Marker Colour:"))
        self.spellingMarkerButton.setToolTip(_translate("EditorSpellCheckingPage", "Select the colour for the spelling markers."))
        self.groupBox.setTitle(_translate("EditorSpellCheckingPage", "Personal lists"))
        self.label_4.setText(_translate("EditorSpellCheckingPage", "Personal word list file:"))
        self.label_5.setText(_translate("EditorSpellCheckingPage", "Personal exclude list file:"))
        self.label_6.setText(_translate("EditorSpellCheckingPage", "<b>Note:</b> leave these entries empty to use the default"))
        self.label_7.setText(_translate("EditorSpellCheckingPage", "<b>Note:</b> valid for all newly opened editors"))
        self.groupBox_5.setTitle(_translate("EditorSpellCheckingPage", "Automatic spell checking"))
        self.enabledCheckBox.setToolTip(_translate("EditorSpellCheckingPage", "Select to enable spellchecking"))
        self.enabledCheckBox.setText(_translate("EditorSpellCheckingPage", "Automatic spell checking enabled"))
        self.label_3.setText(_translate("EditorSpellCheckingPage", "Amount of lines to autocheck at once:"))
        self.chunkSizeSpinBox.setToolTip(_translate("EditorSpellCheckingPage", "Enter the number of lines to check per go. Higher values increase checking speed but decrease GUI responsivenes"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorSpellCheckingPage = QtWidgets.QWidget()
    ui = Ui_EditorSpellCheckingPage()
    ui.setupUi(EditorSpellCheckingPage)
    EditorSpellCheckingPage.show()
    sys.exit(app.exec_())

