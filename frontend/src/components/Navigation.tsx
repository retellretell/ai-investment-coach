import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Home, BarChart3, Briefcase, Trophy } from 'lucide-react';

const Navigation: React.FC = () => {
  const location = useLocation();
  
  const navItems = [
    { path: '/', label: '대시보드', icon: Home },
    { path: '/analysis', label: '상세분석', icon: BarChart3 },
    { path: '/portfolio', label: '포트폴리오', icon: Briefcase },
  ];
  
  return (
    <nav className="bg-white shadow-sm">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center gap-2">
            <Trophy className="w-8 h-8 text-blue-600" />
            <span className="text-xl font-bold">AI 투자주치의</span>
          </div>
          
          <div className="flex gap-6">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  className={`flex items-center gap-2 px-3 py-2 rounded-md transition-colors ${
                    isActive
                      ? 'text-blue-600 bg-blue-50'
                      : 'text-gray-600 hover:text-gray-900'
                  }`}
                >
                  <Icon className="w-5 h-5" />
                  <span>{item.label}</span>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
