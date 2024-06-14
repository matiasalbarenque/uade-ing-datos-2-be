from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

def generate_uuid():
    return str(uuid4())

def generate_date():
    return str(datetime.now())

class ActivitiesDto(BaseModel):
    project_id: str
    task_id: str
    user_id: int
    comment: str
    likes: list
    date: str = Field(default_factory=generate_date)

    class Config:
        json_schema_extra = {
            "example": {
                "project_id": "",
                "task_id": ""
            }
        }
