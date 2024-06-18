from fastapi import APIRouter, Depends, HTTPException, Query, Body
from app.common.auth.auth_bearer import JWTBearer
from app.routes.roles.rol_service import getRolesService, getUserPermissions

router = APIRouter()
entity = "activities"

@router.get("/", dependencies=[Depends(JWTBearer())], tags=[entity])
async def getRoles():
    return getRolesService()

@router.get("/permissions", dependencies=[Depends(JWTBearer())], tags=[entity])
async def getPermissions(userId = Query()): 
    return getUserPermissions(userId)