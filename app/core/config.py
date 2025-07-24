from typing import List
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Dialogix Backend API Configuration Settings.
    
    Centralized configuration management following clean architecture principles.
    All environment variables are properly typed and validated.
    """
    
    # Environment Configuration
    ENVIRONMENT: str = Field(default="development", description="Application environment")
    PORT: int = Field(default=8000, description="Server port")
    DEBUG: bool = Field(default=True, description="Debug mode flag")
    
    # API Configuration  
    API_V1_STR: str = Field(default="/api/v1", description="API v1 prefix")
    PROJECT_NAME: str = Field(default="Dialogix Backend API", description="Project name")
    VERSION: str = Field(default="1.0.0", description="API version")
    DESCRIPTION: str = Field(default="AI Assistant Chat Backend API", description="API description")
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: List[str] = Field(
        default=[
            "http://localhost:5000",
            "http://127.0.0.1:5000"
        ],
        description="Allowed CORS origins"
    )
    
    # Database Configuration
    MONGO_URL: str = Field(default="mongodb://localhost:27017", description="MongoDB connection URL")
    DATABASE_NAME: str = Field(default="Dialogix", description="Database name")
    
    # Collection Names
    USER_COLLECTION: str = Field(default="users", description="User collection name")
    CHAT_COLLECTION: str = Field(default="chats", description="Chat collection name") 
    MESSAGE_COLLECTION: str = Field(default="messages", description="Message collection name")
    
    # Security Configuration
    SECRET_KEY: str = Field(default="your-secret-key-change-in-production", description="JWT secret key")
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="Token expiration time")
    
    # AI Configuration
    AI_MODEL_NAME: str = Field(default="dialogix-model", description="AI model identifier")
    MAX_MESSAGE_LENGTH: int = Field(default=4000, description="Maximum message length")
    DEFAULT_RESPONSE_TIMEOUT: int = Field(default=30, description="AI response timeout")
    AI_TEMPERATURE: float = Field(default=0.7, description="AI response creativity")
    
    # Logging Configuration
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    LOG_FORMAT: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log format string"
    )
    
    @field_validator("ENVIRONMENT")
    def validate_environment(cls, v: str) -> str:
        """Validate environment setting."""
        allowed_envs = ["development", "production", "testing"]
        if v not in allowed_envs:
            raise ValueError(f"Environment must be one of: {allowed_envs}")
        return v

    @field_validator("PORT")
    def validate_port(cls, v: int) -> int:
        """Validate port number."""
        if not (1 <= v <= 65535):
            raise ValueError("Port must be between 1 and 65535")
        return v
    
    @field_validator("MAX_MESSAGE_LENGTH")
    def validate_message_length(cls, v: int) -> int:
        """Validate maximum message length."""
        if v <= 0:
            raise ValueError("Maximum message length must be positive")
        return v

    @field_validator("AI_TEMPERATURE")
    def validate_temperature(cls, v: float) -> float:
        """Validate AI temperature setting."""
        if not (0.0 <= v <= 2.0):
            raise ValueError("AI temperature must be between 0.0 and 2.0")
        return v
    
    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.ENVIRONMENT == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.ENVIRONMENT == "production"
    
    @property
    def database_url(self) -> str:
        """Get formatted database URL."""
        return self.MONGO_URL
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        # Allow extra fields from environment to prevent validation errors
        extra = "ignore"


# Global settings instance
settings = Settings()