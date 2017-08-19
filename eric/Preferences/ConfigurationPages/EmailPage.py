# -*- coding: utf-8 -*-

# Copyright (c) 2006 - 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing the Email configuration page.
"""

from __future__ import unicode_literals

import smtplib
import socket

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication

from E5Gui import E5MessageBox

from .ConfigurationPageBase import ConfigurationPageBase
from .Ui_EmailPage import Ui_EmailPage

import Preferences


class EmailPage(ConfigurationPageBase, Ui_EmailPage):
    """
    Class implementing the Email configuration page.
    """
    def __init__(self):
        """
        Constructor
        """
        super(EmailPage, self).__init__()
        self.setupUi(self)
        self.setObjectName("EmailPage")
        
        # set initial values
        try:
            import googleapiclient      # __IGNORE_WARNING__
            self.googleMailCheckBox.setChecked(
                Preferences.getUser("UseGoogleMailOAuth2"))
        except ImportError:
            # missing libraries, disable Google Mail
            self.googleMailCheckBox.setChecked(False)
            self.googleMailCheckBox.setEnabled(False)
            self.googleMailInfoLabel.setText(self.tr(
                "<p>The Google Mail Client API is not installed."
                " Use <code>pip install --upgrade google-api-python-client"
                "</code> to install it.</p>"))
            Preferences.setUser("UseGoogleMailOAuth2", False)
        
        self.mailServerEdit.setText(Preferences.getUser("MailServer"))
        self.portSpin.setValue(Preferences.getUser("MailServerPort"))
        self.emailEdit.setText(Preferences.getUser("Email"))
        self.signatureEdit.setPlainText(Preferences.getUser("Signature"))
        self.mailAuthenticationGroup.setChecked(
            Preferences.getUser("MailServerAuthentication"))
        self.mailUserEdit.setText(Preferences.getUser("MailServerUser"))
        self.mailPasswordEdit.setText(
            Preferences.getUser("MailServerPassword"))
        encryption = Preferences.getUser("MailServerEncryption")
        if encryption == "TLS":
            self.useTlsButton.setChecked(True)
        elif encryption == "SSL":
            self.useSslButton.setChecked(True)
        else:
            self.noEncryptionButton.setChecked(True)
        
    def save(self):
        """
        Public slot to save the Email configuration.
        """
        Preferences.setUser(
            "UseGoogleMailOAuth2",
            self.googleMailCheckBox.isChecked())
        Preferences.setUser(
            "MailServer",
            self.mailServerEdit.text())
        Preferences.setUser(
            "MailServerPort",
            self.portSpin.value())
        Preferences.setUser(
            "Email",
            self.emailEdit.text())
        Preferences.setUser(
            "Signature",
            self.signatureEdit.toPlainText())
        Preferences.setUser(
            "MailServerAuthentication",
            self.mailAuthenticationGroup.isChecked())
        Preferences.setUser(
            "MailServerUser",
            self.mailUserEdit.text())
        Preferences.setUser(
            "MailServerPassword",
            self.mailPasswordEdit.text())
        if self.useTlsButton.isChecked():
            encryption = "TLS"
        elif self.useSslButton.isChecked():
            encryption = "SSL"
        else:
            encryption = "No"
        Preferences.setUser("MailServerEncryption", encryption)
    
    def __updatePortSpin(self):
        """
        Private slot to set the value of the port spin box depending upon
        the selected encryption method.
        """
        if self.useSslButton.isChecked():
            self.portSpin.setValue(465)
        elif self.useTlsButton.isChecked():
            self.portSpin.setValue(587)
        else:
            self.portSpin.setValue(25)
    
    @pyqtSlot(bool)
    def on_noEncryptionButton_toggled(self, checked):
        """
        Private slot handling a change of no encryption button.
        
        @param checked current state of the button
        @type bool
        """
        self.__updatePortSpin()
    
    @pyqtSlot(bool)
    def on_useSslButton_toggled(self, checked):
        """
        Private slot handling a change of SSL encryption button.
        
        @param checked current state of the button
        @type bool
        """
        self.__updatePortSpin()
    
    @pyqtSlot(bool)
    def on_useTlsButton_toggled(self, checked):
        """
        Private slot handling a change of TLS encryption button.
        
        @param checked current state of the button
        @type bool
        """
        self.__updatePortSpin()
    
    def __updateTestButton(self):
        """
        Private slot to update the enabled state of the test button.
        """
        self.testButton.setEnabled(
            self.mailAuthenticationGroup.isChecked() and
            self.mailUserEdit.text() != "" and
            self.mailPasswordEdit.text() != "" and
            self.mailServerEdit.text() != ""
        )
    
    @pyqtSlot(str)
    def on_mailServerEdit_textChanged(self, txt):
        """
        Private slot to handle a change of the text of the mail server edit.
        
        @param txt current text of the edit (string)
        @type str
        """
        self.__updateTestButton()
    
    @pyqtSlot(bool)
    def on_mailAuthenticationGroup_toggled(self, checked):
        """
        Private slot to handle a change of the state of the authentication
        group.
        
        @param checked state of the group (boolean)
        """
        self.__updateTestButton()
    
    @pyqtSlot(str)
    def on_mailUserEdit_textChanged(self, txt):
        """
        Private slot to handle a change of the text of the user edit.
        
        @param txt current text of the edit (string)
        """
        self.__updateTestButton()
    
    @pyqtSlot(str)
    def on_mailPasswordEdit_textChanged(self, txt):
        """
        Private slot to handle a change of the text of the user edit.
        
        @param txt current text of the edit (string)
        """
        self.__updateTestButton()
    
    @pyqtSlot()
    def on_testButton_clicked(self):
        """
        Private slot to test the mail server login data.
        """
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        QApplication.processEvents()
        try:
            if self.useSslButton.isChecked():
                server = smtplib.SMTP_SSL(self.mailServerEdit.text(),
                                          self.portSpin.value(),
                                          timeout=10)
            else:
                server = smtplib.SMTP(self.mailServerEdit.text(),
                                      self.portSpin.value(),
                                      timeout=10)
                if self.useTlsButton.isChecked():
                    server.starttls()
            try:
                server.login(self.mailUserEdit.text(),
                             self.mailPasswordEdit.text())
                QApplication.restoreOverrideCursor()
                E5MessageBox.information(
                    self,
                    self.tr("Login Test"),
                    self.tr("""The login test succeeded."""))
            except (smtplib.SMTPException, socket.error) as e:
                QApplication.restoreOverrideCursor()
                if isinstance(e, smtplib.SMTPResponseException):
                    errorStr = e.smtp_error.decode()
                elif isinstance(e, socket.timeout):
                    errorStr = str(e)
                elif isinstance(e, socket.error):
                    try:
                        errorStr = e[1]
                    except TypeError:
                        errorStr = str(e)
                else:
                    errorStr = str(e)
                E5MessageBox.critical(
                    self,
                    self.tr("Login Test"),
                    self.tr(
                        """<p>The login test failed.<br>Reason: {0}</p>""")
                    .format(errorStr))
            server.quit()
        except (smtplib.SMTPException, socket.error) as e:
            QApplication.restoreOverrideCursor()
            if isinstance(e, smtplib.SMTPResponseException):
                errorStr = e.smtp_error.decode()
            elif isinstance(e, socket.timeout):
                errorStr = str(e)
            elif isinstance(e, socket.error):
                try:
                    errorStr = e[1]
                except TypeError:
                    errorStr = str(e)
            else:
                errorStr = str(e)
            E5MessageBox.critical(
                self,
                self.tr("Login Test"),
                self.tr("""<p>The login test failed.<br>Reason: {0}</p>""")
                .format(errorStr))


def create(dlg):
    """
    Module function to create the configuration page.
    
    @param dlg reference to the configuration dialog
    @return reference to the instantiated page (ConfigurationPageBase)
    """
    page = EmailPage()
    return page
