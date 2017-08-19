# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\WebBrowser\SearchWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWidget(object):
    def setupUi(self, SearchWidget):
        SearchWidget.setObjectName("SearchWidget")
        SearchWidget.resize(747, 26)
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
        self.infoLine = QtWidgets.QFrame(SearchWidget)
        self.infoLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.infoLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.infoLine.setObjectName("infoLine")
        self.horizontalLayout.addWidget(self.infoLine)
        self.infoLabel = QtWidgets.QLabel(SearchWidget)
        self.infoLabel.setMinimumSize(QtCore.QSize(200, 0))
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout.addWidget(self.infoLabel)

        self.retranslateUi(SearchWidget)
        QtCore.QMetaObject.connectSlotsByName(SearchWidget)
        SearchWidget.setTabOrder(self.findtextCombo, self.caseCheckBox)
        SearchWidget.setTabOrder(self.caseCheckBox, self.findNextButton)
        SearchWidget.setTabOrder(self.findNextButton, self.findPrevButton)
        SearchWidget.setTabOrder(self.findPrevButton, self.closeButton)

    def retranslateUi(self, SearchWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchWidget.setWindowTitle(_translate("SearchWidget", "Find"))
        self.closeButton.setToolTip(_translate("SearchWidget", "Press to close the window"))
        self.label.setText(_translate("SearchWidget", "Find:"))
        self.findPrevButton.setToolTip(_translate("SearchWidget", "Press to find the previous occurrence"))
        self.findNextButton.setToolTip(_translate("SearchWidget", "Press to find the next occurrence"))
        self.caseCheckBox.setText(_translate("SearchWidget", "Match case"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWidget = QtWidgets.QWidget()
    ui = Ui_SearchWidget()
    ui.setupUi(SearchWidget)
    SearchWidget.show()
    sys.exit(app.exec_())

