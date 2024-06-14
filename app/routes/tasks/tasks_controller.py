from fastapi import APIRouter, Depends
from app.common.auth.auth_bearer import JWTBearer
from .tasks_service import getTasksService

router = APIRouter()
entity = "tasks"

@router.get("/", dependencies=[Depends(JWTBearer())], tags=[entity])
async def getTasks():
    return getTasksService()
