from typing import List
from bson import ObjectId
from app.models.base import PyObjectId 
from app.models.message import Message, MessageRequest, Role
import datetime
from app.core.openapi_client import AzureOpenAIClient


class MessageService:
  def __init__(self, db, client: AzureOpenAIClient):
    self.db = db
    self.openai_client = client

  async def list_messages_by_chat_id(self, chat_id: str) -> list[Message]:
    return await self.db.find({'chat_id': ObjectId(chat_id)}).sort('created_at', 1).to_list(100)

  async def get_message_by_id(self, id: str) -> Message | None:
    return await self.db.find_one({'_id': ObjectId(id)})

  async def create_message_and_reply(self, message: MessageRequest) -> Message | None:
    await self.save_and_return_message(message)
    chat_id = message.chat_id
    messages = await self.list_messages_by_chat_id(str(chat_id))
    ai_message = await self.create_ai_message(chat_id=str(chat_id), messages=messages)
    return ai_message

  async def save_and_return_message(self, message: MessageRequest):
    message_dict = message.model_dump()
    message_dict['chat_id'] = ObjectId(message.chat_id)
    message_dict['created_at'] = datetime.datetime.now().isoformat()
    result = await self.db.insert_one(message_dict)
    message_dict['id'] = result.inserted_id
    return Message(**message_dict)


  async def create_ai_message(self, chat_id: str, messages: List[Message]) -> Message:
    conversation = [{'role': msg['role'], 'content': msg['content']} for msg in messages]
    ai_response = self.openai_client.generate_message_with_conversation(messages=conversation) or ''
    message_model = MessageRequest(chat_id=PyObjectId(chat_id), role=Role.ASSISTANT, content=ai_response)
    ai_message = await self.save_and_return_message(message_model) # type: ignore
    return ai_message