"""job service"""
import json
from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate
from app.core.error import NotFoundError, InvalidStateError
from app.services.event_service import append_event


def create_job(db: Session, job_in: JobCreate):
    payload_str = json.dumps(job_in.payload)
    job = Job(
        job_type=job_in.job_type,
        payload=payload_str,
        status="queued"

    )

    db.add(job)
    db.flush()
    append_event(db, job.id, "job.created", payload={"actor":"api"})
    db.commit()
    db.refresh(job)
    return job


def get_job(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()


def start_job(db: Session, job_id: int):
    job = db.query(Job).filter(Job.id == job_id).first()
    if job is None:
        raise NotFoundError()
    if job.status != 'queued':
        raise InvalidStateError()
    job.status = 'running'

    db.flush()
    append_event(db, job.id, "job.started",payload={"actor":"api"})
    db.commit()
    db.refresh(job)

    return job

def succeed_job(db: Session, job_id: int): 
    job = db.query(Job).filter(Job.id == job_id).first()
    if job is None: 
        raise NotFoundError()
    if job.status != "running": 
        raise InvalidStateError()
    job.status = "succeeded"
    db.flush()
    append_event(db, job.id, "job.succeeded",payload={"actor":"api"})
    db.commit()
    db.refresh(job)
    return job 

def fail_job(db: Session, job_id: int ): 
    job = db.query(Job).filter(Job.id == job_id).first()
    if job is None: 
        raise NotFoundError()
    if job.status != "running": 
        raise InvalidStateError()
    job.status = "failed"
    db.flush()
    append_event(db, job.id, "job.failed",payload={"actor":"api"})
    db.commit()
    db.refresh(job)
    return job
    

