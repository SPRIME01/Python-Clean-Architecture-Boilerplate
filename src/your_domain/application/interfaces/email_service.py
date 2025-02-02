from typing import Protocol
from your_domain.domain.entities.user import User

class EmailServiceInterface(Protocol):
    def send_confirmation_email(self, user: User) -> None:
        """
        Sends a confirmation email to the user after registration.

        Args:
            user (User): The user for whom the confirmation email is to be sent.
        """
        ...

    def send_password_reset_email(self, user: User) -> None:
        """
        Sends a password reset email to the user.

        Args:
            user (User): The user for whom the password reset email is to be sent.
        """
        ...
