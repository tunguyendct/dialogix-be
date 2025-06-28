from typing import List
from database.mongo import message_collection
from app.models.message import Message, MessageRequest
import datetime
from core.openapi_client import generate_text_with_conversation


async def list_all_messages() -> List[Message]:
  return message_collection.find().to_list(100)


async def list_messages_by_chat_id(chat_id: str) -> List[Message]:
  return message_collection.find({"chat_id": chat_id}).to_list(100)


async def get_message_by_id(id: str) -> Message | None:
  return message_collection.find_one({'_id': id})


async def create_message_and_reply(message: MessageRequest) -> Message | None:
  await save_and_return_message(message)
  chat_id = message.chat_id
  messages = await list_messages_by_chat_id(str(chat_id))
  ai_message = await create_ai_message(chat_id=str(chat_id), messages = messages)
  return ai_message


async def save_and_return_message(message: MessageRequest):
  message_dict = message.model_dump()
  message_dict['created_at'] = datetime.datetime.now().isoformat()
  result = message_collection.insert_one(message_dict)
  message_dict['id'] = result.inserted_id
  return Message(**message_dict)


async def create_ai_message(chat_id: str, messages: List[Message]) -> Message:
  ai_response = generate_text_with_conversation(messages) 
  message_model = {
    'chat_id': chat_id,
    'role': 'assistant',
    'content': ai_response
  }
  ai_message = await save_and_return_message(message_model) # type: ignore
  return ai_message