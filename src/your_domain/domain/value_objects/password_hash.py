from pydantic import BaseModel, Field
import bcrypt
from typing import Optional

class PasswordHash(BaseModel):
    """Value object that encapsulates password hashing and verification logic using BCrypt."""

    hashed_password: bytes = Field(
        description="The BCrypt hashed password"
    )

    @classmethod
    def create(cls, plain_password: str) -> "PasswordHash":
        """Creates a new PasswordHash from a plain text password."""
        if not plain_password:
            raise ValueError("Password cannot be empty")

        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
        return cls(hashed_password=hashed)

    def verify(self, plain_password: str) -> bool:
        """Verifies if the plain text password matches the hash."""
        if not plain_password:
            return False

        return bcrypt.checkpw(
            plain_password.encode('utf-8'),
            self.hashed_password
        )

    class Config:
        frozen = True  # Makes the value object immutable
        arbitrary_types_allowed = True  # Allows bytes type for hashed_password
