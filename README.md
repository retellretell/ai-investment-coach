# AI 투자주치의
미래에셋증권 AI Festival 2025 출품작. AI 기반 투자 습관 분석 및 코칭 서비스.

## 설치
```bash
# 백엔드
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# 프론트엔드
cd frontend
npm install
npm run dev
```

## 데모
[Live Demo](https://your-vercel-url.vercel.app)

## 구조
- **backend/**: FastAPI 기반 백엔드 (KRX, DART, HyperCLOVA X 연동)
- **frontend/**: React + TypeScript + Tailwind CSS
- **docs/**: API 명세, 아키텍처 다이어그램, 스크린샷

