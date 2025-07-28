import React, { useState, useEffect } from 'react';
import { RefreshCw, TrendingUp, AlertTriangle } from 'lucide-react';
import { api } from '../services/api';

const Portfolio: React.FC = () => {
  const [portfolio, setPortfolio] = useState<any>(null);
  const [rebalancingPlan, setRebalancingPlan] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchPortfolio();
  }, []);
  
  const fetchPortfolio = async () => {
    try {
      const result = await api.getPortfolio('demo_user');
      setPortfolio(result);
    } catch (error) {
      console.error('Failed to fetch portfolio:', error);
    } finally {
      setLoading(false);
    }
  };
  
  const generateRebalancingPlan = async () => {
    try {
      const plan = await api.createRebalancingPlan('demo_user');
      setRebalancingPlan(plan);
    } catch (error) {
      console.error('Failed to generate rebalancing plan:', error);
    }
  };
  
  if (loading) {
    return <div className="flex justify-center items-center h-64">로딩 중...</div>;
  }
  
  return (
    <div className="space-y-4 md:space-y-6">
      {/* 현재 포트폴리오 */}
      <div className="bg-white rounded-lg shadow p-4 md:p-6">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3 mb-4">
          <h2 className="text-xl md:text-2xl font-bold">내 포트폴리오</h2>
          <button
            onClick={generateRebalancingPlan}
            className="flex items-center justify-center gap-2 px-3 py-2 md:px-4 md:py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm md:text-base"
          >
            <RefreshCw className="w-4 h-4 md:w-5 md:h-5" />
            리밸런싱 분석
          </button>
        </div>
        
        <div className="mb-4">
          <p className="text-sm md:text-base text-gray-600">총 평가금액</p>
          <p className="text-2xl md:text-3xl font-bold">₩{portfolio?.total_value?.toLocaleString()}</p>
        </div>
        
        {/* 모바일 테이블 스크롤 */}
        <div className="overflow-x-auto -mx-4 px-4 md:mx-0 md:px-0">
          <table className="w-full min-w-[600px]">
            <thead className="border-b">
              <tr>
                <th className="text-left py-2 text-sm md:text-base">종목명</th>
                <th className="text-left py-2 text-sm md:text-base">섹터</th>
                <th className="text-right py-2 text-sm md:text-base">보유수량</th>
                <th className="text-right py-2 text-sm md:text-base">평가금액</th>
                <th className="text-right py-2 text-sm md:text-base">비중</th>
                <th className="text-right py-2 text-sm md:text-base">수익률</th>
              </tr>
            </thead>
            <tbody>
              {portfolio?.portfolio?.map((stock: any) => {
                const returnRate = ((stock.current_price - stock.avg_price) / stock.avg_price * 100).toFixed(2);
                const weight = (stock.value / portfolio.total_value * 100).toFixed(1);
                
                return (
                  <tr key={stock.stock_code} className="border-b">
                    <td className="py-3">
                      <div>
                        <p className="font-medium text-sm md:text-base">{stock.stock_name}</p>
                        <p className="text-xs md:text-sm text-gray-500">{stock.stock_code}</p>
                      </div>
                    </td>
                    <td className="py-3 text-sm md:text-base">{stock.sector}</td>
                    <td className="py-3 text-right text-sm md:text-base">{stock.shares}주</td>
                    <td className="py-3 text-right text-sm md:text-base">₩{stock.value.toLocaleString()}</td>
                    <td className="py-3 text-right text-sm md:text-base">{weight}%</td>
                    <td className={`py-3 text-right font-medium text-sm md:text-base ${
                      Number(returnRate) >= 0 ? 'text-green-600' : 'text-red-600'
                    }`}>
                      {Number(returnRate) >= 0 ? '+' : ''}{returnRate}%
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
      
      {/* 리밸런싱 제안 */}
      {rebalancingPlan && (
        <div className="bg-white rounded-lg shadow p-4 md:p-6">
          <div className="flex items-center gap-2 mb-4">
            <AlertTriangle className="w-5 h-5 md:w-6 md:h-6 text-yellow-500" />
            <h3 className="text-lg md:text-xl font-bold">리밸런싱 제안</h3>
          </div>
          
          <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3 md:p-4 mb-4">
            <p className="text-xs md:text-sm text-yellow-800">
              IT 섹터 집중도가 65%로 과도합니다. 분산 투자를 통해 리스크를 줄이세요.
            </p>
          </div>
          
          <div className="space-y-3 md:space-y-4">
            <h4 className="font-semibold text-sm md:text-base">추천 거래</h4>
            {rebalancingPlan.required_trades?.map((trade: any, index: number) => (
              <div key={index} className={`flex flex-col sm:flex-row sm:items-center sm:justify-between p-3 rounded-lg gap-2 ${
                trade.action === 'sell' ? 'bg-red-50' : 'bg-green-50'
              }`}>
                <div className="flex items-start sm:items-center gap-3">
                  <span className={`px-2 py-1 rounded text-xs md:text-sm font-medium ${
                    trade.action === 'sell' ? 'bg-red-200 text-red-800' : 'bg-green-200 text-green-800'
                  }`}>
                    {trade.action === 'sell' ? '매도' : '매수'}
                  </span>
                  <div>
                    <p className="font-medium text-sm md:text-base">{trade.stock_name}</p>
                    <p className="text-xs md:text-sm text-gray-600">{trade.reason}</p>
                  </div>
                </div>
                <div className="text-right ml-auto">
                  <p className="font-medium text-sm md:text-base">₩{trade.trade_value.toLocaleString()}</p>
                  <p className="text-xs md:text-sm text-gray-600">{trade.shares}주</p>
                </div>
              </div>
            ))}
          </div>
          
          <div className="mt-6 pt-4 border-t">
            <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3">
              <div>
                <p className="text-xs md:text-sm text-gray-600">예상 거래 비용</p>
                <p className="font-medium text-sm md:text-base">
                  ₩{((rebalancingPlan.estimated_cost?.commission || 0) + (rebalancing
