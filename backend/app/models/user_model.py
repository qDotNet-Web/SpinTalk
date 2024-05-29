from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    disabled: bool = None
    role: str = None
    banned: bool = None
    banned_until: str = None
    banned_reason: str = None
    created_at: str = None
    last_updated: str = None
    last_login: str = None
    last_ip: str = None


