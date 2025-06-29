from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from app.models.base import PyObjectId


class ChatRequest(BaseModel):
  user_id: PyObjectId 
  title: str = "New Chat"


class Chat(BaseModel):
  id: Optional[PyObjectId] = Field(alias='_id', default=None)
  user_id: PyObjectId 
  title: str = "New Chat"
  created_at: Optional[str] = None

  model_config = ConfigDict(
    populate_by_name=True
  )
    