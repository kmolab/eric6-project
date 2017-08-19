# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorAutocompletionQScintillaPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorAutocompletionQScintillaPage(object):
    def setupUi(self, EditorAutocompletionQScintillaPage):
        EditorAutocompletionQScintillaPage.setObjectName("EditorAutocompletionQScintillaPage")
        EditorAutocompletionQScintillaPage.resize(506, 257)
        self.gridLayout = QtWidgets.QGridLayout(EditorAutocompletionQScintillaPage)
        self.gridLayout.setObjectName("gridLayout")
        self.headerLabel = QtWidgets.QLabel(EditorAutocompletionQScintillaPage)
        self.headerLabel.setObjectName("headerLabel")
        self.gridLayout.addWidget(self.headerLabel, 0, 0, 1, 2)
        self.line6 = QtWidgets.QFrame(EditorAutocompletionQScintillaPage)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setObjectName("line6")
        self.gridLayout.addWidget(self.line6, 1, 0, 1, 2)
        self.acShowSingleCheckBox = QtWidgets.QCheckBox(EditorAutocompletionQScintillaPage)
        self.acShowSingleCheckBox.setObjectName("acShowSingleCheckBox")
        self.gridLayout.addWidget(self.acShowSingleCheckBox, 2, 0, 1, 1)
        self.acFillupsCheckBox = QtWidgets.QCheckBox(EditorAutocompletionQScintillaPage)
        self.acFillupsCheckBox.setObjectName("acFillupsCheckBox")
        self.gridLayout.addWidget(self.acFillupsCheckBox, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(EditorAutocompletionQScintillaPage)
        self.groupBox.setObjectName("groupBox")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.hboxlayout.setObjectName("hboxlayout")
        self.acSourceDocumentRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.acSourceDocumentRadioButton.setObjectName("acSourceDocumentRadioButton")
        self.hboxlayout.addWidget(self.acSourceDocumentRadioButton)
        self.acSourceAPIsRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.acSourceAPIsRadioButton.setObjectName("acSourceAPIsRadioButton")
        self.hboxlayout.addWidget(self.acSourceAPIsRadioButton)
        self.acSourceAllRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.acSourceAllRadioButton.setObjectName("acSourceAllRadioButton")
        self.hboxlayout.addWidget(self.acSourceAllRadioButton)
        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(456, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)

        self.retranslateUi(EditorAutocompletionQScintillaPage)
        QtCore.QMetaObject.connectSlotsByName(EditorAutocompletionQScintillaPage)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acShowSingleCheckBox, self.acFillupsCheckBox)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acFillupsCheckBox, self.acSourceDocumentRadioButton)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acSourceDocumentRadioButton, self.acSourceAPIsRadioButton)
        EditorAutocompletionQScintillaPage.setTabOrder(self.acSourceAPIsRadioButton, self.acSourceAllRadioButton)

    def retranslateUi(self, EditorAutocompletionQScintillaPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorAutocompletionQScintillaPage", "<b>Configure QScintilla Completion</b>"))
        self.acShowSingleCheckBox.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this, if single entries shall be inserted automatically"))
        self.acShowSingleCheckBox.setText(_translate("EditorAutocompletionQScintillaPage", "Show single"))
        self.acFillupsCheckBox.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select to enable the use of fill-up characters to autocomplete the current word"))
        self.acFillupsCheckBox.setWhatsThis(_translate("EditorAutocompletionQScintillaPage", "<b>Use fill-up characters</b><p>Select to enable the use of fill-up characters to autocomplete the current word. A fill-up character is one that, when entered while an auto-completion list is being displayed, causes the currently selected item from the list to be added to the text followed by the fill-up character.</p>"))
        self.acFillupsCheckBox.setText(_translate("EditorAutocompletionQScintillaPage", "Use fill-up characters"))
        self.groupBox.setTitle(_translate("EditorAutocompletionQScintillaPage", "Source"))
        self.acSourceDocumentRadioButton.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this to get autocompletion from current document"))
        self.acSourceDocumentRadioButton.setText(_translate("EditorAutocompletionQScintillaPage", "from Document"))
        self.acSourceAPIsRadioButton.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this to get autocompletion from installed APIs"))
        self.acSourceAPIsRadioButton.setText(_translate("EditorAutocompletionQScintillaPage", "from API files"))
        self.acSourceAllRadioButton.setToolTip(_translate("EditorAutocompletionQScintillaPage", "Select this to get autocompletion from current document and installed APIs"))
        self.acSourceAllRadioButton.setText(_translate("EditorAutocompletionQScintillaPage", "from Document and API files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorAutocompletionQScintillaPage = QtWidgets.QWidget()
    ui = Ui_EditorAutocompletionQScintillaPage()
    ui.setupUi(EditorAutocompletionQScintillaPage)
    EditorAutocompletionQScintillaPage.show()
    sys.exit(app.exec_())

