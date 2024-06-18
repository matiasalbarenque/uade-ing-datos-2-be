from fastapi import APIRouter, Depends, HTTPException, Query, Body
#from app.common.auth.auth_bearer import JWTBearer
from app.dto.assignation import AssignDto
from app.dto.profiles import ProfileDto

from typing import Optional, Dict
from app.routes.profiles.profiles_service import addProfileService, getProfileService, updateProfileService, addProfileSkillService, findProfileService

router = APIRouter()
entity = "profiles"

@router.get("/{user_id}", tags=[entity])
async def findProfile(user_id: str):
    result = await findProfileService(user_id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@router.get("/", tags=[entity])
async def getProfile():
    result = await getProfileService()
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result
        
@router.put("/", tags=[entity])
async def updateProfile(req: ProfileDto):
    result = await updateProfileService(req)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@router.post("/", tags=[entity])
async def addProfile(req: ProfileDto):
    result = await addProfileService(req)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@router.post("/skills", tags=[entity])
async def addProfileSkill(req: AssignDto):
    result = await addProfileSkillService(req)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result
