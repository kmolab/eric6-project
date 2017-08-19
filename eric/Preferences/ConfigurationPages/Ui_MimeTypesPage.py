# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\MimeTypesPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MimeTypesPage(object):
    def setupUi(self, MimeTypesPage):
        MimeTypesPage.setObjectName("MimeTypesPage")
        MimeTypesPage.resize(480, 515)
        self.verticalLayout = QtWidgets.QVBoxLayout(MimeTypesPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(MimeTypesPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line9 = QtWidgets.QFrame(MimeTypesPage)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9.setObjectName("line9")
        self.verticalLayout.addWidget(self.line9)
        self.label = QtWidgets.QLabel(MimeTypesPage)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textMimeTypesList = E5StringListEditWidget(MimeTypesPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textMimeTypesList.sizePolicy().hasHeightForWidth())
        self.textMimeTypesList.setSizePolicy(sizePolicy)
        self.textMimeTypesList.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textMimeTypesList.setObjectName("textMimeTypesList")
        self.verticalLayout.addWidget(self.textMimeTypesList)
        self.resetButton = QtWidgets.QPushButton(MimeTypesPage)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)

        self.retranslateUi(MimeTypesPage)
        QtCore.QMetaObject.connectSlotsByName(MimeTypesPage)

    def retranslateUi(self, MimeTypesPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("MimeTypesPage", "<b>Configure Text Mimetypes</b>"))
        self.label.setText(_translate("MimeTypesPage", "Files of the mime types configured below are opened in an eric editor (in addition to all \'text\' mime types)."))
        self.resetButton.setToolTip(_translate("MimeTypesPage", "Press to reset the list to default values"))
        self.resetButton.setText(_translate("MimeTypesPage", "Reset to Defaults"))

from E5Gui.E5StringListEditWidget import E5StringListEditWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MimeTypesPage = QtWidgets.QWidget()
    ui = Ui_MimeTypesPage()
    ui.setupUi(MimeTypesPage)
    MimeTypesPage.show()
    sys.exit(app.exec_())

