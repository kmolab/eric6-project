# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorKeywordsPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorKeywordsPage(object):
    def setupUi(self, EditorKeywordsPage):
        EditorKeywordsPage.setObjectName("EditorKeywordsPage")
        EditorKeywordsPage.resize(462, 422)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditorKeywordsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(EditorKeywordsPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line5 = QtWidgets.QFrame(EditorKeywordsPage)
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setObjectName("line5")
        self.verticalLayout.addWidget(self.line5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TextLabel1_3_3 = QtWidgets.QLabel(EditorKeywordsPage)
        self.TextLabel1_3_3.setToolTip("")
        self.TextLabel1_3_3.setObjectName("TextLabel1_3_3")
        self.horizontalLayout.addWidget(self.TextLabel1_3_3)
        self.languageCombo = QtWidgets.QComboBox(EditorKeywordsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.languageCombo.sizePolicy().hasHeightForWidth())
        self.languageCombo.setSizePolicy(sizePolicy)
        self.languageCombo.setObjectName("languageCombo")
        self.horizontalLayout.addWidget(self.languageCombo)
        self.label = QtWidgets.QLabel(EditorKeywordsPage)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.setSpinBox = QtWidgets.QSpinBox(EditorKeywordsPage)
        self.setSpinBox.setMinimum(1)
        self.setSpinBox.setMaximum(9)
        self.setSpinBox.setObjectName("setSpinBox")
        self.horizontalLayout.addWidget(self.setSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.keywordsEdit = QtWidgets.QPlainTextEdit(EditorKeywordsPage)
        self.keywordsEdit.setObjectName("keywordsEdit")
        self.verticalLayout.addWidget(self.keywordsEdit)

        self.retranslateUi(EditorKeywordsPage)
        QtCore.QMetaObject.connectSlotsByName(EditorKeywordsPage)
        EditorKeywordsPage.setTabOrder(self.languageCombo, self.setSpinBox)
        EditorKeywordsPage.setTabOrder(self.setSpinBox, self.keywordsEdit)

    def retranslateUi(self, EditorKeywordsPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorKeywordsPage", "<b>Configure syntax highlighter keywords</b>"))
        self.TextLabel1_3_3.setText(_translate("EditorKeywordsPage", "Language:"))
        self.languageCombo.setToolTip(_translate("EditorKeywordsPage", "Select the language to be configured."))
        self.label.setText(_translate("EditorKeywordsPage", "Set:"))
        self.keywordsEdit.setToolTip(_translate("EditorKeywordsPage", "Enter the keywords separated by a blank"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorKeywordsPage = QtWidgets.QWidget()
    ui = Ui_EditorKeywordsPage()
    ui.setupUi(EditorKeywordsPage)
    EditorKeywordsPage.show()
    sys.exit(app.exec_())

