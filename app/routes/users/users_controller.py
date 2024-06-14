from fastapi import APIRouter, Depends
from typing import Annotated
from app.common.auth.auth_bearer import JWTBearer
from app.common.auth.auth_utils import get_current_user
from .users_service import getUsersService, getUserInfoService

router = APIRouter()
entity = "users"

@router.get("/", dependencies=[Depends(JWTBearer())], tags=[entity])
async def getUsers():
    return getUsersService()

@router.get("/user-info", dependencies=[Depends(JWTBearer())], tags=[entity])
async def getUserInfo(user: Annotated[dict, Depends(get_current_user)]):
    return getUserInfoService(user['email'])
