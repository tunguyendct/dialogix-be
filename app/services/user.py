from typing import List
from database.mongo import user_collection
from app.models.user import User

async def list_all_users() -> List[User]:
  return await user_collection.find().to_list(100) # type: ignore

async def get_user_by_id(id: User['_id']) -> User | None:
  return await user_collection.find_one({'_id': id}) # type: ignore