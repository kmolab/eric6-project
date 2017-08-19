# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\Preferences\ConfigurationPages\EditorCalltipsQScintillaPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorCalltipsQScintillaPage(object):
    def setupUi(self, EditorCalltipsQScintillaPage):
        EditorCalltipsQScintillaPage.setObjectName("EditorCalltipsQScintillaPage")
        EditorCalltipsQScintillaPage.resize(406, 369)
        self.vboxlayout = QtWidgets.QVBoxLayout(EditorCalltipsQScintillaPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(EditorCalltipsQScintillaPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line18 = QtWidgets.QFrame(EditorCalltipsQScintillaPage)
        self.line18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line18.setObjectName("line18")
        self.vboxlayout.addWidget(self.line18)
        self.groupBox = QtWidgets.QGroupBox(EditorCalltipsQScintillaPage)
        self.groupBox.setObjectName("groupBox")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.ctNoContextButton = QtWidgets.QRadioButton(self.groupBox)
        self.ctNoContextButton.setObjectName("ctNoContextButton")
        self.vboxlayout1.addWidget(self.ctNoContextButton)
        self.ctNoAutoCompletionButton = QtWidgets.QRadioButton(self.groupBox)
        self.ctNoAutoCompletionButton.setObjectName("ctNoAutoCompletionButton")
        self.vboxlayout1.addWidget(self.ctNoAutoCompletionButton)
        self.ctContextButton = QtWidgets.QRadioButton(self.groupBox)
        self.ctContextButton.setObjectName("ctContextButton")
        self.vboxlayout1.addWidget(self.ctContextButton)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vboxlayout1.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)
        self.vboxlayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(EditorCalltipsQScintillaPage)
        QtCore.QMetaObject.connectSlotsByName(EditorCalltipsQScintillaPage)
        EditorCalltipsQScintillaPage.setTabOrder(self.ctNoContextButton, self.ctNoAutoCompletionButton)
        EditorCalltipsQScintillaPage.setTabOrder(self.ctNoAutoCompletionButton, self.ctContextButton)

    def retranslateUi(self, EditorCalltipsQScintillaPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorCalltipsQScintillaPage", "<b>Configure QScintilla Calltips</b>"))
        self.groupBox.setTitle(_translate("EditorCalltipsQScintillaPage", "Context display options"))
        self.ctNoContextButton.setToolTip(_translate("EditorCalltipsQScintillaPage", "Select to display calltips without a context"))
        self.ctNoContextButton.setText(_translate("EditorCalltipsQScintillaPage", "Don\'t show context information"))
        self.ctNoAutoCompletionButton.setToolTip(_translate("EditorCalltipsQScintillaPage", "Select to display calltips with a context only if the user hasn\'t already implicitly identified the context using autocompletion"))
        self.ctNoAutoCompletionButton.setText(_translate("EditorCalltipsQScintillaPage", "Show context information, if no prior autocompletion"))
        self.ctContextButton.setToolTip(_translate("EditorCalltipsQScintillaPage", "Select to display calltips with a context"))
        self.ctContextButton.setText(_translate("EditorCalltipsQScintillaPage", "Show context information"))
        self.label.setText(_translate("EditorCalltipsQScintillaPage", "A context is any scope (e.g. a C++ namespace or a Python module) prior to the function/method name."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditorCalltipsQScintillaPage = QtWidgets.QWidget()
    ui = Ui_EditorCalltipsQScintillaPage()
    ui.setupUi(EditorCalltipsQScintillaPage)
    EditorCalltipsQScintillaPage.show()
    sys.exit(app.exec_())

