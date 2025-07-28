from typing import List, Dict, Optional
from datetime import datetime
import uuid

from ..core.behavior_analyzer import InvestmentBehavior
from ..schemas.response import CoachingAction
from ..config import Constants

class RuleEngine:
    """정책 기반 룰 엔진"""
    
    def __init__(self):
        self.rules = self._initialize_rules()
        self.rule_history = {}
    
    def _initialize_rules(self) -> List[Dict]:
        """룰 정의"""
        return [
            {
                'id': 'R-001',
                'name': '과도한 회전율 경고',
                'priority': 'high',
                'condition': lambda b: b.turnover_rate > 60,
                'action_type': 'warning',
                'recommendation': {
                    'cash_ratio': 0.2,
                    'trading_suspension_days': 3
                },
                'message_template': "회전율이 {rate:.0f}%로 너무 높습니다. 잠시 숨을 고르세요.",
                'expected_impact': {
                    'turnover_reduction': -30,
                    'cost_saving': 0.04
                },
                'mstock_executable': True
            },
            {
                'id': 'R-002',
                'name': '단타 패턴 개선',
                'priority': 'high',
                'condition': lambda b: b.avg_holding_period < 7,
                'action_type': 'goal_setting',
                'recommendation': {
                    'min_holding_days': 7,
                    'stop_loss': -0.07,
                    'take_profit': 0.15
                },
                'message_template': "평균 보유기간이 {days:.1f}일로 너무 짧습니다.",
                'expected_impact': {
                    'holding_period_increase': 50,
                    'win_rate_improvement': 20
                },
                'mstock_executable': True
            },
            {
                'id': 'R-003',
                'name': 'FOMO 매수 억제',
                'priority': 'medium',
                'condition': lambda b: b.fomo_purchase_count > 10,
                'action_type': 'habit_correction',
                'recommendation': {
                    'cooling_period': 24,
                    'price_alert_threshold': 0.03
                },
                'message_template': "급등 후 매수가 {count}회 발생했습니다.",
                'expected_impact': {
                    'fomo_reduction': -50,
                    'entry_price_improvement': 3
                },
                'mstock_executable': False
            }
        ]
    
    async def evaluate_rules(self, behavior: InvestmentBehavior, 
                           user_context: Optional[Dict] = None) -> List[CoachingAction]:
        """행동 패턴에 대한 룰 평가"""
        triggered_actions = []
        
        for rule in self.rules:
            if rule['condition'](behavior):
                action = await self._create_coaching_action(rule, behavior)
                triggered_actions.append(action)
        
        return triggered_actions
    
    async def _create_coaching_action(self, rule: Dict, behavior: InvestmentBehavior) -> CoachingAction:
        """룰로부터 코칭 액션 생성"""
        message_params = {
            'rate': behavior.turnover_rate,
            'days': behavior.avg_holding_period,
            'count': behavior.fomo_purchase_count
        }
        
        description = rule['message_template'].format(**message_params)
        
        return CoachingAction(
            action_id=f"{rule['id']}_{uuid.uuid4().hex[:8]}",
            action_type=rule['action_type'],
            priority=rule['priority'],
            title=rule['name'],
            description=description,
            recommendation=rule['recommendation'],
            expected_impact=rule['expected_impact'],
            mstock_executable=rule['mstock_executable']
        )
