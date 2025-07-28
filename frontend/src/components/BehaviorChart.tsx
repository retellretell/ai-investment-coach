import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

interface BehaviorChartProps {
  data: any;
}

const BehaviorChart: React.FC<BehaviorChartProps> = ({ data }) => {
  // 데모용 차트 데이터
  const chartData = [
    { month: '10월', 보유기간: 3.2, 회전율: 52, 승률: 38 },
    { month: '11월', 보유기간: 4.5, 회전율: 48, 승률: 42 },
    { month: '12월', 보유기간: 5.1, 회전율: 45, 승률: 45 },
    { month: '1월', 보유기간: 5.9, 회전율: 42, 승률: 48 }
  ];
  
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="text-xl font-bold mb-4">투자 행동 추이</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="보유기간" stroke="#3B82F6" strokeWidth={2} />
          <Line type="monotone" dataKey="회전율" stroke="#EF4444" strokeWidth={2} />
          <Line type="monotone" dataKey="승률" stroke="#10B981" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default BehaviorChart;
