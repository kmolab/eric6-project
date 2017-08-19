# -*- coding: utf-8 -*-

# Copyright (c) 2003 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the builtin documentation generator.

The different parts of the module document are assembled from the parsed
Python file. The appearance is determined by several templates defined within
this module.
"""

from __future__ import unicode_literals

import sys
import re

from Utilities import html_uencode
from Utilities.ModuleParser import RB_SOURCE, Function

_signal = re.compile(
    r"""
    ^@signal [ \t]+
    (?P<SignalName1>
        [a-zA-Z_] \w* [ \t]* \( [^)]* \)
    )
    [ \t]* (?P<SignalDescription1> .*)
|
    ^@signal [ \t]+
    (?P<SignalName2>
        [a-zA-Z_] \w*
    )
    [ \t]+ (?P<SignalDescription2> .*)
    """, re.VERBOSE | re.DOTALL | re.MULTILINE).search

_event = re.compile(
    r"""
    ^@event [ \t]+
    (?P<EventName1>
        [a-zA-Z_] \w* [ \t]* \( [^)]* \)
    )
    [ \t]* (?P<EventDescription1> .*)
|
    ^@event [ \t]+
    (?P<EventName2>
        [a-zA-Z_] \w*
    )
    [ \t]+ (?P<EventDescription2> .*)
    """, re.VERBOSE | re.DOTALL | re.MULTILINE).search


class TagError(Exception):
    """
    Exception class raised, if an invalid documentation tag was found.
    """
    pass


class ModuleDocument(object):
    """
    Class implementing the builtin documentation generator.
    """
    def __init__(self, module, colors, stylesheet=None):
        """
        Constructor
        
        @param module the information of the parsed Python file
        @param colors dictionary specifying the various colors for the output
            (dictionary of strings)
        @param stylesheet the style to be used for the generated pages (string)
        """
        self.module = module
        self.empty = True
        
        self.stylesheet = stylesheet
        
        if self.stylesheet:
            from . import TemplatesListsStyleCSS
            self.headerTemplate = TemplatesListsStyleCSS.headerTemplate
            self.footerTemplate = TemplatesListsStyleCSS.footerTemplate
            self.moduleTemplate = TemplatesListsStyleCSS.moduleTemplate
            self.rbFileTemplate = TemplatesListsStyleCSS.rbFileTemplate
            self.classTemplate = TemplatesListsStyleCSS.classTemplate
            self.methodTemplate = TemplatesListsStyleCSS.methodTemplate
            self.constructorTemplate = \
                TemplatesListsStyleCSS.constructorTemplate
            self.rbModuleTemplate = TemplatesListsStyleCSS.rbModuleTemplate
            self.rbModulesClassTemplate = \
                TemplatesListsStyleCSS.rbModulesClassTemplate
            self.functionTemplate = TemplatesListsStyleCSS.functionTemplate
            self.listTemplate = TemplatesListsStyleCSS.listTemplate
            self.listEntryTemplate = TemplatesListsStyleCSS.listEntryTemplate
            self.listEntryNoneTemplate = \
                TemplatesListsStyleCSS.listEntryNoneTemplate
            self.listEntryDeprecatedTemplate = \
                TemplatesListsStyleCSS.listEntryDeprecatedTemplate
            self.listEntrySimpleTemplate = \
                TemplatesListsStyleCSS.listEntrySimpleTemplate
            self.paragraphTemplate = TemplatesListsStyleCSS.paragraphTemplate
            self.parametersListTemplate = \
                TemplatesListsStyleCSS.parametersListTemplate
            self.parameterTypesListEntryTemplate = \
                TemplatesListsStyleCSS.parameterTypesListEntryTemplate
            self.parametersListEntryTemplate = \
                TemplatesListsStyleCSS.parametersListEntryTemplate
            self.returnsTemplate = TemplatesListsStyleCSS.returnsTemplate
            self.returnTypesTemplate = \
                TemplatesListsStyleCSS.returnTypesTemplate
            self.exceptionsListTemplate = \
                TemplatesListsStyleCSS.exceptionsListTemplate
            self.exceptionsListEntryTemplate = \
                TemplatesListsStyleCSS.exceptionsListEntryTemplate
            self.signalsListTemplate = \
                TemplatesListsStyleCSS.signalsListTemplate
            self.signalsListEntryTemplate = \
                TemplatesListsStyleCSS.signalsListEntryTemplate
            self.eventsListTemplate = TemplatesListsStyleCSS.eventsListTemplate
            self.eventsListEntryTemplate = \
                TemplatesListsStyleCSS.eventsListEntryTemplate
            self.deprecatedTemplate = TemplatesListsStyleCSS.deprecatedTemplate
            self.authorInfoTemplate = TemplatesListsStyleCSS.authorInfoTemplate
            self.seeListTemplate = TemplatesListsStyleCSS.seeListTemplate
            self.seeListEntryTemplate = \
                TemplatesListsStyleCSS.seeListEntryTemplate
            self.seeLinkTemplate = TemplatesListsStyleCSS.seeLinkTemplate
            self.sinceInfoTemplate = TemplatesListsStyleCSS.sinceInfoTemplate
        else:
            from . import TemplatesListsStyle
            self.headerTemplate = \
                TemplatesListsStyle.headerTemplate.format(**colors)
            self.footerTemplate = \
                TemplatesListsStyle.footerTemplate.format(**colors)
            self.moduleTemplate = \
                TemplatesListsStyle.moduleTemplate.format(**colors)
            self.rbFileTemplate = \
                TemplatesListsStyle.rbFileTemplate.format(**colors)
            self.classTemplate = \
                TemplatesListsStyle.classTemplate.format(**colors)
            self.methodTemplate = \
                TemplatesListsStyle.methodTemplate.format(**colors)
            self.constructorTemplate = \
                TemplatesListsStyle.constructorTemplate.format(**colors)
            self.rbModuleTemplate = \
                TemplatesListsStyle.rbModuleTemplate.format(**colors)
            self.rbModulesClassTemplate = \
                TemplatesListsStyle.rbModulesClassTemplate.format(**colors)
            self.functionTemplate = \
                TemplatesListsStyle.functionTemplate.format(**colors)
            self.listTemplate = \
                TemplatesListsStyle.listTemplate.format(**colors)
            self.listEntryTemplate = \
                TemplatesListsStyle.listEntryTemplate.format(**colors)
            self.listEntryNoneTemplate = \
                TemplatesListsStyle.listEntryNoneTemplate.format(**colors)
            self.listEntryDeprecatedTemplate = \
                TemplatesListsStyle.listEntryDeprecatedTemplate.format(
                    **colors)
            self.listEntrySimpleTemplate = \
                TemplatesListsStyle.listEntrySimpleTemplate.format(**colors)
            self.paragraphTemplate = \
                TemplatesListsStyle.paragraphTemplate.format(**colors)
            self.parametersListTemplate = \
                TemplatesListsStyle.parametersListTemplate.format(**colors)
            self.parametersListEntryTemplate = \
                TemplatesListsStyle.parametersListEntryTemplate.format(
                    **colors)
            self.parameterTypesListEntryTemplate = \
                TemplatesListsStyle.parameterTypesListEntryTemplate.format(
                    **colors)
            self.returnsTemplate = \
                TemplatesListsStyle.returnsTemplate.format(**colors)
            self.returnTypesTemplate = \
                TemplatesListsStyle.returnTypesTemplate.format(**colors)
            self.exceptionsListTemplate = \
                TemplatesListsStyle.exceptionsListTemplate.format(**colors)
            self.exceptionsListEntryTemplate = \
                TemplatesListsStyle.exceptionsListEntryTemplate.format(
                    **colors)
            self.signalsListTemplate = \
                TemplatesListsStyle.signalsListTemplate.format(**colors)
            self.signalsListEntryTemplate = \
                TemplatesListsStyle.signalsListEntryTemplate.format(**colors)
            self.eventsListTemplate = \
                TemplatesListsStyle.eventsListTemplate.format(**colors)
            self.eventsListEntryTemplate = \
                TemplatesListsStyle.eventsListEntryTemplate.format(**colors)
            self.deprecatedTemplate = \
                TemplatesListsStyle.deprecatedTemplate.format(**colors)
            self.authorInfoTemplate = \
                TemplatesListsStyle.authorInfoTemplate.format(**colors)
            self.seeListTemplate = \
                TemplatesListsStyle.seeListTemplate.format(**colors)
            self.seeListEntryTemplate = \
                TemplatesListsStyle.seeListEntryTemplate.format(**colors)
            self.seeLinkTemplate = \
                TemplatesListsStyle.seeLinkTemplate.format(**colors)
            self.sinceInfoTemplate = \
                TemplatesListsStyle.sinceInfoTemplate.format(**colors)
        
        self.keywords = []
        # list of tuples containing the name (string) and
        # the ref (string). The ref is without the filename part.
        self.generated = False
        
    def isEmpty(self):
        """
        Public method to determine, if the module contains any classes or
        functions.
        
        @return Flag indicating an empty module (i.e. __init__.py without
            any contents)
        """
        return self.empty
        
    def name(self):
        """
        Public method used to get the module name.
        
        @return The name of the module. (string)
        """
        return self.module.name
        
    def description(self):
        """
        Public method used to get the description of the module.
        
        @return The description of the module. (string)
        """
        return self.__formatDescription(self.module.description)
        
    def shortDescription(self):
        """
        Public method used to get the short description of the module.
        
        The short description is just the first line of the modules
        description.
        
        @return The short description of the module. (string)
        """
        return self.__getShortDescription(self.module.description)
        
    def genDocument(self):
        """
        Public method to generate the source code documentation.
        
        @return The source code documentation. (string)
        """
        doc = self.headerTemplate.format(
            **{'Title': self.module.name,
               'Style': self.stylesheet}) + \
            self.__genModuleSection() + \
            self.footerTemplate
        self.generated = True
        return doc
        
    def __genModuleSection(self):
        """
        Private method to generate the body of the document.
        
        @return The body of the document. (string)
        """
        globalsList = self.__genGlobalsListSection()
        classList = self.__genClassListSection()
        functionList = self.__genFunctionListSection()
        try:
            if self.module.type == RB_SOURCE:
                rbModulesList = self.__genRbModulesListSection()
                modBody = self.rbFileTemplate.format(
                    **{'Module': self.module.name,
                       'ModuleDescription':
                        self.__formatDescription(self.module.description),
                       'GlobalsList': globalsList,
                       'ClassList': classList,
                       'RbModulesList': rbModulesList,
                       'FunctionList': functionList,
                       })
            else:
                modBody = self.moduleTemplate.format(
                    **{'Module': self.module.name,
                       'ModuleDescription':
                        self.__formatDescription(self.module.description),
                       'GlobalsList': globalsList,
                       'ClassList': classList,
                       'FunctionList': functionList,
                       })
        except TagError as e:
            sys.stderr.write(
                "Error processing {0}.\n".format(self.module.file))
            sys.stderr.write(
                "Error in tags of description of module {0}.\n".format(
                    self.module.name))
            sys.stderr.write("{0}\n".format(e))
            return ""
            
        classesSection = self.__genClassesSection()
        functionsSection = self.__genFunctionsSection()
        if self.module.type == RB_SOURCE:
            rbModulesSection = self.__genRbModulesSection()
        else:
            rbModulesSection = ""
        return "{0}{1}{2}{3}".format(
            modBody, classesSection, rbModulesSection, functionsSection)
        
    def __genListSection(self, names, sectionDict, kwSuffix=""):
        """
        Private method to generate a list section of the document.
        
        @param names The names to appear in the list. (list of strings)
        @param sectionDict dictionary containing all relevant information
            (dict)
        @param kwSuffix suffix to be used for the QtHelp keywords (string)
        @return list section (string)
        """
        lst = []
        for name in names:
            lst.append(self.listEntryTemplate.format(
                **{'Link': "{0}".format(name),
                   'Name': sectionDict[name].name,
                   'Description':
                    self.__getShortDescription(sectionDict[name].description),
                   'Deprecated':
                    self.__checkDeprecated(sectionDict[name].description) and
                    self.listEntryDeprecatedTemplate or "",
                   }))
            if kwSuffix:
                n = "{0} ({1})".format(name, kwSuffix)
            else:
                n = "{0}".format(name)
            self.keywords.append((n, "#{0}".format(name)))
        return ''.join(lst)
        
    def __genGlobalsListSection(self, class_=None):
        """
        Private method to generate the section listing all global attributes of
        the module.
        
        @param class_ reference to a class object (Class)
        @return The globals list section. (string)
        """
        attrNames = []
        if class_ is not None:
            scope = class_
        else:
            scope = self.module
        attrNames = sorted(attr for attr in scope.globals.keys()
                           if not scope.globals[attr].isSignal)
        if attrNames:
            s = ''.join(
                [self.listEntrySimpleTemplate.format(**{'Name': name})
                 for name in attrNames])
        else:
            s = self.listEntryNoneTemplate
        return self.listTemplate.format(**{'Entries': s})
        
    def __genClassListSection(self):
        """
        Private method to generate the section listing all classes of the
        module.
        
        @return The classes list section. (string)
        """
        names = sorted(list(self.module.classes.keys()))
        if names:
            self.empty = False
            s = self.__genListSection(names, self.module.classes)
        else:
            s = self.listEntryNoneTemplate
        return self.listTemplate.format(**{'Entries': s})
        
    def __genRbModulesListSection(self):
        """
        Private method to generate the section listing all modules of the file
        (Ruby only).
        
        @return The modules list section. (string)
        """
        names = sorted(list(self.module.modules.keys()))
        if names:
            self.empty = False
            s = self.__genListSection(names, self.module.modules)
        else:
            s = self.listEntryNoneTemplate
        return self.listTemplate.format(**{'Entries': s})
        
    def __genFunctionListSection(self):
        """
        Private method to generate the section listing all functions of the
        module.
        
        @return The functions list section. (string)
        """
        names = sorted(list(self.module.functions.keys()))
        if names:
            self.empty = False
            s = self.__genListSection(names, self.module.functions)
        else:
            s = self.listEntryNoneTemplate
        return self.listTemplate.format(**{'Entries': s})
        
    def __genClassesSection(self):
        """
        Private method to generate the document section with details about
        classes.
        
        @return The classes details section. (string)
        """
        classNames = sorted(list(self.module.classes.keys()))
        classes = []
        for className in classNames:
            _class = self.module.classes[className]
            supers = _class.super
            if len(supers) > 0:
                supers = ', '.join(supers)
            else:
                supers = 'None'
            
            globalsList = self.__genGlobalsListSection(_class)
            classMethList, classMethBodies = \
                self.__genMethodSection(_class, className, Function.Class)
            methList, methBodies = \
                self.__genMethodSection(_class, className, Function.General)
            staticMethList, staticMethBodies = \
                self.__genMethodSection(_class, className, Function.Static)
            
            try:
                clsBody = self.classTemplate.format(
                    **{'Anchor': className,
                       'Class': _class.name,
                       'ClassSuper': supers,
                       'ClassDescription':
                        self.__formatDescription(_class.description),
                       'GlobalsList': globalsList,
                       'ClassMethodList': classMethList,
                       'MethodList': methList,
                       'StaticMethodList': staticMethList,
                       'MethodDetails':
                        classMethBodies + methBodies + staticMethBodies,
                       })
            except TagError as e:
                sys.stderr.write(
                    "Error processing {0}.\n".format(self.module.file))
                sys.stderr.write(
                    "Error in tags of description of class {0}.\n".format(
                        className))
                sys.stderr.write("{0}\n".format(e))
                clsBody = ""
            
            classes.append(clsBody)
            
        return ''.join(classes)
        
    def __genMethodsListSection(self, names, sectionDict, className, clsName,
                                includeInit=True):
        """
        Private method to generate the methods list section of a class.
        
        @param names names to appear in the list (list of strings)
        @param sectionDict dictionary containing all relevant information
            (dict)
        @param className class name containing the names
        @param clsName visible class name containing the names
        @param includeInit flag indicating to include the __init__ method
            (boolean)
        @return methods list section (string)
        """
        lst = []
        if includeInit:
            try:
                lst.append(self.listEntryTemplate.format(
                    **{'Link': "{0}.{1}".format(className, '__init__'),
                       'Name': clsName,
                       'Description': self.__getShortDescription(
                           sectionDict['__init__'].description),
                       'Deprecated': self.__checkDeprecated(
                           sectionDict['__init__'].description) and
                        self.listEntryDeprecatedTemplate or "",
                       }))
                self.keywords.append(
                    ("{0} (Constructor)".format(className),
                     "#{0}.{1}".format(className, '__init__')))
            except KeyError:
                pass
        
        for name in names:
            lst.append(self.listEntryTemplate.format(
                **{'Link': "{0}.{1}".format(className, name),
                   'Name': sectionDict[name].name,
                   'Description':
                    self.__getShortDescription(sectionDict[name].description),
                   'Deprecated':
                    self.__checkDeprecated(sectionDict[name].description) and
                    self.listEntryDeprecatedTemplate or "",
                   }))
            self.keywords.append(("{0}.{1}".format(className, name),
                                  "#{0}.{1}".format(className, name)))
        return ''.join(lst)
        
    def __genMethodSection(self, obj, className, modifierFilter):
        """
        Private method to generate the method details section.
        
        @param obj reference to the object being formatted
        @param className name of the class containing the method (string)
        @param modifierFilter filter value designating the method types
        @return method list and method details section (tuple of two string)
        """
        methList = []
        methBodies = []
        methods = sorted(k for k in obj.methods.keys()
                         if obj.methods[k].modifier == modifierFilter)
        if '__init__' in methods:
            methods.remove('__init__')
            try:
                methBody = self.constructorTemplate.format(
                    **{'Anchor': className,
                       'Class': obj.name,
                       'Method': '__init__',
                       'MethodDescription':
                        self.__formatDescription(
                            obj.methods['__init__'].description),
                       'Params':
                        ', '.join(obj.methods['__init__'].parameters[1:]),
                       })
            except TagError as e:
                sys.stderr.write(
                    "Error processing {0}.\n".format(self.module.file))
                sys.stderr.write(
                    "Error in tags of description of method {0}.{1}.\n".format(
                        className, '__init__'))
                sys.stderr.write("{0}\n".format(e))
                methBody = ""
            methBodies.append(methBody)
        
        if modifierFilter == Function.Class:
            methodClassifier = " (class method)"
        elif modifierFilter == Function.Static:
            methodClassifier = " (static)"
        else:
            methodClassifier = ""
        for method in methods:
            try:
                methBody = self.methodTemplate.format(
                    **{'Anchor': className,
                       'Class': obj.name,
                       'Method': obj.methods[method].name,
                       'MethodClassifier': methodClassifier,
                       'MethodDescription':
                        self.__formatDescription(
                            obj.methods[method].description),
                       'Params': ', '.join(obj.methods[method].parameters[1:]),
                       })
            except TagError as e:
                sys.stderr.write(
                    "Error processing {0}.\n".format(self.module.file))
                sys.stderr.write(
                    "Error in tags of description of method {0}.{1}.\n".format(
                        className, method))
                sys.stderr.write("{0}\n".format(e))
                methBody = ""
            methBodies.append(methBody)
            
        methList = self.__genMethodsListSection(
            methods, obj.methods, className, obj.name,
            includeInit=modifierFilter == Function.General)
        
        if not methList:
            methList = self.listEntryNoneTemplate
        return (self.listTemplate.format(**{'Entries': methList}),
                ''.join(methBodies))
        
    def __genRbModulesSection(self):
        """
        Private method to generate the document section with details about
        Ruby modules.
        
        @return The Ruby modules details section. (string)
        """
        rbModulesNames = sorted(list(self.module.modules.keys()))
        rbModules = []
        for rbModuleName in rbModulesNames:
            rbModule = self.module.modules[rbModuleName]
            globalsList = self.__genGlobalsListSection(rbModule)
            methList, methBodies = self.__genMethodSection(
                rbModule, rbModuleName, Function.General)
            classList, classBodies = self.__genRbModulesClassesSection(
                rbModule, rbModuleName)
            
            try:
                rbmBody = self.rbModuleTemplate.format(
                    **{'Anchor': rbModuleName,
                       'Module': rbModule.name,
                       'ModuleDescription':
                        self.__formatDescription(rbModule.description),
                       'GlobalsList': globalsList,
                       'ClassesList': classList,
                       'ClassesDetails': classBodies,
                       'FunctionsList': methList,
                       'FunctionsDetails': methBodies,
                       })
            except TagError as e:
                sys.stderr.write(
                    "Error processing {0}.\n".format(self.module.file))
                sys.stderr.write(
                    "Error in tags of description of Ruby module {0}.\n"
                    .format(rbModuleName))
                sys.stderr.write("{0}\n".format(e))
                rbmBody = ""
            
            rbModules.append(rbmBody)
            
        return ''.join(rbModules)

    def __genRbModulesClassesSection(self, obj, modName):
        """
        Private method to generate the Ruby module classes details section.
        
        @param obj Reference to the object being formatted.
        @param modName Name of the Ruby module containing the classes. (string)
        @return The classes list and classes details section.
            (tuple of two string)
        """
        classNames = sorted(list(obj.classes.keys()))
        classes = []
        for className in classNames:
            _class = obj.classes[className]
            supers = _class.super
            if len(supers) > 0:
                supers = ', '.join(supers)
            else:
                supers = 'None'
            
            methList, methBodies = \
                self.__genMethodSection(_class, className, Function.General)
            
            try:
                clsBody = self.rbModulesClassTemplate.format(
                    **{'Anchor': className,
                       'Class': _class.name,
                       'ClassSuper': supers,
                       'ClassDescription':
                        self.__formatDescription(_class.description),
                       'MethodList': methList,
                       'MethodDetails': methBodies,
                       })
            except TagError as e:
                sys.stderr.write(
                    "Error processing {0}.\n".format(self.module.file))
                sys.stderr.write(
                    "Error in tags of description of class {0}.\n".format(
                        className))
                sys.stderr.write("{0}\n".format(e))
                clsBody = ""
            
            classes.append(clsBody)
            
        classesList = self.__genRbModulesClassesListSection(
            classNames, obj.classes, modName)
        
        if not classesList:
            classesList = self.listEntryNoneTemplate
        return (self.listTemplate.format(**{'Entries': classesList}),
                ''.join(classes))
        
    def __genRbModulesClassesListSection(self, names, sectionDict, moduleName):
        """
        Private method to generate the classes list section of a Ruby module.
        
        @param names The names to appear in the list. (list of strings)
        @param sectionDict dictionary containing all relevant information
            (dict)
        @param moduleName name of the Ruby module containing the classes
            (string)
        @return The list section. (string)
        """
        lst = []
        for name in names:
            lst.append(self.listEntryTemplate.format(
                **{'Link': "{0}.{1}".format(moduleName, name),
                   'Name': sectionDict[name].name,
                   'Description':
                    self.__getShortDescription(sectionDict[name].description),
                   'Deprecated':
                    self.__checkDeprecated(sectionDict[name].description) and
                    self.listEntryDeprecatedTemplate or "",
                   }))
            self.keywords.append(("{0}.{1}".format(moduleName, name),
                                  "#{0}.{1}".format(moduleName, name)))
        return ''.join(lst)
        
    def __genFunctionsSection(self):
        """
        Private method to generate the document section with details about
        functions.
        
        @return The functions details section. (string)
        """
        funcBodies = []
        funcNames = sorted(list(self.module.functions.keys()))
        for funcName in funcNames:
            try:
                funcBody = self.functionTemplate.format(
                    **{'Anchor': funcName,
                       'Function': self.module.functions[funcName].name,
                       'FunctionDescription': self.__formatDescription(
                           self.module.functions[funcName].description),
                       'Params':
                        ', '.join(self.module.functions[funcName].parameters),
                       })
            except TagError as e:
                sys.stderr.write(
                    "Error processing {0}.\n".format(self.module.file))
                sys.stderr.write(
                    "Error in tags of description of function {0}.\n".format(
                        funcName))
                sys.stderr.write("{0}\n".format(e))
                funcBody = ""
            
            funcBodies.append(funcBody)
            
        return ''.join(funcBodies)
        
    def __getShortDescription(self, desc):
        """
        Private method to determine the short description of an object.
        
        The short description is just the first non empty line of the
        documentation string.
        
        @param desc The documentation string. (string)
        @return The short description. (string)
        """
        dlist = desc.splitlines()
        sdlist = []
        descfound = 0
        for desc in dlist:
            desc = desc.strip()
            if desc:
                descfound = 1
                dotpos = desc.find('.')
                if dotpos == -1:
                    sdlist.append(desc.strip())
                else:
                    while dotpos + 1 < len(desc) and \
                            not desc[dotpos + 1].isspace():
                        # don't recognize '.' inside a number or word as
                        # stop condition
                        dotpos = desc.find('.', dotpos + 1)
                        if dotpos == -1:
                            break
                    if dotpos == -1:
                        sdlist.append(desc.strip())
                    else:
                        sdlist.append(desc[:dotpos + 1].strip())
                        break   # break if a '.' is found
            else:
                if descfound:
                    break   # break if an empty line is found
        if sdlist:
            return html_uencode(' '.join(sdlist))
        else:
            return ''
        
    def __checkDeprecated(self, descr):
        """
        Private method to check, if the object to be documented contains a
        deprecated flag.
        
        @param descr documentation string (string)
        @return flag indicating the deprecation status (boolean)
        """
        dlist = descr.splitlines()
        for desc in dlist:
            desc = desc.strip()
            if desc.startswith("@deprecated"):
                return True
        return False
        
    def __genParagraphs(self, lines):
        """
        Private method to assemble the descriptive paragraphs of a docstring.
        
        A paragraph is made up of a number of consecutive lines without
        an intermediate empty line. Empty lines are treated as a paragraph
        delimiter.
        
        @param lines A list of individual lines. (list of strings)
        @return Ready formatted paragraphs. (string)
        """
        lst = []
        linelist = []
        for line in lines:
            if line.strip():
                if line == '.':
                    linelist.append("")
                else:
                    linelist.append(html_uencode(line))
            else:
                lst.append(self.paragraphTemplate.format(
                    **{'Lines': '\n'.join(linelist)}))
                linelist = []
        if linelist:
            lst.append(self.paragraphTemplate.format(
                **{'Lines': '\n'.join(linelist)}))
        return ''.join(lst)
        
    def __genDescriptionListSection(self, dictionary, template):
        """
        Private method to generate the list section of a description.
        
        @param dictionary Dictionary containing the info for the
            list section.
        @param template The template to be used for the list. (string)
        @return The list section. (string)
        """
        lst = []
        keys = sorted(list(dictionary.keys()))
        for key in keys:
            lst.append(template.format(
                **{'Name': key,
                   'Description': html_uencode('\n'.join(dictionary[key])),
                   }))
        return ''.join(lst)
        
    def __genParamDescriptionListSection(self, _list):
        """
        Private method to generate the list section of a description.
        
        @param _list list containing the info for the parameter description
            list section (list of lists with three elements)
        @return formatted list section (string)
        """
        lst = []
        for name, type_, lines in _list:
            if type_:
                lst.append(self.parameterTypesListEntryTemplate.format(
                    **{'Name': name,
                       'Type': type_,
                       'Description': html_uencode('\n'.join(lines)),
                       }))
            else:
                lst.append(self.parametersListEntryTemplate.format(
                    **{'Name': name,
                       'Description': html_uencode('\n'.join(lines)),
                       }))
        return ''.join(lst)
        
    def __formatCrossReferenceEntry(self, entry):
        """
        Private method to format a cross reference entry.
        
        This cross reference entry looks like "package.module#member label".
        
        @param entry the entry to be formatted (string)
        @return formatted entry (string)
        """
        if entry.startswith('"'):
            return entry
        elif entry.startswith('<'):
            entry = entry[3:]
        else:
            try:
                reference, label = entry.split(None, 1)
            except ValueError:
                reference = entry
                label = entry
            try:
                path, anchor = reference.split('#', 1)
            except ValueError:
                path = reference
                anchor = ''
            reference = path and "{0}.html".format(path) or ''
            if anchor:
                reference = "{0}#{1}".format(reference, anchor)
            entry = 'href="{0}">{1}</a>'.format(reference, label)
        
        return self.seeLinkTemplate.format(**{'Link': entry})
        
    def __genSeeListSection(self, _list, template):
        """
        Private method to generate the "see also" list section of a
        description.
        
        @param _list List containing the info for the section.
        @param template The template to be used for the list. (string)
        @return The list section. (string)
        """
        lst = []
        for seeEntry in _list:
            seeEntryString = ''.join(seeEntry)
            lst.append(template.format(
                **{'Link': html_uencode(self.__formatCrossReferenceEntry(
                    seeEntryString)),
                   }))
        return '\n'.join(lst)
        
    def __processInlineTags(self, desc):
        """
        Private method to process inline tags.
        
        @param desc One line of the description (string)
        @return processed line with inline tags expanded (string)
        @exception TagError raised to indicate an invalid tag
        """
        start = desc.find('{@')
        while start != -1:
            stop = desc.find('}', start + 2)
            if stop == -1:
                raise TagError("Unterminated inline tag.\n{0}".format(desc))
            
            tagText = desc[start + 1:stop]
            if tagText.startswith('@link'):
                parts = tagText.split(None, 1)
                if len(parts) < 2:
                    raise TagError(
                        "Wrong format in inline tag {0}.\n{1}".format(
                            parts[0], desc))
                
                formattedTag = self.__formatCrossReferenceEntry(parts[1])
                desc = desc.replace("{{{0}}}".format(tagText), formattedTag)
            else:
                tag = tagText.split(None, 1)[0]
                raise TagError(
                    "Unknown inline tag encountered, {0}.\n{1}".format(
                        tag, desc))
            
            start = desc.find('{@')
        
        return desc
        
    def __formatDescription(self, descr):
        """
        Private method to format the contents of the documentation string.
        
        @param descr The contents of the documentation string. (string)
        @exception TagError A tag doesn't have the correct number
            of arguments.
        @return The formated contents of the documentation string. (string)
        """
        if not descr:
            return ""
        
        paragraphs = []
        paramList = []
        returns = []
        returnTypes = []
        exceptionDict = {}
        signalDict = {}
        eventDict = {}
        deprecated = []
        authorInfo = []
        sinceInfo = []
        seeList = []
        lastItem = paragraphs
        inTagSection = False
        
        dlist = descr.splitlines()
        while dlist and not dlist[0]:
            del dlist[0]
        lastTag = ""
        for ditem in dlist:
            ditem = self.__processInlineTags(ditem)
            desc = ditem.strip()
            if desc:
                if desc.startswith(("@param", "@keyparam")):
                    inTagSection = True
                    parts = desc.split(None, 2)
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    paramName = parts[1]
                    if parts[0] == "@keyparam":
                        paramName += '='
                    try:
                        paramList.append([paramName, "", [parts[2]]])
                    except IndexError:
                        paramList.append([paramName, "", []])
                    lastItem = paramList[-1][2]
                elif desc.startswith("@type"):
                    parts = desc.split(None, 1)
                    if lastTag not in ["@param", "@keyparam"]:
                        raise TagError(
                            "{0} line must be preceded by a parameter line\n"
                            .format(parts[0]))
                    inTagSection = True
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    paramList[-1][1] = parts[1]
                elif desc.startswith("@ptype"):
                    inTagSection = True
                    parts = desc.split(None, 2)
                    lastTag = parts[0]
                    if len(parts) < 3:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    param, type_ = parts[1:]
                    for index in range(len(paramList)):
                        if paramList[index][0] == param:
                            paramList[index][1] = type_
                            break
                    else:
                        raise TagError(
                            "Unknow parameter name '{0}' in {1} line.\n"
                            .format(param, parts[0]))
                elif desc.startswith(("@return", "@ireturn")):
                    inTagSection = True
                    parts = desc.split(None, 1)
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    returns = [parts[1]]
                    lastItem = returns
                elif desc.startswith("@rtype"):
                    parts = desc.split(None, 1)
                    if lastTag not in ["@return", "@ireturn"]:
                        raise TagError(
                            "{0} line must be preceded by a return line\n"
                            .format(parts[0]))
                    inTagSection = True
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    returnTypes = [parts[1]]
                    lastItem = returnTypes
                elif desc.startswith(("@exception", "@throws", "@raise")):
                    inTagSection = True
                    parts = desc.split(None, 2)
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    excName = parts[1]
                    try:
                        exceptionDict[excName] = [parts[2]]
                    except IndexError:
                        exceptionDict[excName] = []
                    lastItem = exceptionDict[excName]
                elif desc.startswith("@signal"):
                    inTagSection = True
                    lastTag = desc.split(None, 1)[0]
                    m = _signal(desc, 0)
                    if m is None:
                        raise TagError("Wrong format in @signal line.\n")
                    signalName = 1 and m.group("SignalName1") \
                        or m.group("SignalName2")
                    signalDesc = 1 and m.group("SignalDescription1") \
                        or m.group("SignalDescription2")
                    signalDict[signalName] = []
                    if signalDesc is not None:
                        signalDict[signalName].append(signalDesc)
                    lastItem = signalDict[signalName]
                elif desc.startswith("@event"):
                    inTagSection = True
                    lastTag = desc.split(None, 1)[0]
                    m = _event(desc, 0)
                    if m is None:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    eventName = 1 and m.group("EventName1") \
                        or m.group("EventName2")
                    eventDesc = 1 and m.group("EventDescription1") \
                        or m.group("EventDescription2")
                    eventDict[eventName] = []
                    if eventDesc is not None:
                        eventDict[eventName].append(eventDesc)
                    lastItem = eventDict[eventName]
                elif desc.startswith("@deprecated"):
                    inTagSection = True
                    parts = desc.split(None, 1)
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    deprecated = [parts[1]]
                    lastItem = deprecated
                elif desc.startswith("@author"):
                    inTagSection = True
                    parts = desc.split(None, 1)
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    authorInfo = [parts[1]]
                    lastItem = authorInfo
                elif desc.startswith("@since"):
                    inTagSection = True
                    parts = desc.split(None, 1)
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    sinceInfo = [parts[1]]
                    lastItem = sinceInfo
                elif desc.startswith("@see"):
                    inTagSection = True
                    parts = desc.split(None, 1)
                    lastTag = parts[0]
                    if len(parts) < 2:
                        raise TagError(
                            "Wrong format in {0} line.\n".format(parts[0]))
                    seeList.append([parts[1]])
                    lastItem = seeList[-1]
                elif desc.startswith("@@"):
                    lastItem.append(desc[1:])
                elif desc.startswith("@"):
                    tag = desc.split(None, 1)[0]
                    raise TagError(
                        "Unknown tag encountered, {0}.\n".format(tag))
                else:
                    lastItem.append(ditem)
            elif not inTagSection:
                lastItem.append(ditem)
        
        if paragraphs:
            description = self.__genParagraphs(paragraphs)
        else:
            description = ""
        
        if paramList:
            parameterSect = self.parametersListTemplate.format(
                **{'Parameters': self.__genParamDescriptionListSection(
                    paramList)})
        else:
            parameterSect = ""
        
        if returns:
            returnSect = self.returnsTemplate.format(
                html_uencode('\n'.join(returns)))
        else:
            returnSect = ""
        
        if returnTypes:
            returnTypesSect = self.returnTypesTemplate.format(
                html_uencode('\n'.join(returnTypes)))
        else:
            returnTypesSect = ""
        
        if exceptionDict:
            exceptionSect = self.exceptionsListTemplate.format(
                **{'Exceptions': self.__genDescriptionListSection(
                    exceptionDict, self.exceptionsListEntryTemplate)})
        else:
            exceptionSect = ""
        
        if signalDict:
            signalSect = self.signalsListTemplate.format(
                **{'Signals': self.__genDescriptionListSection(
                    signalDict, self.signalsListEntryTemplate)})
        else:
            signalSect = ""
        
        if eventDict:
            eventSect = self.eventsListTemplate.format(
                **{'Events': self.__genDescriptionListSection(
                    eventDict, self.eventsListEntryTemplate)})
        else:
            eventSect = ""
        
        if deprecated:
            deprecatedSect = self.deprecatedTemplate.format(
                **{'Lines': html_uencode('\n'.join(deprecated))})
        else:
            deprecatedSect = ""
        
        if authorInfo:
            authorInfoSect = self.authorInfoTemplate.format(
                **{'Authors': html_uencode('\n'.join(authorInfo))})
        else:
            authorInfoSect = ""
        
        if sinceInfo:
            sinceInfoSect = self.sinceInfoTemplate.format(
                **{'Info': html_uencode(sinceInfo[0])})
        else:
            sinceInfoSect = ""
        
        if seeList:
            seeSect = self.seeListTemplate.format(
                **{'Links': self.__genSeeListSection(
                    seeList, self.seeListEntryTemplate)})
        else:
            seeSect = ''
        
        return "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}".format(
            deprecatedSect, description, parameterSect, returnSect,
            returnTypesSect, exceptionSect, signalSect, eventSect,
            authorInfoSect, seeSect, sinceInfoSect,
        )
    
    def getQtHelpKeywords(self):
        """
        Public method to retrieve the parts for the QtHelp keywords section.
        
        @return list of tuples containing the name (string) and the ref
            (string). The ref is without the filename part.
        """
        if not self.generated:
            self.genDocument()
        
        return self.keywords
