from database.mongo import chat_collection
from app.models.chat import Chat, ChatRequest
from typing import List
import datetime

async def list_all_chats() -> List[Chat]:
  return chat_collection.find().to_list(100)

async def list_chats_by_user(user_id: Chat['user_id']) -> List[Chat]:
  return chat_collection.find({"user_id": user_id}).to_list(100)

async def get_chat_by_id(id: Chat['_id']) -> Chat | None:
  return chat_collection.find_one({'_id': id})

async def create_chat(chat: ChatRequest) -> Chat:
  chat_dict = chat.model_dump()
  chat_dict['created_at'] = datetime.datetime.now().isoformat()
  result =  chat_collection.insert_one(chat_dict)
  chat_dict["_id"] = result.inserted_id
  return Chat(**chat_dict)