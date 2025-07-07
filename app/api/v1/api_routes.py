from fastapi import APIRouter
from app.api.v1.endpoints import mock, health, chat

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(health.router)
api_router.include_router(mock.router)
api_router.include_router(chat.router)