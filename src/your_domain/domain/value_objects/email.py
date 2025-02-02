from pydantic import BaseModel, EmailStr
from typing import Any

class Email(BaseModel):
    _address: EmailStr

    def __init__(self, address: EmailStr) -> None:
        super().__init__(_address=address)

    @property
    def address(self) -> EmailStr:
        return self._address

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Email):
            return self._address == other._address
        return False

    def __hash__(self) -> int:
        return hash(self._address)

    def __str__(self) -> str:
        return str(self._address)
