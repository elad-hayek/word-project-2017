# -*- coding: utf-8 -*-
"""
Description      : Sends the eamil with the document

Author           : Elad Hayek
FileName         : client.py
Date             : 27.5.17
Version          : 1.0
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

SUBJECT = 'word document'
BODY = 'you received a word document'
GMAIL = 'eladword2017@gmail.com'
PASSWORD = 'zxcvvcxz!123'


def send(addrto, docx_path, name):
    """
    sends an email with the document

    :arg addrto = the eamil to send to
    :type addrto = string

    :arg docx_path = the document path
    :type docx_path = string

    :arg name = the document's name
    :type name = string
    """
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = name
    msg['To'] = addrto

    text = MIMEText(BODY)
    msg.attach(text)

    openfile = open(docx_path, 'rb')
    doc = MIMEApplication(openfile.read(),
                          _subtype='vnd.openxmlformats-officedocument.'
                                   'wordprocessingml.document')
    doc.add_header('Content-Disposition', 'attachment', filename=name+'.docx')
    msg.attach(doc)
    openfile.close()

    print("connecting")
    s = smtplib.SMTP('smtp.gmail.com', '587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(GMAIL, PASSWORD)
    print("connected")
    s.sendmail(GMAIL, addrto, msg.as_string())
    print("sent")
    s.quit()
