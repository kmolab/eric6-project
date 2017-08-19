# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\github\eric6-17.08\eric\SqlBrowser\SqlBrowserWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SqlBrowserWidget(object):
    def setupUi(self, SqlBrowserWidget):
        SqlBrowserWidget.setObjectName("SqlBrowserWidget")
        SqlBrowserWidget.resize(800, 550)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SqlBrowserWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(SqlBrowserWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.connections = SqlConnectionWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connections.sizePolicy().hasHeightForWidth())
        self.connections.setSizePolicy(sizePolicy)
        self.connections.setObjectName("connections")
        self.table = QtWidgets.QTableView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setObjectName("table")
        self.verticalLayout_2.addWidget(self.splitter)
        self.queryGroup = QtWidgets.QGroupBox(SqlBrowserWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queryGroup.sizePolicy().hasHeightForWidth())
        self.queryGroup.setSizePolicy(sizePolicy)
        self.queryGroup.setMaximumSize(QtCore.QSize(16777215, 200))
        self.queryGroup.setObjectName("queryGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.queryGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sqlEdit = QtWidgets.QPlainTextEdit(self.queryGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqlEdit.sizePolicy().hasHeightForWidth())
        self.sqlEdit.setSizePolicy(sizePolicy)
        self.sqlEdit.setMinimumSize(QtCore.QSize(0, 18))
        self.sqlEdit.setObjectName("sqlEdit")
        self.verticalLayout.addWidget(self.sqlEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clearButton = QtWidgets.QPushButton(self.queryGroup)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.executeButton = QtWidgets.QPushButton(self.queryGroup)
        self.executeButton.setObjectName("executeButton")
        self.horizontalLayout.addWidget(self.executeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.queryGroup)
        self.insertRowAction = QtWidgets.QAction(SqlBrowserWidget)
        self.insertRowAction.setEnabled(False)
        self.insertRowAction.setObjectName("insertRowAction")
        self.deleteRowAction = QtWidgets.QAction(SqlBrowserWidget)
        self.deleteRowAction.setEnabled(False)
        self.deleteRowAction.setObjectName("deleteRowAction")

        self.retranslateUi(SqlBrowserWidget)
        QtCore.QMetaObject.connectSlotsByName(SqlBrowserWidget)
        SqlBrowserWidget.setTabOrder(self.sqlEdit, self.clearButton)
        SqlBrowserWidget.setTabOrder(self.clearButton, self.executeButton)
        SqlBrowserWidget.setTabOrder(self.executeButton, self.connections)
        SqlBrowserWidget.setTabOrder(self.connections, self.table)

    def retranslateUi(self, SqlBrowserWidget):
        _translate = QtCore.QCoreApplication.translate
        SqlBrowserWidget.setWindowTitle(_translate("SqlBrowserWidget", "eric6 SQL Browser"))
        self.queryGroup.setTitle(_translate("SqlBrowserWidget", "SQL Query"))
        self.sqlEdit.setToolTip(_translate("SqlBrowserWidget", "Enter the SQL query to be executed"))
        self.clearButton.setToolTip(_translate("SqlBrowserWidget", "Press to clear the entry"))
        self.clearButton.setText(_translate("SqlBrowserWidget", "&Clear"))
        self.executeButton.setToolTip(_translate("SqlBrowserWidget", "Press to execute the query"))
        self.executeButton.setText(_translate("SqlBrowserWidget", "&Execute"))
        self.insertRowAction.setText(_translate("SqlBrowserWidget", "&Insert Row"))
        self.insertRowAction.setToolTip(_translate("SqlBrowserWidget", "Inserts a new row"))
        self.deleteRowAction.setText(_translate("SqlBrowserWidget", "&Delete Row"))
        self.deleteRowAction.setStatusTip(_translate("SqlBrowserWidget", "Deletes the current row"))

from .SqlConnectionWidget import SqlConnectionWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SqlBrowserWidget = QtWidgets.QWidget()
    ui = Ui_SqlBrowserWidget()
    ui.setupUi(SqlBrowserWidget)
    SqlBrowserWidget.show()
    sys.exit(app.exec_())

