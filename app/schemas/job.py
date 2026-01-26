"""job schemas"""
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Dict, Any


class JobCreate(BaseModel):
    job_type: str = Field(...,min_length=2)
    payload: Dict = Field(default_factory=dict)
    
class JobRead(BaseModel): 
    id: int
    job_type: str
    status: str
    payload: str
    created_at:datetime
    updated_at:datetime
    model_config = ConfigDict(from_attributes=True)
    
class JobEventOut(BaseModel): 
    id: int
    job_id: int
    event_type: str
    payload: dict | None
    created_at: datetime
    
