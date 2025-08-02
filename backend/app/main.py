from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .api.v1 import analysis, portfolio, gamification
from .config import Config

# FastAPI 앱 생성
app = FastAPI(
    title="AI 투자주치의 API",
    description="투자 습관을 진단하고 올바른 행동을 설계하는 AI 코치",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(analysis.router, prefix="/api/v1")
app.include_router(portfolio.router, prefix="/api/v1")
app.include_router(gamification.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "service": "AI 투자주치의",
        "version": "1.0.0",
        "description": "미래에셋증권 AI Festival 2025"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
