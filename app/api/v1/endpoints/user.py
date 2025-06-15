from fastapi import APIRouter
from app.services.user import list_all_users as list_all_users_service, get_user_by_id as get_user_by_id_service

router = APIRouter()

@router.get('/')
async def list_users():
  return list_all_users_service()
  
@router.get('/{id}')
async def get_user_by_id(id: str):
  return get_user_by_id_service(id)