# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\SearchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWidget(object):
    def setupUi(self, SearchWidget):
        SearchWidget.setObjectName("SearchWidget")
        SearchWidget.resize(274, 142)
        self.verticalLayout = QtWidgets.QVBoxLayout(SearchWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QToolButton(SearchWidget)
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.label = QtWidgets.QLabel(SearchWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.findtextCombo = QtWidgets.QComboBox(SearchWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.caseCheckBox = QtWidgets.QCheckBox(SearchWidget)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.horizontalLayout_2.addWidget(self.caseCheckBox)
        self.wordCheckBox = QtWidgets.QCheckBox(SearchWidget)
        self.wordCheckBox.setObjectName("wordCheckBox")
        self.horizontalLayout_2.addWidget(self.wordCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.findPrevButton = QtWidgets.QToolButton(SearchWidget)
        self.findPrevButton.setObjectName("findPrevButton")
        self.horizontalLayout_3.addWidget(self.findPrevButton)
        self.findNextButton = QtWidgets.QToolButton(SearchWidget)
        self.findNextButton.setObjectName("findNextButton")
        self.horizontalLayout_3.addWidget(self.findNextButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.statusLabel = QtWidgets.QLabel(SearchWidget)
        self.statusLabel.setText("")
        self.statusLabel.setWordWrap(True)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)

        self.retranslateUi(SearchWidget)
        QtCore.QMetaObject.connectSlotsByName(SearchWidget)
        SearchWidget.setTabOrder(self.findtextCombo, self.caseCheckBox)
        SearchWidget.setTabOrder(self.caseCheckBox, self.wordCheckBox)
        SearchWidget.setTabOrder(self.wordCheckBox, self.findPrevButton)
        SearchWidget.setTabOrder(self.findPrevButton, self.findNextButton)
        SearchWidget.setTabOrder(self.findNextButton, self.closeButton)

    def retranslateUi(self, SearchWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchWidget.setWindowTitle(_translate("SearchWidget", "Find"))
        self.closeButton.setToolTip(_translate("SearchWidget", "Press to close the window"))
        self.label.setText(_translate("SearchWidget", "Find:"))
        self.caseCheckBox.setText(_translate("SearchWidget", "Match case"))
        self.wordCheckBox.setText(_translate("SearchWidget", "Whole word"))
        self.findPrevButton.setToolTip(_translate("SearchWidget", "Press to find the previous occurrence"))
        self.findNextButton.setToolTip(_translate("SearchWidget", "Press to find the next occurrence"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWidget = QtWidgets.QWidget()
    ui = Ui_SearchWidget()
    ui.setupUi(SearchWidget)
    SearchWidget.show()
    sys.exit(app.exec_())

