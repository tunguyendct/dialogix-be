from database.mongo import chat_collection
from app.models.chat import Chat
from typing import List

async def list_all_chats() -> List[Chat]:
  return await chat_collection.find().to_list(100) # type: ignore

async def list_chats_by_user(user_id: Chat['user_id']) -> List[Chat]:
  return await chat_collection.find({"user_id": user_id}).to_list(100) # type: ignore

async def get_chat_by_id(id: Chat['_id']) -> Chat | None:
  return await chat_collection.find_one({'_id': id}) # type: ignore