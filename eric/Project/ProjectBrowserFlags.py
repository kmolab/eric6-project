# -*- coding: utf-8 -*-

# Copyright (c) 2008 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module defining the project browser flags.
"""

SourcesBrowserFlag = 1
FormsBrowserFlag = 2
ResourcesBrowserFlag = 4
TranslationsBrowserFlag = 8
InterfacesBrowserFlag = 16
OthersBrowserFlag = 32
AllBrowsersFlag = SourcesBrowserFlag | \
    FormsBrowserFlag | \
    ResourcesBrowserFlag | \
    TranslationsBrowserFlag | \
    InterfacesBrowserFlag | \
    OthersBrowserFlag

#
# eflag: noqa = M702
