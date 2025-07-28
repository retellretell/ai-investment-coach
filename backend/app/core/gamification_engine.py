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
            (
