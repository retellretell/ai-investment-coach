from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class TransactionData(BaseModel):
    user_id: str = Field(..., description="사용자 ID")
    transactions: List[Dict[str, Any]] = Field(..., description="거래 내역")
    include_market_data: bool = Field(False, description="시장 데이터 포함 여부")

class PortfolioAnalysisRequest(BaseModel):
    user_id: str
    include_rebalancing: bool = True
    
class RebalancingExecuteRequest(BaseModel):
    user_id: str
    plan_id: str
    execute_immediately: bool = False

class UserPreferences(BaseModel):
    risk_tolerance: str = Field("moderate", description="low, moderate, high")
    investment_goal: str = Field("growth", description="stability, growth, income")
    preferred_sectors: Optional[List[str]] = None
