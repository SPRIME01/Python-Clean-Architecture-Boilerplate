from abc import ABC, abstractmethod
from typing import List, Optional
from src.your_domain.domain.models import User, Post, Comment
from src.your_domain.domain.repositories import UserRepository, PostRepository, CommentRepository

class UserService(ABC):
    @abstractmethod
    def create_user(self, username: str, email: str, password: str) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def update_user(self, user_id: int, username: Optional[str], email: Optional[str], password: Optional[str]) -> Optional[User]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass

class PostService(ABC):
    @abstractmethod
    def create_post(self, title: str, content: str, author_id: int) -> Post:
        pass

    @abstractmethod
    def get_post(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    def update_post(self, post_id: int, title: Optional[str], content: Optional[str]) -> Optional[Post]:
        pass

    @abstractmethod
    def delete_post(self, post_id: int) -> None:
        pass

class CommentService(ABC):
    @abstractmethod
    def create_comment(self, content: str, post_id: int, author_id: int) -> Comment:
        pass

    @abstractmethod
    def get_comment(self, comment_id: int) -> Optional[Comment]:
        pass

    @abstractmethod
    def update_comment(self, comment_id: int, content: Optional[str]) -> Optional[Comment]:
        pass

    @abstractmethod
    def delete_comment(self, comment_id: int) -> None:
        pass

class UserServiceImpl(UserService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str, email: str, password: str) -> User:
        user = User(id=0, username=username, email=email, is_active=True)
        self.user_repository.add(user)
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(user_id)

    def update_user(self, user_id: int, username: Optional[str], email: Optional[str], password: Optional[str]) -> Optional[User]:
        user = self.user_repository.get_by_id(user_id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            self.user_repository.update(user)
        return user

    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete(user_id)

class PostServiceImpl(PostService):
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def create_post(self, title: str, content: str, author_id: int) -> Post:
        post = Post(id=0, title=title, content=content, author_id=author_id)
        self.post_repository.add(post)
        return post

    def get_post(self, post_id: int) -> Optional[Post]:
        return self.post_repository.get_by_id(post_id)

    def update_post(self, post_id: int, title: Optional[str], content: Optional[str]) -> Optional[Post]:
        post = self.post_repository.get_by_id(post_id)
        if post:
            if title:
                post.title = title
            if content:
                post.content = content
            self.post_repository.update(post)
        return post

    def delete_post(self, post_id: int) -> None:
        self.post_repository.delete(post_id)

class CommentServiceImpl(CommentService):
    def __init__(self, comment_repository: CommentRepository):
        self.comment_repository = comment_repository

    def create_comment(self, content: str, post_id: int, author_id: int) -> Comment:
        comment = Comment(id=0, content=content, post_id=post_id, author_id=author_id)
        self.comment_repository.add(comment)
        return comment

    def get_comment(self, comment_id: int) -> Optional[Comment]:
        return self.comment_repository.get_by_id(comment_id)

    def update_comment(self, comment_id: int, content: Optional[str]) -> Optional[Comment]:
        comment = self.comment_repository.get_by_id(comment_id)
        if comment:
            if content:
                comment.content = content
            self.comment_repository.update(comment)
        return comment

    def delete_comment(self, comment_id: int) -> None:
        self.comment_repository.delete(comment_id)
