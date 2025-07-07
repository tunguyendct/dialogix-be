import logging
import os
import uvicorn
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.api.v1.api_routes import api_router
from app.core.config import settings

# Load environment variables
load_dotenv()

def setup_logging() -> None:
    """Configure application logging based on settings."""
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper()),
        format=settings.LOG_FORMAT,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("logs/dialogix.log") if settings.is_production else logging.NullHandler()
        ]
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager for startup and shutdown events.
    
    Handles initialization and cleanup of resources following
    clean architecture principles.
    """
    # Startup
    logger = logging.getLogger(__name__)
    logger.info(f"Starting Dialogix Backend API v{settings.VERSION}")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Database: {settings.DATABASE_NAME}")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Dialogix Backend API")


def create_application() -> FastAPI:
    """
    Create and configure Dialogix FastAPI application.
    
    Implements dependency injection and middleware configuration
    following SOLID principles.
    
    Returns:
        FastAPI: Configured application instance
    """
    # Setup logging first
    setup_logging()
    
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url=f"{settings.API_V1_STR}/docs" if settings.is_development else None,
        redoc_url=f"{settings.API_V1_STR}/redoc" if settings.is_development else None,
        lifespan=lifespan
    )
    
    # Security middleware
    if settings.is_production:
        app.add_middleware(
            TrustedHostMiddleware, 
            allowed_hosts=["dialogix.com", "*.dialogix.com"]
        )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
        allow_headers=["*"],
    )
    
    # Include API routes
    app.include_router(api_router, prefix=settings.API_V1_STR)
    
    @app.get("/", tags=["root"])
    async def root() -> dict[str, str]:
        """
        Root endpoint for Dialogix API.
        
        Returns:
            dict: API information and navigation links
        """
        return {
            "message": f"Welcome to {settings.PROJECT_NAME}",
            "version": settings.VERSION,
            "environment": settings.ENVIRONMENT,
            "docs": f"{settings.API_V1_STR}/docs" if settings.is_development else "Documentation disabled in production",
            "health": f"{settings.API_V1_STR}/health"
        }
    
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        """
        Global exception handler for unhandled exceptions.
        
        Args:
            request: FastAPI request object
            exc: Exception that occurred
            
        Returns:
            JSONResponse: Standardized error response
        """
        logger = logging.getLogger(__name__)
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        
        if settings.is_development:
            return JSONResponse(
                status_code=500,
                content={
                    "error": "Internal server error",
                    "detail": str(exc),
                    "type": type(exc).__name__
                }
            )
        else:
            return JSONResponse(
                status_code=500,
                content={"error": "Internal server error"}
            )
    
    return app


# Create application instance
app = create_application()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=settings.PORT,
        reload=settings.is_development,
        log_level=settings.LOG_LEVEL.lower(),
        access_log=settings.is_development
    )