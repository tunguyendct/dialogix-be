from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId
from app.models.base import PyObjectId

class UserRequest(BaseModel):
  email: str
  name: str
  password: str


class UserResponse(BaseModel):
  email: str
  name: str
  created_at: Optional[str] = None


class User(BaseModel):
  id: Optional[PyObjectId] = Field(alias='_id')
  email: str
  name: str
  password: str
  created_at: Optional[str] = None