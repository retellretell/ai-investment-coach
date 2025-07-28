import uuid
from datetime import datetime, timedelta
from typing import Dict, Optional
import pandas as pd

from .behavior_analyzer import BehaviorAnalyzer
from .rule_engine import RuleEngine
from .rebalancing_engine import RebalancingEngine
from .gamification_engine import GamificationEngine
from ..integrations.hyperclovax import HyperClovaXClient
from ..integrations.krx_data import KRXDataClient
from ..models.behavior import InvestmentBehavior  # 추가

class CoachingOrchestrator:
    """AI 코칭 통합 관리"""
    
    def __init__(self):
        self.behavior_analyzer = BehaviorAnalyzer()
        self.rule_engine = RuleEngine()
        self.rebalancing_engine = RebalancingEngine()
        self.gamification_engine = GamificationEngine()
        self.llm_client = HyperClovaXClient()
        self.krx_client = KRXDataClient()
    
    async def generate_comprehensive_report(self, user_id: str, 
                                          transactions: pd.DataFrame,
                                          include_rebalancing: bool = True) -> Dict:
        """종합 투자 진단 리포트 생성"""
        # 1. 행동 패턴 분석
        behavior = await self.behavior_analyzer.analyze_behavior(transactions)
        
        # 2. 투자자 성향 분류
        investor_types = self.behavior_analyzer.classify_investor_type(behavior)
        
        # 3. 룰 엔진 평가
        coaching_actions = await self.rule_engine.evaluate_rules(behavior)
        
        # 4. AI 메시지 생성
        behavior_summary = await self.llm_client.generate_behavior_summary(behavior, investor_types)
        
        # 5. 리밸런싱 계획
        rebalancing_plan = None
        if include_rebalancing:
            portfolio_df = self._get_current_portfolio(transactions)
            rebalancing_plan = await self.rebalancing_engine.generate_rebalancing_plan(
                portfolio_df, behavior
            )
        
        # 6. 게이미피케이션
        badges = await self.gamification_engine.check_achievements(behavior)
        level_info = await self.gamification_engine.calculate_level(1500)  # 데모용 포인트
        
        # 7. KRX 통계 비교
        investor_stats = await self.krx_client.get_investor_stats()
        
        # 8. 개선 목표
        improvement_goals = self._generate_improvement_goals(behavior, investor_stats)
        
        return {
            'report_id': str(uuid.uuid4()),
            'user_id': user_id,
            'analysis_date': datetime.now().isoformat(),
            'behavior_analysis': behavior.to_dict(),
            'investor_types': [t.value for t in investor_types],
            'behavior_summary': behavior_summary,
            'coaching_actions': [
                {
                    'action_id': action.action_id,
                    'type': action.action_type,
                    'priority': action.priority,
                    'title': action.title,
                    'description': action.description,
                    'recommendation': action.recommendation,
                    'expected_impact': action.expected_impact
                }
                for action in coaching_actions[:3]  # 상위 3개만
            ],
            'rebalancing_plan': rebalancing_plan,
            'gamification': {
                'new_badges': badges,
                'level': level_info,
                'points': 1500
            },
            'market_comparison': {
                'your_metrics': {
                    'avg_holding_period': behavior.avg_holding_period,
                    'turnover_rate': behavior.turnover_rate,
                    'win_rate': behavior.win_rate
                },
                'market_average': investor_stats['individual']
            },
            'improvement_goals': improvement_goals,
            'next_review_date': (datetime.now() + timedelta(days=7)).isoformat()
        }
    
    def _get_current_portfolio(self, transactions: pd.DataFrame) -> pd.DataFrame:
        """현재 포트폴리오 추출 (데모용)"""
        return pd.DataFrame([
            {'stock_code': 'A005930', 'stock_name': '삼성전자', 'sector': 'IT', 'value': 3500000},
            {'stock_code': 'A035720', 'stock_name': '카카오', 'sector': 'IT', 'value': 2500000},
            {'stock_code': 'A000660', 'stock_name': 'SK하이닉스', 'sector': 'IT', 'value': 2000000}
        ])
    
    def _generate_improvement_goals(self, behavior: InvestmentBehavior, market_stats: Dict) -> Dict:
        """개선 목표 생성"""
        goals = {}
        
        # 보유기간 목표
        if behavior.avg_holding_period < 7:
            goals['holding_period'] = {
                'current': behavior.avg_holding_period,
                'target': 7,
                'market_avg': market_stats['individual']['avg_holding_period'],
                'improvement_needed': f'+{7 - behavior.avg_holding_period:.1f}일'
            }
        
        # 회전율 목표
        if behavior.turnover_rate > 30:
            goals['turnover_rate'] = {
                'current': behavior.turnover_rate,
                'target': 30,
                'market_avg': market_stats['individual']['monthly_turnover'],
                'improvement_needed': f'-{behavior.turnover_rate - 30:.0f}%p'
            }
        
        return goals
