from types import NoneType
from typing import List
from pydantic import BaseModel
from datetime import datetime


class CommentCreate(BaseModel):
    text: str
    article_id: int
    author_id: int

class CommentRead(BaseModel):
    id: int
    text: str
    author_id: int
    author_name: str
    created_at: datetime

class ArticleCreate(BaseModel):
    title: str
    text: str
    author_id: int

class ArticleReadShort(BaseModel):
    id: int
    title: str
    text: str
    created_at: datetime
    author_id: int

class ArticleRead(BaseModel):
    id: int
    title: str
    text: str
    created_at: datetime
    author_id: int
    comments: List[CommentRead]
    views: int
    likes: int
    dislikes: int