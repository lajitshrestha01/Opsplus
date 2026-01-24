# import session from sqlachemy.orm
# import the job_event model
# create a function that take db, job id, eventtype
# create a job event rwow
"""evebt_service"""
from sqlalchemy.orm import Session
from app.models.job_event import JobEvent


def append_event(db: Session, job_id: int, event_type: str):
    job_event = JobEvent(
        job_id=job_id,
        event_type=event_type,

    )

    db.add(job_event)
    db.commit()
    db.refresh(job_event)
    return job_event


