from fastapi.security import OAuth2PasswordBearer
from fastapi_users.authentication import JWTStrategy
import os


class Settings:
    MONGODB_URL: str = os.getenv("MONGODB_URL")
    MONGODB_DB_ACCOUNTS: str = "accounts_db"
    MONGODB_DB_REPORTS: str = "reports_db"
    MONGODB_DB_CHATS: str = "chats_db"
    MONGODB_DB_BANS: str = "bans_db"
    SECRET_KEY: str = os.getenv("SECRET_KEY")

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_PORT: int = os.getenv("MAIL_PORT")
    MAIL_SERVER: str = os.getenv("MAIL_SERVER")
    MAIL_STARTTLS: bool = os.getenv("MAIL_STARTTLS")
    MAIL_SSL_TLS: bool = os.getenv("MAIL_SSL_TLS")

    def get_jwt_strategy(self) -> JWTStrategy:
        return JWTStrategy(secret=self.SECRET_KEY, lifetime_seconds=3600)


settings = Settings()
