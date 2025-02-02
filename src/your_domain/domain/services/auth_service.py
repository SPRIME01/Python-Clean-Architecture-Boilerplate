import datetime
from typing import Any
import jwt  # PyJWT package
from pydantic import BaseSettings

from src.your_domain.application.interfaces.auth_service import AuthServiceInterface
from your_domain.domain.entities.user import User

class JWTSettings(BaseSettings):
    """
    Settings required for JWT token generation and validation.
    """
    jwt_secret: str  # Secret key used for encoding and decoding
    jwt_algorithm: str = "HS256"  # Algorithm used for JWT encoding (default: HS256)
    token_expiration_seconds: int = 3600  # Token expiration time in seconds

    class Config:
        env_file = ".env"  # Environment file that contains the JWT settings

class AuthService(AuthServiceInterface):
    """
    AuthService implements AuthServiceInterface using JWT (OAuth2 style tokens).
    """
    def __init__(self, settings: JWTSettings) -> None:
        """
        Initialize the AuthService with JWT settings.

        Args:
            settings (JWTSettings): JWT configuration settings.
        """
        self.settings = settings

    def generate_jwt_token(self, user: User) -> str:
        """
        Generate a JWT token for the given user.

        Args:
            user (User): The user object for which to generate the token.

        Returns:
            str: A JWT token string.
        """
        # Payload data for the JWT token.
        payload = {
            "user_id": str(user.id),
            # Set the token's expiration time
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=self.settings.token_expiration_seconds),
            # Set the issued at time
            "iat": datetime.datetime.utcnow(),
        }
        # Encode the payload using the secret and algorithm specified in settings.
        token = jwt.encode(payload, self.settings.jwt_secret, algorithm=self.settings.jwt_algorithm)
        # PyJWT in versions >= 2 returns a str, if older it may return bytes so decode if necessary.
        if isinstance(token, bytes):
            token = token.decode("utf-8")
        return token

    def validate_token(self, token: str) -> bool:
        """
        Validate the provided JWT token.

        Args:
            token (str): The JWT token string to validate.

        Returns:
            bool: True if the token is valid, False otherwise.
        """
        try:
            # Attempt to decode the token. If successful, token is valid.
            jwt.decode(token, self.settings.jwt_secret, algorithms=[self.settings.jwt_algorithm])
            return True
        except jwt.ExpiredSignatureError:
            # Token has expired.
            return False
        except jwt.InvalidTokenError:
            # Token is invalid.
            return False
