from fastapi import FastAPI
from src.api.routes import router
from storage.db import engine
from storage.models import Base

app = FastAPI(title="Weather AI API")

Base.metadata.create_all(bind=engine)

app.include_router(router)