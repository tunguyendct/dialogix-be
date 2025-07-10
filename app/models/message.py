from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class Role(str, Enum):
  USER = 'user'
  ASSISTANT = 'assistant'


class MessageRequest(BaseModel):
  role: Role
  content: str


class Message(BaseModel):
  message_id: str 
  role: Role 
  content: str
  created_at: datetime = Field(default_factory=datetime.now)