from enum import Enum


class ClassificationEnum(str, Enum):
    CONFIDENTIAL = "CONFIDENTIAL"
    SUSPICIOUS = "SUSPICIOUS"
    NORMAL = "NORMAL"
    ERROR = "ERROR"
