from typing import Protocol, Optional
from uuid import UUID
from your_domain.domain.entities.user import User
from your_domain.domain.value_objects.email import Email

class UserMgmtInterface(Protocol):
    def add(self, user: User) -> None:
        ...

    def update(self, user: User) -> None:
        ...

    def find_by_email(self, email: Email) -> Optional[User]:
        ...

    def find_by_id(self, user_id: UUID) -> Optional[User]:
        ...
