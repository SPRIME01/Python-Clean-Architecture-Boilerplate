from typing import Protocol
from your_domain.domain.entities.user import User

class AuthServiceInterface(Protocol):
    def generate_jwt_token(self, user: User) -> str:
        """
        Generates a JWT token for the given user.

        Args:
            user (User): The user object for which a JWT is generated.

        Returns:
            str: The generated JWT token.
        """
        ...

    def validate_token(self, token: str) -> bool:
        """
        Validates the provided JWT token.

        Args:
            token (str): The JWT token string to validate.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        ...
