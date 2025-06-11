from fastapi import APIRouter
from app.services.user import list_all_users

router = APIRouter(prefix='/users', tags=['users'])

@router.get('/')
async def list_users():
  return list_all_users()