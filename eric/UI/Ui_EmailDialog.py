# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\UI\EmailDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EmailDialog(object):
    def setupUi(self, EmailDialog):
        EmailDialog.setObjectName("EmailDialog")
        EmailDialog.resize(600, 547)
        EmailDialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EmailDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainSplitter = QtWidgets.QSplitter(EmailDialog)
        self.mainSplitter.setOrientation(QtCore.Qt.Vertical)
        self.mainSplitter.setObjectName("mainSplitter")
        self.messageGroup = QtWidgets.QGroupBox(self.mainSplitter)
        self.messageGroup.setObjectName("messageGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.messageGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.textLabel1 = QtWidgets.QLabel(self.messageGroup)
        self.textLabel1.setObjectName("textLabel1")
        self.hboxlayout.addWidget(self.textLabel1)
        self.subject = QtWidgets.QLineEdit(self.messageGroup)
        self.subject.setObjectName("subject")
        self.hboxlayout.addWidget(self.subject)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.msgLabel = QtWidgets.QLabel(self.messageGroup)
        self.msgLabel.setObjectName("msgLabel")
        self.verticalLayout.addWidget(self.msgLabel)
        self.message = QtWidgets.QTextEdit(self.messageGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setLineWrapMode(QtWidgets.QTextEdit.FixedColumnWidth)
        self.message.setLineWrapColumnOrWidth(70)
        self.message.setTabStopWidth(8)
        self.message.setAcceptRichText(False)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.attachmentsGroup = QtWidgets.QGroupBox(self.mainSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachmentsGroup.sizePolicy().hasHeightForWidth())
        self.attachmentsGroup.setSizePolicy(sizePolicy)
        self.attachmentsGroup.setObjectName("attachmentsGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.attachmentsGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.attachments = QtWidgets.QTreeWidget(self.attachmentsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.attachments.sizePolicy().hasHeightForWidth())
        self.attachments.setSizePolicy(sizePolicy)
        self.attachments.setAlternatingRowColors(True)
        self.attachments.setRootIsDecorated(False)
        self.attachments.setObjectName("attachments")
        self.gridLayout.addWidget(self.attachments, 0, 0, 1, 1)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.addButton = QtWidgets.QPushButton(self.attachmentsGroup)
        self.addButton.setObjectName("addButton")
        self.vboxlayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(self.attachmentsGroup)
        self.deleteButton.setObjectName("deleteButton")
        self.vboxlayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.vboxlayout, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.mainSplitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(EmailDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.textLabel1.setBuddy(self.subject)
        self.msgLabel.setBuddy(self.message)

        self.retranslateUi(EmailDialog)
        QtCore.QMetaObject.connectSlotsByName(EmailDialog)
        EmailDialog.setTabOrder(self.subject, self.message)
        EmailDialog.setTabOrder(self.message, self.addButton)
        EmailDialog.setTabOrder(self.addButton, self.attachments)
        EmailDialog.setTabOrder(self.attachments, self.deleteButton)

    def retranslateUi(self, EmailDialog):
        _translate = QtCore.QCoreApplication.translate
        EmailDialog.setWindowTitle(_translate("EmailDialog", "Send bug report"))
        self.messageGroup.setTitle(_translate("EmailDialog", "Message"))
        self.textLabel1.setText(_translate("EmailDialog", "&Subject:"))
        self.subject.setToolTip(_translate("EmailDialog", "Enter the subject"))
        self.attachmentsGroup.setTitle(_translate("EmailDialog", "Attachments"))
        self.attachments.headerItem().setText(0, _translate("EmailDialog", "Name"))
        self.attachments.headerItem().setText(1, _translate("EmailDialog", "Type"))
        self.addButton.setToolTip(_translate("EmailDialog", "Press to add an attachment"))
        self.addButton.setText(_translate("EmailDialog", "&Add..."))
        self.addButton.setShortcut(_translate("EmailDialog", "Alt+A"))
        self.deleteButton.setToolTip(_translate("EmailDialog", "Delete the selected entry from the list of attachments"))
        self.deleteButton.setText(_translate("EmailDialog", "&Delete"))
        self.deleteButton.setShortcut(_translate("EmailDialog", "Alt+D"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EmailDialog = QtWidgets.QDialog()
    ui = Ui_EmailDialog()
    ui.setupUi(EmailDialog)
    EmailDialog.show()
    sys.exit(app.exec_())

