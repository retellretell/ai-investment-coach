import aiohttp
import json
from typing import Dict, List
from ..config import Config
from ..models.behavior import InvestmentBehavior, InvestorType

class HyperClovaXClient:
    """HyperCLOVA X API 클라이언트 (데모용)"""
    
    def __init__(self):
        self.api_key = Config.HYPERCLOVAX_API_KEY
        self.prompt_templates = self._load_prompt_templates()
    
    def _load_prompt_templates(self) -> Dict[str, str]:
        return {
            'behavior_summary': """
당신은 친근한 투자 코치입니다. 다음 투자자의 행동을 분석하여 따뜻하고 동기부여가 되는 조언을 해주세요.

투자자 데이터:
- 평균 보유기간: {avg_holding}일
- 월 회전율: {turnover}%
- 승률: {win_rate}%
- 투자 성향: {investor_types}

2-3문장으로 핵심 문제와 개선 방향을 제시해주세요.
""",
            'coaching_message': """
상황: {situation}
권장 조치: {recommendation}

구체적이고 실천 가능한 조언을 150자 이내로 작성해주세요.
"""
        }
    
    async def generate_behavior_summary(self, behavior: InvestmentBehavior, 
                                      investor_types: List[InvestorType]) -> str:
        """행동 패턴 요약 생성"""
        # 데모용 응답 (실제로는 API 호출)
        if behavior.avg_holding_period < 7:
            return f"""
평균 보유기간이 {behavior.avg_holding_period:.1f}일로 너무 짧아요. 
단기 매매보다는 기업의 가치를 보고 투자하는 연습을 해보세요. 
최소 1주일은 보유하는 것을 목표로 시작해보면 어떨까요? 📈
"""
        elif behavior.fomo_purchase_count > 10:
            return f"""
급등주를 쫓아가는 패턴이 자주 보이네요. 
FOMO(Fear Of Missing Out)는 투자의 적입니다. 
차분하게 본인만의 기준을 세우고 투자해보세요! 💪
"""
        else:
            return f"""
전반적으로 균형잡힌 투자를 하고 계시네요! 
조금 더 안정적인 수익을 위해 포트폴리오 다각화를 고려해보세요. 
꾸준함이 최고의 투자 전략입니다. 👍
"""
    
    async def generate_coaching_message(self, action: Dict) -> str:
        """개인화된 코칭 메시지 생성"""
        # 데모용 응답
        if action['action_type'] == 'warning':
            return "지금은 잠시 숨을 고르는 시간이 필요해요. 감정적 매매는 수익의 적입니다! 🛑"
        elif action['action_type'] == 'goal_setting':
            return "작은 목표부터 시작해볼까요? 이번 주는 최소 3일 이상 보유를 목표로! 🎯"
        else:
            return "함께 더 나은 투자 습관을 만들어가요. 당신의 성장을 응원합니다! 🌟"
