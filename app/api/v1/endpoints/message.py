from fastapi import APIRouter, HTTPException, status, Depends
from app.services.message import MessageService
from app.models.message import Message, MessageRequest
from app.api.deps import get_message_service


router = APIRouter()


@router.get('/chat/{chat_id}', status_code=status.HTTP_200_OK) 
async def list_messages_by_chat_id(chat_id: str, message_service: MessageService = Depends(get_message_service)):
  if not chat_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID is required")
  if len(chat_id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID must be at least 1 character long")

  return await message_service.list_messages_by_chat_id(chat_id)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_message(message: MessageRequest, message_service: MessageService = Depends(get_message_service)) -> Message | None:
  if not message.chat_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID is required")
  if len(str(message.chat_id)) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID must be at least 1 character long")
  
  return await message_service.create_message_and_reply(message)