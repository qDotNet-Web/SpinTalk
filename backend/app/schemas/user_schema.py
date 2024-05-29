from pydantic import BaseModel
from typing import Optional


class UserInDB(BaseModel):
    username: str
    email: str
    hashed_password: str
    disabled: Optional[bool] = None
    role: Optional[str] = None
    banned: Optional[bool] = None
    banned_until: Optional[str] = None
    banned_reason: Optional[str] = None
    created_at: Optional[str] = None
    last_updated: Optional[str] = None
    last_login: Optional[str] = None
    last_ip: Optional[str] = None


class User(BaseModel):
    username: str
    email: str
    password: str
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


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
