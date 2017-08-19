# -*- coding: utf-8 -*-

# Copyright (c) 2009 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the QtHelp generator for the builtin documentation
generator.
"""

from __future__ import unicode_literals

import sys
import os
import shutil
import subprocess

from Utilities import joinext, relpath, html_encode, getQtBinariesPath, \
    generateQtToolName

HelpCollection = r"""<?xml version="1.0" encoding="utf-8" ?>
<QHelpCollectionProject version="1.0">
  <docFiles>
    <register>
      <file>{helpfile}</file>
    </register>
  </docFiles>
</QHelpCollectionProject>
"""

HelpProject = r"""<?xml version="1.0" encoding="UTF-8"?>
<QtHelpProject version="1.0">
  <namespace>{namespace}</namespace>
  <virtualFolder>{folder}</virtualFolder>
  <customFilter name="{filter_name}">
{filter_attributes}
  </customFilter>
  <filterSection>
{filter_attributes}
    <toc>
{sections}
    </toc>
    <keywords>
{keywords}
    </keywords>
    <files>
{files}
    </files>
  </filterSection>
</QtHelpProject>
"""

HelpProjectFile = 'source.qhp'
HelpHelpFile = 'source.qch'
HelpCollectionProjectFile = 'source.qhcp'
HelpCollectionFile = 'collection.qhc'


class QtHelpGenerator(object):
    """
    Class implementing the QtHelp generator for the builtin documentation
    generator.
    """
    def __init__(self, htmlDir,
                 outputDir, namespace, virtualFolder, filterName,
                 filterAttributes, title, createCollection):
        """
        Constructor
        
        @param htmlDir directory containing the HTML files (string)
        @param outputDir output directory for the files (string)
        @param namespace namespace to be used (string)
        @param virtualFolder virtual folder to be used (string)
        @param filterName name of the custom filter (string)
        @param filterAttributes ':' separated list of filter attributes
            (string)
        @param title title to be used for the generated help (string)
        @param createCollection flag indicating the generation of the
            collection files (boolean)
        """
        self.htmlDir = htmlDir
        self.outputDir = outputDir
        self.namespace = namespace
        self.virtualFolder = virtualFolder
        self.filterName = filterName
        self.filterAttributes = \
            filterAttributes and filterAttributes.split(':') or []
        self.relPath = relpath(self.htmlDir, self.outputDir)
        self.title = title
        self.createCollection = createCollection
        
        self.packages = {
            "00index": {
                "subpackages": {},
                "modules": {}
            }
        }
        self.remembered = False
        self.keywords = []
    
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
            elt["subpackages"][package] = moduleDocument.name()
            
            self.packages[package] = {
                "subpackages": {},
                "modules": {}
            }
            
            kwEntry = ("{0} (Package)".format(package.split('.')[-1]),
                       joinext("index-{0}".format(package), ".html"))
            if kwEntry not in self.keywords:
                self.keywords.append(kwEntry)
            
            if moduleDocument.isEmpty():
                return
        
        package = os.path.dirname(file).replace(os.sep, ".")
        try:
            elt = self.packages[package]
        except KeyError:
            elt = self.packages["00index"]
        elt["modules"][moduleDocument.name()] = moduleDocument.name()
        
        if "__init__" not in file:
            kwEntry = (
                "{0} (Module)".format(moduleDocument.name().split('.')[-1]),
                joinext(moduleDocument.name(), ".html"))
            if kwEntry not in self.keywords:
                self.keywords.append(kwEntry)
        for kw in moduleDocument.getQtHelpKeywords():
            kwEntry = (kw[0], "{0}{1}".format(
                joinext(moduleDocument.name(), ".html"), kw[1]))
            if kwEntry not in self.keywords:
                self.keywords.append(kwEntry)
    
    def __generateSections(self, package, level):
        """
        Private method to generate the sections part.
        
        @param package name of the package to process (string)
        @param level indentation level (integer)
        @return sections part (string)
        """
        indent = level * '  '
        indent1 = indent + '  '
        s = indent + '<section title="{0}" ref="{1}">\n'.format(
            package == "00index" and self.title or package,
            package == "00index" and
            joinext("index", ".html") or
            joinext("index-{0}".format(package), ".html"))
        for subpack in sorted(self.packages[package]["subpackages"]):
            s += self.__generateSections(subpack, level + 1)
            s += '\n'
        for mod in sorted(self.packages[package]["modules"]):
            s += indent1 + '<section title="{0}" ref="{1}" />\n'.format(
                mod, joinext(mod, ".html"))
        s += indent + '</section>'
        return s
    
    def __convertEol(self, txt, newline):
        """
        Private method to convert the newline characters.
        
        @param txt text to be converted (string)
        @param newline newline character to be used (string)
        @return converted text (string)
        """
        # step 1: normalize eol to '\n'
        txt = txt.replace("\r\n", "\n").replace("\r", "\n")
        
        # step 2: convert to the target eol
        if newline is None:
            return txt.replace("\n", os.linesep)
        elif newline in ["\r", "\r\n"]:
            return txt.replace("\n", newline)
        else:
            return txt
    
    def generateFiles(self, basename="", newline=None):
        """
        Public method to generate all index files.
        
        @param basename The basename of the file hierarchy to be documented.
            The basename is stripped off the filename if it starts with
            the basename.
        @param newline newline character to be used (string)
        """
        if not self.remembered:
            sys.stderr.write("No QtHelp to generate.\n")
            return
        
        if basename:
            basename = basename.replace(os.sep, ".")
            if not basename.endswith("."):
                basename = "{0}.".format(basename)
        
        sections = self.__generateSections("00index", 3)
        filesList = sorted(e for e in os.listdir(self.htmlDir)
                           if e.endswith('.html'))
        files = "\n".join(
            ["      <file>{0}</file>".format(f) for f in filesList])
        filterAttribs = "\n".join(
            ["    <filterAttribute>{0}</filterAttribute>".format(a)
             for a in sorted(self.filterAttributes)])
        keywords = "\n".join(
            ['      <keyword name="{0}" id="{1}" ref="{2}" />'.format(
             html_encode(kw[0]), html_encode(kw[0]), html_encode(kw[1]))
             for kw in sorted(self.keywords)])
        
        helpAttribs = {
            "namespace": self.namespace,
            "folder": self.virtualFolder,
            "filter_name": self.filterName,
            "filter_attributes": filterAttribs,
            "sections": sections,
            "keywords": keywords,
            "files": files,
        }
        
        txt = self.__convertEol(HelpProject.format(**helpAttribs), newline)
        f = open(os.path.join(self.outputDir, HelpProjectFile), "w",
                 encoding="utf-8", newline=newline)
        f.write(txt)
        f.close()
        
        if self.createCollection and \
           not os.path.exists(
                os.path.join(self.outputDir, HelpCollectionProjectFile)):
            collectionAttribs = {
                "helpfile": HelpHelpFile,
            }
            
            txt = self.__convertEol(
                HelpCollection.format(**collectionAttribs), newline)
            f = open(os.path.join(self.outputDir, HelpCollectionProjectFile),
                     "w", encoding="utf-8", newline=newline)
            f.write(txt)
            f.close()
        
        sys.stdout.write("QtHelp files written.\n")
        sys.stdout.write("Generating QtHelp documentation...\n")
        sys.stdout.flush()
        sys.stderr.flush()
        
        cwd = os.getcwd()
        # generate the compressed files
        shutil.copy(
            os.path.join(self.outputDir, HelpProjectFile), self.htmlDir)
        os.chdir(self.htmlDir)
        subprocess.call([
            os.path.join(getQtBinariesPath(),
                         generateQtToolName("qhelpgenerator")),
            HelpProjectFile, "-o", os.path.join(self.outputDir, HelpHelpFile)])
        os.remove(HelpProjectFile)
        
        if self.createCollection:
            sys.stdout.write("Generating QtHelp collection...\n")
            sys.stdout.flush()
            sys.stderr.flush()
            os.chdir(self.outputDir)
            subprocess.call([
                os.path.join(getQtBinariesPath(),
                             generateQtToolName("qcollectiongenerator")),
                HelpCollectionProjectFile, "-o", HelpCollectionFile])
        
        os.chdir(cwd)
