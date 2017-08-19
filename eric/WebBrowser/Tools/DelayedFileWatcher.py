# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a file system watcher with a delay.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QFileSystemWatcher, QTimer


class DelayedFileWatcher(QFileSystemWatcher):
    """
    Class implementing a file system watcher with a delay.
    
    @signal delayedDirectoryChanged(path) emitted to indicate a changed
        directory
    @signal delayedFileChanged(path) emitted to indicate a changed file
    """
    delayedDirectoryChanged = pyqtSignal(str)
    delayedFileChanged = pyqtSignal(str)
    
    def __init__(self, paths=None, parent=None):
        """
        Constructor
        
        @param paths list of paths to be watched
        @type list of str
        @param parent reference to the parent object
        @type QObject
        """
        if paths:
            super(DelayedFileWatcher, self).__init__(paths, parent)
        else:
            super(DelayedFileWatcher, self).__init__(parent)
        
        self.__dirQueue = []
        self.__fileQueue = []
        
        self.directoryChanged.connect(self.__directoryChanged)
        self.fileChanged.connect(self.__fileChanged)
    
    @pyqtSlot(str)
    def __directoryChanged(self, path):
        """
        Private slot handling a changed directory.
        
        @param path name of the changed directory
        @type str
        """
        self.__dirQueue.append(path)
        QTimer.singleShot(500, self.__dequeueDirectory)
    
    @pyqtSlot(str)
    def __fileChanged(self, path):
        """
        Private slot handling a changed file.
        
        @param path name of the changed file
        @type str
        """
        self.__fileQueue.append(path)
        QTimer.singleShot(500, self.__dequeueFile)
    
    @pyqtSlot()
    def __dequeueDirectory(self):
        """
        Private slot to signal a directory change.
        """
        self.delayedDirectoryChanged.emit(self.__dirQueue.pop(0))
    
    @pyqtSlot()
    def __dequeueFile(self):
        """
        Private slot to signal a file change.
        """
        self.delayedFileChanged.emit(self.__fileQueue.pop(0))
