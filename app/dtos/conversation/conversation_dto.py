from typing import List, Any, Dict
from datetime import datetime
from pydantic import BaseModel
from app.dtos.base_dto import BaseDTO


class ConversationDTO(BaseModel, BaseDTO['ConversationDTO']):
    """Data Transfer Object for Conversation responses"""

    id: str
    title: str
    created_at: datetime
    messages: List[Dict[str, Any]]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConversationDTO':
        """Convert MongoDB document to ConversationDTO"""
        if not data:
            raise ValueError('Cannot convert empty data to ConversationDTO')
    
        conversation_id = data.get('_id')
        if conversation_id is None:
            raise ValueError('Conversation ID cannot be None')
        
        if hasattr(conversation_id, '__str__'):
            conversation_id = str(conversation_id)
    
        return cls(
            id=conversation_id,
            title=data.get('title', ''),
            created_at=data.get('createdAt', datetime.now()),
            messages=data.get('messages', [])
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert DTO to dictionary for API responses."""
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at.isoformat(),
            'messages': self.messages
        }