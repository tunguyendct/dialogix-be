from typing import List
from database.mongo import message_collection
from app.models.message import Message, MessageRequest
import datetime

async def list_all_messages() -> List[Message]:
  return message_collection.find().to_list(100)

async def list_messages_by_chat_id(chat_id: str) -> List[Message]:
  return message_collection.find({"chat_id": chat_id}).to_list(100)

async def get_message_by_id(id: str) -> Message | None:
  return message_collection.find_one({'_id': id})

async def create_message(message: MessageRequest) -> Message:
  message_dict = message.model_dump()
  message_dict['created_at'] = datetime.datetime.now().isoformat()
  result = message_collection.insert_one(message_dict)
  message_dict["_id"] = result.inserted_id
  return Message(**message_dict)