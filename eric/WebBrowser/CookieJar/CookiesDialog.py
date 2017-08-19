# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to show all cookies.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, Qt, QByteArray
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem, QHeaderView

from E5Gui import E5MessageBox

from .Ui_CookiesDialog import Ui_CookiesDialog


class CookiesDialog(QDialog, Ui_CookiesDialog):
    """
    Class implementing a dialog to show all cookies.
    """
    DomainRole = Qt.UserRole + 1
    CookieRole = Qt.UserRole + 2
    
    def __init__(self, cookieJar, parent=None):
        """
        Constructor
        
        @param cookieJar reference to the cookie jar (CookieJar)
        @param parent reference to the parent widget (QWidget)
        """
        super(CookiesDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.addButton.setEnabled(False)
        
        self.__cookieJar = cookieJar
        
        self.__domainDict = {}
        
        self.cookiesTree.headerItem().setText(
            self.cookiesTree.columnCount(), "")
        
        for cookie in self.__cookieJar.cookies():
            self.__addCookie(cookie)
        self.__resizeColumns()
        
        self.cookiesTree.itemExpanded.connect(self.__resizeColumns)
        self.cookiesTree.itemCollapsed.connect(self.__resizeColumns)
    
    @pyqtSlot()
    def __resizeColumns(self):
        """
        Private slot to resize the columns.
        """
        self.cookiesTree.header().resizeSections(QHeaderView.ResizeToContents)
        self.cookiesTree.header().setStretchLastSection(True)
    
    def __cookieDomain(self, cookie):
        """
        Private method to extract the cookie domain.
        
        @param cookie cookie to get the domain from
        @type QNetworkCookie
        @return domain of the cookie
        @rtype str
        """
        domain = cookie.domain()
        if domain.startswith("."):
            domain = domain[1:]
        return domain
    
    def __addCookie(self, cookie):
        """
        Private method to add a cookie to the tree.
        
        @param cookie reference to the cookie
        @type QNetworkCookie
        """
        domain = self.__cookieDomain(cookie)
        if domain in self.__domainDict:
            itm = QTreeWidgetItem(self.__domainDict[domain])
        else:
            newParent = QTreeWidgetItem(self.cookiesTree)
            newParent.setText(0, domain)
            newParent.setData(0, self.DomainRole, cookie.domain())
            self.__domainDict[domain] = newParent
            
            itm = QTreeWidgetItem(newParent)
        
        itm.setText(0, cookie.domain())
        itm.setText(1, bytes(cookie.name()).decode())
        itm.setData(0, self.CookieRole, cookie)
    
    @pyqtSlot()
    def on_addButton_clicked(self):
        """
        Private slot to add a new exception.
        """
        current = self.cookiesTree.currentItem()
        if current is None:
            return
        
        from .CookiesExceptionsDialog import CookiesExceptionsDialog
        
        domain = current.text(0)
        dlg = CookiesExceptionsDialog(self.__cookieJar, self)
        dlg.setDomainName(domain)
        dlg.exec_()
    
    @pyqtSlot()
    def on_removeButton_clicked(self):
        """
        Private slot to remove the selected cookie(s).
        """
        current = self.cookiesTree.currentItem()
        if current is None:
            return
        
        if current.childCount() == 0:
            # single cookie
            cookie = current.data(0, self.CookieRole)
            self.__cookieJar.removeCookie(cookie)
            current.parent().removeChild(current)
            del current
        else:
            cookies = []
            for row in range(current.childCount() - 1, -1, -1):
                child = current.child(row)
                cookies.append(child.data(0, self.CookieRole))
                current.removeChild(child)
                del child
            self.__cookieJar.removeCookies(cookies)
            index = self.cookiesTree.indexOfTopLevelItem(current)
            self.cookiesTree.takeTopLevelItem(index)
            del current
    
    @pyqtSlot()
    def on_removeAllButton_clicked(self):
        """
        Private slot to remove all cookies.
        """
        res = E5MessageBox.yesNo(
            self,
            self.tr("Remove All Cookies"),
            self.tr("""Do you really want to remove all stored cookies?"""))
        if res:
            self.__cookieJar.clear()
            self.__domainDict = {}
            self.cookiesTree.clear()
    
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_cookiesTree_currentItemChanged(self, current, previous):
        """
        Private slot to handle a change of the current item.
        
        @param current reference to the current item
        @type QTreeWidgetItem
        @param previous reference to the previous current item
        @type QTreeWidgetItem
        """
        self.addButton.setEnabled(current is not None)
        self.removeButton.setEnabled(current is not None)
        
        if current is None:
            return
        
        if not current.text(1):
            # it is a cookie domain entry
            self.domain.setText(self.tr("<no cookie selected>"))
            self.name.setText(self.tr("<no cookie selected>"))
            self.path.setText(self.tr("<no cookie selected>"))
            self.secure.setText(self.tr("<no cookie selected>"))
            self.expiration.setText(self.tr("<no cookie selected>"))
            self.value.setText(self.tr("<no cookie selected>"))
            
            self.removeButton.setText(self.tr("Remove Cookies"))
        else:
            # it is a cookie entry
            cookie = current.data(0, self.CookieRole)
            
            self.domain.setText(cookie.domain())
            self.name.setText(bytes(cookie.name()).decode())
            self.path.setText(cookie.path())
            if cookie.isSecure():
                self.secure.setText(self.tr("Secure connections only"))
            else:
                self.secure.setText(self.tr("All connections"))
            if cookie.isSessionCookie():
                self.expiration.setText(self.tr("Session Cookie"))
            else:
                self.expiration.setText(
                    cookie.expirationDate().toString("yyyy-MM-dd HH:mm:ss"))
            self.value.setText(
                bytes(QByteArray.fromPercentEncoding(cookie.value())).decode())
            
            self.removeButton.setText(self.tr("Remove Cookie"))
    
    @pyqtSlot(str)
    def on_searchEdit_textChanged(self, txt):
        """
        Private slot to search and filter the cookie tree.
        
        @param txt text to search for
        @type str
        """
        if not txt:
            for row in range(self.cookiesTree.topLevelItemCount()):
                self.cookiesTree.topLevelItem(row).setHidden(False)
        else:
            for row in range(self.cookiesTree.topLevelItemCount()):
                text = self.cookiesTree.topLevelItem(row).text(0)
                self.cookiesTree.topLevelItem(row).setHidden(txt not in text)
