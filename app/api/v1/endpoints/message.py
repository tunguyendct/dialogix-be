from fastapi import APIRouter, HTTPException, status, Depends
from app.services.message import MessageService
from app.models.message import Message, MessageRequest
from app.api.deps import get_message_service


router = APIRouter(prefix='/message', tags=['message'])


# @router.get('/chat/{chat_id}', status_code=status.HTTP_200_OK) 
# async def list_messages_by_chat_id(chat_id: str, message_service: MessageService = Depends(get_message_service)):
#   if not chat_id:
#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID is required")
#   if len(chat_id) < 1:
#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Chat ID must be at least 1 character long")

#   return await message_service.list_messages_by_chat_id(chat_id)



# @router.post(
#     "/",
#     response_model=ChatCompletionResponse,
# )
# async def create_chat_completion(
#     request: ChatCompletionRequest,
#     ai_service: Annotated[AIService, Depends(get_ai_service)],
#     conversation_service: ConversationService = Depends(get_conversation_service)
# ) -> ChatCompletionResponse:
#     """
#     Create AI chat completion for Dialogix assistant.
    
#     Args:
#         request: Chat completion request with conversation_id and message
#         ai_service: Injected AI service dependency
        
#     Returns:
#         ChatCompletionResponse with AI generated response
        
#     Raises:
#         HTTPException: 400 if conversation is invalid
#         HTTPException: 500 if AI service fails
#     """
#     try:
#         # Validate conversation
#         is_valid_conversation = await conversation_service.validate_conversation(
#             request.conversation_id
#         )
        
#         if not is_valid_conversation:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Invalid conversation ID provided"
#             )
        
#         # Generate AI completion
#         logger.info(
#             f"Processing completion for conversation: {request.conversation_id}"
#         )
        
#         conversation = ''

#         response = await ai_service.generate_completion(request)
        
#         logger.info(
#             f"Completion generated successfully: {response.message_id}"
#         )
        
#         return response
        
#     except HTTPException:
#         # Re-raise HTTP exceptions
#         raise
#     except Exception as e:
#         logger.error(f"Error generating completion: {str(e)}")
#         raise HTTPException(
#             status_code=500,
#             detail="Internal server error during AI completion generation"
#         )
