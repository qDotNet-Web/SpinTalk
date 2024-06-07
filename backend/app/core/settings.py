from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import os


class Settings:
    MONGODB_URL: str = os.getenv("MONGODB_URL")
    MONGODB_DB_ACCOUNTS: str = "accounts_db"
    MONGODB_DB_REPORTS: str = "reports_db"
    MONGODB_DB_CHATS: str = "chats_db"
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
