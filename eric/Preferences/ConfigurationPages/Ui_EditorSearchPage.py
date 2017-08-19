# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorSearchPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorSearchPage(object):
    def setupUi(self, EditorSearchPage):
        EditorSearchPage.setObjectName("EditorSearchPage")
        EditorSearchPage.resize(576, 596)
        self.vboxlayout = QtWidgets.QVBoxLayout(EditorSearchPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(EditorSearchPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line3 = QtWidgets.QFrame(EditorSearchPage)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setObjectName("line3")
        self.vboxlayout.addWidget(self.line3)
        self.groupBox_4 = QtWidgets.QGroupBox(EditorSearchPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.occurrencesMarkersEnabledCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.occurrencesMarkersEnabledCheckBox.setObjectName("occurrencesMarkersEnabledCheckBox")
        self.vboxlayout1.addWidget(self.occurrencesMarkersEnabledCheckBox)
        self.searchMarkersEnabledCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.searchMarkersEnabledCheckBox.setObjectName("searchMarkersEnabledCheckBox")
        self.vboxlayout1.addWidget(self.searchMarkersEnabledCheckBox)
        self.quicksearchMarkersEnabledCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.quicksearchMarkersEnabledCheckBox.setObjectName("quicksearchMarkersEnabledCheckBox")
        self.vboxlayout1.addWidget(self.quicksearchMarkersEnabledCheckBox)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.markOccurrencesTimeoutSpinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.markOccurrencesTimeoutSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.markOccurrencesTimeoutSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.markOccurrencesTimeoutSpinBox.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.markOccurrencesTimeoutSpinBox.setMinimum(100)
        self.markOccurrencesTimeoutSpinBox.setMaximum(5000)
        self.markOccurrencesTimeoutSpinBox.setSingleStep(100)
        self.markOccurrencesTimeoutSpinBox.setObjectName("markOccurrencesTimeoutSpinBox")
        self.hboxlayout.addWidget(self.markOccurrencesTimeoutSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.TextLabel2_2_2_2_2_2 = QtWidgets.QLabel(self.groupBox_4)
        self.TextLabel2_2_2_2_2_2.setObjectName("TextLabel2_2_2_2_2_2")
        self.hboxlayout1.addWidget(self.TextLabel2_2_2_2_2_2)
        self.searchMarkerButton = QtWidgets.QPushButton(self.groupBox_4)
        self.searchMarkerButton.setMinimumSize(QtCore.QSize(100, 0))
        self.searchMarkerButton.setText("")
        self.searchMarkerButton.setObjectName("searchMarkerButton")
        self.hboxlayout1.addWidget(self.searchMarkerButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addWidget(self.groupBox_4)
        spacerItem2 = QtWidgets.QSpacerItem(558, 231, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)

        self.retranslateUi(EditorSearchPage)
        QtCore.QMetaObject.connectSlotsByName(EditorSearchPage)
        EditorSearchPage.setTabOrder(self.occurrencesMarkersEnabledCheckBox, self.searchMarkersEnabledCheckBox)
        EditorSearchPage.setTabOrder(self.searchMarkersEnabledCheckBox, self.quicksearchMarkersEnabledCheckBox)
        EditorSearchPage.setTabOrder(self.quicksearchMarkersEnabledCheckBox, self.markOccurrencesTimeoutSpinBox)
        EditorSearchPage.setTabOrder(self.markOccurrencesTimeoutSpinBox, self.searchMarkerButton)

    def retranslateUi(self, EditorSearchPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorSearchPage", "<b>Configure editor search options</b>"))
        self.groupBox_4.setTitle(_translate("EditorSearchPage", "Search Markers"))
        self.occurrencesMarkersEnabledCheckBox.setToolTip(_translate("EditorSearchPage", "Select, whether markers for all occurrences of the current word shall be shown"))
        self.occurrencesMarkersEnabledCheckBox.setText(_translate("EditorSearchPage", "Highlight all occurrences of current word"))
        self.searchMarkersEnabledCheckBox.setToolTip(_translate("EditorSearchPage", "Select, whether search markers shall be shown for a standard search"))
        self.searchMarkersEnabledCheckBox.setText(_translate("EditorSearchPage", "Highlight all occurrences of search text"))
        self.quicksearchMarkersEnabledCheckBox.setToolTip(_translate("EditorSearchPage", "Select, whether search markers shall be shown for a quicksearch"))
        self.quicksearchMarkersEnabledCheckBox.setText(_translate("EditorSearchPage", "Highlight all occurrences of quicksearch text"))
        self.label.setText(_translate("EditorSearchPage", "Timeout for current word highlighting:"))
        self.markOccurrencesTimeoutSpinBox.setToolTip(_translate("EditorSearchPage", "Enter the time in milliseconds after which occurrences of the current word shall be highlighted"))
        self.markOccurrencesTimeoutSpinBox.setSuffix(_translate("EditorSearchPage", " ms"))
        self.TextLabel2_2_2_2_2_2.setText(_translate("EditorSearchPage", "Marker Colour:"))
        self.searchMarkerButton.setToolTip(_translate("EditorSearchPage", "Select the colour for the search markers."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorSearchPage = QtWidgets.QWidget()
    ui = Ui_EditorSearchPage()
    ui.setupUi(EditorSearchPage)
    EditorSearchPage.show()
    sys.exit(app.exec_())

