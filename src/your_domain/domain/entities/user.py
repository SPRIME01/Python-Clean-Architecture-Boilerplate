from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from your_domain.domain.value_objects.email import Email
from your_domain.domain.value_objects.password_hash import PasswordHash

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email: Email
    password_hash: PasswordHash
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))

    @classmethod
    def create(cls, email: str, plain_text_password: str) -> "User":
        # Create value objects from the provided parameters
        email_obj = Email(address=email)
        password_hash_obj = PasswordHash.create(plain_text_password)
        return cls(email=email_obj, password_hash=password_hash_obj)

    def verify_password(self, plain_text_password: str) -> bool:
        return self.password_hash.verify(plain_text_password)

    class Config:
        arbitrary_types_allowed = True
