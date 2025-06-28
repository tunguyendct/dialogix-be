from pydantic import BaseModel, Field
from typing import Literal, Optional
from bson import ObjectId
from app.models.base import PyObjectId 


class MessageRequest(BaseModel):
  chat_id: PyObjectId # Foreign key to Chat._id
  role: Literal['user', 'assistant', 'system']
  content: str
  token_usage: Optional[int] = 0
  feedback: Optional[Literal['like', 'dislike']] = None


class Message(BaseModel):
  id: Optional[PyObjectId] = Field(alias='_id')
  chat_id: PyObjectId # Foreign key to Chat._id
  role: Literal['user', 'assistant', 'system']
  content: str
  created_at: Optional[str] = None
  token_usage: Optional[int] = 0
  feedback: Optional[Literal['like', 'dislike']] = None

  class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
