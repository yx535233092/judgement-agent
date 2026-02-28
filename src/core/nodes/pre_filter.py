from src.schemas.base import ClassificationEnum
from src.schemas.business import JudgeResult
from src.schemas.state import AgentState
from src.core.tools.regular_filter import regular_filer


# 前置初筛过滤
def pre_filter(state: AgentState) -> AgentState:
    text = state["input_data"].full_txt

    reg_filter_result = regular_filer(text)

    if reg_filter_result:
        # LangGraph 的节点如果返回一部分，它会自动 merge 到原始状态中
        return {
            "is_filtered": True,
            "positive_analysis": JudgeResult(
                verdict=ClassificationEnum.CONFIDENTIAL,
                confidence=1.0,
                reasoning="文本内出现密级标识",
                evidence=[f"文中密标：{reg_filter_result}"],  # 修正为列表类型
            ),
            "internal_logs": [
                f"检测到密级标识 [{reg_filter_result}]，命中硬过滤规则，跳过AI研判。"
            ],
        }

    return {"is_filtered": False}
