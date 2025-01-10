from fastapi import FastAPI, HTTPException, APIRouter
from schemas.user_schema import LoginRequest
from services.user_service import UserService

router = APIRouter(prefix="/api/user", tags=["user"])


@router.post("/login")
async def login(request: LoginRequest):
    return await UserService.login_user(request) 