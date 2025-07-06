from fastapi import APIRouter
from pydantic import BaseModel
from typing import Literal
from datetime import datetime
from app.core.config import settings

router = APIRouter(prefix="/health", tags=["health"])

class HealthResponse(BaseModel):
    """Health check response schema for Dialogix API."""
    status: Literal["online", "offline"]
    timestamp: datetime
    service: str
    version: str

@router.get("/", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Health check endpoint to verify Dialogix server status.
    Returns server status and basic information.
    """
    return HealthResponse(
        status="online",
        timestamp=datetime.utcnow(),
        service=settings.PROJECT_NAME,
        version=settings.VERSION
    )