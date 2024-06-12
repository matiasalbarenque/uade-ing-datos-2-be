from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

def generate_uuid():
    return str(uuid4())

def generate_date():
    return str(datetime.now())

class Users(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    project_id: str
    task_id: str
    user_id: int
    comment: str
    likes: list
    date: str = Field(default_factory=generate_date)