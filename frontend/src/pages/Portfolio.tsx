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
    <div className="space-y-6">
      {/* 현재 포트폴리오 */}
      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-bold">내 포트폴리오</h2>
          <button
            onClick={generateRebalancingPlan}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            <RefreshCw className="w-5 h-5" />
            리밸런싱 분석
          </button>
        </div>
        
        <div className="mb-4">
          <p className="text-gray-600">총 평가금액</p>
          <p className="text-3xl font-bold">₩{portfolio?.total_value?.toLocaleString()}</p>
        </div>
        
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="border-b">
              <tr>
                <th className="text-left py-2">종목명</th>
                <th className="text-left py-2">섹터</th>
                <th className="text-right py-2">보유수량</th>
                <th className="text-right py-2">평가금액</th>
                <th className="text-right py-2">비중</th>
                <th className="text-right py-2">수익률</th>
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
                        <p className="font-medium">{stock.stock_name}</p>
                        <p className="text-sm text-gray-500">{stock.stock_code}</p>
                      </div>
                    </td>
                    <td className="py-3">{stock.sector}</td>
                    <td className="py-3 text-right">{stock.shares}주</td>
                    <td className="py-3 text-right">₩{stock.value.toLocaleString()}</td>
                    <td className="py-3 text-right">{weight}%</td>
                    <td className={`py-3 text-right font-medium ${
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
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center gap-2 mb-4">
            <AlertTriangle className="w-6 h-6 text-yellow-500" />
            <h3 className="text-xl font-bold">리밸런싱 제안</h3>
          </div>
          
          <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-4">
            <p className="text-sm text-yellow-800">
              IT 섹터 집중도가 65%로 과도합니다. 분산 투자를 통해 리스크를 줄이세요.
            </p>
          </div>
          
          <div className="space-y-4">
            <h4 className="font-semibold">추천 거래</h4>
            {rebalancingPlan.required_trades?.map((trade: any, index: number) => (
              <div key={index} className={`flex items-center justify-between p-3 rounded-lg ${
                trade.action === 'sell' ? 'bg-red-50' : 'bg-green-50'
              }`}>
                <div className="flex items-center gap-3">
                  <span className={`px-2 py-1 rounded text-sm font-medium ${
                    trade.action === 'sell' ? 'bg-red-200 text-red-800' : 'bg-green-200 text-green-800'
                  }`}>
                    {trade.action === 'sell' ? '매도' : '매수'}
                  </span>
                  <div>
                    <p className="font-medium">{trade.stock_name}</p>
                    <p className="text-sm text-gray-600">{trade.reason}</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="font-medium">₩{trade.trade_value.toLocaleString()}</p>
                  <p className="text-sm text-gray-600">{trade.shares}주</p>
                </div>
              </div>
            ))}
          </div>
          
          <div className="mt-6 pt-4 border-t">
            <div className="flex justify-between items-center">
              <div>
                <p className="text-sm text-gray-600">예상 거래 비용</p>
                <p className="font-medium">
                  ₩{(rebalancingPlan.estimated_cost?.commission + rebalancingPlan.estimated_cost?.tax).toLocaleString()}
                </p>
              </div>
              <button className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
                M-STOCK에서 실행
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Portfolio;
