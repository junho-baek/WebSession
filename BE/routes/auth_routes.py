from fastapi import APIRouter
from schemas.user_schema import LoginRequest, LoginResponse
from BE.services.user_service import AuthService

router = APIRouter()

