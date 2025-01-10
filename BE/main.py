from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프론트엔드 서버 주소
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 서버 상태 확인용 엔드포인트
@app.get("/")
async def read_root():
    return {"status": "running"}

# 로그인 요청 모델 json으로 리퀘스트를 받으려면 필요하다.
class LoginRequest(BaseModel):
    email: str
    password: str
    username: str

# 임시 사용자 데이터 (실제로는 데이터베이스를 사용해야 함)
USERS = [
    {
        "email": "test@example.com",
        "password": "1234",
        "username": "테스트"
    },
    {
        "email": "junho@example.com",
        "password": "1234",
        "username": "junho"
    }
]

@app.post("/api/user/login")
async def login(request: LoginRequest):
    # 간단한 로그인 검증
    for user in USERS:
        if user["email"] == request.email and user["password"] == request.password:
            return {"message": "로그인 성공", "username": user["username"]}
    
    raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 잘못되었습니다.")


