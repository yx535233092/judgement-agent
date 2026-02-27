from pydantic import BaseModel, Field
from typing import List
from enum import Enum


# 分类标签ENUM
class ClassificationEnum(str, Enum):
    CONFIDENTIAL = "CONFIDENTIAL"  # 涉密
    SUSPICIOUS = "SUSPICIOUS"  # 疑似涉密
    NORMAL = "NORMAL"  # 非涉密


# 状态ENUM
class StatusEnum(str, Enum):
    PROGRESS = "PROGRESS"
    SUCCESS = "SUCCESS"
    FAILTURE = "FAILTURE"


# 输入Schema
class InputSchema(BaseModel):
    file_name: str = Field(description="文件名")
    summary: str = Field(description="摘要")
    full_txt: str = Field(description="全文")
    organization: str = Field(description="组织")
    ip: str = Field(description="ip地址")
    response_person: str = Field(description="责任人")
    hit_keywords: str = Field(description="命中关键词")


# 输出Schema
class OutputSchema(BaseModel):
    trace_id: int = Field(default=0, description="用于追踪的唯一id")
    classification: ClassificationEnum = Field(default=ClassificationEnum.NORMAL, description="分类标签")
    status: StatusEnum = Field(default=StatusEnum.PROGRESS, description="状态")
    confidence: float = Field(default=0.0, description="置信度")
    reasoning: str = Field(default="", description="研判理由")
    evidence: List[str] = Field(default_factory=list, description="证据片段")
    policy_reference: str = Field(default="", description="定密依据")


# LangGraph State
class State(BaseModel):
    input: InputSchema
    output: OutputSchema = Field(default_factory=OutputSchema)
