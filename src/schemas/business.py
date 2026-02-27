from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from schemas.base import ClassificationEnum


class ScanInput:
    trace_id: str = Field(..., description="全局唯一的任务追踪id")
    file_name: str = Field(..., description="待扫描文件名")
    full_txt: str = Field(..., description="完整文本内容")
    organization: str = Field("", description="所属组织")
    response_person: str = Field(..., description="负责人")
    hit_keywords: str = Field(..., description="命中关键词")


class ScanOutput:
    trace_id: str
    classification: ClassificationEnum = Field(..., description="最终密级状态")
    confidence: float = Field(..., "综合正反研判后的最终置信度")
    reasoning: str = Field(..., description="综合多方意见后的裁决理由")
    evidence: List[str] = Field(..., description="汇总后的关键证据列表")
    policy_reference: Optional[str] = Field(None, description="匹配到的定密政策")

    metadata: Dict[str, Any] = Field(
        default_factory=lambda: {
            "model_version": "v1.0",
            "process_time_ms": 0,
            "token_usage": {},
        },
        description="存放模型版本、耗时、Token 消耗等审计信息",
    )


class JudgeResult(BaseModel):
    verdict: ClassificationEnum = Field(..., description="研判结论")
    confidence: float = Field(..., ge=0, le=1, description="置信度，范围 0.0 到 1.0")
    reasoning: str = Field(..., description="详细的研判理由和逻辑分析")
    evidence: List[str] = Field(
        default_factory=list, description="从原文中抽取的支撑证据片段"
    )
