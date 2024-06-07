from fastapi import Request
from .exceptions import *


async def request_handler(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        if isinstance(e, BaseAPIException):
            return e.response()
        raise e