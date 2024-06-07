from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate
from typing import Optional


class UserRead(BaseUser):
    username: str = None
    disabled: Optional[bool] = None
    role: Optional[str] = None
    banned: Optional[bool] = None
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    created_at: Optional[str] = None
    last_updated: Optional[str] = None
    last_login: Optional[str] = None
    last_ip: Optional[str] = None


class UserUpdate(BaseUserUpdate):
    username: str
    disabled: Optional[bool] = None
    role: Optional[str] = None
    banned: Optional[bool] = None
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    created_at: Optional[str] = None
    last_updated: Optional[str] = None
    last_login: Optional[str] = None
    last_ip: Optional[str] = None

    class Config:
        orm_mode = True


class UserCreate(BaseUserCreate):
    username: str
    role: str = None
