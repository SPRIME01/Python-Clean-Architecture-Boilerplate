import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from pydantic import BaseSettings

# Import the EmailServiceInterface to implement it
from src.your_domain.application.interfaces.email_service import EmailServiceInterface
from your_domain.domain.entities.user import User

# SMTPSettings holds configuration for the SMTP server.
class SMTPSettings(BaseSettings):
    smtp_server: str  # e.g., "smtp.sendgrid.net" or your SMTP host
    smtp_port: int    # e.g., 587 for TLS
    smtp_username: str  # SMTP username
    smtp_password: str  # SMTP password
    use_tls: bool = True  # Indicates whether to use TLS
    from_email: str  # The email address used in the "From" field

    class Config:
        env_file = ".env"  # Use a .env file to load environment variables

class EmailService(EmailServiceInterface):
    def __init__(self, settings: SMTPSettings) -> None:
        """
        Initializes the EmailService with the given SMTP settings.

        Args:
            settings (SMTPSettings): Configuration for the SMTP server.
        """
        self.settings = settings

    def send_confirmation_email(self, user: User) -> None:
        """
        Sends an email confirmation message to the user.

        Args:
            user (User): The user to send the confirmation email to.
        """
        subject = "Email Confirmation"
        # In a real implementation, include a proper token or link for confirmation.
        body = (
            f"Hello,\n\n"
            f"Please confirm your email by clicking on the link below:\n"
            f"http://example.com/confirm?user_id={user.id}\n\n"
            f"Thank you!"
        )
        self._send_email(to_email=str(user.email.address), subject=subject, body=body)

    def send_password_reset_email(self, user: User) -> None:
        """
        Sends a password reset email to the user.

        Args:
            user (User): The user to send the password reset email to.
        """
        subject = "Password Reset Request"
        # In a real-world scenario, include a secure token to reset the password.
        body = (
            f"Hello,\n\n"
            f"You have requested to reset your password. Please click on the link below to proceed:\n"
            f"http://example.com/reset-password?user_id={user.id}\n\n"
            f"If you did not request a password reset, please ignore this email."
        )
        self._send_email(to_email=str(user.email.address), subject=subject, body=body)

    def _send_email(self, to_email: str, subject: str, body: str) -> None:
        """
        Internal helper that sends an email via SMTP.

        Args:
            to_email (str): Recipient's email address.
            subject (str): Email subject.
            body (str): Email body content.

        Raises:
            smtplib.SMTPException: If there is an error sending the email.
        """
        # Create a MIME message
        msg = MIMEMultipart()
        msg["From"] = self.settings.from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            # Set up the SMTP connection
            with smtplib.SMTP(self.settings.smtp_server, self.settings.smtp_port) as server:
                if self.settings.use_tls:
                    server.starttls()
                server.login(self.settings.smtp_username, self.settings.smtp_password)
                server.send_message(msg)
        except smtplib.SMTPException as e:
            # Exception handling and logging should be extended as needed.
            raise e
