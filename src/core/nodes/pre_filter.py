from src.schemas.models import State
from src.core.tools.regular_filter import regular_filer


# 前置初筛过滤
def pre_filter(state: State) -> State:
    reg_filter_result = regular_filer(state.input.summary)
    if reg_filter_result:
        state.output.classification = "CONFIDENTIAL"
        state.output.reasoning = "符合密标评定标准，判定为涉密文件"
    return state
