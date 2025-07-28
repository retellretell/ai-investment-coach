import React, { useState, useEffect } from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Legend, Tooltip } from 'recharts';
import { ArrowUp, ArrowDown, Minus } from 'lucide-react';
import { api } from '../services/api';

const Analysis: React.FC = () => {
  const [analysis, setAnalysis] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchAnalysis();
  }, []);
  
  const fetchAnalysis = async () => {
    try {
      const result = await api.getAnalysis('demo_user');
      setAnalysis(result);
    } catch (error) {
      console.error('Failed to fetch analysis:', error);
    } finally {
      setLoading(false);
    }
  };
  
  if (loading) {
    return <div className="flex justify-center items-center h-64">로딩 중...</div>;
  }
  
  // 섹터 집중도 차트 데이터
  const sectorData = Object.entries(analysis?.behavior_analysis?.sector_concentration || {})
    .map(([name, value]) => ({ name, value: (value as number) * 100 }));
  
  const COLORS = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'];
  
  return (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-2xl font-bold mb-4">상세 행동 분석</h2>
        
        {/* 투자자 유형 */}
        <div className="mb-6">
          <h3 className="text-lg font-semibold mb-2">투자자 유형</h3>
          <div className="flex flex-wrap gap-2">
            {analysis?.investor_types?.map((type: string) => (
              <span key={type} className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm">
                {type}
              </span>
            ))}
          </div>
        </div>
        
        {/* 상세 지표 */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-semibold mb-3">행동 지표</h3>
            <div className="space-y-3">
              <MetricRow
                label="평균 보유기간"
                value={`${analysis?.behavior_analysis?.avg_holding_period?.toFixed(1)}일`}
                target={7}
                current={analysis?.behavior_analysis?.avg_holding_period}
              />
              <MetricRow
                label="월 회전율"
                value={`${analysis?.behavior_analysis?.turnover_rate?.toFixed(0)}%`}
                target={30}
                current={analysis?.behavior_analysis?.turnover_rate}
                inverse
              />
              <MetricRow
                label="승률"
                value={`${analysis?.behavior_analysis?.win_rate?.toFixed(1)}%`}
                target={60}
                current={analysis?.behavior_analysis?.win_rate}
              />
              <MetricRow
                label="손익비"
                value={`${analysis?.behavior_analysis?.win_loss_ratio?.toFixed(2)}`}
                target={1.5}
                current={analysis?.behavior_analysis?.win_loss_ratio}
              />
            </div>
          </div>
          
          <div>
            <h3 className="text-lg font-semibold mb-3">리스크 지표</h3>
            <div className="space-y-3">
              <MetricRow
                label="포트폴리오 변동성"
                value={`${analysis?.behavior_analysis?.portfolio_volatility?.toFixed(1)}%`}
                target={12}
                current={analysis?.behavior_analysis?.portfolio_volatility}
                inverse
              />
              <MetricRow
                label="최대 손실폭 (MDD)"
                value={`${analysis?.behavior_analysis?.max_drawdown?.toFixed(1)}%`}
                target={15}
                current={analysis?.behavior_analysis?.max_drawdown}
                inverse
              />
              <MetricRow
                label="현금 비중"
                value={`${(analysis?.behavior_analysis?.cash_ratio * 100)?.toFixed(0)}%`}
                target={10}
                current={analysis?.behavior_analysis?.cash_ratio * 100}
              />
              <MetricRow
                label="FOMO 매수 횟수"
                value={`${analysis?.behavior_analysis?.fomo_purchase_count}회/월`}
                target={5}
                current={analysis?.behavior_analysis?.fomo_purchase_count}
                inverse
              />
            </div>
          </div>
        </div>
      </div>
      
      {/* 섹터 집중도 */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-xl font-bold mb-4">섹터별 투자 비중</h3>
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie
                data={sectorData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name} ${percent.toFixed(0)}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {sectorData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
      
      {/* 시장 평균 비교 */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-xl font-bold mb-4">시장 평균과 비교</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <ComparisonCard
            label="평균 보유기간"
            myValue={analysis?.behavior_analysis?.avg_holding_period}
            marketValue={5.9}
            unit="일"
          />
          <ComparisonCard
            label="월 회전율"
            myValue={analysis?.behavior_analysis?.turnover_rate}
            marketValue={45.2}
            unit="%"
            inverse
          />
          <ComparisonCard
            label="승률"
            myValue={analysis?.behavior_analysis?.win_rate}
            marketValue={42.3}
            unit="%"
          />
        </div>
      </div>
    </div>
  );
};

interface MetricRowProps {
  label: string;
  value: string;
  target: number;
  current: number;
  inverse?: boolean;
}

const MetricRow: React.FC<MetricRowProps> = ({ label, value, target, current, inverse }) => {
  const isGood = inverse ? current <= target : current >= target;
  const diff = inverse ? target - current : current - target;
  
  return (
    <div className="flex items-center justify-between py-2 border-b">
      <span className="text-gray-600">{label}</span>
      <div className="flex items-center gap-3">
        <span className="font-semibold">{value}</span>
        {isGood ? (
          <ArrowUp className="w-4 h-4 text-green-600" />
        ) : (
          <ArrowDown className="w-4 h-4 text-red-600" />
        )}
      </div>
    </div>
  );
};

interface ComparisonCardProps {
  label: string;
  myValue: number;
  marketValue: number;
  unit: string;
  inverse?: boolean;
}

const ComparisonCard: React.FC<ComparisonCardProps> = ({ label, myValue, marketValue, unit, inverse }) => {
  const diff = ((myValue - marketValue) / marketValue * 100).toFixed(1);
  const isGood = inverse ? myValue < marketValue : myValue > marketValue;
  
  return (
    <div className="bg-gray-50 rounded-lg p-4">
      <p className="text-sm text-gray-600 mb-2">{label}</p>
      <div className="flex items-baseline gap-2">
        <span className="text-2xl font-bold">{myValue?.toFixed(1)}{unit}</span>
        <span className="text-sm text-gray-500">vs {marketValue}{unit}</span>
      </div>
      <div className={`mt-2 text-sm font-medium ${isGood ? 'text-green-600' : 'text-red-600'}`}>
        {Number(diff) > 0 ? '+' : ''}{diff}%
      </div>
    </div>
  );
};

export default Analysis;
