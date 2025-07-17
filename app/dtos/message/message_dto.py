from app.models.message import Role

class MessageDTO:
    message_id: str
    role: Role
    content: str
    created_at: str