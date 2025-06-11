from database.mongo import db
from app.config import USER_COLLECTION

user_collection = db[USER_COLLECTION] # type: ignore

def list_all_users():
  return list(user_collection.find())