from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from app.models.base import PyObjectId

class User(BaseModel):
  id: Optional[PyObjectId] = Field(alias='_id')
  email: str
  name: str
  password_hash: str
  created_at: Optional[str] = None