from typing import Dict, List
from datetime import datetime
import uuid

from ..models.behavior import InvestmentBehavior

class GamificationEngine:
    """게이미피케이션 엔진"""
    
    def __init__(self):
        self.badges = {
            'first_week': {'name': '첫 주 완주', 'points': 100, 'icon': '🎯'},
            'steady_investor': {'name': '꾸준한 투자자', 'points': 500, 'icon': '💪'},
            'risk_manager': {'name': '리스크 관리자', 'points': 300, 'icon': '🛡️'},
            'profit_taker': {'name': '수익 실현 달인', 'points': 600, 'icon': '📈'},
            'fomo_fighter': {'name': 'FOMO 극복', 'points': 800, 'icon': '🧘'}
        }
        
        self.levels = [
            (0, '투자 입문자'),
            (1000, '투자 수련생'),
            (3000, '투자 중급자'),
            (6000, '투자 고급자'),
            (10000, '투자 전문가'),
            (20000, '투자 마스터')
        ]
    
    async def check_achievements(self, behavior: InvestmentBehavior) -> List[Dict]:
        """달성한 배지 확인"""
        new_badges = []
        
        # 첫 주 완주
        if behavior.avg_holding_period >= 7:
            new_badges.append({
                'badge_id': 'first_week',
                'name': self.badges['first_week']['name'],
                'points': self.badges['first_week']['points'],
                'icon': self.badges['first_week']['icon'],
                'achieved_at': datetime.now().isoformat()
            })
        
        # FOMO 극복
        if behavior.fomo_purchase_count <= 5:
            new_badges.append({
                'badge_id': 'fomo_fighter',
                'name': self.badges['fomo_fighter']['name'],
                'points': self.badges['fomo_fighter']['points'],
                'icon': self.badges['fomo_fighter']['icon'],
                'achieved_at': datetime.now().isoformat()
            })
        
        return new_badges
    
    async def calculate_level(self, total_points: int) -> Dict:
        """사용자 레벨 계산"""
        current_level = None
        next_level = None
        
        for i, (points, title) in enumerate(self.levels):
            if total_points >= points:
                current_level = {'level': i + 1, 'title': title, 'min_points': points}
            else:
                next_level = {'level': i + 1, 'title': title, 'required_points': points}
                break
        
        progress = 0
        if current_level and next_level:
            progress = ((total_points - current_level['min_points']) / 
                       (next_level['required_points'] - current_level['min_points']) * 100)
        
        return {
            'current': current_level,
            'next': next_level,
            'progress': progress,
            'total_points': total_points
        }
