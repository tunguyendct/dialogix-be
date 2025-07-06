from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings and configuration for Dialogix Backend API."""
    
    # Environment Configuration
    ENVIRONMENT: str = "development"
    PORT: int = 5001
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Dialogix Backend API"
    VERSION: str = "1.0.0"
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:5000",
        "http://127.0.0.1:5000"
    ]
    
    # Database Configuration
    MONGO_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "Dialogix"
    
    # Collection Names
    USER_COLLECTION: str = "User"
    CHAT_COLLECTION: str = "Chat"
    MESSAGE_COLLECTION: str = "Message"
    
    # Security Configuration
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        # Allow extra fields from environment variables
        extra = "ignore"

settings = Settings()