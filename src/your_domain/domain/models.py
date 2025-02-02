from typing import List, Optional
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True

class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int

class Comment(BaseModel):
    id: int
    content: str
    post_id: int
    author_id: int

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class CommentCreate(BaseModel):
    content: str
    post_id: int
    author_id: int

class CommentUpdate(BaseModel):
    content: Optional[str] = None
