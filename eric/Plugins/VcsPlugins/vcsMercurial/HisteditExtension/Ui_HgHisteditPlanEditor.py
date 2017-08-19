# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Plugins\VcsPlugins\vcsMercurial\HisteditExtension\HgHisteditPlanEditor.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HgHisteditPlanEditor(object):
    def setupUi(self, HgHisteditPlanEditor):
        HgHisteditPlanEditor.setObjectName("HgHisteditPlanEditor")
        HgHisteditPlanEditor.resize(500, 650)
        HgHisteditPlanEditor.setSizeGripEnabled(True)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(HgHisteditPlanEditor)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(HgHisteditPlanEditor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.planTreeWidget = QtWidgets.QTreeWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.planTreeWidget.sizePolicy().hasHeightForWidth())
        self.planTreeWidget.setSizePolicy(sizePolicy)
        self.planTreeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.planTreeWidget.setAlternatingRowColors(True)
        self.planTreeWidget.setRootIsDecorated(False)
        self.planTreeWidget.setItemsExpandable(False)
        self.planTreeWidget.setObjectName("planTreeWidget")
        self.planTreeWidget.header().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.planTreeWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.upButton = QtWidgets.QPushButton(self.groupBox)
        self.upButton.setObjectName("upButton")
        self.verticalLayout_2.addWidget(self.upButton)
        self.downButton = QtWidgets.QPushButton(self.groupBox)
        self.downButton.setObjectName("downButton")
        self.verticalLayout_2.addWidget(self.downButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.infoEdit.setReadOnly(True)
        self.infoEdit.setObjectName("infoEdit")
        self.verticalLayout.addWidget(self.infoEdit)
        self.verticalLayout_3.addWidget(self.splitter)
        self.buttonBox = QtWidgets.QDialogButtonBox(HgHisteditPlanEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(HgHisteditPlanEditor)
        self.buttonBox.accepted.connect(HgHisteditPlanEditor.accept)
        self.buttonBox.rejected.connect(HgHisteditPlanEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(HgHisteditPlanEditor)
        HgHisteditPlanEditor.setTabOrder(self.planTreeWidget, self.upButton)
        HgHisteditPlanEditor.setTabOrder(self.upButton, self.downButton)
        HgHisteditPlanEditor.setTabOrder(self.downButton, self.infoEdit)

    def retranslateUi(self, HgHisteditPlanEditor):
        _translate = QtCore.QCoreApplication.translate
        HgHisteditPlanEditor.setWindowTitle(_translate("HgHisteditPlanEditor", "Edit Plan"))
        self.groupBox.setTitle(_translate("HgHisteditPlanEditor", "Modification Plan"))
        self.planTreeWidget.headerItem().setText(0, _translate("HgHisteditPlanEditor", "Action"))
        self.planTreeWidget.headerItem().setText(1, _translate("HgHisteditPlanEditor", "Revision"))
        self.planTreeWidget.headerItem().setText(2, _translate("HgHisteditPlanEditor", "Summary"))
        self.upButton.setToolTip(_translate("HgHisteditPlanEditor", "Press to move the selected entry up"))
        self.upButton.setText(_translate("HgHisteditPlanEditor", "Up"))
        self.downButton.setToolTip(_translate("HgHisteditPlanEditor", "Press to move the selected entry down"))
        self.downButton.setText(_translate("HgHisteditPlanEditor", "Down"))
        self.groupBox_2.setTitle(_translate("HgHisteditPlanEditor", "Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HgHisteditPlanEditor = QtWidgets.QDialog()
    ui = Ui_HgHisteditPlanEditor()
    ui.setupUi(HgHisteditPlanEditor)
    HgHisteditPlanEditor.show()
    sys.exit(app.exec_())

