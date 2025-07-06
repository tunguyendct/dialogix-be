import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api_routes import api_router
from app.core.config import settings

# Load environment variables
load_dotenv()

def create_application() -> FastAPI:
    """Create and configure the Dialogix FastAPI application."""
    
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="AI Assistant Chat Backend API",
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url=f"{settings.API_V1_STR}/docs",
        redoc_url=f"{settings.API_V1_STR}/redoc"
    )
    
    # Configure CORS middleware for frontend integration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
        allow_headers=["*"],
    )
    
    # Include API routes
    app.include_router(api_router, prefix=settings.API_V1_STR)
    
    @app.get("/")
    async def root() -> dict[str, str]:
        """Root endpoint for Dialogix API."""
        return {
            "message": "Welcome to Dialogix Backend API",
            "version": settings.VERSION,
            "docs": f"{settings.API_V1_STR}/docs"
        }
    
    return app

# Create the FastAPI application instance
app = create_application()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=settings.PORT,
        reload=(settings.ENVIRONMENT == "development"),
        log_level="info"
    )