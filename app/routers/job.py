"""job router"""
from fastapi import APIRouter, HTTPException, status, Path, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.job import JobCreate, JobRead
from app.services.job_service import create_job, get_job, start_job
from app.core.error import NotFoundError, InvalidStateError

router = APIRouter(prefix="/jobs", tags=["jobs"])
@router.post("/", response_model=JobRead, status_code=status.HTTP_201_CREATED)
def create_job_endpoint(job_in: JobCreate, db: Session = Depends(get_db)):
    job = create_job(db, job_in)
    return job 

@router.get("/{job_id}", response_model=JobRead)
def get_job_endpoint(job_id: int = Path(...,gt=0), db: Session = Depends(get_db)):
    job = get_job(db,job_id)
    if not job: 
        raise HTTPException(status_code=404, detail="job not found")
    return job

@router.post("/{job_id}/start", response_model=JobRead)
def start_job_endpoint(job_id: int, db: Session = Depends(get_db)):
    try: 
        job = start_job(db, job_id)
        return job 
    except NotFoundError: 
        raise HTTPException(404)
    except InvalidStateError: 
        raise HTTPException(409)