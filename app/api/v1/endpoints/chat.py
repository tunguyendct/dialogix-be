from fastapi import APIRouter, HTTPException, status, Depends
from app.services.chat import ChatService
from app.models.chat import ChatRequest
from app.api.deps import get_chat_service


router = APIRouter()


@router.get('/user/{user_id}', status_code=status.HTTP_200_OK)
async def list_chats_by_user(user_id: str, chat_service: ChatService = Depends(get_chat_service)):
  if not user_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID is required")
  if len(user_id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID must be at least 1 character long")
  return await chat_service.list_chats_by_user(user_id)


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_chat_by_id(id: str, chat_service: ChatService = Depends(get_chat_service)):
  if not id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID is required")
  if len(id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID must be at least 1 character long")

  chat = chat_service.get_chat_by_id(id)
  if not chat:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
  return await chat_service.get_chat_by_id(id)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_chat(chat: ChatRequest, chat_service: ChatService = Depends(get_chat_service)):
  if not chat.user_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID is required")
  if len(str(chat.user_id)) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID must be at least 1 character long")

  return await chat_service.create_chat(chat)