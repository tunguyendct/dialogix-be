from typing import List
from database.mongo import message_collection
from app.models.message import Message

async def list_all_messages() -> List[Message]:
  return await message_collection.find().to_list(100) # type: ignore

async def list_messages_by_chat_id(chat_id: Message['chat_id']) -> List[Message]:
  return await message_collection.find({chat_id: chat_id}).to_list(100) # type: ignore

async def get_message_by_id(id: Message['_id']) -> Message | None:
  return await message_collection.find_one({'_id': id}) # type: ignore