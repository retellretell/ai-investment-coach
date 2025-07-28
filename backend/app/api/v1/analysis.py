from fastapi import APIRouter, HTTPException, Depends
from typing import Dict
import pandas as pd

from ...schemas.request import TransactionData, PortfolioAnalysisRequest
from ...schemas.response import ComprehensiveReportResponse
from ...core.coaching_orchestrator import CoachingOrchestrator
from ...utils.demo_data import generate_demo_transactions

router = APIRouter(prefix="/analysis", tags=["analysis"])

# 전역 오케스트레이터 인스턴스
orchestrator = CoachingOrchestrator()

@router.post("/comprehensive", response_model=ComprehensiveReportResponse)
async def analyze_comprehensive(request: PortfolioAnalysisRequest):
    """종합 투자 행동 분석"""
    try:
        # 데모용 거래 데이터 생성
        transactions = generate_demo_transactions(request.user_id)
        
        # 종합 분석 실행
        report = await orchestrator.generate_comprehensive_report(
            request.user_id,
            transactions,
            include_rebalancing=request.include_rebalancing
        )
        
        return ComprehensiveReportResponse(**report)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/demo/{user_id}")
async def get_demo_analysis(user_id: str):
    """데모 분석 결과 조회"""
    try:
        # 데모 데이터로 분석 실행
        transactions = generate_demo_transactions(user_id)
        report = await orchestrator.generate_comprehensive_report(
            user_id, transactions, include_rebalancing=True
        )
        
        return report
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
