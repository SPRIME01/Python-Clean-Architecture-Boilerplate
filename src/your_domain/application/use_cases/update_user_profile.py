from uuid import UUID
from typing import Optional
from pydantic import BaseModel, EmailStr, constr

from your_domain.application.interfaces.user_mgmt_interface import UserMgmtInterface
from your_domain.domain.entities.user import User
from your_domain.domain.value_objects.email import Email
from your_domain.domain.value_objects.password_hash import PasswordHash

class UpdateUserProfileInput(BaseModel):
    """
    Input data for updating a user's profile.

    Attributes:
        user_id (UUID): Unique identifier of the user.
        new_email (Optional[EmailStr]): New email address to update.
        new_plain_text_password (Optional[str]): New password in plain text (minimum 6 characters).
    """
    user_id: UUID
    new_email: Optional[EmailStr] = None
    new_plain_text_password: Optional[constr(min_length=6)] = None

class UpdateUserProfile:
    """
    Use case for updating user details. It retrieves a user, validates new input,
    checks for uniqueness if email is updated, and persists the modified user.
    """
    def __init__(self, user_mgmt: UserMgmtInterface) -> None:
        """
        Initialize the use case with a user management interface.

        Args:
            user_mgmt (UserMgmtInterface): Interface for user management operations.
        """
        self.user_mgmt = user_mgmt

    def execute(self, input_data: UpdateUserProfileInput) -> User:
        """
        Execute the update user profile use case.

        Args:
            input_data (UpdateUserProfileInput): Input data containing the user ID and new details.

        Returns:
            User: The updated user.

        Raises:
            ValueError: If the user does not exist or the new email is already in use.
        """
        # Retrieve the user from the repository
        user = self.user_mgmt.find_by_id(input_data.user_id)
        if user is None:
            raise ValueError("User not found")

        # If new email is provided, validate and check for uniqueness
        if input_data.new_email:
            new_email_vo = Email(address=input_data.new_email)
            # Check if any other user is already using this email
            existing_user = self.user_mgmt.find_by_email(new_email_vo)
            if existing_user and existing_user.id != user.id:
                raise ValueError("Email already taken by another user")
            user.email = new_email_vo

        # If new password is provided, generate a new password hash and update the user
        if input_data.new_plain_text_password:
            new_password_hash = PasswordHash.create(input_data.new_plain_text_password)
            user.password_hash = new_password_hash

        # Persist the updated user details
        self.user_mgmt.update(user)
        return user
