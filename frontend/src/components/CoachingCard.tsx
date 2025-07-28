import React from 'react';
import { AlertCircle, Target, TrendingUp, Shield } from 'lucide-react';

interface CoachingCardProps {
  action: {
    title: string;
    description: string;
    priority: string;
    type: string;
    expected_impact: any;
  };
}

const CoachingCard: React.FC<CoachingCardProps> = ({ action }) => {
  const getIcon = () => {
    switch (action.type) {
      case 'warning':
        return <AlertCircle className="w-5 h-5" />;
      case 'goal_setting':
        return <Target className="w-5 h-5" />;
      case 'rebalancing':
        return <TrendingUp className="w-5 h-5" />;
      default:
        return <Shield className="w-5 h-5" />;
    }
  };
  
  const getPriorityColor = () => {
    switch (action.priority) {
      case 'high':
        return 'border-red-200 bg-red-50';
      case 'medium':
        return 'border-yellow-200 bg-yellow-50';
      case 'low':
        return 'border-green-200 bg-green-50';
      default:
        return 'border-gray-200 bg-gray-50';
    }
  };
  
  return (
    <div className={`rounded-lg border p-4 ${getPriorityColor()}`}>
      <div className="flex items-start gap-3">
        <div className="mt-1">{getIcon()}</div>
        <div className="flex-1">
          <h4 className="font-semibold text-gray-900">{action.title}</h4>
          <p className="text-sm text-gray-600 mt-1">{action.description}</p>
          {action.expected_impact && (
            <div className="mt-2 flex items-center gap-2">
              <span className="text-xs bg-white px-2 py-1 rounded">
                예상 개선: {Object.values(action.expected_impact)[0]}%
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default CoachingCard;
