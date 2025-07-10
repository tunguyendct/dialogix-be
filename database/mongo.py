import motor.motor_asyncio
from app.config import MONGO_URL, DATABASE_NAME, CHAT_COLLECTION, USER_COLLECTION, MESSAGE_COLLECTION, CONVERSION_COLLECTION


class Database:
    def __init__(self, mongo_url: str, db_name: str):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
        self.db = self.client[db_name]

    def get_user_collection(self):
        return self.db[USER_COLLECTION] # type: ignore

    def get_chat_collection(self):
        return self.db[CHAT_COLLECTION] # type: ignore

    def get_message_collection(self):
        return self.db[MESSAGE_COLLECTION] # type: ignore

    def get_conversation_collection(self):
        return self.db[CONVERSION_COLLECTION] # type: ignore

db = Database(MONGO_URL, DATABASE_NAME) # type: ignore