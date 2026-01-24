#import from sqlalchemy such as coulmn, integer, string, Datetime
#create a class,
#create a table with the field id, job_id event_type, create_at
from sqlalchemy import Column, Integer, String, DateTime, text
from app.db.base import Base
from app.models.job import Job
class JobEvent(Base):
    __tablename__ = 'job_events'
    id = Column(Integer, nullable=False, primary_key=True, index= True)
    job_id = Column(Integer, nullable = False)
    event_type = Column(String, nullable= False)
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
 

