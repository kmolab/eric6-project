# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\MultiProjectPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MultiProjectPage(object):
    def setupUi(self, MultiProjectPage):
        MultiProjectPage.setObjectName("MultiProjectPage")
        MultiProjectPage.resize(494, 362)
        self.verticalLayout = QtWidgets.QVBoxLayout(MultiProjectPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(MultiProjectPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line8 = QtWidgets.QFrame(MultiProjectPage)
        self.line8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line8.setObjectName("line8")
        self.verticalLayout.addWidget(self.line8)
        self.groupBox_2 = QtWidgets.QGroupBox(MultiProjectPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.workspacePicker = E5PathPicker(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspacePicker.sizePolicy().hasHeightForWidth())
        self.workspacePicker.setSizePolicy(sizePolicy)
        self.workspacePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.workspacePicker.setObjectName("workspacePicker")
        self.horizontalLayout.addWidget(self.workspacePicker)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(MultiProjectPage)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.vboxlayout.setObjectName("vboxlayout")
        self.openMasterAutomaticallyCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.openMasterAutomaticallyCheckBox.setObjectName("openMasterAutomaticallyCheckBox")
        self.vboxlayout.addWidget(self.openMasterAutomaticallyCheckBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_6 = QtWidgets.QGroupBox(MultiProjectPage)
        self.groupBox_6.setObjectName("groupBox_6")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.multiProjectTimestampCheckBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.multiProjectTimestampCheckBox.setObjectName("multiProjectTimestampCheckBox")
        self.vboxlayout1.addWidget(self.multiProjectTimestampCheckBox)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(MultiProjectPage)
        self.groupBox_7.setObjectName("groupBox_7")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.multiProjectRecentSpinBox = QtWidgets.QSpinBox(self.groupBox_7)
        self.multiProjectRecentSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.multiProjectRecentSpinBox.setMinimum(5)
        self.multiProjectRecentSpinBox.setMaximum(50)
        self.multiProjectRecentSpinBox.setObjectName("multiProjectRecentSpinBox")
        self.hboxlayout.addWidget(self.multiProjectRecentSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout2.addLayout(self.hboxlayout)
        self.verticalLayout.addWidget(self.groupBox_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(MultiProjectPage)
        QtCore.QMetaObject.connectSlotsByName(MultiProjectPage)
        MultiProjectPage.setTabOrder(self.workspacePicker, self.openMasterAutomaticallyCheckBox)
        MultiProjectPage.setTabOrder(self.openMasterAutomaticallyCheckBox, self.multiProjectTimestampCheckBox)
        MultiProjectPage.setTabOrder(self.multiProjectTimestampCheckBox, self.multiProjectRecentSpinBox)

    def retranslateUi(self, MultiProjectPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("MultiProjectPage", "<b>Configure multiproject settings</b>"))
        self.groupBox_2.setTitle(_translate("MultiProjectPage", "Workspace"))
        self.workspacePicker.setToolTip(_translate("MultiProjectPage", "Enter the name of the workspace directory"))
        self.groupBox.setTitle(_translate("MultiProjectPage", "Master Project"))
        self.openMasterAutomaticallyCheckBox.setToolTip(_translate("MultiProjectPage", "Select to open the master project automatically upon opening the multiproject"))
        self.openMasterAutomaticallyCheckBox.setText(_translate("MultiProjectPage", "Open master project automatically"))
        self.groupBox_6.setTitle(_translate("MultiProjectPage", "XML"))
        self.multiProjectTimestampCheckBox.setToolTip(_translate("MultiProjectPage", "Select, if a timestamp should be written to all multiproject related XML files"))
        self.multiProjectTimestampCheckBox.setText(_translate("MultiProjectPage", "Include timestamp in multiproject related XML files"))
        self.groupBox_7.setTitle(_translate("MultiProjectPage", "Recent Multiprojects"))
        self.label.setText(_translate("MultiProjectPage", "Number of recent multiprojects:"))
        self.multiProjectRecentSpinBox.setToolTip(_translate("MultiProjectPage", "Enter the number of recent multiprojects to remember"))

from E5Gui.E5PathPicker import E5PathPicker

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MultiProjectPage = QtWidgets.QWidget()
    ui = Ui_MultiProjectPage()
    ui.setupUi(MultiProjectPage)
    MultiProjectPage.show()
    sys.exit(app.exec_())

