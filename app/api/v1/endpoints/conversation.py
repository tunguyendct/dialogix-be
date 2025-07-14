from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
import logging
from app.models.conversation import ConversationRequest, ConversationResponse, Conversation
from app.services.conversation import ConversationService
from app.services.ai_service import AIService
from app.api.deps import get_ai_service, get_conversation_service


router = APIRouter(prefix='/conversation', tags=['conversation'])

# Configure logging
logger = logging.getLogger(__name__)


@router.get('/{conversation_id}', status_code=status.HTTP_200_OK)
async def get_conversation(
    conversation_id: str,
    conversation_service: ConversationService = Depends(get_conversation_service)
) -> Conversation:
    try:
        # Validate conversation
        is_valid_conversation = await conversation_service.validate_conversation(
            conversation_id
        )
        
        if not is_valid_conversation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid conversation ID provided"
            )
        
        # Generate AI completion
        logger.info(
            f"Processing completion for conversation: {conversation_id}"
        )

        conversation = await conversation_service.get_conversation_by_id(conversation_id=conversation_id)
        
        if conversation is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Conversation not found'
            )

        return conversation

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieve conversation: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


@router.post(
    "/message",
    response_model=ConversationRequest,
    status_code=status.HTTP_200_OK
)
async def create_conversation_message(
    request: ConversationRequest,
    ai_service: Annotated[AIService, Depends(get_ai_service)],
    conversation_service: ConversationService = Depends(get_conversation_service)
) -> ConversationResponse:
    """
    Create AI conversation for Dialogix assistant.
    
    Args:
        request: Conversation request with conversation_id and message
        ai_service: Injected AI service dependency
        
    Returns:
        ConversationResponse with AI generated response
        
    Raises:
        HTTPException: 400 if conversation is invalid
        HTTPException: 500 if AI service fails
    """
    try:
        # Validate conversation
        is_valid_conversation = await conversation_service.validate_conversation(
            request.conversation_id
        )
        
        if not is_valid_conversation:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid conversation ID provided"
            )
        
        # Generate AI completion
        logger.info(
            f"Processing completion for conversation: {request.conversation_id}"
        )
        
        conversation = await conversation_service.get_conversation_by_id(conversation_id=request.conversation_id)

        if conversation is None:
            conversation = await conversation_service.create_conversation(conversation_id=request.conversation_id, title='Title')
        
        conversation_history = conversation.messages

        response = await ai_service.generate_completion(request, conversation_history)
        
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
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during AI completion generation"
        )