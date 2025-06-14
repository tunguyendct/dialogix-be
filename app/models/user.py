from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class User(BaseModel):
  id: Optional[ObjectId] = Field(alias='_id')
  email: str
  name: str
  password_hash: str
  created_at: Optional[str]