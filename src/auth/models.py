from datetime import datetime
from fastapi_users.db import SQLAlchemyBaseUserTable
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, TIMESTAMP

class Role(Base):
    __tablename__ = 'role'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    permission = Column(String)

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey(Role.id), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

class Verify(Base):
    __tablename__ = 'verify'
    __table_args__ = {'extend_existing': True}

    user_id = Column(Integer, ForeignKey(User.id), primary_key=True, nullable=False)
    code = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)