from fastapi import FastAPI
from app.api.v1.api_routes import api_router

app = FastAPI()

app.include_router(api_router, prefix='/api/v1', tags=['v1'])