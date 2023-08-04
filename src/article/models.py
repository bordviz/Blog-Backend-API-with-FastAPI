from datetime import datetime
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from auth.models import User


class Article(Base):
    __tablename__ = 'article'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey(User.id))
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    dislikes = Column(Integer, default=0)

class Comment(Base):
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    article_id = Column(Integer, ForeignKey(Article.id))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey(User.id))