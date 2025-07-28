import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const api = {
  // 분석 API
  getAnalysis: async (userId: string) => {
    const response = await apiClient.get(`/analysis/demo/${userId}`);
    return response.data;
  },
  
  // 포트폴리오 API
  getPortfolio: async (userId: string) => {
    const response = await apiClient.get(`/portfolio/current/${userId}`);
    return response.data;
  },
  
  createRebalancingPlan: async (userId: string) => {
    const response = await apiClient.post('/portfolio/rebalance', {
      user_id: userId,
      execute_immediately: false
    });
    return response.data;
  },
  
  // 게이미피케이션 API
  getGamificationStatus: async (userId: string) => {
    const response = await apiClient.get(`/gamification/user/${userId}/status`);
    return response.data;
  },
  
  getLeaderboard: async () => {
    const response = await apiClient.get('/gamification/leaderboard');
    return response.data;
  }
};
