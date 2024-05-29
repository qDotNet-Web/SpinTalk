from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from starlette import status

from ..schemas.user_schema import UserInDB
from ..routes.auth_router import pwd_context, oauth2_scheme, SECRET_KEY, ALGORITHM
from ..core.database import db


async def get_user(username: str):
    user = await db.accounts_db.find_one({"username": username})
    if user:
        return UserInDB(**user)
    return None


async def create_user(user: UserInDB):
    await db.accounts_db.insert_one(user.dict())


async def authenticate_user(username: str, password: str):
    user = await get_user(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(username)
    if user is None:
        raise credentials_exception
    return user
