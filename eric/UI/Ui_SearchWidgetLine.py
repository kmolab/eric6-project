# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\SearchWidgetLine.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWidgetLine(object):
    def setupUi(self, SearchWidgetLine):
        SearchWidgetLine.setObjectName("SearchWidgetLine")
        SearchWidgetLine.resize(550, 52)
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchWidgetLine)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QToolButton(SearchWidgetLine)
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.label = QtWidgets.QLabel(SearchWidgetLine)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.findtextCombo = QtWidgets.QComboBox(SearchWidgetLine)
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
        self.findPrevButton = QtWidgets.QToolButton(SearchWidgetLine)
        self.findPrevButton.setObjectName("findPrevButton")
        self.horizontalLayout.addWidget(self.findPrevButton)
        self.findNextButton = QtWidgets.QToolButton(SearchWidgetLine)
        self.findNextButton.setObjectName("findNextButton")
        self.horizontalLayout.addWidget(self.findNextButton)
        self.caseCheckBox = QtWidgets.QCheckBox(SearchWidgetLine)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wordCheckBox = QtWidgets.QCheckBox(SearchWidgetLine)
        self.wordCheckBox.setObjectName("wordCheckBox")
        self.horizontalLayout.addWidget(self.wordCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.statusLabel = QtWidgets.QLabel(SearchWidgetLine)
        self.statusLabel.setText("")
        self.statusLabel.setWordWrap(True)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)

        self.retranslateUi(SearchWidgetLine)
        QtCore.QMetaObject.connectSlotsByName(SearchWidgetLine)
        SearchWidgetLine.setTabOrder(self.findtextCombo, self.caseCheckBox)
        SearchWidgetLine.setTabOrder(self.caseCheckBox, self.wordCheckBox)
        SearchWidgetLine.setTabOrder(self.wordCheckBox, self.findNextButton)
        SearchWidgetLine.setTabOrder(self.findNextButton, self.findPrevButton)
        SearchWidgetLine.setTabOrder(self.findPrevButton, self.closeButton)

    def retranslateUi(self, SearchWidgetLine):
        _translate = QtCore.QCoreApplication.translate
        SearchWidgetLine.setWindowTitle(_translate("SearchWidgetLine", "Find"))
        self.closeButton.setToolTip(_translate("SearchWidgetLine", "Press to close the window"))
        self.label.setText(_translate("SearchWidgetLine", "Find:"))
        self.findPrevButton.setToolTip(_translate("SearchWidgetLine", "Press to find the previous occurrence"))
        self.findNextButton.setToolTip(_translate("SearchWidgetLine", "Press to find the next occurrence"))
        self.caseCheckBox.setText(_translate("SearchWidgetLine", "Match case"))
        self.wordCheckBox.setText(_translate("SearchWidgetLine", "Whole word"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWidgetLine = QtWidgets.QWidget()
    ui = Ui_SearchWidgetLine()
    ui.setupUi(SearchWidgetLine)
    SearchWidgetLine.show()
    sys.exit(app.exec_())

