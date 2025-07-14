from app.models.conversation import Conversation
import datetime
from typing import List


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
    

    async def create_conversation(self, conversation_id: str, title: str, messages: List = []) -> Conversation:
        conversation = await self.db.insert_one({
            '_id': conversation_id,
            'title': title,
            'createdAt': datetime.datetime.now(), 
            'messages': messages
        })

        return conversation


    async def get_conversation_by_id(self, conversation_id: str) -> Conversation | None:
        conversation = await self.db.find_one({'_id': conversation_id})
        return conversation