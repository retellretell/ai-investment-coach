import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """시스템 설정"""
    # API Keys
    KRX_API_KEY = os.getenv("KRX_API_KEY", "E7E66EAC74E4449AA6A429176F96F0F37D5EDD57")
    DART_API_KEY = os.getenv("DART_API_KEY", "e45fa610cea4a8e8a6eebd9e05e3580daa071f82")
    HYPERCLOVAX_API_KEY = os.getenv("HYPERCLOVAX_API_KEY", "demo_key")
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./investment_coach.db")
    
    # App Settings
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Constants:
    """시스템 상수"""
    # 미래에셋증권 연동 (데모용)
    MSTOCK_COMMISSION_RATE = 0.08  # 기본 수수료율 0.08%
    MSTOCK_DISCOUNT_RATE = 0.04    # 리밸런싱 실행 시 할인율 0.04%
    
    # 행동 분석 임계값
    BEHAVIOR_THRESHOLDS = {
        'high_turnover': 2.0,      # 평균 대비 2배
        'short_holding': 7,        # 7일 미만
        'high_volatility': 0.15,   # 15% 초과
        'sector_concentration': 0.3, # 30% 이상
        'loss_delay': 0.3,         # 30% 이상
        'fomo_threshold': 0.05,    # 5% 급등 후 매수
        'min_cash_ratio': 0.1      # 최소 현금 비중 10%
    }
    
    # KPI 목표치
    TARGET_KPI = {
        'avg_holding_period': 7,    # 7일 이상
        'monthly_turnover': 30,     # 30% 이하
        'win_rate': 60,            # 60% 이상
        'portfolio_volatility': 12, # 12% 이하
        'fomo_count': 5            # 월 5회 이하
    }
