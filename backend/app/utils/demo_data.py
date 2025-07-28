import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict
import random

from ..models.behavior import InvestmentBehavior

def generate_demo_transactions(user_id: str) -> pd.DataFrame:
    """데모용 거래 데이터 생성"""
    stocks = [
        {'code': 'A005930', 'name': '삼성전자', 'sector': 'IT'},
        {'code': 'A035720', 'name': '카카오', 'sector': 'IT'},
        {'code': 'A000660', 'name': 'SK하이닉스', 'sector': 'IT'},
        {'code': 'A051910', 'name': 'LG화학', 'sector': '화학'},
        {'code': 'A105560', 'name': 'KB금융', 'sector': '금융'}
    ]
    
    transactions = []
    base_date = datetime.now() - timedelta(days=90)
    
    for i in range(50):
        stock = random.choice(stocks)
        date = base_date + timedelta(days=random.randint(0, 90))
        
        transaction = {
            'user_id': user_id,
            'date': date,
            'stock_code': stock['code'],
            'stock_name': stock['name'],
            'sector': stock['sector'],
            'type': random.choice(['buy', 'sell']),
            'shares': random.randint(10, 100),
            'price': random.randint(50000, 150000),
            'value': 0
        }
        transaction['value'] = transaction['shares'] * transaction['price']
        transactions.append(transaction)
    
    return pd.DataFrame(transactions).sort_values('date')

def get_demo_portfolio(user_id: str) -> List[Dict]:
    """데모용 포트폴리오 데이터"""
    return [
        {
            'stock_code': 'A005930',
            'stock_name': '삼성전자',
            'sector': 'IT',
            'shares': 50,
            'avg_price': 70000,
            'current_price': 72000,
            'value': 3600000
        },
        {
            'stock_code': 'A035720',
            'stock_name': '카카오',
            'sector': 'IT',
            'shares': 60,
            'avg_price': 42000,
            'current_price': 41000,
            'value': 2460000
        },
        {
            'stock_code': 'A000660',
            'stock_name': 'SK하이닉스',
            'sector': 'IT',
            'shares': 20,
            'avg_price': 130000,
            'current_price': 135000,
            'value': 2700000
        }
    ]

def get_demo_behavior(user_id: str) -> InvestmentBehavior:
    """데모용 행동 분석 데이터"""
    return InvestmentBehavior(
        user_id=user_id,
        analysis_date=datetime.now(),
        avg_holding_period=5.9,
        turnover_rate=45.2,
        win_loss_ratio=0.82,
        win_rate=42.3,
        loss_delay_rate=0.32,
        fomo_purchase_count=12,
        portfolio_volatility=18.5,
        sector_concentration={'IT': 0.65, '금융': 0.15, '화학': 0.20},
        total_trades=156,
        avg_trade_size=1500000,
        max_drawdown=23.5,
        cash_ratio=0.05
    )
