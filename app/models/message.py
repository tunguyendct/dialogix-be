from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from enum import Enum
from app.models.base import PyObjectId 


class Role(str, Enum):
  USER = 'user'
  ASSISTANT = 'assistant'


class MessageRequest(BaseModel):
  chat_id: PyObjectId # Foreign key to Chat._id
  role: Role
  content: str


class Message(BaseModel):
  id: Optional[PyObjectId] = Field(alias='_id')
  chat_id: PyObjectId # Foreign key to Chat._id
  role: Role 
  content: str
  created_at: datetime = Field(default_factory=datetime.now)

  model_config = ConfigDict(
    populate_by_name=True,
    arbitrary_types_allowed=True,
    json_encoders={datetime: lambda dt: dt.isoformat()}
  )

  def __getitem__(self, key):
    return getattr(self, key)
  