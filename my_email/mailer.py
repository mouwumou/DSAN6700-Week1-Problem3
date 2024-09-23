from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from pathlib import Path
from smtplib import SMTP
from typing import Optional

from email.message import EmailMessage


def send_email(sender, recipient, subject, body):
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    if body is not None:
        msg.attach(MIMEText(body, "plain"))

    s = SMTP("localhost", 1025)
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()
