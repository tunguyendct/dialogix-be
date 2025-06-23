from fastapi import APIRouter, HTTPException, status
from app.services.chat import list_all_chats as list_all_chats_service, list_chats_by_user as list_chats_by_user_service, get_chat_by_id as get_chat_by_id_service, create_chat as create_chat_service
from app.models.chat import ChatRequest

router = APIRouter()

@router.get('/', status_code=status.HTTP_200_OK)
async def list_all_chats():
  return await list_all_chats_service()

@router.get('/user/{user_id}', status_code=status.HTTP_200_OK)
async def list_chats_by_user(user_id: str):
  if not user_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID is required")
  if len(user_id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID must be at least 1 character long")
  return await list_chats_by_user_service(user_id)

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_chat_by_id(id: str):
  if not id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID is required")
  if len(id) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID must be at least 1 character long")

  chat = get_chat_by_id_service(id)
  if not chat:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found")
  return await get_chat_by_id_service(id)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_chat(chat: ChatRequest):
  if not chat.user_id:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID is required")
  if len(str(chat.user_id)) < 1:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User ID must be at least 1 character long")

  return await create_chat_service(chat)