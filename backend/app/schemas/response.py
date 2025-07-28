from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class CoachingAction(BaseModel):
    action_id: str
    action_type: str
    priority: str
    title: str
    description: str
    recommendation: Dict[str, Any]
    expected_impact: Dict[str, float]
    mstock_executable: bool = False

class BehaviorAnalysisResponse(BaseModel):
    user_id: str
    analysis_date: str
    avg_holding_period: float
    turnover_rate: float
    win_rate: float
    portfolio_volatility: float
    investor_types: List[str]
    behavior_summary: str

class RebalancingPlanResponse(BaseModel):
    plan_id: str
    created_at: str
    current_portfolio: Dict
    target_portfolio: Dict
    required_trades: List[Dict]
    expected_results: Dict
    estimated_cost: Dict

class ComprehensiveReportResponse(BaseModel):
    report_id: str
    user_id: str
    analysis_date: str
    behavior_analysis: Dict
    investor_types: List[str]
    behavior_summary: str
    coaching_actions: List[Dict]
    rebalancing_plan: Optional[Dict]
    gamification: Dict
    market_comparison: Dict
    improvement_goals: Dict
    next_review_date: str
