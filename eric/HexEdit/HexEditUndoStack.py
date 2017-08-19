# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Undo stack for the hex edit widget.
"""

from __future__ import unicode_literals

try:
    from enum import Enum
except ImportError:
    from ThirdParty.enum import Enum

from PyQt5.QtWidgets import QUndoStack, QUndoCommand


class HexEditCommand(Enum):
    """
    Class implementing the edit comands.
    """
    Insert = 0
    RemoveAt = 1
    Overwrite = 2


class HexEditUndoCommand(QUndoCommand):
    """
    Class implementing the Undo command.
    """
    def __init__(self, chunks, cmd, pos, newByte, parent=None):
        """
        Constructor
        
        @param chunks reference to the data container
        @type HexEditChunks
        @param cmd edit command
        @type HexEditCommand
        @param pos edit position
        @type int
        @param newByte new byte value
        @type int (range 0 to 255)
        @param parent reference to the parent command
        @type QUndoCommand
        """
        super(HexEditUndoCommand, self).__init__(parent)
        
        self.__chunks = chunks
        self._pos = pos
        self._newByte = newByte
        self._cmd = cmd
        
        self.__wasChanged = False
        self.__oldByte = 0
    
    def undo(self):
        """
        Public method to undo the command.
        """
        if self._cmd == HexEditCommand.Insert:
            self.__chunks.removeAt(self._pos)
        elif self._cmd == HexEditCommand.Overwrite:
            self.__chunks.overwrite(self._pos, self.__oldByte)
            self.__chunks.setDataChanged(self._pos, self.__wasChanged)
        elif self._cmd == HexEditCommand.RemoveAt:
            self.__chunks.insert(self._pos, self.__oldByte)
            self.__chunks.setDataChanged(self._pos, self.__wasChanged)
    
    def redo(self):
        """
        Public method to redo the command.
        """
        if self._cmd == HexEditCommand.Insert:
            self.__chunks.insert(self._pos, self._newByte)
        elif self._cmd == HexEditCommand.Overwrite:
            self.__oldByte = self.__chunks[self._pos]
            self.__wasChanged = self.__chunks.dataChanged(self._pos)
            self.__chunks.overwrite(self._pos, self._newByte)
        elif self._cmd == HexEditCommand.RemoveAt:
            self.__oldByte = self.__chunks[self._pos]
            self.__wasChanged = self.__chunks.dataChanged(self._pos)
            self.__chunks.removeAt(self._pos)
    
    def mergeWith(self, command):
        """
        Public method to merge this command with another one.
        
        @param command reference to the command to merge with
        @type QUndoCommand
        @return flag indicating a successful merge
        @rtype bool
        """
        result = False
        
        if self._cmd != HexEditCommand.RemoveAt:
            if command._cmd == HexEditCommand.Overwrite:
                if command._pos == self._pos:
                    self._newByte = command._newByte
                    result = True
        
        return result
    
    def id(self):
        """
        Public method to get the ID of this undo command class.
        
        @return ID of the undo command class
        @rtype int
        """
        return 4242


class HexEditUndoStack(QUndoStack):
    """
    Class implementing an Undo stack for the hex edit widget.
    """
    def __init__(self, chunks, parent=None):
        """
        Constructor
        
        @param chunks reference to the data container
        @type HexEditChunks
        @param parent reference to the parent object
        @type QObject
        """
        super(HexEditUndoStack, self).__init__(parent)
        
        self.__chunks = chunks
        self.__parent = parent
    
    def insert(self, pos, data):
        """
        Public method to insert a byte.
        
        @param pos position to insert at
        @type int
        @param data byte to be inserted
        @type int (range 0 to 255)
        """
        if pos >= 0 and pos <= self.__chunks.size():
            uc = HexEditUndoCommand(
                self.__chunks, HexEditCommand.Insert, pos, data)
            self.push(uc)
    
    def insertByteArray(self, pos, byteArray):
        """
        Public method to insert bytes.
        
        @param pos position to insert at
        @type int
        @param byteArray data to be inserted
        @type byteArray or QByteArray
        """
        ba = bytearray(byteArray)
        
        if pos >= 0 and pos <= self.__chunks.size():
            txt = self.tr("Inserting %n byte(s)", "", len(ba))
            self.beginMacro(txt)
            for idx in range(len(ba)):
                uc = HexEditUndoCommand(
                    self.__chunks, HexEditCommand.Insert, pos + idx, ba[idx])
                self.push(uc)
            self.endMacro()
    
    def removeAt(self, pos, length=1):
        """
        Public method to remove bytes.
        
        @param pos position to remove bytes from
        @type int
        @param length amount of bytes to remove
        @type int
        """
        if pos >= 0 and pos <= self.__chunks.size():
            if length == 1:
                uc = HexEditUndoCommand(
                    self.__chunks, HexEditCommand.RemoveAt, pos, 0)
                self.push(uc)
            else:
                txt = self.tr("Deleting %n byte(s)", "", length)
                self.beginMacro(txt)
                for cnt in range(length):
                    uc = HexEditUndoCommand(
                        self.__chunks, HexEditCommand.RemoveAt, pos, 0)
                    self.push(uc)
                self.endMacro()
    
    def overwrite(self, pos, data):
        """
        Public method to replace a byte.
        
        @param pos position to replace the byte at
        @type int
        @param data byte to replace with
        @type int (range 0 to 255)
        """
        if pos >= 0 and pos <= self.__chunks.size():
            uc = HexEditUndoCommand(
                self.__chunks, HexEditCommand.Overwrite, pos, data)
            self.push(uc)
    
    def overwriteByteArray(self, pos, length, byteArray):
        """
        Public method to replace bytes.
        
        @param pos position to replace the bytes at
        @type int
        @param length amount of bytes to replace
        @type int
        @param byteArray bytes to replace with
        @type bytearray or QByteArray
        """
        ba = bytearray(byteArray)
        
        if pos >= 0 and pos <= self.__chunks.size():
            txt = self.tr("Inserting %n byte(s)", "", len(ba))
            self.beginMacro(txt)
            self.removeAt(pos, length)
            self.insertByteArray(pos, ba)
            self.endMacro()
