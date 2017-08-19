# -*- coding: utf-8 -*-

# Copyright (c) 2016 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a ConfigParser wrapper for Python 2 to provide the
dictionary like interface of the Python 3 variant.
"""

from __future__ import unicode_literals

try:
    from configparser import ConfigParser as E5ConfigParser
except ImportError:
    # Py2 part with the compatibility wrapper class
    try:
        from collections import OrderedDict as _default_dict
        # __IGNORE_WARNING_N813__
    except ImportError:
        # fallback for setup.py which hasn't yet built _collections
        _default_dict = dict

    import re
    import itertools
    from ConfigParser import SafeConfigParser, DEFAULTSECT
    
    class E5ConfigParser(SafeConfigParser):
        """
        Class implementing a wrapper of the ConfigParser class implementing
        dictionary like special methods and some enhancements from Python 3.
        """
        _OPT_TMPL = r"""
            (?P<option>.*?)                    # very permissive!
            \s*(?P<vi>{delim})\s*              # any number of space/tab,
                                               # followed by any of the
                                               # allowed delimiters,
                                               # followed by any space/tab
            (?P<value>.*)$                     # everything up to eol
            """
        _OPT_NV_TMPL = r"""
            (?P<option>.*?)                    # very permissive!
            \s*(?:                             # any number of space/tab,
            (?P<vi>{delim})\s*                 # optionally followed by
                                               # any of the allowed
                                               # delimiters, followed by any
                                               # space/tab
            (?P<value>.*))?$                   # everything up to eol
            """
        # Compiled regular expression for matching options with typical
        # separators
        OPTCRE = re.compile(_OPT_TMPL.format(delim="=|:"), re.VERBOSE)
        # Compiled regular expression for matching options with optional
        # values delimited using typical separators
        OPTCRE_NV = re.compile(_OPT_NV_TMPL.format(delim="=|:"), re.VERBOSE)
        
        def __init__(self, defaults=None, dict_type=_default_dict,
                     allow_no_value=False, delimiters=('=', ':')):
            """
            Constructor
            """
            SafeConfigParser.__init__(
                self,
                defaults=defaults, dict_type=dict_type,
                allow_no_value=allow_no_value)
            
            if delimiters == ('=', ':'):
                self._optcre = \
                    self.OPTCRE_NV if allow_no_value else self.OPTCRE
            else:
                d = "|".join(re.escape(d) for d in delimiters)
                if allow_no_value:
                    self._optcre = re.compile(
                        self._OPT_NV_TMPL.format(delim=d), re.VERBOSE)
                else:
                    self._optcre = re.compile(
                        self._OPT_TMPL.format(delim=d), re.VERBOSE)
        
        def __getitem__(self, key):
            """
            Special method to get a section.
            
            @param key name of the section
            @type str
            @return section for the given key
            @rtype dict
            @exception KeyError raised if a non-existent key is given
            """
            if key == DEFAULTSECT:
                return self._defaults
            elif self.has_section(key):
                return self._sections[key]
            else:
                raise KeyError(key)
        
        def __setitem__(self, key, values):
            """
            Special method to set the values of a section.
            
            @param key name of the section
            @type str
            @param values value for the section
            @type dict
            """
            # To conform with the mapping protocol, overwrites existing values
            # in the section.
            if key == DEFAULTSECT:
                self._defaults.clear()
            elif self.has_section(key):
                self._sections[key].clear()
            else:
                self.add_section(key)
            for subkey, value in values.items():
                subkey = self.optionxform(str(subkey))
                if value is not None:
                    value = str(value)
                self.set(key, subkey, value)
        
        def __delitem__(self, key):
            """
            Special method to delete a section.
            
            @param key name of the section
            @type str
            @exception ValueError raised to indicate non-removal of the
                default section
            @exception KeyError raised to indicate a non-existent section
            """
            if key == DEFAULTSECT:
                raise ValueError("Cannot remove the default section.")
            if not self.has_section(key):
                raise KeyError(key)
            self.remove_section(key)
        
        def __contains__(self, key):
            """
            Special method to test, if a section is contained in the config.
            
            @param key name of the section
            @type str
            @return flag indicating containment
            @rtype bool
            """
            return key == DEFAULTSECT or self.has_section(key)
        
        def __len__(self):
            """
            Special method get the number of sections of the config.
            
            @return number of sections
            @rtype int
            """
            return len(self._sections) + 1  # the default section
        
        def __iter__(self):
            """
            Special method to return an iterator of the section names starting
            with the default section.
            
            @return iterator of the section names contained in the config
            @rtype iterator of str
            """
            return itertools.chain((DEFAULTSECT,), self._sections.keys())


if __name__ == "__main__":
    # This is some test code.
    import sys
    
    c = E5ConfigParser()
    c["DEFAULT"] = {'ServerAliveInterval': '45',
                    'Compression': 'yes',
                    'CompressionLevel': '9'}
    c['bitbucket.org'] = {}
    c['bitbucket.org']['User'] = 'hg'
    c['topsecret.server.com'] = {}
    topsecret = c['topsecret.server.com']
    topsecret['Port'] = '50022'
    topsecret['ForwardX11'] = 'no'
    c['DEFAULT']['ForwardX11'] = 'yes'
    
    c.write(sys.stdout)
