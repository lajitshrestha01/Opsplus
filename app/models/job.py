"""job data model"""
from sqlalchemy import Column, Integer, String, DateTime, text
from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    job_type = Column(String, nullable=False)
    status = Column(String, nullable=False, default="queued")
    payload = Column(String, nullable=False,default="{}")
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"),onupdate=text("CURRENT_TIMESTAMP"), nullable=False)
