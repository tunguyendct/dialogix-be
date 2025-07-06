from database.mongo import db
from app.core.openapi_client import AzureOpenAIClient
from app.services.chat import ChatService
from app.services.message import MessageService
from app.services.user import UserService


openai_client = AzureOpenAIClient()


def get_chat_service() -> ChatService:
  return ChatService(db=db.get_chat_collection())


def get_message_service() -> MessageService:
  return MessageService(db=db.get_message_collection(), client=openai_client)


def get_user_service() -> UserService:
  return UserService(db=db.get_user_collection())