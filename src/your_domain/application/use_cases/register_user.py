from typing import Callable
from pydantic import BaseModel, EmailStr, constr
from your_domain.domain.entities.user import User
from src.your_domain.application.interfaces.user_mgmt import UserMgmtInterface
from src.your_domain.domain.events.user_registered import UserRegisteredEvent
from your_domain.domain.value_objects.email import Email

class RegisterUserInput(BaseModel):
    """
    Input data for registering a user.
    """
    email: EmailStr
    plain_text_password: constr(min_length=6)

class RegisterUser:
    """
    Use case that validates input, checks for uniqueness,
    persists a new user and triggers a UserRegisteredEvent.
    """
    def __init__(
        self,
        user_mgmt: UserMgmtInterface,
        event_publisher: Callable[[UserRegisteredEvent], None]
    ) -> None:
        """
        Initialize the RegisterUser use case with required dependencies.

        Args:
            user_mgmt (UserMgmtInterface): Interface for user management operations.
            event_publisher (Callable[[UserRegisteredEvent], None]): Callable to publish events.
        """
        self.user_mgmt = user_mgmt
        self.event_publisher = event_publisher

    def execute(self, input_data: RegisterUserInput) -> User:
        """
        Execute the registration process.

        Args:
            input_data (RegisterUserInput): Input data containing email and password.

        Returns:
            User: The newly created user.

        Raises:
            ValueError: If a user with the provided email already exists.
        """
        # Validate uniqueness by creating an Email value object
        email_vo = Email(address=input_data.email)
        if self.user_mgmt.find_by_email(email_vo) is not None:
            raise ValueError(f"User with email {input_data.email} already exists")

        # Create the user entity via the domain factory method
        user = User.create(input_data.email, input_data.plain_text_password)

        # Persist the user using the User Management Interface
        self.user_mgmt.add(user)

        # Trigger a domain event to allow for email confirmation processing
        # In a real system, 'confirmation_token' should be securely generated.
        confirmation_token = "dummy-token"
        event = UserRegisteredEvent(
            user_id=user.id,
            email=user.email.address,
            registered_at=user.created_at,
            confirmation_token=confirmation_token
        )
        self.event_publisher(event)

        return user
