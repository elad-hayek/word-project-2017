# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

SUBJECT = 'word document'
BODY = 'you received a word document'
GMAIL = 'eladword2017@gmail.com'
PASSWORD = 'zxcvvcxz!123'

def send(addrto, docx_path, name):
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = name
    msg['To'] = addrto

    text = MIMEText(BODY)
    msg.attach(text)


    openfile = open(docx_path, 'rb')
    doc = MIMEApplication(openfile.read(), _subtype='vnd.openxmlformats-officedocument.wordprocessingml.document')
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
