import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Home, BarChart3, Briefcase, Trophy, Menu, X } from 'lucide-react';

const Navigation: React.FC = () => {
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  
  const navItems = [
    { path: '/', label: '대시보드', icon: Home },
    { path: '/analysis', label: '상세분석', icon: BarChart3 },
    { path: '/portfolio', label: '포트폴리오', icon: Briefcase },
  ];
  
  return (
    <>
      {/* 상단 네비게이션 */}
      <nav className="bg-white shadow-sm sticky top-0 z-40">
        <div className="container mx-auto">
          <div className="flex items-center justify-between h-14 sm:h-16">
            <Link to="/" className="flex items-center gap-2">
              <Trophy className="w-6 h-6 sm:w-8 sm:h-8 text-blue-600" />
              <span className="text-base sm:text-xl font-bold">AI 투자주치의</span>
            </Link>
            
            {/* Desktop Navigation */}
            <div className="hidden md:flex gap-2 lg:gap-6">
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
                        : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                    }`}
                  >
                    <Icon className="w-5 h-5" />
                    <span className="font-medium">{item.label}</span>
                  </Link>
                );
              })}
            </div>
            
            {/* Mobile Menu Button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 -mr-2 rounded-lg hover:bg-gray-100 active:bg-gray-200"
              aria-label="메뉴"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
          
          {/* Mobile Navigation Dropdown */}
          {mobileMenuOpen && (
            <div className="md:hidden py-2 border-t">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = location.pathname === item.path;
                
                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    onClick={() => setMobileMenuOpen(false)}
                    className={`flex items-center gap-3 px-4 py-3 rounded-md transition-colors ${
                      isActive
                        ? 'text-blue-600 bg-blue-50'
                        : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                    }`}
                  >
                    <Icon className="w-5 h-5" />
                    <span className="font-medium">{item.label}</span>
                  </Link>
                );
              })}
            </div>
          )}
        </div>
      </nav>
      
      {/* 모바일 하단 네비게이션 (옵션) */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-white border-t z-40 safe-padding-bottom">
        <div className="flex items-center justify-around h-14">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`flex flex-col items-center justify-center flex-1 h-full gap-1 ${
                  isActive ? 'text-blue-600' : 'text-gray-500'
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="text-xs">{item.label}</span>
              </Link>
            );
          })}
        </div>
      </nav>
    </>
  );
};

export default Navigation;
