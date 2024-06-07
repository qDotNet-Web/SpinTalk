import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase

from ..core.settings import settings


client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGODB_URL,
    uuidRepresentation="standard"
)

db = client[settings.MONGODB_DB_ACCOUNTS]


class User(BeanieBaseUser, Document):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)



