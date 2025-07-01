from bson import ObjectId
from typing import List
from app.models.user import UserRequest, UserResponse
import datetime


class UserService:
  def __init__(self, db):
    self.db = db

  async def list_all_users(self) -> List[UserResponse]:
    return self.db.find().to_list(100)

  async def get_user_by_id(self, id: str) -> UserResponse | None:
    return self.db.find_one({'_id': ObjectId(id)})

  async def create_user(self, user: UserRequest) -> UserResponse:
    user_dict = user.model_dump()
    user_dict['created_at'] = datetime.datetime.now().isoformat()
    result = await self.db.insert_one(user_dict)
    user_dict["_id"] = result.inserted_id
    return UserResponse(**user_dict) 