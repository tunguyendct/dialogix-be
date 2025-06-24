from typing import List
from database.mongo import user_collection
from app.models.user import User, UserRequest, UserResponse
import datetime

async def list_all_users() -> List[UserResponse]:
  return user_collection.find().to_list(100)

async def get_user_by_id(id: str) -> UserResponse | None:
  return user_collection.find_one({'_id': id})

async def create_user(user: UserRequest) -> UserResponse:
  user_dict = user.model_dump()
  user_dict['created_at'] = datetime.datetime.now().isoformat()
  result = user_collection.insert_one(user_dict)
  user_dict["_id"] = result.inserted_id
  return UserResponse(**user_dict) 
