from fastapi import APIRouter
from app.api.v1.endpoints import chat, user, message

router = APIRouter()

router.include_router(chat.router, prefix='/chats', tags=['Chats'])
router.include_router(user.router, prefix='/users', tags=['Users'])
router.include_router(message.router, prefix='/messages', tags=['Messages'])