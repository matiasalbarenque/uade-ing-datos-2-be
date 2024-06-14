from fastapi import APIRouter, Depends
from app.common.auth.auth_bearer import JWTBearer
from .projects_service import getProjectsService

router = APIRouter()
entity = "projects"

@router.get("/", dependencies=[Depends(JWTBearer())], tags=[entity])
async def getProjects():
    return getProjectsService()
