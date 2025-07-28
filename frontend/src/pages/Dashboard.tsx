import React, { useState, useEffect } from 'react';
import { TrendingUp, AlertCircle, Target, Trophy } from 'lucide-react';
import BehaviorChart from '../components/BehaviorChart';
import CoachingCard from '../components/CoachingCard';
import { api } from '../services/api';

const Dashboard: React.FC = () => {
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
  
  return (
    <div className="space-y-4 md:space-y-6">
      <div className="bg-white rounded-lg shadow p-4 md:p-6">
        <h1 className="text-2xl md:text-3xl font-bold mb-2">AI 투자주치의</h1>
        <p className="text-sm md:text-base text-gray-600">투자, 공부보다 습관이 더 중요합니다</p>
      </div>
      
      {/* 주요 지표 카드 - 모바일에서 2x2 그리드 */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4">
        <MetricCard
          icon={<TrendingUp className="w-5 h-5 md:w-6 md:h-6" />}
          title="평균 보유기간"
          value={`${analysis?.behavior_analysis?.avg_holding_period?.toFixed(1)}일`}
          target="목표: 7일 이상"
          status={analysis?.behavior_analysis?.avg_holding_period >= 7 ? 'good' : 'bad'}
        />
        <MetricCard
          icon={<AlertCircle className="w-5 h-5 md:w-6 md:h-6" />}
          title="월 회전율"
          value={`${analysis?.behavior_analysis?.turnover_rate?.toFixed(0)}%`}
          target="목표: 30% 이하"
          status={analysis?.behavior_analysis?.turnover_rate <= 30 ? 'good' : 'bad'}
        />
        <MetricCard
          icon={<Target className="w-5 h-5 md:w-6 md:h-6" />}
          title="승률"
          value={`${analysis?.behavior_analysis?.win_rate?.toFixed(1)}%`}
          target="목표: 60% 이상"
          status={analysis?.behavior_analysis?.win_rate >= 60 ? 'good' : 'bad'}
        />
        <MetricCard
          icon={<Trophy className="w-5 h-5 md:w-6 md:h-6" />}
          title="레벨"
          value={analysis?.gamification?.level?.current?.title || '투자 입문자'}
          target={`${analysis?.gamification?.points || 0}P`}
          status="neutral"
        />
      </div>
      
      {/* AI 코칭 메시지 */}
      <div className="bg-blue-50 border-l-4 border-blue-500 p-3 md:p-4 rounded">
        <p className="text-base md:text-lg font-medium text-blue-900 mb-1 md:mb-2">오늘의 AI 코칭</p>
        <p className="text-sm md:text-base text-blue-800">{analysis?.behavior_summary}</p>
      </div>
      
      {/* 행동 분석 차트 - 모바일에서 세로 배치 */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 md:gap-6">
        <div className="order-2 lg:order-1">
          <BehaviorChart data={analysis?.behavior_analysis} />
        </div>
        <div className="order-1 lg:order-2 space-y-3 md:space-y-4">
          <h3 className="text-lg md:text-xl font-bold">추천 행동</h3>
          {analysis?.coaching_actions?.map((action: any, index: number) => (
            <CoachingCard key={index} action={action} />
          ))}
        </div>
      </div>
    </div>
  );
};

interface MetricCardProps {
  icon: React.ReactNode;
  title: string;
  value: string;
  target: string;
  status: 'good' | 'bad' | 'neutral';
}

const MetricCard: React.FC<MetricCardProps> = ({ icon, title, value, target, status }) => {
  const statusColors = {
    good: 'text-green-600 bg-green-50',
    bad: 'text-red-600 bg-red-50',
    neutral: 'text-gray-600 bg-gray-50'
  };
  
  return (
    <div className={`rounded-lg p-3 md:p-4 ${statusColors[status]}`}>
      <div className="flex items-center justify-between mb-1 md:mb-2">
        {icon}
        <span className="text-lg md:text-2xl font-bold">{value}</span>
      </div>
      <p className="text-xs md:text-sm font-medium">{title}</p>
      <p className="text-xs opacity-75">{target}</p>
    </div>
  );
};

export default Dashboard;
