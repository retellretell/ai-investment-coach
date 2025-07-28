# 배포 가이드

## 로컬 개발 환경

### 사전 요구사항
- Python 3.9+
- Node.js 18+
- Git

### 설치 및 실행
```bash
# 1. 저장소 클론
git clone https://github.com/yourusername/ai-investment-coach.git
cd ai-investment-coach

# 2. 환경 변수 설정
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# 3. 의존성 설치
make install

# 4. 실행
make run
