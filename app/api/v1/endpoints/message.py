from fastapi import APIRouter, HTTPException, status
from app.services.message import list_all_messages as list_all_messages_service, list_messages_by_chat_id as list_messages_by_chat_id_service, get_message_by_id as get_message_by_id_service, create_message as create_message_service
from app.models.message import MessageRequest

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
async def list_all_messages():
  return await list_all_messages_service()

@router.get('/chat/{chat_id}', status_code=status.HTTP_200_OK) 
async def list_messages_by_chat_id(chat_id: str):
  if not chat_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID is required")
  if len(chat_id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID must be at least 1 character long")

  return await list_messages_by_chat_id_service(chat_id)

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_message_by_id(id: str):
  if not id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message ID is required")
  if len(id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message ID must be at least 1 character long")

  message = get_message_by_id_service(id)
  if not message:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
  return await get_message_by_id_service(id)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_message(message: MessageRequest):
  if not message.chat_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID is required")
  if len(str(message.chat_id)) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID must be at least 1 character long")

  return await create_message_service(message)