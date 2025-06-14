import os
from pymongo import MongoClient
from app.config import MONGO_URL, DATABASE_NAME, CHAT_COLLECTION, USER_COLLECTION, MESSAGE_COLLECTION
from motor.motor_asyncio import AsyncIOMotorCollection

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME] # type: ignore
chat_collection: AsyncIOMotorCollection = db[CHAT_COLLECTION] # type: ignore
message_collection: AsyncIOMotorCollection = db[MESSAGE_COLLECTION] # type: ignore
user_collection:AsyncIOMotorCollection = db[USER_COLLECTION] # type: ignore