from fastapi import APIRouter, Depends
from app.common.auth.auth_bearer import JWTBearer
from app.dto.activities import ActivitiesDto
from .activities_service import getActivitiesService, addActivity

router = APIRouter()
entity = "activities"

@router.get("/", dependencies=[Depends(JWTBearer())], tags=[entity])
async def getActivities():
    return getActivitiesService()

@router.post("/", dependencies=[Depends(JWTBearer())], tags=[entity])
async def addActivity(req: ActivitiesDto):
    return addActivity(req)
