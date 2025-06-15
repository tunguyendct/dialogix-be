from fastapi import APIRouter
from app.services.chat import list_all_chats as list_all_chats_service, list_chats_by_user as list_chats_by_user_service, get_chat_by_id as get_chat_by_id_service

router = APIRouter()

@router.get('/')
def list_all_chats():
  return list_all_chats_service()

@router.get('/user/{user_id}')
def list_chats_by_user(user_id: str):
  return list_chats_by_user_service(user_id)

@router.get('/{id}')
def get_chat_by_id(id: str):
  return get_chat_by_id_service(id)