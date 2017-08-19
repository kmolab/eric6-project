# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\PluginManager\PluginInfoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PluginInfoDialog(object):
    def setupUi(self, PluginInfoDialog):
        PluginInfoDialog.setObjectName("PluginInfoDialog")
        PluginInfoDialog.resize(800, 600)
        PluginInfoDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(PluginInfoDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(PluginInfoDialog)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.pluginList = QtWidgets.QTreeWidget(PluginInfoDialog)
        self.pluginList.setRootIsDecorated(False)
        self.pluginList.setItemsExpandable(False)
        self.pluginList.setAllColumnsShowFocus(True)
        self.pluginList.setObjectName("pluginList")
        self.vboxlayout.addWidget(self.pluginList)
        self.buttonBox = QtWidgets.QDialogButtonBox(PluginInfoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PluginInfoDialog)
        self.buttonBox.accepted.connect(PluginInfoDialog.accept)
        self.buttonBox.rejected.connect(PluginInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginInfoDialog)
        PluginInfoDialog.setTabOrder(self.pluginList, self.buttonBox)

    def retranslateUi(self, PluginInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        PluginInfoDialog.setWindowTitle(_translate("PluginInfoDialog", "Loaded Plugins"))
        self.label.setText(_translate("PluginInfoDialog", "Double-Click an entry to show detailed info. Plugins with an error are shown in red."))
        self.pluginList.setWhatsThis(_translate("PluginInfoDialog", "<b>Plugin List</b><p>This lists all loaded plugins. Double-clicking an entry shows more detailed information in a separate dialog.</p>"))
        self.pluginList.setSortingEnabled(True)
        self.pluginList.headerItem().setText(0, _translate("PluginInfoDialog", "Module"))
        self.pluginList.headerItem().setText(1, _translate("PluginInfoDialog", "Name"))
        self.pluginList.headerItem().setText(2, _translate("PluginInfoDialog", "Version"))
        self.pluginList.headerItem().setText(3, _translate("PluginInfoDialog", "Autoactivate"))
        self.pluginList.headerItem().setText(4, _translate("PluginInfoDialog", "Active"))
        self.pluginList.headerItem().setText(5, _translate("PluginInfoDialog", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PluginInfoDialog = QtWidgets.QDialog()
    ui = Ui_PluginInfoDialog()
    ui.setupUi(PluginInfoDialog)
    PluginInfoDialog.show()
    sys.exit(app.exec_())

