# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\E5Network\E5SslCertificatesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_E5SslCertificatesDialog(object):
    def setupUi(self, E5SslCertificatesDialog):
        E5SslCertificatesDialog.setObjectName("E5SslCertificatesDialog")
        E5SslCertificatesDialog.resize(760, 440)
        E5SslCertificatesDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(E5SslCertificatesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.certificatesWidget = QtWidgets.QTabWidget(E5SslCertificatesDialog)
        self.certificatesWidget.setObjectName("certificatesWidget")
        self.serversTab = QtWidgets.QWidget()
        self.serversTab.setObjectName("serversTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.serversTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.serversTab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.serversCertificatesTree = QtWidgets.QTreeWidget(self.serversTab)
        self.serversCertificatesTree.setObjectName("serversCertificatesTree")
        self.verticalLayout_2.addWidget(self.serversCertificatesTree)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serversViewButton = QtWidgets.QPushButton(self.serversTab)
        self.serversViewButton.setEnabled(False)
        self.serversViewButton.setObjectName("serversViewButton")
        self.horizontalLayout.addWidget(self.serversViewButton)
        self.serversImportButton = QtWidgets.QPushButton(self.serversTab)
        self.serversImportButton.setObjectName("serversImportButton")
        self.horizontalLayout.addWidget(self.serversImportButton)
        self.serversExportButton = QtWidgets.QPushButton(self.serversTab)
        self.serversExportButton.setEnabled(False)
        self.serversExportButton.setObjectName("serversExportButton")
        self.horizontalLayout.addWidget(self.serversExportButton)
        self.serversDeleteButton = QtWidgets.QPushButton(self.serversTab)
        self.serversDeleteButton.setEnabled(False)
        self.serversDeleteButton.setObjectName("serversDeleteButton")
        self.horizontalLayout.addWidget(self.serversDeleteButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.certificatesWidget.addTab(self.serversTab, "")
        self.caTab = QtWidgets.QWidget()
        self.caTab.setObjectName("caTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.caTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.caTab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.caCertificatesTree = QtWidgets.QTreeWidget(self.caTab)
        self.caCertificatesTree.setObjectName("caCertificatesTree")
        self.verticalLayout_3.addWidget(self.caCertificatesTree)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.caViewButton = QtWidgets.QPushButton(self.caTab)
        self.caViewButton.setEnabled(False)
        self.caViewButton.setObjectName("caViewButton")
        self.horizontalLayout_2.addWidget(self.caViewButton)
        self.caImportButton = QtWidgets.QPushButton(self.caTab)
        self.caImportButton.setObjectName("caImportButton")
        self.horizontalLayout_2.addWidget(self.caImportButton)
        self.caExportButton = QtWidgets.QPushButton(self.caTab)
        self.caExportButton.setEnabled(False)
        self.caExportButton.setObjectName("caExportButton")
        self.horizontalLayout_2.addWidget(self.caExportButton)
        self.caDeleteButton = QtWidgets.QPushButton(self.caTab)
        self.caDeleteButton.setEnabled(False)
        self.caDeleteButton.setObjectName("caDeleteButton")
        self.horizontalLayout_2.addWidget(self.caDeleteButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.certificatesWidget.addTab(self.caTab, "")
        self.verticalLayout.addWidget(self.certificatesWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(E5SslCertificatesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(E5SslCertificatesDialog)
        self.certificatesWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(E5SslCertificatesDialog.accept)
        self.buttonBox.rejected.connect(E5SslCertificatesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(E5SslCertificatesDialog)
        E5SslCertificatesDialog.setTabOrder(self.certificatesWidget, self.serversCertificatesTree)
        E5SslCertificatesDialog.setTabOrder(self.serversCertificatesTree, self.serversViewButton)
        E5SslCertificatesDialog.setTabOrder(self.serversViewButton, self.serversImportButton)
        E5SslCertificatesDialog.setTabOrder(self.serversImportButton, self.serversExportButton)
        E5SslCertificatesDialog.setTabOrder(self.serversExportButton, self.serversDeleteButton)
        E5SslCertificatesDialog.setTabOrder(self.serversDeleteButton, self.caCertificatesTree)
        E5SslCertificatesDialog.setTabOrder(self.caCertificatesTree, self.caViewButton)
        E5SslCertificatesDialog.setTabOrder(self.caViewButton, self.caImportButton)
        E5SslCertificatesDialog.setTabOrder(self.caImportButton, self.caExportButton)
        E5SslCertificatesDialog.setTabOrder(self.caExportButton, self.caDeleteButton)
        E5SslCertificatesDialog.setTabOrder(self.caDeleteButton, self.buttonBox)

    def retranslateUi(self, E5SslCertificatesDialog):
        _translate = QtCore.QCoreApplication.translate
        E5SslCertificatesDialog.setWindowTitle(_translate("E5SslCertificatesDialog", "SSL Certificate Manager"))
        self.label.setText(_translate("E5SslCertificatesDialog", "You have saved certificates identifying these servers:"))
        self.serversCertificatesTree.headerItem().setText(0, _translate("E5SslCertificatesDialog", "Certificate name"))
        self.serversCertificatesTree.headerItem().setText(1, _translate("E5SslCertificatesDialog", "Server"))
        self.serversCertificatesTree.headerItem().setText(2, _translate("E5SslCertificatesDialog", "Expiry Date"))
        self.serversViewButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to view the selected certificate"))
        self.serversViewButton.setText(_translate("E5SslCertificatesDialog", "&View..."))
        self.serversImportButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to import a certificate"))
        self.serversImportButton.setText(_translate("E5SslCertificatesDialog", "&Import..."))
        self.serversExportButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to export the selected certificate"))
        self.serversExportButton.setText(_translate("E5SslCertificatesDialog", "&Export..."))
        self.serversDeleteButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to delete the selected certificate"))
        self.serversDeleteButton.setText(_translate("E5SslCertificatesDialog", "&Delete..."))
        self.certificatesWidget.setTabText(self.certificatesWidget.indexOf(self.serversTab), _translate("E5SslCertificatesDialog", "&Servers"))
        self.label_2.setText(_translate("E5SslCertificatesDialog", "You have saved certificates identifying these certification authorities:"))
        self.caCertificatesTree.headerItem().setText(0, _translate("E5SslCertificatesDialog", "Certificate name"))
        self.caCertificatesTree.headerItem().setText(1, _translate("E5SslCertificatesDialog", "Expiry Date"))
        self.caViewButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to view the selected certificate"))
        self.caViewButton.setText(_translate("E5SslCertificatesDialog", "&View..."))
        self.caImportButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to import a certificate"))
        self.caImportButton.setText(_translate("E5SslCertificatesDialog", "&Import..."))
        self.caExportButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to export the selected certificate"))
        self.caExportButton.setText(_translate("E5SslCertificatesDialog", "&Export..."))
        self.caDeleteButton.setToolTip(_translate("E5SslCertificatesDialog", "Press to delete the selected certificate"))
        self.caDeleteButton.setText(_translate("E5SslCertificatesDialog", "&Delete..."))
        self.certificatesWidget.setTabText(self.certificatesWidget.indexOf(self.caTab), _translate("E5SslCertificatesDialog", "Certificate &Authorities"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    E5SslCertificatesDialog = QtWidgets.QDialog()
    ui = Ui_E5SslCertificatesDialog()
    ui.setupUi(E5SslCertificatesDialog)
    E5SslCertificatesDialog.show()
    sys.exit(app.exec_())

