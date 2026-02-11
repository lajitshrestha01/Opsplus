# import session from sqlachemy.orm
# import the job_event model
# create a function that take db, job id, eventtype
# create a job event rwow
"""evebt_service"""
import json
from sqlalchemy.orm import Session
from app.models.job_event import JobEvent


def append_event(db: Session, job_id: int, event_type: str, payload=None):
    payload_str = json.dumps(payload) if payload is not None else None

    job_event = JobEvent(
        job_id=job_id,
        event_type=event_type,
        payload=payload_str

    )

    db.add(job_event)
    db.flush()
    return job_event


def list_job_events(db: Session, job_id: int):
    events = db.query(JobEvent).filter(JobEvent.job_id ==
                                       job_id).order_by(JobEvent.created_at.asc()).all()
    return [
        {
            "id": e.id,
            "job_id": e.job_id,
            "event_type": e.event_type,
            "payload": e.payload_obj,
            "created_at": e.created_at
        }
        for e in events
    ]
