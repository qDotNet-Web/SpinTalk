from contextlib import asynccontextmanager
from beanie import init_beanie
from fastapi import Depends, FastAPI

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
from .accounts.accounts_db import User, accounts_db
from .accounts.accounts_schema import UserCreate, UserUpdate, UserRead
from .accounts.accounts_manager import fastapi_users, auth_backend, current_active_user
from .core.database import db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_beanie(
        database=accounts_db,
        document_models=[
            User,
        ],
    )
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "https://spintalk.net",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return user


@app.on_event("startup")
async def startup_event():
    await db_manager.initialize()


@app.on_event("shutdown")
def shutdown_event():
    db_manager.close()


