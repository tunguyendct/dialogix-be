from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated
import logging

from app.schemas.chat_completion import ChatCompletionRequest, ChatCompletionResponse
from app.services.ai_service import AIService
from app.services.chat import ChatService
from app.models.chat import ChatRequest
from app.api.deps import get_chat_service, get_ai_service


# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["chat"])


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


@router.post(
    "/completions",
    response_model=ChatCompletionResponse,
    summary="Generate AI Chat Completion",
    description="Generate AI assistant response for user message in conversation context"
)
async def create_chat_completion(
    request: ChatCompletionRequest,
    ai_service: Annotated[AIService, Depends(get_ai_service)]
) -> ChatCompletionResponse:
    """
    Create AI chat completion for Dialogix assistant.
    
    Args:
        request: Chat completion request with conversation_id and message
        ai_service: Injected AI service dependency
        
    Returns:
        ChatCompletionResponse with AI generated response
        
    Raises:
        HTTPException: 400 if conversation is invalid
        HTTPException: 500 if AI service fails
    """
    try:
        # Validate conversation
        is_valid_conversation = await ai_service.validate_conversation(
            request.conversation_id
        )
        
        if not is_valid_conversation:
            raise HTTPException(
                status_code=400,
                detail="Invalid conversation ID provided"
            )
        
        # Generate AI completion
        logger.info(
            f"Processing completion for conversation: {request.conversation_id}"
        )
        
        response = await ai_service.generate_completion(request)
        
        logger.info(
            f"Completion generated successfully: {response.message_id}"
        )
        
        return response
        
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        logger.error(f"Error generating completion: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error during AI completion generation"
        )