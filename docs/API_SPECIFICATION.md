# AI 투자주치의 API 명세서

## 기본 정보
- Base URL: `http://localhost:8000/api/v1`
- Content-Type: `application/json`

## 엔드포인트

### 1. 종합 분석
**GET** `/analysis/demo/{user_id}`

사용자의 투자 행동을 종합적으로 분석합니다.

**Response:**
```json
{
  "report_id": "uuid",
  "user_id": "string",
  "analysis_date": "2024-01-15T10:30:00",
  "behavior_analysis": {
    "avg_holding_period": 5.9,
    "turnover_rate": 45.2,
    "win_rate": 42.3,
    "portfolio_volatility": 18.5
  },
  "investor_types": ["단타형", "FOMO 취약형"],
  "behavior_summary": "AI가 생성한 행동 요약",
  "coaching_actions": [],
  "gamification": {
    "level": {},
    "new_badges": [],
    "points": 1500
  }
}
