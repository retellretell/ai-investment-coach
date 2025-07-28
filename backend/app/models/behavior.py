from sqlalchemy import Column, String, Float, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    analyses = relationship("BehaviorAnalysis", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")

class BehaviorAnalysis(Base):
    __tablename__ = "behavior_analyses"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    analysis_date = Column(DateTime, nullable=False)
    
    # 기본 지표
    avg_holding_period = Column(Float)
    turnover_rate = Column(Float)
    win_loss_ratio = Column(Float)
    win_rate = Column(Float)
    total_trades = Column(Integer)
    avg_trade_size = Column(Float)
    
    # 행동경제학 지표
    loss_delay_rate = Column(Float)
    fomo_purchase_count = Column(Integer)
    portfolio_volatility = Column(Float)
    max_drawdown = Column(Float)
    cash_ratio = Column(Float)
    
    # 섹터 정보
    sector_concentration = Column(JSON)
    
    # 투자자 유형
    investor_types = Column(JSON)
    
    # AI 생성 요약
    behavior_summary = Column(String)
    
    # Relationships
    user = relationship("User", back_populates="analyses")

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    stock_code = Column(String, nullable=False)
    stock_name = Column(String)
    type = Column(String)  # 'buy' or 'sell'
    shares = Column(Integer)
    price = Column(Float)
    value = Column(Float)
    sector = Column(String)
    
    # Relationships
    user = relationship("User", back_populates="transactions")

class CoachingAction(Base):
    __tablename__ = "coaching_actions"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    action_type = Column(String)  # 'rebalancing', 'warning', 'goal_setting', 'habit_correction'
    priority = Column(String)      # 'high', 'medium', 'low'
    title = Column(String)
    description = Column(String)
    recommendation = Column(JSON)
    expected_impact = Column(JSON)
    mstock_executable = Column(String)
    status = Column(String, default='pending')  # 'pending', 'completed', 'dismissed'
