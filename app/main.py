"""main file """
from fastapi import FastAPI
from app.routers.api_router import api_router
from contextlib import asynccontextmanager
from app.db.intit_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield

app = FastAPI(title="opsPulse")

app.include_router(api_router)

