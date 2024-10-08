from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from smtplib import SMTP


def send_email(sender, recipient, subject, body):
    """Send an email using the Simple Mail Transfer Protocol (SMTP).

    This function creates an email message with the provided sender, recipient,
    subject, and body, and sends it via SMTP using a local server running on
    localhost at port 1025.

    Args:
        sender (str): The email address of the sender.
        recipient (str): The email address of the recipient.
        subject (str): The subject line of the email.
        body (str): The body of the email message. If None is provided,
            no message body will be sent.

    Raises:
        SMTPException: If there is any error in connecting to the SMTP server
            or sending the email.

    Example:
        To send an email from 'test@example.com' to 'recipient@example.com'
        with a subject and body, you can use the following code:

        >>> send_email('test@example.com', 'recipient@example.com', 'Hello', 'This is a test email.')

    Notes:
        This function connects to an SMTP server at 'localhost' on port 1025,
        which is often used for testing with local SMTP servers such as
        `MailHog` or `smtp4dev`. For real-world usage, replace the server
        configuration with a valid SMTP host and port.

    Returns:
        None
    """

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
