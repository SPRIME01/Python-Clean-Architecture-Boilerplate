from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

C = TypeVar("C")
R = TypeVar("R")

class Command(ABC):
    pass

class Query(ABC):
    pass

class CommandHandler(ABC, Generic[C]):
    @abstractmethod
    def handle(self, command: C) -> None:
        pass

class QueryHandler(ABC, Generic[R]):
    @abstractmethod
    def handle(self, query: Query) -> R:
        pass

class CreateUserCommand(Command):
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class GetUserQuery(Query):
    def __init__(self, user_id: int):
        self.user_id = user_id

class CreateUserCommandHandler(CommandHandler[CreateUserCommand]):
    def handle(self, command: CreateUserCommand) -> None:
        # Implement the logic to create a user
        pass

class GetUserQueryHandler(QueryHandler[Any]):
    def handle(self, query: GetUserQuery) -> Any:
        # Implement the logic to get a user
        pass
