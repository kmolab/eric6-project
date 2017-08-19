# -*- coding: utf-8 -*-

# Copyright (c) 2003 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the index generator for the builtin documentation
generator.
"""

from __future__ import unicode_literals

import sys
import os

from Utilities import joinext


class IndexGenerator(object):
    """
    Class implementing the index generator for the builtin documentation
    generator.
    """
    def __init__(self, outputDir, colors, stylesheet=None):
        """
        Constructor
        
        @param outputDir The output directory for the files. (string)
        @param colors Dictionary specifying the various colors for the output.
            (dictionary of strings)
        @param stylesheet the style to be used for the generated pages (string)
        """
        self.outputDir = outputDir
        self.packages = {
            "00index": {
                "description": "",
                "subpackages": {},
                "modules": {}
            }
        }
        self.remembered = False
        
        self.stylesheet = stylesheet
        
        if self.stylesheet:
            from . import TemplatesListsStyleCSS
            self.headerTemplate = TemplatesListsStyleCSS.headerTemplate
            self.footerTemplate = TemplatesListsStyleCSS.footerTemplate
            self.indexBodyTemplate = TemplatesListsStyleCSS.indexBodyTemplate
            self.indexListPackagesTemplate = \
                TemplatesListsStyleCSS.indexListPackagesTemplate
            self.indexListModulesTemplate = \
                TemplatesListsStyleCSS.indexListModulesTemplate
            self.indexListEntryTemplate = \
                TemplatesListsStyleCSS.indexListEntryTemplate
        else:
            from . import TemplatesListsStyle
            self.headerTemplate = \
                TemplatesListsStyle.headerTemplate.format(**colors)
            self.footerTemplate = \
                TemplatesListsStyle.footerTemplate.format(**colors)
            self.indexBodyTemplate = \
                TemplatesListsStyle.indexBodyTemplate.format(**colors)
            self.indexListPackagesTemplate = \
                TemplatesListsStyle.indexListPackagesTemplate.format(**colors)
            self.indexListModulesTemplate = \
                TemplatesListsStyle.indexListModulesTemplate.format(**colors)
            self.indexListEntryTemplate = \
                TemplatesListsStyle.indexListEntryTemplate.format(**colors)
        
    def remember(self, file, moduleDocument, basename=""):
        """
        Public method to remember a documentation file.
        
        @param file The filename to be remembered. (string)
        @param moduleDocument The ModuleDocument object containing the
            information for the file.
        @param basename The basename of the file hierarchy to be documented.
            The basename is stripped off the filename if it starts with
            the basename.
        """
        self.remembered = True
        if basename:
            file = file.replace(basename, "")
            
        if "__init__" in file:
            dirName = os.path.dirname(file)
            udir = os.path.dirname(dirName)
            if udir:
                upackage = udir.replace(os.sep, ".")
                try:
                    elt = self.packages[upackage]
                except KeyError:
                    elt = self.packages["00index"]
            else:
                elt = self.packages["00index"]
            package = dirName.replace(os.sep, ".")
            elt["subpackages"][package] = moduleDocument.shortDescription()
                
            self.packages[package] = {
                "description": moduleDocument.description(),
                "subpackages": {},
                "modules": {}
            }
            
            if moduleDocument.isEmpty():
                return
        
        package = os.path.dirname(file).replace(os.sep, ".")
        try:
            elt = self.packages[package]
        except KeyError:
            elt = self.packages["00index"]
        elt["modules"][moduleDocument.name()] = \
            moduleDocument.shortDescription()
    
    def __writeIndex(self, packagename, package, newline=None):
        """
        Private method to generate an index file for a package.
        
        @param packagename The name of the package. (string)
        @param package A dictionary with information about the package.
        @param newline newline character to be used (string)
        @return The name of the generated index file.
        """
        if packagename == "00index":
            f = os.path.join(self.outputDir, "index")
            title = "Table of contents"
        else:
            f = os.path.join(self.outputDir, "index-{0}".format(packagename))
            title = packagename
        
        filename = joinext(f, ".html")
        
        subpackages = ""
        modules = ""
        
        # 1) subpackages
        if package["subpackages"]:
            subpacks = package["subpackages"]
            names = sorted(list(subpacks.keys()))
            lst = []
            for name in names:
                link = joinext("index-{0}".format(name), ".html")
                lst.append(self.indexListEntryTemplate.format(**{
                    "Description": subpacks[name],
                    "Name": name.split(".")[-1],
                    "Link": link,
                }))
            subpackages = self.indexListPackagesTemplate.format(**{
                "Entries": "".join(lst),
            })
            
        # 2) modules
        if package["modules"]:
            mods = package["modules"]
            names = sorted(list(mods.keys()))
            lst = []
            for name in names:
                link = joinext(name, ".html")
                nam = name.split(".")[-1]
                if nam == "__init__":
                    nam = name.split(".")[-2]
                lst.append(self.indexListEntryTemplate.format(**{
                    "Description": mods[name],
                    "Name": nam,
                    "Link": link,
                }))
            modules = self.indexListModulesTemplate.format(**{
                "Entries": "".join(lst),
            })
            
        doc = self.headerTemplate.format(
            **{"Title": title,
               "Style": self.stylesheet}) + \
            self.indexBodyTemplate.format(
                **{"Title": title,
                   "Description": package["description"],
                   "Subpackages": subpackages,
                   "Modules": modules}) + \
            self.footerTemplate
    
        f = open(filename, "w", encoding="utf-8", newline=newline)
        f.write(doc)
        f.close()
    
        return filename
    
    def writeIndices(self, basename="", newline=None):
        """
        Public method to generate all index files.
        
        @param basename The basename of the file hierarchy to be documented.
            The basename is stripped off the filename if it starts with
            the basename.
        @param newline newline character to be used (string)
        """
        if not self.remembered:
            sys.stderr.write("No index to generate.\n")
            return
            
        if basename:
            basename = basename.replace(os.sep, ".")
            if not basename.endswith("."):
                basename = "{0}.".format(basename)
        for package, element in list(self.packages.items()):
            try:
                if basename:
                    package = package.replace(basename, "")
                out = self.__writeIndex(package, element, newline)
            except IOError as v:
                sys.stderr.write("{0} error: {1}\n".format(package, v[1]))
            else:
                if out:
                    sys.stdout.write("{0} ok\n".format(out))
    
        sys.stdout.write("Indices written.\n")
        sys.stdout.flush()
        sys.stderr.flush()
