# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\DataViews\PyProfileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyProfileDialog(object):
    def setupUi(self, PyProfileDialog):
        PyProfileDialog.setObjectName("PyProfileDialog")
        PyProfileDialog.resize(832, 587)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(PyProfileDialog.sizePolicy().hasHeightForWidth())
        PyProfileDialog.setSizePolicy(sizePolicy)
        PyProfileDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(PyProfileDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.resultList = QtWidgets.QTreeWidget(PyProfileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.resultList.sizePolicy().hasHeightForWidth())
        self.resultList.setSizePolicy(sizePolicy)
        self.resultList.setAlternatingRowColors(True)
        self.resultList.setRootIsDecorated(False)
        self.resultList.setItemsExpandable(False)
        self.resultList.setObjectName("resultList")
        self.vboxlayout.addWidget(self.resultList)
        self.summaryList = QtWidgets.QTreeWidget(PyProfileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.summaryList.sizePolicy().hasHeightForWidth())
        self.summaryList.setSizePolicy(sizePolicy)
        self.summaryList.setAlternatingRowColors(True)
        self.summaryList.setRootIsDecorated(False)
        self.summaryList.setItemsExpandable(False)
        self.summaryList.setObjectName("summaryList")
        self.vboxlayout.addWidget(self.summaryList)
        self.checkProgress = QtWidgets.QProgressBar(PyProfileDialog)
        self.checkProgress.setProperty("value", 0)
        self.checkProgress.setOrientation(QtCore.Qt.Horizontal)
        self.checkProgress.setObjectName("checkProgress")
        self.vboxlayout.addWidget(self.checkProgress)
        self.buttonBox = QtWidgets.QDialogButtonBox(PyProfileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(PyProfileDialog)
        QtCore.QMetaObject.connectSlotsByName(PyProfileDialog)
        PyProfileDialog.setTabOrder(self.resultList, self.summaryList)

    def retranslateUi(self, PyProfileDialog):
        _translate = QtCore.QCoreApplication.translate
        PyProfileDialog.setWindowTitle(_translate("PyProfileDialog", "Profile Results"))
        PyProfileDialog.setWhatsThis(_translate("PyProfileDialog", "<b>Profile Results</b>\n"
"<p>This dialog shows the profile results.</p>"))
        self.resultList.setWhatsThis(_translate("PyProfileDialog", "<b>Profile Results</b>\n"
"<p>This list shows the profile results. There are several actions available via the context menu.</p>"))
        self.resultList.setSortingEnabled(True)
        self.resultList.headerItem().setText(0, _translate("PyProfileDialog", "Nr. Calls"))
        self.resultList.headerItem().setText(1, _translate("PyProfileDialog", "Total Time"))
        self.resultList.headerItem().setText(2, _translate("PyProfileDialog", "Tot. Time / Call"))
        self.resultList.headerItem().setText(3, _translate("PyProfileDialog", "Cumulative Time"))
        self.resultList.headerItem().setText(4, _translate("PyProfileDialog", "Cum. Time / Call"))
        self.resultList.headerItem().setText(5, _translate("PyProfileDialog", "Filename"))
        self.resultList.headerItem().setText(6, _translate("PyProfileDialog", "Line"))
        self.resultList.headerItem().setText(7, _translate("PyProfileDialog", "Function"))
        self.summaryList.setWhatsThis(_translate("PyProfileDialog", "<b>Summary</b>\n"
"<p>This shows some overall profile data. There are several actions available via the context menu.</p>"))
        self.summaryList.headerItem().setText(0, _translate("PyProfileDialog", "Summary"))
        self.summaryList.headerItem().setText(1, _translate("PyProfileDialog", "#"))
        self.checkProgress.setToolTip(_translate("PyProfileDialog", "Shows the progress of the profile data calculation"))
        self.checkProgress.setFormat(_translate("PyProfileDialog", "%v/%m Files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyProfileDialog = QtWidgets.QDialog()
    ui = Ui_PyProfileDialog()
    ui.setupUi(PyProfileDialog)
    PyProfileDialog.show()
    sys.exit(app.exec_())

