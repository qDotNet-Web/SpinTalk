from typing import Optional

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import BeanieUserDatabase, ObjectIDIDMixin
from .accounts_db import User, get_user_db
from ..utils.settings import settings
from ..mail.mail import send_email


SECRET = settings.SECRET_KEY


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        subject = f"Welcome to SpinTalk!"
        body = f"Welcome to SpinTalk, {user.email}! We're excited to have you on board.\n\n" \
                f"Please verify your email address by clicking the link below:\n\n"
        await send_email(subject, user.email, body)

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        reset_link = f"https://spintalk.net/reset-password?token={token}"
        subject = "Password reset"
        body = f"Hi {user.email}!\n\n" \
               f"Please click the link below to reset your password:\n\n" \
               f"{reset_link}"
        await send_email(subject, user.email, body)

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        verify_link = f"https://spintalk.net/verify?token={token}"
        subject = "Verify your email address"
        body = f"Hi {user.email}!\n\n" \
                f"Please click the link below to verify your email address:\n\n" \
                f"{verify_link}"
        await send_email(subject, user.email, body)


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
