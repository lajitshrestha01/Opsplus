"""job data model"""
import json
from sqlalchemy import Column, Integer, String, DateTime, text
from app.db.base import Base


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, nullable=False, primary_key=True, index=True)
    job_type = Column(String, nullable=False)
    status = Column(String, nullable=False, default="queued")
    payload = Column(String, nullable=False, default="{}")
    attempts = Column(Integer, default=0, nullable=False)
    max_attempts = Column(Integer, default=3, nullable=False)
    run_after = Column(DateTime(timezone=True), nullable=True)
    locked_at = Column(DateTime(timezone=True), nullable=True)
    locked_by = Column(String(64), nullable=True)
    result_json = Column(String, nullable=True)
    error_json = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=text(
        "CURRENT_TIMESTAMP"), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=text(
        "CURRENT_TIMESTAMP"), onupdate=text("CURRENT_TIMESTAMP"), nullable=False)

    @property
    def payload_obj(self):
        try:
            return json.loads(self.payload) if self.payload else None
        except Exception:
            return {"_raw": self.payload}

    @property
    def result(self):
        try:
            return json.loads(self.result_json) if self.result_json else None
        except Exception:
            return {"_raw": self.result_json}

    @property
    def error(self):
        try:
            return json.loads(self.error_json) if self.error_json else None
        except Exception:
            return {"_raw": self.error_json}
