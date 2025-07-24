import datetime
from typing import List
from app.dtos.conversation.conversation_dto import ConversationDTO


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
    

    async def create_conversation(self, conversation_id: str, title: str, messages: List = []) -> ConversationDTO:
        conversation_data = {
            '_id': conversation_id,
            'title': title,
            'createdAt': datetime.datetime.now(), 
            'messages': messages
        }
        
        # Insert the document into database
        await self.db.insert_one(conversation_data)
        
        # Retrieve the inserted document to ensure we have the complete data
        inserted_conversation = await self.db.find_one({'_id': conversation_id})
        
        if not inserted_conversation:
            raise RuntimeError(f"Failed to retrieve inserted conversation: {conversation_id}")
        
        return ConversationDTO.from_dict(inserted_conversation)


    async def get_conversation_by_id(self, conversation_id: str) -> ConversationDTO | None:
        conversation = await self.db.find_one({'_id': conversation_id})
        
        if not conversation:
            return None

        return ConversationDTO.from_dict(conversation)
    
    
    async def add_messages_to_conversation(
        self, 
        conversation_id: str, 
        messages: List[dict]
    ) -> ConversationDTO:
        """
        Add multiple messages to an existing conversation.

        Args:
            conversation_id: Conversation session identifier
            messages: List of message content to add

        Returns:
            Updated ConversationDTO with new messages
        """
        await self.db.update_one(
            {'_id': conversation_id},
            {'$push': {'messages': {'$each': messages}}}
        )

        updated_conversation = await self.get_conversation_by_id(conversation_id)
        if updated_conversation is None:
            raise ValueError(f"Conversation with ID {conversation_id} not found after update")
        
        return updated_conversation