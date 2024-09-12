from fastapi_users import schemas
from typing import Optional
from beanie import PydanticObjectId
from pydantic import Field
from datetime import datetime


class UserRead(schemas.BaseUser[PydanticObjectId]):
    username: Optional[str] = None
    status: Optional[str] = None
    role: Optional[str] = None
    created_at: Optional[str] = None
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    banned_from: Optional[str] = None
    last_updated: Optional[str] = None
    last_login: Optional[str] = None
    last_ip: Optional[str] = None


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    status: Optional[str] = None
    role: Optional[str] = None
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    banned_from: Optional[str] = None
    last_updated: Optional[str] = None
    last_login: Optional[str] = None
    last_ip: Optional[str] = None

    class Config:
        from_attributes = True


class UserRegistration(schemas.BaseUserCreate):
    username: str


class UserCreate(schemas.BaseUserCreate):
    status: str = "active"
    role: str = "user"
    created_at: datetime = Field(default_factory=datetime.now)
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    banned_from: Optional[str] = None
    last_updated: datetime = Field(default_factory=datetime.now)
    last_login: Optional[str] = None
    last_ip: Optional[str] = None

