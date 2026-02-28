from typing import Annotated, List, Optional
from typing_extensions import TypedDict
import operator
from .business import ScanInput, JudgeResult, ScanOutput


class AgentState(TypedDict):
    input_data: ScanInput

    is_filtered: bool

    scene: Optional[str]

    active_policies: Optional[List[str]]

    positive_analysis: Optional[JudgeResult]
    negative_analysis: Optional[JudgeResult]

    finnal_result: Optional[ScanOutput]

    internal_logs: Annotated[List[str], operator.add]

    error_info: Optional[str]
