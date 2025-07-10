from app.models.conversation import Conversation
import datetime


class ConversationService:
    def __init__(self, db):
        self.db = db

    async def validate_conversation(self, conversation_id: str) -> bool:
        """
        Validate if conversation exists and is accessible.
        
        Args:
            conversation_id: Conversation session identifier
            
        Returns:
            Boolean indicating if conversation is valid
        """
        # For now, accept all conversation IDs
        # In production, validate against database
        return len(conversation_id) > 0
    

    async def create_conversation(self, conversation_id: str, title: str) -> Conversation:
        conversation = await self.db.insert_one({
            'conversation_id': conversation_id,
            'title': title,
            'created_at': datetime.datetime.now(), 
            'messages': []
        })

        return conversation


    async def get_conversation_by_id(self, conversation_id: str) -> Conversation | None:
        conversation = await self.db.find_one({'conversation_id': conversation_id})
        return conversation