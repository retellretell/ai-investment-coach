from typing import Dict, List
import pandas as pd
import numpy as np
import uuid
from datetime import datetime

from ..core.behavior_analyzer import InvestmentBehavior
from ..config import Constants

class RebalancingEngine:
    """포트폴리오 리밸런싱 엔진"""
    
    def __init__(self):
        self.risk_limits = {
            'max_sector_concentration': 0.3,
            'max_single_stock': 0.1,
            'target_volatility': 0.12,
            'min_cash_ratio': 0.1,
            'max_correlation': 0.7
        }
    
    async def generate_rebalancing_plan(self, portfolio: pd.DataFrame, 
                                       behavior: InvestmentBehavior) -> Dict:
        """리밸런싱 계획 생성"""
        # 데모용 포트폴리오 분석
        current_positions = self._analyze_current_portfolio(portfolio)
        
        # 데모용 목표 포트폴리오
        target_positions = {
            'A005930': {'name': '삼성전자', 'sector': 'IT', 'target_weight': 0.15},
            'A035720': {'name': '카카오', 'sector': 'IT', 'target_weight': 0.10},
            'A051910': {'name': 'LG화학', 'sector': '화학', 'target_weight': 0.10},
            'A105560': {'name': 'KB금융', 'sector': '금융', 'target_weight': 0.15},
            'A207940': {'name': '삼성바이오로직스', 'sector': '바이오', 'target_weight': 0.10},
            'cash': {'name': '현금', 'sector': '현금', 'target_weight': 0.15}
        }
        
        # 필요한 거래 계산
        trades = self._calculate_required_trades(current_positions, target_positions)
        
        return {
            'plan_id': str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(),
            'current_portfolio': current_positions,
            'target_portfolio': target_positions,
            'required_trades': trades,
            'expected_results': {
                'volatility_reduction': -15,
                'sector_balance_improvement': 25,
                'risk_score_improvement': -20
            },
            'estimated_cost': {
                'commission': sum(t['trade_value'] for t in trades) * 0.0008,
                'tax': sum(t['trade_value'] for t in trades if t['action'] == 'sell') * 0.0023
            }
        }
    
    def _analyze_current_portfolio(self, portfolio: pd.DataFrame) -> Dict:
        """현재 포트폴리오 분석 (데모용)"""
        # 데모 포트폴리오
        return {
            'A005930': {'name': '삼성전자', 'sector': 'IT', 'weight': 0.35, 'value': 3500000},
            'A035720': {'name': '카카오', 'sector': 'IT', 'weight': 0.25, 'value': 2500000},
            'A000660': {'name': 'SK하이닉스', 'sector': 'IT', 'weight': 0.20, 'value': 2000000},
            'cash': {'name': '현금', 'sector': '현금', 'weight': 0.05, 'value': 500000}
        }
    
    def _calculate_required_trades(self, current: Dict, target: Dict) -> List[Dict]:
        """필요한 거래 계산"""
        trades = []
        total_value = sum(pos['value'] for pos in current.values())
        
        # 매도 거래
        trades.append({
            'stock_code': 'A000660',
            'stock_name': 'SK하이닉스',
            'action': 'sell',
            'shares': 150,
            'trade_value': 2000000,
            'reason': 'IT 섹터 과다 집중 해소'
        })
        
        # 매수 거래
        trades.extend([
            {
                'stock_code': 'A105560',
                'stock_name': 'KB금융',
                'action': 'buy',
                'shares': 200,
                'trade_value': 1500000,
                'reason': '금융 섹터 비중 확대'
            },
            {
                'stock_code': 'A207940',
                'stock_name': '삼성바이오로직스',
                'action': 'buy',
                'shares': 2,
                'trade_value': 1000000,
                'reason': '바이오 섹터 신규 편입'
            }
        ])
        
        return trades
