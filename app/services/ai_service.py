import asyncio
from typing import List, Dict, Any
from datetime import datetime, timezone
from app.models.conversation import ConversationRequest, ConversationResponse
from app.core.openapi_client import AzureOpenAIClient
from app.prompts.system_prompt import assistant_prompt

class AIService:
    """Service layer for AI completion operations."""
    
    def __init__(self, client: AzureOpenAIClient):
        self.client = client

        # Mock AI responses for demonstration
        self._mock_responses = [
            "Hello! I'm doing well, thank you for asking. How can I help you today?",
            "That's an interesting question! Let me think about that.",
            "I'd be happy to help you with that. Can you provide more details?",
            "Based on what you've told me, here's what I think...",
            "That's a great point! Here's my perspective on this topic.",
        ]
    
    async def generate_completion(
        self, 
        request: ConversationRequest,
        conversation_history: List[Dict[str, Any]]
    ) -> ConversationResponse:
        """
        Generate AI completion response for user message.
        
        Args:
            request: Conversation request with conversation_id and message
            
        Returns:
            ChatCompletionResponse with AI generated response
        """
        # Simulate AI processing time
        await asyncio.sleep(0.5)

        messages = []
        user_message = {
            'role': 'user',
            'content': request.message
        }

        if not conversation_history:
            messages = [
                {
                    'role': 'system',
                    'content': assistant_prompt
                }
            ]
        else:
            messages = [{'role': msg['role'], 'content': msg['content']} for msg in conversation_history]

        messages.append(user_message)
        
        # Generate response based on user input
        ai_response = self.client.generate_message_with_conversation(messages)
        
        # Generate unique message ID
        message_id = self._generate_message_id()
        
        return ConversationResponse(
            message=ai_response,
            message_id=message_id,
            conversation_id=request.conversation_id,
            timestamp=datetime.now()
        )
    
    def _generate_message_id(self) -> str:
        """Generate unique message identifier."""
        timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)
        return f"msg-{timestamp}"
    