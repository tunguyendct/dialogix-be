from pydantic import BaseModel, Field


class ConversationRequest(BaseModel):
    conversation_id: str = Field(
        description="Unique identifier for the conversation session",
        examples=["session-1704459600000"]
    )


class ConversationResponse(BaseModel):
    conversation_id: str = Field(
        description="Unique identifier for the conversation session",
        examples=["session-1704459600000"]
    )
