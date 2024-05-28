from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    MONGODB_URL = os.getenv("MONGODB_URL")
    MONGODB_DB_ACCOUNTS = "accounts_db"
    MONGODB_DB_REPORTS = "reports_db"
    MONGODB_DB_CHATS = "chats_db"
    SECRET_KEY = os.getenv("SECRET_KEY")


settings = Settings()

