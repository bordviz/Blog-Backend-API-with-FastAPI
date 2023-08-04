from typing import Optional
from fastapi_users import schemas
from pydantic import BaseModel
from datetime import datetime


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    role_id: int
    email: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class VerifyRead(BaseModel):
    user_id: int
    code: int
    created_at: datetime

class VerifySend(BaseModel):
    code: int