import pytest
import pandas as pd
from datetime import datetime, timedelta
from app.core.behavior_analyzer import BehaviorAnalyzer, InvestorType

@pytest.fixture
def sample_transactions():
    """테스트용 거래 데이터"""
    data = []
    base_date = datetime.now() - timedelta(days=30)
    
    for i in range(10):
        data.append({
            'user_id': 'test_user',
            'date': base_date + timedelta(days=i),
            'stock_code': 'A005930',
            'stock_name': '삼성전자',
            'sector': 'IT',
            'type': 'buy' if i % 2 == 0 else 'sell',
            'shares': 10,
            'price': 70000 + (i * 1000),
            'value': 10 * (70000 + (i * 1000))
        })
    
    return pd.DataFrame(data)

@pytest.mark.asyncio
async def test_analyze_behavior(sample_transactions):
    """행동 분석 테스트"""
    analyzer = BehaviorAnalyzer()
    behavior = await analyzer.analyze_behavior(sample_transactions)
    
    assert behavior.user_id == 'test_user'
    assert behavior.avg_holding_period >= 0
    assert 0 <= behavior.win_rate <= 100
    assert behavior.total_trades == len(sample_transactions)

@pytest.mark.asyncio
async def test_classify_investor_type():
    """투자자 유형 분류 테스트"""
    analyzer = BehaviorAnalyzer()
    
    # 단타형 투자자 시뮬레이션
    from app.core.behavior_analyzer import InvestmentBehavior
    
    short_term_behavior = InvestmentBehavior(
        user_id='test_user',
        analysis_date=datetime.now(),
        avg_holding_period=3.5,  # 7일 미만
        turnover_rate=80,
        win_loss_ratio=0.9,
        win_rate=45,
        loss_delay_rate=0.2,
        fomo_purchase_count=15,
        portfolio_volatility=25,
        sector_concentration={'IT': 0.8},
        total_trades=200,
        avg_trade_size=1000000,
        max_drawdown=30,
        cash_ratio=0.05
    )
    
    types = analyzer.classify_investor_type(short_term_behavior)
    assert InvestorType.SHORT_TERM_TRADER in types
    assert InvestorType.FOMO_PRONE in types
