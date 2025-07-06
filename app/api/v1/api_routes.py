from fastapi import APIRouter
from app.api.v1.endpoints import mock, health

api_router = APIRouter()

api_router.include_router(mock.router)
api_router.include_router(health.router)