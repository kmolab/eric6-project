# -*- coding: utf-8 -*-

# Copyright (c) 2014 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing an import hook converting PyQt5 imports to PyQt4 imports.
"""

from __future__ import unicode_literals

import sys
import importlib


class PyQt4Importer(object):
    """
    Class implementing an importer converting PyQt5 imports to PyQt4
    imports.
    """
    def __init__(self):
        """
        Constructor
        """
        self.__path = None
    
    def find_module(self, fullname, path=None):
        """
        Public method returning the module loader.
        
        @param fullname name of the module to be loaded (string)
        @param path path to resolve the module name (string)
        @return module loader object
        """
        if fullname.startswith("PyQt5"):
            self.__path = path
            return self
        
        return None
    
    @staticmethod
    def QComboBox_currentData(other, role=None):
        """
        Static method to emulate the currentData method of Qt5.
        
        @param other reference to the combo box to get the user data of
        @type QComboBox
        @param role role of which data should be retrieved
        @type int
        @return stored data at current selection
        @rtype any
        """
        import PyQt4.Qt
        if role is None:
            role = PyQt4.Qt.Qt.UserRole
        
        idx = other.currentIndex()
        return other.itemData(idx, role)
    
    def load_module(self, fullname):
        """
        Public method to load a module.
        
        @param fullname name of the module to be loaded (string)
        @return reference to the loaded module (module)
        """
        if fullname in ["PyQt5.QtWidgets", "PyQt5.QtPrintSupport"]:
            newname = "PyQt4.QtGui"
        elif fullname in ["PyQt5.QtWebKitWidgets"]:
            newname = "PyQt4.QtWebKit"
        else:
            newname = fullname.replace("PyQt5", "PyQt4")
        
        module = importlib.import_module(newname)
        sys.modules[fullname] = module
        if fullname == "PyQt5.QtCore":
            import PyQt4.QtGui
            module.qInstallMessageHandler = module.qInstallMsgHandler
            module.QItemSelectionModel = PyQt4.QtGui.QItemSelectionModel
            module.QItemSelection = PyQt4.QtGui.QItemSelection
            module.QSortFilterProxyModel = \
                PyQt4.QtGui.QSortFilterProxyModel
            module.QAbstractProxyModel = PyQt4.QtGui.QAbstractProxyModel
            module.QStringListModel = PyQt4.QtGui.QStringListModel
            
            PyQt4.QtGui.QComboBox.currentData = self.QComboBox_currentData
        return module

try:
    if "--pyqt4" in sys.argv:
        sys.argv.remove("--pyqt4")
        # fake a failed PyQt5 import
        raise ImportError
    import PyQt5    # __IGNORE_WARNING__
except ImportError:
    sys.meta_path.insert(0, PyQt4Importer())
    
    if sys.version_info[0] == 2:
        import sip
        sip.setapi('QString', 2)
        sip.setapi('QVariant', 2)
        sip.setapi('QTextStream', 2)
