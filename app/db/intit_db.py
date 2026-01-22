from app.db.base import Base
from app.db.session import engine

#import model: 
from app.models.job import Job

def init_db():
    Base.metadata.create_all(bind=engine)