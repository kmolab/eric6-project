# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\DocumentationPlugins\Ericdoc\EricdocExecDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EricdocExecDialog(object):
    def setupUi(self, EricdocExecDialog):
        EricdocExecDialog.setObjectName("EricdocExecDialog")
        EricdocExecDialog.resize(753, 602)
        EricdocExecDialog.setSizeGripEnabled(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(EricdocExecDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messagesGroup = QtWidgets.QGroupBox(EricdocExecDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.messagesGroup.sizePolicy().hasHeightForWidth())
        self.messagesGroup.setSizePolicy(sizePolicy)
        self.messagesGroup.setObjectName("messagesGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.messagesGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.contents = QtWidgets.QTextBrowser(self.messagesGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.contents.sizePolicy().hasHeightForWidth())
        self.contents.setSizePolicy(sizePolicy)
        self.contents.setObjectName("contents")
        self.verticalLayout.addWidget(self.contents)
        self.verticalLayout_3.addWidget(self.messagesGroup)
        self.errorGroup = QtWidgets.QGroupBox(EricdocExecDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.errorGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.errors = QtWidgets.QTextBrowser(self.errorGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errors.sizePolicy().hasHeightForWidth())
        self.errors.setSizePolicy(sizePolicy)
        self.errors.setObjectName("errors")
        self.verticalLayout_2.addWidget(self.errors)
        self.verticalLayout_3.addWidget(self.errorGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(EricdocExecDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(EricdocExecDialog)
        QtCore.QMetaObject.connectSlotsByName(EricdocExecDialog)
        EricdocExecDialog.setTabOrder(self.contents, self.errors)
        EricdocExecDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, EricdocExecDialog):
        _translate = QtCore.QCoreApplication.translate
        EricdocExecDialog.setWindowTitle(_translate("EricdocExecDialog", "Ericdoc"))
        self.messagesGroup.setTitle(_translate("EricdocExecDialog", "Messages"))
        self.contents.setWhatsThis(_translate("EricdocExecDialog", "<b>Ericdoc Execution</b>\n"
"<p>This shows the output of the Ericdoc generator command.</p>"))
        self.errorGroup.setTitle(_translate("EricdocExecDialog", "Errors"))
        self.errors.setWhatsThis(_translate("EricdocExecDialog", "<b>Ericdoc Execution</b>\n"
"<p>This shows the errors of the Ericdoc generator command.</p>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EricdocExecDialog = QtWidgets.QDialog()
    ui = Ui_EricdocExecDialog()
    ui.setupUi(EricdocExecDialog)
    EricdocExecDialog.show()
    sys.exit(app.exec_())

