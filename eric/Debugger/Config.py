# -*- coding: utf-8 -*-

# Copyright (c) 2002 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module defining the different Python types and their display strings.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QT_TRANSLATE_NOOP

# Variables type definition
# Special case for Python 2: don't add 'instancemethod'. It's renamed to
# 'method' in DebugClientBase.py to be identical to Python 3
ConfigVarTypeDispStrings = {
    '__': QT_TRANSLATE_NOOP('Variable Types', 'Hidden Attributes'),
    'NoneType': QT_TRANSLATE_NOOP('Variable Types', 'None'),
    'type': QT_TRANSLATE_NOOP('Variable Types', 'Type'),
    'bool': QT_TRANSLATE_NOOP('Variable Types', 'Boolean'),
    'int': QT_TRANSLATE_NOOP('Variable Types', 'Integer'),
    'long': QT_TRANSLATE_NOOP('Variable Types', 'Long Integer'),
    'float': QT_TRANSLATE_NOOP('Variable Types', 'Float'),
    'complex': QT_TRANSLATE_NOOP('Variable Types', 'Complex'),
    'str': QT_TRANSLATE_NOOP('Variable Types', 'String'),
    'unicode': QT_TRANSLATE_NOOP('Variable Types', 'Unicode String'),
    'tuple': QT_TRANSLATE_NOOP('Variable Types', 'Tuple'),
    'list': QT_TRANSLATE_NOOP('Variable Types', 'List/Array'),
    'dict': QT_TRANSLATE_NOOP('Variable Types', 'Dictionary/Hash/Map'),
    'dict-proxy': QT_TRANSLATE_NOOP('Variable Types', 'Dictionary Proxy'),
    'set': QT_TRANSLATE_NOOP('Variable Types', 'Set'),
    'frozenset': QT_TRANSLATE_NOOP('Variable Types', 'Frozen Set'),
    'file': QT_TRANSLATE_NOOP('Variable Types', 'File'),
    'xrange': QT_TRANSLATE_NOOP('Variable Types', 'X Range'),
    'slice': QT_TRANSLATE_NOOP('Variable Types', 'Slice'),
    'buffer': QT_TRANSLATE_NOOP('Variable Types', 'Buffer'),
    'class': QT_TRANSLATE_NOOP('Variable Types', 'Class'),
    'instance': QT_TRANSLATE_NOOP('Variable Types', 'Class Instance'),
    'method': QT_TRANSLATE_NOOP('Variable Types', 'Class Method'),
    'property': QT_TRANSLATE_NOOP('Variable Types', 'Class Property'),
    'generator': QT_TRANSLATE_NOOP('Variable Types', 'Generator'),
    'function': QT_TRANSLATE_NOOP('Variable Types', 'Function'),
    'builtin_function_or_method':
        QT_TRANSLATE_NOOP('Variable Types', 'Builtin Function'),
    'code': QT_TRANSLATE_NOOP('Variable Types', 'Code'),
    'module': QT_TRANSLATE_NOOP('Variable Types', 'Module'),
    'ellipsis': QT_TRANSLATE_NOOP('Variable Types', 'Ellipsis'),
    'traceback': QT_TRANSLATE_NOOP('Variable Types', 'Traceback'),
    'frame': QT_TRANSLATE_NOOP('Variable Types', 'Frame'),
    'other': QT_TRANSLATE_NOOP('Variable Types', 'Other'),
}


ConfigVarTypeFilters = {
    '__': 0,
    'NoneType': 1,
    'type': 2,
    'bool': 3,
    'int': 4,
    'long': 5,
    'float': 6,
    'complex': 7,
    'str': 8,
    'unicode': 9,
    'tuple': 10,
    'list': 11,
    'dict': 12,
    'dict-proxy': 13,
    'set': 14,
    'file': 15,
    'xrange': 16,
    'slice': 17,
    'buffer': 18,
    'class': 19,
    'instance': 20,
    'method': 21,
    'property': 22,
    'generator': 23,
    'function': 24,
    'builtin_function_or_method': 25,
    'code': 26,
    'module': 27,
    'ellipsis': 28,
    'traceback': 29,
    'frame': 30,
    'other': 31,
    'frozenset': 32,
}
