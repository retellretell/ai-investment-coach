from fastapi import APIRouter, HTTPException
from typing import Dict

from ...schemas.request import RebalancingExecuteRequest
from ...schemas.response import RebalancingPlanResponse
from ...core.rebalancing_engine import RebalancingEngine
from ...utils.demo_data import get_demo_portfolio

router = APIRouter(prefix="/portfolio", tags=["portfolio"])

rebalancing_engine = RebalancingEngine()

@router.get("/current/{user_id}")
async def get_current_portfolio(user_id: str):
    """현재 포트폴리오 조회"""
    try:
        portfolio = get_demo_portfolio(user_id)
        return {
            'user_id': user_id,
            'portfolio': portfolio,
            'total_value': sum(p['value'] for p in portfolio),
            'last_updated': '2024-01-15T10:30:00'
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/rebalance")
async def create_rebalancing_plan(request: RebalancingExecuteRequest):
    """리밸런싱 계획 생성"""
    try:
        # 데모용 포트폴리오와 행동 데이터
        from ...utils.demo_data import get_demo_behavior
        
        portfolio_df = get_demo_portfolio(request.user_id)
        behavior = get_demo_behavior(request.user_id)
        
        plan = await rebalancing_engine.generate_rebalancing_plan(
            portfolio_df, behavior
        )
        
        return RebalancingPlanResponse(**plan)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
