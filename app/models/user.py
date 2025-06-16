from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from app.models.base import PyObjectId

class UserRequest(BaseModel):
  email: str
  name: str
  password: str

class User(BaseModel):
  id: Optional[PyObjectId] = Field(alias='_id')
  email: str
  name: str
  password: str
  created_at: Optional[str] = None