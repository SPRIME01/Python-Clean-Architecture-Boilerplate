from your_domain.domain.entities.user import User
from src.your_domain.application.interfaces.user_mgmt import UserMgmtInterface
from your_domain.domain.value_objects.email import Email

class UserRegistrationService:
    def __init__(self, user_mgmt: UserMgmtInterface) -> None:
        self.user_mgmt = user_mgmt

    def register_user(self, email: str, plain_text_password: str) -> User:
        email_obj = Email(address=email)
        if self.user_mgmt.find_by_email(email_obj) is not None:
            raise ValueError(f"User with email {email} already exists")
        user = User.create(email, plain_text_password)
        self.user_mgmt.add(user)
        return user
