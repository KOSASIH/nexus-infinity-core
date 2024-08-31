import smtplib
from email.mime.text import MIMEText
from config import get_config

class EmailService:
    def __init__(self, config):
        self.config = config
        self.email_username = None
        self.email_password = None

    def _get_email_username(self):
        if not self.email_username:
            self.email_username = self.config.get_config("email", "username")
        return self.email_username

    def _get_email_password(self):
        if not self.email_password:
            self.email_password = self.config.get_config("email", "password")
        return self.email_password

    def send_email(self, recipient, subject, message):
        """
        Sends an email to a recipient.

        :param recipient: The recipient of the email
        :param subject: The subject of the email
        :param message: The message of the email
        :return: The response from the email server
        """
        email_username = self._get_email_username()
        email_password = self._get_email_password()
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = email_username
        msg['To'] = recipient
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_username, email_password)
        server.sendmail(email_username, recipient, msg.as_string())
        server.quit()
        return "Email sent successfully"

    def send_email_with_attachment(self, recipient, subject, message, attachment):
        """
        Sends an email with an attachment to a recipient.

        :param recipient: The recipient of the email
        :param subject: The subject of the email
        :param message: The message of the email
        :param attachment: The attachment to send with the email
        :return: The response from the email server
        """
        email_username = self._get_email_username()
        email_password = self._get_email_password()
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = email_username
        msg['To'] = recipient
        msg.attach(MIMEText(message, 'plain'))
        with open(attachment, 'rb') as f:
            msg.attach(MIMEApplication(f.read(), Name=os.path.basename(attachment)))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_username, email_password)
        server.sendmail(email_username, recipient, msg.as_string())
        server.quit()
        return "Email sent successfully"
