from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserRegisteredEvent(BaseModel):
    """
    Event triggered when a new user registers and an email confirmation is required.

    Attributes:
        user_id (UUID): Unique identifier of the registered user.
        email (EmailStr): Email address of the registered user.
        registered_at (datetime): Timestamp when the user was registered.
        confirmation_token (str): Token used for verifying the user's email.
    """
    user_id: UUID
    email: EmailStr
    registered_at: datetime
    confirmation_token: str
