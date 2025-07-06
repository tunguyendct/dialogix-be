from bson import ObjectId
from app.models.chat import Chat, ChatRequest
import datetime


class ChatService:
  def __init__(self, db):
    self.db = db

  async def list_all_chats(self) -> list[Chat]:
    return self.db.find().to_list(100)

  async def list_chats_by_user(self, user_id: str) -> list[Chat]:
    return self.db.find({"user_id": ObjectId(user_id)}).to_list(100)

  async def get_chat_by_id(self, id: str) -> Chat | None:
    return self.db.find_one({'_id': ObjectId(id)})

  async def create_chat(self, chat: ChatRequest) -> Chat:
    chat_dict = chat.model_dump()
    chat_dict['created_at'] = datetime.datetime.now().isoformat()
    result = await self.db.insert_one(chat_dict)
    chat_dict["_id"] = result.inserted_id
    return Chat(**chat_dict)
