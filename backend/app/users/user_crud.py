from ..core.database import accounts_db
from ..accounts.accounts_schema import UserRead, UserUpdate
from bson import ObjectId
from fastapi import HTTPException

class UserManager: 
    def __init__(self):
        self.accounts_db = accounts_db

    async def get_user_by_id(self, user_id: str) -> UserRead:
        try:
            user = await self.accounts_db.users.find_one({"_id": ObjectId(user_id)})
            if not user:
                raise HTTPException(status_code=404, detail=f"Benutzer mit ID {user_id} nicht gefunden")
            return user
        except ValueError:
            raise HTTPException(status_code=400, detail="Ungültige Benutzer-ID")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Interner Serverfehler: {str(e)}")

    async def get_user_by_email(self, email: str) -> UserRead: 
        try:
            user = await self.accounts_db.users.find_one({"email": email})
            if not user:
                raise HTTPException(status_code=404, detail=f"Benutzer mit E-Mail {email} nicht gefunden")
            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Interner Serverfehler: {str(e)}")

    async def get_all_users(self) -> list[UserRead]:
        try:
            usersList = await self.accounts_db.find()
            if not usersList:
                raise HTTPException(status_code=404, detail="Keine Benutzer gefunden")
            return usersList
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Interner Serverfehler: {str(e)}")
    
    async def update_user(self, user_id: str, user: UserUpdate) -> UserRead:
        try:
            return await self.accounts_db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict(exclude_unset=True)})
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Interner Serverfehler: {str(e)}")

    async def delete_user(self, user_id: str) -> None: 
        try:
            result = await self.accounts_db.users.delete_one({"_id": ObjectId(user_id)})
            if result.deleted_count == 0:
                raise HTTPException(status_code=404, detail=f"Benutzer mit ID {user_id} nicht gefunden")
            return True
        except ValueError:
            raise HTTPException(status_code=400, detail="Ungültige Benutzer-ID")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Interner Serverfehler: {str(e)}")
