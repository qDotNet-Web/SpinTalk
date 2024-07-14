from pydantic import BaseModel, Optional
import datetime


class CreateBan(BaseModel):
    user_id: int = None
    reason: str = None
    expires_at: datetime = None

    class Config:
        orm_mode = True


class UpdateBan(BaseModel):
    user_id: Optional(int) = None
    reason: str = None
    expires_at: datetime = None

    class Config:
        orm_mode = True


class ReadBan(BaseModel):
    id: int = None
    user_id: int = None
    reason: str = None
    expires_at: datetime = None
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
