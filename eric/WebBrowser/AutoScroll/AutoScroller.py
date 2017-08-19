# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the automatic scroller.
"""

#
# This module is based on the Qupzilla auto scroller.
# Copyright (C) 2014  David Rosca <nowrep@gmail.com>
#

from __future__ import unicode_literals

from PyQt5.QtCore import Qt, QObject, QRect, QEvent, QPoint
from PyQt5.QtWidgets import QApplication, QLabel

from .FrameScroller import FrameScroller

import Preferences
import UI.PixmapCache


class AutoScroller(QObject):
    """
    Class implementing the automatic scroller.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent object
        @type QObject
        """
        super(AutoScroller, self).__init__(parent)
        
        self.__view = None
        
        self.__indicator = QLabel()
        self.__indicator.resize(32, 32)
        self.__indicator.setContentsMargins(0, 0, 0, 0)
        self.__indicator.installEventFilter(self)
        
        self.__scroller = FrameScroller(self)
        self.__scroller.setScrollDivider(
            Preferences.getWebBrowser("AutoScrollDivider"))
        
        self.__enabled = Preferences.getWebBrowser("AutoScrollEnabled")
    
    def isEnabled(self):
        """
        Public method to get the enabled state.
        
        @return enabled state
        @rtype bool
        """
        return self.__enabled
    
    def mouseMove(self, evt):
        """
        Public method to handle mouse move events.
        
        @param evt reference to the mouse move event
        @type QMouseEvent
        @return flag indicating, that the event was handled
        @rtype bool
        """
        if self.__enabled and self.__indicator.isVisible():
            rect = self.__indicatorGlobalRect()
            xlen = 0
            ylen = 0
            egp = evt.globalPos()
            
            if rect.left() > egp.x():
                xlen = egp.x() - rect.left()
            elif rect.right() < egp.x():
                xlen = egp.x() - rect.right()
            
            if rect.top() > egp.y():
                ylen = egp.y() - rect.top()
            elif rect.bottom() < egp.y():
                ylen = egp.y() - rect.bottom()
            
            self.__scroller.startScrolling(xlen, ylen)
        
        return False
    
    def mousePress(self, view, evt):
        """
        Public method to handle mouse button presses.
        
        @param view reference to the web view the button was pressed on
        @type WebBrowserView
        @param evt reference to the mouse button press event
        @type QMouseEvent
        @return flag indicating, that the event was handled
        @rtype bool
        """
        if self.__enabled:
            middleButton = evt.buttons() == Qt.MiddleButton
            
            if view:
                # test for start
                if self.__view != view and middleButton:
                    return self.__showIndicator(view, evt.pos())
                elif not self.__indicator.isVisible() and middleButton:
                    return self.__showIndicator(view, evt.pos())
                
                # test for stop
                if self.__indicator.isVisible():
                    self.__stopScrolling()
                    return True
        
        return False
    
    def mouseRelease(self, evt):
        """
        Public method to handle mouse button releases.
        
        @param evt reference to the mouse button release event
        @type QMouseEvent
        @return flag indicating, that the event was handled
        @rtype bool
        """
        if self.__enabled and self.__indicator.isVisible():
            if not self.__indicatorGlobalRect().contains(
                    evt.globalPos()):
                self.__stopScrolling()
            return True
        
        return False
    
    def wheel(self):
        """
        Public method to handle a mouse wheel event.
        
        @return flag indicating, that the event was handled
        @rtype bool
        """
        if self.__enabled and self.__indicator.isVisible():
            self.__stopScrolling()
            return True
        
        return False
    
    def preferencesChanged(self):
        """
        Public method to handle a change of the settings.
        """
        enabled = Preferences.getWebBrowser("AutoScrollEnabled")
        if enabled != self.__enabled:
            if self.__indicator.isVisible():
                self.__stopScrolling()
            self.__enabled = enabled
        
        self.__scroller.setScrollDivider(
            Preferences.getWebBrowser("AutoScrollDivider"))
    
    def eventFilter(self, obj, evt):
        """
        Public method to handle event for an object.
        
        @param obj refernce to the object sending the event
        @type QObject
        @param evt reference to the event to be handled
        @type QEvent
        @return flag indicating, that the event was handled
        @rtype bool
        """
        if obj == self.__indicator:
            if evt.type() == QEvent.Enter:
                self.__scroller.stopScrolling()
            elif evt.type() in [QEvent.Wheel, QEvent.Hide,
                                QEvent.MouseButtonPress]:
                self.__stopScrolling()
        
        return False
    
    def __showIndicator(self, view, pos):
        """
        Private method to show the auto scroll indicator.
        
        @param view reference to the view to show the indicator on
        @type WebBrowserView
        @param pos position to show the indicator at
        @type QPoint
        @return flag indicating, that the indicator is shown
        @rtype bool
        """
        hit = view.page().hitTestContent(pos)
        
        if hit.isContentEditable() or not hit.linkUrl().isEmpty():
            return False
        
        jsSource = """
            var out = {
             vertical:
                window.innerWidth > document.documentElement.clientWidth,
             horizontal:
                window.innerHeight > document.documentElement.clientHeight
            };
            out;"""
        
        res = view.page().execJavaScript(jsSource)
        if res is None:
            return False
        
        vertical = res["vertical"]
        horizontal = res["horizontal"]
        if not vertical and not horizontal:
            return False
        
        if vertical and horizontal:
            self.__indicator.setPixmap(
                UI.PixmapCache.getPixmap("scrollAll.png"))
        elif vertical:
            self.__indicator.setPixmap(
                UI.PixmapCache.getPixmap("scrollVertical.png"))
        else:
            self.__indicator.setPixmap(
                UI.PixmapCache.getPixmap("scrollHorizontal.png"))
        
        self.__view = view
        p = QPoint(
            pos.x() - self.__indicator.pixmap().width() // 2,
            pos.y() - self.__indicator.pixmap().height() // 2
        )
        
        self.__indicator.setParent(self.__view)
        self.__indicator.move(p)
        self.__indicator.show()
        
        self.__scroller.setPage(view.page())
        
        self.__view.inputWidget().grabMouse()
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        
        return True
    
    def __stopScrolling(self):
        """
        Private method to stop scrolling.
        """
        self.__view.inputWidget().releaseMouse()
        QApplication.restoreOverrideCursor()
        
        self.__indicator.hide()
        self.__indicator.setParent(None)
        self.__scroller.stopScrolling()
    
    def __indicatorGlobalRect(self):
        """
        Private method to calculate the global indicator parameters.
        
        @return global indicator parameters
        @rtype QRect
        """
        pos = self.__indicator.parentWidget().mapToGlobal(
            self.__indicator.geometry().topLeft())
        return QRect(pos.x(), pos.y(),
                     self.__indicator.width(), self.__indicator.height())
