# -*- coding: utf-8 -*-

# Copyright (c) 2004 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing templates for the documentation generator (lists style).
"""

from __future__ import unicode_literals

#################################################
##  Common templates for index and docu files  ##
#################################################

headerTemplate = \
'''<!DOCTYPE html>
<html><head>
<title>{{Title}}</title>
<meta charset="UTF-8">
</head>
<body style="background-color:{BodyBgColor};color:{BodyColor}">'''

footerTemplate = '''
</body></html>'''

#########################################
##  Templates for documentation files  ##
#########################################

moduleTemplate = \
'''<a NAME="top" ID="top"></a>
<h1 style="background-color:{Level1HeaderBgColor};color:{Level1HeaderColor}">
{{Module}}</h1>
{{ModuleDescription}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Global Attributes</h3>
{{GlobalsList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Classes</h3>
{{ClassList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Functions</h3>
{{FunctionList}}
<hr />'''

rbFileTemplate = \
'''<a NAME="top" ID="top"></a>
<h1 style="background-color:{Level1HeaderBgColor};color:{Level1HeaderColor}">
{{Module}}</h1>
{{ModuleDescription}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Global Attributes</h3>
{{GlobalsList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Classes</h3>
{{ClassList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Modules</h3>
{{RbModulesList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Functions</h3>
{{FunctionList}}
<hr />'''

classTemplate = \
'''<hr />
<a NAME="{{Anchor}}" ID="{{Anchor}}"></a>
<h2 style="background-color:{CFBgColor};color:{CFColor}">{{Class}}</h2>
{{ClassDescription}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Derived from</h3>
{{ClassSuper}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Class Attributes</h3>
{{GlobalsList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Class Methods</h3>
{{ClassMethodList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Methods</h3>
{{MethodList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Static Methods</h3>
{{StaticMethodList}}
{{MethodDetails}}
<div align="right"><a style="color:{LinkColor}" href="#top">Up</a></div>
<hr />'''

methodTemplate = \
'''<a NAME="{{Anchor}}.{{Method}}" ID="{{Anchor}}.{{Method}}"></a>
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
{{Class}}.{{Method}}{{MethodClassifier}}</h3>
<b>{{Method}}</b>(<i>{{Params}}</i>)
{{MethodDescription}}'''

constructorTemplate = \
'''<a NAME="{{Anchor}}.{{Method}}" ID="{{Anchor}}.{{Method}}"></a>
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
{{Class}} (Constructor)</h3>
<b>{{Class}}</b>(<i>{{Params}}</i>)
{{MethodDescription}}'''

rbModuleTemplate = \
'''<hr />
<a NAME="{{Anchor}}" ID="{{Anchor}}"></a>
<h2 style="background-color:{CFBgColor};color:{CFColor}">{{Module}}</h2>
{{ModuleDescription}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Module Attributes</h3>
{{GlobalsList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Classes</h3>
{{ClassesList}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Functions</h3>
{{FunctionsList}}
<hr />
{{ClassesDetails}}
{{FunctionsDetails}}
<div align="right"><a style="color:{LinkColor}" href="#top">Up</a></div>
<hr />'''

rbModulesClassTemplate = \
'''<a NAME="{{Anchor}}" ID="{{Anchor}}"></a>
<h2 style="background-color:{CFBgColor};color:{CFColor}">{{Class}}</h2>
{{ClassDescription}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Derived from</h3>
{{ClassSuper}}
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Methods</h3>
{{MethodList}}
{{MethodDetails}}
<div align="right"><a style="color:{LinkColor}" href="#top">Up</a></div>
<hr />'''

functionTemplate = \
'''<hr />
<a NAME="{{Anchor}}" ID="{{Anchor}}"></a>
<h2 style="background-color:{CFBgColor};color:{CFColor}">{{Function}}</h2>
<b>{{Function}}</b>(<i>{{Params}}</i>)
{{FunctionDescription}}
<div align="right"><a style="color:{LinkColor}" href="#top">Up</a></div>
<hr />'''

listTemplate = \
'''<table>
{{Entries}}
</table>'''

listEntryTemplate = \
'''<tr>
<td><a style="color:{LinkColor}" href="#{{Link}}">{{Name}}</a></td>
<td>{{Deprecated}}{{Description}}</td>
</tr>'''

listEntryNoneTemplate = '''<tr><td>None</td></tr>'''

listEntryDeprecatedTemplate = '''<b>Deprecated.</b>'''

listEntrySimpleTemplate = '''<tr><td>{{Name}}</td></tr>'''

paragraphTemplate = \
'''<p>
{{Lines}}
</p>'''

parametersListTemplate = \
'''<dl>
{{Parameters}}
</dl>'''

parametersListEntryTemplate = \
'''<dt><i>{{Name}}</i></dt>
<dd>
{{Description}}
</dd>'''

parameterTypesListEntryTemplate = \
'''<dt><i>{{Name}}</i> ({{Type}})</dt>
<dd>
{{Description}}
</dd>'''

returnsTemplate = \
'''<dl>
<dt>Returns:</dt>
<dd>
{{0}}
</dd>
</dl>'''

returnTypesTemplate = \
'''<dl>
<dt>Return Type:</dt>
<dd>
{{0}}
</dd>
</dl>'''

exceptionsListTemplate = \
'''<dl>
{{Exceptions}}
</dl>'''

exceptionsListEntryTemplate = \
'''<dt>Raises <b>{{Name}}</b>:</dt>
<dd>
{{Description}}
</dd>'''

signalsListTemplate = \
'''<h4>Signals</h4>
<dl>
{{Signals}}
</dl>'''

signalsListEntryTemplate = \
'''<dt>{{Name}}</dt>
<dd>
{{Description}}
</dd>'''

eventsListTemplate = \
'''<h4>Events</h4>
<dl>
{{Events}}
</dl>'''

eventsListEntryTemplate = \
'''<dt>{{Name}}</dt>
<dd>
{{Description}}
</dd>'''

deprecatedTemplate = \
'''<p>
<b>Deprecated.</b>
{{Lines}}
</p>'''

authorInfoTemplate = \
'''<p>
<i>Author(s)</i>:
{{Authors}}
</p>'''

seeListTemplate = \
'''<dl>
<dt><b>See Also:</b></dt>
{{Links}}
</dl>'''

seeListEntryTemplate = \
'''<dd>
{{Link}}
</dd>'''

seeLinkTemplate = '''<a style="color:{LinkColor}" {{Link}}'''

sinceInfoTemplate = \
'''<p>
<b>since</b> {{Info}}
</p>'''

#################################
##  Templates for index files  ##
#################################

indexBodyTemplate = '''
<h1 style="background-color:{Level1HeaderBgColor};color:{Level1HeaderColor}">
{{Title}}</h1>
{{Description}}
{{Subpackages}}
{{Modules}}'''

indexListPackagesTemplate = '''
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Packages</h3>
<table>
{{Entries}}
</table>'''

indexListModulesTemplate = '''
<h3 style="background-color:{Level2HeaderBgColor};color:{Level2HeaderColor}">
Modules</h3>
<table>
{{Entries}}
</table>'''

indexListEntryTemplate = \
'''<tr>
<td><a style="color:{LinkColor}" href="{{Link}}">{{Name}}</a></td>
<td>{{Description}}</td>
</tr>'''

#
# eflag: noqa = E122
