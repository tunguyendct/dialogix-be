from fastapi import APIRouter
from typing import List

router = APIRouter(prefix="/mock", tags=["mock"])

@router.get("/user", response_model=dict)
def get_mock_user() -> dict:
    """Return a mock user object."""
    return {
        "id": 1,
        "username": "mockuser",
        "email": "mockuser@example.com",
        "full_name": "Mock User"
    }

@router.get("/chat", response_model=List[dict])
def get_mock_chats() -> List[dict]:
    """Return a list of mock chat objects."""
    return [
        {
            "id": 1,
            "title": "Mock Chat Room",
            "participants": [
                {"id": 1, "username": "mockuser"},
                {"id": 2, "username": "anotheruser"}
            ]
        },
        {
            "id": 2,
            "title": "Project Discussion",
            "participants": [
                {"id": 1, "username": "mockuser"},
                {"id": 3, "username": "thirduser"}
            ]
        }
    ]

@router.get("/message", response_model=List[dict])
def get_mock_messages() -> List[dict]:
    """Return a list of mock message objects."""
    return [
        {
            "id": 1,
            "chat_id": 1,
            "sender_id": 1,
            "content": "Hello, this is a mock message!",
            "timestamp": "2025-07-05T12:00:00Z"
        },
        {
            "id": 2,
            "chat_id": 1,
            "sender_id": 2,
            "content": "Hi! Welcome to the chat room.",
            "timestamp": "2025-07-05T12:01:00Z"
        },
        {
            "id": 3,
            "chat_id": 2,
            "sender_id": 3,
            "content": "Let's discuss the project requirements.",
            "timestamp": "2025-07-05T12:05:00Z"
        }
    ]
