import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 데모 데이터
const demoData = {
  analysis: {
    report_id: "demo-001",
    user_id: "demo_user",
    analysis_date: new Date().toISOString(),
    behavior_analysis: {
      user_id: "demo_user",
      analysis_date: new Date().toISOString(),
      avg_holding_period: 5.9,
      turnover_rate: 45.2,
      win_loss_ratio: 0.82,
      win_rate: 42.3,
      loss_delay_rate: 0.32,
      fomo_purchase_count: 12,
      portfolio_volatility: 18.5,
      sector_concentration: {
        'IT': 0.65,
        '금융': 0.15,
        '화학': 0.10,
        '바이오': 0.05,
        '소비재': 0.05
      },
      total_trades: 156,
      avg_trade_size: 1500000,
      max_drawdown: 23.5,
      cash_ratio: 0.05
    },
    investor_types: ["단타형", "FOMO 취약형"],
    behavior_summary: "평균 보유기간이 5.9일로 너무 짧아요. 단기 매매보다는 기업의 가치를 보고 투자하는 연습을 해보세요. 최소 1주일은 보유하는 것을 목표로 시작해보면 어떨까요? 📈",
    coaching_actions: [
      {
        action_id: "R-001_demo",
        type: "warning",
        priority: "high",
        title: "과도한 회전율 경고",
        description: "회전율이 45%로 너무 높습니다. 잠시 숨을 고르세요.",
        recommendation: {
          cash_ratio: 0.2,
          trading_suspension_days: 3
        },
        expected_impact: {
          turnover_reduction: -30
        }
      },
      {
        action_id: "R-002_demo",
        type: "goal_setting",
        priority: "high",
        title: "단타 패턴 개선",
        description: "평균 보유기간이 5.9일로 너무 짧습니다.",
        recommendation: {
          min_holding_days: 7
        },
        expected_impact: {
          holding_period_increase: 50
        }
      },
      {
        action_id: "R-003_demo",
        type: "habit_correction",
        priority: "medium",
        title: "FOMO 매수 억제",
        description: "급등 후 매수가 12회 발생했습니다.",
        recommendation: {
          cooling_period: 24
        },
        expected_impact: {
          fomo_reduction: -50
        }
      }
    ],
    gamification: {
      level: {
        current: {
          level: 2,
          title: "투자 수련생",
          min_points: 1000
        },
        next: {
          level: 3,
          title: "투자 중급자",
          required_points: 3000
        },
        progress: 25
      },
      points: 1500,
      new_badges: []
    },
    market_comparison: {
      your_metrics: {
        avg_holding_period: 5.9,
        turnover_rate: 45.2,
        win_rate: 42.3
      },
      market_average: {
        avg_holding_period: 5.9,
        monthly_turnover: 45.2,
        win_rate: 42.3
      }
    },
    improvement_goals: {},
    next_review_date: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString()
  },
  portfolio: {
    user_id: "demo_user",
    portfolio: [
      {
        stock_code: 'A005930',
        stock_name: '삼성전자',
        sector: 'IT',
        shares: 50,
        avg_price: 70000,
        current_price: 72000,
        value: 3600000
      },
      {
        stock_code: 'A035720',
        stock_name: '카카오',
        sector: 'IT',
        shares: 60,
        avg_price: 42000,
        current_price: 41000,
        value: 2460000
      },
      {
        stock_code: 'A000660',
        stock_name: 'SK하이닉스',
        sector: 'IT',
        shares: 20,
        avg_price: 130000,
        current_price: 135000,
        value: 2700000
      }
    ],
    total_value: 8760000,
    last_updated: new Date().toISOString()
  }
};

export const api = {
  // 분석 API
  getAnalysis: async (userId: string) => {
    try {
      const response = await apiClient.get(`/analysis/demo/${userId}`);
      return response.data;
    } catch (error) {
      console.log('Using demo data due to API error');
      return demoData.analysis;
    }
  },
  
  // 포트폴리오 API
  getPortfolio: async (userId: string) => {
    try {
      const response = await apiClient.get(`/portfolio/current/${userId}`);
      return response.data;
    } catch (error) {
      console.log('Using demo data due to API error');
      return demoData.portfolio;
    }
  },
  
  createRebalancingPlan: async (userId: string) => {
    try {
      const response = await apiClient.post('/portfolio/rebalance', {
        user_id: userId,
        execute_immediately: false
      });
      return response.data;
    } catch (error) {
      console.log('Using demo data due to API error');
      return {
        plan_id: "demo-plan-001",
        created_at: new Date().toISOString(),
        current_portfolio: {
          'A005930': { name: '삼성전자', sector: 'IT', weight: 0.41, value: 3600000 },
          'A035720': { name: '카카오', sector: 'IT', weight: 0.28, value: 2460000 },
          'A000660': { name: 'SK하이닉스', sector: 'IT', weight: 0.31, value: 2700000 }
        },
        target_portfolio: {
          'A005930': { name: '삼성전자', sector: 'IT', target_weight: 0.15 },
          'A035720': { name: '카카오', sector: 'IT', target_weight: 0.10 },
          'A105560': { name: 'KB금융', sector: '금융', target_weight: 0.15 }
        },
        required_trades: [
          {
            stock_code: 'A000660',
            stock_name: 'SK하이닉스',
            action: 'sell',
            shares: 15,
            trade_value: 2025000,
            reason: 'IT 섹터 과다 집중 해소'
          },
          {
            stock_code: 'A105560',
            stock_name: 'KB금융',
            action: 'buy',
            shares: 200,
            trade_value: 1500000,
            reason: '금융 섹터 비중 확대'
          }
        ],
        expected_results: {
          volatility_reduction: -15,
          sector_balance_improvement: 25
        },
        estimated_cost: {
          commission: 2800,
          tax: 4657
        }
      };
    }
  },
  
  // 게이미피케이션 API
  getGamificationStatus: async (userId: string) => {
    try {
      const response = await apiClient.get(`/gamification/user/${userId}/status`);
      return response.data;
    } catch (error) {
      console.log('Using demo data due to API error');
      return {
        user_id: userId,
        total_points: 1500,
        level: demoData.analysis.gamification.level,
        badges: [
          {
            badge_id: 'first_week',
            name: '첫 주 완주',
            icon: '🎯',
            achieved_at: '2024-01-10T15:30:00'
          }
        ],
        streaks: {
          plan_adherence: 7,
          no_fomo: 14
        }
      };
    }
  },
  
  getLeaderboard: async () => {
    try {
      const response = await apiClient.get('/gamification/leaderboard');
      return response.data;
    } catch (error) {
      console.log('Using demo data due to API error');
      return {
        weekly: [
          { rank: 1, user_name: '투자왕', points: 2500, improvement: '+15%' },
          { rank: 2, user_name: '현명한투자자', points: 2300, improvement: '+12%' },
          { rank: 3, user_name: '장기투자자', points: 2100, improvement: '+10%' }
        ]
      };
    }
  }
};
