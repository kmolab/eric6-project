# -*- coding: utf-8 -*-

# Copyright (c) 2014 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to enter some user data.
"""

from __future__ import unicode_literals

import os

from PyQt5.QtCore import pyqtSlot, Qt, QEvent
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem

from E5Gui.E5PathPicker import E5PathPickerModes
from E5Gui import E5MessageBox

import Globals
from Globals.E5ConfigParser import E5ConfigParser

from .HgUtilities import getConfigPath
from .HgUserConfigHostFingerprintDialog import \
    HgUserConfigHostFingerprintDialog
from .HgUserConfigHostMinimumProtocolDialog import \
    HgUserConfigHostMinimumProtocolDialog

from .Ui_HgUserConfigDialog import Ui_HgUserConfigDialog

import UI.PixmapCache


class HgUserConfigDialog(QDialog, Ui_HgUserConfigDialog):
    """
    Class implementing a dialog to enter some user data.
    """
    def __init__(self, version=(0, 0, 0), parent=None):
        """
        Constructor
        
        @param version Mercurial version info
        @type tuple of three integers
        @param parent reference to the parent widget
        @type QWidget
        """
        super(HgUserConfigDialog, self).__init__(parent)
        self.setupUi(self)
        
        self.__version = version
        
        self.__minimumProtocols = {
            "tls1.0": self.tr("TLS 1.0"),
            "tls1.1": self.tr("TLS 1.1"),
            "tls1.2": self.tr("TLS 1.2"),
        }
        
        self.lfUserCachePicker.setMode(E5PathPickerModes.DirectoryMode)
        if Globals.isLinuxPlatform():
            self.lfUserCachePicker.setDefaultDirectory(os.path.expanduser(
                "~/.cache/largefiles"))
        elif Globals.isMacPlatform():
            self.lfUserCachePicker.setDefaultDirectory(os.path.expanduser(
                "~/Library/Caches/largefiles"))
        else:
            self.lfUserCachePicker.setDefaultDirectory(os.path.expanduser(
                "~\\AppData\\Local\\largefiles"))
        
        self.fpAddButton.setIcon(UI.PixmapCache.getIcon("plus.png"))
        self.fpDeleteButton.setIcon(UI.PixmapCache.getIcon("minus.png"))
        self.fpEditButton.setIcon(UI.PixmapCache.getIcon("edit.png"))
        
        self.protocolAddButton.setIcon(UI.PixmapCache.getIcon("plus.png"))
        self.protocolDeleteButton.setIcon(UI.PixmapCache.getIcon("minus.png"))
        self.protocolEditButton.setIcon(UI.PixmapCache.getIcon("edit.png"))
        
        self.minimumProtocolComboBox.addItem(self.tr("Default"), "")
        for protocol in sorted(self.__minimumProtocols.keys()):
            self.minimumProtocolComboBox.addItem(
                self.__minimumProtocols[protocol], protocol)
        
        self.fingerprintsList.headerItem().setText(
            self.fingerprintsList.columnCount(), "")
        self.protocolsList.headerItem().setText(
            self.protocolsList.columnCount(), "")
        
        if self.__version < (3, 9, 0):
            self.disableTls10WarningCheckBox.setEnabled(False)
            self.minimumProtocolComboBox.setEnabled(False)
            self.minimumProtcolGroupBox.setEnabled(False)
        
        self.tabWidget.setCurrentIndex(0)
        
        self.__editor = None
        
        self.__config = None
        self.readUserConfig()
    
        self.__updateFingerprintsButtons()
        self.__updateProtocolsButtons()
    
    def writeUserConfig(self):
        """
        Public method to write the user configuration file.
        """
        if self.__config is None:
            self.__config = E5ConfigParser()
        
        ###################################################################
        ## ui section
        ###################################################################
        if "ui" not in self.__config:
            self.__config["ui"] = {}
        self.__config["ui"]["username"] = "{0} <{1}>".format(
            self.userNameEdit.text(),
            self.emailEdit.text(),
        )
        ###################################################################
        ## extensions section
        ###################################################################
        if "extensions" not in self.__config:
            self.__config["extensions"] = {}
        if self.fetchCheckBox.isChecked():
            self.__config["extensions"]["fetch"] = ""
        else:
            if "fetch" in self.__config["extensions"]:
                del self.__config["extensions"]["fetch"]
            self.__config["extensions"]["#fetch"] = ""
        
        if self.gpgCheckBox.isChecked():
            self.__config["extensions"]["gpg"] = ""
        else:
            if "gpg" in self.__config["extensions"]:
                del self.__config["extensions"]["gpg"]
            self.__config["extensions"]["#gpg"] = ""
        
        if self.purgeCheckBox.isChecked():
            self.__config["extensions"]["purge"] = ""
        else:
            if "purge" in self.__config["extensions"]:
                del self.__config["extensions"]["purge"]
            self.__config["extensions"]["#purge"] = ""
        
        if self.queuesCheckBox.isChecked():
            self.__config["extensions"]["mq"] = ""
        else:
            if "mq" in self.__config["extensions"]:
                del self.__config["extensions"]["mq"]
            self.__config["extensions"]["#mq"] = ""
        
        if self.rebaseCheckBox.isChecked():
            self.__config["extensions"]["rebase"] = ""
        else:
            if "rebase" in self.__config["extensions"]:
                del self.__config["extensions"]["rebase"]
            self.__config["extensions"]["#rebase"] = ""
        
        if self.shelveCheckBox.isChecked():
            self.__config["extensions"]["shelve"] = ""
        else:
            if "shelve" in self.__config["extensions"]:
                del self.__config["extensions"]["shelve"]
            self.__config["extensions"]["#shelve"] = ""
        
        if self.stripCheckBox.isChecked():
            self.__config["extensions"]["strip"] = ""
        else:
            if "strip" in self.__config["extensions"]:
                del self.__config["extensions"]["strip"]
            self.__config["extensions"]["#strip"] = ""
        
        if self.histeditCheckBox.isChecked():
            self.__config["extensions"]["histedit"] = ""
        else:
            if "histedit" in self.__config["extensions"]:
                del self.__config["extensions"]["histedit"]
            self.__config["extensions"]["#histedit"] = ""
        
        if self.largefilesCheckBox.isChecked():
            self.__config["extensions"]["largefiles"] = ""
            ###############################################################
            ## largefiles section
            ###############################################################
            if "largefiles" not in self.__config:
                self.__config["largefiles"] = {}
            self.__config["largefiles"]["minsize"] = \
                str(self.lfFileSizeSpinBox.value())
            lfFilePatterns = self.lfFilePatternsEdit.text()
            if lfFilePatterns:
                self.__config["largefiles"]["patterns"] = lfFilePatterns
            elif "patterns" in self.__config["largefiles"]:
                del self.__config["largefiles"]["patterns"]
            lfUserCache = self.lfUserCachePicker.text()
            if lfUserCache:
                self.__config["largefiles"]["usercache"] = lfUserCache
            elif "usercache" in self.__config["largefiles"]:
                del self.__config["largefiles"]["usercache"]
        else:
            if "largefiles" in self.__config["extensions"]:
                del self.__config["extensions"]["largefiles"]
            self.__config["extensions"]["#largefiles"] = ""
        ###################################################################
        ## http_proxy section
        ###################################################################
        if self.proxyHostEdit.text():
            self.__config["http_proxy"] = {
                "host": self.proxyHostEdit.text(),
                "user": self.proxyUserEdit.text(),
                "passwd": self.proxyPasswordEdit.text()
            }
            if self.proxyBypassEdit.text():
                self.__config["http_proxy"]["no"] = \
                    self.proxyBypassEdit.text()
        else:
            if "http_proxy" in self.__config:
                del self.__config["http_proxy"]
        ###################################################################
        ## hostfingerprints/hostsecurity section
        ###################################################################
        if self.__version < (3, 9, 0):
            #
            # delete hostsecurity section
            #
            if "hostsecurity" in self.__config:
                del self.__config["hostsecurity"]
            
            #
            # hostfingerprints section
            #
            if self.fingerprintsList.topLevelItemCount() > 0:
                self.__config["hostfingerprints"] = {}
                for row in range(self.fingerprintsList.topLevelItemCount()):
                    itm = self.fingerprintsList.topLevelItem(row)
                    fingerprint = itm.text(1)
                    if fingerprint.startswith("sha1:"):
                        fingerprint = fingerprint[5:]
                    self.__config["hostfingerprints"][itm.text(0)] = \
                        fingerprint
            else:
                if "hostfingerprints" in self.__config:
                    del self.__config["hostfingerprints"]
        else:
            #
            # delete hostfingerprints section
            #
            if "hostfingerprints" in self.__config:
                del self.__config["hostfingerprints"]
            
            #
            # hostsecurity section
            #
            if "hostsecurity" not in self.__config:
                self.__config["hostsecurity"] = {}
            
            if self.fingerprintsList.topLevelItemCount() > 0:
                self.__clearFingerprints()
                fingerprints = self.__assembleFingerprints()
                for host in fingerprints:
                    key = "{0}:fingerprints".format(host)
                    self.__config["hostsecurity"][key] = \
                        ", ".join(fingerprints[host])
            else:
                self.__clearFingerprints()
            
            if self.disableTls10WarningCheckBox.isChecked():
                disabletls10warning = "true"
            else:
                disabletls10warning = "false"
            self.__config["hostsecurity"]["disabletls10warning"] = \
                disabletls10warning
            
            if self.minimumProtocolComboBox.currentIndex() == 0:
                self.__config.remove_option("hostsecurity", "minimumprotocol")
            else:
                minimumProtocol = self.minimumProtocolComboBox.itemData(
                    self.minimumProtocolComboBox.currentIndex())
                self.__config["hostsecurity"]["minimumprotocol"] = \
                    minimumProtocol
            
            if self.protocolsList.topLevelItemCount() > 0:
                self.__clearMinimumProtocols()
                minimumProtocols = self.__assembleMinimumProtocols()
                for host in minimumProtocols:
                    key = "{0}:minimumprotocol".format(host)
                    self.__config["hostsecurity"][key] = minimumProtocols[host]
            else:
                self.__clearMinimumProtocols()
            
            if len(self.__config.options("hostsecurity")) == 0:
                del self.__config["hostsecurity"]
        ###################################################################
        
        cfgFile = getConfigPath()
        with open(cfgFile, "w") as configFile:
            self.__config.write(configFile)
    
    def readUserConfig(self):
        """
        Public method to read the user configuration file.
        """
        cfgFile = getConfigPath()
        
        self.__config = E5ConfigParser(delimiters=("=",))
        if self.__config.read(cfgFile):
            # step 1: extract user name and email
            try:
                username = self.__config["ui"]["username"].strip()
                if "<" in username and username.endswith(">"):
                    name, email = username[:-1].rsplit("<", 1)
                else:
                    name = username
                    email = ""
                self.userNameEdit.setText(name.strip()),
                self.emailEdit.setText(email.strip()),
            except KeyError:
                pass
            
            # step 2: extract extensions information
            if "extensions" in self.__config:
                self.fetchCheckBox.setChecked(
                    "fetch" in self.__config["extensions"])
                self.gpgCheckBox.setChecked(
                    "gpg" in self.__config["extensions"])
                self.purgeCheckBox.setChecked(
                    "purge" in self.__config["extensions"])
                self.queuesCheckBox.setChecked(
                    "mq" in self.__config["extensions"])
                self.rebaseCheckBox.setChecked(
                    "rebase" in self.__config["extensions"])
                self.shelveCheckBox.setChecked(
                    "shelve" in self.__config["extensions"])
                self.largefilesCheckBox.setChecked(
                    "largefiles" in self.__config["extensions"])
                self.stripCheckBox.setChecked(
                    "strip" in self.__config["extensions"])
                self.histeditCheckBox.setChecked(
                    "histedit" in self.__config["extensions"])
            
            # step 3: extract large files information
            if "largefiles" in self.__config:
                if "minsize" in self.__config["largefiles"]:
                    self.lfFileSizeSpinBox.setValue(
                        self.__config.getint("largefiles", "minsize"))
                if "patterns" in self.__config["largefiles"]:
                    self.lfFilePatternsEdit.setText(
                        self.__config["largefiles"]["patterns"])
                if "usercache" in self.__config["largefiles"]:
                    self.lfUserCachePicker.setText(
                        self.__config["largefiles"]["usercache"])
            
            # step 4: extract http proxy information
            if "http_proxy" in self.__config:
                if "host" in self.__config["http_proxy"]:
                    self.proxyHostEdit.setText(
                        self.__config["http_proxy"]["host"])
                if "user" in self.__config["http_proxy"]:
                    self.proxyUserEdit.setText(
                        self.__config["http_proxy"]["user"])
                if "passwd" in self.__config["http_proxy"]:
                    self.proxyPasswordEdit.setText(
                        self.__config["http_proxy"]["passwd"])
                if "no" in self.__config["http_proxy"]:
                    self.proxyBypassEdit.setText(
                        self.__config["http_proxy"]["no"])
            
            # step 5a: extract host fingerprints
            if "hostfingerprints" in self.__config:
                for host in self.__config.options("hostfingerprints"):
                    if self.__version < (3, 9, 0):
                        QTreeWidgetItem(self.fingerprintsList, [
                            host,
                            self.__config["hostfingerprints"][host]
                        ])
                    else:
                        # convert to hostsecurity fingerprint
                        QTreeWidgetItem(self.fingerprintsList, [
                            host,
                            "sha1:" + self.__config["hostfingerprints"][host]
                        ])
            
            # step 5b: extract hostsecurity fingerprints
            if "hostsecurity" in self.__config:
                for key in self.__config.options("hostsecurity"):
                    if key.endswith(":fingerprints"):
                        host = key.replace(":fingerprints", "")
                        fingerprints = \
                            self.__config["hostsecurity"][key].split(",")
                        for fingerprint in fingerprints:
                            if self.__version < (3, 9, 0):
                                # downgrade from a newer version
                                if fingerprint.startswith("sha1:"):
                                    fingerprint = fingerprint[5:]
                                else:
                                    # Mercurial < 3.9.0 supports sha1
                                    # fingerprints only
                                    continue
                            QTreeWidgetItem(self.fingerprintsList, [
                                host,
                                fingerprint.replace("\\", "").strip()
                            ])
                    
                    elif key == "disabletls10warning":
                        self.disableTls10WarningCheckBox.setChecked(
                            self.__config.getboolean(
                                "hostsecurity", "disabletls10warning"))
                    
                    elif key == "minimumprotocol":
                        minimumProtocol = self.__config["hostsecurity"][key]
                        index = self.minimumProtocolComboBox.findData(
                            minimumProtocol)
                        if index == -1:
                            index = 0
                        self.minimumProtocolComboBox.setCurrentIndex(index)
                    
                    elif key.endswith(":minimumprotocol"):
                        host = key.replace(":minimumprotocol", "")
                        protocol = self.__config["hostsecurity"][key].strip()
                        if protocol in self.__minimumProtocols:
                            itm = QTreeWidgetItem(self.protocolsList, [
                                host,
                                self.__minimumProtocols[protocol]
                            ])
                            itm.setData(1, Qt.UserRole, protocol)
            
            self.__finalizeFingerprintsColumns()
            self.__finalizeProtocolsColumns()
    
    @pyqtSlot()
    def accept(self):
        """
        Public slot to accept the dialog.
        """
        self.writeUserConfig()
        
        super(HgUserConfigDialog, self).accept()
    
    def __clearDialog(self):
        """
        Private method to clear the data of the dialog.
        """
        self.userNameEdit.clear()
        self.emailEdit.clear()
        
        self.fetchCheckBox.setChecked(False)
        self.gpgCheckBox.setChecked(False)
        self.purgeCheckBox.setChecked(False)
        self.queuesCheckBox.setChecked(False)
        self.rebaseCheckBox.setChecked(False)
        self.shelveCheckBox.setChecked(False)
        self.stripCheckBox.setChecked(False)
        self.largefilesCheckBox.setChecked(False)
        self.lfFileSizeSpinBox.setValue(10)
        self.lfFilePatternsEdit.clear()
        self.lfUserCachePicker.clear()
        
        self.proxyHostEdit.clear()
        self.proxyUserEdit.clear()
        self.proxyPasswordEdit.clear()
        self.proxyBypassEdit.clear()
        
        self.fingerprintsList.clear()
        self.__finalizeFingerprintsColumns()
        self.__updateFingerprintsButtons()
        
        self.protocolsList.clear()
        self.__finalizeProtocolsColumns()
        self.__updateProtocolsButtons()
    
    #######################################################################
    ## Methods and slots for the host fingerprint handling below
    #######################################################################
    
    def __clearFingerprints(self):
        """
        Private method to clear the fingerprints from the hostsecurity section.
        """
        if "hostsecurity" in self.__config:
            for key in self.__config.options("hostsecurity"):
                if key.endswith(":fingerprints"):
                    self.__config.remove_option("hostsecurity", key)
    
    def __assembleFingerprints(self):
        """
        Private method to assemble a list of host fingerprints.
        
        @return dictionary with list of fingerprints per host
        @rtype dict with str as key and list of str as value
        """
        hostFingerprints = {}
        for row in range(self.fingerprintsList.topLevelItemCount()):
            itm = self.fingerprintsList.topLevelItem(row)
            host = itm.text(0)
            fingerprint = itm.text(1)
            if host in hostFingerprints:
                hostFingerprints[host].append(fingerprint)
            else:
                hostFingerprints[host] = [fingerprint]
        return hostFingerprints
    
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_fingerprintsList_currentItemChanged(self, current, previous):
        """
        Private slot handling a change of the current fingerprints item.
        
        @param current reference to the current item
        @type QTreeWidgetItem
        @param previous reference to the previous current item
        @type QTreeWidgetItem
        """
        self.__updateFingerprintsButtons()
    
    @pyqtSlot()
    def on_fpAddButton_clicked(self):
        """
        Private slot to add a fingerprints entry.
        """
        dlg = HgUserConfigHostFingerprintDialog(self, version=self.__version)
        if dlg.exec_() == QDialog.Accepted:
            host, fingerprint = dlg.getData()
            itm = QTreeWidgetItem(self.fingerprintsList, [host, fingerprint])
            self.__finalizeFingerprintsColumns()
            self.fingerprintsList.setCurrentItem(itm)
            self.fingerprintsList.scrollToItem(itm)
    
    @pyqtSlot()
    def on_fpDeleteButton_clicked(self):
        """
        Private slot to delete the current fingerprints item.
        """
        itm = self.fingerprintsList.currentItem()
        if itm is not None:
            host = itm.text(0)
            yes = E5MessageBox.yesNo(
                self,
                self.tr("Delete Host Fingerprint"),
                self.tr("""<p>Shall the fingerprint for host <b>{0}</b>"""
                        """ really be deleted?</p>""").format(host))
            if yes:
                self.fingerprintsList.takeTopLevelItem(
                    self.fingerprintsList.indexOfTopLevelItem(itm))
                del itm
                self.__finalizeFingerprintsColumns()
    
    @pyqtSlot()
    def on_fpEditButton_clicked(self):
        """
        Private slot to edit the current fingerprints item.
        """
        itm = self.fingerprintsList.currentItem()
        if itm is not None:
            host = itm.text(0)
            fingerprint = itm.text(1)
            dlg = HgUserConfigHostFingerprintDialog(self, host, fingerprint,
                                                    version=self.__version)
            if dlg.exec_() == QDialog.Accepted:
                host, fingerprint = dlg.getData()
                itm.setText(0, host)
                itm.setText(1, fingerprint)
                self.__finalizeFingerprintsColumns()
                self.fingerprintsList.scrollToItem(itm)
    
    def __finalizeFingerprintsColumns(self):
        """
        Private method to resize and sort the host fingerprints columns.
        """
        for col in range(self.fingerprintsList.columnCount()):
            self.fingerprintsList.resizeColumnToContents(col)
        self.fingerprintsList.sortItems(0, Qt.AscendingOrder)
    
    def __updateFingerprintsButtons(self):
        """
        Private slot to update the host fingerprints edit buttons.
        """
        enable = self.fingerprintsList.currentItem() is not None
        self.fpDeleteButton.setEnabled(enable)
        self.fpEditButton.setEnabled(enable)
    
    #######################################################################
    ## Methods and slots for the host minimum protocol handling below
    #######################################################################
    
    def __clearMinimumProtocols(self):
        """
        Private method to clear the minimum protocols from the hostsecurity
        section.
        """
        if "hostsecurity" in self.__config:
            for key in self.__config.options("hostsecurity"):
                if key.endswith(":minimumprotocol"):
                    self.__config.remove_option("hostsecurity", key)
    
    def __assembleMinimumProtocols(self):
        """
        Private method to assemble a list of host minimum protocols.
        
        @return dictionary with list of minimum protocol per host
        @rtype dict with str as key and str as value
        """
        minimumProtocols = {}
        for row in range(self.protocolsList.topLevelItemCount()):
            itm = self.protocolsList.topLevelItem(row)
            host = itm.text(0)
            minimumProtocol = itm.data(1, Qt.UserRole)
            minimumProtocols[host] = minimumProtocol
        return minimumProtocols
    
    @pyqtSlot(QTreeWidgetItem, QTreeWidgetItem)
    def on_protocolsList_currentItemChanged(self, current, previous):
        """
        Private slot handling a change of the current minimum protocol item.
        
        @param current reference to the current item
        @type QTreeWidgetItem
        @param previous reference to the previous current item
        @type QTreeWidgetItem
        """
        self.__updateProtocolsButtons()
    
    @pyqtSlot()
    def on_protocolAddButton_clicked(self):
        """
        Private slot to add a minimum protocol entry.
        """
        dlg = HgUserConfigHostMinimumProtocolDialog(self.__minimumProtocols,
                                                    self)
        if dlg.exec_() == QDialog.Accepted:
            host, protocol = dlg.getData()
            itm = QTreeWidgetItem(self.protocolsList, [
                host,
                self.__minimumProtocols[protocol]
            ])
            itm.setData(1, Qt.UserRole, protocol)
            self.__finalizeProtocolsColumns()
            self.protocolsList.setCurrentItem(itm)
            self.protocolsList.scrollToItem(itm)
    
    @pyqtSlot()
    def on_protocolDeleteButton_clicked(self):
        """
        Private slot to delete the current minimum protocol item.
        """
        itm = self.protocolsList.currentItem()
        if itm is not None:
            host = itm.text(0)
            yes = E5MessageBox.yesNo(
                self,
                self.tr("Delete Host Minimum Protocol"),
                self.tr("""<p>Shall the minimum protocol entry for host"""
                        """ <b>{0}</b> really be deleted?</p>""").format(host))
            if yes:
                self.protocolsList.takeTopLevelItem(
                    self.protocolsList.indexOfTopLevelItem(itm))
                del itm
                self.__finalizeProtocolsColumns()
    
    @pyqtSlot()
    def on_protocolEditButton_clicked(self):
        """
        Private slot to edit the current minimum protocol item.
        """
        itm = self.protocolsList.currentItem()
        if itm is not None:
            host = itm.text(0)
            protocol = itm.data(1, Qt.UserRole)
            dlg = HgUserConfigHostMinimumProtocolDialog(
                self.__minimumProtocols, self, host, protocol)
            if dlg.exec_() == QDialog.Accepted:
                host, protocol = dlg.getData()
                itm.setText(0, host)
                itm.setText(1, self.__minimumProtocols[protocol])
                itm.setData(1, Qt.UserRole, protocol)
                self.__finalizeProtocolsColumns()
                self.protocolsList.scrollToItem(itm)
    
    def __finalizeProtocolsColumns(self):
        """
        Private method to resize and sort the host fingerprints columns.
        """
        for col in range(self.protocolsList.columnCount()):
            self.protocolsList.resizeColumnToContents(col)
        self.protocolsList.sortItems(0, Qt.AscendingOrder)
    
    def __updateProtocolsButtons(self):
        """
        Private slot to update the host minimum protocol edit buttons.
        """
        enable = self.protocolsList.currentItem() is not None
        self.protocolDeleteButton.setEnabled(enable)
        self.protocolEditButton.setEnabled(enable)
    
    #######################################################################
    ## Slot to edit the user configuration in an editor below
    #######################################################################
    
    @pyqtSlot()
    def on_editorButton_clicked(self):
        """
        Private slot to open the user configuration file in a text editor.
        """
        from QScintilla.MiniEditor import MiniEditor
        cfgFile = getConfigPath()
        
        yes = E5MessageBox.yesNo(
            self,
            self.tr("Edit User Configuration"),
            self.tr("""You will loose all changes made in this dialog."""
                    """ Shall the data be saved first?"""),
            icon=E5MessageBox.Warning,
            yesDefault=True)
        if yes:
            self.writeUserConfig()
        
        self.__editor = MiniEditor(cfgFile, "Properties", self)
        self.__editor.setWindowModality(Qt.WindowModal)
        self.__editor.installEventFilter(self)
        self.__editor.show()
    
    def eventFilter(self, watched, event):
        """
        Public method called to filter the event queue.
        
        @param watched reference to the object being watched
        @type QObject
        @param event event to be handled
        @type QEvent
        @return flag indicating, if we handled the event
        @rtype bool
        """
        if watched is self.__editor and event.type() == QEvent.Close:
            self.__editor.closeEvent(event)
            if event.isAccepted():
                self.__clearDialog()
                self.readUserConfig()
                return True
        
        return False
