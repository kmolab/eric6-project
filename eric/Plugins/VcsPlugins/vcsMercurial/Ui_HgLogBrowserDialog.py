# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HgLogBrowserDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgLogBrowserDialog(object):
    def setupUi(self, HgLogBrowserDialog):
        HgLogBrowserDialog.setObjectName("HgLogBrowserDialog")
        HgLogBrowserDialog.resize(1000, 800)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(HgLogBrowserDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.actionsButton = QtWidgets.QToolButton(HgLogBrowserDialog)
        self.actionsButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.actionsButton.setObjectName("actionsButton")
        self.horizontalLayout_2.addWidget(self.actionsButton)
        self.line_5 = QtWidgets.QFrame(HgLogBrowserDialog)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.modeComboBox = QtWidgets.QComboBox(HgLogBrowserDialog)
        self.modeComboBox.setObjectName("modeComboBox")
        self.horizontalLayout_2.addWidget(self.modeComboBox)
        self.line_4 = QtWidgets.QFrame(HgLogBrowserDialog)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.label = QtWidgets.QLabel(HgLogBrowserDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.fromDate = QtWidgets.QDateEdit(HgLogBrowserDialog)
        self.fromDate.setCalendarPopup(True)
        self.fromDate.setObjectName("fromDate")
        self.horizontalLayout_2.addWidget(self.fromDate)
        self.label_2 = QtWidgets.QLabel(HgLogBrowserDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.toDate = QtWidgets.QDateEdit(HgLogBrowserDialog)
        self.toDate.setCalendarPopup(True)
        self.toDate.setObjectName("toDate")
        self.horizontalLayout_2.addWidget(self.toDate)
        self.line_2 = QtWidgets.QFrame(HgLogBrowserDialog)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(HgLogBrowserDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.branchCombo = QtWidgets.QComboBox(HgLogBrowserDialog)
        self.branchCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.branchCombo.setObjectName("branchCombo")
        self.horizontalLayout_2.addWidget(self.branchCombo)
        self.line_3 = QtWidgets.QFrame(HgLogBrowserDialog)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.fieldCombo = QtWidgets.QComboBox(HgLogBrowserDialog)
        self.fieldCombo.setObjectName("fieldCombo")
        self.horizontalLayout_2.addWidget(self.fieldCombo)
        self.rxEdit = E5ClearableLineEdit(HgLogBrowserDialog)
        self.rxEdit.setObjectName("rxEdit")
        self.horizontalLayout_2.addWidget(self.rxEdit)
        self.findPrevButton = QtWidgets.QToolButton(HgLogBrowserDialog)
        self.findPrevButton.setObjectName("findPrevButton")
        self.horizontalLayout_2.addWidget(self.findPrevButton)
        self.findNextButton = QtWidgets.QToolButton(HgLogBrowserDialog)
        self.findNextButton.setObjectName("findNextButton")
        self.horizontalLayout_2.addWidget(self.findNextButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.mainSplitter = QtWidgets.QSplitter(HgLogBrowserDialog)
        self.mainSplitter.setOrientation(QtCore.Qt.Vertical)
        self.mainSplitter.setObjectName("mainSplitter")
        self.layoutWidget = QtWidgets.QWidget(self.mainSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logTree = QtWidgets.QTreeWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.logTree.sizePolicy().hasHeightForWidth())
        self.logTree.setSizePolicy(sizePolicy)
        self.logTree.setAlternatingRowColors(True)
        self.logTree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.logTree.setRootIsDecorated(False)
        self.logTree.setItemsExpandable(False)
        self.logTree.setAllColumnsShowFocus(True)
        self.logTree.setObjectName("logTree")
        self.verticalLayout_2.addWidget(self.logTree)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.upButton = QtWidgets.QToolButton(self.layoutWidget)
        self.upButton.setAutoRepeat(True)
        self.upButton.setObjectName("upButton")
        self.horizontalLayout_3.addWidget(self.upButton)
        self.downButton = QtWidgets.QToolButton(self.layoutWidget)
        self.downButton.setAutoRepeat(True)
        self.downButton.setObjectName("downButton")
        self.horizontalLayout_3.addWidget(self.downButton)
        self.line_6 = QtWidgets.QFrame(self.layoutWidget)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_3.addWidget(self.line_6)
        self.nextButton = QtWidgets.QPushButton(self.layoutWidget)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_3.addWidget(self.nextButton)
        self.limitSpinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.limitSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.limitSpinBox.setMinimum(1)
        self.limitSpinBox.setMaximum(10000)
        self.limitSpinBox.setProperty("value", 20)
        self.limitSpinBox.setObjectName("limitSpinBox")
        self.horizontalLayout_3.addWidget(self.limitSpinBox)
        self.stopCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.stopCheckBox.setObjectName("stopCheckBox")
        self.horizontalLayout_3.addWidget(self.stopCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.sbsSelectLabel = QtWidgets.QLabel(self.layoutWidget)
        self.sbsSelectLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sbsSelectLabel.setText("")
        self.sbsSelectLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.sbsSelectLabel.setObjectName("sbsSelectLabel")
        self.horizontalLayout_3.addWidget(self.sbsSelectLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.detailsSplitter = QtWidgets.QSplitter(self.mainSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.detailsSplitter.sizePolicy().hasHeightForWidth())
        self.detailsSplitter.setSizePolicy(sizePolicy)
        self.detailsSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.detailsSplitter.setObjectName("detailsSplitter")
        self.detailsEdit = QtWidgets.QTextBrowser(self.detailsSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.detailsEdit.sizePolicy().hasHeightForWidth())
        self.detailsEdit.setSizePolicy(sizePolicy)
        self.detailsEdit.setReadOnly(True)
        self.detailsEdit.setOpenLinks(False)
        self.detailsEdit.setObjectName("detailsEdit")
        self.diffSplitter = QtWidgets.QSplitter(self.detailsSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diffSplitter.sizePolicy().hasHeightForWidth())
        self.diffSplitter.setSizePolicy(sizePolicy)
        self.diffSplitter.setOrientation(QtCore.Qt.Vertical)
        self.diffSplitter.setObjectName("diffSplitter")
        self.filesTree = QtWidgets.QTreeWidget(self.diffSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.filesTree.sizePolicy().hasHeightForWidth())
        self.filesTree.setSizePolicy(sizePolicy)
        self.filesTree.setAlternatingRowColors(True)
        self.filesTree.setRootIsDecorated(False)
        self.filesTree.setItemsExpandable(False)
        self.filesTree.setAllColumnsShowFocus(True)
        self.filesTree.setObjectName("filesTree")
        self.layoutWidget1 = QtWidgets.QWidget(self.diffSplitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.diffLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.diffLabel.setObjectName("diffLabel")
        self.horizontalLayout.addWidget(self.diffLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.diffSelectLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.diffSelectLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.diffSelectLabel.setText("")
        self.diffSelectLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.diffSelectLabel.setObjectName("diffSelectLabel")
        self.horizontalLayout.addWidget(self.diffSelectLabel)
        self.saveLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.saveLabel.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.saveLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.saveLabel.setObjectName("saveLabel")
        self.horizontalLayout.addWidget(self.saveLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.diffEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.diffEdit.sizePolicy().hasHeightForWidth())
        self.diffEdit.setSizePolicy(sizePolicy)
        self.diffEdit.setTabChangesFocus(True)
        self.diffEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.diffEdit.setReadOnly(True)
        self.diffEdit.setAcceptRichText(False)
        self.diffEdit.setObjectName("diffEdit")
        self.verticalLayout.addWidget(self.diffEdit)
        self.verticalLayout_3.addWidget(self.mainSplitter)
        self.errorGroup = QtWidgets.QGroupBox(HgLogBrowserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout.addWidget(self.errors)
        self.verticalLayout_3.addWidget(self.errorGroup)
        self.inputGroup = QtWidgets.QGroupBox(HgLogBrowserDialog)
        self.inputGroup.setObjectName("inputGroup")
        self.gridlayout = QtWidgets.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem2 = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.inputGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgLogBrowserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(HgLogBrowserDialog)
        QtCore.QMetaObject.connectSlotsByName(HgLogBrowserDialog)
        HgLogBrowserDialog.setTabOrder(self.actionsButton, self.modeComboBox)
        HgLogBrowserDialog.setTabOrder(self.modeComboBox, self.fromDate)
        HgLogBrowserDialog.setTabOrder(self.fromDate, self.toDate)
        HgLogBrowserDialog.setTabOrder(self.toDate, self.branchCombo)
        HgLogBrowserDialog.setTabOrder(self.branchCombo, self.fieldCombo)
        HgLogBrowserDialog.setTabOrder(self.fieldCombo, self.rxEdit)
        HgLogBrowserDialog.setTabOrder(self.rxEdit, self.findPrevButton)
        HgLogBrowserDialog.setTabOrder(self.findPrevButton, self.findNextButton)
        HgLogBrowserDialog.setTabOrder(self.findNextButton, self.logTree)
        HgLogBrowserDialog.setTabOrder(self.logTree, self.upButton)
        HgLogBrowserDialog.setTabOrder(self.upButton, self.downButton)
        HgLogBrowserDialog.setTabOrder(self.downButton, self.nextButton)
        HgLogBrowserDialog.setTabOrder(self.nextButton, self.limitSpinBox)
        HgLogBrowserDialog.setTabOrder(self.limitSpinBox, self.stopCheckBox)
        HgLogBrowserDialog.setTabOrder(self.stopCheckBox, self.sbsSelectLabel)
        HgLogBrowserDialog.setTabOrder(self.sbsSelectLabel, self.detailsEdit)
        HgLogBrowserDialog.setTabOrder(self.detailsEdit, self.filesTree)
        HgLogBrowserDialog.setTabOrder(self.filesTree, self.diffSelectLabel)
        HgLogBrowserDialog.setTabOrder(self.diffSelectLabel, self.saveLabel)
        HgLogBrowserDialog.setTabOrder(self.saveLabel, self.diffEdit)
        HgLogBrowserDialog.setTabOrder(self.diffEdit, self.errors)
        HgLogBrowserDialog.setTabOrder(self.errors, self.input)
        HgLogBrowserDialog.setTabOrder(self.input, self.passwordCheckBox)
        HgLogBrowserDialog.setTabOrder(self.passwordCheckBox, self.sendButton)

    def retranslateUi(self, HgLogBrowserDialog):
        _translate = QtCore.QCoreApplication.translate
        HgLogBrowserDialog.setWindowTitle(_translate("HgLogBrowserDialog", "Mercurial Log"))
        self.actionsButton.setToolTip(_translate("HgLogBrowserDialog", "Select action from menu"))
        self.modeComboBox.setToolTip(_translate("HgLogBrowserDialog", "Select the mode (find or filter)"))
        self.label.setText(_translate("HgLogBrowserDialog", "From:"))
        self.fromDate.setToolTip(_translate("HgLogBrowserDialog", "Enter the start date"))
        self.label_2.setText(_translate("HgLogBrowserDialog", "To:"))
        self.toDate.setToolTip(_translate("HgLogBrowserDialog", "Enter the end date"))
        self.label_3.setText(_translate("HgLogBrowserDialog", "Branch:"))
        self.branchCombo.setToolTip(_translate("HgLogBrowserDialog", "Select the branch to filter on"))
        self.fieldCombo.setToolTip(_translate("HgLogBrowserDialog", "Select the field to filter on"))
        self.rxEdit.setToolTip(_translate("HgLogBrowserDialog", "Enter the regular expression to filter on or search for"))
        self.findPrevButton.setToolTip(_translate("HgLogBrowserDialog", "Press to find the previous occurrence"))
        self.findNextButton.setToolTip(_translate("HgLogBrowserDialog", "Press to find the next occurrence"))
        self.logTree.headerItem().setText(0, _translate("HgLogBrowserDialog", "Graph"))
        self.logTree.headerItem().setText(1, _translate("HgLogBrowserDialog", "Branch"))
        self.logTree.headerItem().setText(2, _translate("HgLogBrowserDialog", "Revision"))
        self.logTree.headerItem().setText(3, _translate("HgLogBrowserDialog", "Phase"))
        self.logTree.headerItem().setText(4, _translate("HgLogBrowserDialog", "Author"))
        self.logTree.headerItem().setText(5, _translate("HgLogBrowserDialog", "Date"))
        self.logTree.headerItem().setText(6, _translate("HgLogBrowserDialog", "Message"))
        self.logTree.headerItem().setText(7, _translate("HgLogBrowserDialog", "Tags"))
        self.upButton.setToolTip(_translate("HgLogBrowserDialog", "Press to move up in the log list"))
        self.downButton.setToolTip(_translate("HgLogBrowserDialog", "Press to move down in the log list"))
        self.nextButton.setToolTip(_translate("HgLogBrowserDialog", "Press to get the next bunch of log entries"))
        self.nextButton.setText(_translate("HgLogBrowserDialog", "&Next"))
        self.limitSpinBox.setToolTip(_translate("HgLogBrowserDialog", "Enter the limit of entries to fetch"))
        self.stopCheckBox.setToolTip(_translate("HgLogBrowserDialog", "Select to stop listing log messages at a copy or move"))
        self.stopCheckBox.setText(_translate("HgLogBrowserDialog", "Stop on Copy/Move"))
        self.filesTree.setSortingEnabled(True)
        self.filesTree.headerItem().setText(0, _translate("HgLogBrowserDialog", "Action"))
        self.filesTree.headerItem().setText(1, _translate("HgLogBrowserDialog", "Path"))
        self.filesTree.headerItem().setText(2, _translate("HgLogBrowserDialog", "Copy from"))
        self.diffLabel.setText(_translate("HgLogBrowserDialog", "Differences"))
        self.saveLabel.setText(_translate("HgLogBrowserDialog", "<a href=\"save:me\">Save</a>"))
        self.errorGroup.setTitle(_translate("HgLogBrowserDialog", "Errors"))
        self.errors.setWhatsThis(_translate("HgLogBrowserDialog", "<b>Mercurial log errors</b><p>This shows possible error messages of the hg log command.</p>"))
        self.inputGroup.setTitle(_translate("HgLogBrowserDialog", "Input"))
        self.sendButton.setToolTip(_translate("HgLogBrowserDialog", "Press to send the input to the hg process"))
        self.sendButton.setText(_translate("HgLogBrowserDialog", "&Send"))
        self.sendButton.setShortcut(_translate("HgLogBrowserDialog", "Alt+S"))
        self.input.setToolTip(_translate("HgLogBrowserDialog", "Enter data to be sent to the hg process"))
        self.passwordCheckBox.setToolTip(_translate("HgLogBrowserDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("HgLogBrowserDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("HgLogBrowserDialog", "Alt+P"))

from E5Gui.E5LineEdit import E5ClearableLineEdit

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgLogBrowserDialog = QtWidgets.QWidget()
    ui = Ui_HgLogBrowserDialog()
    ui.setupUi(HgLogBrowserDialog)
    HgLogBrowserDialog.show()
    sys.exit(app.exec_())
