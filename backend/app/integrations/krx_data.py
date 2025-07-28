import aiohttp
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from ..config import Config

class KRXDataClient:
    """한국거래소 데이터 클라이언트"""
    
    def __init__(self):
        self.api_key = Config.KRX_API_KEY
        self.base_url = "http://data-dbg.krx.co.kr/svc/apis"
    
    async def get_market_data(self, stock_code: str, start_date: str, end_date: str) -> Dict:
        """주식 시세 정보 조회"""
        # 데모용 데이터 반환
        return {
            'stock_code': stock_code,
            'data': [
                {
                    'date': '2024-01-15',
                    'open': 70000,
                    'high': 72000,
                    'low': 69500,
                    'close': 71500,
                    'volume': 15000000
                }
            ]
        }
    
    async def get_investor_stats(self) -> Dict:
        """투자자별 매매 통계"""
        # 데모용 통계 데이터
        return {
            'individual': {
                'avg_holding_period': 5.9,
                'monthly_turnover': 45.2,
                'win_rate': 42.3,
                'avg_return': -4.7
            },
            'institutional': {
                'avg_holding_period': 23.5,
                'monthly_turnover': 15.3,
                'win_rate': 58.2,
                'avg_return': 8.2
            }
        }
    
    async def get_sector_performance(self) -> Dict:
        """섹터별 수익률"""
        return {
            'IT': {'return': 15.3, 'volatility': 22.5},
            '금융': {'return': 8.7, 'volatility': 15.2},
            '바이오': {'return': -5.2, 'volatility': 35.7},
            '소비재': {'return': 6.5, 'volatility': 18.3},
            '산업재': {'return': 11.2, 'volatility': 20.1}
        }
