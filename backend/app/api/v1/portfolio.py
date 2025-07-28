from fastapi import APIRouter, HTTPException
from typing import Dict
import pandas as pd

from ...schemas.request import RebalancingExecuteRequest
from ...schemas.response import RebalancingPlanResponse
from ...core.rebalancing_engine import RebalancingEngine
from ...utils.demo_data import get_demo_portfolio, get_demo_behavior

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
