from fastapi import FastAPI
from app.api.v1.api_routes import router

app = FastAPI()

app.include_router(router, prefix='/api/v1', tags=['v1'])