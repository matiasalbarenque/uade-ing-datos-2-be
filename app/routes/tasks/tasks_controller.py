from fastapi import APIRouter, Depends, HTTPException, Query, Body
# from app.common.auth.auth_bearer import JWTBearer
from app.dto.tasks import TasksDto
from typing import Optional, Dict
from app.routes.tasks.tasks_service import addTaskService, getTasksService, updateTaskService

router = APIRouter()
entity = "tasks"

@router.get("/", tags=[entity])
async def getTasks():
    result = await getTasksService()
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@router.post("/", tags=[entity])
async def addActivity(req: TasksDto):
    result = await addTaskService(req)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@router.put("/", tags=[entity])
async def updateActivity(req: TasksDto):
    result = await updateTaskService(req)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result
