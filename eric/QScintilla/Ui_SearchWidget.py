# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\QScintilla\SearchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWidget(object):
    def setupUi(self, SearchWidget):
        SearchWidget.setObjectName("SearchWidget")
        SearchWidget.resize(973, 25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SearchWidget.sizePolicy().hasHeightForWidth())
        SearchWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SearchWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.closeButton = QtWidgets.QToolButton(SearchWidget)
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.label = QtWidgets.QLabel(SearchWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.findtextCombo = QtWidgets.QComboBox(SearchWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findtextCombo.sizePolicy().hasHeightForWidth())
        self.findtextCombo.setSizePolicy(sizePolicy)
        self.findtextCombo.setMinimumSize(QtCore.QSize(300, 0))
        self.findtextCombo.setEditable(True)
        self.findtextCombo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.findtextCombo.setDuplicatesEnabled(False)
        self.findtextCombo.setObjectName("findtextCombo")
        self.horizontalLayout.addWidget(self.findtextCombo)
        self.findPrevButton = QtWidgets.QToolButton(SearchWidget)
        self.findPrevButton.setObjectName("findPrevButton")
        self.horizontalLayout.addWidget(self.findPrevButton)
        self.findNextButton = QtWidgets.QToolButton(SearchWidget)
        self.findNextButton.setObjectName("findNextButton")
        self.horizontalLayout.addWidget(self.findNextButton)
        self.caseCheckBox = QtWidgets.QCheckBox(SearchWidget)
        self.caseCheckBox.setObjectName("caseCheckBox")
        self.horizontalLayout.addWidget(self.caseCheckBox)
        self.wordCheckBox = QtWidgets.QCheckBox(SearchWidget)
        self.wordCheckBox.setObjectName("wordCheckBox")
        self.horizontalLayout.addWidget(self.wordCheckBox)
        self.regexpCheckBox = QtWidgets.QCheckBox(SearchWidget)
        self.regexpCheckBox.setObjectName("regexpCheckBox")
        self.horizontalLayout.addWidget(self.regexpCheckBox)
        self.wrapCheckBox = QtWidgets.QCheckBox(SearchWidget)
        self.wrapCheckBox.setObjectName("wrapCheckBox")
        self.horizontalLayout.addWidget(self.wrapCheckBox)
        self.selectionCheckBox = QtWidgets.QCheckBox(SearchWidget)
        self.selectionCheckBox.setObjectName("selectionCheckBox")
        self.horizontalLayout.addWidget(self.selectionCheckBox)
        self.label.setBuddy(self.findtextCombo)

        self.retranslateUi(SearchWidget)
        QtCore.QMetaObject.connectSlotsByName(SearchWidget)
        SearchWidget.setTabOrder(self.findtextCombo, self.caseCheckBox)
        SearchWidget.setTabOrder(self.caseCheckBox, self.wordCheckBox)
        SearchWidget.setTabOrder(self.wordCheckBox, self.regexpCheckBox)
        SearchWidget.setTabOrder(self.regexpCheckBox, self.wrapCheckBox)
        SearchWidget.setTabOrder(self.wrapCheckBox, self.selectionCheckBox)
        SearchWidget.setTabOrder(self.selectionCheckBox, self.findNextButton)
        SearchWidget.setTabOrder(self.findNextButton, self.findPrevButton)
        SearchWidget.setTabOrder(self.findPrevButton, self.closeButton)

    def retranslateUi(self, SearchWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchWidget.setWindowTitle(_translate("SearchWidget", "Find"))
        self.closeButton.setToolTip(_translate("SearchWidget", "Press to close the window"))
        self.label.setText(_translate("SearchWidget", "&Find:"))
        self.findPrevButton.setToolTip(_translate("SearchWidget", "Press to find the previous occurrence"))
        self.findNextButton.setToolTip(_translate("SearchWidget", "Press to find the next occurrence"))
        self.caseCheckBox.setText(_translate("SearchWidget", "&Match case"))
        self.wordCheckBox.setText(_translate("SearchWidget", "Whole &word"))
        self.regexpCheckBox.setText(_translate("SearchWidget", "Rege&xp"))
        self.wrapCheckBox.setText(_translate("SearchWidget", "Wrap &around"))
        self.selectionCheckBox.setText(_translate("SearchWidget", "&Selection only"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWidget = QtWidgets.QWidget()
    ui = Ui_SearchWidget()
    ui.setupUi(SearchWidget)
    SearchWidget.show()
    sys.exit(app.exec_())

