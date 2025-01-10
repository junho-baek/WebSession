from fastapi import HTTPException
from database.users import USERS
from schemas.user_schema import LoginRequest

class UserService:
    @staticmethod
    async def login_user(request: LoginRequest):
        for user in USERS:
            if user["email"] == request.email and user["password"] == request.password:
                return {"message": "로그인 성공", "username": user["username"]}
        
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 잘못되었습니다.") 