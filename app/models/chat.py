from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from app.models.base import PyObjectId

class Chat(BaseModel):
  id: Optional[PyObjectId] = Field(alias='_id')
  user_id: str
  title: str = "New Chat"
  created_at: Optional[str] = None
  updated_at: Optional[str] = None

  class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}