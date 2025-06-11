from database.mongo import db
from app.config import CHAT_COLLECTION

chat_collection = db[CHAT_COLLECTION] # type: ignore

def list_all_chats():
  return list(chat_collection.find())