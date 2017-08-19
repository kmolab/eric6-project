# -*- coding: utf-8 -*-

# Copyright (c) 2014 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing message translations for pyflakes warning messages.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QCoreApplication

__all__ = ["getTranslatedFlakesMessage"]

_messages = {
    'F01': QCoreApplication.translate(
        'pyFlakes',
        '{0!r} imported but unused.'),
    'F02': QCoreApplication.translate(
        'pyFlakes',
        'Redefinition of unused {0!r} from line {1!r}.'),
    'F03': QCoreApplication.translate(
        'pyFlakes',
        'Import {0!r} from line {1!r} shadowed by loop variable.'),
    'F04': QCoreApplication.translate(
        'pyFlakes',
        "'from {0} import *' used; unable to detect undefined names."),
    'F05': QCoreApplication.translate(
        'pyFlakes',
        'Undefined name {0!r}.'),
    'F06': QCoreApplication.translate(
        'pyFlakes',
        'Undefined name {0!r} in __all__.'),
    'F07': QCoreApplication.translate(
        'pyFlakes',
        "Local variable {0!r} (defined in enclosing scope on line {1!r})"
        " referenced before assignment."),
    'F08': QCoreApplication.translate(
        'pyFlakes',
        'Duplicate argument {0!r} in function definition.'),
    'F09': QCoreApplication.translate(
        'pyFlakes',
        'Redefinition of {0!r} from line {1!r}.'),
    'F10': QCoreApplication.translate(
        'pyFlakes',
        'from __future__ imports must occur at the beginning of the file'),
    'F11': QCoreApplication.translate(
        'pyFlakes',
        'Local variable {0!r} is assigned to but never used.'),
    'F12': QCoreApplication.translate(
        'pyFlakes',
        'List comprehension redefines {0!r} from line {1!r}.'),
    'F13': QCoreApplication.translate(
        'pyFlakes',
        'Syntax error detected in doctest.'),
    'F14': QCoreApplication.translate(
        'pyFlakes',
        "'return' with argument inside generator"),
    'F15': QCoreApplication.translate(
        'pyFlakes',
        "'return' outside function"),
    'F16': QCoreApplication.translate(
        'pyFlakes',
        "'from {0} import *' only allowed at module level"),
    'F17': QCoreApplication.translate(
        'pyFlakes',
        "{0!r} may be undefined, or defined from star imports: {1}"),
    'F18': QCoreApplication.translate(
        'pyFlakes',
        "Dictionary key {0!r} repeated with different values"),
    'F19': QCoreApplication.translate(
        'pyFlakes',
        "Dictionary key variable {0} repeated with different values"),
    'F20': QCoreApplication.translate(
        'pyFlakes',
        "Future feature {0} is not defined"),
    'F21': QCoreApplication.translate(
        'pyFlakes',
        "'yield' outside function"),
    'F22': QCoreApplication.translate(
        'pyFlakes',
        "'continue' not properly in loop"),
    'F23': QCoreApplication.translate(
        'pyFlakes',
        "'break' outside loop"),
    'F24': QCoreApplication.translate(
        'pyFlakes',
        "'continue' not supported inside 'finally' clause"),
    'F25': QCoreApplication.translate(
        'pyFlakes',
        "Default 'except:' must be last"),
    'F26': QCoreApplication.translate(
        'pyFlakes',
        "Two starred expressions in assignment"),
    'F27': QCoreApplication.translate(
        'pyFlakes',
        "Too many expressions in star-unpacking assignment"),
    'F28': QCoreApplication.translate(
        'pyFlakes',
        "Assertion is always true, perhaps remove parentheses?"),
}


def getTranslatedFlakesMessage(message_id, message_args):
    """
    Module function to get a translated and formatted message for a
    given pyflakes message ID.
    
    @param message_id message ID (string)
    @param message_args arguments for a formatted message (list)
    @return translated and formatted message (string)
    """
    if message_id in _messages:
        # Avoid leading "u" at Python2 unicode strings
        msg = _messages[message_id].replace("{0!r}", "'{0}'")
        msg = msg.replace("{1!r}", "'{1}'")
        return msg.format(*message_args)
    else:
        return QCoreApplication.translate(
            "pyFlakes", "no message defined for code '{0}'")\
            .format(message_id)
