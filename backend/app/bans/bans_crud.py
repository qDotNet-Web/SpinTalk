from ..core.database import bans_db
from .bans_schema import CreateBan, UpdateBan, ReadBan
from bson import ObjectId


class BanManager():
    def __init__(self):
        self.bans_db = bans_db

    async def get_ban_by_id(self, ban_id: str):
        """
        Get Ban by ID
        :param ban_id:
        :return:
        """
        return await self.bans_db.bans.find_one({"_id": ban_id})

    async def create_ban(self, ban: CreateBan):
        """
        Create Ban
        :param ban:
        :return:
        """
        return await self.bans_db.bans.insert_one(ban.dict())

    async def update_ban(self, ban_id: str, ban: UpdateBan):
        """
        Update Ban
        :param ban_id:
        :param ban:
        :return:
        """
        return await self.bans_db.bans.update_one({"_id": ObjectId(ban_id)}, {"$set": ban.dict(exclude_unset=True)})

    async def delete_ban(self, ban_id: str):
        """
        Delete Ban
        :param ban_id:
        :return:
        """
        return await self.bans_db.bans.delete_one({"_id": ObjectId(ban_id)})


def get_ban_manager():
    return BanManager()
