from fastapi import APIRouter
from app.api.v1.endpoints import health, conversation

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(health.router)
api_router.include_router(conversation.router)