import secrets
from pydantic import BaseModel, EmailStr
from typing import Optional
from your_domain.application.interfaces.user_mgmt_interface import UserMgmtInterface
from your_domain.application.interfaces.email_service_interface import EmailServiceInterface
from your_domain.domain.entities.user import User
from your_domain.domain.value_objects.email import Email

class ResetPasswordInput(BaseModel):
    """
    Input data for initiating a password reset.

    Attributes:
        email (EmailStr): The email address of the user requesting a password reset.
    """
    email: EmailStr

class ResetPassword:
    """
    Use case for resetting a user's password. This use case generates a secure reset token,
    and sends a password reset email using an email service.
    """
    def __init__(
        self,
        user_mgmt: UserMgmtInterface,
        email_service: EmailServiceInterface
    ) -> None:
        """
        Initialize the ResetPassword use case with required dependencies.

        Args:
            user_mgmt (UserMgmtInterface): Interface for user management operations.
            email_service (EmailServiceInterface): Service to send emails.
        """
        self.user_mgmt = user_mgmt
        self.email_service = email_service

    def execute(self, input_data: ResetPasswordInput) -> str:
        """
        Execute the password reset process.

        Args:
            input_data (ResetPasswordInput): Input data containing the user's email.

        Returns:
            str: The generated password reset token.

        Raises:
            ValueError: If no user exists with the provided email.
        """
        # Create the Email value object from the provided email string
        email_vo = Email(address=input_data.email)

        # Retrieve the user based on email
        user: Optional[User] = self.user_mgmt.find_by_email(email_vo)
        if user is None:
            raise ValueError("User with the provided email does not exist.")

        # Generate a secure reset token (URL-safe)
        reset_token = secrets.token_urlsafe(32)

        # Send password reset email including the reset token.
        # Note: This assumes that the implementation of send_password_reset_email
        # has been adapted to accept a reset token parameter.
        self.email_service.send_password_reset_email(user, reset_token)

        # In a real application, you would store the reset token for later verification.
        return reset_token
