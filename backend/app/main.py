from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import auth_router

app = FastAPI()

origins = [
    "https://spintalk.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router, prefix="/auth")
