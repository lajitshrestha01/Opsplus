from fastapi import APIRouter
from app.routers.health import router as health_router
from app.routers.job import router as job_router
#create top level api
api_router = APIRouter(prefix="/api/v1")

#include sub-router
api_router.include_router(health_router)
api_router.include_router(job_router)
