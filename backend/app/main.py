from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from beanie import init_beanie
from .accounts.accounts_db import User, accounts_db
from .accounts.accounts_schema import UserCreate, UserUpdate, UserRead
from .accounts.accounts_manager import fastapi_users, auth_backend, current_active_user
from .core.database import db_manager
from .bans.bans_routes import bans_router


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
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
Routers for FastAPI Users Routes
"""
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/api/v1/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/v1/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/api/v1/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/api/v1/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/api/v1/users",
    tags=["users"],
)


@app.get("/api/v1/auth/validate-token")
async def validate_token(user: User = Depends(current_active_user)):
    return {"status": "valid"}


"""
Router for Bans
"""
"""app.include_router(
    bans_router.router,
    prefix="/api/v1/bans",
    tags=["bans"]
)"""

@app.on_event("startup")
async def startup_event():
    await db_manager.initialize()


@app.on_event("shutdown")
def shutdown_event():
    db_manager.close()


