# -*- coding: utf-8 -*-

# Copyright (c) 2011 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to show some information about a site.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSlot, QUrl, Qt
from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QBrush
from PyQt5.QtNetwork import QNetworkRequest, QNetworkReply
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem, QGraphicsScene, QMenu, \
    QApplication, QGraphicsPixmapItem

from E5Gui import E5MessageBox, E5FileDialog

from .Ui_SiteInfoDialog import Ui_SiteInfoDialog

from ..Tools import Scripts, WebBrowserTools
from ..WebBrowserPage import WebBrowserPage

import UI.PixmapCache


class SiteInfoDialog(QDialog, Ui_SiteInfoDialog):
    """
    Class implementing a dialog to show some information about a site.
    """
    okStyle = "QLabel { color : white; background-color : green; }"
    nokStyle = "QLabel { color : white; background-color : red; }"
    
    def __init__(self, browser, parent=None):
        """
        Constructor
        
        @param browser reference to the browser window (HelpBrowser)
        @param parent reference to the parent widget (QWidget)
        """
        super(SiteInfoDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        
        # put icons
        self.tabWidget.setTabIcon(
            0, UI.PixmapCache.getIcon("siteinfo-general.png"))
        self.tabWidget.setTabIcon(
            1, UI.PixmapCache.getIcon("siteinfo-media.png"))
        
        self.__imageReply = None
        
        self.__baseUrl = browser.url()
        title = browser.title()
        
        #prepare background of image preview
        self.__imagePreviewStandardBackground = \
            self.imagePreview.backgroundBrush()
        color1 = QColor(220, 220, 220)
        color2 = QColor(160, 160, 160)
        self.__tilePixmap = QPixmap(8, 8)
        self.__tilePixmap.fill(color1)
        tilePainter = QPainter(self.__tilePixmap)
        tilePainter.fillRect(0, 0, 4, 4, color2)
        tilePainter.fillRect(4, 4, 4, 4, color2)
        tilePainter.end()
        
        # populate General tab
        self.heading.setText("<b>{0}</b>".format(title))
        self.siteAddressLabel.setText(self.__baseUrl.toString())
        if self.__baseUrl.scheme() in ["https"]:
            self.securityLabel.setStyleSheet(SiteInfoDialog.okStyle)
            self.securityLabel.setText('<b>Connection is encrypted.</b>')
        else:
            self.securityLabel.setStyleSheet(SiteInfoDialog.nokStyle)
            self.securityLabel.setText('<b>Connection is not encrypted.</b>')
        browser.page().runJavaScript(
            "document.charset", WebBrowserPage.SafeJsWorld,
            lambda res: self.encodingLabel.setText(res))
        
        # populate Meta tags
        browser.page().runJavaScript(Scripts.getAllMetaAttributes(),
                                     WebBrowserPage.SafeJsWorld,
                                     self.__processMetaAttributes)
        
        # populate Media tab
        browser.page().runJavaScript(Scripts.getAllImages(),
                                     WebBrowserPage.SafeJsWorld,
                                     self.__processImageTags)
        
    def __processImageTags(self, res):
        """
        Private method to process the image tags.
        
        @param res result of the JavaScript script
        @type list of dict
        """
        for img in res:
            src = img["src"]
            alt = img["alt"]
            if not alt:
                if src.find("/") == -1:
                    alt = src
                else:
                    pos = src.rfind("/")
                    alt = src[pos + 1:]
            
            if not src or not alt:
                continue
            
            QTreeWidgetItem(self.imagesTree, [alt, src])
        
        for col in range(self.imagesTree.columnCount()):
            self.imagesTree.resizeColumnToContents(col)
        if self.imagesTree.columnWidth(0) > 300:
            self.imagesTree.setColumnWidth(0, 300)
        self.imagesTree.setCurrentItem(self.imagesTree.topLevelItem(0))
        self.imagesTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.imagesTree.customContextMenuRequested.connect(
            self.__imagesTreeContextMenuRequested)
    
    def __processMetaAttributes(self, res):
        """
        Private method to process the meta attributes.
        
        @param res result of the JavaScript script
        @type list of dict
        """
        for meta in res:
            content = meta["content"]
            name = meta["name"]
            if not name:
                name = meta["httpequiv"]
            
            if not name or not content:
                continue
            
            if meta["charset"]:
                self.encodingLabel.setText(meta["charset"])
            if "charset=" in content:
                self.encodingLabel.setText(
                    content[content.index("charset=") + 8:])
            
            QTreeWidgetItem(self.tagsTree, [name, content])
        for col in range(self.tagsTree.columnCount()):
            self.tagsTree.resizeColumnToContents(col)
    
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_imagesTree_currentItemChanged(self, current, previous):
        """
        Private slot to show a preview of the selected image.
        
        @param current current image entry (QTreeWidgetItem)
        @param previous old current entry (QTreeWidgetItem)
        """
        if current is None:
            return
        
        imageUrl = QUrl(current.text(1))
        if imageUrl.isRelative():
            imageUrl = self.__baseUrl.resolved(imageUrl)
        
        pixmap = QPixmap()
        loading = False
        
        if imageUrl.scheme() == "data":
            encodedUrl = current.text(1).encode("utf-8")
            imageData = encodedUrl[encodedUrl.find(b",") + 1:]
            pixmap = WebBrowserTools.pixmapFromByteArray(imageData)
        elif imageUrl.scheme() == "file":
            pixmap = QPixmap(imageUrl.toLocalFile())
        elif imageUrl.scheme() == "qrc":
            pixmap = QPixmap(imageUrl.toString()[3:])
        else:
            if self.__imageReply is not None:
                self.__imageReply.deleteLater()
                self.__imageReply = None
            
            from WebBrowser.WebBrowserWindow import WebBrowserWindow
            self.__imageReply = WebBrowserWindow.networkManager().get(
                QNetworkRequest(imageUrl))
            self.__imageReply.finished.connect(self.__imageReplyFinished)
            loading = True
            self.__showLoadingText()
        
        if not loading:
            self.__showPixmap(pixmap)
    
    @pyqtSlot()
    def __imageReplyFinished(self):
        """
        Private slot handling the loading of an image.
        """
        if self.__imageReply.error() != QNetworkReply.NoError:
            return
        
        data = self.__imageReply.readAll()
        self.__showPixmap(QPixmap.fromImage(QImage.fromData(data)))
    
    def __showPixmap(self, pixmap):
        """
        Private method to show a pixmap in the preview pane.
        
        @param pixmap pixmap to be shown
        @type QPixmap
        """
        scene = QGraphicsScene(self.imagePreview)
        if pixmap.isNull():
            self.imagePreview.setBackgroundBrush(
                self.__imagePreviewStandardBackground)
            scene.addText(self.tr("Preview not available."))
        else:
            self.imagePreview.setBackgroundBrush(QBrush(self.__tilePixmap))
            scene.addPixmap(pixmap)
        self.imagePreview.setScene(scene)
    
    def __showLoadingText(self):
        """
        Private method to show some text while loading an image.
        """
        self.imagePreview.setBackgroundBrush(
            self.__imagePreviewStandardBackground)
        scene = QGraphicsScene(self.imagePreview)
        scene.addText(self.tr("Loading..."))
        self.imagePreview.setScene(scene)
    
    def __imagesTreeContextMenuRequested(self, pos):
        """
        Private slot to show a context menu for the images list.
        
        @param pos position for the menu (QPoint)
        """
        itm = self.imagesTree.itemAt(pos)
        if itm is None:
            return
        
        menu = QMenu()
        menu.addAction(
            self.tr("Copy Image Location to Clipboard"),
            self.__copyAction).setData(itm.text(1))
        menu.addAction(
            self.tr("Copy Image Name to Clipboard"),
            self.__copyAction).setData(itm.text(0))
        menu.addSeparator()
        menu.addAction(
            self.tr("Save Image"),
            self.__saveImage).setData(self.imagesTree.indexOfTopLevelItem(itm))
        menu.exec_(self.imagesTree.viewport().mapToGlobal(pos))
    
    def __copyAction(self):
        """
        Private slot to copy the image URL or the image name to the clipboard.
        """
        act = self.sender()
        QApplication.clipboard().setText(act.data())
    
    def __saveImage(self):
        """
        Private slot to save the selected image to disk.
        """
        act = self.sender()
        index = act.data()
        itm = self.imagesTree.topLevelItem(index)
        if itm is None:
            return
        
        if not self.imagePreview.scene() or \
                len(self.imagePreview.scene().items()) == 0:
            return
        
        pixmapItem = self.imagePreview.scene().items()[0]
        if not isinstance(pixmapItem, QGraphicsPixmapItem):
            return
        
        if pixmapItem.pixmap().isNull():
            E5MessageBox.warning(
                self,
                self.tr("Save Image"),
                self.tr(
                    """<p>This preview is not available.</p>"""))
            return
        
        imageFileName = WebBrowserTools.getFileNameFromUrl(QUrl(itm.text(1)))
        index = imageFileName.rfind(".")
        if index != -1:
            imageFileName = imageFileName[:index] + ".png"
        
        filename = E5FileDialog.getSaveFileName(
            self,
            self.tr("Save Image"),
            imageFileName,
            self.tr("All Files (*)"),
            E5FileDialog.Options(E5FileDialog.DontConfirmOverwrite))
        
        if not filename:
            return
        
        if not pixmapItem.pixmap().save(filename, "PNG"):
            E5MessageBox.critical(
                self,
                self.tr("Save Image"),
                self.tr(
                    """<p>Cannot write to file <b>{0}</b>.</p>""")
                .format(filename))
            return
