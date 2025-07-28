from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd
import numpy as np
from enum import Enum

from ..config import Constants

@dataclass
class InvestmentBehavior:
    """투자 행동 패턴 데이터"""
    user_id: str
    analysis_date: datetime
    avg_holding_period: float
    turnover_rate: float
    win_loss_ratio: float
    win_rate: float
    loss_delay_rate: float
    fomo_purchase_count: int
    portfolio_volatility: float
    sector_concentration: Dict[str, float]
    total_trades: int
    avg_trade_size: float
    max_drawdown: float
    cash_ratio: float

    def to_dict(self) -> Dict:
        data = {
            'user_id': self.user_id,
            'analysis_date': self.analysis_date.isoformat(),
            'avg_holding_period': self.avg_holding_period,
            'turnover_rate': self.turnover_rate,
            'win_loss_ratio': self.win_loss_ratio,
            'win_rate': self.win_rate,
            'loss_delay_rate': self.loss_delay_rate,
            'fomo_purchase_count': self.fomo_purchase_count,
            'portfolio_volatility': self.portfolio_volatility,
            'sector_concentration': self.sector_concentration,
            'total_trades': self.total_trades,
            'avg_trade_size': self.avg_trade_size,
            'max_drawdown': self.max_drawdown,
            'cash_ratio': self.cash_ratio
        }
        return data

class InvestorType(Enum):
    SHORT_TERM_TRADER = "단타형"
    LOSS_AVERSE = "손실회피 과도형"
    CONFIRMATION_BIAS = "확증편향 주의"
    FOMO_PRONE = "FOMO 취약형"
    OVERCONFIDENT = "과신형"
    BALANCED = "균형형"
    CONSERVATIVE = "보수형"
    AGGRESSIVE = "공격형"

class BehaviorAnalyzer:
    """투자 행동 패턴 분석기"""
    
    def __init__(self):
        self.thresholds = Constants.BEHAVIOR_THRESHOLDS
    
    async def analyze_behavior(self, transactions: pd.DataFrame, 
                             market_data: Optional[pd.DataFrame] = None) -> InvestmentBehavior:
        """거래 데이터로부터 행동 패턴 분석"""
        user_id = transactions['user_id'].iloc[0] if len(transactions) > 0 else 'demo_user'
        
        # 기본 메트릭 계산
        metrics = await self._calculate_basic_metrics(transactions)
        
        # 행동경제학 기반 추가 분석
        behavioral_metrics = await self._analyze_behavioral_biases(transactions, market_data)
        
        # 포트폴리오 리스크 분석
        risk_metrics = await self._analyze_portfolio_risk(transactions)
        
        return InvestmentBehavior(
            user_id=user_id,
            analysis_date=datetime.now(),
            avg_holding_period=metrics['avg_holding_period'],
            turnover_rate=metrics['turnover_rate'],
            win_loss_ratio=metrics['win_loss_ratio'],
            win_rate=metrics['win_rate'],
            loss_delay_rate=behavioral_metrics['loss_delay_rate'],
            fomo_purchase_count=behavioral_metrics['fomo_count'],
            portfolio_volatility=risk_metrics['volatility'],
            sector_concentration=risk_metrics['sector_concentration'],
            total_trades=metrics['total_trades'],
            avg_trade_size=metrics['avg_trade_size'],
            max_drawdown=risk_metrics['max_drawdown'],
            cash_ratio=risk_metrics['cash_ratio']
        )
    
    async def _calculate_basic_metrics(self, transactions: pd.DataFrame) -> Dict:
        """기본 투자 지표 계산"""
        if len(transactions) == 0:
            return {
                'avg_holding_period': 0,
                'turnover_rate': 0,
                'win_loss_ratio': 0,
                'win_rate': 0,
                'total_trades': 0,
                'avg_trade_size': 0
            }
        
        # 평균 보유기간 계산 (데모용 간단 계산)
        avg_holding = np.random.uniform(3, 15)  # 3-15일 사이 랜덤
        
        # 회전율 계산
        turnover_rate = np.random.uniform(20, 80)  # 20-80% 사이
        
        # 승률 계산
        win_rate = np.random.uniform(35, 65)  # 35-65% 사이
        
        # 익절/손절 비율
        win_loss_ratio = np.random.uniform(0.5, 2.0)
        
        return {
            'avg_holding_period': avg_holding,
            'turnover_rate': turnover_rate,
            'win_loss_ratio': win_loss_ratio,
            'win_rate': win_rate,
            'total_trades': len(transactions),
            'avg_trade_size': transactions['value'].mean() if 'value' in transactions else 1000000
        }
    
    async def _analyze_behavioral_biases(self, transactions: pd.DataFrame, 
                                       market_data: Optional[pd.DataFrame]) -> Dict:
        """행동경제학적 편향 분석"""
        # FOMO 패턴 (데모용)
        fomo_count = np.random.randint(3, 20)
        
        # 손실 확정 지연
        loss_delay_rate = np.random.uniform(0.1, 0.5)
        
        return {
            'fomo_count': fomo_count,
            'loss_delay_rate': loss_delay_rate,
            'herding_score': np.random.uniform(0, 1),
            'overconfidence_score': np.random.uniform(0, 1)
        }
    
    async def _analyze_portfolio_risk(self, transactions: pd.DataFrame) -> Dict:
        """포트폴리오 리스크 분석"""
        # 섹터 집중도 (데모용)
        sectors = ['IT', '금융', '바이오', '소비재', '산업재']
        sector_weights = np.random.dirichlet(np.ones(len(sectors)))
        sector_concentration = {sector: weight for sector, weight in zip(sectors, sector_weights)}
        
        # 변동성
        volatility = np.random.uniform(8, 25)
        
        # MDD
        max_drawdown = np.random.uniform(5, 30)
        
        # 현금 비중
        cash_ratio = np.random.uniform(0.05, 0.3)
        
        return {
            'volatility': volatility,
            'sector_concentration': sector_concentration,
            'max_drawdown': max_drawdown,
            'cash_ratio': cash_ratio
        }
    
    def classify_investor_type(self, behavior: InvestmentBehavior) -> List[InvestorType]:
        """투자자 성향 분류"""
        types = []
        
        if behavior.avg_holding_period < self.thresholds['short_holding']:
            types.append(InvestorType.SHORT_TERM_TRADER)
        
        if behavior.loss_delay_rate > self.thresholds['loss_delay']:
            types.append(InvestorType.LOSS_AVERSE)
        
        if behavior.fomo_purchase_count > Constants.TARGET_KPI['fomo_count']:
            types.append(InvestorType.FOMO_PRONE)
        
        if behavior.portfolio_volatility > 20:
            types.append(InvestorType.AGGRESSIVE)
        
        if not types:
            types.append(InvestorType.BALANCED)
        
        return types
