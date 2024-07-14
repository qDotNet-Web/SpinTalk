from fastapi import FastAPI, APIRouter
from bans_crud import get_ban_manager

bans_router = APIRouter()


@bans_router.get("")
def read_all_bans():
