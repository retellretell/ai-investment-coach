from fastapi import APIRouter, HTTPException
from typing import Dict

from ...core.gamification_engine import GamificationEngine

router = APIRouter(prefix="/gamification", tags=["gamification"])

gamification_engine = GamificationEngine()

@router.get("/user/{user_id}/status")
async def get_gamification_status(user_id: str):
    """사용자 게이미피케이션 현황"""
    try:
        # 데모용 데이터
        total_points = 1500
        level_info = await gamification_engine.calculate_level(total_points)
        
        return {
            'user_id': user_id,
            'total_points': total_points,
            'level': level_info,
            'badges': [
                {
                    'badge_id': 'first_week',
                    'name': '첫 주 완주',
                    'icon': '🎯',
                    'achieved_at': '2024-01-10T15:30:00'
                }
            ],
            'streaks': {
                'plan_adherence': 7,
                'no_fomo': 14
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/leaderboard")
async def get_leaderboard():
    """리더보드 조회"""
    return {
        'weekly': [
            {'rank': 1, 'user_name': '투자왕', 'points': 2500, 'improvement': '+15%'},
            {'rank': 2, 'user_name': '현명한투자자', 'points': 2300, 'improvement': '+12%'},
            {'rank': 3, 'user_name': '장기투자자', 'points': 2100, 'improvement': '+10%'}
        ]
    }
