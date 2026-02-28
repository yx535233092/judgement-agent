from typing import List
from src.schemas.base import ClassificationEnum


class structor_scene_output:
    scene_key: str
    reason: str
    confidence: float


class structor_positive_output:
    verdict: ClassificationEnum
    confidence: float
    reasoning: str
    evidence: List[str]
