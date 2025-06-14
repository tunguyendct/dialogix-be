from pydantic import BaseModel, Field
from typing import Literal, Optional
from bson import ObjectId

class Message(BaseModel):
  id: Optional[ObjectId] = Field(alias='_id')
  chat_id: ObjectId # Foreign key to Chat._id
  role: Literal['user', 'assistant', 'system']
  content: str
  created_at: Optional[str]
  token_usage: Optional[int] = 0
  feedback: Optional[Literal['like', 'dislike']] = None

  class Config:
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}
