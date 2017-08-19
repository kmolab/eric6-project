# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\PluginManager\PluginUninstallDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PluginUninstallDialog(object):
    def setupUi(self, PluginUninstallDialog):
        PluginUninstallDialog.setObjectName("PluginUninstallDialog")
        PluginUninstallDialog.resize(400, 131)
        self.vboxlayout = QtWidgets.QVBoxLayout(PluginUninstallDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label_3 = QtWidgets.QLabel(PluginUninstallDialog)
        self.label_3.setObjectName("label_3")
        self.vboxlayout.addWidget(self.label_3)
        self.pluginDirectoryCombo = QtWidgets.QComboBox(PluginUninstallDialog)
        self.pluginDirectoryCombo.setObjectName("pluginDirectoryCombo")
        self.vboxlayout.addWidget(self.pluginDirectoryCombo)
        self.label_2 = QtWidgets.QLabel(PluginUninstallDialog)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)
        self.pluginNameCombo = QtWidgets.QComboBox(PluginUninstallDialog)
        self.pluginNameCombo.setObjectName("pluginNameCombo")
        self.vboxlayout.addWidget(self.pluginNameCombo)
        self.buttonBox = QtWidgets.QDialogButtonBox(PluginUninstallDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PluginUninstallDialog)
        QtCore.QMetaObject.connectSlotsByName(PluginUninstallDialog)
        PluginUninstallDialog.setTabOrder(self.pluginDirectoryCombo, self.pluginNameCombo)
        PluginUninstallDialog.setTabOrder(self.pluginNameCombo, self.buttonBox)

    def retranslateUi(self, PluginUninstallDialog):
        _translate = QtCore.QCoreApplication.translate
        PluginUninstallDialog.setWindowTitle(_translate("PluginUninstallDialog", "Plugin Uninstallation"))
        self.label_3.setText(_translate("PluginUninstallDialog", "Plugin directory:"))
        self.pluginDirectoryCombo.setToolTip(_translate("PluginUninstallDialog", "Select the plugin area containing the plugin to uninstall"))
        self.label_2.setText(_translate("PluginUninstallDialog", "Plugin:"))
        self.pluginNameCombo.setToolTip(_translate("PluginUninstallDialog", "Select the plugin to uninstall"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PluginUninstallDialog = QtWidgets.QWidget()
    ui = Ui_PluginUninstallDialog()
    ui.setupUi(PluginUninstallDialog)
    PluginUninstallDialog.show()
    sys.exit(app.exec_())

