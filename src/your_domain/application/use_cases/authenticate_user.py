from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from your_domain.application.interfaces.user_mgmt_interface import UserMgmtInterface
from your_domain.application.interfaces.auth_service_interface import AuthServiceInterface
from your_domain.domain.entities.user import User
from your_domain.domain.value_objects.email import Email

class AuthenticateUserInput(BaseModel):
    """
    Input data for authenticating a user.
    """
    email: EmailStr
    plain_text_password: constr(min_length=6)

class AuthenticateUser:
    """
    Use case for authenticating a user. This use case validates the provided credentials
    and returns a JWT token if authentication is successful.
    """
    def __init__(
        self,
        user_mgmt: UserMgmtInterface,
        auth_service: AuthServiceInterface
    ) -> None:
        """
        Initialize the AuthenticateUser use case with required dependencies.

        Args:
            user_mgmt (UserMgmtInterface): Interface for user management operations.
            auth_service (AuthServiceInterface): Service for providing JWT token generation.
        """
        self.user_mgmt = user_mgmt
        self.auth_service = auth_service

    def execute(self, input_data: AuthenticateUserInput) -> str:
        """
        Execute the authentication process.

        Args:
            input_data (AuthenticateUserInput): Input data containing email and plain text password.

        Returns:
            str: A JWT token string if authentication is successful.

        Raises:
            ValueError: If authentication fails due to invalid credentials.
        """
        # Construct the Email value object
        email_vo = Email(address=input_data.email)
        # Retrieve the user based on email
        user: Optional[User] = self.user_mgmt.find_by_email(email_vo)
        if user is None:
            raise ValueError("Invalid credentials")

        # Validate the provided password against the stored password hash
        if not user.verify_password(input_data.plain_text_password):
            raise ValueError("Invalid credentials")

        # If credentials are valid, generate and return a JWT token
        jwt_token = self.auth_service.generate_jwt_token(user)
        return jwt_token
