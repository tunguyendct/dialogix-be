from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone
from app.models.message import Message


class ConversationRequest(BaseModel):
    """Schema for chat completion request payload."""
    conversation_id: str = Field(
        description="Unique identifier for the conversation session",
        examples=["session-1704459600000"]
    )
    message: str = Field(
        ..., 
        min_length=1, 
        max_length=4000,
        description="User message content",
        examples=["Hi"]
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Message timestamp"
    )

class ConversationResponse(BaseModel):
    """Schema for chat completion response."""
    message: str = Field(
        ..., 
        description="AI assistant response message",
        examples=["Hello! I'm doing well, thank you for asking. How can I help you today?"]
    )
    message_id: str = Field(
        ..., 
        description="Unique identifier for the response message",
        examples=["msg-1704459601000"]
    )
    conversation_id: str = Field(
        ..., 
        description="Conversation session identifier",
        examples=["session-1704459600000"]
    )
    timestamp: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Message timestamp"
    )


class Conversation(BaseModel):
    conversation_id: str
    title: str
    created_at: datetime = Field(default_factory=datetime.now)
    messages: List[Message]