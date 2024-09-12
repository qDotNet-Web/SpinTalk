import motor.motor_asyncio
from beanie import Document, init_beanie
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase
from typing import Optional

from ..utils.settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGODB_URL,
    uuidRepresentation="standard"
)

accounts_db = client[settings.MONGODB_DB_ACCOUNTS]


class User(BeanieBaseUser, Document):
    username: str


async def get_user_db():
    yield BeanieUserDatabase(User)
