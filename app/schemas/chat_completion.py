from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime

class ChatCompletionRequest(BaseModel):
    """Schema for chat completion request payload."""
    conversation_id: str = Field(
        description="Unique identifier for the conversation session",
        example="session-1704459600000"
    )
    message: str = Field(
        ..., 
        min_length=1, 
        max_length=4000,
        description="User message content",
        example="Hi"
    )

class ChatCompletionResponse(BaseModel):
    """Schema for chat completion response."""
    message: str = Field(
        ..., 
        description="AI assistant response message",
        example="Hello! I'm doing well, thank you for asking. How can I help you today?"
    )
    message_id: str = Field(
        ..., 
        description="Unique identifier for the response message",
        example="msg-1704459601000"
    )
    conversation_id: str = Field(
        ..., 
        description="Conversation session identifier",
        example="session-1704459600000"
    )
    timestamp: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        description="Message timestamp"
    )