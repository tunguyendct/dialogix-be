from pymongo import MongoClient
from app.config import MONGO_URL, DATABASE_NAME, CHAT_COLLECTION, USER_COLLECTION, MESSAGE_COLLECTION

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME] # type: ignore
chat_collection = db[CHAT_COLLECTION] # type: ignore
message_collection = db[MESSAGE_COLLECTION] # type: ignore
user_collection = db[USER_COLLECTION] # type: ignore