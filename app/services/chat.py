from database.mongo import chat_collection
from app.models.chat import Chat
from typing import List

async def list_all_chats() -> List[Chat]:
  chats = await chat_collection.find().to_list(100)
  return [Chat(**chat) for chat in chats]

async def list_chats_by_user(user_id) -> List[Chat]:
  chats = await chat_collection.find({"user_id": user_id}).to_list(100)
  return [Chat(**chat) for chat in chats]

async def get_chat_by_id(id) -> Chat | None:
  chat = await chat_collection.find_one({'id': id})
  return chat