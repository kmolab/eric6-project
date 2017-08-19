# -*- coding: utf-8 -*-

# Copyright (c) 2017 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to send bug reports.
"""

from __future__ import unicode_literals
try:
    str = unicode       # __IGNORE_EXCEPTION__
except NameError:
    pass

import os
import sys
import base64

import httplib2

import oauth2client.file
from oauth2client import client, tools

from googleapiclient import discovery

import Globals


SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'eric_client_secret.json'
APPLICATION_NAME = 'Eric Python Send Email'


def getCredentials():
    """
    Module function to get the Google credentials.
    
    @return Google Mail credentials
    """
    homeDir = os.path.expanduser('~')
    credentialDir = os.path.join(homeDir, '.credentials')
    if not os.path.exists(credentialDir):
        os.makedirs(credentialDir)
    credentialPath = os.path.join(credentialDir,
                                  'eric-python-email-send.json')
    store = oauth2client.file.Storage(credentialPath)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(
            os.path.join(Globals.getConfigDir(), CLIENT_SECRET_FILE),
            SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
    return credentials


def GoogleMailSendMessage(message):
    """
    Module function to send an email message via Google Mail.
    
    @param message email message to be sent
    @type email.mime.text.MIMEBase
    @return tuple containing a success flag and a result or error message
    @rtype tuple of (bool, str)
    """
    try:
        credentials = getCredentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)
        if sys.version_info[0] == 2:
            message1 = _prepareMessage_v2(message)
        else:
            message1 = _prepareMessage_v3(message)
        result = service.users().messages()\
            .send(userId="me", body=message1).execute()

        return True, result
    except Exception as error:
        return False, str(error)


def _prepareMessage_v2(message):
    """
    Module function to prepare the message for sending (Python2 Variant).
    
    @param message message to be prepared
    @type email.mime.text.MIMEBase
    @return prepared message dictionary
    @rtype dict
    """
    raw = base64.urlsafe_b64encode(message.as_string())
    return {'raw': raw}


def _prepareMessage_v3(message):
    """
    Module function to prepare the message for sending (Python2 Variant).
    
    @param message message to be prepared
    @type email.mime.text.MIMEBase
    @return prepared message dictionary
    @rtype dict
    """
    messageAsBase64 = base64.urlsafe_b64encode(message.as_bytes())
    raw = messageAsBase64.decode()
    return {'raw': raw}


def GoogleMailHelp():
    """
    Module function to get some help about how to enable the Google Mail
    OAuth2 service.
    
    @return help text
    @rtype str
    """
    return (
        "<h2>Steps to turn on the Gmail API</h2>"
        "<ol>"
        "<li>Use <a href='{0}'>this wizard</a> to create or select a project"
        " in the Google Developers Console and automatically turn on the API."
        " Click <b>Continue</b>, then <b>Go to credentials</b>.</li>"
        "<li>At the top of the page, select the <b>OAuth consent screen</b>"
        " tab. Select an <b>Email address</b>, enter a <b>Product name</b> if"
        " not already set, and click the <b>Save</b> button.</li>"
        "<li>Select the <b>Credentials</b> tab, click the <b>Add credentials"
        "</b> button and select <b>OAuth 2.0 client ID</b>.</li>"
        "<li>Select the application type <b>Other</b>, enter the name &quot;"
        "{1}&quot;, and click the <b>Create</b>"
        " button.</li>"
        "<li>Click <b>OK</b> to dismiss the resulting dialog.</li>"
        "<li>Click the (Download JSON) button to the right of the client ID."
        "</li>"
        "<li>Move this file to the eric configuration directory"
        " <code>{2}</code> and rename it <code>{3}</code>.</li>"
        "</ol>".format(
            "https://console.developers.google.com/start/api?id=gmail",
            APPLICATION_NAME,
            Globals.getConfigDir(),
            CLIENT_SECRET_FILE
        )
    )
