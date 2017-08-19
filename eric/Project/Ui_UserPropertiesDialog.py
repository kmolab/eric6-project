# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Project\UserPropertiesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserPropertiesDialog(object):
    def setupUi(self, UserPropertiesDialog):
        UserPropertiesDialog.setObjectName("UserPropertiesDialog")
        UserPropertiesDialog.resize(543, 182)
        UserPropertiesDialog.setSizeGripEnabled(True)
        self._2 = QtWidgets.QVBoxLayout(UserPropertiesDialog)
        self._2.setObjectName("_2")
        self.groupBox_2 = QtWidgets.QGroupBox(UserPropertiesDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self._3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self._3.setObjectName("_3")
        self.vcsStatusMonitorIntervalSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.vcsStatusMonitorIntervalSpinBox.setMaximum(3600)
        self.vcsStatusMonitorIntervalSpinBox.setObjectName("vcsStatusMonitorIntervalSpinBox")
        self._3.addWidget(self.vcsStatusMonitorIntervalSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._3.addItem(spacerItem)
        self._2.addWidget(self.groupBox_2)
        self.vcsGroup = QtWidgets.QGroupBox(UserPropertiesDialog)
        self.vcsGroup.setObjectName("vcsGroup")
        self._4 = QtWidgets.QVBoxLayout(self.vcsGroup)
        self._4.setObjectName("_4")
        self.vcsInterfaceCombo = QtWidgets.QComboBox(self.vcsGroup)
        self.vcsInterfaceCombo.setObjectName("vcsInterfaceCombo")
        self._4.addWidget(self.vcsInterfaceCombo)
        self.vcsInterfaceDefaultCheckBox = QtWidgets.QCheckBox(self.vcsGroup)
        self.vcsInterfaceDefaultCheckBox.setObjectName("vcsInterfaceDefaultCheckBox")
        self._4.addWidget(self.vcsInterfaceDefaultCheckBox)
        self._2.addWidget(self.vcsGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(UserPropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self._2.addWidget(self.buttonBox)

        self.retranslateUi(UserPropertiesDialog)
        self.buttonBox.accepted.connect(UserPropertiesDialog.accept)
        self.buttonBox.rejected.connect(UserPropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UserPropertiesDialog)
        UserPropertiesDialog.setTabOrder(self.vcsStatusMonitorIntervalSpinBox, self.vcsInterfaceCombo)
        UserPropertiesDialog.setTabOrder(self.vcsInterfaceCombo, self.vcsInterfaceDefaultCheckBox)
        UserPropertiesDialog.setTabOrder(self.vcsInterfaceDefaultCheckBox, self.buttonBox)

    def retranslateUi(self, UserPropertiesDialog):
        _translate = QtCore.QCoreApplication.translate
        UserPropertiesDialog.setWindowTitle(_translate("UserPropertiesDialog", "User Project Properties"))
        UserPropertiesDialog.setWhatsThis(_translate("UserPropertiesDialog", "<b>User Project Properties</b>\n"
"<p>This dialog is used to show and edit the user specific project properties.</p>"))
        self.groupBox_2.setTitle(_translate("UserPropertiesDialog", "VCS Status Monitor"))
        self.vcsStatusMonitorIntervalSpinBox.setToolTip(_translate("UserPropertiesDialog", "Select the interval in seconds for VCS status updates (0 to disable)"))
        self.vcsStatusMonitorIntervalSpinBox.setSuffix(_translate("UserPropertiesDialog", " sec"))
        self.vcsGroup.setTitle(_translate("UserPropertiesDialog", "VCS Interface"))
        self.vcsInterfaceCombo.setToolTip(_translate("UserPropertiesDialog", "Select the vcs interface to be used"))
        self.vcsInterfaceDefaultCheckBox.setToolTip(_translate("UserPropertiesDialog", "Select to make the interface selection the default for the project"))
        self.vcsInterfaceDefaultCheckBox.setText(_translate("UserPropertiesDialog", "Make interface selection the default"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserPropertiesDialog = QtWidgets.QDialog()
    ui = Ui_UserPropertiesDialog()
    ui.setupUi(UserPropertiesDialog)
    UserPropertiesDialog.show()
    sys.exit(app.exec_())

