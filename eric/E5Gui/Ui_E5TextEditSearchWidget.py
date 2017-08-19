# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\E5Gui\E5TextEditSearchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_E5TextEditSearchWidget(object):
    def setupUi(self, E5TextEditSearchWidget):
        E5TextEditSearchWidget.setObjectName("E5TextEditSearchWidget")
        E5TextEditSearchWidget.resize(475, 22)
        self.horizontalLayout = QtWidgets.QHBoxLayout(E5TextEditSearchWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(E5TextEditSearchWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.findtextCombo = QtWidgets.QComboBox(E5TextEditSearchWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findtextCombo.sizePolicy().hasHeightForWidth())
        self.findtextCombo.setSizePolicy(sizePolicy)
        self.findtextCombo.setMinimumSize(QtCore.QSize(200, 0))
        self.findtextCombo.setEditable(True)
        self.findtextCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.findtextCombo.setDuplicatesEnabled(False)
        self.findtextCombo.setObjectName("findtextCombo")
        self.horizontalLayout.addWidget(self.findtextCombo)
        self.caseCheckBox = QtWidgets.QCheckBox(E5TextEditSearchWidget)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wordCheckBox = QtWidgets.QCheckBox(E5TextEditSearchWidget)
        self.wordCheckBox.setObjectName("wordCheckBox")
        self.horizontalLayout.addWidget(self.wordCheckBox)
        self.findPrevButton = QtWidgets.QToolButton(E5TextEditSearchWidget)
        self.findPrevButton.setObjectName("findPrevButton")
        self.horizontalLayout.addWidget(self.findPrevButton)
        self.findNextButton = QtWidgets.QToolButton(E5TextEditSearchWidget)
        self.findNextButton.setObjectName("findNextButton")
        self.horizontalLayout.addWidget(self.findNextButton)

        self.retranslateUi(E5TextEditSearchWidget)
        QtCore.QMetaObject.connectSlotsByName(E5TextEditSearchWidget)
        E5TextEditSearchWidget.setTabOrder(self.findtextCombo, self.caseCheckBox)
        E5TextEditSearchWidget.setTabOrder(self.caseCheckBox, self.wordCheckBox)
        E5TextEditSearchWidget.setTabOrder(self.wordCheckBox, self.findPrevButton)
        E5TextEditSearchWidget.setTabOrder(self.findPrevButton, self.findNextButton)

    def retranslateUi(self, E5TextEditSearchWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("E5TextEditSearchWidget", "Find:"))
        self.caseCheckBox.setText(_translate("E5TextEditSearchWidget", "Match case"))
        self.wordCheckBox.setText(_translate("E5TextEditSearchWidget", "Whole word"))
        self.findPrevButton.setToolTip(_translate("E5TextEditSearchWidget", "Press to find the previous occurrence"))
        self.findNextButton.setToolTip(_translate("E5TextEditSearchWidget", "Press to find the next occurrence"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    E5TextEditSearchWidget = QtWidgets.QWidget()
    ui = Ui_E5TextEditSearchWidget()
    ui.setupUi(E5TextEditSearchWidget)
    E5TextEditSearchWidget.show()
    sys.exit(app.exec_())

