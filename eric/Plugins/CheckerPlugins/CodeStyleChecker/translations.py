# -*- coding: utf-8 -*-

# Copyright (c) 2014 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing message translations for the code style plugin messages.
"""

from __future__ import unicode_literals

from PyQt5.QtCore import QCoreApplication

from Globals import translate

__all__ = ["getTranslatedMessage"]

_messages = {
    "E101": QCoreApplication.translate(
        "pycodestyle",
        "indentation contains mixed spaces and tabs"),
    "E111": QCoreApplication.translate(
        "pycodestyle",
        "indentation is not a multiple of four"),
    "E112": QCoreApplication.translate(
        "pycodestyle",
        "expected an indented block"),
    "E113": QCoreApplication.translate(
        "pycodestyle",
        "unexpected indentation"),
    "E114": QCoreApplication.translate(
        "pycodestyle",
        "indentation is not a multiple of four (comment)"),
    "E115": QCoreApplication.translate(
        "pycodestyle",
        "expected an indented block (comment)"),
    "E116": QCoreApplication.translate(
        "pycodestyle",
        "unexpected indentation (comment)"),
    "E121": QCoreApplication.translate(
        "pycodestyle",
        "continuation line indentation is not a multiple of four"),
    "E122": QCoreApplication.translate(
        "pycodestyle",
        "continuation line missing indentation or outdented"),
    "E123": QCoreApplication.translate(
        "pycodestyle",
        "closing bracket does not match indentation of opening"
        " bracket's line"),
    "E124": QCoreApplication.translate(
        "pycodestyle",
        "closing bracket does not match visual indentation"),
    "E125": QCoreApplication.translate(
        "pycodestyle",
        "continuation line with same indent as next logical line"),
    "E126": QCoreApplication.translate(
        "pycodestyle",
        "continuation line over-indented for hanging indent"),
    "E127": QCoreApplication.translate(
        "pycodestyle",
        "continuation line over-indented for visual indent"),
    "E128": QCoreApplication.translate(
        "pycodestyle",
        "continuation line under-indented for visual indent"),
    "E129": QCoreApplication.translate(
        "pycodestyle",
        "visually indented line with same indent as next logical line"),
    "E131": QCoreApplication.translate(
        "pycodestyle",
        "continuation line unaligned for hanging indent"),
    "E133": QCoreApplication.translate(
        "pycodestyle",
        "closing bracket is missing indentation"),
    "W191": QCoreApplication.translate(
        "pycodestyle",
        "indentation contains tabs"),
    "E201": QCoreApplication.translate(
        "pycodestyle",
        "whitespace after '{0}'"),
    "E202": QCoreApplication.translate(
        "pycodestyle",
        "whitespace before '{0}'"),
    "E203": QCoreApplication.translate(
        "pycodestyle",
        "whitespace before '{0}'"),
    "E211": QCoreApplication.translate(
        "pycodestyle",
        "whitespace before '{0}'"),
    "E221": QCoreApplication.translate(
        "pycodestyle",
        "multiple spaces before operator"),
    "E222": QCoreApplication.translate(
        "pycodestyle",
        "multiple spaces after operator"),
    "E223": QCoreApplication.translate(
        "pycodestyle",
        "tab before operator"),
    "E224": QCoreApplication.translate(
        "pycodestyle",
        "tab after operator"),
    "E225": QCoreApplication.translate(
        "pycodestyle",
        "missing whitespace around operator"),
    "E226": QCoreApplication.translate(
        "pycodestyle",
        "missing whitespace around arithmetic operator"),
    "E227": QCoreApplication.translate(
        "pycodestyle",
        "missing whitespace around bitwise or shift operator"),
    "E228": QCoreApplication.translate(
        "pycodestyle",
        "missing whitespace around modulo operator"),
    "E231": QCoreApplication.translate(
        "pycodestyle",
        "missing whitespace after '{0}'"),
    "E241": QCoreApplication.translate(
        "pycodestyle",
        "multiple spaces after '{0}'"),
    "E242": QCoreApplication.translate(
        "pycodestyle",
        "tab after '{0}'"),
    "E251": QCoreApplication.translate(
        "pycodestyle",
        "unexpected spaces around keyword / parameter equals"),
    "E261": QCoreApplication.translate(
        "pycodestyle",
        "at least two spaces before inline comment"),
    "E262": QCoreApplication.translate(
        "pycodestyle",
        "inline comment should start with '# '"),
    "E265": QCoreApplication.translate(
        "pycodestyle",
        "block comment should start with '# '"),
    "E266": QCoreApplication.translate(
        "pycodestyle",
        "too many leading '#' for block comment"),
    "E271": QCoreApplication.translate(
        "pycodestyle",
        "multiple spaces after keyword"),
    "E272": QCoreApplication.translate(
        "pycodestyle",
        "multiple spaces before keyword"),
    "E273": QCoreApplication.translate(
        "pycodestyle",
        "tab after keyword"),
    "E274": QCoreApplication.translate(
        "pycodestyle",
        "tab before keyword"),
    "E275": QCoreApplication.translate(
        "pycodestyle",
        "missing whitespace after keyword"),
    "W291": QCoreApplication.translate(
        "pycodestyle",
        "trailing whitespace"),
    "W292": QCoreApplication.translate(
        "pycodestyle",
        "no newline at end of file"),
    "W293": QCoreApplication.translate(
        "pycodestyle",
        "blank line contains whitespace"),
    "E301": QCoreApplication.translate(
        "pycodestyle",
        "expected 1 blank line, found 0"),
    "E302": QCoreApplication.translate(
        "pycodestyle",
        "expected 2 blank lines, found {0}"),
    "E303": QCoreApplication.translate(
        "pycodestyle",
        "too many blank lines ({0})"),
    "E304": QCoreApplication.translate(
        "pycodestyle",
        "blank lines found after function decorator"),
    "E305": QCoreApplication.translate(
        "pycodestyle",
        "expected 2 blank lines after class or function definition,"
        " found {0}"),
    "E306": QCoreApplication.translate(
        "pycodestyle",
        "expected 1 blank line before a nested definition, found 0"),
    "W391": QCoreApplication.translate(
        "pycodestyle",
        "blank line at end of file"),
    "E401": QCoreApplication.translate(
        "pycodestyle",
        "multiple imports on one line"),
    "E402": QCoreApplication.translate(
        "pycodestyle",
        "module level import not at top of file"),
    "E501": QCoreApplication.translate(
        "pycodestyle",
        "line too long ({0} > {1} characters)"),
    "E502": QCoreApplication.translate(
        "pycodestyle",
        "the backslash is redundant between brackets"),
    "W503": QCoreApplication.translate(
        "pycodestyle",
        "line break before binary operator"),
    "W601": QCoreApplication.translate(
        "pycodestyle",
        ".has_key() is deprecated, use 'in'"),
    "W602": QCoreApplication.translate(
        "pycodestyle",
        "deprecated form of raising exception"),
    "W603": QCoreApplication.translate(
        "pycodestyle",
        "'<>' is deprecated, use '!='"),
    "W604": QCoreApplication.translate(
        "pycodestyle",
        "backticks are deprecated, use 'repr()'"),
    "E701": QCoreApplication.translate(
        "pycodestyle",
        "multiple statements on one line (colon)"),
    "E702": QCoreApplication.translate(
        "pycodestyle",
        "multiple statements on one line (semicolon)"),
    "E703": QCoreApplication.translate(
        "pycodestyle",
        "statement ends with a semicolon"),
    "E704": QCoreApplication.translate(
        "pycodestyle",
        "multiple statements on one line (def)"),
    "E711": QCoreApplication.translate(
        "pycodestyle",
        "comparison to {0} should be {1}"),
    "E712": QCoreApplication.translate(
        "pycodestyle",
        "comparison to {0} should be {1}"),
    "E713": QCoreApplication.translate(
        "pycodestyle",
        "test for membership should be 'not in'"),
    "E714": QCoreApplication.translate(
        "pycodestyle",
        "test for object identity should be 'is not'"),
    "E721": QCoreApplication.translate(
        "pycodestyle",
        "do not compare types, use 'isinstance()'"),
    "E722": QCoreApplication.translate(
        "pycodestyle",
        "do not use bare except"),
    "E731": QCoreApplication.translate(
        "pycodestyle",
        "do not assign a lambda expression, use a def"),
    "E741": QCoreApplication.translate(
        "pycodestyle",
        "ambiguous variable name '{0}'"),
    "E742": QCoreApplication.translate(
        "pycodestyle",
        "ambiguous class definition '{0}'"),
    "E743": QCoreApplication.translate(
        "pycodestyle",
        "ambiguous function definition '{0}'"),
    "E901": QCoreApplication.translate(
        "pycodestyle",
        "{0}: {1}"),
    "E902": QCoreApplication.translate(
        "pycodestyle",
        "{0}"),

    # DocStyleChecker messages
    "D101": QCoreApplication.translate(
        "DocStyleChecker", "module is missing a docstring"),
    "D102": QCoreApplication.translate(
        "DocStyleChecker",
        "public function/method is missing a docstring"),
    "D103": QCoreApplication.translate(
        "DocStyleChecker",
        "private function/method may be missing a docstring"),
    "D104": QCoreApplication.translate(
        "DocStyleChecker", "public class is missing a docstring"),
    "D105": QCoreApplication.translate(
        "DocStyleChecker", "private class may be missing a docstring"),
    "D111": QCoreApplication.translate(
        "DocStyleChecker", 'docstring not surrounded by """'),
    "D112": QCoreApplication.translate(
        "DocStyleChecker",
        'docstring containing \\ not surrounded by r"""'),
    "D113": QCoreApplication.translate(
        "DocStyleChecker",
        'docstring containing unicode character not surrounded by u"""'),
    "D121": QCoreApplication.translate(
        "DocStyleChecker", "one-liner docstring on multiple lines"),
    "D122": QCoreApplication.translate(
        "DocStyleChecker", "docstring has wrong indentation"),
    "D130": QCoreApplication.translate(
        "DocStyleChecker", "docstring does not contain a summary"),
    "D131": QCoreApplication.translate(
        "DocStyleChecker", "docstring summary does not end with a period"),
    "D132": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring summary is not in imperative mood"
        " (Does instead of Do)"),
    "D133": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring summary looks like a function's/method's signature"),
    "D134": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring does not mention the return value type"),
    "D141": QCoreApplication.translate(
        "DocStyleChecker",
        "function/method docstring is separated by a blank line"),
    "D142": QCoreApplication.translate(
        "DocStyleChecker",
        "class docstring is not preceded by a blank line"),
    "D143": QCoreApplication.translate(
        "DocStyleChecker",
        "class docstring is not followed by a blank line"),
    "D144": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring summary is not followed by a blank line"),
    "D145": QCoreApplication.translate(
        "DocStyleChecker",
        "last paragraph of docstring is not followed by a blank line"),
    
    "D203": QCoreApplication.translate(
        "DocStyleChecker",
        "private function/method is missing a docstring"),
    "D205": QCoreApplication.translate(
        "DocStyleChecker", "private class is missing a docstring"),
    "D221": QCoreApplication.translate(
        "DocStyleChecker",
        "leading quotes of docstring not on separate line"),
    "D222": QCoreApplication.translate(
        "DocStyleChecker",
        "trailing quotes of docstring not on separate line"),
    "D231": QCoreApplication.translate(
        "DocStyleChecker", "docstring summary does not end with a period"),
    "D232": QCoreApplication.translate(
        "DocStyleChecker", "docstring summary does not start with '{0}'"),
    "D234": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring does not contain a @return line but function/method"
        " returns something"),
    "D235": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring contains a @return line but function/method doesn't"
        " return anything"),
    "D236": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring does not contain enough @param/@keyparam lines"),
    "D237": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring contains too many @param/@keyparam lines"),
    "D238": QCoreApplication.translate(
        "DocStyleChecker",
        "keyword only arguments must be documented with @keyparam lines"),
    "D239": QCoreApplication.translate(
        "DocStyleChecker", "order of @param/@keyparam lines does"
        " not match the function/method signature"),
    "D242": QCoreApplication.translate(
        "DocStyleChecker", "class docstring is preceded by a blank line"),
    "D243": QCoreApplication.translate(
        "DocStyleChecker", "class docstring is followed by a blank line"),
    "D244": QCoreApplication.translate(
        "DocStyleChecker",
        "function/method docstring is preceded by a blank line"),
    "D245": QCoreApplication.translate(
        "DocStyleChecker",
        "function/method docstring is followed by a blank line"),
    "D246": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring summary is not followed by a blank line"),
    "D247": QCoreApplication.translate(
        "DocStyleChecker",
        "last paragraph of docstring is followed by a blank line"),
    "D250": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring does not contain a @exception line but function/method"
        " raises an exception"),
    "D251": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring contains a @exception line but function/method doesn't"
        " raise an exception"),
    "D252": QCoreApplication.translate(
        "DocStyleChecker",
        "raised exception '{0}' is not documented in docstring"),
    "D253": QCoreApplication.translate(
        "DocStyleChecker",
        "documented exception '{0}' is not raised"),
    "D260": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring does not contain a @signal line but class defines signals"),
    "D261": QCoreApplication.translate(
        "DocStyleChecker",
        "docstring contains a @signal line but class doesn't define signals"),
    "D262": QCoreApplication.translate(
        "DocStyleChecker",
        "defined signal '{0}' is not documented in docstring"),
    "D263": QCoreApplication.translate(
        "DocStyleChecker",
        "documented signal '{0}' is not defined"),
    
    "D901": QCoreApplication.translate(
        "DocStyleChecker", "{0}: {1}"),

    # NamingStyleChecker messages
    "N801": QCoreApplication.translate(
        "NamingStyleChecker",
        "class names should use CapWords convention"),
    "N802": QCoreApplication.translate(
        "NamingStyleChecker",
        "function name should be lowercase"),
    "N803": QCoreApplication.translate(
        "NamingStyleChecker",
        "argument name should be lowercase"),
    "N804": QCoreApplication.translate(
        "NamingStyleChecker",
        "first argument of a class method should be named 'cls'"),
    "N805": QCoreApplication.translate(
        "NamingStyleChecker",
        "first argument of a method should be named 'self'"),
    "N806": QCoreApplication.translate(
        "NamingStyleChecker",
        "first argument of a static method should not be named"
        " 'self' or 'cls"),
    "N807": QCoreApplication.translate(
        "NamingStyleChecker",
        "module names should be lowercase"),
    "N808": QCoreApplication.translate(
        "NamingStyleChecker",
        "package names should be lowercase"),
    "N811": QCoreApplication.translate(
        "NamingStyleChecker",
        "constant imported as non constant"),
    "N812": QCoreApplication.translate(
        "NamingStyleChecker",
        "lowercase imported as non lowercase"),
    "N813": QCoreApplication.translate(
        "NamingStyleChecker",
        "camelcase imported as lowercase"),
    "N814": QCoreApplication.translate(
        "NamingStyleChecker",
        "camelcase imported as constant"),
    "N821": QCoreApplication.translate(
        "NamingStyleChecker",
        "variable in function should be lowercase"),
    "N831": QCoreApplication.translate(
        "NamingStyleChecker",
        "names 'l', 'O' and 'I' should be avoided"),

    # Code complexity messages
    "C101": QCoreApplication.translate(
        "ComplexityChecker", "'{0}' is too complex ({1})"),
    "C111": QCoreApplication.translate(
        "ComplexityChecker", "source code line is too complex ({0})"),
    "C112": QCoreApplication.translate(
        "ComplexityChecker",
        "overall source code line complexity is too high ({0})"),
    "C901": QCoreApplication.translate(
        "ComplexityChecker", "{0}: {1}"),
    
    # Messages of the Miscellaneous Checker
    "M101": QCoreApplication.translate(
        "MiscellaneousChecker",
        "coding magic comment not found"),
    "M102": QCoreApplication.translate(
        "MiscellaneousChecker",
        "unknown encoding ({0}) found in coding magic comment"),
    "M111": QCoreApplication.translate(
        "MiscellaneousChecker",
        "copyright notice not present"),
    "M112": QCoreApplication.translate(
        "MiscellaneousChecker",
        "copyright notice contains invalid author"),
    "M131": QCoreApplication.translate(
        "MiscellaneousChecker",
        '"{0}" is a Python builtin and is being shadowed; '
        'consider renaming the variable'),
    "M132": QCoreApplication.translate(
        "MiscellaneousChecker",
        '"{0}" is used as an argument and thus shadows a '
        'Python builtin; consider renaming the argument'),
    "M191": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary generator - rewrite as a list comprehension'),
    "M192": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary generator - rewrite as a set comprehension'),
    "M193": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary generator - rewrite as a dict comprehension'),
    "M194": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary list comprehension - rewrite as a set comprehension'),
    "M195": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary list comprehension - rewrite as a dict comprehension'),
    "M196": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary list literal - rewrite as a set literal'),
    "M197": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary list literal - rewrite as a dict literal'),
    "M198": QCoreApplication.translate(
        "MiscellaneousChecker",
        'unnecessary list comprehension - "{0}" can take a generator'),
    "M601": QCoreApplication.translate(
        "MiscellaneousChecker",
        "found {0} formatter"),
    "M611": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format string does contain unindexed parameters"),
    "M612": QCoreApplication.translate(
        "MiscellaneousChecker",
        "docstring does contain unindexed parameters"),
    "M613": QCoreApplication.translate(
        "MiscellaneousChecker",
        "other string does contain unindexed parameters"),
    "M621": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format call uses too large index ({0})"),
    "M622": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format call uses missing keyword ({0})"),
    "M623": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format call uses keyword arguments but no named entries"),
    "M624": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format call uses variable arguments but no numbered entries"),
    "M625": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format call uses implicit and explicit indexes together"),
    "M631": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format call provides unused index ({0})"),
    "M632": QCoreApplication.translate(
        "MiscellaneousChecker",
        "format call provides unused keyword ({0})"),
    "M701": QCoreApplication.translate(
        "MiscellaneousChecker",
        "expected these __future__ imports: {0}; but only got: {1}"),
    "M702": QCoreApplication.translate(
        "MiscellaneousChecker",
        "expected these __future__ imports: {0}; but got none"),
    "M801": QCoreApplication.translate(
        "MiscellaneousChecker",
        "print statement found"),
    "M811": QCoreApplication.translate(
        "MiscellaneousChecker",
        "one element tuple found"),
    "M821": QCoreApplication.translate(
        "MiscellaneousChecker",
        "mutable default argument of type {0}"),
    "M822": QCoreApplication.translate(
        "MiscellaneousChecker",
        "mutable default argument of type {0}"),
    "M901": QCoreApplication.translate(
        "MiscellaneousChecker",
        "{0}: {1}"),
    
    # CodeStyleFixer messages
    "FD111": QCoreApplication.translate(
        'CodeStyleFixer',
        "Triple single quotes converted to triple double quotes."),
    'FD112': QCoreApplication.translate(
        'CodeStyleFixer',
        'Introductory quotes corrected to be {0}"""'),
    "FD121": QCoreApplication.translate(
        'CodeStyleFixer',
        "Single line docstring put on one line."),
    "FD131": QCoreApplication.translate(
        'CodeStyleFixer',
        "Period added to summary line."),
    "FD141": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line before function/method docstring removed."),
    "FD142": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line inserted before class docstring."),
    "FD143": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line inserted after class docstring."),
    "FD144": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line inserted after docstring summary."),
    "FD145": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line inserted after last paragraph of docstring."),
    "FD221": QCoreApplication.translate(
        'CodeStyleFixer',
        "Leading quotes put on separate line."),
    "FD222": QCoreApplication.translate(
        'CodeStyleFixer',
        "Trailing quotes put on separate line."),
    "FD242": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line before class docstring removed."),
    "FD244": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line before function/method docstring removed."),
    "FD243": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line after class docstring removed."),
    "FD245": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line after function/method docstring removed."),
    "FD247": QCoreApplication.translate(
        'CodeStyleFixer',
        "Blank line after last paragraph removed."),
    "FE101": QCoreApplication.translate(
        'CodeStyleFixer',
        "Tab converted to 4 spaces."),
    "FE111": QCoreApplication.translate(
        'CodeStyleFixer',
        "Indentation adjusted to be a multiple of four."),
    "FE121": QCoreApplication.translate(
        'CodeStyleFixer',
        "Indentation of continuation line corrected."),
    "FE124": QCoreApplication.translate(
        'CodeStyleFixer',
        "Indentation of closing bracket corrected."),
    "FE122": QCoreApplication.translate(
        'CodeStyleFixer',
        "Missing indentation of continuation line corrected."),
    "FE123": QCoreApplication.translate(
        'CodeStyleFixer',
        "Closing bracket aligned to opening bracket."),
    "FE125": QCoreApplication.translate(
        'CodeStyleFixer',
        "Indentation level changed."),
    "FE126": QCoreApplication.translate(
        'CodeStyleFixer',
        "Indentation level of hanging indentation changed."),
    "FE127": QCoreApplication.translate(
        'CodeStyleFixer',
        "Visual indentation corrected."),
    "FE201": QCoreApplication.translate(
        'CodeStyleFixer',
        "Extraneous whitespace removed."),
    "FE225": QCoreApplication.translate(
        'CodeStyleFixer',
        "Missing whitespace added."),
    "FE221": QCoreApplication.translate(
        'CodeStyleFixer',
        "Extraneous whitespace removed."),
    "FE231": QCoreApplication.translate(
        'CodeStyleFixer',
        "Missing whitespace added."),
    "FE251": QCoreApplication.translate(
        'CodeStyleFixer',
        "Extraneous whitespace removed."),
    "FE261": QCoreApplication.translate(
        'CodeStyleFixer',
        "Whitespace around comment sign corrected."),
    "FE301": QCoreApplication.translate(
        'CodeStyleFixer',
        "One blank line inserted."),
    
    "FE302+": lambda n=1: translate(
        'CodeStyleFixer',
        "%n blank line(s) inserted.", '', n),
    "FE302-": lambda n=1: translate(
        'CodeStyleFixer',
        "%n superfluous lines removed", '', n),
    
    "FE303": QCoreApplication.translate(
        'CodeStyleFixer',
        "Superfluous blank lines removed."),
    "FE304": QCoreApplication.translate(
        'CodeStyleFixer',
        "Superfluous blank lines after function decorator removed."),
    "FE401": QCoreApplication.translate(
        'CodeStyleFixer',
        "Imports were put on separate lines."),
    "FE501": QCoreApplication.translate(
        'CodeStyleFixer',
        "Long lines have been shortened."),
    "FE502": QCoreApplication.translate(
        'CodeStyleFixer',
        "Redundant backslash in brackets removed."),
    "FE701": QCoreApplication.translate(
        'CodeStyleFixer',
        "Compound statement corrected."),
    "FE702": QCoreApplication.translate(
        'CodeStyleFixer',
        "Compound statement corrected."),
    "FE711": QCoreApplication.translate(
        'CodeStyleFixer',
        "Comparison to None/True/False corrected."),
    "FN804": QCoreApplication.translate(
        'CodeStyleFixer',
        "'{0}' argument added."),
    "FN806": QCoreApplication.translate(
        'CodeStyleFixer',
        "'{0}' argument removed."),
    "FW291": QCoreApplication.translate(
        'CodeStyleFixer',
        "Whitespace stripped from end of line."),
    "FW292": QCoreApplication.translate(
        'CodeStyleFixer',
        "newline added to end of file."),
    "FW391": QCoreApplication.translate(
        'CodeStyleFixer',
        "Superfluous trailing blank lines removed from end of file."),
    "FW603": QCoreApplication.translate(
        'CodeStyleFixer',
        "'<>' replaced by '!='."),
        
    "FWRITE_ERROR": QCoreApplication.translate(
        'CodeStyleFixer',
        "Could not save the file! Skipping it. Reason: {0}"),
}

_messages_sample_args = {
    "E201": ["([{"],
    "E202": ["}])"],
    "E203": [",;:"],
    "E211": ["(["],
    "E231": [",;:"],
    "E241": [",;:"],
    "E242": [",;:"],
    "E302": [1],
    "E303": [3],
    "E305": [1],
    "E501": [85, 79],
    "E711": ["None", "'if cond is None:'"],
    "E712": ["True", "'if cond is True:' or 'if cond:'"],
    "E741": ["l"],
    "E742": ["l"],
    "E743": ["l"],
    "E901": ["SyntaxError", "Invalid Syntax"],
    "E902": ["IOError"],
    "D232": ["public"],
    "D252": ["RuntimeError"],
    "D253": ["RuntimeError"],
    "D262": ["buttonClicked"],
    "D263": ["buttonClicked"],
    "D901": ["SyntaxError", "Invalid Syntax"],
    "C101": ["foo.bar", "42"],
    "C111": [42],
    "C112": [12.0],
    "C901": ["SyntaxError", "Invalid Syntax"],
    "M102": ["enc42"],
    "M131": ["list"],
    "M132": ["list"],
    "M198": ["sorted"],
    "M601": ["%s"],
    "M621": [5],
    "M622": ["foo"],
    "M631": [5],
    "M632": ["foo"],
    "M701": ["print_function, unicode_literals", "print_function"],
    "M702": ["print_function, unicode_literals"],
    "M821": ["Dict"],
    "M822": ["Call"],
    "M901": ["SyntaxError", "Invalid Syntax"],
    "FWRITE_ERROR": ["IOError"],
}


def getTranslatedMessage(message):
    """
    Module function to get a translated and formatted message for a
    given pyflakes message ID.
    
    @param message the message ID (string)
    @return translated and formatted message (string)
    """
    if isinstance(message, list):
        message, args = message
    else:
        args = []

    if message in _messages:
        if isinstance(args, int):
            # Retranslate with correct plural form
            return _messages[message](args)
        else:
            if message.startswith(('FD', 'FE', 'FN', 'FW')):
                prefix = ''
            else:
                prefix = message + ' '
            return prefix + _messages[message].format(*args)
    elif ' ' in message:
        # already translated
        return message
    else:
        return QCoreApplication.translate(
            "CodeStyleFixer", " no message defined for code '{0}'")\
            .format(message)
