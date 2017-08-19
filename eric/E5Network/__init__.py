# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Package implementing some special network related objects and functions.
"""

from __future__ import unicode_literals

from PyQt5.QtNetwork import QAbstractSocket, QHostAddress


def isValidAddress(address):
    """
    Public function to check, if the given address is valid.
    
    @param address IPv4 or IPv6 address string
    @type str
    @return flag indicating validity
    @rtype bool
    """
    h = QHostAddress(address)
    return not h.isNull()


def isValidIPv4Address(address):
    """
    Public function to check, if the given address is a valid IPv4 address.
    
    @param address IPv4 address string
    @type str
    @return flag indicating validity
    @rtype bool
    """
    h = QHostAddress(address)
    return not h.isNull() and h.protocol() == QAbstractSocket.IPv4Protocol


def isValidIPv6Address(address):
    """
    Public function to check, if the given address is a valid IPv6 address.
    
    @param address IPv6 address string
    @type str
    @return flag indicating validity
    @rtype bool
    """
    h = QHostAddress(address)
    return not h.isNull() and h.protocol() == QAbstractSocket.IPv6Protocol
