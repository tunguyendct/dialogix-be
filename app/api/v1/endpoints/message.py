from fastapi import APIRouter
from app.services.message import list_all_messages as list_all_messages_service, list_messages_by_chat_id as list_messages_by_chat_id_service, get_message_by_id as get_message_by_id_service
from app.models.message import Message

router = APIRouter()

@router.get('/')
def list_all_messages():
  return list_all_messages_service()

@router.get('/chat/{chat_id}') 
def list_messages_by_chat_id(chat_id: Message['chat_id']):
  return list_messages_by_chat_id_service(chat_id)

@router.get('/{id}')
def get_message_by_id(id: Message['_id']):
  return get_message_by_id_service(id)