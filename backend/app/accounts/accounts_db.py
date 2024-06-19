import motor.motor_asyncio
from beanie import Document, init_beanie
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase
from pydantic import EmailStr

from ..utils.settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGODB_URL,
    uuidRepresentation="standard"
)

accounts_db = client[settings.MONGODB_DB_ACCOUNTS]


class User(BeanieBaseUser, Document):
    email: EmailStr
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Settings:
        collection = "users"


async def get_user_db():
    yield BeanieUserDatabase(User)
