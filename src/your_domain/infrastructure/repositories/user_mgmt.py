from uuid import UUID
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Import the UserMgmtInterface to implement it
from src.your_domain.application.interfaces.user_mgmt import UserMgmtInterface
# Import the User entity and Email value object
from your_domain.domain.entities.user import User
from your_domain.domain.value_objects.email import Email

# This repository uses an ORM (SQLAlchemy in this example) to manage User entity persistence.
# Note: The ORM mapping for User should be set up separately (e.g., with SQLAlchemy declarative base).

class UserMgmtRepository(UserMgmtInterface):
    def __init__(self, session: Session) -> None:
        """
        Initialize the repository with a SQLAlchemy session.

        Args:
            session (Session): SQLAlchemy session for DB transactions.
        """
        self.session = session

    def add(self, user: User) -> None:
        """
        Add a new User to the database.

        Args:
            user (User): User entity to be added.

        Raises:
            SQLAlchemyError: If there's an error during the database operation.
        """
        try:
            # Add the user instance to the current session
            self.session.add(user)
            # Commit the transaction to persist the new user
            self.session.commit()
        except SQLAlchemyError as e:
            # Roll back the session in case of an error
            self.session.rollback()
            # Re-raise the exception or handle logging as needed
            raise e

    def update(self, user: User) -> None:
        """
        Update an existing User in the database.

        Args:
            user (User): User entity with updated data.

        Raises:
            SQLAlchemyError: If there's an error during the database operation.
        """
        try:
            # Use merge to update the existing user record with new values
            self.session.merge(user)
            # Commit the changes to the database
            self.session.commit()
        except SQLAlchemyError as e:
            # Roll back the session in case of error
            self.session.rollback()
            raise e

    def find_by_email(self, email: Email) -> Optional[User]:
        """
        Find a User in the database by email.

        Args:
            email (Email): Email value object representing the email.

        Returns:
            Optional[User]: User entity if found, else None.

        Raises:
            SQLAlchemyError: If there's an error during the database operation.
        """
        try:
            # Assuming User has an 'email' column that stores the email address as a string.
            user = self.session.query(User).filter_by(email=email.address).first()
            return user
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def find_by_id(self, user_id: UUID) -> Optional[User]:
        """
        Find a User in the database by unique identifier.

        Args:
            user_id (UUID): Unique identifier of the user.

        Returns:
            Optional[User]: User entity if found, else None.

        Raises:
            SQLAlchemyError: If there's an error during the database operation.
        """
        try:
            user = self.session.query(User).filter_by(id=user_id).first()
            return user
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

# To complete this implementation:
# 1. Ensure that the SQLAlchemy ORM mappings for the User entity are correctly defined.
# 2. Configure the SQLAlchemy session (e.g., using sessionmaker) and pass it to this repository.
# 3. Handle the exceptions and logging as per your application's requirements.
