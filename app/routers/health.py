from fastapi import APIRouter

router = APIRouter(prefix="/health")

@router.get("/")
def checkfunction():
    return {'status' : 'ok'}
