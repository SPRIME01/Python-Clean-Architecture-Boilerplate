from abc import ABC, abstractmethod
from typing import List, Optional
from src.your_domain.domain.models import User, Post, Comment

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass

class PostRepository(ABC):
    @abstractmethod
    def get_by_id(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    def get_all(self) -> List[Post]:
        pass

    @abstractmethod
    def add(self, post: Post) -> None:
        pass

    @abstractmethod
    def update(self, post: Post) -> None:
        pass

    @abstractmethod
    def delete(self, post_id: int) -> None:
        pass

class CommentRepository(ABC):
    @abstractmethod
    def get_by_id(self, comment_id: int) -> Optional[Comment]:
        pass

    @abstractmethod
    def get_all(self) -> List[Comment]:
        pass

    @abstractmethod
    def add(self, comment: Comment) -> None:
        pass

    @abstractmethod
    def update(self, comment: Comment) -> None:
        pass

    @abstractmethod
    def delete(self, comment_id: int) -> None:
        pass

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_all(self) -> List[User]:
        return self.session.query(User).all()

    def add(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()

    def update(self, user: User) -> None:
        self.session.merge(user)
        self.session.commit()

    def delete(self, user_id: int) -> None:
        user = self.get_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()

class SqlAlchemyPostRepository(PostRepository):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, post_id: int) -> Optional[Post]:
        return self.session.query(Post).filter(Post.id == post_id).first()

    def get_all(self) -> List[Post]:
        return self.session.query(Post).all()

    def add(self, post: Post) -> None:
        self.session.add(post)
        self.session.commit()

    def update(self, post: Post) -> None:
        self.session.merge(post)
        self.session.commit()

    def delete(self, post_id: int) -> None:
        post = self.get_by_id(post_id)
        if post:
            self.session.delete(post)
            self.session.commit()

class SqlAlchemyCommentRepository(CommentRepository):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, comment_id: int) -> Optional[Comment]:
        return self.session.query(Comment).filter(Comment.id == comment_id).first()

    def get_all(self) -> List[Comment]:
        return self.session.query(Comment).all()

    def add(self, comment: Comment) -> None:
        self.session.add(comment)
        self.session.commit()

    def update(self, comment: Comment) -> None:
        self.session.merge(comment)
        self.session.commit()

    def delete(self, comment_id: int) -> None:
        comment = self.get_by_id(comment_id)
        if comment:
            self.session.delete(comment)
            self.session.commit()
