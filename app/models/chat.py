from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Chat(BaseModel):
  id: Optional[ObjectId] = Field(alias='_id')
  user_id: str
  title: str = "New Chat"
  created_at: Optional[str]
  updated_at: Optional[str]

  class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}