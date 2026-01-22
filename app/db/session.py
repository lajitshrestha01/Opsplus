"""database connection"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(
    autoflush=False, 
    autocommit =False, 
    bind=engine,
)

def get_db():
    db = SessionLocal()
    try: 
        yield db 
    finally: 
        db.close()


