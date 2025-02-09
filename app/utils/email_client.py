#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class HTMLEmailSender:
    """Simple HTML email sender that connects to an SMTP server and sends HTML emails."""

    def __init__(
        self, smtp_server: str, smtp_port: int, username: str, password: str, use_tls: bool = False
    ) -> None:
        """
        Initialize with SMTP server details.

        :param smtp_server: SMTP server address (e.g., 'smtp.gmail.com')
        :param smtp_port: SMTP port (e.g., 587 for TLS or 465 for SSL)
        :param username: Email username
        :param password: Email password or app-specific password
        :param use_tls: If True, use TLS (starttls). Otherwise, use SSL.
        """
        self.smtp_server: str = smtp_server
        self.smtp_port: int = smtp_port
        self.username: str = username
        self.password: str = password
        self.use_tls: bool = use_tls

    def send_email(
        self, from_addr: str, to_addrs: str | list[str], subject: str, html_body: str
    ) -> None:
        """
        Send an HTML email.

        :param from_addr: Sender's email address.
        :param to_addrs: Recipient email address or a list of addresses.
        :param subject: Email subject.
        :param html_body: HTML content of the email.
        """
        # Create a MIME message with HTML content.
        msg = MIMEMultipart("alternative")
        msg["From"] = from_addr
        msg["To"] = ", ".join(to_addrs) if isinstance(to_addrs, list) else to_addrs
        msg["Subject"] = subject

        # Attach the HTML part.
        msg.attach(MIMEText(html_body, "html"))

        try:
            # Connect to the SMTP server using TLS or SSL.
            if self.use_tls:
                server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            else:
                server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)

            server.set_debuglevel(0)  # 0: Disable debug output, 1: Enable debug output.
            server.ehlo()
            if self.use_tls:
                server.starttls()
                server.ehlo()
            server.login(self.username, self.password)
            server.sendmail(from_addr, to_addrs, msg.as_string())
            server.quit()
        except Exception as e:
            raise e
