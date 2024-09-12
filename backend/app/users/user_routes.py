from fastapi import APIRouter, Depends
from .user_crud import UserManager


user_router = APIRouter()

@user_router.get("/get_user_by_id/{user_id}")
async def get_user_by_id(user_id: str, user_manager: UserManager = Depends(UserManager)):
    return await user_manager.get_user_by_id(user_id)
    
@user_router.get("/get_user_by_email/{email}")
async def get_user_by_email(email: str, user_manager: UserManager = Depends(UserManager)):
   return await user_manager.get_user_by_email(email)
    
@user_router.get("/get_all_users")
async def get_all_users(user_manager: UserManager = Depends(UserManager)):
    return await user_manager.get_all_users()

@user_router.put("/update_user/{user_id}")
async def update_user(user_id: str, user_manager: UserManager = Depends(UserManager)):
    return await user_manager.update_user(user_id, UpdateUser)

@user_router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str, user_manager: UserManager = Depends(UserManager)):
    return await user_manager.delete_user(user_id)
