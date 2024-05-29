from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import os


class Settings():
    MONGODB_URL = os.getenv("MONGODB_URL")
    MONGODB_DB_ACCOUNTS = "accounts_db"
    MONGODB_DB_REPORTS = "reports_db"
    MONGODB_DB_CHATS = "chats_db"
    SECRET_KEY = os.getenv("SECRET_KEY")

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


settings = Settings()

