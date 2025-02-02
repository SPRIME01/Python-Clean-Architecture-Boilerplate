from uuid import UUID
from typing import Optional
from pydantic import BaseModel

from your_domain.application.interfaces.user_mgmt_interface import UserMgmtInterface
from your_domain.domain.entities.user import User

class DeleteUserInput(BaseModel):
    """
    Input data for deleting a user.

    Attributes:
        user_id (UUID): Unique identifier of the user to be deleted.
        hard_delete (bool): Flag to determine type of deletion.
            If True, perform a hard delete; otherwise, perform a soft delete.
    """
    user_id: UUID
    hard_delete: bool = False

class DeleteUser:
    """
    Use case for deleting a user.

    Supports both soft and hard deletion. For soft deletion,
    the user entity should be updated (e.g., mark as deleted). For hard deletion,
    the user record is permanently removed from the database.

    Note: The User entity and the repository must be extended to support soft deletion
    (e.g., adding a 'is_deleted' flag) and hard deletion (e.g., a dedicated delete method).
    """
    def __init__(self, user_mgmt: UserMgmtInterface) -> None:
        """
        Initialize the DeleteUser use case with the user management interface.

        Args:
            user_mgmt (UserMgmtInterface): Interface for user management operations.
        """
        self.user_mgmt = user_mgmt

    def execute(self, input_data: DeleteUserInput) -> None:
        """
        Execute the deletion process.

        Args:
            input_data (DeleteUserInput): Data required for deletion.

        Raises:
            ValueError: If the user does not exist.
        """
        user: Optional[User] = self.user_mgmt.find_by_id(input_data.user_id)
        if user is None:
            raise ValueError("User not found")

        if input_data.hard_delete:
            # Hard deletion: permanently remove the user from the database.
            # NOTE: Ensure that the UserMgmtInterface and its repository implementation
            # provide a method for hard deletion (e.g., delete(user) or delete_by_id(user_id)).
            # Here we assume such a method exists as self.user_mgmt.hard_delete(user)
            if hasattr(self.user_mgmt, "hard_delete"):
                self.user_mgmt.hard_delete(user)
            else:
                raise NotImplementedError("Hard delete operation is not implemented in the repository")
        else:
            # Soft deletion: mark the user as deleted.
            # NOTE: The User entity should have an 'is_deleted' attribute or similar.
            # For demonstration purposes, we set an imaginary 'is_deleted' attribute.
            user.is_deleted = True  # This requires the User model to include this field.
            self.user_mgmt.update(user)
