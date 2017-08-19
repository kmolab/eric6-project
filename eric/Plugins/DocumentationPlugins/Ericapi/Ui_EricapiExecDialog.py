# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\DocumentationPlugins\Ericapi\EricapiExecDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EricapiExecDialog(object):
    def setupUi(self, EricapiExecDialog):
        EricapiExecDialog.setObjectName("EricapiExecDialog")
        EricapiExecDialog.resize(753, 602)
        EricapiExecDialog.setSizeGripEnabled(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(EricapiExecDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messagesGroup = QtWidgets.QGroupBox(EricapiExecDialog)
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
        self.errorGroup = QtWidgets.QGroupBox(EricapiExecDialog)
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
        self.buttonBox = QtWidgets.QDialogButtonBox(EricapiExecDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(EricapiExecDialog)
        QtCore.QMetaObject.connectSlotsByName(EricapiExecDialog)
        EricapiExecDialog.setTabOrder(self.contents, self.errors)
        EricapiExecDialog.setTabOrder(self.errors, self.buttonBox)

    def retranslateUi(self, EricapiExecDialog):
        _translate = QtCore.QCoreApplication.translate
        EricapiExecDialog.setWindowTitle(_translate("EricapiExecDialog", "Ericapi"))
        self.messagesGroup.setTitle(_translate("EricapiExecDialog", "Messages"))
        self.contents.setWhatsThis(_translate("EricapiExecDialog", "<b>Ericapi Execution</b>\n"
"<p>This shows the output of the Ericapi generator command.</p>"))
        self.errorGroup.setTitle(_translate("EricapiExecDialog", "Errors"))
        self.errors.setWhatsThis(_translate("EricapiExecDialog", "<b>Ericapi Execution</b>\n"
"<p>This shows the errors of the Ericapi generator command.</p>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EricapiExecDialog = QtWidgets.QDialog()
    ui = Ui_EricapiExecDialog()
    ui.setupUi(EricapiExecDialog)
    EricapiExecDialog.show()
    sys.exit(app.exec_())

