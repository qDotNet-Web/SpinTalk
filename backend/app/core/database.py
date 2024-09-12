from motor.motor_asyncio import AsyncIOMotorClient
from ..utils.settings import settings


class Database:
    client: AsyncIOMotorClient = None
    accounts_db = None
    reports_db = None
    chats_db = None
    bans_db = None

    @classmethod
    async def initialize(cls):
        """
        Initialisiert die Verbindung zur MongoDB-Datenbank und erstellt die benötigten Sammlungen,
        falls sie nicht existieren.
        """
        cls.client = AsyncIOMotorClient(settings.MONGODB_URL)

        cls.reports_db = cls.client[settings.MONGODB_DB_REPORTS]
        if "reports" not in await cls.reports_db.list_collection_names():
            await cls.reports_db.create_collection("Reports")
            print("Created reports collection")

        cls.chats_db = cls.client[settings.MONGODB_DB_CHATS]
        if "chats" not in await cls.chats_db.list_collection_names():
            await cls.chats_db.create_collection("Chats")
            print("Created chats collection")

        cls.bans_db = cls.client[settings.MONGODB_DB_BANS]
        if "bans" not in await cls.bans_db.list_collection_names():
            await cls.bans_db.create_collection("Bans")
            print("Created bans collection")

    @classmethod
    def close(cls):
        cls.client.close()

    @classmethod
    async def users_exists(cls, collection_name: str, field: str, value) -> bool:
        """
        :param collection_name:
        :param field:
        :param value:
        :return: bool
        """
        if cls.accounts_db is None:
            raise ValueError("Database Users not initialized")

        accounts_collection = cls.accounts_db[collection_name]
        document = await accounts_collection.find_one({field: value})
        return document is not None

    @classmethod
    async def chats_exists(cls, collection_name: str, field: str, value) -> bool:
        """
        :param collection_name:
        :param field:
        :param value:
        :return: bool
        """
        if cls.chats_db is None:
            raise ValueError("Database Chats not initialized")

        chats_collection = cls.chats_db[collection_name]
        document = await chats_collection.find_one({field: value})
        return document is not None

    @classmethod
    async def reports_exists(cls, collection_name: str, field: str, value) -> bool:
        """
        :param collection_name:
        :param field:
        :param value:
        :return: bool
        """
        if cls.reports_db is None:
            raise ValueError("Database Reports not initialized")

        reports_collection = cls.reports_db[collection_name]
        document = await reports_collection.find_one({field: value})
        return document is not None

    @classmethod
    async def bans_exists(cls, collection_name: str, field: str, value) -> bool:
        """
        :param collection_name:
        :param field:
        :param value:
        :return: bool
        """
        if cls.bans_db is None:
            raise ValueError("Database Bans not initialized")

        bans_collection = cls.bans_db[collection_name]
        document = await bans_collection.find_one({field: value})
        return document is not None


db_manager = Database()
reports_db = db_manager.reports_db
chats_db = db_manager.chats_db
bans_db = db_manager.bans_db
accounts_db = db_manager.accounts_db