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
    db.commit()
    db.refresh(job)
    append_event(db, job.id, "job.created")
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

    db.commit()
    db.refresh(job)
    append_event(db, job.id, "job.started")
    return job
