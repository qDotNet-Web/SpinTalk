from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate
from typing import Optional
from beanie import PydanticObjectId


class UserRead(BaseUser[PydanticObjectId]):
    username: str = None
    status: Optional[bool] = None
    role: Optional[str] = None
    created_at: Optional[str] = None
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    banned_from: Optional[str] = None
    last_updated: Optional[str] = None
    last_login: Optional[str] = None
    last_ip: Optional[str] = None


class UserUpdate(BaseUserUpdate):
    username: str
    status: Optional[bool] = None
    role: Optional[str] = None
    created_at: Optional[str] = None
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    banned_from: Optional[str] = None
    last_updated: Optional[str] = None
    last_login: Optional[str] = None
    last_ip: Optional[str] = None

    class Config:
        from_attributes = True


class UserCreate(BaseUserCreate):
    username: str
    role: str = "user"
